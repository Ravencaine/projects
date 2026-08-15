---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, graph, transitive-closure, hierarchy, network]
note_type: pattern

---

# Transitive Closure in DAX

Finding all reachable nodes in a network/hierarchy, even when direct relationships don't exist.

## Purpose

If A is related to B and B is related to C, transitive closure finds that A is related to C.

## Pattern

```dax
-- Requires a Parent-Child hierarchy table
-- Table has: NodeID, ParentID

Transitive Closure :=
VAR __StartNode = [SelectedNode]
VAR __Closure =
    UNION(
        { { __StartNode } },
        GENERATESERIES( 1, 100 )  -- max depth
    )
RETURN
-- Recursive pattern: for each depth, find children of current nodes
-- This requires a loop which DAX does not support natively
-- Use a supporting table built in Power Query for production use
```

## Notes

- DAX does not support recursion — transitive closure requires a pre-computed table
- Build the closure table in Power Query using a recursive function
- Use for organizational hierarchies, supply chain networks, bill-of-materials

## Related

- [[dax-index-pattern-deckler]]
- [[disconnected-tables-in-dax]]
