---
title: "An Unexpected Lesson with Calculating Currency Conversions in DAX"
source: "https://medium.com/data-science/an-unexpected-lesson-with-calculating-currency-conversions-in-dax-58014260a98"
author:
  - "[[Salvatore Cagliari]]"
published: 2022-01-07
created: 2026-08-12
description: "Currency conversion is a common reporting requirement. While implementing the solution, I learned an unexpected lesson on data modelling in Power BI."
Processed: "Unprocessed"
---
## Currency conversion is a common reporting requirement. While implementing the solution, I learned an unexpected lesson on data modelling in Power BI.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*qoeDkXW3-yiY43_g)

Photo by John McArthur on Unsplash

## Introduction

When working with Currency conversion, you have to have a list of conversion rates for any specific period. The period can be daily or monthly with Average Rates or the last (closing) rate per month.

You can get such a list online from your national bank.

In my case, as I live in Germany and work in Switzerland; I looked at the [European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) and the [Swiss National Bank](https://data.snb.ch/en/publishingSet/A) (SNB).

There you can download the complete set of exchange rates for free as an Excel file or a CSV file.

Based on the requirements, I had to get the exchange rates from SNB. Unfortunately, the exported data contained only the monthly average and the Closing rates per month.

Because I needed the Daily rates, I used a trick described in one of my past articles to fill Gaps in Time Series data:

## [Fill Gaps in Time Series with this simple trick in SQL](https://medium.com/codex/fill-gaps-in-time-series-with-this-simple-trick-in-sql-81ac655e5ad7?source=post_page-----58014260a98---------------------------------------)

### Time-based data can contain gaps. Such gaps can cause issues when you have to process this data. Here’s a trick to fill…

medium.com

After importing the rates table into Power BI, I wrote the Measure(s) to calculate the result.

The following three approaches go from simple to complex.

I encountered unexpected difficulties during my development work, which led to new knowledge while working on the last approach to fulfil specific requirements.

## Case 1 — One source currency to multiple currencies

In this case, we have a Transaction- (Fact-) table, which contains values in USD. Then, we have a Currency rate table, which includes the daily conversion rates from USD in all other currencies.

The data model is the following:

![Data model for a simple conversion (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7jyHqk15DIRR-7D4qaUxxQ.png)

Figure 1 — Data model for a simple conversion (Figure by the Author)

I will use the same principle to model the third and final solution.

As I always need one conversion rate per period, I must aggregate the daily rates when looking at monthly or yearly data.

For this reason, I need to create an Average rate Measure first:

```c
Average Rate = AVERAGE(‘Exchange Rate’[Average_Rate])
```

Now, I can use the following Measure to calculate the conversion:

```c
Online Sales Currency =VAR SalesUSD =
    CALCULATE([Online Sales (By Order Date)]
              ,REMOVEFILTERS(‘Currency’)
              )VAR ExchangeRate = SELECTEDVALUE(‘Exchange Rate’[Average_Rate])RETURN
     SalesUSD * ExchangeRate
```

I have to use REMOVEFILTERS(‘Currency’) in CALCULATE() to ensure that the target currency selection doesn’t filter the Online Sales table.

As an alternative, it is possible to disable the Relationship between the currency and the Online Sales table.

This simple approach has some drawbacks:

1. The Measure calculates the average currency rate over the selected period. This introduces inaccuracy in the calculation of the results
2. The Measure doesn’t consider missing rates
3. The approach works only in one direction and with one source currency.

## Case 2 — Many currencies to many currencies

The guys at SQLBI wrote an article about currency conversion as a [DAX Pattern](https://www.daxpatterns.com/).

Their solution covers all issues of the first case:

- Mapping the daily transactions to the corresponding daily rate
- Consider missing rates
- The ability to work with multiple sources and target currencies

It makes no sense to repeat the details here, as the article and video contain very detailed solutions descriptions.

You can find the article and the corresponding video in the Reference section below.

## Case 3 — Using a bridge currency

In my situation, I have the following data and requirements:

- My data is with the currency Euro
- I have the table with the conversion rates with Swiss Francs (CHF) as the base currency
- I need to report my data mainly in CHF
- I must be able to analyze the data in USD as well

Because of the fixed input currency, I don’t need two currency rate tables, as shown in one of the DAX Pattern solutions from the second case.

When I want to calculate the result, I first have to multiply the Value in EUR by the Exchange Rate for EUR to get the Value in CHF. Then, I can divide the outcome with the target currency’s Exchange Rate to get the final result.

I implemented the following intermediate Measure with a slightly different logic than in the first case. The embedded the explanations of the logic as comments:

```c
Cost (Currency) =// Step 1: Get the last date with an Exchange-Rate in the actual period
VAR LastExchRate = CALCULATE(
         LASTNONBLANK(‘Date’[Date], MIN(‘Exchange Rates’[Value]) )
         )// Step 2: Get the last Exchange-Rate for Euros
VAR ExchRateEUR = CALCULATE(AVERAGE(‘Exchange Rates’[Value])
                              ,REMOVEFILTERS(‘Currencies’)
                              ,’Currencies’[CurrencyCode] = “EUR1”
                              ,’Date’[Date] = LastExchRate
                              )// Step 3: Convert the Cost in EURO to CHF
// The Reason for the REMOVEFILTERS() is the same as explained in the first case
VAR CostCHF = CALCULATE([Cost (EUR)] * ExchRateEUR
                         ,REMOVEFILTERS(‘Currencies’)
                         )// Step 4: Get the current Currency Code
VAR SelectedCurr = SELECTEDVALUE(‘Currencies’[CurrencyCode])// Step 5: Calculate the Result using the Cost in CHF and the Rate of the current Currency Code
// The Formula to calculate the result is: (CostEuro * RateEUR => CHF) / RateSelectedCurrency
VAR Result = CALCULATE(DIVIDE ( CostCHF
                                , AVERAGE(‘Exchange Rates’[Value])
                                )
                          ,’Currencies’[CurrencyCode] = SelectedCurr
                          ,’Date’[Date] = LastExchRate
                          )RETURN
// Return the Result from Step 5 only when one Currency is selected.
// If no specific Currency is selected, the return Blank
IF ( HASONEVALUE(‘Currencies’[CurrencyCode])
                  ,SWITCH ( SelectedCurr
                            ,”EUR1", [Cost (EUR)]
                            ,”CHF1", CostCHF
                            ,Result)
                  , BLANK()
                  )
```

As you can see from the comments, I get the last Exchange Rate from the current period instead of calculating the Average Exchange Rate over the actual period.

The reason for this is that it is straightforward to validate the result with this approach, as I only have to get the last Exchange Rate for a specific period to check if the outcome for aggregated results (e. g. Months and Years) is correct.

Anyway, I have to aggregate the Exchange Rate in Step 2, as CALCULATE can use only an aggregation expression as the first argument. But, As I restrict the Exchange rate to the last date in the actual period, the AVERAGE() has no effect.

I need the SWITCH() inside the IF() to check if:

- The current currency is EUR, the return the Value in EUR
- The current Currency is CHF, the return the Value in CHF
- Else, return the calculated result

The next step is to improve the Code by implementing the approach described in the DAX Pattern solution.

The final Measure is the following:

```c
Cost (Currency) =// Step 1:
// Get the Rates for each row in the Data table for CHF (The bridge/intermediary) currency
// As the Data currency is EURO, I have to take the rate for EURO to be able the calculate the value in CHF
VAR AggregatedValue_CHF =
                  CALCULATETABLE (
                      ADDCOLUMNS(
                        SUMMARIZE(‘Azure_UsageDetails’
                                          ,‘Date’[Date])
                        ,“RateEUR”
                        ,CALCULATE(
                          SELECTEDVALUE( ‘Exchange Rates’[Value] ))
                        , “Cost_EUR”, [Cost (EUR)]
                        ),
                      ‘Currencies’[CurrencyCode] = “EUR1”
                      )// Step 2:
// Get the Rates for each row in the Data table for the selected currency
VAR AggregatedValue_EUR =
                 ADDCOLUMNS(
                     SUMMARIZE(‘Azure_UsageDetails’
                       ,‘Date’[Date])
                       ,“Rate”
                        ,CALCULATE(
                          SELECTEDVALUE( ‘Exchange Rates’[Value] ) )                       ,“Cost_EUR”, [Cost (EUR)]
                     )// Step 3:
// Combine both tables into one to be able to perform the correct currency conversion
VAR Cost_Rates = NATURALINNERJOIN(AggregatedValue_CHF,
                                  AggregatedValue_EUR)// Step 4:
// Perform the actual currency conversion with the use of the intermediary currency
VAR Result = SUMX(Cost_Rates
                   ,DIVIDE(([Cost (EUR)] * [RateEUR]), [Rate])
                   )// Step 5:
// Get the CurrencyCode of the actual currency
VAR SelectedCurr = SELECTEDVALUE(‘Currencies’[CurrencyCode])RETURN
// Step 6:
// Return the Result from Step 5 only when one Currency is selected.
// If no specific Currency is selected, the return is the Value in EURO
IF ( HASONEVALUE(‘Currencies’[CurrencyCode])
                  // Step 7:
                  // Check if the Currency is either CHF or EURO
                  // if the selected curreny is one of these, use the existing measures to get the result
                  ,SWITCH ( SelectedCurr
                             ,”EUR1", [Cost (EUR)]
                             ,”CHF1", [Cost (CHF)]
                             ,Result)
                  , [Cost (EUR)]
                  )
```

The first two steps generate two tables with the corresponding exchange rates for each row in the Data table. One table contains the conversion rate to convert Euro to Swiss Francs (CHF). And the other takes the conversion rate from the actual filter context (e. g. USD or AUD).

Step three combines the two tables into a table that looks like this:

![Sample combined data (Not actual data) (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8arzUbr6IQ-H6A3kUlF3zg.png)

Figure 2 — Sample combined data (Not actual data) (Figure by the Author)

Now, I can use the formula in Step 4 to calculate the result.

Steps four and five are the same as in the first Measure, used to solve this case. This step controls the output.

The Cost (CHF) Measure has the following code:

```c
Cost (CHF) =
    VAR AggregatedValue_CHF =
            CALCULATETABLE (
               ADDCOLUMNS(
                    SUMMARIZE(‘Azure_UsageDetails’
                               ,‘Date’[Date])
                    , “Rate”
                    ,CALCULATE(
                          SELECTEDVALUE( ‘Exchange Rates’[Value] ) )
                    ,“Cost_EUR”, [Cost (EUR)]
               ),
               ‘Currencies’[CurrencyCode] = “EUR1”
             )VAR Result = CALCULATE(
                    SUMX(AggregatedValue_CHF
                         ,[Cost (EUR)] * [Rate]
                         )
                    ,’Currencies’[CurrencyCode] = “CHF1”
                    )RETURN
     Result
```

At first sight, this Measure looks inefficient, as it uses almost only the Formula Engine:

![Server Timings of Currency Conversion (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*0QYrv3Bv3z23v0YvPaeMdw.png)

Figure 3 — Server Timings of Currency Conversion (Figure by the Author)

I used it with a small dataset with only 32'000 rows.

I checked the Timing in the solution provided with the solution by SQLBI. The performance is slightly better when you use the monthly rates instead of the daily rates. When you can live with the less precise monthly conversion rates, the calculation with the monthly rates could be a viable solution.

In any case, you need to evaluate the performance with your data to know if the performance is good for you.

The response time of 180 ms is good enough for my data set.

Then, I tested the same Measure on my large dataset with 64 million rows. The result is surprising:

![Server Timings of Currency Conversion with large Fact table (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*SGof6zDcGd_6mkB54nb95A.png)

Figure 4 — Server Timings of Currency Conversion with large Fact table (Figure by the Author)

The Storage Engine performs 71.8 % of the work with a parallelism of 3.4 (On a Quad-Core Laptop). The Measure returns the result after less than 1.5 seconds.  
This measurement leads to the conclusion that this solution scales very well with the amount of data.

The result looks like this, with only CHF, EUR and USD selected:

![Result from Currency Conversion (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*nDpvc8a68vcdkzQfUftYmQ.png)

Figure 5 — Result from Currency Conversion (Figure by the Author)

As mentioned initially, I learned something unexpected while solving this challenge.

When you look at the data model used at the start, there are two paths, between the Currencies table and the Fact table:

![Ambiguous paths (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bSCquE6SsdBYUI_KtCKETg.png)

Figure 6 — Ambiguous paths (Figure by the Author)

These two paths caused problems with my Measure.

The ambiguity comes from selecting a Currency in the Currencies table filters the data in the Fact table.

This filter leads to an empty result, as the Fact table contains only values in the Euro currency.

I cannot add REMOVEFILTERS(‘Currencies’) to the Measure (Step 1 & 2), as I need the selected currency to get the correct conversion rate.

The only way to solve this issue was to disable the Relationship between the Currencies and the Fact table. This change didn’t change the result:

![Corrected Data model (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5b4haVVZOq3BqM5Hd67evA.png)

Figure 7 — Corrected Data model (Figure by the Author)

This behaviour was unexpected, as I used this modelling technique in other projects with currency conversions.

## Conclusion

The calculation of currency conversion can be a tricky challenge.

The solution in the first case is straightforward, but it has some drawbacks, as it returns imprecise data through the use of an average conversion rate.

The solutions shown on the DAX Pattern website are excellent, as they’re using daily or monthly rates to calculate the correct result. In addition, these solutions contain checks for missing rates, etc.

You can use the solutions shown there in most of the cases.

I created my solution based on my specific requirements and available data.

But, even though this solution is particular, I learn some valuable lessons:

- Make sure that the data model doesn’t contain any potentially ambiguous relationships
- A solution can perform better with a large amount of data depending on the number of distinct values and many other factors
- When creating a complex solution, start with a solution, which is easy to test. Then, use the first version to validate the result of the following versions, with the need for complex queries or check against the source data

The next step for any approach is to create a Calculation group. But, it’s not possible to develop one Calculation item for the entire data model, as the solutions from the second and third cases iterate over one fact table. Therefore, you have to create one Calculation item per Fact table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*aCgZWX43h4147S1m)

Photo by Tim Mossholder on Unsplash

## References

You can find the SQLBI article mentioned above here: [Currency conversion — DAX Patterns](https://www.daxpatterns.com/currency-conversion/)

The corresponding video is in the SQLBI YouTube channel:

I use the Contoso sample dataset for the first example, like in my previous articles. You can download the ContosoRetailDW Dataset for free from Microsoft [here](https://www.microsoft.com/en-us/download/details.aspx?id=18279).

The Contoso Data can be freely used under the MIT License, as described [here](https://github.com/microsoft/Power-BI-Embedded-Contoso-Sales-Demo).

The data set used in the third example contains actual Usage data from my Azure cloud subscription, imported into Power BI.

## [Join Medium with my referral link - Salvatore Cagliari](https://medium.com/@salvatorecagliari/membership?source=post_page-----58014260a98---------------------------------------)

### As a Medium member, a portion of your membership fee goes to writers you read, and you get full access to every story…

medium.com

If you appreciate my work, feel free to support me through

## [Salvatore Cagliari](https://buymeacoffee.com/salvatorecagliari?source=post_page-----58014260a98---------------------------------------)

### I write technical articles about Data Analysis and Reporting with Power BI. In addition I love building and flying RC…

buymeacoffee.com

Or scan this QR Code:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*btH95UXO7gboS30eZMk6ug.png)

Any support is greatly appreciated.

Thank you.