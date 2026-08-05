---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: gotcha
tags: [power-bi, gotcha, relationship, null-values, date-column, power-query]
---

# Null Date Values Break P&L Relationships

When building the 1-to-Many relationships between the P&L Structure table and the Transactions table, the relationship validation will fail if the Transactions table contains null values in the Date column.

Power BI cannot establish a valid relationship when one side of the join contains nulls.

## Symptom

The relationship between Chart of Accounts[Account Code] and Transactions[Account Code] (or between P&L Structure and Transactions) fails to validate in the relationship view.

## Fix

1. Open **Power Query Editor**
2. Filter the **Date** column to remove null/blank values
3. Click **Close & Apply**
4. The relationship should now validate successfully

## Prevention

Filter the Date column during the Excel preparation stage (Stage 2 of the Xero pipeline). This is faster and cleaner than fixing it in Power Query after loading.

## Related

- [[pl-data-model-relationships]] — `pattern`
- [[xero-power-bi-pl-pipeline]] — `pattern`
