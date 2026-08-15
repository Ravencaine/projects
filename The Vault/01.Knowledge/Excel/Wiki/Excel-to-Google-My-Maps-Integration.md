---
created: 2026-08-10
updated: 2026-08-10
source: "Google Maps took my Excel spreadsheet to the next level with this little-known tool"
source_url: "https://www.howtogeek.com/microsoft-excel-google-my-maps/"
note_type: workflow
tags: [excel, workflow, google-my-maps, data-prep, geocoding, visualization, integration]
---

# Excel to Google My Maps Integration

Turn an Excel location dataset into an interactive map with custom markers, layers, and shareable links.

## Use Case

- Location datasets (addresses, stadiums, customer visits, trip planning) are harder to read as tables than as map pins
- Excel 3D Maps is an alternative but requires staying inside Excel
- Google My Maps provides a free, shareable, no-code alternative

## Prerequisites

- Google account with access to [google.com/mymaps](https://google.com/mymaps)
- Excel workbook with one sheet of location data
- At minimum: city + country for each row; full addresses preferred for accuracy

## Excel Data Preparation

**Requirements:**
- All data on a single worksheet (one map layer = one sheet)
- Distinct column headers in row 1 — these become the field names Google uses during import
- One row per location
- Sufficient address detail: city + country is often enough; full street address reduces geocoding ambiguity

**Recommended column layout:**
| Stadium | Address | City | State | Country |
|---------|---------|------|-------|---------|

Save as `.xlsx` (Google My Maps reads XLSX, not legacy `.xls`).

## Step-by-Step

### Step 1 — Create the Map

1. Open [google.com/mymaps](https://google.com/mymaps)
2. Click **Create a New Map**
3. Click **Import** under the untitled layer
4. Drag the `.xlsx` file into the import box, or click **Browse** to select it

### Step 2 — Map Columns to Fields

Google asks two questions:

1. **Location columns:** Check the boxes for all columns that define location (Address, City, State, Country). Click **Continue**.
2. **Marker names:** Select the single column to use for labeling each pin (e.g., Stadium). Click **Finish**.

Entries appear as pins on the map.

### Step 3 — Style the Pins

1. Click the **paint bucket** icon next to **All items**
2. Change colour and icon shape for all pins at once
3. To style by category: click an individual pin → **Edit** → choose a different colour or icon
4. Example: soccer-ball icon for stadium pins

### Step 4 — Add Details to Individual Pins

With a pin selected, click the **info card** to:
- View all imported fields
- Add an image or video
- Get directions to that location
- Delete the pin

### Step 5 — Switch Base Map Style

Click **Base map** → select **Terrain** to show topography around venues (optional).

### Step 6 — Share the Map

1. Click the map title to rename it
2. Click **Share**
3. Enable **Anyone with this link can view** for a public URL
4. Optionally enable public searchability
5. Click **Copy Link** to share, or use **Share on Drive** for access control

## Adding Layers

Each Excel file = one layer. To add more:

1. Click **Add layer**
2. Import the second Excel file
3. Repeat the column mapping steps
4. Toggle layers on/off with the checkbox

Layer names default to the filename — name files clearly before importing.

## Updating the Map

Changes to the local Excel file **do not** automatically update the map.

**To edit inside My Maps:**
1. Click **three dots** next to the layer name
2. Select **Open data table**
3. Click any cell to edit; right-click a row to delete or insert

**To reimport updated Excel data:**
1. Click **three dots** next to the layer name
2. Select **Reimport and merge**
3. Follow the prompts — existing pin positions are matched by content

## Limitations

- No native Excel sync — reimport required for Excel changes
- Custom labels can conflict with Google's default map labels
- Permissions are URL-based — no granular per-layer access control
- Mobile editing is limited compared to desktop

## Related

- [[Source-Google-Maps-Excel-Integration-Tony-Phillips]] — source
