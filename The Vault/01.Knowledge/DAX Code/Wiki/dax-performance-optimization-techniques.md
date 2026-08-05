---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "performance", "optimization", "speed", "vertipaq"]
note_type: pattern

---

# DAX Performance Optimization Techniques

Practical methods for improving DAX query speed in large semantic models.

## 1. Use DIVIDE Instead of /

```dax
-- Slow: error on divide by zero, forces error handling into FE
Ratio := [A] / [B]

-- Fast: handled in SE, returns BLANK() instead of error
Ratio := DIVIDE( [A], [B] )
```

## 2. Prefer Simple Filters in CALCULATE

```dax
-- Faster: SE handles simple column filter
Total := CALCULATE( SUM( 'Sales'[Amount] ), 'Product'[Category] = "Electronics" )

-- Slower: FE handles complex expression
Total := CALCULATE( SUM( 'Sales'[Amount] ), [Margin] > 0.2 )
```

## 3. Avoid IF/SWITCH on Large Tables

```dax
-- Slower: FE evaluates IF for every row
Result := IF( [Sales] > 1000, "High", "Low" )

-- Faster: use a calculated column or disconnected table
Result := LOOKUPVALUE( 'Thresholds'[Label], 'Thresholds'[Min], [Sales] )
```

## 4. Use SUMMARIZECOLUMNS Instead of SUMMARIZE

```dax
-- SUMMARIZE includes non-aggregated columns, slower
-- SUMMARIZECOLUMNS is optimized for aggregation
Summary := SUMMARIZECOLUMNS( 'Date'[Year], "Sales", SUM( 'Sales'[Amount] ) )
```

## 5. Reduce Iterator Nesting

```dax
-- Slow: nested iterators
SUMX( 'Table1', SUMX( 'Table2', [Val] ) )

-- Better: pre-filter before iterating
SUMX( FILTER( 'Table1', [Condition] ), [Val] )
```

## Notes

- Profile with DAX Studio (Query Plan / Server Timings) before optimizing
- The biggest gains come from fixing data model issues, not DAX code
- VertiPaq compression settings (encodings) have more impact than DAX changes

## Related

- [[storage-engine-vs-formula-engine-in-dax]]
- [[performance-analyzer-debugging]]
