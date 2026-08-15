---
title: "Using REMOVEFILTERS in DAX user"
source: "https://www.sqlbi.com/articles/using-removefilters-in-dax-user-defined-functions"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> In this article, we implement a function that removes filter-keep column filters from a calendar, using REMOVEFILTERS as the return value of the function. A

Using REMOVEFILTERS in DAX user-defined functions - SQLBI A DAX user-defined function, also known as a UDF, is expected to return a scalar or a table. However, because functions are fundamentally macro-expansion of DAX code, it is possible to return CALCULATE modifiers if the function is to be called only as a filter argument of CALCULATE . To show a practical example of when the feature proves to be useful, we debug a measure that fails because some calendar filters are not being removed correctly. Fixing the measure elegantly requires creating a function that removes filters rather than returning a value. Introducing the scenario We wrote a measure that computes the running total for the last three months, using basic time intelligence functions and calendar-based time intelligence: Measure in Sales table  Please note that we used ENDALIGNED in DATESINPERIOD to ensure the calculation aligns the time period with its end. If you are not familiar with the behavior of ENDALIGNED, you should read Understanding DATEADD parameters with calendar-based time intelligence . A thorough understanding of the particular behavior of ENDALIGNED is key in order to fully appreciate the problem to fix, so we strongly recommend checking out that article before or after reading this one. To verify that the measure computes the correct value, we also authored a visual calculation that computes the same value, with the visual calculation technique: Visual calculation  It is worth noting that we had to use -2 in RANGE rather than -3, because the current row is included in the range. The two measures produce different results at the quarter and year levels because of the different techniques they use. However, we are mainly interested in the measure, and we use the visual calculation only for debugging purposes. If you want to better understand how RANGE and visual calculations work, make sure to check out this mini-course in SQLBI+: Understanding visual calculations in DAX . From now on, we will focus only on the month level. Spotting the glitch in the measure Right now, all the numbers look correct. However, because there may be many rows to check, a simple visual calculation helps in focusing on the presence of errors: Visual calculation  The calendar table includes, among the many columns, one column indicating the weekday. One of the requirements is that the measure should work if users decide to focus on specific weekdays. In technical terms, we call such columns filter-keep columns, that is, columns whose filter needs to be maintained when the filter on the Date table is changed. You can find more information about filter-keep columns here: Introducing calendar-based time intelligence in DAX . Luckily, the calendar-based time-intelligence functions treat filter-keep columns in a sweet and safe way. Unfortunately, as we will discover, our measure does not. To demonstrate this, we add a slicer for the weekday and the test column to the report, focusing on Wednesday only. You can see that several months show an error: the visual calculation does not compute the same value as the measure. We will spare you the math: the visual calculation works smoothly, whereas the measure fails to compute the correct result. In the video, we outline the full debugging process to explain how to find the issue. Here, we go straight to the solution. When the measure is computing the reference date, it uses this expression:  MAX is being computed in the current filter context, which includes the weekday. Therefore, it finds the last Wednesday in the month. For some months, this will be the end of the month. For some others, it will be very close to the end of the month, while for several other months it will be a few days before the end of the month. Because of this, it will happen pretty frequently that the value of RefDate is not close enough to the end of the month to trigger the behavior of ENDALIGNED. As a consequence, the dates returned by DATESINPERIOD will include periods from subsequent months, thus producing an incorrect result. Therefore, we need to ensure that the reference date ignores the weekday filter. Fixing the bug To fix the problem, we could add REMOVEFILTERS on the Date[Weekday] column (as well as weekday number) because the sort-by-column feature is being used. While focusing on the columns we want to remove the filter from, we may also notice that the table includes not only the weekday, but also its short version (Mon, Tue, and so on). We need to remove the filters from these columns as well to provide more flexibility for our users. In general, we need to remove filters from any column that is not already included in the calendar (either as a level or as a time-related column) and that we want to consider as a filter-keep column. The list is known today, but it may grow later, when the semantic model is further developed. Therefore, we decided to consolidate the list of columns into a function that removes the filter from

## Code / Examples

```
Measure 3 Months = VAR RefDate = MAX ( 'Date'[Date] ) RETURN CALCULATE ( [Sales Amount], DATESINPERIOD ( 'Gregorian', RefDate, -3, MONTH, ENDALIGNED ) )
```
```
Visual 3 Months = CALCULATE ( SUM ( [Sales Amount] ), RANGE ( -2, TRUE, ROWS ) )
```
```
Test = IF ( [Measure 3 Months] - [Visual 3 Months] <> 0, "Error" )
```
```
VAR RefDate = MAX ( 'Date'[Date] )
```
```
Gregorian.RemoveFilterKeepColumns = () => REMOVEFILTERS ( 'Date'[Day of Week], 'Date'[Day of Week Number], 'Date'[Day of Week Short] )
```
```
Measure 3 Months = VAR RefDate = CALCULATE ( MAX ( 'Date'[Date] ), Gregorian.RemoveFilterKeepColumns() ) RETURN CALCULATE ( [Sales Amount], DATESINPERIOD ( 'Gregorian', RefDate, -3, MONTH, ENDALIGNED ) )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/using-removefilters-in-dax-user-defined-functions)*
