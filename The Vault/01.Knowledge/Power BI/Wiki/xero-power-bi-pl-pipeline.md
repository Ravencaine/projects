---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: pattern
tags: [power-bi, pattern, power-query, data-preparation, xero, excel, accounting]
---

# Xero-to-Power BI P&L Pipeline

End-to-end workflow for extracting financial data from Xero, preparing it in Excel, loading it into Power BI, and building a dynamic Profit & Loss report.

## Stage 1: Xero Data Extraction

### Chart of Accounts
1. Navigate to **Accounting** tab → **Chart of Accounts** under ACCOUNTING TOOLS
2. Export as **Excel Workbook** (.xlsx) — not CSV — to preserve data types
3. The Chart of Accounts is the master list of account codes and categories

### Transaction Data
1. Navigate to **Reporting** tab → **Account Transactions** (under FAVOURITE REPORTS)
2. Select **all accounts:** easier to filter in Excel later
3. Select the **13 core columns** (Date, Account Code, Account Name, Account Type, Description, Net, etc.)
4. Export as **Excel Workbook** (.xlsx)

### Pro Tip
Always save exports as **Excel Workbook (.xlsx)** not CSV — CSV defaults strip data type metadata.

## Stage 2: Excel — Data Preparation

1. Open Transaction Data file, **delete top 4 rows** of report metadata — headers must sit on row 1
2. Select all columns → **Data** tab → **Filter** to add filter arrows
3. Filter **Account Type** column to show only **Revenue** and **Expense** (P&L only)
4. Ensure **Date** column is formatted as Date type
5. Copy filtered data to a clean tab
6. Save and close

## Stage 3: Power BI — Load Data

1. Open Power BI Desktop → **Home** → **Excel Workbook** → select cleaned Transaction Data file
2. Confirm correct tab selected → **Load**
3. Repeat for **Chart of Accounts** file
4. You now have two tables loaded

## Stage 4: Create Mapping Tables

Via **Home** → **Enter Data**:

### P&L Section Mapping Table
Enter section names with a **Custom sort order** column. This controls the vertical flow: Revenue → Direct Costs → Gross Profit → Operating Expenses → Operating Profit → Net Profit.

### P&L Structure Table
Contains the full P&L line structure (each account mapped to its section). Acts as the row hierarchy in the Matrix visual.

**Result:** Four tables total in the model — Transactions, Chart of Accounts, Section Mapping, Structure.

## Related

- [[pl-mapping-table-pattern]] — `pattern`
- [[pl-dynamic-matrix-visual]] — `pattern`
- [[pl-styling]] — `pattern`
- [[pl-conditional-formatting]] — `pattern`
- [[pl-data-model-relationships]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
- [[dynamic-pl-measure]] — `function`
- [[ytd-kpi-measures-pl]] — `function`
- [[pl-null-date-break-relationships]] — `gotcha`
