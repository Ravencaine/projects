---
title: "Custom Subtotals in Power BI: A Rescue for Matrix Totals"
source: "https://medium.com/microsoft-power-bi/custom-subtotals-in-power-bi-a-rescue-for-matrix-totals-5f009d381b08"
author:
  - "[[Mateusz Mossakowski]]"
published: 2026-01-27
created: 2026-08-12
description: "Today in our company Viva Engage Power BI group, I noticed a question about how to tackle custom subtotals that should show up only as a column subtotal and not be repeated in every column of the matrix split. Depending on whether you want to overwrite the original measure in the column subtotal section or have the custom subtotal presented next to the original subtotal, the implementation might be simpler or slightly more complex, but I believe it’s still relatively easy to understand and implement."
Processed: "Unprocessed"
---
## Today in our company Viva Engage Power BI group, I noticed a question about how to tackle custom subtotals that should show up only as a column subtotal and not be repeated in every column of the matrix split. Depending on whether you want to overwrite the original measure in the column subtotal section or have the custom subtotal presented next to the original subtotal, the implementation might be simpler or slightly more complex, but I believe it’s still relatively easy to understand and implement.

![](https://miro.medium.com/v2/format:webp/1*zqyM6ZpjEKmUYp7G-nPS6Q.gif)

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

Let me give a fairly simple example. Suppose we have two measures of interest: Revenue and Revenue Share (which, in our case, represents the percentage of the product brand revenue within a product category). Now imagine that in the column subtotal we would like to see Revenue Share, while for each column representing a country we would like to see the absolute Revenue measure. We cannot, of course, achieve this by adding both measures to the matrix, as it would create too much noise and that’s not what we want.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*lvN4xfa5VtGjDCqfaY3LmQ.png)

Example of what we expect to see after the workaround

The solution here is a calculation group that checks whether the country is in scope and, depending on the result, either keeps the original measure (be it Revenue) or artificially overwrites it with a custom measure needed in the subtotal section. To achieve the desired results we need to have only one calculation item, though we must remember to adjust not only the Expression but also the Format String Expression.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*e9F7AOCeKtYTxLu5V_ggKA.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sS3g0LcjdPVZfYxf7Qb30Q.png)

```c
----------------------------------------------
-- Calculation Group: 'Single custom subtotal'
----------------------------------------------
CALCULATIONGROUP 'Single custom subtotal'[Calculation group column]    , Precedence = 1

    CALCULATIONITEM "Revenue" = 
        IF
        (
            ISINSCOPE( store_dim[country] ),
            SELECTEDMEASURE( ),
            [Revenue Share]
        )
        , FormatString = 
            IF
            (
                ISINSCOPE( store_dim[country] ),
                SELECTEDMEASUREFORMATSTRING( ),
                "#,0.0%;-#,0.0%;#,0.0%"
            )
```

Then we only need the Revenue measure in the Values section of the matrix visual. The last, but crucial, step is to expand the Filters section of the matrix visual, add the calculation group column there, and select the one item we just created. Voilà, the column subtotal changes to the custom one.

The situation becomes a bit more complex if we want to have both subtotals — the original and the custom one.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*gWG8-EGGWgM5hDbo_5umNA.png)

Example of what we expect to see after the workaround

You might be tempted to complicate the calculate group approach for a single custom column subtotal by using the following Expression and the Format String Expression.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6iXzyUhi896WHydr4n6dyw.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*gC2MSCjkNIGjGyt573hpWw.png)

```c
---------------------------------------------------------
-- Calculation Group: 'Double custom subtotals imperfect'
---------------------------------------------------------
CALCULATIONGROUP 'Double custom subtotals imperfect'[Calc item]    , Precedence = 2

    CALCULATIONITEM "Revenue" = 
        SWITCH
        (
            TRUE( ),
            ISINSCOPE( store_dim[country] ) && SELECTEDMEASURENAME( ) = "Revenue", SELECTEDMEASURE( ),
            ISINSCOPE( store_dim[country] ) && SELECTEDMEASURENAME( ) = "Revenue Share", BLANK( ),
            SELECTEDMEASURE( )
        )
        , FormatString = 
            SWITCH
            (
                TRUE( ),
                ISINSCOPE( store_dim[country] ) && SELECTEDMEASURENAME( ) = "Revenue", SELECTEDMEASUREFORMATSTRING( ),
                ISINSCOPE( store_dim[country] ) && SELECTEDMEASURENAME( ) = "Revenue Share", "",
                SELECTEDMEASURENAME( ) = "Revenue", "#,0",
                "#,0.0%;-#,0.0%;#,0.0%"
            )
```

We’re almost there, but the repeated blank columns in the matrix aren’t something Winnie the Pooh likes. Let’s stretch our neurons a little more and find a better solution!

The solution for double custom subtotals requires a couple of things:

First, a placeholder measure that the calculation group will overwrite completely.

![](https://miro.medium.com/v2/format:webp/1*VsJyfz7hvynUGM-UYeslLQ.png)

Second, a calculation group with two separate precooked calculation items (one for Revenue and the other for Revenue Share). The Revenue Share item returns the measure value only if the country is not in scope — meaning in the column subtotal section.

![](https://miro.medium.com/v2/format:webp/1*iE6Cl0v9ApB-on2ok9PPrA.png)

Third, we need to add the calculation group column into the Columns section of the matrix visual. A crucial caveat: add it as the primary attribute split — meaning it needs to be the first attribute; the country column comes afterwards.

![](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*zqyM6ZpjEKmUYp7G-nPS6Q.gif)

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----5f009d381b08---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** DAX, Data Visualization

**Tags:** Tutorial, DAX, Data Visualization