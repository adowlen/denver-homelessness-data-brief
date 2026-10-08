"""Phase 2b cost decomposition: Denver $105k/exit waterfall + conversion sensitivity.
All inputs are verified public numbers (see host_spending_research.md):
  spend = $178.1M (auditor, Jul 2023-Jun 2025), entrants = 3,902, housed = 1,695.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/home/hatch/workspace/goals/denver-homelessness-response-data-driven-accountability/hidden_files/charts"

SPEND = 178_100_000
ENTRANTS = 3_902
HOUSED = 1_695
CONV = HOUSED / ENTRANTS  # 0.4344
PER_ENTRANT = SPEND / ENTRANTS
PER_EXIT = SPEND / HOUSED
DRAG = PER_EXIT - PER_ENTRANT

print(f"per-entrant: ${PER_ENTRANT:,.0f}  conversion: {CONV:.1%}  per-exit: ${PER_EXIT:,.0f}  drag: ${DRAG:,.0f}")

plt.rcParams.update({"font.size": 11})

# --- Chart 15: waterfall decomposition ---
fig, ax = plt.subplots(figsize=(9, 5.5))
labels = ["Cost per\nentrant", "Conversion drag\n(43.4% housed)", "Cost per\nhousing exit"]
vals = [PER_ENTRANT, DRAG, PER_EXIT]
colors = ["#2a7f62", "#c0392b", "#1f3a5f"]
# waterfall bars
ax.bar([0], [PER_ENTRANT], color=colors[0], width=0.55)
ax.bar([1], [DRAG], bottom=PER_ENTRANT, color=colors[1], width=0.55)
ax.bar([2], [PER_EXIT], color=colors[2], width=0.55, alpha=0.25)
ax.bar([2], [PER_EXIT], color="none", edgecolor=colors[2], linewidth=2, width=0.55)
for x, v, lab in [(0, PER_ENTRANT, f"${PER_ENTRANT:,.0f}"),
                  (1, PER_ENTRANT + DRAG, f"+${DRAG:,.0f}"),
                  (2, PER_EXIT, f"${PER_EXIT:,.0f}")]:
    ax.text(x, v + 2500, lab, ha="center", fontweight="bold", fontsize=12)
ax.plot([0.35, 0.65], [PER_ENTRANT, PER_ENTRANT], "k--", lw=1)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(labels)
ax.set_ylabel("Dollars")
ax.set_title("Denver AIMH: decomposing the $105k per housing exit\n$178.1M / 3,902 entrants / 43.4% conversion (auditor, Jul 2023-Jun 2025)",
             fontsize=12, fontweight="bold")
ax.set_ylim(0, PER_EXIT * 1.18)
fig.tight_layout()
fig.savefig(f"{OUT}/15_cost_waterfall.png", dpi=130)
plt.close(fig)

# --- Chart 16: sensitivity of $/exit to conversion rate ---
convs = np.linspace(0.30, 0.90, 200)
per_exit = SPEND / (ENTRANTS * convs)
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(convs * 100, per_exit / 1000, lw=2.5, color="#1f3a5f")
for c, lab in [(CONV, f"actual 43.4%\n${SPEND/(ENTRANTS*CONV):,.0f}"),
               (0.55, "55%"), (0.70, "70%"), (0.85, "85%")]:
    v = SPEND / (ENTRANTS * c)
    ax.plot(c * 100, v / 1000, "o", color="#c0392b", ms=8)
    ax.annotate(f"{lab}\n${v:,.0f}" if "\n" in lab else f"{lab}: ${v:,.0f}",
                (c * 100, v / 1000), textcoords="offset points",
                xytext=(12, -6 if c > 0.6 else 10), fontsize=10,
                fontweight="bold" if c == CONV else "normal")
ax.set_xlabel("Shelter-to-housing conversion rate")
ax.set_ylabel("Cost per housing exit ($ thousands)")
ax.set_title("Holding $178.1M spend and 3,902 entrants constant:\n$/exit falls as conversion rises",
             fontsize=12, fontweight="bold")
ax.set_xlim(30, 90)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(f"{OUT}/16_conversion_sensitivity.png", dpi=130)
plt.close(fig)

# sensitivity table for the memo
print("\nSensitivity table (spend + entrants held constant):")
for c in [0.4344, 0.50, 0.55, 0.60, 0.70, 0.80, 0.85]:
    print(f"  {c:5.1%}  ->  ${SPEND/(ENTRANTS*c):>9,.0f}/exit")
print("\ncharts written: 15_cost_waterfall.png, 16_conversion_sensitivity.png")
