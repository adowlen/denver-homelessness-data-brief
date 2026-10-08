"""Phase 2b chart 17: benchmark comparison — Denver $/exit vs PSH/RRH/shelter/prevention unit costs."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/home/hatch/workspace/goals/denver-homelessness-response-data-driven-accountability/hidden_files/charts"

# (label, value, color-group)
items = [
    ("Denver AIMH $/housing exit\n(auditor, '23-'25)", 105074, "#c0392b"),
    ("Denver NCS shelter, Stone Creek\n$98.60/bed/night (2026 budget)", 36000, "#e67e22"),
    ("Denver PSH, H2H WellPower arm\n(high-acuity, Urban Inst.)", 35770, "#2a7f62"),
    ("Denver NCS shelter, Aspen\n$93.77/bed/night (2026 budget)", 34226, "#e67e22"),
    ("Denver micro-communities\n(tiny homes, 2025-26)", 33755, "#e67e22"),
    ("Prevention $/case averted\n(Chicago HPCC quasi-exp.)", 40000, "#5b7fa6"),
    ("Denver PSH, H2H CCH arm\n(Urban Inst. evaluation)", 22265, "#2a7f62"),
    ("PSH national (NAEH 2022)", 20115, "#2a7f62"),
    ("RRH $/household/yr (NAEH 2022)", 8486, "#1f6f6f"),
    ("Prevention $/household assisted\n(program range)", 3600, "#5b7fa6"),  # midpoint of 1k-7.2k
]
items.sort(key=lambda t: t[1], reverse=True)
labels = [i[0] for i in items]
vals = [i[1] for i in items]
colors = [i[2] for i in items]

fig, ax = plt.subplots(figsize=(11, 6.5))
y = np.arange(len(labels))
bars = ax.barh(y, vals, color=colors, edgecolor="white")
for yi, v in zip(y, vals):
    ax.text(v + 1500, yi, f"${v:,}", va="center", fontsize=10, fontweight="bold")
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlabel("Dollars (per person-year, per bed-year, or per exit — see labels)")
ax.set_title("What $105k/exit buys vs. alternatives (all-in operating, capital excluded)\n"
             "Denver's shelter beds already cost PSH-level money",
             fontsize=12, fontweight="bold")
ax.set_xlim(0, 122000)
from matplotlib.patches import Patch
legend = [Patch(color="#c0392b", label="Denver $/housing exit"),
          Patch(color="#e67e22", label="Denver shelter bed-year"),
          Patch(color="#2a7f62", label="PSH person-year"),
          Patch(color="#1f6f6f", label="RRH household-year"),
          Patch(color="#5b7fa6", label="Prevention")]
ax.legend(handles=legend, loc="lower right", fontsize=9)
fig.tight_layout()
fig.savefig(f"{OUT}/17_benchmark_comparison.png", dpi=130)
plt.close(fig)
print("chart 17 written")
