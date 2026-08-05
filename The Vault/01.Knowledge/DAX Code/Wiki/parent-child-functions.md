---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, parent-child]
---

# Parent-Child Functions: PATH, PATHITEM, PATHLENGTH

Work with self-referencing hierarchies where each row contains a reference to its parent row.

## PATH

Returns a delimited text string of ancestor IDs from the root to the current node.

## Signature

```dax
PATH(<child_column>, <parent_column>)
```

## Parameters

| Term | Definition |
|------|------------|
| `child_column` | Column containing the child's unique ID |
| `parent_column` | Column containing the parent's unique ID |

## Example

```
Employee | ManagerID | PATH(EmployeeKey, ManagerID)
---------|-----------|---------------------------
Alice    | (blank)  | "Alice"
Bob      | Alice    | "Alice|Bob"
Carol    | Bob      | "Alice|Bob|Carol"
Dave     | Bob      | "Alice|Bob|Dave"
```

## PATHITEM

Extracts a specific level from a PATH result.

```dax
-- Get the grandparent (2nd level from root)
Grandparent := PATHITEM(PATH(EmployeeKey, ManagerID), 2)

-- Get the immediate manager
Manager := PATHITEM(PATH(EmployeeKey, ManagerID), PATHLENGTH(PATH(EmployeeKey, ManagerID)) - 1)
```

## PATHLENGTH

Returns the number of levels in a PATH.

```dax
Depth := PATHLENGTH(PATH(EmployeeKey, ManagerID))
```

## Related Functions

| Function | Purpose |
|----------|---------|
| `PATHCONTAINS` | Returns TRUE if a descendant is in the PATH |
| `PATHITEM` | Extracts the Nth level from a PATH |
| `PATHLENGTH` | Returns the number of levels |
| `LOOKUPVALUE` | Can look up values at each level |

## Notes

- PATH uses `|` (pipe) as the delimiter by default
- PATH returns BLANK for root-level nodes (where child = parent)
- PATHLENGTH returns 1 for root nodes, 2 for children of root, etc.
- PATHITEM uses 1-based indexing from the root
- Useful for org charts, bill-of-materials, and geographic hierarchies
