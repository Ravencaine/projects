---
title: "IF vs SWITCH in DAX (Power BI)"
source: "https://medium.com/write-your-world/if-vs-switch-in-dax-power-bi-484f293ab47e"
author:
  - "[[Anurodh Kumar]]"
published: 2025-05-27
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xVe3a_LgZG9GfWm2cGxaWw.png)

image by Anurodh kumar

Both IF and SWITCH are conditional functions used in DAX, but they serve slightly different purposes and are best suited for different scenarios.

## 🔹 IF Function

### ✅ Use When:

- You have simple true/false logic
- You need to check a single condition

### 📌 Syntax:

```c
IF(condition, result_if_true, result_if_false)
```

### Example:

```c
IsHighSales = IF(Sales[Amount] > 1000, "High", "Low")
```

### 🔄 Nested IF:

You can nest IFs, but it becomes hard to read:

```c
Category = IF(Value > 1000, "High", IF(Value > 500, "Medium", "Low"))
```

## 🔸 SWITCH Function

### ✅ Use When:

- You have multiple conditions or values to match
- You want cleaner, more readable code than nested IFs

### 📌 Syntax:

```c
SWITCH(expression, value1, result1, value2, result2, ..., else_result)
```

### Example:

```c
Grade = SWITCH([Score],
    5, "Excellent",
    4, "Good",
    3, "Average",
    2, "Poor",
    "Fail"
)
```

You can also combine with TRUE() for condition-based logic:

```c
Grade = SWITCH(TRUE(),
    [Score] >= 90, "A",
    [Score] >= 80, "B",
    [Score] >= 70, "C",
    [Score] >= 60, "D",
    "F"
)
```