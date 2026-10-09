#!/usr/bin/env python3
"""Derive the internal full ranking dataset from the original uploaded SP500 workbook.
No CSV is published, and the Excel remains the only public data download.
"""
import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

root = Path(__file__).resolve().parents[1]
folder = root / "studies" / "2026-10-08-sp500"
workbook = folder / "assets" / "Weekly_Analysis_SP500_20261007.xlsx"
output = folder / "companies.json"

if not workbook.is_file():
    raise SystemExit(f"Upload the original workbook first: {workbook}")

ns = {"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
with ZipFile(workbook) as z:
    strings = []
    if "xl/sharedStrings.xml" in z.namelist():
        tree = ET.fromstring(z.read("xl/sharedStrings.xml"))
        strings = ["".join(t.text or "" for t in x.findall(".//m:t",ns))
                   for x in tree.findall("m:si",ns)]
    book = ET.fromstring(z.read("xl/workbook.xml"))
    relations = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    targets = {x.get("Id"): x.get("Target") for x in relations}
    sheet = next(x for x in book.findall("m:sheets/m:sheet",ns)
                 if x.get("name")=="ALL_COMPANIES")
    target = targets[sheet.get("{"+ns["r"]+"}id")]
    location = target.lstrip("/") if target.startswith("/") else "xl/"+target
    xml = ET.fromstring(z.read(location))
    parsed = []
    for row in xml.findall("m:sheetData/m:row",ns):
        values=[None]*9
        for c in row.findall("m:c",ns):
            match=re.match(r"[A-Z]+",c.get("r",""))
            if not match: continue
            ix=0
            for letter in match.group(): ix=ix*26+ord(letter)-64
            ix-=1
            if ix>=9:continue
            typ=c.get("t")
            v=c.find("m:v",ns)
            if typ=="inlineStr":
                values[ix]="".join(t.text or "" for t in c.findall(".//m:t",ns))
            elif v is not None and v.text is not None:
                value=v.text
                if typ=="s": values[ix]=strings[int(value)]
                elif typ in ("str","e"): values[ix]=value
                else: values[ix]=float(value)
        parsed.append(values)

expected=["rank_weekly","rank_global","ticker","name","last_close","return_week_pct","return_4w_pct","return_3m_pct","return_ytd_pct"]
if len(parsed)!=502 or parsed[1]!=expected:
    raise SystemExit(f"Unexpected workbook structure: {len(parsed)} rows")
data=[]
for row in parsed[2:]:
    if not isinstance(row[2],str) or not isinstance(row[3],str):
        raise SystemExit("Invalid company name or ticker")
    clean=[None if v=="" else v for v in row]
    for ix in (0,1):
        if isinstance(clean[ix],float):clean[ix]=int(clean[ix])
    for ix in (4,5,6,7,8):
        if isinstance(clean[ix],float):clean[ix]=round(clean[ix],5)
    data.append(clean)
if len(data)!=500 or len({r[2] for r in data})!=500 or sorted(r[0] for r in data)!=list(range(1,501)):
    raise SystemExit("Full company dataset validation failed")
assert sum(isinstance(r[1],int) for r in data)==497
output.write_text(json.dumps({"columns":expected,"data":data},ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
print("Generated 500-company internal ranking dataset from uploaded Excel")
