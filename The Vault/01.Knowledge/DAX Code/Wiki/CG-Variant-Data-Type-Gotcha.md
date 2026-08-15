---
created: 2026-08-08
updated: 2026-08-08
source: "Create calculation groups in Power BI"
source_url: https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups
note_type: gotcha
tags: [calculation-groups, variant-data-type, power-bi, dax]
---

# CG Variant Data Type Gotcha

When a calculation group is added to a semantic model, all existing measures automatically change to **variant** data type. Removing all calculation groups from the model reverts measures to their original data types.

## Expected Behaviour

You create a measure with a specific data type (e.g., Decimal Number). The measure is used in a dynamic format string on another measure. Everything works correctly.

## Actual Behaviour

As soon as a calculation group is added to the model, all measures in the model — including those unrelated to the calculation group — become **variant** data type. This breaks dynamic format string patterns where one measure references another measure's format string, showing an error instead.

## Why It Happens

Calculation groups introduce context-dependent evaluation for measures. The DAX engine can no longer guarantee a single, fixed data type for any measure that might be affected by a calculation item — hence the variant type. This is a Power BI engine behaviour, not a bug.

## How to Handle It

### Option 1 — FORMAT Function

Wrap the measure reference to force string recognition:

```dax
FORMAT([Dynamic format string], "")
```

The `FORMAT` function explicitly converts the variant measure to a string, bypassing the dynamic format string chain.

### Option 2 — DAX User-Defined Function

Define the dynamic format string expression as a DAX user-defined function instead of referencing a measure directly:

```dax
// User-defined function returning the format string
MyFormatString = "#,##0.00"

// Use the UDF in the calculation group
calculationItem 'YOY%'
    expression = ...
    formatStringExpression = MyFormatString
```

UDFs are not affected by the variant data type and can be used safely in format string expressions.

### Option 3 — Remove All Calculation Groups

If all CGs are removed, the variant type is automatically reverted. This is not a practical option in production.

## Related

- [[ISNUMERIC-Guard-Pattern-for-CG]] — companion gotcha for non-numeric measures in CGs
- [[dax-user-defined-functions-udfs]] — UDFs as the safe format string workaround
- [[Format-String-Expression-in-Calculation-Groups]] — format string in CG context
