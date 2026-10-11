# Structural Alpha Research — Publication Schedule

A quick reference for scheduled research releases. **The authoritative release times are defined in `index.html` under `publicationTimes`**; this document is a human-readable companion and must be updated whenever that block changes.

## Upcoming releases

| Release date | Madrid time (CEST) | New York time (EDT) | Study | Article |
|---|---|---|---|---|
| Sun, 11 Oct 2026 | 15:25 | 09:25 AM ET | ENERGY | [ENERGY: Strong Relative Performance, but Market Breadth Has Yet to Recover](studies/2026-10-11-energy/index.html) |
| Mon, 12 Oct 2026 | **10:30** | **04:30 AM ET** | COPPER | [Copper Miners: Breadth Deteriorates Despite Resilient Three-Month Relative Strength](studies/2026-10-12-copper/index.html) |
| Mon, 12 Oct 2026 | **16:30** | **10:30 AM ET** | URANIUM | [Uranium Miners: Selling Pressure Eases, but Structural Damage Remains Severe](studies/2026-10-12-uranium/index.html) |

*These are the releases still scheduled as of Sunday, 11 October 2026, before the ENERGY release at 15:25 Madrid time. Times are converted from UTC and reflect daylight-saving time on the listed dates.*

## Earlier scheduled releases

| Release date | Madrid time (CEST) | New York time (EDT) | Study | Article |
|---|---|---|---|---|
| Sat, 10 Oct 2026 | 15:25 | 09:25 AM ET | GDX–GDXJ | [GDX–GDXJ: Selling Pressure Eases, but Market Breadth Keeps Deteriorating](studies/2026-10-10-gdx-gdxj/index.html) |
| Sun, 11 Oct 2026 | 10:25 | 04:25 AM ET | JUNIOR MINERS | [JUNIOR MINERS: Selling Pressure Eases, but Structural Damage Deepens](studies/2026-10-11-junior/index.html) |

## How scheduling works

- **Schedule source:** [`index.html`](index.html), search for `publicationTimes`.
- **Study catalog:** [`reports.json`](reports.json).
- **Deployment status:** [GitHub Actions](https://github.com/BroadLuis/structural-alpha-research/actions).
- **Publication behavior:** the homepage hides future-dated studies from its published research sections and displays them in the Upcoming area until their configured release time. The study's direct URL may already be accessible before then. This is **not a hard embargo**.
- **Important:** editing this Markdown file does **not** schedule a release. To add, change or cancel one, update the entry in `index.html`, keep the catalog and generated homepage snapshot in sync, and update this table.
- **Maintenance:** after a release, move its row from “Upcoming releases” to “Earlier scheduled releases.” This document is not updated automatically.

## New release checklist

1. Prepare the article following [`RANKING_FORMAT.md`](RANKING_FORMAT.md), using the established visual style.
2. Verify the ranking, original Excel download, links, mobile presentation and research narrative.
3. Register the study in `reports.json` and synchronize the generated report snapshot in `index.html`.
4. Add the exact UTC release timestamp to `publicationTimes` and record its Madrid/ET equivalents here.
5. Verify the [GitHub Pages deployment](https://github.com/BroadLuis/structural-alpha-research/actions) and the Upcoming listing.
