# Denver's Homelessness Response: A Resident's Data Brief

**What $178 million bought, and four ways to spend it better — from public data.**

An independent analysis by a Denver resident (not a researcher, not an advocate) of the city's
homelessness response, built entirely from public sources. Start with the visual brief:

- 📄 [Denver's Homelessness Response: A Resident's Data Brief (PDF)](visuals/Denvers-Homelessness-Response-A-Residents-Data-Brief.pdf) — 4 pages, every number cited
- 🖼️ [Shareable infographics](visuals/) — the $105k waterfall, Denver vs. Houston, the housing funnel

## Three numbers

1. **$105,074 per permanent-housing exit.** All In Mile High spent an auditor-estimated $178.1M to
   move 3,902 people indoors (Jul 2023–Jun 2025); ~1,695 exited to long-term housing. Only 43% of
   entrants ever exited to housing — more than half the headline figure is the arithmetic penalty of
   non-conversion, not the cost of helping someone.
2. **Shelter beds cost $34,000–$36,000/bed/year** (HOST 2026 budget: $93.77–$98.60/night) — about the
   same as verified permanent supportive housing operating costs ($22k–$36k/person/yr, Urban Institute
   evaluation of Denver's own Housing to Health pilot).
3. **Houston holds ~60% of beds as permanent supportive housing + rapid rehousing**; its homelessness
   rate rose 14% in six years. Denver nearly doubled shelter beds and posted the steepest increase of
   six western cities compared (+80%).

## What's here

| Path | Contents |
|---|---|
| `visuals/` | 4-page PDF brief, 3 infographic PNGs, 2-minute hearing remarks |
| `docs/pilot-findings.md` | Phase 1: crime + 311 encampment trends (382,746 NIBRS records; 74,113 311 requests) |
| `docs/phase2-options-memo.md` | Phase 2: cross-city evidence + four costed policy options |
| `docs/phase2b-cost-analysis.md` | Phase 2b: the $105k decomposition, ranked cost-reduction levers, evidence gaps |
| `charts/` | 17 charts backing the memos |
| `code/` | Analysis scripts (Python) |
| `data/DATA_NOTES.md` | Sources, coverage, and known limitations for every dataset |

## Reproduce it

Raw data (275 MB) is not committed. To rebuild from public sources:

```bash
python code/download_crime.py      # Denver Open Data Catalog: NIBRS crime offenses, 2021–2026
python code/download_311_encamp.py # Denver Open Data Catalog: 311 encampment requests, 2022–2025
python code/analyze_pilot.py       # Phase 1 findings + charts 01–08
python code/analyze_phase2_local.py# Phase 2 findings + charts 09–17
```

HUD Point-in-Time and Housing Inventory Count data: [hudexchange.info](https://www.hudexchange.info/programs/hdx/pit-hic/).
Denver Auditor reports: All In Mile High audit (Mar 2026); City Shelters audit + follow-ups (2024–2026).

## Caveats (read before quoting)

- 311 volume reflects reporting behavior as well as ground truth; ~80% of recent encampment reports
  close as "Transferred to External Agency" (routing, not resolution).
- Cross-city comparison is six continuums — correlation, not causal proof.
- Per-exit is one-time; PSH is annual — multi-year PSH stays accumulate cost.
- Inflow is unmeasured; eviction filings are a bounded proxy, not an attribution.
- Audits the *system*, never individuals. No person-level data is included or mapped.

## License

Analysis and text: public domain (CC0). Code: MIT.
