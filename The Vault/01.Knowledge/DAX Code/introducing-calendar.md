---
title: "Introducing calendar"
source: "https://www.sqlbi.com/articles/introducing-calendar-based-time-intelligence-in-dax"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> This article introduces the new calendar-based time intelligence functions in DAX, available in preview from the September 2025 release of Power BI. Since i

Introducing calendar-based time intelligence in DAX - SQLBI Since its first release in 2010, DAX has had a set of time intelligence functions to simplify calculations like year-to-date, year-over-year, and so on. However, the calculations only supported the Gregorian calendar, without addressing similar requirements for other calendars, such as the 4-4-5, ISO, and many other non-Gregorian calendars. With the classic time intelligence, the columns of the Date table were unknown to the time intelligence functions, with the only exception of the date column in the Date table, typically Date[Date] . The calendar-based time intelligence functions are designed to handle different types of calendars; therefore, they rely on columns in the date table to provide information about when a year begins and ends, as well as how it is divided into quarters, months, and/or weeks. Consequently, the Date table must contain several columns with specific meanings, and the developer must associate these columns with levels in the calendar definition. These columns are meaningful to both humans and DAX. For example, the SAMEPERIODLASTYEAR function is used to display the value of a measure over the same period in the previous year. In classic time intelligence, the function works by detecting the currently-selected time period, and using the Date column, moving the filter back one year. With calendar-based time intelligence, the Date table must contain a specific column indicating the year, which allows the DAX engine to adjust the filter on that column to move it back to the previous year. Things are much more complicated than this, but – at this point – a generic idea of the behavior is more than enough. This article does not include the user interface. Please watch the video to see how the user interface works, and refer to the additional links in case we create new videos, should the user interface that defines calendars evolve. Introducing calendars The calendar-based time intelligence does not assume a year is a Gregorian year. The calendar-based functions base their behavior on the content of columns in the Date table itself. This is why the Date table must include columns to indicate how a year is divided into periods, and developers must label these columns to inform DAX of their meaning. Columns are associated with their meaning by creating one or more Calendar objects. A calendar stores the association between table columns and time levels, such as year, quarter, and month. We can build multiple calendars on the same table. For example, we could include in the same Date table a Gregorian calendar, an ISO calendar, and a fiscal calendar. However, including multiple calendars in the same Date table poses some challenges because of the way calendar-based time intelligence functions remove filters: all the calendars participate in that activity even when only one calendar is referenced in the function. Here is a typical hierarchy of a Gregorian calendar, divided into years, quarters, months, and dates. On the left, there are four levels; on the right, a sample of values is shown. A calendar associates levels of the hierarchy with columns in the Date table. This mapping allows developers to create any calendar. For example, creating a calendar with thirteen months is a viable option with calendars, whereas it would not be possible with classic time intelligence. While 13-month calendars are not frequent, a type of calendar that is very commonly used and requires calendar-based time intelligence functions is the weekly calendar. Indeed, weeks cannot be aggregated to months or quarters in a regular Gregorian calendar, because there are weeks belonging to two months. Therefore, it is not possible to create a hierarchy that includes weeks and months according to the definition of the Gregorian calendar. However, it is possible to use weeks as the primary calendar entity and to redefine the concepts of years, quarters, and months to establish a natural hierarchy based on weeks, where every week belongs to a single “period” (sometimes called a month) and to a single quarter. We will create a weekly calendar later in this chapter. Using calendars With classic time intelligence functions, the presence of a Date column in the Date table is enough to make them work. With the calendar-based time intelligence functions, once the Date table is in the model, it is still necessary to associate columns with the proper category in calendars. A single date table can host multiple calendars, and the same column can be used in multiple calendars. Adequate care must be taken to ensure that the column is always associated with the same category. For example, if the Date[Month] column is associated with the Month in Year category, then the same column cannot be associated with a different category in another calendar. A column category defines the semantics of the column for the calendar and describes the expected behavior of the column related t

## Code / Examples

```
createOrReplace ref table Date calendar Gregorian calendarColumnGroup = year primaryColumn: Year calendarColumnGroup = quarter primaryColumn: 'Year Quarter Number' associatedColumn: 'Year Quarter' calendarColumnGroup = month primaryColumn: 'Year Month Number' associatedColumn: 'Year Month' associatedColumn: 'Year Month Short' calendarColumnGroup = date primaryColumn: Date
```
```
createOrReplace ref table Date calendar Gregorian calendarColumnGroup = year primaryColumn: Year calendarColumnGroup = monthOfYear primaryColumn: 'Month Number' associatedColumn: Month calendarColumnGroup column: Period column: Season
```
```
Sales SPLY Calendar = CALCULATE ( [Sales Amount], SAMEPERIODLASTYEAR ( 'Gregorian' ) )
```
```
SAMEPERIODLASTYEAR ( <Dates> )
```
```
REMOVEFILTERS ( [<TableNameOrColumnName>] [, <ColumnName> [, <ColumnName> [, … ] ] ] )
```
```
DATEADD ( <Dates>, <NumberOfIntervals>, <Interval> [, <Extension>] [, <Truncation>] )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/introducing-calendar-based-time-intelligence-in-dax)*
