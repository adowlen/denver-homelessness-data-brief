"""Download Denver crime offenses from the city's ArcGIS Feature Service.
Source: City and County of Denver Open Data (ODC_CRIME_OFFENSES_P), owner The_City_and_County_of_Denver.
"""
import csv, json, sys, time, urllib.request, urllib.parse

SVC = "https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services/ODC_CRIME_OFFENSES_P/FeatureServer/324/query"
OUT = "/home/hatch/workspace/goals/denver-homelessness-response-data-driven-accountability/hidden_files/data/denver_crime_offenses.csv"

FIELDS = ["OBJECTID","INCIDENT_ID","OFFENSE_ID","OFFENSE_CODE","OFFENSE_CODE_EXTENSION",
          "OFFENSE_TYPE_ID","OFFENSE_CATEGORY_ID","FIRST_OCCURRENCE_DATE","LAST_OCCURRENCE_DATE",
          "REPORTED_DATE","INCIDENT_ADDRESS","GEO_LON","GEO_LAT","DISTRICT_ID","PRECINCT_ID",
          "NEIGHBORHOOD_ID","IS_CRIME","IS_TRAFFIC","VICTIM_COUNT"]

def q(params):
    url = SVC + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print(f"retry {attempt} offset={params.get('resultOffset')}: {e}", flush=True)
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("failed after retries")

# page size
info = q({"where":"1=1","returnCountOnly":"true","f":"json"})
total = info["count"]
print("total records:", total, flush=True)

PAGE = 2000
got = 0
with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(FIELDS)
    for offset in range(0, total, PAGE):
        d = q({"where":"1=1","outFields":",".join(FIELDS),"returnGeometry":"false",
               "orderByFields":"OBJECTID","resultOffset":offset,"resultRecordCount":PAGE,"f":"json"})
        feats = d.get("features", [])
        for ft in feats:
            a = ft["attributes"]
            w.writerow([a.get(c) for c in FIELDS])
        got += len(feats)
        print(f"offset {offset}: +{len(feats)} (total {got}/{total})", flush=True)
        if len(feats) < PAGE:
            break
print("DONE, wrote", got, "rows to", OUT)
