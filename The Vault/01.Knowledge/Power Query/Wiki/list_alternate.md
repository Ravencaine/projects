---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.Alternate

Returns a list comprised of all the odd numbered offset elements in a list. Alternates between taking and skipping values from the list list depending on the parameters. count: Specifies number of values that are skipped each time. repeatInterval: An optional repeat interval to indicate how many values are added in between the skipped values. offset: An option offset parameter to begin skipping the values at the initial offset.

## Signature

```m
List.Alternate(
list as list,
count as number,
optional repeatInterval as nullable number,
optional offset as nullable number
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| count | number | |
| optional repeatInterval | nullable number | |
| optional offset | nullable number | |

## Returns

list

### Example 1

Create a list from {1..10} that skips the first number.

```m
List.Alternate({1..10}, 1)
```

// Output
```
{2, 3, 4, 5, 6, 7, 8, 9, 10}
```

### Example 2

Create a list from {1..10} that skips every other number.

```m
List.Alternate({1..10}, 1, 1)
```

// Output
```
{2, 4, 6, 8, 10}
```

### Example 3

Create a list from {1..10} that starts at 1 and skips every other number.

```m
List.Alternate({1..10}, 1, 1, 1)
```

// Output
```
{1, 3, 5, 7, 9}
```

### Example 4

Create a list from {1..10} that starts at 1, skips one value, keeps two values, and so on.

```m
List.Alternate({1..10}, 1, 2, 1)
```

// Output
```
{1, 3, 4, 6, 7, 9, 10}
```

