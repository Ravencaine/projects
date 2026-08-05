---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.Permutations

Returns the number of permutations that can be generated from a number of items, setSize, with a specified permutation size, permutationSize.

## Signature

```m
Number.Permutations(setSize as nullable number, permutationSize as nullable
number) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| setSize | nullable number | |
| permutationSize | nullable number | |

## Returns

nullable number

### Example 1

Find the number of permutations from a total of 5 items in groups of 3.

```m
Number.Permutations(5, 3)
```

// Output
```
60
```

