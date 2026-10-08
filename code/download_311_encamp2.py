"""Download encampment-related 311 records for 2022-2023. Page until empty; verify counts."""
import csv, json, time, urllib.request, urllib.parse

BASE = "https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services"
FIELDS = ["ObjectId","Case_Summary","Case_Status","Case_Source","Case_Created_Date","Case_Closed_Date",
          "First_Call_Resolution","Incident_Zip_Code","Longitude","Latitude","Agency","Neighborhood",
          "Council_District","Police_District"]
WHERE = ("(UPPER(Case_Summary) LIKE '%ENCAMP%' AND UPPER(Case_Summary) NOT LIKE '%CAMPAIGN%')"
         " OR UPPER(Case_Summary) LIKE '%URBAN CAMPING%'"
         " OR UPPER(Case_Summary) LIKE '%HOMELESS%'")

def q(url, params):
    u = url + "?" + urllib.parse.urlencode(params)
    for a in range(6):
        try:
            with urllib.request.urlopen(u, timeout=120) as r:
                d = json.load(r)
            if "error" in d:
                raise RuntimeError(d["error"])
            return d
        except Exception as e:
            print(f"  retry {a}: {str(e)[:120]}", flush=True)
            time.sleep(3 * (a + 1))
    raise RuntimeError("failed after retries")

for yr in (2022, 2023):
    svc = f"{BASE}/311_Service_Requests_{yr}/FeatureServer/0/query"
    out = f"/home/hatch/workspace/goals/denver-homelessness-response-data-driven-accountability/hidden_files/data/sr{yr}_encampment.csv"
    PAGE = 1000; off = 0; got = 0
    with open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(FIELDS)
        while True:
            d = q(svc, {"where": WHERE, "outFields": ",".join(FIELDS), "returnGeometry": "false",
                        "orderByFields": "ObjectId", "resultOffset": off, "resultRecordCount": PAGE, "f": "json"})
            feats = d.get("features", [])
            if not feats:
                break
            for ft in feats:
                w.writerow([ft["attributes"].get(c) for c in FIELDS])
            got += len(feats); off += len(feats)
            if off % 5000 == 0 or len(feats) < PAGE:
                print(f"  {yr}: {got} rows so far", flush=True)
            if len(feats) < PAGE:
                break
    print(f"{yr} DONE: {got} rows -> {out}", flush=True)
