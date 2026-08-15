---
title: "Understanding DATEADD parameters with calendar"
source: "https://www.sqlbi.com/articles/understanding-dateadd-parameters-with-calendar-based-time-intelligence"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, reading-list]
created: "2026-08-11"
---

> The new calendar-based time intelligence functions offer greater flexibility than the classic time intelligence functions. This article describes the DATEAD

Understanding DATEADD parameters with calendar-based time intelligence - SQLBI The primary reason to adopt the new calendar-based time intelligence in Power BI is its flexibility (read more on Introducing calendar-based time intelligence in DAX ). Classic time intelligence functions work out of the box and deliver meaningful results in most scenarios. However, to do so, they make assumptions about the calendar structure and the desired outcomes. Sometimes, the choices are not aligned with the user requirements, and developers need to author their own time intelligence calculations. The new calendar-based time intelligence functions provide greater flexibility by allowing developers to configure parameters that drive the internal algorithms to meet diverse requirements. Using these parameters requires a precise understanding of the scenario for which they were built, which requires some attention to detail. Most of the article focuses on understanding the complex scenarios you may encounter when performing time-intelligence calculations. Choosing the right set of arguments is a very simple step if you understand the scenario well, but it may be a frustrating experience if you just try these arguments without having already gained the required knowledge. In this article, we focus on a specific function: DATEADD , which shifts time intervals. Be mindful that DATEADD is internally used by many time intelligence calculations; therefore, the concepts explained for DATEADD apply to other time intelligence functions, like, for example, DATESINPERIOD . Comparing months with different lengths DATEADD shifts the original selection (the current filter context) back and forth by the specified number of intervals, where an interval can be DAY , WEEK, MONTH , QUARTER , or YEAR . For example: DATEADD ( ‘Gregorian’, -6, MONTH ) shifts the current filter context six months back in time. The interval is MONTH , -6 is the number of months to shift, Gregorian is the calendar to use. Let us start investigating the scenario with a simple measure that computes the sales in the previous month, using classic time intelligence: Measure in Sales table  Using the measure in a report shows that the sales of January 2024 are reported correctly in February 2024. Despite it looking natural and correct, the result requires a deeper understanding. February 2024 contains 29 days, because 2024 is a leap year. January 2024 contains 31 days. The report is currently comparing two periods of different lengths. We are so used to variable-length months that we seldom worry about the fact that the we compare entities that are different (in this case in number of days). For the purposes of this article, the key point is that the two months have different lengths. The same scenario happens when comparing March 2024 with February 2024 or – in general – whenever we compare two months with a different number of days. It is important to note that right now, the granularity of the values we are inspecting is the month, and the period used for the shift is also the month. When the granularity of the selection and the granularity of the period used for the shift are the same, numbers are easy to read. If we expand the matrix at the day level, the selection granularity becomes the day, while the period-to-shift granularity is the month. The measure still reports correct results: each day in February is shifted back to the same day in January. As expected, Sales PM Date on the third of February reports the sales of the third of January. The scenario quickly becomes more complex i\f, rather than looking at the beginning of the month, we go to the end of February, namely the 29 th of February. The 29 th of February correctly shows the value of sales for the 29 th of January. However, January includes two additional days with sales: the 30 th and 31 st , which are not shown in February. Let us repeat this simple concept: January 2024 has 31 days, with a total Sales Amount of 188,419.28 . February 2024 contains only 29 days; Sales PM Date displays the exact sales amount of the corresponding day in the previous month. Two dates and their corresponding sales (9,534.40 and 9,445.42 for the 30 th and 31 st of January) are missing. Still, the total is the same: 188,419.28 . In other words, the total shown is not the sum of the displayed daily rows. Be mindful: this is not an incorrect behavior. It is a precise choice made by DAX to solve a problem that has no clear and simple solution: comparing two months with a different number of days, and showing the daily values at the same time, requires a compromise because we need to pack the total of $188,419.28 into only 29 rows rather than the original 31. The problem is not new; it has always been there. Classic time intelligence functions addressed this scenario differently. The same formula to compute the sales in the previous month can be written using the new calendar-based time intelligence: Measure in Sales table  Quit

## Code / Examples

```
Sales PM Date = CALCULATE ( [Sales Amount], DATEADD ( 'Date'[Date], -1, MONTH ) )
```
```
Sales PM Cal = CALCULATE ( [Sales Amount], DATEADD ( 'Gregorian', -1, MONTH ) )
```
```
Moving Average Calendar = CALCULATE ( DIVIDE ( [Sales Amount], COUNTROWS ( SUMMARIZE ( Sales, 'Date'[Year Month Number] ) ) ), DATESINPERIOD ( 'Gregorian', MAX ( 'Date'[Date] ), -6, MONTH ) )
```
```
Moving Average Classic = CALCULATE ( DIVIDE ( [Sales Amount], COUNTROWS ( SUMMARIZE ( Sales, 'Date'[Year Month Number] ) ) ), DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -6, MONTH ) )
```
```
Moving Average Calendar = CALCULATE ( DIVIDE ( [Sales Amount], COUNTROWS ( SUMMARIZE ( Sales, 'Date'[Year Month Number] ) ) ), DATESINPERIOD ( 'Gregorian', MAX ( 'Date'[Date] ), -6, MONTH, ENDALIGNED ) )
```
```
DATEADD ( <Dates>, <NumberOfIntervals>, <Interval> [, <Extension>] [, <Truncation>] )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/understanding-dateadd-parameters-with-calendar-based-time-intelligence)*
