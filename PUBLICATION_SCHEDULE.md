# Structural Alpha Research — Publication Schedule

This schedule is **generated automatically** from the `publicationTimes` block in [`index.html`](index.html), the study metadata in [`reports.json`](reports.json), and editorial release metadata in [`scripts/update_publication_schedule.py`](scripts/update_publication_schedule.py). Do not edit the tables manually.

Times are shown in **Madrid** and **New York (ET)**, with daylight-saving changes applied for each release date. **Upcoming studies display titles without clickable article links; links appear in the earlier-releases table after publication.**

## Upcoming releases

| Release date | Madrid time | New York time | Study | Article |
|---|---|---|---|---|
| Sun, 25 Oct 2026 | 18:00 | 01:00 PM ET | MARKET PERSPECTIVES | Buy the Bottom or Wait for Confirmation? The Real Cost of Both Strategies |
| Sun, 01 Nov 2026 | 19:00 | 01:00 PM ET | MARKET PERSPECTIVES | Why Gold Miners Can Lag Gold During a Bull Market |

## Earlier scheduled releases

| Release date | Madrid time | New York time | Study | Article |
|---|---|---|---|---|
| Sat, 10 Oct 2026 | 15:25 | 09:25 AM ET | GDX–GDXJ | [GDX–GDXJ: Selling Pressure Eases, but Market Breadth Keeps Deteriorating](studies/2026-10-10-gdx-gdxj/index.html) |
| Sun, 11 Oct 2026 | 10:25 | 04:25 AM ET | JUNIOR | [JUNIOR MINERS: Selling Pressure Eases, but Structural Damage Deepens](studies/2026-10-11-junior/index.html) |
| Sun, 11 Oct 2026 | 15:25 | 09:25 AM ET | ENERGY | [ENERGY &#124; Strong Relative Performance, but Market Breadth Has Yet to Recover](studies/2026-10-11-energy/index.html) |
| Mon, 12 Oct 2026 | 10:30 | 04:30 AM ET | COPPER | [Copper Miners: Breadth Deteriorates Despite Resilient Three-Month Relative Strength](studies/2026-10-12-copper/index.html) |
| Mon, 12 Oct 2026 | 16:30 | 10:30 AM ET | URANIUM | [Uranium Miners: Selling Pressure Eases, but Structural Damage Remains Severe](studies/2026-10-12-uranium/index.html) |
| Tue, 13 Oct 2026 | 15:30 | 09:30 AM ET | AGRIBUSINESS | [AGRIBUSINESS &#124; Selling Pressure Eases, but Market Breadth Suffers a Sharp Four-Week Decline](studies/2026-10-13-agribusiness/index.html) |
| Sat, 17 Oct 2026 | 14:30 | 08:30 AM ET | GLOBAL | [Global Market Structure: Equities Diverge as Mining Breadth Breaks Down](studies/2026-10-18-global/index.html) |
| Sat, 17 Oct 2026 | 20:30 | 02:30 PM ET | JUNIOR | [Junior Gold Miners: Deep Drawdowns and Weak Breadth Across 482 Securities](studies/2026-10-17-junior/index.html) |
| Sun, 18 Oct 2026 | 10:30 | 04:30 AM ET | SIL–SILJ | [Silver Miners SIL–SILJ: Broad Selling Pressure and Deepening Drawdowns](studies/2026-10-18-sil-silj/index.html) |
| Sun, 18 Oct 2026 | 16:30 | 10:30 AM ET | MARKET PERSPECTIVES | [Mining Breadth: What Happens When the Market Starts to Recover?](perspectives/2026-10-18-mining-breadth-recovery/index.html) |
| Sat, 24 Oct 2026 | 18:15 | 12:15 PM ET | MARKET PERSPECTIVES | [The Hidden Cost of Waiting for Confirmation](perspectives/2026-10-20-hidden-cost-confirmation/index.html) |
| Sun, 25 Oct 2026 | 14:30 | 09:30 AM ET | JUNIOR | [Junior Miners: Record-Low Market Breadth Across 482 Securities](studies/2026-10-25-junior/index.html) |

## How scheduling works

- **Source of truth:** [`index.html`](index.html) → `publicationTimes` and [`reports.json`](reports.json) for studies; editorial dates and titles are registered in [`scripts/update_publication_schedule.py`](scripts/update_publication_schedule.py).
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
