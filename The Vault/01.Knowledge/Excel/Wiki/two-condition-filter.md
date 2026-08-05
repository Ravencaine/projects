---
created: 2026-07-31
updated: 2026-08-02
source: "🧠 Mastering Excel's Superpower FILTER, UNIQUE, SORT, and CHOOSE (a.k.a. Data Magic).md"
source_url: "https://medium.com/@markchen69/mastering-excels-superpower-filter-unique-sort-and-choose-a-k-a-data-magic-b5dbeeb02f0d"
note_type: pattern
tags: [excel, dynamic-arrays, filter, multi-condition]
---

# Two-Condition FILTER Pattern

Filters an array using two independent conditions combined with AND logic — like a SQL `WHERE` clause in a single formula.

## Purpose

When a simple column filter isn't enough and you need to apply multiple criteria simultaneously (e.g., "Status = Active" AND "Revenue > 10,000"), this pattern combines two boolean arrays into a single filter expression.

## Components

- `FILTER()` — returns only rows matching the combined condition
- `*` operator — multiplies boolean arrays (AND logic)
- `+` operator — adds boolean arrays (OR logic)

## Structure

**AND (both conditions must be true):**
```excel
=FILTER(<data_range>, (<condition1>)*(<condition2>))
```

**OR (either condition can be true):**
```excel
=FILTER(<data_range>, (<condition1>)+(<condition2>))
```

## Example

From a table with columns A (Name), B (Status), C (Revenue):

```excel
=FILTER(A2:C100, (B2:B100="Active")*(C2:C100>10000))
```

Returns all rows where Status is "Active" AND Revenue exceeds 10,000.

## Variations

**Three conditions — all AND:**
```excel
=FILTER(A2:D100, (B2:B100="Active")*(C2:C100>10000)*(D2:D100<>"Cancelled"))
```

**Mixed AND/OR:**
```excel
=FILTER(A2:C100, (B2:B100="Active")*((C2:C100>10000)+(C2:C100<100)))
```

**Add IFERROR for no-match fallback:**
```excel
=IFERROR(FILTER(A2:C100, (B2:B100="Active")*(C2:C100>10000)), "No matching records")
```

## Related

- [[filter-function-excel]] — `atomic` — FILTER function mechanics
- [[dynamic-dropdown-unique-sort-filter]] — `pattern` — FILTER in a dropdown context
- [[excel-data-validation]] — `pattern` — data validation patterns
