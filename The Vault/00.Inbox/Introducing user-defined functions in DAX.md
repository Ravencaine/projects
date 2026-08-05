---
title: "Introducing user-defined functions in DAX"
source: "https://www.sqlbi.com/articles/introducing-user-defined-functions-in-dax/"
author:
  - "[[Marco Russo & Alberto Ferrari]]"
published: 2025-09-16
created: 2026-08-04
description: "User-defined functions are a new and exciting feature in DAX. In this article, we outline the key concepts to understand before using them in Power BI proje"
Processed: "Unprocessed"
---
Although DAX is a functional language, it did not previously offer the option to let users define their own functions. Starting from the September 2025 version, it is possible to define functions, which are parametrized expressions that can be reused throughout the entire semantic model. This article explains how the functions work. Watch the related video to see the user interface for defining functions.

Functions can be used to share a common business logic within a semantic model, as well as between different models. You can get libraries of DAX user-defined functions at [https://daxlib.org/](https://daxlib.org/), a free open-source repository of model-independent DAX functions that you can easily import and use in your models.

The easiest way to learn about functions is to define them in a query and to check their result immediately. Here is a first example:

```
DEFINE
 
FUNCTIONSumTwoNumbers =(A,B )=> A +B
 
EVALUATE
    {SumTwoNumbers (10,20)}
```

| Value |
| --- |
| 30 |

The function definition includes the signature (the name and the parameters: *A*, *B*) and the function body (*A + B*), separated by the *\=>* symbol. To invoke the function, use the function name followed by the parameters, as you would for any native DAX function.

To avoid confusion, we always use Pascal case for user-defined functions. This allows us to distinguish between predefined DAX functions, which are always uppercase, and user-defined functions, which use Pascal casing.

When defining parameters, we have the option to choose the parameter type, subtype, and parameter-passing mode. The most crucial detail is the parameter-passing mode; we dedicate a specific section to this topic later on in the chapter. There are two parameter-passing modes, and the choice of parameter-passing mode significantly impacts the function’s behavior. In contrast, the parameter type and subtype are less relevant.

The parameter-passing modes are:

- **VAL**: Short for *Value*. Indicates a parameter that is evaluated before the function call, in the evaluation context of the caller. A *VAL* parameter has a single and well-defined value during the execution of the function body. Multiple evaluations of the same parameter always produce the same result.
- **EXPR**: short for *Expression*. Indicates a parameter that is an expression, evaluated in the evaluation context where it is being used in the function body. Multiple evaluations of an *EXPR* parameter may (and oftentimes do) lead to different results.

The parameter-passing mode can be added to parameters with a colon sign (*:*), as in the following definition:

Function

```
FUNCTIONSumTwoNumbers =(A : Val,B : Expr )=> A +B
```

[Copy](#) [Conventions](#)

Developers can also specify the type of parameters, choosing among a broad range of options, listed in the following table.

| Type | Subtype | Passing mode | Remarks |
| --- | --- | --- | --- |
| ANYVAL |  | VAL | No restriction, any expression can be used. This is the default. |
| SCALAR |  | VAL / EXPR | Any scalar value, like an integer or a string; tables cannot be used |
|  | VARIANT | VAL / EXPR | Scalar expression, any data type is fine. |
|  | INT64 | VAL / EXPR | Scalar expression, the data type must be Integer. |
|  | DECIMAL | VAL / EXPR | Scalar expression, the data type must be Fixed Decimal. |
|  | DOUBLE | VAL / EXPR | Scalar expression, the data type must be Decimal. |
|  | STRING | VAL / EXPR | Scalar expression, the data type must be String. |
|  | DATETIME | VAL / EXPR | Scalar expression, the data type must be Date or DateTime. |
|  | BOOLEAN | VAL / EXPR | Scalar expression, the data type must be Boolean. |
|  | NUMERIC | VAL / EXPR | Scalar expression, the data type must be Integer. |
| TABLE |  | VAL / EXPR | Any table expression, scalars are not allowed. |
| ANYREF |  | EXPR | A reference to any table, column, measure, or calendar. |

The parameter type can be added along with the parameter-passing mode, like in the following example:

Function

```
FUNCTIONSumTwoNumbers =(
    a : SCALARVAL,
    b : SCALAREXPR
)=> a +b
```

[Copy](#) [Conventions](#)

Functions use automatic casting of parameters, meaning that the expressions used to instantiate the parameters are cast (converted) to the required data type. Automatic casting may cause some confusion, and it warrants further explanation.

Let us define a function whose expected parameter data type is an integer. When the function is evaluated with integers, everything works as expected. For example, passing three and two produces the expected result of five:

```
DEFINE
FUNCTIONSumTwoNumbers =(
    a : INT64VAL,
    b : INT64VAL
)=> a +b
 
EVALUATE
{
    SumTwoNumbers(3,2)
}
```

| Value |
| --- |
| 5 |

However, if the function is invoked by passing two decimal numbers, no error occurs because of automatic casting. Indeed, each argument is automatically converted to the required data type before evaluating the function:

```
DEFINE
FUNCTIONSumTwoNumbers =(
    a : INT64VAL,
    b : INT64VAL
)=> a +b
 
EVALUATE
{
    SumTwoNumbers(3.4,2.4),-- evaluates INT ( 3.4 ) + INT ( 2.4 )
    SumTwoNumbers("3.4","2.4")-- evaluates INT ( "3.4" ) + INT ( "2.4" )
}
```

| Value |
| --- |
| 5 |
| 5 |

Even though the sum of the decimal numbers should be 5.8 (which, rounded to an integer, would be six), because each parameter is separately cast to an integer, the result of 3+2 is five.

## Understanding parameter-passing modes

The parameter-passing mode can be added to parameters with a colon sign (:), as in the following definition:

```
DEFINE
FUNCTIONSumTwoNumbers =(a : VAL,b : VAL)=> a +b
 
EVALUATE
    {SumTwoNumbers(10,20)}
```

| Value |
| --- |
| 30 |

In the function defined above, both *a* and *b* are value parameters. By default, arguments of functions are value parameters. However, it is possible to use *EXPR* to force them to be treated as expressions. The difference is very important to understand because using the wrong parameter-passing mode is likely to generate glitches in your code that are hard to debug.

The caller evaluates value parameters before the function is executed. The function receives the value of the parameter as an argument and uses it for its own purposes. A value parameter is like a variable definition: the formula used by the caller produces a value; this value is assigned to a variable, and then the function is executed. Consider the following function:

Function

```
FUNCTIONSumTwoNumbers =(a : VAL,b : VAL)=> a +b
```

[Copy](#) [Conventions](#)

Because the parameters are both *VAL* parameters, the code is transformed as follows:

```
--
-- When the function is invoked with two arguments like this:
--
    SumTwoNumbers(
        SUM(Sales[Net Price]),
        SUM(Sales[Quantity])
    )
--
-- The code being executed is equivalent to this:
--
    VARa =SUM(Sales[Net Price])
    VARb =SUM(Sales[Quantity])
    RETURN
        a +b
```

[Copy](#) [Conventions](#)

On the other hand, expression parameters are not evaluated by the caller. Expression parameters are passed as formulas, and they are evaluated every time the function uses them. An expression parameter can have different values in different parts of the function body, depending on the evaluation context that is active when the parameter is evaluated. The following is the same *SumTwoNumbers* function we used earlier, this time with expression parameters (*EXPR*):

Function

```
FUNCTIONSumTwoNumbers =(a : EXPR,b : EXPR)=> a +b
```

[Copy](#) [Conventions](#)

Because the parameters are both *EXPR* parameters, the code is equivalent to the following:

```
--
-- When the function is invoked with two arguments like this:
--
    SumTwoNumbers(
        SUM(Sales[Net Price]),
        SUM(Sales[Quantity])
    )
--
-- The code being executed is equivalent to this:
--
    SUM(Sales[Net Price])+SUM(Sales[Quantity])
```

[Copy](#) [Conventions](#)

In the example we have shown so far, there are no differences in the result of the function, whether one uses the *VAL* or *EXPR* parameters. However, in most cases, determining the correct passing mode depends on the function’s semantics, which has a profound impact on the function’s behavior.

Using *VAL* parameters is the default, and you should use *VAL* (implicitly or explicitly, but we suggest always being explicit) whenever the function expects a specific value to work with. *EXPR* parameters are required when the function evaluates an expression in a potentially different context and produces different results based on the function’s logic. Let us see this through an example.

The following function aims at computing an expression, limiting the calculation to only the red products. The function does not work as intended because the parameter-passing mode is *VAL* by default, but the function requires an *EXPR* parameter to work correctly:

Function

```
FUNCTIONComputeForRed =(amount )=>
    CALCULATE(
        amount,
        'Product'[Color]="Red"
    )
```

[Copy](#) [Conventions](#)

Suppose we invoke the function passing the *Sales Amount* measure as the *amount* argument. In that case, the code is transformed with a variable, vanishing the effect of the change in the filter context operated by [CALCULATE](https://dax.guide/calculate/?aff=sqlbi):

```
--
-- When the function is invoked with an argument like this:
--
    ComputeForRed([Sales Amount])
--
-- The code being executed is equivalent to this:
--
    VARamount =[Sales Amount]
    RETURN
        CALCULATE(
            amount,
            'Product'[Color]="Red"
        )
```

[Copy](#) [Conventions](#)

The function body of *ComputeForRed* evaluates the parameter inside [CALCULATE](https://dax.guide/calculate/?aff=sqlbi), where it changes the filter context to force the product color to be Red. However, with a *VAL* parameter, the evaluation of the argument occurs before the function is executed. In the previous code snippet, we used the *amount* variable to mimic this behavior. Since the parameter is constant, it remains unchanged regardless of the filter context. Despite the function body evaluating the parameter in a filter context that filters only red products, the result is the *Sales Amount* for all the visible product colors.

Changing the parameter-passing mode to *EXPR* makes the function work smoothly:

Function

```
FUNCTIONComputeForRed =(amountExpr : EXPR)=>
    CALCULATE(
        amountExpr ,
        'Product'[Color]="Red"
    )
```

[Copy](#) [Conventions](#)

Let us elaborate further on the topic through a more realistic example. We create a table function that returns the best customers based on a metric. A customer is considered best if the value for the metric of the customer itself is larger than the average value of the metric for all the customers. We want the metric to be one of the parameters of the function. Here is a query that defines and executes the BestCustomers function:

```
DEFINE
FUNCTIONBestCustomers =(metricExpr : EXPR)=>
    VARAverageMetric =AVERAGEX(Customer,metricExpr )
    VARBestCustomersResult =
        FILTER(
            Customer,
            metricExpr > AverageMetric
        )
    RETURN
        BestCustomersResult
EVALUATE
    BestCustomers([Sales Amount])
```

There are several details worth mentioning in this code:

- *metricExpr* is an *EXPR* parameter; it is evaluated every time it is invoked. In the function body, two different iterators reference *metricExpr*; therefore, *metricExpr* will be evaluated for every row in every iterator.
- *metricExpr* is evaluated inside [AVERAGEX](https://dax.guide/averagex/?aff=sqlbi), once per customer, in the definition of the *AverageMetric* Please note that the evaluation occurs during an iteration over the *Customer*, where [AVERAGEX](https://dax.guide/averagex/?aff=sqlbi) creates a row context. Hence, *metricExpr* is evaluated in a row context.
- *metricExpr* is evaluated again inside the [FILTER](https://dax.guide/filter/?aff=sqlbi) iteration while computing *BestCustomers*. In this scenario, there is a different row context, this time created by [FILTER](https://dax.guide/filter/?aff=sqlbi). Therefore, *metricExpr* is evaluated once per customer in the row context created by [FILTER](https://dax.guide/filter/?aff=sqlbi).

The *metricExpr* parameter is evaluated multiple times, under different evaluation contexts. Consequently, it produces different results each time it is evaluated. This is not by chance. We do need *metricExpr* to produce different results for the function to work. Indeed, *metricExpr* is invoked in two different row contexts during two distinct iterations, and it needs to evaluate the sales of the customer being iterated through the context transition every time.

The function produces the correct result; once executed, the result contains 1,807 customers, some of which are shown in the following screenshot.

![](99.System/Attachments/image1-118.png)

Changing the parameter type to *VAL* produces an empty result. The following query returns an empty table, and the only difference between the previous version and this one is the parameter-passing mode.

```
DEFINE
FUNCTIONBestCustomers =(metricVal : VAL)=>
    VARAverageMetric =AVERAGEX(Customer,metricVal )
    VARBestCustomersResult =
        FILTER(
            Customer,
            metricVal > AverageMetric
        )
    RETURN
        BestCustomersResult
EVALUATE
    BestCustomers([Sales Amount])
```

The reason for the empty result is that a value parameter is evaluated once at the invocation of the function and then never again. Every time the function accesses the parameter, it obtains the same result, regardless of the evaluation context in which it is being used.

In the *VAL* example, the *Sales Amount* measure is evaluated before the *BestCustomers* function is invoked. Therefore, the *metricVal* parameter contains the total value of *Sales Amount* for all customers. Then, when the function runs, *AverageMetric* produces the average of all identical values (because *metricVal* is no longer evaluated, just read). Finally, [FILTER](https://dax.guide/filter/?aff=sqlbi) does not return any results because the condition checks that a value is strictly greater than itself, resulting in FALSE for all rows. In the previous EXPR example, every time there is a *metricExpr* reference, the *Sales* *Amount* measure is evaluated, as if *metricExpr* were replaced by the *Sales Amoun* t measure reference. This produces the expected result.

Using *VAL* parameters is the default behavior because it is the most intuitive way to use parameters. However, in many functions, it is helpful to inject part of the code through *EXPR* parameters, as demonstrated in the last two examples.

When using expression parameters, we must pay close attention to how the function utilizes the parameter. For example, let us modify the query code. This time, we still use an expression parameter, but we use [SUMX](https://dax.guide/sumx/?aff=sqlbi) instead of the *Sales Amount* measure when invoking the function:

```
DEFINE
FUNCTIONBestCustomers =(metricExpr : EXPR)=>
    VARAverageMetric =AVERAGEX(Customer,metricExpr )
    VARBestCustomersResult =
        FILTER(
            Customer,
            metricExpr > AverageMetric
        )
    RETURN
        BestCustomersResult
EVALUATE
    BestCustomers(SUMX(Sales,Sales[Quantity]*Sales[Net Price]))
```

Quite surprisingly, this query returns an empty table. This time, finding the issue requires a bit more effort because the parameter is set to the correct type; therefore, the problem is elsewhere. Indeed, the problem this time is the missing context transition within the iterations.

In the previous EXPR example, the argument of *BestCustomers* was a measure reference, *Sales Amount*. In the last EXPR example, we used a simple formula involving [SUMX](https://dax.guide/sumx/?aff=sqlbi), which corresponds to the definition of the *Sales Amount* measure. When we used a measure reference as a *metricExpr* argument, an implicit context transition occurred every time a reference to the *metricExpr* parameter was made in the *BestCustomers* function, and the code worked as expected. By using the [SUMX](https://dax.guide/sumx/?aff=sqlbi) expression, the context transition does not happen because the implicit [CALCULATE](https://dax.guide/calculate/?aff=sqlbi) around the measure reference is missing.

Parameters are not like measures: there is no automatic context transition happening. Because there is no context transition, the evaluation of the expression is not influenced by the row context created by [FILTER](https://dax.guide/filter/?aff=sqlbi) and [AVERAGEX](https://dax.guide/averagex/?aff=sqlbi). The difference between measures and expressions in EXPR arguments is crucial because it gives functions more control and flexibility, potentially improving performance if used effectively. Still, it must be managed carefully to avoid unexpected results.

To restore the correct code behavior, it is necessary to use [CALCULATE](https://dax.guide/calculate/?aff=sqlbi) explicitly:

```
DEFINE
FUNCTIONBestCustomers =(metricExpr : EXPR)=>
    VARAverageMetric =AVERAGEX(Customer,metricExpr )
    VARBestCustomersResult =
        FILTER(
            Customer,
            metricExpr > AverageMetric
        )
    RETURN
        BestCustomersResult
EVALUATE
    BestCustomers(CALCULATE(SUMX(Sales,Sales[Quantity]*Sales[Net Price])))
```

Adding the external [CALCULATE](https://dax.guide/calculate/?aff=sqlbi) forces a context transition, causing the query to return 1,807 customers. However, when writing functions, we must pay special attention to these details. Instead of changing the way the function is invoked, it is better to modify the function code to activate the context transition when needed. In our example, it is enough to add [CALCULATE](https://dax.guide/calculate/?aff=sqlbi) every time *metricExpr* is evaluated in a row context, to make it clear that we need the context transition:

```
DEFINE
FUNCTIONBestCustomers =(metricExpr : EXPR)=>
    VARAverageMetric =AVERAGEX(Customer,CALCULATE(metricExpr ))
    VARBestCustomersResult =
        FILTER(
            Customer,
            CALCULATE(metricExpr )> AverageMetric
        )
    RETURN
        BestCustomersResult
EVALUATE
    BestCustomers(SUMX(Sales,Sales[Quantity]*Sales[Net Price]))
```

This version of the function works regardless of the parameter it receives; either a formula or a measure will work just fine. When the context transition is required, it is forced by the function code through an explicit [CALCULATE](https://dax.guide/calculate/?aff=sqlbi). This may seem like a small detail, but it is the difference between a function written by a newbie and a function written by a DAX professional. A professional ensures that the function works even when it is used in an unexpected way.

Finally, when writing functions, it is always a good idea to optimize the code by writing it in the most efficient way possible. The reason is that functions are expected to be called by several measures and other functions; therefore, writing optimal code may have a profound impact on the semantic model performance. This last version of the function reduces the number of executions of the metric by consolidating the result of *metricExpr* for each customer into a variable:

```
DEFINE
FUNCTIONBestCustomers =(metricExpr : EXPR)=>
    VARCustomersAndMetric =
        ADDCOLUMNS(
            Customer,
            "@Metric",CALCULATE(metricExpr )
        )
    VARAverageMetric =AVERAGEX(CustomersAndMetric,[@Metric])
    VARBestCustomersResult =
        FILTER(
            CustomersAndMetric,
            [@Metric]> AverageMetric
        )
    RETURN
        BestCustomersResult
EVALUATE
    BestCustomers(SUMX(Sales,Sales[Quantity]*Sales[Net Price]))
```

## Conclusions

User-defined functions are valuable resources for DAX developers. By creating functions, developers can compartmentalize model code into smaller, manageable segments that facilitate independent testing and debugging. After thorough validation and optimization, each function becomes a building block that contributes to the overall robustness of the project.

When developing functions, it is essential to consider both parameter-passing modes and, specifically for expression parameters, to evaluate whether encapsulation with [CALCULATE](https://dax.guide/calculate/?aff=sqlbi) is necessary to support context transitions.

We cannot envision a future where a sophisticated semantic model possesses numerous measures and yet lacks user-defined functions. Traditionally, measures and calculation groups have handled calculation complexity, but this often leads to reduced performance and less readable code. User-defined functions provide an effective way to abstract complex calculations without sacrificing performance.

Context transition

Evaluates an expression in a context modified by filters.

`CALCULATE ( <Expression> [, <Filter> [, <Filter> [, … ] ] ] )`

Calculates the average (arithmetic mean) of a set of expressions evaluated over a table.

`AVERAGEX ( <Table>, <Expression> )`

Returns a table that has been filtered.

`FILTER ( <Table>, <FilterExpression> )`

Returns the sum of an expression evaluated for each row in a table.

`SUMX ( <Table>, <Expression> )`