---
title: "Power BI Visual DAX: Advanced Tricks for Smarter Report Design"
source: "https://databear.com/power-bi-visual-dax/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-03-19
created: 2026-08-04
description: "Enhance your Power BI reports with visual DAX: row numbers, moving averages, and advanced tricks using visual calculations."
Processed: "Unprocessed"
---
**Power BI visual DAX** opens up a new way to create powerful, row‑level calculations directly inside table and matrix visuals without cluttering your model with extra measures. In this post, you’ll learn how to use visual calculations to add row numbers, handle totals, create moving averages, and apply advanced logic beyond the standard dropdown options.

##### Turning On Visual Calculations

Before you begin, make sure visual calculations are enabled:

1. Go to **File > Options and settings > Options**
2. Open the **Preview features** tab
3. Turn on **Visual calculations**
4. Restart Power BI Desktop if required

Once enabled, you’ll see a new **Visual calculation** button in the **Home** tab when a visual is selected. This opens the editor to define a new visual calculation.

##### Trick 1 Adding Row Numbers to a Matrix or Table

Often, you want a simple index like 1, 2, 3 for rows. Instead of building complex measures, use the built‑in `ROW_NUMBER()` function.

1. Select your matrix or table visual
2. Click **Visual calculation > New**
3. Name the calculation (e.g., `Index`)
4. Enter:
	```
	= ROW_NUMBER()
	```

Now the visual displays sequential row numbers.

##### Resetting Per Group

If you want the row numbers to reset for each group (e.g., each year), provide a grouping column:

```
= ROW_NUMBER([Year])
```

This restarts the count with each year.

##### Formatting the Index

Use column formatting options to show integers (no decimals) for clean display.

##### Trick 2 Handling Totals with IS\_AT\_LEVEL\<img decoding="async" class="aligncenter wp-image-49140 size-full" src="https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-215235.png" alt="Handling Totals with IS\_AT\_LEVEL" width="804" height="551" srcset="https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-215235.png 804w, https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-215235-300x206.png 300w, https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-215235-150x103.png 150w" sizes="(max-width: 804px) 100vw, 804px" />

Sometimes the totals row shouldn’t show row numbers or summaries. The `IS_AT_LEVEL()` function comes in handy:

```
IF(
    IS_AT_LEVEL([Quarter]),
    ROW_NUMBER([Year]),
    BLANK()
)
```

This shows the row number only when the context is at the Quarter level hiding it at total rows.

##### Trick 3 Simple Moving Averages

Calculating moving averages can be complex with DAX measures. With visual calculations:

1. Create a new visual calculation called `MOV AVG`
2. Use the `MOVING_AVERAGE()` function:
	```
	= MOVING_AVERAGE([Total Sales], 2)
	```

This calculates a 2‑period moving average.

##### Excluding Current Period

To average only previous values:

```
= MOVING_AVERAGE([Total Sales], 2, FALSE)
```

##### Resetting Averages by Year

To reset the window each year:

```
= MOVING_AVERAGE([Total Sales], 2, TRUE, [Year])
```

This ensures rolling averages don’t mix data across years.

##### Trick 4 Using the ROWS() Operator

The `ROWS()` operator references the *entire set* of visual rows (excluding totals). This is useful if you want to compute something like the overall maximum across the visible column.

##### Example: Maximum Value in Visual

```
= MAXX(ROWS(), [Total Sales])
```

This gives the maximum value seen in the current visual segment.

##### Trick 5 Filtering Within ROWS()\<img loading="lazy" decoding="async" class="aligncenter wp-image-49143 size-full" src="https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-215744.png" alt="Filtering Within ROWS() Power BI visual DAX" width="536" height="569" srcset="https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-215744.png 536w, https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-215744-283x300.png 283w, https://databear.com/wp-content/uploads/2026/01/Screenshot-2026-01-04-215744-141x150.png 141w" sizes="(max-width: 536px) 100vw, 536px" />

Want the maximum sales within a specific year?

1. Inside the visual calculation, define a variable to capture the selected year:
	```
	VAR currentYear = SELECTEDVALUE([Year])
	```
2. Then filter:
	```
	RETURN
	MAXX(
	    FILTER(
	        ROWS(),
	        [Year] = currentYear
	    ),
	    [Total Sales]
	)
	```

This counts only rows where the year matches, then evaluates the maximum.

##### Trick 6 First and Last Values

Visual calculations also let you pull edge values like first or last value across a group.

##### First Value in Table

```
= FIRST([Total Sales])
```

This repeats the first value across the table.

##### Group Reset (e.g., by Channel)

To reset by group:

```
= FIRST([Total Sales], [Channel])
```

Or by column position:

```
= FIRST([Total Sales], 2)
```

##### Why These Tricks Matter

Visual calculations let you:

- Add row computations *without writing additional DAX measures*
- Customize outputs for each level of your visual
- Build advanced analytics (rolling metrics, first/last values)
- Improve report readability

For deeper learning on visuals, DAX, and data modelling, [explore professional courses](https://databear.com/power-bi-training/)

By using **Power BI visual DAX**, you can perform advanced calculations at the visual level, keeping your data model cleaner while still delivering highly customized analytics.

##### Conclusion

Visual calculations in Power BI go far beyond simple summaries. From adding dynamic row numbers and moving averages to powerful operators like `ROWS()` and context controls with `IS_AT_LEVEL()`, these techniques unlock advanced analytics without bloating your model with measures.