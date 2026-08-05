---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: gotcha
tags: [dax, gotcha, logical-operators, in, not-in, filter]
---

# NOT IN in DAX

DAX does not have a NOT IN operator. You must use the NOT function with the IN operator.

## The IN Operator

```dax
<value> IN {<value1>, <value2>, ...}
```

Returns TRUE if the value matches any value in the set.

```dax
[Color] IN {"Red", "Blue", "Green"}
```

## NOT IN Pattern

```dax
NOT <value> IN {<value1>, <value2>, ...}
```

```dax
-- NOT IN: Find customers NOT in the VIP set
FILTER(
    'Customer',
    NOT 'Customer'[CustomerKey] IN VALUES('VIPList'[CustomerKey])
)

-- Equivalent using NOT IN pattern with EXCEPT
EXCEPT(
    VALUES('Customer'[CustomerKey]),
    VALUES('VIPList'[CustomerKey])
)
```

## Common Uses

### Exclude specific values
```dax
-- Exclude certain product colors
FILTER(
    'Product',
    NOT 'Product'[Color] IN {"Black", "White"}
)
```

### Anti-join pattern (find items with no match in another table)
```dax
-- Customers with no orders
FILTER(
    'Customer',
    NOT 'Customer'[CustomerKey] IN VALUES('Sales'[CustomerKey])
)
```

### Combined with CALCULATE
```dax
Non VIP Sales =
CALCULATE(
    [Sales Amount],
    NOT 'Customer'[VIPFlag] IN {TRUE()}
)
```

## Performance Note

For large sets, EXCEPT may be faster than NOT IN with FILTER:

```dax
-- Using EXCEPT (often faster)
Non VIP Customers =
EXCEPT(
    ALL('Customer'),
    CALCULATETABLE('Customer', 'Customer'[VIPFlag] = TRUE())
)
```

## Related

- [[filter]]
- [[calculate]]
- 
