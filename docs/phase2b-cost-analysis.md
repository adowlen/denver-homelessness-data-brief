# Phase 2b — Cost deep-dive: verifying and attacking Denver's $105k per housing exit
*Addendum to the Phase 2 options memo. 2026-10-08. INTERNAL WORKING DOCUMENT — not published, not shared externally. All statistics are system-level aggregates from public sources. Every number below is cited; unverifiable numbers are given as bounded ranges, never point estimates.*

---

## Executive summary

**The "4×" claim checks out — and the deeper finding is worse.** Denver's $105,074 per housing exit is ~4.0× the midpoint of verified PSH operating costs ($20–36k/person/year, anchored by the Urban Institute's evaluation of Denver's own Housing to Health pilot: $22,265–$35,770). But the comparison that should alarm a policymaker isn't exit-vs-PSH — it's shelter-vs-PSH: **Denver's noncongregate shelter beds already cost $34–36k/bed/year** (2026 HOST budget: Aspen $93.77/night, Stone Creek $98.60/night). The city is paying permanent-housing prices for temporary shelter beds that retain nobody.

**Decomposition:** $105,074 = $45,643/entrant × 2.30 (the 43.4% conversion penalty). More than half the headline number ($59,430) is the arithmetic cost of non-conversion, not the cost of helping people.

**How to bring it down, ranked:** (1) raise conversion 43%→70% — cuts $/exit to ~$65k with *zero new spend*; (2) shift marginal bed dollars shelter→PSH — roughly operating-cost-neutral per the city's own bed-night figures, while converting temporary beds to permanent ones; (3) targeted prevention — ~$40k per case averted (honest quasi-experimental figure) vs. $105k/exit, credible only with tight targeting; (4) competitive procurement — bounded ~$4–8k/entrant; (5) outcome tracking — the precondition, still not done.

**Gaps filled this round:** final 2025 exits (1,744 housed vs 2,000 goal); 2025 PIT totals (7,327 city / 10,774 metro); 2026 proposed HOST budget ($71.64M GF); confirmed returns-to-homelessness tracking still absent from the dashboard; Denver eviction filings at a record 15,953 (+72% vs pre-pandemic) as a bounded inflow proxy (formal evictions ≈ 5–20% of inflow).

---

## 1. Decomposing the $105,074 per exit

$105,074/exit = ($178.1M ÷ 3,902 entrants) × (3,902 ÷ 1,695 housed). Two multiplicative terms:

| Term | Value | Source |
|---|---|---|
| **Cost per entrant** | **$45,643** ($178.1M ÷ 3,902) | Auditor AIMH audit, Mar 2026 (spend); HMIS via auditor (entrants), Jul 2023–Jun 2025 |
| **Conversion multiplier** | **×2.30** (1 ÷ 43.4%) | 1,695 long-term-housing moves ÷ 3,902 entrants, same period |
| **= Cost per exit** | **$105,074** | Arithmetic |

![Cost waterfall](charts/15_cost_waterfall.png)

The waterfall makes the policy point visually: more than half of the $105k ($59,430) is not the cost of helping someone — it is the arithmetic penalty of a 43.4% conversion rate. Every entrant who cycles through shelter without reaching housing raises the per-exit cost of those who do.

### Conversion sensitivity (spend and entrants held constant)

![Conversion sensitivity](charts/16_conversion_sensitivity.png)

| Conversion rate | Implied $/exit | What it resembles |
|---|---|---|
| 43.4% (actual) | $105,074 | Denver AIMH, Jul 2023–Jun 2025 |
| 55% | ~$83,000 | — |
| 70% | ~$65,200 | At Home/Chez Soi RCT housing-first arm (~73% days housed) |
| 85% | ~$53,700 | Upper-end housing-first retention benchmarks |

Two readings: (a) even at an excellent 85% conversion, Denver's model would still cost ~$54k/exit — the per-entrant cost itself ($45.6k) is high; (b) conversion is the single biggest lever because it attacks the multiplier, not just the base.

### Cost-per-entrant drivers ($45,643)

