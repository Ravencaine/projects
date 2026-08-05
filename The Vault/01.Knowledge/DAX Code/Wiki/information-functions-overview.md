---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# Information Functions Overview

Information functions inspect the current context to determine what values, filters, or relationships are active.

| Function | Returns | Use Case |
|----------|---------|----------|
| `ISFILTERED` | TRUE if column has a direct filter | Check if a slicer is active |
| `ISCROSSFILTERED` | TRUE if column is filtered directly or through cross-filtering | Detect any filter propagation |
| `HASONEFILTER` | TRUE if column has exactly one direct filter | Check single-value filter |
| `HASONEVALUE` | TRUE if column has exactly one value in current context | Safe check before using VALUES |
| `ISINSCOPE` | TRUE if the column is in the grouping set of the current visual | Detect if column is being iterated |
| `ISBLANK` | TRUE if value is BLANK | Null checking |
| `ISERROR` | TRUE if expression returns an error | Error detection |
| `CONTAINS` | TRUE if a row exists with specified values | Table membership test |
| `LOOKUPVALUE` | Returns value from a related row (no relationship required) | VLOOKUP equivalent |
| `TABLEOF` | Returns the table of values currently in scope for a measure | New — preview |
| `NAMEOF` | Returns the qualified name of an object | New — preview |

## Notes

- ISFILTERED checks **direct** filters only; ISCROSSFILTERED checks both direct and cross-filtered
- HASONEVALUE and ISINSCOPE are safer than checking COUNTROWS(VALUES(...)) = 1 manually
- For single-value detection, `SELECTEDVALUE` is preferred over `HASONEVALUE + VALUES`

## Related

- [[selectedvalue]]
- [[values]]
- [[dax-context]]
