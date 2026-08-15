---
title: "DAX - the previous day"
source: "https://medium.com/@michalmolka/dax-previous-day-1cd3f8c2eae6"
author:
  - "[[Michal Molka]]"
published: 2020-10-16
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

When you want to get a value from the previous day, the first idea is the **PREVIOUSDAY()** DAX function. But there are more options.

The entire code used in this post is in a code example at the end of this post.

A source dataset is a [Covid-19](https://www.kaggle.com/imdevskp/corona-virus-report/data) dataset from the Kaggle website.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SiP1hYUyIFN_ASVL4dCufA.png)

We will focus on the \[**Confirmed**\] column. Confirmed cases of Covid-19 are stored as a cumulative sum. The goal is to compute a quantity difference between the current and the yesterday’s date. Of course, we can do it on a integration level. But I want to show you how can you achieve it in the DAX.

This is the visualization where we put the final measure.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tTpOyw3BALrSuWG9x3XCnw.png)

There are three measures and one computed column.

```c
Previous Date PREVIOUSDAY = 
    CALCULATE(
        VALUES('Covid-19'[Date].[Date]),
        PREVIOUSDAY('Covid-19'[Date].[Date])
    )
//---------------------------
Previous Date Max&LASTDATE = 
    VAR MaxValue = LASTDATE('Covid-19'[Date].[Date])
    RETURN 
    CALCULATE(
        LASTDATE('Covid-19'[Date].[Date]), 
        'Covid-19'[Date].[Date] < MaxValue
    )
//---------------------------
Previous Date DATEADD&LASTDATE = 
    DATEADD(
        LASTDATE('Covid-19'[Date].[Date]),
        -1,
        DAY
    )
//---------------------------
Previous Date EARLIER = 
    VAR LagColumn = 
        CALCULATE(MAX('Covid-19'[Date]),
            FILTER('Covid-19',
                'Covid-19'[Country/Region] = EARLIER('Covid-19'[Country/Region]) && 
                'Covid-19'[Date] < EARLIER('Covid-19'[Date]) &&
                'Covid-19'[Province/State] = EARLIER('Covid-19'[Province/State])
            )
        )
    
    VAR PreviousValue = 
        CALCULATE(
            MAX('Covid-19'[Confirmed]),
            FILTER('Covid-19','Covid-19'[Country/Region] = EARLIER('Covid-19'[Country/Region]) && 
                'Covid-19'[Province/State] = EARLIER('Covid-19'[Province/State]) && 
                'Covid-19'[Date] = LagColumn
                    )
                )
    RETURN
        LagColumn
```

The first one uses the **PREVIOUSDAY()** function, which is pretty simple to understand.

The second one calculates the latest date and the next. It looks for a date which is smaller than the **MaxValue** variable. Alternatively you can use the **MAX()** function.

The third one calculates the latest date like the previous function and after that uses the **DATEADD()** function and subtracts one day.

The fourth one is a computed column which uses the **EARLIER()** function to get the previous value.

Here is a table containing the result.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XWdxE4d2grEOMyy8PJFR0w.png)