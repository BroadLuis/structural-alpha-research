# Structural Alpha / Research Archive

Public archive of independent, data-driven market research.

**Live website:** After GitHub Pages is enabled, the planned URL is:
https://broadluis.github.io/structural-alpha-research/

## Publishing model
- Public research landing page: `index.html`
- Catalog metadata: `reports.json` (empty until reviewed studies are approved)
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
4. Confirm public links work without authentication.

## Enable GitHub Pages
In the repository: **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**.

The website will become accessible after deployment completes. The configured Pages URL should be verified in GitHub.
