---
created: 2026-07-26
source: dax.pdf
note_type: gotcha
tags: [dax, gotcha, filter, performance]
---

# Avoid Using FILTER as Filter Argument

Using FILTER as a CALCULATE filter argument is a common mistake that hurts performance.

## Expected Behaviour

Passing a filter expression directly to CALCULATE as a Boolean or table argument, expecting it to filter rows.

## Actual Behaviour

FILTER creates a full table scan over the filtered table every time CALCULATE evaluates. In import models, this is slower than using a Boolean expression, which the column store can optimise.

## Why It Happens

FILTER is an iterator — it loops over every row in the table. CALCULATE with a Boolean expression leverages the in-memory column store's internal optimisations. FILTER bypasses these optimisations.

## How to Handle It

```dax
-- WRONG: FILTER as filter argument (slower)
RedSales := CALCULATE(
    [Sales],
    FILTER('Product', 'Product'[Color] = "Red")
)

-- CORRECT: Boolean expression (faster)
RedSales := CALCULATE(
    [Sales],
    'Product'[Color] = "Red"
)
```

**Use FILTER** only when the filter cannot be expressed as a Boolean:
- Complex row-level conditions
- Filtering on aggregated values
- Conditions that require iterating over rows

```dax
-- FILTER is needed: filter to products with above-average sales
HighMarginProducts := CALCULATE(
    [Sales],
    FILTER(
        'Product',
        [Sales] > AVERAGE('Product'[Sales])
    )
)
```

## Related Gotchas

- [[avoid-converting-blanks-to-values]] — related to measure design
- [[calculate]] — function
- [[filter]] — function
