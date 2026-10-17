#!/usr/bin/env python3
"""Regenerate PUBLICATION_SCHEDULE.md from the homepage schedule and catalog."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
HOME = (ROOT / "index.html").read_text(encoding="utf-8")
REPORTS = json.loads((ROOT / "reports.json").read_text(encoding="utf-8"))
MATCH = re.search(r"const publicationTimes\s*=\s*(\{[\s\S]*?\})\s*;", HOME)
if not MATCH:
    raise SystemExit("Cannot find publicationTimes in index.html")
TIMES = json.loads(MATCH.group(1))
CATALOG = {item["url"]: item for item in REPORTS}
# Editorial releases remain separate from quantitative reports, but share the calendar.
EDITORIAL_RELEASES = {
    "perspectives/2026-10-18-mining-breadth-recovery/index.html": {
        "title": "Mining Breadth: What Happens When the Market Starts to Recover?",
        "universe": "MARKET PERSPECTIVES",
        "release": "2026-10-18T14:30:00Z",
    },
    "perspectives/2026-10-18-gold-miners-vs-gold/index.html": {
        "title": "Why Gold Miners Can Lag Gold During a Bull Market",
        "universe": "MARKET PERSPECTIVES",
        "release": "2026-10-18T17:00:00Z",
    }
}
for url, item in EDITORIAL_RELEASES.items():
    CATALOG[url] = item
    TIMES[url] = item["release"]
MISSING = set(TIMES) - set(CATALOG)
if MISSING:
    raise SystemExit("Scheduled articles missing from reports.json: " + ", ".join(sorted(MISSING)))
now = datetime.now(timezone.utc)
madrid = ZoneInfo("Europe/Madrid")
new_york = ZoneInfo("America/New_York")

def escape(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")

def row(item, published):
    instant, url, report = item
    es, us = instant.astimezone(madrid), instant.astimezone(new_york)
    article = f"[{escape(report['title'])}]({url})" if published else escape(report["title"])
    return (
        f"| {es.strftime('%a, %d %b %Y')} | {es.strftime('%H:%M')} "
        f"| {us.strftime('%I:%M %p')} ET | {escape(report['universe'])} "
        f"| {article} |"
    )

items = []
for url, value in TIMES.items():
    instant = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if instant.tzinfo is None:
        raise SystemExit("Timestamp must have timezone: " + url)
    items.append((instant, url, CATALOG[url]))
items.sort(key=lambda x: x[0])
upcoming = [item for item in items if item[0] > now]
released = [item for item in items if item[0] <= now]
header = "| Release date | Madrid time | New York time | Study | Article |\n|---|---|---|---|---|"
def table(items, published):
    return header + "\n" + ("\n".join(row(item, published) for item in items) if items else "| — | — | — | No scheduled studies | — |")
content = f"""# Structural Alpha Research — Publication Schedule

This schedule is **generated automatically** from the `publicationTimes` block in [`index.html`](index.html), the study metadata in [`reports.json`](reports.json), and editorial release metadata in [`scripts/update_publication_schedule.py`](scripts/update_publication_schedule.py). Do not edit the tables manually.

Times are shown in **Madrid** and **New York (ET)**, with daylight-saving changes applied for each release date. **Upcoming studies display titles without clickable article links; links appear in the earlier-releases table after publication.**

## Upcoming releases

{table(upcoming, False)}

## Earlier scheduled releases

{table(released, True)}

## How scheduling works

- **Source of truth:** [`index.html`](index.html) → `publicationTimes` and [`reports.json`](reports.json) for studies; editorial dates and titles are registered in [`scripts/update_publication_schedule.py`](scripts/update_publication_schedule.py).
- **Automatic refresh:** [Publication schedule workflow](.github/workflows/update-publication-schedule.yml) checks hourly and commits changes **only when the displayed schedule changes**. GitHub may delay scheduled workflows, so status can lag behind the exact release time.
- **Manual refresh:** open [GitHub Actions](https://github.com/BroadLuis/structural-alpha-research/actions/workflows/update-publication-schedule.yml) and choose **Run workflow**.
- **Homepage behavior:** articles move automatically from Upcoming to published sections at their scheduled time in the visitor's browser, independently of this Markdown file. Direct article URLs may be accessible earlier; this is not a hard embargo.
- **No redundant commits:** the workflow avoids rewriting this file when nothing has changed, limiting unnecessary GitHub Pages deployments.

## New release checklist

1. Prepare the study following [`RANKING_FORMAT.md`](RANKING_FORMAT.md) and verify the complete ranking, downloads and mobile presentation.
2. Register it in [`reports.json`](reports.json) and synchronize the homepage report snapshot.
3. Add the UTC release timestamp to `publicationTimes` in [`index.html`](index.html).
4. Run the [schedule workflow](https://github.com/BroadLuis/structural-alpha-research/actions/workflows/update-publication-schedule.yml) manually if the calendar must reflect the new article immediately; otherwise it updates at the next hourly check.
5. Verify the [GitHub Pages deployment](https://github.com/BroadLuis/structural-alpha-research/actions).
"""
target = ROOT / "PUBLICATION_SCHEDULE.md"
if not target.exists() or target.read_text(encoding="utf-8") != content:
    target.write_text(content, encoding="utf-8")
    print(f"Updated schedule: {len(upcoming)} upcoming, {len(released)} earlier releases")
else:
    print("Schedule already up to date")
