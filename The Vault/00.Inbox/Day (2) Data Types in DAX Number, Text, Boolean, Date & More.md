---
title: "Day (2) Data Types in DAX: Number, Text, Boolean, Date & More"
source: "https://medium.com/write-a-catalyst/day-2-data-types-in-dax-number-text-boolean-date-more-83ccffcda673"
author:
  - "[[Anurodh Kumar]]"
published: 2025-05-27
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2Xn2xR0ViwJduFbaJGh8-Q.png)

image By Anurodh kumar

[***If you want to go to Day (1)***](https://medium.com/write-a-catalyst/what-is-dax-understanding-the-role-of-dax-in-power-bi-5e5d697c0eff)

Understanding **data types in DAX** is essential for writing accurate formulas and avoiding unexpected errors in Power BI. DAX may feel similar to Excel at first, but behind the scenes, it handles data types very strictly.

Let’s break down the core data types you’ll encounter while writing DAX formulas.

## 1️⃣ Number (Numeric)

DAX has several numeric types, but all numbers fall under **decimal** or **integer** categories. These are used in most calculations (like SUM, AVERAGE, etc.).

### ✅ Examples:

- 100
- 3.14
- \-5

**🔧 Used in:**

- Arithmetic (`+`, `-`, `*`, `/`)
- Aggregations (`SUM`, `MIN`, `MAX`)
- Logical comparisons (`>`, `<`, `=`, etc.)

## 2️⃣ Text (String)

Text data represents alphanumeric characters — names, categories, codes, etc.

### ✅ Examples:

- `"Sales"`
- `"A101"`
- `"John Doe"`

**🔧 Used in:**

- Concatenation (`"Region: " & [Region]`)
- Filtering (`FILTER`, `CONTAINSSTRING`)
- Sorting and grouping

> *📌 DAX uses* ***double quotes (“ “)*** *to define text.*

## 3️⃣ Boolean (TRUE/FALSE)

Boolean values are either `TRUE` or `FALSE`. You’ll use them constantly in `IF`, `FILTER`, `CALCULATE`, and logical functions.

**✅ Examples:**

- `[Amount] > 1000` → returns TRUE or FALSE
- `AND([Flag1], [Flag2])`

**🔧 Used in:**

- Condition checking
- Filter expressions
- Logical operators (`AND`, `OR`, `NOT`)

## 4️⃣ Date/Time

DAX has a rich Date/Time type that stores both **date and time** in a single field.

### ✅ Examples:

- `2025-01-01`
- `2025-01-01 14:30:00`

**🔧 Used in:**

- Time intelligence (`DATESYTD`, `SAMEPERIODLASTYEAR`)
- Date arithmetic (`TODAY() - [Date]`)
- Sorting and filtering by period

> *📌 Dates are internally stored as floating-point numbers where the* ***integer part is the date*** *and* ***decimal part is the time****.*

## 🔁 Note:

- **Blank (NULL)** is also a data type. Functions like `ISBLANK()` check for it.
- DAX does **automatic type conversion** in some functions — but not always! Be careful when comparing text with numbers.
- **Type mismatches** often cause errors like: *“Cannot compare value of type Text with value of type Number.”*
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZT_fbXIdPxlL1BluJfsulw.png)

DAX is a powerful language, but it’s also strongly typed. Mastering data types helps you write cleaner, bug-free formulas, and unlock the full potential of Power BI analytics.

> *💬 Next up in the series:* **Calculated Columns vs Measures — Core Differences** *— stay tuned!*