- **205-day average noncongregate-shelter stays** (Dec 2025 council presentation). At the city's own 2026 estimate of **$140–$160/family/night** for noncongregate shelter — and that figure *excludes* capital, security, maintenance, and leasing (HOST family-homelessness presentation to council, 2026) — a 205-day stay implies roughly **$29k–$33k in shelter operating cost alone per entrant** for families; the true all-in figure is higher. No published per-bed-night figure exists for individual adults (gap).
- **Hotel-based model.** AIMH's noncongregate approach (converted hotels) carries hotel economics: 24/7 staffing, food, wraparound services. The auditor's shelter audit found the city could not produce per-shelter total costs at all — which is itself a cost driver: unmeasured costs can't be managed down.
- **Sole-source contracting.** The auditor found HOST awarded sole-source (non-competitive) contracts to major vendors without adequate justification (AIMH audit, Mar 2026). Competitive procurement is a standard 10–20% lever in public contracting literature; applied to the shelter-operations portion of spend this is a bounded, not precise, estimate — see levers below.
- **Admin/overhead.** Not separately published (part of the visibility gap). The 2026 proposed HOST budget shows 73.66 FTE on a $71.6M General Fund base; special-revenue funds sit outside that figure, so a true overhead share cannot be computed from public data.

---

## 2. Verifying the "4× PSH" comparison

Best-supported all-in PSH operating range: **~$20,000–$36,000 per person per year**, anchored by the Urban Institute's evaluation of **Denver's own Housing to Health (H2H) supportive-housing pilot** — the most apples-to-apples comparator available.

| Benchmark | $/person/yr (or as noted) | Includes / excludes | Geography | Year ($) | Source |
|---|---|---|---|---|---|
| Denver H2H, CCH arm (scattered-site) | **$22,265** | All-in: ~$10,950 housing + ~$2,150 Medicaid services + ~$9,183 program services; excludes capital | Denver | 2016–20 | Urban Institute, via NYC HPD deck |
| Denver H2H, WellPower arm (high-acuity) | **$35,770** | All-in: ~$10,950 housing + ~$9,165 Medicaid + ~$15,637 program services; excludes capital | Denver | 2016–20 | Same |
| Denver city planning figure | ~$18,000 | Rough all-in (rent + wraparound) | Denver | ~2017 | 5280, quoting city |
| NAEH national PSH estimate | $20,115/adult household | Rental subsidy + services; excludes capital | National | 2022 | National Alliance to End Homelessness |
| Terner Center (26 properties) | ~$17,000 avg | Property mgmt + services; excludes capital | Bay Area | 2022 | UC Berkeley Terner Center |
| HUD Cityscape (LA-based) | $17,000 ($11k rent + $6k services) | Rent + services; authors call it "high-side" | Los Angeles | ~2018 | HUD USER |
| CSH supportive housing | $41,833 | Full operating; excludes capital | NYC | ~2021–22 | Corporation for Supportive Housing |
| NAEH rapid rehousing | **$8,486/household/yr** | Time-limited rent assistance + case mgmt | National | 2022 | NAEH |
| RRH cost per successful exit | ~$4,100/household | Per exit to permanent housing | Multi-state | ~2015–16 | NAEH |
| **Denver NCS shelter, Aspen (289 beds)** | **$34,226/bed/yr** ($93.77/night) | Operations; excludes overhead + hotel capital | Denver | 2026 budget | HOST presentation to City Council, Oct 2025 |
| **Denver NCS shelter, Stone Creek (182 beds)** | **$36,000/bed/yr** ($98.60/night) | Operations; excludes overhead + hotel capital | Denver | 2026 budget | Same |
| Denver micro-communities (tiny homes) | $33,755/bed/yr ($92.48/night) | Operations; excludes ~$25k/unit construction | Denver | 2025–26 | Same |

![Benchmark comparison](charts/17_benchmark_comparison.png)

**Verdict: the "roughly 4×" claim is fair — arguably conservative.** $105,074 ÷ ~$26,000 (midpoint of the $20–36k Denver-anchored range) ≈ **4.0×**. Against the H2H CCH arm ($22,265) it's 4.7×; against the high-acuity WellPower arm ($35,770) it's 2.9×. Three caveats, all labeled: (1) per-exit is a one-time throughput metric while PSH is an *annual* cost — a PSH tenant housed for years costs multiples of one year's figure, so the comparison favors exits over multi-year PSH stays; (2) H2H served high-utilizer, high-acuity participants (the expensive end of PSH), which flatters the ratio; (3) **the sharper policy point is inside the chart**: Denver's own noncongregate shelter beds already cost **$34–36k/bed/year** — PSH-level operating money for a shelter bed that is not permanent housing and retains nobody. The city is paying housing prices for shelter.

*Not verified:* HUD's "Costs Associated with First- and Second-Generation Permanent Supportive Housing" could not be located as a published study; no Denver HOST-published PSH operating figure outside the H2H evaluation was found. Denver rents run materially above national averages, so national benchmarks understate Denver's true PSH cost — the H2H Denver figures are the primary comparator for that reason.

---

## 3. Cost-reduction levers, ranked by estimated impact

