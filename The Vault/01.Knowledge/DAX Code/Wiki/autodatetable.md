---
created: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, date-table, calendar, fiscal]
---

# AutoDateTable — Calendar Table with Fiscal Column Support

Generates a complete Date table between two dates with standard + fiscal columns.

```dax
DEFINE
    FUNCTION AutoDateTable =
        ( startDate : DATETIME, endDate : DATETIME, fiscalStartMonth : INT64 ) =>
        VAR dmin = DATE(YEAR(startDate),MONTH(startDate),DAY(startDate))
        VAR dmax = DATE(YEAR(endDate),MONTH(endDate),DAY(endDate))
        VAR base = CALENDAR(dmin,dmax)
        VAR addCols = ADDCOLUMNS(base,
            "DateKey",       YEAR([Date])*10000+MONTH([Date])*100+DAY([Date]),
            "Year",          YEAR([Date]),
            "MonthNo",       MONTH([Date]),
            "Month",         FORMAT([Date],"MMM"),
            "Quarter",       "Q"&ROUNDUP(MONTH([Date])/3,0),
            "StartOfMonth",  DATE(YEAR([Date]),MONTH([Date]),1),
            "EndOfMonth",   EOMONTH([Date],0),
            "WeekNoMon",    WEEKNUM([Date],2),
            "YearMonth",     FORMAT([Date],"YYYY-MM"),

            -- Fiscal (shifted by fiscalStartMonth)
            "FiscalYear",    YEAR([Date]) + IF(MONTH([Date])>=fiscalStartMonth,1,0),
            "FiscalMonthNo", MOD(MONTH([Date])-fiscalStartMonth+12,12)+1,
            "FiscalQuarter", "Q"&ROUNDUP((MOD(MONTH([Date])-fiscalStartMonth+12,12)+1)/3,0),

            -- Current flags
            "IsToday",       [Date]=TODAY(),
            "IsCurrentMonth",YEAR([Date])=YEAR(TODAY()) && MONTH([Date])=MONTH(TODAY())
        )
        RETURN addCols
```

**Usage — standard (FY starts January):**
```dax
Date = AutoDateTable(
    DATE(YEAR(MIN(Sales[Date]))-1,1,1),
    EOMONTH(MAX(Sales[Date]),0),
    1  -- fiscalStartMonth
)
```

**Usage — fiscal year starting July:**
```dax
Date = AutoDateTable(
    DATE(YEAR(MIN(Sales[Date]))-1,1,1),
    EOMONTH(MAX(Sales[Date]),0),
    7  -- fiscalStartMonth
)
```

After creating: **Table tools → Mark as date table → Date[Date]**.
