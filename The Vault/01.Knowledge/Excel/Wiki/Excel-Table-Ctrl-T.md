---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, table, ctrl+t, structured-reference, auto-expand, pivot-table]
---

# Excel Table: Ctrl+T

Pressing Ctrl+T converts a plain range into an **Excel Table** — adding filter dropdowns, auto-expanding formulas, named range creation, and clean row shading automatically.

## Steps

1. Select any cell in the data range
2. Press **Ctrl + T**
3. Confirm the range and check "My table has headers"
4. Click **OK**

## What You Get

| Feature | Detail |
|---------|--------|
| Filter dropdowns | Auto-added to every column header |
| Auto-expanding formulas | Adding a row extends structured references automatically |
| Named table | The table gets a name (Table1, Table2…) in the Name Manager |
| Row shading | Alternating row colours (auto-applied, customisable) |
| Header freezing | Headers stay visible when scrolling |
| Total row | Optional total row with dropdown aggregation functions |

## Auto-Expand Formula Example

If column E has `=SUM(Table1[Amount])` and you add a new row to the table, the formula extends to include the new row — no manual range adjustment needed.

## Named Table in Formulas

```excel
=SUM(Table1[Amount])          -- structured reference
=SUMIF(Table1[Region],"West",Table1[Amount])  -- structured reference
```

Structured references update if column names change, unlike cell ranges like `A:A`.

## When to Use

- Any dataset that will grow (append rows regularly)
- Data that feeds Pivot Tables or Power Query
- Data that will be used in Power BI (Excel Tables are recognised as a table source)

## When Not to Use

- One-off calculations on static data
- Data that will be converted to Power Query — use a native Excel Table as the source, then transform in PQ

## Related

- [[Text-to-Columns]] — preparing messy columns before converting to Table
- [[Data-Validation-Dropdown]] — applying Data Validation after creating the Table
