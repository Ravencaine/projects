---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, text-to-columns, delimiter, split, comma, pipe, power-query]
---

# Text to Columns

Data → Text to Columns splits a single column of text into multiple columns using a delimiter (comma, space, pipe `|`) or a fixed width — converting a packed cell like `John Smith | Sales | Texas` into separate columns.

## Steps

1. Select the column
2. Go to **Data → Text to Columns**
3. Choose **Delimited** (most common) or **Fixed Width**
4. Select the delimiter(s): Comma, Space, Tab, Semicolon, Other (`|` for pipe-delimited data)
5. Set the destination column
6. Click **Finish**

## Delimiter Examples

| Delimiter | Input | Output columns |
|----------|-------|---------------|
| Comma `,` | `John,Smith,USA` | John / Smith / USA |
| Space ` ` | `John Smith` | John / Smith |
| Pipe `|` | `John Smith \| Sales \| Texas` | John Smith / Sales / Texas |
| Tab | (imported from database) | auto-split |

## When to Use

- CSV files where delimiters were not split on import
- Reports that combine multiple fields in one column (e.g., name + department + region packed together)
- Pipe-delimited exports from legacy systems

## Power Query Equivalent

In Power Query, split by delimiter using **Split Column → By Delimiter:** this is repeatable and preserves the transformation for future refreshes.

```
Home → Split Column → By Delimiter
```

## Limitations

- Text to Columns is a one-time transformation — the result is static values, not formulas
- For repeatable splits, use Power Query instead
- Splitting by space splits on ALL spaces, not just specific ones — use "Treat consecutive delimiters as one" option to avoid empty columns

## Related

- [[Excel-Table-Ctrl-T]] — convert the result into an Excel Table after splitting
- [[Flash-Fill-Ctrl-E]] — alternative for pattern-based extraction rather than delimiter-based split
