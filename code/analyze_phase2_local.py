"""Phase 2 — displacement test + targeting hotspot analysis.
Displacement (exploratory): for each CLOSED 2024-2025 encampment 311 report, check
whether a NEW report appears within 500m within 30 days after its close date.
Baseline: same computation with created-dates shuffled (destroys spatiotemporal
association while preserving marginal distributions).
Hotspots: 0.005-degree grid ranking by 2024-2025 encampment report density,
joined with crime counts for targeting context.
All aggregate; audits the system, not individuals.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.neighbors import BallTree

HERE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.abspath(os.path.join(HERE, "..", "charts"))
EARTH_KM = 6371.0088
# parameter sweep: (radius_km, window_days). 500m/30d saturates (background
# density too high to distinguish); tighter scales test for genuine signal.
PARAM_SETS = [(0.5, 30), (0.15, 14), (0.15, 30), (0.25, 14)]

df = pd.read_csv(os.path.join(HERE, "encampment_311_2022_2025.csv"),
                 encoding="latin-1", low_memory=False)
df["created_dt"] = pd.to_datetime(df["created"], errors="coerce")
df["closed_dt"] = pd.to_datetime(df["closed"], errors="coerce")
sub = df[df["created_dt"].dt.year.isin([2024, 2025])].copy()
sub = sub.dropna(subset=["Latitude", "Longitude"]).reset_index(drop=True)
print(f"2024-25 geocoded records: {len(sub)}")

# exclude single-day reporting-surge artifacts (>150 reports in one day)
day_counts = sub["created_dt"].dt.date.value_counts()
surge_days = set(day_counts[day_counts > 150].index)
print(f"surge days excluded: {sorted(str(d) for d in surge_days)}")
sub = sub[~sub["created_dt"].dt.date.isin(surge_days)].reset_index(drop=True)

coords = np.radians(sub[["Latitude", "Longitude"]].to_numpy())
tree = BallTree(coords, metric="haversine")

created = sub["created_dt"].to_numpy()  # datetime64
closed = sub["closed_dt"].to_numpy()
anchor_mask = ~pd.isna(sub["closed_dt"]).to_numpy()
anchor_idx = np.where(anchor_mask)[0]
print(f"anchors (closed reports): {len(anchor_idx)}")


def reappearance_rate(created_arr, anchor_idx, nbr_idx, closed_arr,
                      radius_km, window_days):
    radius_rad = radius_km / EARTH_KM
    hits = 0
    for i in anchor_idx:
        c = closed_arr[i]
        lo = c + np.timedelta64(1, "D")
        hi = c + np.timedelta64(window_days, "D")
        nb = nbr_idx_all[i] if radius_km == 0.5 else None
        if nb is None:
            nb = tree.query_radius(coords[i:i + 1], r=radius_rad)[0]
        nb = nb[nb != i]
        if len(nb) == 0:
            continue
        nbc = created_arr[nb]
        if np.any((nbc >= lo) & (nbc <= hi)):
            hits += 1
    return hits / len(anchor_idx)


# precompute 500m neighborhoods once (largest radius; subsets for smaller)
nbr_idx_all = tree.query_radius(coords, r=0.5 / EARTH_KM)

rng = np.random.default_rng(42)
disp_results = []
for radius_km, window_days in PARAM_SETS:
    obs = reappearance_rate(created, anchor_idx, None, closed, radius_km, window_days)
    base_runs = []
    for b in range(3):
        perm = rng.permutation(len(created))
        base_runs.append(reappearance_rate(created[perm], anchor_idx, None,
                                           closed, radius_km, window_days))
    base_mean = float(np.mean(base_runs))
    disp_results.append((radius_km, window_days, obs, base_mean))
    print(f"r={radius_km*1000:.0f}m w={window_days}d: observed={obs:.3f} "
          f"baseline={base_mean:.3f} (runs {[f'{x:.3f}' for x in base_runs]})")

# cut by closure type at the tightest scale (150m/14d): triaged vs otherwise
triage_mask = sub["Case Status"].str.contains("Transferred to External", na=False).to_numpy()
tri_idx = anchor_idx[triage_mask[anchor_idx]]
oth_idx = anchor_idx[~triage_mask[anchor_idx]]
obs_tri = reappearance_rate(created, tri_idx, None, closed, 0.15, 14)
obs_oth = reappearance_rate(created, oth_idx, None, closed, 0.15, 14)
print(f"150m/14d reappearance | triaged (Transferred): {obs_tri:.3f} (n={len(tri_idx)})")
print(f"150m/14d reappearance | other closures:        {obs_oth:.3f} (n={len(oth_idx)})")

# monthly observed rate (for chart context)
sub["ym"] = sub["created_dt"].dt.to_period("M").astype(str)

# ---- chart 09: observed vs baseline across parameter sets ----
fig, ax = plt.subplots(figsize=(8, 4.8))
x = np.arange(len(disp_results))
w = 0.35
obs_v = [r[2] for r in disp_results]
base_v = [r[3] for r in disp_results]
b1 = ax.bar(x - w / 2, obs_v, w, label="Observed", color="#b03a2e")
b2 = ax.bar(x + w / 2, base_v, w, label="Baseline (shuffled dates)", color="#7f8c8d")
ax.set_xticks(x)
ax.set_xticklabels([f"{int(r[0]*1000)}m / {r[1]}d" for r in disp_results])
ax.set_ylabel("Share of closed reports with a new nearby report")
ax.set_title("Displacement test (exploratory): do encampment reports reappear\n"
             "nearby after closure? Denver 311, 2024-2025", fontsize=11)
ax.legend(fontsize=9)
ax.set_ylim(0, max(obs_v + base_v) * 1.2)
for bars in (b1, b2):
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.008,
                f"{bar.get_height():.0%}", ha="center", fontsize=9)
ax.text(0.5, -0.30,
        "At 150m/14d the gap vs baseline is the displacement signal (same-block reappearance).\n"
        "Exploratory: reappearance \u2260 same encampment; reporting behavior confounds.",
        ha="center", va="top", transform=ax.transAxes, fontsize=8, color="#555555")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS, "09_displacement_reappearance.png"), dpi=130)
plt.close()

# ---- hotspot targeting analysis ----
CELL = 0.005
sub["cell_lat"] = (sub["Latitude"] / CELL).round().astype(int)
sub["cell_lon"] = (sub["Longitude"] / CELL).round().astype(int)
cell_counts = (sub.groupby(["cell_lat", "cell_lon"]).size()
                 .reset_index(name="encampment_reports"))
cell_counts["center_lat"] = cell_counts["cell_lat"] * CELL
cell_counts["center_lon"] = cell_counts["cell_lon"] * CELL

# join crime counts per cell (2024-2025; violent + property categories)
VIOLENT = ["murder", "aggravated-assault", "robbery", "other-crimes-against-persons"]
PROPERTY = ["theft-from-motor-vehicle", "larceny", "auto-theft", "burglary", "arson"]
crime = pd.read_csv(os.path.join(HERE, "denver_crime_offenses.csv"), low_memory=False,
                    usecols=["OFFENSE_CATEGORY_ID", "FIRST_OCCURRENCE_DATE",
                             "GEO_LAT", "GEO_LON"])
crime["dt"] = pd.to_datetime(crime["FIRST_OCCURRENCE_DATE"], unit="ms",
                             errors="coerce")  # ArcGIS exports epoch ms
crime = crime[crime["dt"].dt.year.isin([2024, 2025])]
crime = crime[crime["OFFENSE_CATEGORY_ID"].isin(VIOLENT + PROPERTY)].dropna(
    subset=["GEO_LAT", "GEO_LON"])
crime["cell_lat"] = (crime["GEO_LAT"] / CELL).round().astype(int)
crime["cell_lon"] = (crime["GEO_LON"] / CELL).round().astype(int)
crime_cells = (crime.groupby(["cell_lat", "cell_lon"]).size()
                 .reset_index(name="violent_property_crimes"))
hot = cell_counts.merge(crime_cells, on=["cell_lat", "cell_lon"], how="left")
hot["violent_property_crimes"] = hot["violent_property_crimes"].fillna(0).astype(int)
hot = hot.sort_values("encampment_reports", ascending=False).reset_index(drop=True)
hot["rank"] = hot.index + 1
print("\nTop 10 hotspot cells (encampment reports 2024-25 + violent/property crimes):")
print(hot[["rank", "center_lat", "center_lon", "encampment_reports",
           "violent_property_crimes"]].head(10).to_string(index=False))
tot_enc = hot["encampment_reports"].sum()
print(f"\nTop 10 cells hold {hot['encampment_reports'].head(10).sum()/tot_enc:.1%} of all encampment reports")
print(f"Top 25 cells hold {hot['encampment_reports'].head(25).sum()/tot_enc:.1%} of all encampment reports")
hot.head(25).to_csv(os.path.join(HERE, "..", "phase2_data", "hotspot_top25.csv"),
                    index=False)

# ---- chart 10: hotspot map ----
fig, ax = plt.subplots(figsize=(8, 7))
sc = ax.scatter(hot["center_lon"], hot["center_lat"], c=hot["encampment_reports"],
                s=14, cmap="YlOrRd", alpha=0.75, edgecolors="none")
top10 = hot.head(10)
ax.scatter(top10["center_lon"], top10["center_lat"], s=90, facecolors="none",
           edgecolors="#1a1a1a", linewidths=1.2, label="Top 10 cells")
for _, r in top10.iterrows():
    ax.annotate(int(r["rank"]), (r["center_lon"], r["center_lat"]),
                fontsize=7, fontweight="bold", ha="center", va="center")
plt.colorbar(sc, ax=ax, label="Encampment 311 reports, 2024-2025")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("Where street-level disorder concentrates — Denver 311 encampment\n"
             "reports by ~500m grid cell, 2024-2025 (targeting input)", fontsize=11)
ax.legend(loc="lower right", fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS, "10_hotspot_map.png"), dpi=130)
plt.close()

print("\nCharts saved: 09_displacement_reappearance.png, 10_hotspot_map.png")
print("DISP", "; ".join(
    f"r={r[0]*1000:.0f}m/w={r[1]}d obs={r[2]:.4f} base={r[3]:.4f}" for r in disp_results))
print(f"TRI150 {obs_tri:.4f} OTH150 {obs_oth:.4f}")
