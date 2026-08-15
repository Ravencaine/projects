---
title: "10 Essential DAX Functions for Beginners in Power BI"
source: "https://medium.com/write-a-catalyst/10-essential-dax-functions-for-beginners-in-power-bi-ad282ba96875"
author:
  - "[[Anurodh Kumar]]"
published: 2025-08-27
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XHLHJFuk7_ZjP2SgnlLKCQ.png)

image by Anurodh kumar

## 1\. SUM

Adds up all the values in a column.

👉 Example: SUM(Sales\[Revenue\])

## 2\. AVERAGE

Calculates the mean of a column.

👉 Example: AVERAGE(Sales\[Profit\])

## 3\. COUNT / COUNTROWS

Counts the number of rows or values.

👉 Example: COUNT(Sales\[OrderID\]) or COUNTROWS(Sales)

## 4\. DISTINCTCOUNT

Counts unique values in a column.

👉 Example: DISTINCTCOUNT(Sales\[CustomerID\])

## 5\. CALCULATE

The most powerful function! Modifies filter context to calculate values under specific conditions.

👉 Example: CALCULATE(SUM(Sales\[Revenue\]), Sales\[Region\] = “East”)

## 6\. FILTER

Returns a subset of a table that meets certain criteria.

👉 Example: FILTER(Sales, Sales\[Revenue\] > 1000)

## 7\. IF

Performs conditional logic.

👉 Example: IF(Sales\[Profit\] > 0, “Profit”, “Loss”)

## 8\. RELATED

Brings values from another table using relationships.

👉 Example: RELATED(Customer\[CustomerName\])

## 9\. ALL

Removes filters from a table or column.

👉 Example: CALCULATE(SUM(Sales\[Revenue\]), ALL(Sales))

## 10\. DIVIDE

Safely divides numbers and avoids errors when dividing by zero.

👉 Example: DIVIDE(SUM(Sales\[Revenue\]), SUM(Sales\[Orders\]))