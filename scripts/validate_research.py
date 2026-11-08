#!/usr/bin/env python3
"""Validate the Structural Alpha public catalog and home-page fallback."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((ROOT / "reports.json").read_text(encoding="utf-8"))
html = (ROOT / "index.html").read_text(encoding="utf-8")
match = re.search(r'// BEGIN GENERATED REPORT SNAPSHOT[^\n]*\n\s*let reports=(\[.*?\]);\s*// END GENERATED REPORT SNAPSHOT', html, re.S)
if not match:
    errors.append("Home-page fallback snapshot markers missing.")
else:
    try:
        snapshot = json.loads(match.group(1))
        if snapshot != catalog:
            errors.append("Home-page fallback differs from reports.json.")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid fallback JSON: {exc}")

# The market filter may use a canonical value distinct from the visible label.
# Validate the submitted value when supplied; otherwise use the option text.
options = set()
market_select = re.search(r'<select\b[^>]*\bid=["\']universe["\'][^>]*>(.*?)</select>', html, re.S)
if market_select:
    for attrs, label in re.findall(r'<option([^>]*)>(.*?)</option>', market_select.group(1), re.S):
        value_match = re.search(r'\bvalue=["\']([^"\']*)["\']', attrs)
        value = value_match.group(1) if value_match else label.strip()
        options.add(value.replace('&amp;', '&'))
seen = set()
for i, item in enumerate(catalog, 1):
    for field in ("title", "date", "universe", "summary", "url"):
        if not isinstance(item.get(field), str) or not item[field].strip():
            errors.append(f"Study {i}: missing {field}.")
    if not all(item.get(f) for f in ("title", "date", "universe", "summary", "url")):
        continue
    if item["universe"] not in options:
        errors.append(f"Study {i}: market {item['universe']!r} missing from filter.")
    if len(item["summary"].split()) > 85:
        errors.append(f"Study {i}: summary exceeds 85 words.")
    if item["url"] in seen:
        errors.append(f"Study {i}: duplicate URL {item['url']}.")
    seen.add(item["url"])
    for field in ("url", "download"):
        value = item.get(field)
        if not value:
            continue
        parsed = urlparse(value)
        if parsed.scheme in ("http", "https") and parsed.netloc:
            continue
        if parsed.scheme or parsed.netloc or value.startswith("/") or ".." in Path(unquote(value)).parts:
            errors.append(f"Study {i}: unsafe {field} path: {value}")
            continue
        path = ROOT / unquote(parsed.path)
        if not path.is_file():
            errors.append(f"Study {i}: missing {field} file: {value}")

if errors:
    print("Research catalog validation failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print(f"Validated {len(catalog)} studies, filters, local links and fallback snapshot.")
