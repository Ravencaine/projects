---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# SAMPLECARTESIANPOINTSBYCOVER

Applies to: Calculated column Calculated table Measure Visual calculation Returns a sample subset from a Table that is obtained by plotting the rows as points in

## Syntax

```dax
SAMPLECARTESIANPOINTSBYCOVER(<Size>, <Table>, <XAxis>, <YAxis>[, <Radius>][, <MaxMinRatio>] [, <MaxBlankRatio>] )
```

## Return Value

Table Any DAX expression that returns a table of data from where to return a sample subset from. XAxis The numerical XAxis column from the Table. YAxis The numerical YAxis column from the Table. Radius (Optional) The numerical Radius column from the Table. MaxMinRatio (Optional) When Radius is speci