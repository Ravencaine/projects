---
created: 2026-08-02
updated: 2026-08-02
source: Mastering M Language and DAX Functions in Power BI A Comprehensive Guide with Real-World Use Cases.md
note_type: pattern
tags: [dax, pattern, real-world, time-intelligence, kpi, ranking, abc-analysis, rls]
---

# DAX Real-World Use Cases

Four practical scenarios demonstrating DAX in production Power BI models.

## 1. Dynamic KPIs with CALCULATE

**Scenario:** Calculate YTD profit and % contribution to total.

```dax
Total YTD Profit =
    CALCULATE(
        [Total Profit],
        DATESYTD('Date'[Date])
    )

% Contribution =
    DIVIDE(
        [Total Profit],
        CALCULATE([Total Profit], ALLSELECTED())
    )
```

`CALCULATE` modifies filter context to apply the DATESYTD time filter. `ALLSELECTED()` removes visual-level filters but keeps external slicers.

## 2. Time Comparisons — YoY Growth

**Scenario:** Year-over-year sales growth with rolling 12-month totals.

```dax
YoY Growth =
    DIVIDE(
        [Total Sales] - CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date])),
        CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
    )

Rolling 12M =
    CALCULATE(
        [Total Sales],
        DATESBETWEEN(
            'Date'[Date],
            NEXTDAY(LASTDATE('Date'[Date]) - 365),
            LASTDATE('Date'[Date])
        )
    )
```

## 3. Advanced Analytics — ABC Analysis / Pareto

**Scenario:** Classify products into A/B/C based on cumulative revenue contribution.

```dax
Product Revenue Rank =
    RANKX(
        ALL('Product'[Product]),
        [Total Sales],
        ,
        DESC,
        Dense
    )

ABC Class =
    VAR CumulativePct =
        DIVIDE(
            CALCULATE([Total Sales], FILTER(ALL('Product'), [Product Revenue Rank] <= EARLIER([Product Revenue Rank]))),
            [Total Sales]
        )
    RETURN
        SWITCH(TRUE(),
            CumulativePct <= 0.70, "A",
            CumulativePct <= 0.90, "B",
            "C"
        )
```

`RANKX` assigns revenue rank. A `SWITCH` on cumulative percentage threshold assigns class.

## 4. Row-Level Security (RLS)

**Scenario:** Restrict data by user email using `USERPRINCIPALNAME()`.

```dax
[Region] = USERPRINCIPALNAME()
-- or
[Email] = USERPRINCIPALNAME()
```

Applied as a DAX filter in the RLS role definition. `USERPRINCIPALNAME()` returns the signed-in user's UPN from Azure AD.

## Related

- [[dax-function-taxonomy]] — `reference`
- [[m-language-real-world-use-cases]] — `pattern`
