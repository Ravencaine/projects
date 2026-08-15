---
title: "Creating DAX functions with AI to remove duplicated code"
source: "https://www.sqlbi.com/articles/creating-dax-functions-with-ai-to-remove-duplicated-code/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Marco Russo & Alberto Ferrari]]"
published: 2026-08-10
created: 2026-08-13
description: "Code written by AI can contain many duplicate parts. User-defined functions are a great tool to simplify complex measures; this article shows how to leverag"
Processed: "Unprocessed"
---
AI is getting better and better at generating DAX code, and as of today, it is pretty common to see rather complex DAX code that is entirely AI-generated. Sometimes AI-generated code requires refactoring or adjustment to make it more performant or reusable.

In this article, we show the process of first obtaining DAX code that actually works with AI, and then refactoring it to produce a better version. How do we refactor it? With AI, of course. AI can be a great tool if you ask it the right questions.

As an example, we are going to use the [New Customer](https://www.daxpatterns.com/new-and-returning-customers/) pattern. The prompt is deliberately simple and somewhat ambiguous, as it does not contain any clarification about what we mean by “new” customer, or how we want to generate the code. However, we are not interested in the algorithm but, rather, in the type of DAX code generated:

> Create two measures: I want to compute the new customers and then the sales of new customers

AI quickly answers with two measures:

Measure in Sales table

```
# New Customers =
VARFirstVisibleDate =
    MIN('Date'[Date])
VARLastVisibleDate =
    MAX('Date'[Date])
VARCustomersInCurrentPeriod =
    VALUES(Sales[CustomerKey])
VARNewCustomers =
    FILTER(
        CustomersInCurrentPeriod,
        VARCurrentCustomerKey =Sales[CustomerKey]
        VARFirstPurchaseDate =
            CALCULATE(
                MIN(Sales[Order Date]),
                REMOVEFILTERS(),
                TREATAS({CurrentCustomerKey },Customer[CustomerKey])
            )
        RETURN
            FirstPurchaseDate >=FirstVisibleDate
                && FirstPurchaseDate <=LastVisibleDate
    )
RETURN
    COUNTROWS(NewCustomers )
```

[Copy](#) [Conventions](#)

Measure in Sales table

```
Sales New Customers =
VARFirstVisibleDate =
    MIN('Date'[Date])
VARLastVisibleDate =
    MAX('Date'[Date])
VARCustomersInCurrentPeriod =
    VALUES(Sales[CustomerKey])
VARNewCustomers =
    FILTER(
        CustomersInCurrentPeriod,
        VARCurrentCustomerKey =Sales[CustomerKey]
        VARFirstPurchaseDate =
            CALCULATE(
                MIN(Sales[Order Date]),
                REMOVEFILTERS(),
                TREATAS({CurrentCustomerKey },Customer[CustomerKey])
            )
        RETURN
            FirstPurchaseDate >=FirstVisibleDate
                && FirstPurchaseDate <=LastVisibleDate
    )
RETURN
    CALCULATE(
        [Sales Amount],
        KEEPFILTERS(
            TREATAS(NewCustomers,Customer[CustomerKey])
        )
    )
```

[Copy](#) [Conventions](#)

AI being AI, the result is not always the same. However, most of the time it produces a similar algorithm. Despite not being super-duper optimized, this algorithm works fine, and it is not a bad solution for a small/medium data model.

As humans, we quickly notice that most of the code is duplicated. Both measures compute the *NewCustomers* variable; the first one just counts its rows, whereas the second uses the variable as a table filter in [CALCULATE](https://dax.guide/calculate/?aff=sqlbi). It is the perfect scenario where designing a user-defined function (UDF) would have been a great solution.

However, because of the final step, creating the function is not entirely obvious. A good DAX developer would solve the scenario immediately. What about AI? Let us test it:

> Both measures have a very similar logic, apart from the last step. Can you create a function that embeds most of the logic of new customers, so to produce simpler measures and put the DAX code at a common factor in the function?

AI decides to create a function for the *NewCustomers* variable only and, AI being AI, it decides to make the function as [model-independent](https://www.sqlbi.com/articles/model-dependent-and-model-independent-user-defined-functions-in-dax/) as possible, by passing the required columns as arguments. This is definitely a very good idea, but it also increases the number of parameters to call the function, unless we create a proxy:

Function

```
NewCustomersSet =(
    customerKey : COLUMNREF,
    orderDate : COLUMNREF,
    dateColumn : COLUMNREF
)=>
    VARFirstVisibleDate =MIN(dateColumn )
    VARLastVisibleDate =MAX(dateColumn )
    VARCustomersInCurrentPeriod =VALUES(customerKey )
    VARNewCustomers =
        FILTER(
            CustomersInCurrentPeriod,
            VARCurrentCustomerKey =customerKey
            VARFirstPurchaseDate =
                CALCULATE(
                    MIN(orderDate ),
                    REMOVEFILTERS(),
                    TREATAS({CurrentCustomerKey },customerKey )
                )
            RETURN
                FirstPurchaseDate >=FirstVisibleDate
                    && FirstPurchaseDate <=LastVisibleDate
        )
    RETURN
        NewCustomers
```

[Copy](#) [Conventions](#)

Indeed, despite the function being very generic, the measures are still quite complicated:

Measure in Sales table

```
# New Customers =
COUNTROWS(
    NewCustomersSet (
        Sales[CustomerKey],
        Sales[Order Date],
        'Date'[Date]
    )
)
```

[Copy](#) [Conventions](#)

Measure in Sales table

```
Sales New Customers =
VARNewCustomers =
    NewCustomersSet (
        Sales[CustomerKey],
        Sales[Order Date],
        'Date'[Date]
    )
RETURN
    CALCULATE(
        [Sales Amount],
        KEEPFILTERS(
            TREATAS(NewCustomers,Customer[CustomerKey])
        )
    )
```

[Copy](#) [Conventions](#)

We want to go one step further by simplifying the measures at the cost of generating a model-dependent UDF:

> I don’t want the function to use so many arguments. Create one function that accepts as its only parameter the formula to compute, and then returns the formula computed for only the new customers.

Now that our intentions are clearer, AI produces the desired code:

Function

```
NewCustomers =(
    expression : SCALAREXPR
)=>
    VARFirstVisibleDate =MIN('Date'[Date])
    VARLastVisibleDate =MAX('Date'[Date])
    VARCustomersInCurrentPeriod =VALUES(Sales[CustomerKey])
    VARNewCustomersSet =
        FILTER(
            CustomersInCurrentPeriod,
            VARCurrentCustomerKey =Sales[CustomerKey]
            VARFirstPurchaseDate =
                CALCULATE(
                    MIN(Sales[Order Date]),
                    REMOVEFILTERS(),
                    TREATAS({CurrentCustomerKey },Customer[CustomerKey])
                )
            RETURN
                FirstPurchaseDate >=FirstVisibleDate
                    && FirstPurchaseDate <=LastVisibleDate
        )
    RETURN
        CALCULATE(
            expression,
            KEEPFILTERS(
                TREATAS(NewCustomersSet,Customer[CustomerKey])
            )
        )
```

[Copy](#) [Conventions](#)

And the two measures are straightforward, as desired:

Measure in Sales table

```
# New Customers =
NewCustomers ([# Customers])
```

[Copy](#) [Conventions](#)

Measure in Sales table

```
Sales New Customers =
NewCustomers ([Sales Amount])
```

[Copy](#) [Conventions](#)

There are several non-trivial aspects to note here. First, when asked to refactor the function, AI actually changed the algorithm for *NewCustomers*, moving from [COUNTROWS](https://dax.guide/countrows/?aff=sqlbi) to [CALCULATE](https://dax.guide/calculate/?aff=sqlbi) with a filter. This is not an easy step at all. Moreover, when we requested simpler code, AI decided to reuse the *\# Customers* measure rather than keeping the old [COUNTROWS](https://dax.guide/countrows/?aff=sqlbi).

## Conclusions

AI is a great tool to author DAX code. Clearly, the code needs to be validated thoroughly before putting it in production. When using AI, a good practice is to ask exactly for what you want, so the code can be generated in a single pass and be good, straight out of the box.

User-defined functions are a great tool in Power BI to centralize code. When authoring code with AI, never forget to search for opportunities to use UDFs, as AI does not always use them. However, a human who can read and understand DAX can produce good results with minimal effort by using functions.

Context transition

Evaluates an expression in a context modified by filters.

`CALCULATE ( <Expression> [, <Filter> [, <Filter> [, … ] ] ] )`

Counts the number of rows in a table.

`COUNTROWS ( [<Table>] )`