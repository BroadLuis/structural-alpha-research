#!/usr/bin/env python3
"""Synchronize read-only Hits.sh counts for published studies.

The hits.sh /api/urns/{urn} endpoint returns the existing total
WITHOUT incrementing it. Never request the .svg counter from this script.
"""
import json
import pathlib
import urllib.error
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = "broadluis.github.io/structural-alpha-research/"
REPORTS = ROOT / "reports.json"
OUTPUT = ROOT / "views.json"


def main():
    reports = json.loads(REPORTS.read_text(encoding="utf-8"))
    previous = {}
    if OUTPUT.exists():
        try:
            previous = json.loads(OUTPUT.read_text(encoding="utf-8")).get("counts", {})
        except (ValueError, OSError):
            pass

    counts = dict(previous)
    updated = []
    for report in reports:
        path = report.get("url")
        if not path or not path.startswith("studies/"):
            continue
        urn = BASE + path
        url = "https://hits.sh/api/urns/" + urn
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "StructuralAlpha-ReadOnlyViews/1.0", "Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=15) as response:
                payload = json.load(response)
            value = payload.get("total")
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError("Unexpected count in API response")
            counts[path] = value
            updated.append(path)
            print(f"{path}: {value} page views")
        except (urllib.error.URLError, ValueError, TimeoutError, json.JSONDecodeError) as exc:
            print(f"Could not read {path}: {exc}; retaining earlier value if available")

    valid_paths = {r.get("url") for r in reports}
    counts = {key: val for key, val in counts.items() if key in valid_paths}
    if not updated:
        print("No valid responses: preserving existing counts.")
        return

    document = {"updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "counts": counts}
    OUTPUT.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
