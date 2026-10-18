#!/usr/bin/env python3
"""Reassemble the exact Energy ranking into its canonical JSON file."""
import json
from pathlib import Path
folder = Path(__file__).resolve().parents[1] / "studies/2026-10-18-energy/assets"
parts = [json.loads((folder / f"ranking-part-{i}.json").read_text(encoding="utf-8")) for i in (1, 2, 3)]
keys = ("schema_version", "universe", "start_date", "as_of_date", "columns")
assert all(all(p[k] == parts[0][k] for k in keys) for p in parts)
data = {k: v for k, v in parts[0].items() if k != "rows"}
data["rows"] = [r for p in parts for r in p["rows"]]
assert data["universe"] == "ENERGY" and len(data["rows"]) == 169
assert len(data["columns"]) == 9 and all(len(r) == 9 for r in data["rows"])
assert [r[0] for r in data["rows"]] == list(range(1, 170))
(folder / "ranking.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
