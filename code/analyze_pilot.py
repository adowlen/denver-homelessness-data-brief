"""Phase 1 pilot analysis: Denver crime trends + 311 encampment reports.
Aggregates only; no individual-level output. Charts -> ../charts/.
"""
import os, re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(os.path.dirname(HERE), "charts")
os.makedirs(CH, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.grid": True, "grid.alpha": 0.3})

# ---------------- CRIME ----------------
print("loading crime...", flush=True)
c = pd.read_csv(os.path.join(HERE, "denver_crime_offenses.csv"), low_memory=False)
print("crime rows:", len(c))
c["occ"] = pd.to_datetime(c["FIRST_OCCURRENCE_DATE"], unit="ms", errors="coerce")
c = c[c["IS_CRIME"] == 1]
c["ym"] = c["occ"].dt.to_period("M")
c["year"] = c["occ"].dt.year
c["hour"] = c["occ"].dt.hour
c["dow"] = c["occ"].dt.day_name()

# NIBRS category-based grouping (OFFENSE_CATEGORY_ID values use dashes)
VIOLENT_CATS = {"murder", "aggravated-assault", "robbery", "other-crimes-against-persons"}
PROPERTY_CATS = {"theft-from-motor-vehicle", "larceny", "auto-theft", "burglary", "arson"}
def grp(cat):
    s = str(cat)
    if s in VIOLENT_CATS: return "Violent"
    if s in PROPERTY_CATS: return "Property"
    return "Other"
c["vtype"] = c["OFFENSE_CATEGORY_ID"].apply(grp)
# display-friendly offense group from type id (dashes -> readable)
c["crime_group"] = (c["OFFENSE_TYPE_ID"].fillna("").str.replace("-", " ")
                    .str.replace("mtr veh", "motor vehicle").str.title())

print("\n== top offense groups =="); print(c["crime_group"].value_counts().head(15))
print("\n== yearly totals =="); print(c.groupby("year").size())
print("\n== violent vs property by year ==")
vp = c.groupby(["year", "vtype"]).size().unstack(fill_value=0)
print(vp)

# Chart 1: monthly crime trend
m = c.groupby("ym").size()
fig, ax = plt.subplots(figsize=(11, 4.5))
ax.plot(m.index.astype(str), m.values, lw=1.2)
ax.set_title("Denver reported crimes per month (all offenses)")
ax.set_ylabel("incidents"); ax.tick_params(axis="x", rotation=60)
for lbl in ax.get_xticklabels()[::12]: lbl.set_visible(True)
fig.tight_layout(); fig.savefig(f"{CH}/01_monthly_crime_trend.png"); plt.close(fig)

# Chart 2: violent vs property yearly
fig, ax = plt.subplots(figsize=(8, 4.5))
vp[["Violent", "Property"]].plot(kind="bar", ax=ax)
ax.set_title("Violent vs property crimes per year (Denver)")
ax.set_ylabel("incidents"); ax.tick_params(axis="x", rotation=0)
fig.tight_layout(); fig.savefig(f"{CH}/02_violent_vs_property_yearly.png"); plt.close(fig)

# Chart 3: top offense groups
top = c["crime_group"].value_counts().head(12)
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.barh(top.index[::-1], top.values[::-1])
ax.set_title("Top offense groups, 2021–2026 YTD")
ax.set_xlabel("incidents")
fig.tight_layout(); fig.savefig(f"{CH}/03_top_offense_groups.png"); plt.close(fig)

# Chart 4: hour of day + day of week
fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))
c.groupby("hour").size().plot(kind="bar", ax=axes[0], color="steelblue")
axes[0].set_title("Crimes by hour of day"); axes[0].set_xlabel("hour")
dow_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
c.groupby("dow").size().reindex(dow_order).plot(kind="bar", ax=axes[1], color="darkorange")
axes[1].set_title("Crimes by day of week"); axes[1].tick_params(axis="x", rotation=45)
fig.tight_layout(); fig.savefig(f"{CH}/04_crime_time_patterns.png"); plt.close(fig)

# Chart 5: top neighborhoods
nh = c["NEIGHBORHOOD_ID"].value_counts().head(15)
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(nh.index[::-1], nh.values[::-1])
ax.set_title("Top 15 neighborhoods by reported crimes (2021–2026 YTD)")
ax.set_xlabel("incidents")
fig.tight_layout(); fig.savefig(f"{CH}/05_crime_by_neighborhood.png"); plt.close(fig)
print("\n== top neighborhoods =="); print(nh.head(10))

# perception checks
print("\n== violent crime: 2021 vs 2025 ==")
for y in sorted(c["year"].dropna().unique()):
    vy = c[(c["year"] == y) & (c["vtype"] == "Violent")].shape[0]
    py = c[(c["year"] == y) & (c["vtype"] == "Property")].shape[0]
    print(f"{int(y)}: violent={vy} property={py}")
