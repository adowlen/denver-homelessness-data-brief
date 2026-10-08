# Policy Options Memo — Making Denver's Homelessness Response Work Better
*Phase 2, goal "Denver homelessness response: data-driven accountability" — 2026-10-08.*
*INTERNAL WORKING DOCUMENT. Not published, not shared externally. All statistics are
system-level aggregates from public sources. We audit the system, never individuals.*

Phase 1 answered "is it working" (see `pilot-findings.md`). This memo answers Alex's
follow-up: **what could make it work better** — with 3–4 roughly-costed options a council
member could act on, in the style of a CBO options brief. Uncertainty is labeled
throughout; nothing here is causal proof.

---

## Executive summary

Denver's All In Mile High program moved 3,902 people indoors (Jul 2023–Jun 2025) at an
auditor-estimated $178.1M — **$45,650 per person moved indoors, $105,070 per person who
reached long-term housing**. Only ~43% of those brought indoors exited to long-term
housing, and ~13% of that "housing" was HUD-classified *temporary* housing. The public
dashboard never subtracts people who return to the street.

Cross-city comparison (HUD data, 6 western CoCs, 2019–2025) finds the lever associated
with bent homelessness curves is **bed composition, not bed volume**: Houston held ~60%
of beds as permanent supportive housing + rapid rehousing and its rate barely moved
(4.7→5.3 per 10k, +14%). Denver nearly *doubled* emergency-shelter beds yet posted the
steepest rate increase of the six (+80%, 17.8→32.1 per 10k).

Two new findings from Denver's own 311 data: (1) after a report closes, a new report is
significantly more likely to appear within 150m within 14 days than chance predicts
(+9.2pp vs. a shuffled baseline) — consistent with encampments reforming nearby; and
(2) 24% of all encampment reports come from just 25 half-kilometer grid cells, which also
carry heavy violent/property crime loads — making targeted deployment viable.

**Bottom line for a policymaker:** Denver is spending at a high per-person rate on a
shelter-led funnel that converts ~4 in 10 entrants to housing, while the cities that
bent their curves spent their marginal dollar on housing-first capacity and measured
outcomes ruthlessly. The four options below follow directly from that evidence.

---

## E1. The funnel: 3,902 in, ~1,475 truly housed

![AIMH funnel](charts/13_aimh_funnel.png)

HMIS figures via the Denver Auditor, Mar 2026 (the auditor could *not* independently
verify them — Metro Denver Homeless Initiative owns the data):

| Stage | Count | Share of intake |
|---|---|---|
| Moved indoors (temporary/noncongregate shelter) | 3,902 | 100% |
| → moved to "long-term housing" | 1,695 | 43% |
| → true permanent housing (HUD definition) | ~1,475 | ~38% |

Leakage points, all from public sources:
- **~13%** of the "long-term housing" count was "stable housing" — foster care,
  transitional housing, self-paid hotels, temporary family reunification — which HUD
  classifies as *temporary*, not permanent (Auditor, p. 19).
- **Returns are never subtracted.** Pre-redesign dashboard (Dec 2024): 11.6% returned to
  unsheltered homelessness, ~3% to jail, <1% died. The "moved into housing" figure is a
  running total; HOST says it cannot currently track when someone leaves housing.
- **Pace is slipping.** 2025 goal: 2,000 exits to housing; 1,180 achieved Jan–Sep 2025.
- **Stays are long.** Average noncongregate-shelter stay: 205 days (~7 months) — shelter
  beds are silting up because exits are slow.

Benchmark: the At Home/Chez Soi randomized trial (n=2,148, the largest Housing First RCT)
found 73% of days housed at 24 months vs. 32% for treatment-as-usual; HUD-VASH Housing
First retained 98% vs. 86% for traditional approaches; Houston reports >90% retention.
Denver's ~38–43% conversion sits well below housing-first benchmarks.

## E2. Cross-city: composition beats volume

![PIT per 10k trends](charts/11_pit_per10k_trends.png)

| CoC | PIT/10k 2019 → 2025 | Δ rate | PSH+RRH bed share 2019 → 2025 |
|---|---|---|---|
| Denver CO-503 | 17.8 → 32.1 | **+80%** | 43% → 50% |
| Houston TX-500 | 4.7 → 5.3 | **+14%** | 60% → 58% |
| Salt Lake City UT-500 | 15.9 → 23.5 | +48% | 65% → 62% |
| Phoenix AZ-502 | 14.8 → 20.8 | +41% | 65% → **57%** |
| Seattle WA-500 | 49.7 → 72.2 | +45% | 52% → 57% |
| San Diego CA-601 | 24.3 → 30.2 | +24% | 59% → **67%** |

![HIC bed mix shift](charts/12_hic_bedmix_shift.png)