### Lever A — Raise conversion (attack the ×2.30 multiplier)
- **Mechanism:** rapid-rehousing scale-up + 12-month retention case management + explicit exits/month targets to relieve 205-day stays (Phase 2 Option 4).
- **Math:** 43% → 70% conversion cuts $/exit from ~$105k to ~$65k *with zero change in total spend* — a ~$40k/exit reduction, the largest single lever in the decomposition.
- **Benchmark support:** At Home/Chez Soi RCT 73% days housed; HUD-VASH Housing First 98% vs 86% retention; Pathways 80% at 12 months (see host_spending_research.md §C).
- **Cost to implement:** illustrative $10–15M for 1,000 RRH households (national $10–15k/household; Denver-specific RRH unit cost still a gap).

### Lever B — Shift marginal bed dollars from shelter to PSH/RRH (lower the $45.6k base)
- **Mechanism:** Denver's own numbers now make this airtight: noncongregate shelter beds cost **$34–36k/bed/year** (Aspen $93.77/night, Stone Creek $98.60/night, 2026 HOST budget figures) while Denver PSH costs **$22–36k/person/year** (Urban Institute H2H evaluation). **Shifting a bed from hotel-shelter to PSH is roughly cost-neutral on operating dollars while converting a temporary bed into a permanent one** with 80%+ retention — and every PSH placement avoids repeat $45.6k shelter episodes through the 205-day loop.
- **Math:** shifting $18M/yr (≈20% of shelter operating spend) funds ~690 PSH slots at ~$26k/person/yr (midpoint of Denver's H2H range). Each slot that retains a tenant year-over-year compounds the saving; each avoided shelter recycle avoids another $45.6k entrant-cost.
- **Benchmark support:** Houston held ~60% PSH+RRH bed share with the flattest PIT curve (+14% vs Denver +80%, 2019–2025).

### Lever C — Competitive procurement (attack the base)
- **Mechanism:** implement the auditor's open recommendations on sole-source contracting; require competitive bids for shelter operations and services contracts.
- **Math:** bounded estimate — public-procurement literature typically finds 10–20% savings from competitive vs. sole-source contracting. Applied to the shelter-operations portion of the $178.1M (roughly the $149.6M shelter-ops figure from the Nov 2024 audit, different period — treat as order-of-magnitude), that's **~$15–30M over a two-year period**, or roughly **$4k–$8k off the per-entrant cost**. Labeled bounded: the true addressable base is not published.
- **Cost to implement:** negligible (process change).

### Lever D — Prevention (shrink the inflow, cheapest per touch)
- **Mechanism:** emergency rental assistance / eviction-prevention for high-risk households before they enter the shelter system at $45.6k/entrant.
- **Math:** published prevention costs run **~$1,000–$7,200/household** depending on depth (NYC HomeBase RCT ~$2,235/family; Chicago call-center ~$1,300/referral; Philadelphia COVID ERA ~$7,172/household for deep assistance). BUT the decision-relevant number is cost per *case of homelessness actually averted*: the best quasi-experimental estimate (Chicago HPCC, Evans et al., Science 2016) implies **~$40k/person (~$100k/household) per case averted** because most assisted households would not have become homeless anyway.
- **Honest verdict:** even at the honest ~$40k/person averted cost, prevention is at or below Denver's $105k/exit — and the NYC HomeBase RCT returned >$1.25 per $1 invested on shelter savings alone. **The lever is credible but lives or dies on targeting.** Blanketing all ~16,000 annual eviction-filing households at $2,000 each ($32M/yr) with a 4pp hit rate averts ~640 entries at ~$50k each — roughly break-even vs. exits, far better with tight targeting (prior filings, arrears depth, families, institutional-discharge linkage).
- **Denver inflow context:** eviction filings hit a record 15,953 in 2025 (+72% vs pre-pandemic); MDHI's PIT survey ranks inability to pay rent #1 and eviction #2 as self-reported causes. Formal evictions plausibly drive 5–20% of inflow; the broader rent-burden cluster is larger but harder to target. 847 families received city eviction-prevention assistance in 2025 (no published $/household — gap).
- **Cost to implement:** scales with targeting quality; a tight pilot (2,000 highest-risk households × ~$3,000) ≈ **$6M/yr**.

### Lever E — Outcome tracking itself (the precondition)
- **Mechanism:** implement the auditor's open recommendations — per-shelter/per-program cost tracking in Workday, decrement housing counts on return, publish 1-year retention, restore removed dashboard metrics.
- **Math:** no direct $/exit effect; but the 205-day stays, the sole-source contracts, and the $59k conversion drag all persisted for years *unmeasured*. Unit cost you don't measure can't be managed down.
- **Cost to implement:** <$1M one-time admin/IT (Phase 2 estimate); confirmed still not done — returns-to-homelessness and 1-year retention remain absent from the public dashboard as of Dec 2025 (Urban Institute interim evaluation).

**Ranking by estimated $/exit impact:** A (conversion, ~$40k/exit at 70%) > B (bed-mix shift, lowers base + breaks recycle loop) > D (prevention, ~$50k/averted entry targeted) > C (procurement, ~$4–8k/entrant bounded) > E (precondition, indirect).

---

## 4. Evidence gaps — updated status

| Gap | Status | Finding |
|---|---|---|
| Returns-to-homelessness tracking on public dashboard | **Confirmed still absent** | Urban Institute interim evaluation (Dec 2025): "Future evaluation reporting will examine… returns to homelessness" — i.e., not public. Auditor Mar 2026: Mayor's Office *disagreed* with dashboard-revision recommendation. Current dashboard (renamed "Citywide Progress Report") shows only moves-to-shelter/moves-to-housing totals. |
| Final 2025 housing exits | **FILLED** | 2,584 moved indoors (goal 2,000 — exceeded); **1,744 connected to permanent housing (goal 2,000 — missed at 87%)**. City 2025 Scorecard annual report. Note: "people" vs earlier "moves" units may not be perfectly comparable. |
| 2026 budget | **Partially filled** | HOST 2026 *proposed* General Fund $71.64M (86.9% homelessness-resolution share); special-revenue funds (incl. ~$55M/yr Homelessness Resolution Fund) sit outside that figure. Adopted-book total not verified. |
| Newer audits | **Partially filled** | May 2026 follow-up on Nov 2024 shelter audit: only 5 recommendations partially implemented; HOST still unaware of per-shelter spend. No newer AIMH audit found through Oct 2026 (Mar 2026 audit's implementation targets run to Dec 2026). |
| 2025 PIT total | **FILLED** | Metro CoC (CO-503): **10,774** (unsheltered 2,149, down from 2,919). Denver city: **7,327** (+12% vs 2024; +86% vs 2019). Advocates dispute the sheltered/unsheltered split (extreme-cold count night). |
| Denver-specific PSH/RRH unit costs | **In progress** | See §2. |
| Inflow data | **Partially filled** | Eviction filings: 15,953 (2025, record, +72% vs pre-pandemic); pre-pandemic baseline ~9,200/yr. Formal evictions ≈ 5–20% of inflow (bounded estimate); broader rent-burden cluster larger. No Denver study pins the exact share. |

---

## 5. Revised option costs (Phase 2 options, updated)

- **Option 1 (rebalance to ≥60% housing-first):** unchanged — budget-neutral reallocation within ~$89M/yr run-rate. Now sharpened: shifting $18M/yr funds **~690 PSH slots at ~$26k/person/yr** (Denver H2H midpoint), and Denver's shelter beds ($34–36k/bed/yr) already cost as much as PSH — the reallocation is close to operating-cost-neutral while converting temporary beds to permanent ones.
- **Option 2 (fix outcome tracking):** unchanged — <$1M one-time. Strengthened by confirmation that returns tracking is *still* absent (Dec 2025).
- **Option 3 (hotspot deployment):** revised to **~$13M/yr for 500 placements** at Denver's ~$26k/person/yr PSH midpoint (was illustrative $12.5M at national $25k). RRH variants run less (~$8.5k/household/yr nationally).
- **Option 4 (unclog the funnel):** unchanged at illustrative $10–15M for 1,000 RRH households. Now anchored: 2025 final was 1,744 housed vs 2,000 goal — the funnel is the binding constraint, and the sensitivity table (§1) shows 70% conversion cuts $/exit to ~$65k with no new spend.

---

## 6. What remains unfilled

1. **Denver-specific RRH $/household** — national figure ($8,486/yr) verified; Denver-local RRH unit cost still a gap (HOST's 2025 RRH expansion contracts may state it).
2. **Denver-specific prevention $/household** — the city's 847-family 2025 program has no published unit cost.
3. **Eviction-attributable share of inflow** — bounded at 5–20%, no Denver linkage study.
4. **Adopted (not proposed) 2026 HOST budget total** including special-revenue funds.
5. **Per-shelter and per-program cost splits** — the auditor's core complaint; still unmeasurable from public data.
6. **Adult-individual noncongregate shelter $/bed-night for the 2023–25 period** — only 2026 budget figures ($93.77–$98.60/night) and the family figure ($140–160/night, excl. capital/security) are published.