print("\n== motor vehicle theft (auto-theft) by year ==")
print(c[c["OFFENSE_CATEGORY_ID"] == "auto-theft"].groupby("year").size())
print("\n== aggravated assault + robbery + murder by year ==")
print(c[c["OFFENSE_CATEGORY_ID"].isin(["aggravated-assault","robbery","murder"])].groupby("year").size())

# ---------------- 311 ENCAMPMENTS ----------------
print("\nloading 311 encampment files...", flush=True)
frames = []
for yr, fn in [(2022, "sr2022_encampment.csv"), (2023, "sr2023_encampment.csv")]:
    p = os.path.join(HERE, fn)
    if os.path.exists(p):
        d = pd.read_csv(p, low_memory=False)
        d["yr_src"] = yr
        # normalize underscore column names to the space style of the yearly CSVs
        d = d.rename(columns={c: c.replace("_", " ") for c in d.columns})
        # feature-service dates are epoch milliseconds
        for col in ["Case Created Date", "Case Closed Date"]:
            if col in d.columns and pd.api.types.is_numeric_dtype(d[col]):
                d[col] = pd.to_datetime(d[col], unit="ms", errors="coerce")
        frames.append(d); print(yr, len(d))
for yr, fn in [(2024, "sr2024.csv"), (2025, "sr2025.csv")]:
    p = os.path.join(HERE, fn)
    d = pd.read_csv(p, usecols=["Case Summary","Case Status","Case Created Date","Case Closed Date",
        "Longitude","Latitude","Council District","Police District","Agency","Case Source"],
        low_memory=False, encoding="cp1252")
    s = d["Case Summary"].fillna("")
    noise = s.str.startswith("[EXTERNAL]") | s.str.startswith("[BULK]") | s.str.startswith("Automatic reply")
    m = s.str.contains(re.compile(r"encamp(?!aign)|urban camping|homeless", re.I), na=False) & ~noise
    e = d[m].copy(); e["yr_src"] = yr
    frames.append(e); print(yr, "encampment rows:", len(e))
e311 = pd.concat(frames, ignore_index=True)
e311["created"] = pd.to_datetime(e311["Case Created Date"], errors="coerce")
e311["closed"] = pd.to_datetime(e311["Case Closed Date"], errors="coerce")
e311["ym"] = e311["created"].dt.to_period("M")
e311.to_csv(os.path.join(HERE, "encampment_311_2022_2025.csv"), index=False)
print("total encampment records:", len(e311))

# Chart 6: monthly encampment volume
em = e311.groupby("ym").size()
fig, ax = plt.subplots(figsize=(11, 4.5))
ax.plot(em.index.astype(str), em.values, lw=1.4, color="firebrick")
ax.set_title("311 encampment-related reports per month (2022–2025)")
ax.set_ylabel("reports"); ax.tick_params(axis="x", rotation=60)
ax.axvline("2023-07", color="gray", ls="--", lw=1)
ax.text("2023-07", ax.get_ylim()[1]*0.92, " All In Mile High\n launches ~mid-2023", fontsize=8, color="gray")
fig.tight_layout(); fig.savefig(f"{CH}/06_encampment_monthly.png"); plt.close(fig)

# Chart 7: yearly totals + status breakdown
ey = e311.groupby(e311["created"].dt.year).size()
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
ey.plot(kind="bar", ax=axes[0], color="firebrick")
axes[0].set_title("Encampment reports per year"); axes[0].tick_params(axis="x", rotation=0)
st = e311["Case Status"].value_counts().head(8)
axes[1].barh(st.index[::-1], st.values[::-1], color="teal")
axes[1].set_title("Resolution status (2022–2025)")
fig.tight_layout(); fig.savefig(f"{CH}/07_encampment_yearly_status.png"); plt.close(fig)
print("\n== encampment yearly =="); print(ey)
print("\n== encampment status =="); print(e311["Case Status"].value_counts().head(10))

# resolution times
res = (e311["closed"] - e311["created"]).dt.total_seconds() / 86400
res = res[(res >= 0)]
print(f"\nresolution days: n={res.notna().sum()} median={res.median():.1f} p90={res.quantile(.9):.1f} unclosed={e311['closed'].isna().mean()*100:.1f}%")

# Chart 8: encampment by council district — restrict to 2024-2025
# (2022/2023 feature-service records carry Council_District=0, i.e. unmapped)
cd_sub = e311[e311["created"].dt.year >= 2024]
cdist = pd.to_numeric(cd_sub["Council District"], errors="coerce").dropna()
cdist = cdist[cdist > 0].astype(int)
cd = cdist.value_counts().head(11)
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.bar([f"D{x}" for x in cd.index[::-1]], cd.values[::-1], color="darkgreen")
ax.set_title("Encampment reports by council district (2024–2025)")
ax.set_ylabel("reports")
fig.tight_layout(); fig.savefig(f"{CH}/08_encampment_by_district.png"); plt.close(fig)
print("\n== encampment by council district =="); print(cd)

print("\nANALYSIS COMPLETE")
