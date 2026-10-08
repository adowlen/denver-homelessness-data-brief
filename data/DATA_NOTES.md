# Data notes — Phase 1 pilot (downloaded 2026-10-08)

All data is public, aggregate, and published by the City and County of Denver.
No individual-level or personal information is used. Analysis audits the SYSTEM,
never identifies vulnerable individuals.

## 1. Crime incidents — `denver_crime_offenses.csv`
- **Source**: City and County of Denver Open Data, "Crime" (Denver Police Department).
  Denver's old Socrata portal (data.denvergov.org) was retired; the dataset now lives
  on the city's ArcGIS Hub as Feature Service `ODC_CRIME_OFFENSES_P`.
- **Service URL**: https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services/ODC_CRIME_OFFENSES_P/FeatureServer/324/query
- **Item**: https://www.arcgis.com/sharing/rest/content/items/16d9c82bb36c4475bf87189cfaed653c
- **Coverage**: rolling ~5 prior calendar years + year-to-date (NIBRS format).
  Downloaded 2026-10-08: **382,746 records**, Jan 2021 → Oct 2026 YTD.
- **Key fields**: OFFENSE_TYPE_ID, OFFENSE_CATEGORY_ID, FIRST_OCCURRENCE_DATE,
  REPORTED_DATE, INCIDENT_ADDRESS (block-level, e.g. "100 BLOCK OF..."), GEO_LON/GEO_LAT,
  DISTRICT_ID, PRECINCT_ID, NEIGHBORHOOD_ID, IS_CRIME, IS_TRAFFIC, VICTIM_COUNT.
- **Update cadence**: weekdays (Mon–Fri) per the city's description.
- **Known gaps**: reporting lag (recent weeks incomplete); unfounded reports excluded;
  addresses are block-level only; NIBRS categorization changes can break long trends.

## 2. 311 service requests
Denver publishes 311 data two ways: (a) a rolling-12-month Feature Service
(`ODC_service_requests_311`, table 53, 395,257 records — NOTE: its Type/Topic/Division/
Major_Area fields are almost entirely NULL; only Case_Summary/Agency/Status are usable),
and (b) yearly archives. We used the yearly archives.

- **2025** (`sr2025.csv`, 451,943 rows): https://www.arcgis.com/sharing/rest/content/items/5bdb9b3033d74782a4c410e548887ede/data
- **2024** (`sr2024.csv`): https://www.arcgis.com/sharing/rest/content/items/79f43c95bf9a4ac19ef8217c5367e6c4/data
- **2023** (`sr2023_encampment.csv`, encampment-filtered server-side, 474,695 total records in source):
  https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services/311_Service_Requests_2023/FeatureServer
- **2022** (`sr2022_encampment.csv`, encampment-filtered server-side, 421,008 total records in source):
  https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services/311_Service_Requests_2022/FeatureServer
- **Encampment filter** (applied to Case_Summary): contains ENCAMP (excluding CAMPAIGN),
  URBAN CAMPING, or HOMELESS. 2022/2023 filtered server-side via WHERE clause;
  2024/2025 filtered locally with the same logic.
- **Encoding note**: yearly CSVs are Windows-1252 encoded (smart quotes); read with
  encoding='cp1252'.
- **Key fields**: Case_Summary, Case_Status, Case_Source, Case_Created_Date,
  Case_Closed_Date, Agency, Neighborhood, Council_District, Police_District,
  Longitude/Latitude.
- **Known gaps**: 311 volume reflects *reporting behavior* as well as ground truth
  (awareness campaigns and app changes move the numbers); Case_Summary is a terse
  clerk-entered code, not a verified outcome; "Closed" statuses do not all mean
  the underlying issue was resolved (e.g. "Closed - Transferred to External Agency").

## 3. Context (not downloaded; from published reports)
- Denver Auditor "City Shelters" audit (2024) + follow-up (May 2026): ~$149.6M shelter
  spending Jan 2022–Mar 2024 untracked per-shelter; security recommendations unimplemented.
- Denver Auditor All In Mile High audit (Mar 2026): $178.1M actual vs $158M reported
  (Jul 2023–Jun 2025); 38% of sampled invoices missing documentation; dashboard
  redesigned Apr 2025 removing deaths/jail placements/returns-to-street.
- HUD Point-in-Time counts: one-night January snapshots; widely considered an undercount;
  NOT downloaded in this pilot (Phase 2).
