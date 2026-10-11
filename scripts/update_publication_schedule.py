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
MISSING = set(TIMES) - set(CATALOG)
if MISSING:
    raise SystemExit("Scheduled articles missing from reports.json: " + ", ".join(sorted(MISSING)))
now = datetime.now(timezone.utc)
madrid = ZoneInfo("Europe/Madrid")
new_york = ZoneInfo("America/New_York")

def escape(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")

def row(item):
    instant, url, report = item
    es, us = instant.astimezone(madrid), instant.astimezone(new_york)
    return (
        f"| {es.strftime('%a, %d %b %Y')} | {es.strftime('%H:%M')} "
        f"| {us.strftime('%I:%M %p')} ET | {escape(report['universe'])} "
        f"| [{escape(report['title'])}]({url}) |"
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
def table(items):
    return header + "\n" + ("\n".join(map(row, items)) if items else "| — | — | — | No scheduled studies | — |")
content = f"""# Structural Alpha Research — Publication Schedule

This schedule is **generated automatically** from the `publicationTimes` block in [`index.html`](index.html) and the study metadata in [`reports.json`](reports.json). Do not edit the tables manually.

Times are shown in **Madrid** and **New York (ET)**, with daylight-saving changes applied for each release date.

## Upcoming releases

{table(upcoming)}

## Earlier scheduled releases

{table(released)}

## How scheduling works

- **Source of truth:** [`index.html`](index.html) → `publicationTimes`; titles and links come from [`reports.json`](reports.json).
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
