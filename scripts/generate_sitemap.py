#!/usr/bin/env python3
"""Generate sitemap.xml from published reports and perspectives."""
import json
from datetime import date
from pathlib import Path
from urllib.parse import urljoin
from xml.etree.ElementTree import Element, SubElement, ElementTree, indent

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://structuralalpharesearch.net/'
today = date.today()
paths = ['', 'methodology.html', 'legal.html', 'privacy.html', 'asx/index.html', 'gdx-gdxj/index.html', 'junior/index.html', 'sil-silj/index.html', 'energy/index.html', 'copper/index.html']
reports = json.loads((ROOT / 'reports.json').read_text(encoding='utf-8'))
for report in reports:
    path = str(report.get('url', '')).lstrip('/')
    try:
        published = date.fromisoformat(report['date']) <= today
    except (ValueError, KeyError, TypeError):
        published = False
    if published and path and (ROOT / path).is_file():
        paths.append(path)
for page in sorted((ROOT / 'perspectives').glob('*/index.html')):
    try:
        published = date.fromisoformat(page.parent.name[:10]) <= today
    except ValueError:
        published = False
    if published:
        paths.append(page.relative_to(ROOT).as_posix())
root = Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for path in dict.fromkeys(paths):
    if path and not (ROOT / path).is_file():
        continue
    node = SubElement(root, 'url')
    SubElement(node, 'loc').text = urljoin(BASE, path)
indent(root, space='  ')
ElementTree(root).write(ROOT / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
print(f'Generated {len(root)} URLs')
