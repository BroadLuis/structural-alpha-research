# Structural Alpha / Research Archive

Public archive of independent, data-driven market research.

**Live website:**
https://broadluis.github.io/structural-alpha-research/

## Publishing model
- Public research landing page: `index.html`
- Catalog metadata: `reports.json` (source of truth; the home page contains a synchronized fallback snapshot)
- Each study gets a page and links to the approved PDF, images, spreadsheet and/or complete ZIP.
- Do **not** upload private datasets, internal scripts, API keys, unpublished account information, or proprietary trading signals.

## Adding a study
1. Review and remove private/internal information from the files.
2. Upload public study artifacts to a dedicated folder such as `studies/2026-10-10-gdx-gdxj/` (or GitHub Releases for large ZIPs).
3. Add a JSON entry in `reports.json`:
```json
{
  "title": "Study title",
  "date": "2026-10-10",
  "universe": "GDX–GDXJ",
  "summary": "A concise, evidence-based summary.",
  "url": "studies/2026-10-10-gdx-gdxj/index.html",
  "download": "https://github.com/BroadLuis/structural-alpha-research/releases/download/RELEASE/FILE.zip"
}
```
4. Update the fallback snapshot in `index.html` to match `reports.json` (the validation workflow checks this automatically).
5. Run `python scripts/validate_research.py` and fix any missing local files or invalid metadata.
6. Confirm public links work without authentication.

## Editorial standards
- Use a clear, evidence-led title and a concise summary (ideally 30–65 words).
- Distinguish observation, interpretation, and scenario; never present a hypothesis as confirmed.
- Include observation date, universe size, methodology, relevant breadth/drawdown/volume measures, and limitations.
- Publish supporting charts and a reviewed Excel workbook when appropriate.
- Check for private datasets, proprietary signals, personal information, and broken download paths before publishing.
- Keep the market label exactly consistent with the homepage dropdown (including `ENERGY`).

## Deployment
The site is designed for GitHub Pages on branch `main` at the repository root. After publication, verify the live page and downloads.