Reading (correlation across six CoCs, **not** causal proof):
- **Houston** added little capacity but held ~60% of beds as PSH/RRH and ~1.6 beds per
  counted person — flattest curve, lowest rate (one-sixth of Denver's), unsheltered share
  *fell* 41%→31%.
- **San Diego** had the largest housing-first shift (59%→67%) and the only rising
  beds-per-person ratio — second-flattest curve (+24%).
- **Denver** added the *most* beds of any city in the set (shelter beds nearly doubled:
  2,986→5,491) and raised its housing-first share — yet posted the steepest rate rise.
  Capacity grew; the count outgrew capacity (beds per person fell 1.59→1.40).
- **Phoenix** is the cautionary inverse: started with the highest housing-first share
  (65%), let it erode to 57% while doubling shelter beds — rate and unsheltered share
  both grew.

Caveats: PIT is a one-night January undercount; 2021 is methodologically broken (COVID);
Denver's 2024 spike partly reflects expanded count methodology; CoC boundaries ≠ city
boundaries (CO-503 is 7-county metro Denver). Full detail in
`phase2_data/hud_crosscity_findings.md`.

## E3. Cost-effectiveness

![Cost per person](charts/14_cost_per_person.png)

| Metric | Value | Period / source |
|---|---|---|
| Denver AIMH spend (auditor estimate) | $178.1M | Jul 2023–Jun 2025 (mayor's office had reported $158M) |
| → per person moved indoors | **$45,650** | $178.1M ÷ 3,902 |
| → per person reaching long-term housing | **$105,070** | $178.1M ÷ 1,695 |
| CSI estimate per person served | $69,413 | Dec 2024 ($155M projected ÷ 2,233) — different scope |
| Houston $/person | *not published comparably* | Houston's edge shows in outcome rates (>90% retention), not unit costs |

The uncomfortable arithmetic: at $105k per permanent-housing exit, Denver's model costs
roughly **4× a year of PSH operating costs** per successful exit — before counting the
205-day shelter stays consumed along the way. (PSH operating costs ~$20–30k/person/year
are national illustrative ranges, not Denver-specific — see evidence gaps.)

## E4. Displacement test (exploratory): cleared sites see nearby reappearance

![Displacement test](charts/09_displacement_reappearance.png)

Method: for each closed 2024–2025 encampment 311 report, checked whether a new report
appeared within a radius/window after its close date; baseline = same test with
created-dates shuffled (destroys spatiotemporal association). n=21,684 closed reports.

- At **150m / 14 days**: 54.7% observed vs. 45.5% baseline (**+9.2pp**, ~20% relative
  elevation). At 500m/30d the test saturates (90% vs 91%) — background density is too
  high to distinguish, an honest null at that scale.
- Reports closed as **"Transferred to External Agency"** (85% of 2024–25 closures —
  triage routing, not resolution) reappear at 55.3% vs. 50.3% for other closure types.

Interpretation (labeled exploratory): consistent with encampments reforming or persisting
nearby after the report is administratively closed. Cannot distinguish "encampment moved
100m" from "same encampment re-reported" — but either way, *closure ≠ resolution*, which
matches the auditor's outcome-visibility finding.

## E5. Targeting: a quarter of the problem sits in 25 grid cells

![Hotspot map](charts/10_hotspot_map.png)

~500m grid over Denver, 2024–2025 encampment 311 reports joined with violent+property
crime counts:
- **Top 10 cells: 12.6%** of all encampment reports. **Top 25 cells: 24.3%.**
- The top cells also carry the heaviest crime loads (e.g., cell #1: 463 encampment
  reports + 673 violent/property crimes) — encampment density and crime density overlap.
- Full ranked list: `phase2_data/hotspot_top25.csv` (center lat/lon per cell).

Policy implication: a fixed number of housing placements buys the largest
street-disorder reduction if deployed where reports *and* crime concentrate — rather
than spread thinly or allocated by complaint volume alone.

---

## Policy options

### Option 1 — Rebalance bed capacity toward housing-first (the Houston/San Diego play)
- **What:** commit to holding **≥60% of year-round beds as PSH + rapid rehousing**
  (Houston's level; Denver is at 50%), and direct marginal capital/operating dollars to
  PSH/RRH instead of new emergency-shelter beds.
- **Rough cost:** budget-neutral at the margin — reallocate within the ~$89M/yr AIMH
  run-rate. Illustrative: shifting 20% of shelter operating spend (~$18M/yr) funds
  roughly 600–900 PSH slots at national $20–30k/person/year operating ranges
  (*Denver-specific PSH unit costs are an evidence gap — see below*).
- **Expected effect:** the cross-city pattern associates a held housing-first mix with
  flatter PIT curves (Houston +14% vs. Denver +80%, 2019–2025). Uncertainty is **wide**:
  six-CoC correlation, not causation; Denver's inflow dynamics may differ.
- **Supported by:** Houston TX-500, San Diego CA-601.
- **Risks:** PSH takes years to build/lease; near-term visible encampments persist;
  political pressure favors visible shelter action over slow housing pipelines.

### Option 2 — Fix the outcome-visibility gap (the auditor's play)
- **What:** implement the auditor's still-open recommendations: per-shelter and
  per-program cost tracking in Workday; **decrement housing counts when people return**
  to homelessness; publish 1-year post-placement retention; restore the dashboard
  metrics removed in Apr 2025 (returns, jail placements, deaths).
- **Rough cost:** low — administrative/IT, on the order of **<$1M one-time** plus staff
  time (rough estimate; the cost is political more than fiscal).
- **Expected effect:** no direct housing effect — but it is the precondition for every
  other option. You cannot manage a $89M/yr program whose outcomes cannot be verified.
  Feasibility uncertainty: **low**; impact uncertainty: indirect.
- **Supported by:** Denver Auditor Mar 2026 + May 2026 follow-up; our finding that 85%
  of 311 encampment closures are triage routing with zero outcome visibility.
- **Risks:** honest numbers are politically uncomfortable in the short run.

### Option 3 — Targeted hotspot deployment (the place-based play)
- **What:** concentrate the next wave of housing placements, outreach teams, and
  services in the **top-25 grid cells** (24% of encampment reports, overlapping violent/
  property crime hotspots), instead of allocating by complaint volume or evenly.
- **Rough cost:** illustrative — 500 placements at ~$25k/yr PSH-equivalent ≈
  **$12.5M/yr**; rapid-rehousing variants cost less per household.
- **Expected effect:** our displacement test suggests administratively "closed" sites
  see elevated nearby reappearance (+9pp at 150m/14d) — *placements*, not sweeps, are
  the mechanism that breaks the cycle. Targeting concentrates that mechanism where
  measured disorder is densest. Uncertainty: **moderate** (reporting-behavior confounds).
- **Supported by:** our hotspot analysis (E5); Houston's coordinated-access
  prioritization model as the process template.
- **Risks:** geographic-equity objections ("why does that neighborhood get the
  resources?"); requires co-located services, not just vouchers.

### Option 4 — Unclog the shelter→housing funnel (the throughput play)
- **What:** attack the 43% conversion rate directly: scale **rapid rehousing**
  (596 AIMH exits via RRH 2023–25; HOST targets ≤60-day move-in, ≥80% permanent exits),
  add 12-month retention case management, and set an explicit exits-per-month target to
  relieve the 205-day average shelter stay.
- **Rough cost:** illustrative — RRH runs roughly **$10–15k/household** nationally;
  1,000-household scale ≈ **$10–15M** (Denver-specific RRH costs are an evidence gap).
- **Expected effect:** RCT evidence (At Home/Chez Soi: 73% days housed vs 32%;
  HUD-VASH HF: 98% vs 86% retention) suggests housing-first exits stick far better than
  shelter cycling. If Denver's conversion rose from ~43% toward 70%, that's on the order
  of **~1,000 additional permanent exits per 3,900 entrants**. Uncertainty: **moderate** —
  RCT populations differ from Denver's unsheltered cohort.
- **Supported by:** At Home/Chez Soi, HUD-VASH, Pathways (80% 12-month retention).
- **Risks:** landlord recruitment in a tight rental market; RRH subsidies are
  time-limited — cliff effects if employment/income doesn't stabilize.

---

## What we'd need to tighten this up (evidence gaps)

1. **Final 2025 housing-exit figure** (1,180 vs 2,000 goal as of Sep 2025 — year-end
   unknown) and any **1-year post-placement retention** number for AIMH.
2. **Denver-specific unit costs**: PSH operating cost/person/year and RRH
   cost/household in the Denver market — needed to turn illustrative option costs
   into real ones.
3. **Year-by-year budget splits** for homelessness spending (the auditor's core
   complaint: HOST cannot produce per-program, per-shelter costs).
4. **Inflow data**: how many people become homeless in Denver per year — the analysis
   above is all about the *stock* and *outflow*; without inflow, we can't say whether
   any option bends the curve or just drains it faster.
5. **2024 PIT methodology documentation** (to separate measurement from real change
   in the 2023→2024 jump) and 2025 PIT final tables.
6. **Returns-to-homelessness tracking** reinstated on the public dashboard.

## Methods & files

- Phase 1 data/methods: `pilot-findings.md`, `data/DATA_NOTES.md`.
- Phase 2 inputs: `phase2_data/hud_pit_hic_2019_2025.csv` (+ `hud_crosscity_findings.md`,
  build scripts), `phase2_data/host_spending_research.md` (every number sourced),
  `phase2_data/hotspot_top25.csv`.
- New analysis code: `data/analyze_phase2_local.py` (displacement test via BallTree
  haversine + shuffled-date baseline; 500m grid hotspot join with NIBRS crime).
- Charts: `charts/09_displacement_reappearance.png`,
  `charts/10_hotspot_map.png`, `charts/11_pit_per10k_trends.png`,
  `charts/12_hic_bedmix_shift.png`, `charts/13_aimh_funnel.png`,
  `charts/14_cost_per_person.png`.
- Key analytic choices: displacement baseline shuffles created-dates (3 iterations,
  stable to ±0.5pp); single-day reporting surges excluded from anchors; 2026 crime
  data excluded (YTD + reporting lag); all uncertainty labeled in-text, not footnoted
  away.
