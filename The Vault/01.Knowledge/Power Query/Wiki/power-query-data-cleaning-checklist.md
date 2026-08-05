---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Data Cleaning Checklist Before Creating Dashboards 12 Essential Steps That Save Hours of Rework.md
note_type: pattern
tags: [power-query, pattern, data-cleaning, power-bi, data-quality, duplicate, trim, data-type]
---

# Power Query Data Cleaning Checklist (12 Steps)

A systematic 12-step data cleaning workflow to run in Power Query before building any Power BI dashboard. Prevents the category gotchas, numeric errors, and relationship bugs that surface in live stakeholder meetings.

## Step 1 — Remove Duplicate Records
Always inspect duplicates before removing — they may be legitimate updates. Create a duplicate count column first to understand why the data multiplied.

Fields to check for duplicates: Order IDs, Invoice Numbers, Customer IDs, Transaction IDs.

## Step 2 — Standardize Column Names
Rename from developer shorthand to human-readable labels:
- `Sales_Value_Final_v2_FINAL` → `Sales Amount`
- `Cust_Name1_copy` → `Customer Name`
- `Date_Updated_New_FIXED` → `Order Date`

Reduces DAX formula errors and makes the field pane navigable.

## Step 3 — Fix Data Types Immediately
Never trust automatic detection. Explicitly verify:
- Dates → **Date** type
- Prices → **Decimal Number**
- Unique IDs → **Text** (prevents ZIP codes from being summed)
- Percentages → **Percentage** format

Automatic detection may import numbers as text, causing alphabetical sorting ($10 before $2) and broken date filters.

## Step 4 — Handle Missing/Blank Values
Every blank must have a deliberate resolution. Options:
- Label as `"Unknown"` or `"Unassigned"`
- Remove the row entirely
- Replace with a default value (`0`)

A blank `Product Category` silently creates a phantom `"Blank"` category in your charts.

## Step 5 — Trim Spaces and Hidden Characters
Trailing spaces and non-printable characters are invisible to the human eye but break relationships and grouping in Power BI. Run **Trim** and **Clean** on all text columns before loading.

## Step 6 — Standardize Date Formats
Convert all date columns to a single consistent format before building visuals. Multi-source data often arrives with mixed formats (`05/06/2026` vs `June 5, 2026` vs `2026-06-05`). Also check for extreme anomalies (year 1900 or 2099).

## Step 7 — Validate Numeric Values
Use Power Query Column Distribution and profile statistics to check min/max values. Catch impossible outliers early:
- Negative sales amounts
- Age = 250
- Order Quantity = -5
- Discount percentage > 100

## Step 8 — Build Relationships Carefully
Before creating visuals, verify:
- Primary keys are truly unique
- Foreign keys actually match their lookup tables
- No uncontrolled many-to-many relationships
- Cross-filter direction set correctly

A relationship that "almost works" produces numbers that "almost look right" — the most dangerous class of error.

## Step 9 — Delete Unused Columns
Ruthless column removal:
1. Ask: will this column appear in a visual, filter, calculation, or relationship?
2. If no — drop it.

Unused columns inflate model size, slow refreshes, and clutter the field pane.

## Step 10 — Standardize Inconsistent Categories
Group typos and regional variants before loading:
- `USA` / `U.S.A.` / `United States` / `US` → `USA`
- `Male` / `M` → `Male`
- `Paid` / `payment complete` → `Paid`

Use **Replace Values** or **Group By** in Power Query.

## Step 11 — Test Aggregations in a Table First
Before designing visuals, verify core metrics in a simple Matrix/Table:
- Total Revenue matches source system
- Customer Count makes sense
- Average Order Value passes sanity check

If totals look wrong in a table, bar charts will not fix them.

## Step 12 — Create a Hidden Data Quality Page
Before the final dashboard, add a hidden tab monitoring data health:
- Total rows imported
- Count of blank/NULL critical fields
- Number of duplicate records
- Max/Min dates

Catches data corruption before end users notice it. See [[data-quality-page-pattern]].

## Related

- [[data-quality-page-pattern]] — `pattern`
- [[pre-dashboard-cleaning-checklist-reference]] — `reference`
