---
created: 2026-08-09
updated: 2026-08-09
source: "5 Hidden Excel Formula Rules Every Pro Follows • My Online Training Hub"
note_type: atomic
tags: [excel, formulas, lambda, custom-functions, name-manager, let, modular-design]
---

# LAMBDA: Reusable Custom Functions via Name Manager

`LAMBDA` wraps a formula and turns it into a custom Excel function — no VBA, no add-ins. Save in Name Manager and use it like any built-in function across the workbook.

## Syntax

```
=LAMBDA(parameter1, parameter2, ..., expression)
```

## Pattern: LET + LAMBDA + Name Manager

**Step 1 — Write the formula with LET (using parameter names):**
```
=LET(
  eligible, AND(name<>"", status="Active"),
  rate, XLOOKUP(sales, CommTable[Sales Band], CommTable[Rate],, -1),
  sales * rate * eligible
)
```

**Step 2 — Wrap in LAMBDA (replace cell refs with parameter names):**
```
=LAMBDA(sales, name, status,
  LET(
    eligible, AND(name<>"", status="Active"),
    rate, XLOOKUP(sales, CommTable[Sales Band], CommTable[Rate],, -1),
    sales * rate * eligible
  )
)
```

**Step 3 — Save in Name Manager as `COMMISSION`.**

**Step 4 — Use anywhere in the workbook:**
```
=COMMISSION(D5, C5, E5)
```

## Why It's Powerful

- Non-technical users get a simple interface: `=COMMISSION(sales, name, status)`
- Logic is defined once, in one place — easy to update
- Works like a built-in function: autocomplete, argument hints, documentation
- Modular design: formula is separated from its invocation

## When to Use

- Any formula you use in more than 3 places
- Logic that non-formula users need to apply
- Complex calculations that should be centrally maintained

## Related

- [[Source-5-Hidden-Excel-Formula-Rules-Mynda-Treacy]] — source
- [[LET-Makes-Formulas-Readable]] — LAMBDA wraps LET; LET is the prerequisite
- [[Helper-Columns-Build-for-Humans]] — LAMBDA is the formula-level version of the helper column pattern
