---
created: 2026-08-13
source: How to Build a Clean P&L in Power BI
note_type: pattern
tags: [power-bi, workflow, financial-reporting, p&l, xero, excel, power-query, data-preparation]
---

# P&L Dashboard Build: Xero → Excel → Power BI End-to-End

<!-- Full end-to-end pipeline for building an executive P&L dashboard from Xero accounting data through Excel preparation to a published Power BI report. -->

## Overview

Three-stage pipeline: extract from Xero → clean/prepare in Excel → model and visualise in Power BI.

```
Xero (raw ledger)
  → Excel (Chart of Accounts + Transaction Data, cleaned)
  → Power BI (mapping tables + DAX measures + matrix visual)
  → Executive P&L Dashboard
```

## Stage 1 — Xero Data Extraction

### Chart of Accounts
1. Accounting → Chart of Accounts → Export as Excel workbook
2. Contains: account codes, names, categories

### Transaction Data
1. Reporting → Account Transactions → select all accounts
2. Select 13 core columns (or add as needed)
3. Export as Excel workbook

```
Columns needed:
Date, Contact, Account Code, Account Type, Description,
Net, GST, Total, Currency, Exchange Rate,
Region, Tracking Name 1, Tracking Name 2
```

**Pro tip:** Save as `.xlsx` (not `.csv`) to preserve data types.

## Stage 2 — Excel Data Preparation

1. Delete top 4 rows of report metadata → headers on row 1
2. Apply Filter on all columns
3. Filter Account Type to show Revenue + Expense only
4. Ensure Date column is formatted as Date type
5. Copy filtered data to a clean tab
6. Save and close

## Stage 3 — Power BI Data Model

### Load Data
1. Load Transaction Data Excel file → `Transactions` table
2. Load Chart of Accounts Excel file → `ChartOfAccounts` table

### Create Mapping Tables (Enter Data)

**Table 1: P&L Section Mapping**
```
Section Name | Custom Sort Order
Revenue      | 1
Cost of Sales | 2
Gross Profit | 3
Expenses     | 4
Net Profit   | 5
```

**Table 2: P&L Structure**
Full account-level structure with Section + Account Name + Sort Order, matching the chart of accounts.

**Final model: 4 tables**
```
ChartOfAccounts   — account master data
Transactions      — raw transaction data
PLSectionMapping — section names + sort
PLStructure      — full account hierarchy
```

### Relationship
```
ChartOfAccounts[Code]  1──∞  Transactions[Account Code]
PLSectionMapping[Section Name]  1──∞  PLStructure[Section]
PLStructure[Account Name]  1──∞  Transactions[Account Name]
```

### Sort the P&L Section Mapping Table
Sort the Section column by the Custom sort order column so the P&L flows Revenue → Gross Profit → Expenses → Net Profit.

## Dynamic P&L Measure

```dax
Dynamic P&L =
VAR CurrentSection = MAX('PLStructure'[Section])
VAR CurrentAccount = MAX('PLStructure'[Account])
RETURN
SWITCH(
    TRUE(),
    -- Subtotals
    CurrentSection = "Revenue",          CALCULATE(SUM(Transactions[Total]), Transactions[Account Type] = "Revenue"),
    CurrentSection = "Cost of Sales",   CALCULATE(SUM(Transactions[Total]), Transactions[Account Type] = "Cost of Sales"),
    CurrentSection = "Expenses",        CALCULATE(SUM(Transactions[Total]), Transactions[Account Type] = "Expense"),
    -- Account-level detail
    NOT(ISBLANK(CurrentAccount)),       CALCULATE(SUM(Transactions[Total]), Transactions[Account Name] = CurrentAccount)
)
```

## Matrix Visual Configuration

```
Rows:     PLStructure[Section] → PLStructure[Account Name]
Columns:  Transactions[Date] → Year (or Month/Year hierarchy)
Values:   Dynamic P&L measure
```

**Tip:** Switch Date from day-by-day hierarchy to Year or Month/Year to prevent horizontal overflow.

**Fix blank rows:** Right-click row field → toggle Show items with no data against Section.

## Related

- [[matrix-cash-flow-pl-report-workflow]] — Matrix visual for financial reports (different source, different angle)
