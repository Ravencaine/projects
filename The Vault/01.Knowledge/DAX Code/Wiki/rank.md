---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# RANK

Returns the ranking for the current context within the specified partition, sorted by the specified order. If a match cannot be found, the rank is blank.

## Syntax

```dax
RANK ( [<ties>][, <relation>][, <orderBy>][, <blanks>][, <partitionBy>][, <matchBy>][, <reset>] )
```

## Parameters

| Term | Definition |
|------|------------|
| `ties` | (Optional) Defines how to handle ties — DENSE (no gaps) or SKIP (default — next rank skips). |
| `relation` | (Optional) A table expression from which the output row is returned. |
| `orderBy` | (Optional) An ORDERBY() clause defining how each partition is sorted. |
| `blanks` | (Optional) How to handle blank values when sorting: BLANKS DEFAULT or BLANKS FIRST. |
| `partitionBy` | (Optional) A PARTITIONBY() clause defining partitions. |
| `matchBy` | (Optional) A MATCHBY() clause defining how to match rows. |
| `reset` | (Optional) Defines when the rank resets within a visual calculation. |

## Return Value

An integer representing the rank of the current row within its partition.

## Remarks

Newer than RANK.EQ — supports ties parameter, relation/axis parameter for visual calculations, and blank handling. See RANK.EQ for the simpler form.