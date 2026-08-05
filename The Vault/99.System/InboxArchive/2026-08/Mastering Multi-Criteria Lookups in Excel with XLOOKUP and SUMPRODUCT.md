---
title: "Mastering Multi-Criteria Lookups in Excel with XLOOKUP and SUMPRODUCT"
source: "https://medium.com/@markchen69/mastering-multi-criteria-lookups-in-excel-with-xlookup-and-sumproduct-58bcc2dd2606"
author:
  - "[[Mark Chen]]"
published: 2024-11-14
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
When it comes to Excel, one of the most common (and sometimes trickiest) tasks is finding data based on multiple criteria. If you’ve ever needed to filter data based on more than one condition, you may have discovered that most lookup functions, like `VLOOKUP` and `HLOOKUP`, only handle a single criterion. That’s where `XLOOKUP` comes in, along with a few powerful tricks to make it work with multiple criteria.

In this article, I’ll show you how to use `XLOOKUP` to handle multiple conditions in a lookup, and we'll even cover a way to sum data based on multiple criteria using `SUMPRODUCT`. Whether you're just getting started with Excel formulas or want to expand your data lookup skills, this article will have something for you!

![](99.System/Attachments/1!6iA5jIdqum2AJuDPzG6BqQ.png.webp)

I need the magnifier! Not a bad idea for a data analyst.

## What You Need to Know About XLOOKUP

`XLOOKUP` is one of Excel’s latest and greatest lookup functions. Introduced in Excel 365 and Excel 2019, `XLOOKUP` replaces `VLOOKUP`, `HLOOKUP`, and even `INDEX` / `MATCH` in many scenarios. It’s flexible, user-friendly, and unlike its predecessors, it can look to the left, right, above, or below the lookup value. However, it wasn't specifically designed for multi-criteria lookups, so we have to get a bit creative.

Let’s dive into an example.

## The Scenario: Looking Up Sales Data with Multiple Conditions

Imagine you work in a retail company with sales data organized in a table. You want to retrieve the sales amount for a specific product category, product type, and region. Here’s how the data might look:

![](99.System/Attachments/1!R4MjH4bmyomLewfYBGUgbA.png.webp)

Let’s say you want to look up the sales for the “Electronics” category, the “TV” product, and the “South” region.

## Solution 1: Using XLOOKUP with Multiple Criteria

To make `XLOOKUP` work with multiple conditions, we can combine each criterion into a single lookup value using concatenation. Here’s how:

1. **Concatenate the Criteria in a Single String**  
	We’ll combine “Electronics”, “TV”, and “South” into a single string, separated by `&`.
2. **Concatenate the Search Columns**  
	Next, we’ll combine each column in the data range (`Category`, `Product`, and `Region`) the same way. This lets us match the concatenated lookup value with each row.

Here’s the formula you’ll use:

```c
=XLOOKUP("Electronics" & "TV" & "South", A2:A7 & B2:B7 & C2:C7, D2:D7)
```

## Explanation:

- The lookup value is `"Electronics" & "TV" & "South"`, which combines all the criteria.
- `A2:A7 & B2:B7 & C2:C7` concatenates each row in `Category`, `Product`, and `Region` to create an array of combined values.
- `D2:D7` is the return array, which contains the `Sales` data.

When you enter this formula, it will return `300`, which is the sales for "Electronics" "TV" in the "South" region. 🎉

> ***Pro Tip:*** *To make this formula dynamic, you can replace the hard-coded criteria (“Electronics”, “TV”, “South”) with cell references (e.g., F1, F2, and F3), like this:*
> 
> `*=XLOOKUP(F1 & F2 & F3, A2:A7 & B2:B7 & C2:C7, D2:D7)*`

## Solution 2: Using FILTER for Multiple Matches

If your data has multiple rows that meet the criteria, `FILTER` is another fantastic option. Here’s how to find all matching rows:

```c
=FILTER(D2:D7, (A2:A7="Electronics") * (B2:B7="TV") * (C2:C7="South"), "Not Found")
```
- `FILTER` returns an array of values that meet the conditions.
- `(A2:A7="Electronics") * (B2:B7="TV") * (C2:C7="South")` filters rows based on all three conditions.

`FILTER` is powerful because it displays all matching values rather than just one.

## Solution 3: Summing with Multiple Criteria Using SUMPRODUCT

Now, what if you wanted to calculate the **total sales** for all rows that meet these criteria? `SUMPRODUCT` can handle this beautifully:

```c
=SUMPRODUCT((A2:A7="Electronics") * (B2:B7="TV") * (C2:C7="South") * D2:D7)
```
- This formula evaluates each condition and returns `TRUE` or `FALSE` arrays.
- The arrays are multiplied together with `D2:D7` to sum up all matching `Sales` values.

## Summary

Using these formulas, you can unlock the power of multi-criteria lookups in Excel, whether you need to look up a single value, filter multiple matches, or sum based on conditions. While `XLOOKUP` doesn’t natively support multiple criteria, combining it with `&` for concatenation allows you to handle complex lookups without adding extra columns.