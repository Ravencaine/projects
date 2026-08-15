---
created: 2026-08-14
source: 4 ways to use error bars in Power BI - small feature, big impact.md
note_type: pattern
tags: [error-bars, data-flags, power-bi]
---

# Error Bar Data Flags

Add contextual vertical markers to a column chart that display summary labels at key positions (e.g., quarterly flags on a monthly chart).

## Purpose

Place summary information — labels, totals, annotations — at exact positions on a chart without cluttering the visual with extra tables or tooltips. Data flags anchor contextual data to the chart canvas, making it self-explanatory.

## Components

- **Monthly Max** — measure that returns the overall max value across all selected periods; controls flag height
- **Dummy0** — measure that always returns 0; used as the lower bound so the error bar starts at the baseline
- **Monthly Max - Start Quarter** — returns Monthly Max value only at the start of each quarter; controls where flags appear
- **Data Labels Value** — returns the quarter label (Q1, Q2 etc.) only at quarter starts; the main flag text
- **Data Labels Detail** — returns the quarter total formatted with separators; the detail line below the label

## Structure

### Measure: Monthly Max
```dax
Monthly Max = MAX( 'Table'[Likes] )
```

### Measure: Dummy0
```dax
Dummy0 = 0
```

### Measure: Monthly Max - Start Quarter
```dax
Monthly Max - Start Quarter =
VAR IsStartOfQuarter = DAY( MIN( 'Table'[Date] ) ) <= DAY( 'Table'[Date] )
RETURN
    IF( MONTH( 'Table'[Date] ) IN { 1, 4, 7, 10 }, [Monthly Max], BLANK() )
```

### Measure: Data Labels Value
```dax
Data Labels Value =
IF( MONTH( 'Table'[Date] ) IN { 1, 4, 7, 10 }, "Q" & QUOTIENT( MONTH( 'Table'[Date] ) - 1, 3 ) + 1, BLANK() )
```

### Measure: Data Labels Detail
```dax
Data Labels Detail =
VAR QuarterLikes = CALCULATE( SUM( 'Table'[Likes] ), ALLEXCEPT( 'Table', 'Table'[Year] ) )
RETURN
    IF( MONTH( 'Table'[Date] ) IN { 1, 4, 7, 10 }, FORMAT( QuarterLikes, "#,##0" ), BLANK() )
```

### Visual Setup
1. Clustered column chart: X-axis = Month, Y-axis series in order: Monthly Max, Likes, Monthly Max - Start Quarter
2. Set Monthly Max and Monthly Max - Start Quarter series transparency to 100%
3. Reduce series spacing to ~25% so the anchor series aligns with the data columns
4. Error bar on Monthly Max series: Type = By Field, Upper = `Monthly Max - Start Quarter`, Lower = `Dummy0`
5. Data labels on Monthly Max - Start Quarter series: Field = `Data Labels Value`, Detail = `Data Labels Detail`, Background = on

## Key Mechanism

Because `Monthly Max - Start Quarter` returns BLANK() for all non-quarter-start months, the error bar has nothing to draw — flags appear only where a value exists. No IF() inside the error bar config needed.

## Related

- [[Error-Bar-Rounded-Bars]]
- [[Error-Bar-Dumbbell-Chart]]
- [[Error-Bar-Boxplot]]
- [[Dummy0-Lower-Bound-Anchor]]
