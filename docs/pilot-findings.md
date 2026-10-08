# Phase 1 pilot findings — "Is Denver's homelessness response working?"
*Independent data check, 2026-10-08. All statistics aggregate; no individual-level data used.*

## What we did
Downloaded two public datasets from the City and County of Denver Open Data program
(see `data/DATA_NOTES.md` for sources and caveats):
- **Crime incidents**: 382,746 NIBRS records, Jan 2021 → Oct 2026 YTD (Denver PD).
- **311 encampment-related service requests**: 74,113 records, 2022 → 2025
  (filtered from ~1.75M total 311 requests on encampment/homelessness keywords).

Charts: `charts/01–08`.

## The 5 most important findings

**1. Property crime has fallen sharply; violent crime is flat-to-easing — not rising.**
Property offenses dropped **33% from the 2022 peak** (44,356 → 29,750 in 2025).
Motor vehicle theft — the emblematic "out of control" crime — is down **63%**
(14,932 in 2022 → 5,574 in 2025). Violent crime (murder, aggravated assault,
robbery, simple assault) peaked at 6,882 in 2024 and eased to 6,710 in 2025;
aggravated assault + robbery + murder together are down ~14% from 2022.
The dominant trend in Denver crime data is *improvement since 2022*, led by property crime.

**2. Encampment 311 reports collapsed 62% from 2022 to 2025.**
26,908 (2022) → 24,383 (2023) → 12,661 (2024) → 10,161 (2025).
The steepest sustained decline begins right after the All In Mile High program
launched (~July 2023, marked on chart 06). The direction is consistent with the
city's claim of reduced street homelessness — but see caveat 4: 311 volume also
reflects reporting behavior, and this is correlation, not proof of causation.

**3. But 311 "resolution" is mostly triage, not resolution.**
About **80% of 2024–2025 encampment reports were closed as "Transferred to
External Agency"** — routed to the Department of Safety, not resolved by 311.
Median time-to-close is under a day, which measures *routing speed*, not how fast
an encampment was actually addressed. From this dataset we can say reports are
falling and being routed quickly; we **cannot** say what happened on the ground
after routing. That is the central visibility gap — and it matches the auditor's
finding that the city can't track outcomes per intervention.

**4. Crime is hyper-concentrated; "unsafe everywhere" is wrong.**
Five Points (25,259 incidents) has nearly 3x the count of Civic Center (9,028).
The top 5 neighborhoods (Five Points, Central Park, DIA, Capitol Hill, CBD)
dominate the citywide total. Risk in Denver is *place-specific*, which means
interventions can be place-specific too — a useful input for Phase 2 targeting.

**5. Reporting surges can masquerade as ground truth.**
Feb–Mar 2023 shows a dramatic spike (~3,400 reports in March), but it was driven
by a **single day — March 28, 2023 — with 1,116 PocketGov app reports**, almost
all "Encampment Reporting." That is an organized reporting surge (or bulk import),
not 1,116 new encampments in a day. Any analysis — including the city's own —
must scrub these artifacts before drawing conclusions.

## Perception vs. reality (3 claims tested)
| Claim a Denverite might believe | What the data says |
|---|---|
| "Violent crime keeps rising" | **Mostly false.** Flat since 2021 (~6.1–6.9K/yr); serious violent offenses down ~14% from 2022 peak. |
| "Car theft is out of control" | **False.** Down 63% from the 2022 peak; 2025 is the lowest in the 5-year window. |
| "Downtown is the most dangerous area" | **Misplaced.** CBD ranks 5th; Five Points has 2x its count. Concentrated, not citywide. |

## Honest caveats — what this data CAN'T tell us
- **2026 is year-to-date** (through early Oct, with reporting lag); don't annualize it.
- **311 volume = reporting behavior + ground truth.** App adoption, awareness campaigns,
  and single-day surges move the numbers independent of street conditions.
- **"Closed" ≠ fixed.** 311 statuses describe administrative handling, not outcomes.
- **Reported crimes only.** Victimization surveys consistently show underreporting;
  trends are more reliable than levels.
- **No sexual-assault breakout** in this NIBRS export (bucketed into "all other crimes").
- **Encampment reports ≠ count of unhoused people.** They measure visible encampments
  that someone bothered to report — a proxy with known biases.
- **Correlation ≠ causation** on All In Mile High. No control group; economy,
  seasonality, enforcement changes, and reporting fatigue are all confounders.
- **PIT counts not analyzed** — they're one-night January snapshots, widely
  considered an undercount, and need careful handling (Phase 2).

## What Phase 2 would need
1. **HUD PIT + HIC data by Continuum of Care** (public, annual) — cross-city comparison:
   which cities bent their curves, at what spend, under which model.
2. **HOST dashboard placement data** — the shelter→permanent-housing funnel
   (intake, placements, returns to homelessness) to quantify conversion rates.
3. **City budget figures** — homelessness spending by year/program to compute
   dollars-per-person-housed vs. alternatives.
4. **Displacement test** — using 2024–2025 geocoded 311 records (lat/lon available),
   test whether reports reappear near cleared sites (sweeps vs. solutions).
5. **Auditor's underlying datasets** if obtainable — to extend rather than duplicate
   the audit work.

## Recommendation
**Phase 2 is viable and worth doing.** The pilot proves the data pipeline works,
the signal is strong (both crime and encampment reports moving favorably since
2022/2023, with clear geographic concentration to exploit for targeting analysis),
and the visibility gap the auditor identified is real and measurable — 311 can
track *reports*, but nobody publishing public data tracks *outcomes*.
The highest-value Phase 2 deliverable remains the options memo: funnel math,
cross-city benchmarks, and cost-effectiveness in one brief a policymaker can act on.
