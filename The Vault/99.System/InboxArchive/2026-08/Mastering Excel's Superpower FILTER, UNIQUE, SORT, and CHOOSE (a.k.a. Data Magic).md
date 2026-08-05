---
title: "#🧠 Mastering Excel’s Superpower: FILTER, UNIQUE, SORT, and CHOOSE (a.k.a. Data Magic)"
source: "https://medium.com/@markchen69/mastering-excels-superpower-filter-unique-sort-and-choose-a-k-a-data-magic-b5dbeeb02f0d"
author:
  - "[[Mark Chen]]"
published: 2025-07-14
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!YoXJ6o0Qnor3EorJiKnJmg.png.webp)

Let’s face it — classic Excel was like a loyal spreadsheet soldier. But modern Excel? It’s a full-blown data ninja. And the weapons of choice? Array formulas like `FILTER()`, `UNIQUE()`, `SORT()`, and `CHOOSE()`.

Individually, these functions are smart. Together? They’re game-changing.

In this guide, I’ll walk you through how I transformed a messy table into a dynamic, sorted, deduplicated, filtered dream — all without helper columns or pivot tables.

## 🎯 The Goal: Real-World Excel Wizardry

Let’s say you’ve got a data table with thousands of rows:

- Column F: Project ID
- Column Q: Budget Category

You want to:

- Combine these two non-adjacent columns into a single view
- Remove duplicate combinations
- Sort by both columns
- Filter out rows where the category is 0 or blank

This used to be a pain. But not anymore.

## 🧪 The Formula That Does It All

```c
=SORT(
   UNIQUE(
      FILTER(
         CHOOSE({1,2}, F2:F3039, Q2:Q3039),
         (Q2:Q3039<>0)*(Q2:Q3039<>"")
      )
   ),
   {1,2},
   {TRUE,TRUE}
)
```

## 🔍 What’s Happening Here:

1. `**CHOOSE({1,2}, F:..., Q:...)**`: Virtually stacks non-adjacent columns into a 2D array
2. `**FILTER(...)**`: Excludes rows where column Q is 0 or blank
3. `**UNIQUE(...)**`: Keeps only distinct pairs
4. `**SORT(..., {1,2}, {TRUE,TRUE})**`: Sorts first by Project ID (F), then Budget Category (Q)

This entire operation lives in a single cell. And yes — it auto-expands.

## 🧵 Other Array Formula Power Combos

### 🔁 Combine and Flatten Columns

```c
=UNIQUE(VSTACK(A2:A100, C2:C100))
```

→ Merges two separate columns into one list of unique values

### 🧠 Create a Dynamic Dropdown List

```c
=SORT(UNIQUE(FILTER(A2:A100, A2:A100<>"")))
```

→ Great for named ranges or Data Validation

### 🎯 Filter by Two Conditions

```c
=FILTER(A2:C100, (B2:B100="Active")*(C2:C100>10000))
```

→ Think SQL `WHERE` clause with AND logic

### 🧹 Remove Duplicates While Ignoring Blanks

```c
=UNIQUE(FILTER(A2:A100, A2:A100<>""))
```

## ⚠️ Tips for Success

- Always match row lengths — dynamic arrays break if your input arrays are uneven
- Use `LET()` for readability and performance
- Wrap results with `IFERROR()` to handle blanks or mismatches gracefully

## 🧙♂️ Final Thoughts

With these array formulas, you’re not just working in Excel — you’re scripting data behavior like a low-code Jedi. And the best part? No VBA. No macros. Just clean, fast, modern Excel.

> *“What used to take 6 steps and 4 helper columns now lives in one formula.”*

If you haven’t embraced `FILTER()`, `UNIQUE()`, `SORT()`, and `CHOOSE()`, now’s the time. Your data deserves better. And so do you.

✍️ Written by a data analyst who now dreams in curly brackets and spill ranges.