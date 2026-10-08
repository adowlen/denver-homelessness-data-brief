"""Download encampment-related 311 records for 2022-2023 (server-side filtered)."""
import csv, json, time, urllib.request, urllib.parse

BASE = "https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services"
FIELDS = ["ObjectId","Case_Summary","Case_Status","Case_Source","Case_Created_Date","Case_Closed_Date",
          "First_Call_Resolution","Incident_Zip_Code","Longitude","Latitude","Agency","Neighborhood",
          "Council_District","Police_District"]
# encampment signal in Case_Summary; exclude 'Campaign Information' false positive
WHERE = ("(UPPER(Case_Summary) LIKE '%ENCAMP%' AND UPPER(Case_Summary) NOT LIKE '%CAMPAIGN%')"
         " OR UPPER(Case_Summary) LIKE '%URBAN CAMPING%'"
         " OR UPPER(Case_Summary) LIKE '%HOMELESS%'")

def q(url, params):
    u = url + "?" + urllib.parse.urlencode(params)
    for a in range(5):
        try:
            with urllib.request.urlopen(u, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print(" retry", a, e, flush=True); time.sleep(2*(a+1))
    raise RuntimeError("failed")

for yr in (2022, 2023):
    svc = f"{BASE}/311_Service_Requests_{yr}/FeatureServer/0/query"
    n = q(svc, {"where": WHERE, "returnCountOnly": "true", "f": "json"})["count"]
    print(f"{yr}: {n} encampment records", flush=True)
    out = f"/home/hatch/workspace/goals/denver-homelessness-response-data-driven-accountability/hidden_files/data/sr{yr}_encampment.csv"
    PAGE = 1000; got = 0
    with open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(FIELDS)
        for off in range(0, n, PAGE):
            d = q(svc, {"where": WHERE, "outFields": ",".join(FIELDS), "returnGeometry": "false",
                        "orderByFields": "ObjectId", "resultOffset": off, "resultRecordCount": PAGE, "f": "json"})
            feats = d.get("features", [])
            for ft in feats:
                w.writerow([ft["attributes"].get(c) for c in FIELDS])
            got += len(feats)
            if off % 10000 == 0: print(f"  {yr} offset {off}: {got}/{n}", flush=True)
            if len(feats) == 0: break
    print(f"{yr} DONE: {got} rows -> {out}", flush=True)
