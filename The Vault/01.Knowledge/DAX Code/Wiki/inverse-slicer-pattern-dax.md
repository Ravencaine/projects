---

created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, pattern, slicer, not, filter, disconnected-table]

---

# NOT / Inverse Slicer Pattern in DAX

A NOT slicer filters OUT the values selected in the slicer, rather than keeping them. This is the inverse of standard slicer behavior and is built using a disconnected table and a DAX measure.

## Purpose

Standard slicers include only selected values. A NOT slicer excludes selected values — useful for "show everything except X" scenarios where the exclusion set changes dynamically based on user selection.

## Structure

**Step 1 — Create the disconnected table:**

```dax
Categories = DISTINCT( 'Products'[Category] )
```

**Step 2 — Create the NOT Selector measure:**

```dax
NOT Selector =
VAR __Category = MAX( 'Products'[Category] )
VAR __Categories = DISTINCT( 'Categories'[Category] )
VAR __Result = IF( __Category IN __Categories, BLANK(), 1 )
RETURN __Result
```

**Step 3 — Add the measure to the Table visual's Visual Level Filters and set it to Show items when the value is 1.**

## Example

With a `Categories` disconnected table driving a Slicer visual, selecting "AB" and "BB" in the slicer excludes those categories from the Table visual — showing only products not in the selected categories.

## Extended: NOT Aggregator

```dax
NOT Aggregator =
VAR __Categories = DISTINCT( 'Categories'[Category] )
VAR __Table = FILTER( 'Products', NOT( [Category] IN __Categories ) )
VAR __Result = SUMX( __Table, [Value] )
RETURN __Result
```

This aggregates values for rows whose category is NOT in the slicer selection.

## Notes

- The measure returns `BLANK()` for included rows and `1` for excluded rows. The Visual Level Filter then shows only rows returning `1`.
- This is a specific case of the more general Complex Selector pattern using disconnected tables.

## Related

- [[disconnected-tables-in-dax]]
- [[and-slicer-multi-select-dax]]
