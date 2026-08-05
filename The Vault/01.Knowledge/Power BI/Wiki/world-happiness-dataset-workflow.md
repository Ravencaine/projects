---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [world-happiness-report, csv, import, power-bi, dataset]
---

# World Happiness Dataset Import Workflow

Import the World Happiness Report CSV into Power BI and split into full and year-filtered queries.

## Prerequisites

- Power BI Desktop
- URL: `https://raw.githubusercontent.com/PacktPublishing/Artificial-Intelligence-with-Power-BI/main/Chapter02/world-happiness-report.csv`

## Steps

1. Go to **Get Data** → **Text/CSV**
2. Navigate to the downloaded `world-happiness-report.csv` file
3. In the preview pop-up:
   - Verify **Delimiter** = Comma
   - Confirm column headers are detected correctly
4. Select **Load** or **Transform Data**
5. In Power Query Editor:
   - Rename the query: `world-happiness-all`
   - **Duplicate** the query: right-click → Duplicate → name it `world-happiness-2019`
   - Apply a filter on the Year column = 2019 in the duplicate query
6. Close and Apply

## Variations

- Import directly into Power BI Service if the file is stored in OneDrive or SharePoint
- For GitHub-hosted CSVs, download first then import locally

## Related

- [[exploratory-data-analysis-eda-workflow]]
- [[data-profiling-column-quality-distribution-profile]]
