# Structural Alpha Research — mandatory ranking format

The ASX study (`studies/2026-10-09-asx/index.html`) is the canonical reference for all company ranking publications.

1. Publish every security in the study's universe, not just a top/bottom subset.
2. Show weekly rank, global rank, ticker, company, last close, and 1W, 4W, 3M, YTD percentage returns when available.
3. Positive returns have green background; negative returns have red/pink background; zero returns are neutral. Display signed percentages consistently.
4. On narrow mobile screens, show each company as a vertically stacked, labeled card with no horizontal scrolling; retain the same values as desktop.
5. Include search and sort, total count, and a working download of the source workbook.
6. Keep workbook, JSON data (when applicable), and HTML references synchronized; test all rows load before announcing completion.
7. Never replace an existing working table with an unverified implementation. Use `assets/structural-alpha-ranking.css` for shared ranking presentation.
8. Before publishing, run `python scripts/validate_research.py`; ensure `reports.json` matches the generated snapshot in `index.html`.
