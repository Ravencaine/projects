---
title: "Introducing user"
source: "https://www.sqlbi.com/articles/introducing-user-defined-functions-in-dax"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> User-defined functions are a new and exciting feature in DAX. In this article, we outline the key concepts to understand before using them in Power BI proje

Introducing user-defined functions in DAX - SQLBI Although DAX is a functional language, it did not previously offer the option to let users define their own functions. Starting from the September 2025 version, it is possible to define functions, which are parametrized expressions that can be reused throughout the entire semantic model. This article explains how the functions work. Watch the related video to see the user interface for defining functions. Functions can be used to share a common business logic within a semantic model, as well as between different models. You can get libraries of DAX user-defined functions at https://daxlib.org/ , a free open-source repository of model-independent DAX functions that you can easily import and use in your models. The easiest way to learn about functions is to define them in a query and to check their result immediately. Here is a first example:  Value 30 The function definition includes the signature (the name and the parameters: A , B ) and the function body ( A + B ), separated by the => symbol. To invoke the function, use the function name followed by the parameters, as you would for any native DAX function. To avoid confusion, we always use Pascal case for user-defined functions. This allows us to distinguish between predefined DAX functions, which are always uppercase, and user-defined functions, which use Pascal casing. When defining parameters, we have the option to choose the parameter type, subtype, and parameter-passing mode. The most crucial detail is the parameter-passing mode; we dedicate a specific section to this topic later on in the chapter. There are two parameter-passing modes, and the choice of parameter-passing mode significantly impacts the function’s behavior. In contrast, the parameter type and subtype are less relevant. The parameter-passing modes are: VAL : Short for Value . Indicates a parameter that is evaluated before the function call, in the evaluation context of the caller. A VAL parameter has a single and well-defined value during the execution of the function body. Multiple evaluations of the same parameter always produce the same result. EXPR : short for Expression . Indicates a parameter that is an expression, evaluated in the evaluation context where it is being used in the function body. Multiple evaluations of an EXPR parameter may (and oftentimes do) lead to different results. The parameter-passing mode can be added to parameters with a colon sign ( : ), as in the following definition: Function  Developers can also specify the type of parameters, choosing among a broad range of options, listed in the following table. Type Subtype Passing mode Remarks ANYVAL VAL No restriction, any expression can be used. This is the default. SCALAR VAL / EXPR Any scalar value, like an integer or a string; tables cannot be used VARIANT VAL / EXPR Scalar expression, any data type is fine. INT64 VAL / EXPR Scalar expression, the data type must be Integer. DECIMAL VAL / EXPR Scalar expression, the data type must be Fixed Decimal. DOUBLE VAL / EXPR Scalar expression, the data type must be Decimal. STRING VAL / EXPR Scalar expression, the data type must be String. DATETIME VAL / EXPR Scalar expression, the data type must be Date or DateTime. BOOLEAN VAL / EXPR Scalar expression, the data type must be Boolean. NUMERIC VAL / EXPR Scalar expression, the data type must be Integer. TABLE VAL / EXPR Any table expression, scalars are not allowed. ANYREF EXPR A reference to any table, column, measure, or calendar. The parameter type can be added along with the parameter-passing mode, like in the following example: Function  Functions use automatic casting of parameters, meaning that the expressions used to instantiate the parameters are cast (converted) to the required data type. Automatic casting may cause some confusion, and it warrants further explanation. Let us define a function whose expected parameter data type is an integer. When the function is evaluated with integers, everything works as expected. For example, passing three and two produces the expected result of five:  Value 5 However, if the function is invoked by passing two decimal numbers, no error occurs because of automatic casting. Indeed, each argument is automatically converted to the required data type before evaluating the function:  Value 5 5 Even though the sum of the decimal numbers should be 5.8 (which, rounded to an integer, would be six), because each parameter is separately cast to an integer, the result of 3+2 is five. Understanding parameter-passing modes The parameter-passing mode can be added to parameters with a colon sign (:), as in the following definition:  Value 30 In the function defined above, both a and b are value parameters. By default, arguments of functions are value parameters. However, it is possible to use EXPR to force them to be treated as expressions. The difference is very important to understand because using the wrong parameter-passing mode is likely

## Code / Examples

```
DEFINE FUNCTION SumTwoNumbers = ( A, B ) => A + B EVALUATE { SumTwoNumbers ( 10, 20 ) }
```
```
FUNCTION SumTwoNumbers = ( A : Val, B : Expr ) => A + B
```
```
FUNCTION SumTwoNumbers = ( a : SCALAR VAL, b : SCALAR EXPR ) => a + b
```
```
DEFINE FUNCTION SumTwoNumbers = ( a : INT64 VAL, b : INT64 VAL ) => a + b EVALUATE { SumTwoNumbers( 3, 2 ) }
```
```
DEFINE FUNCTION SumTwoNumbers = ( a : INT64 VAL, b : INT64 VAL ) => a + b EVALUATE { SumTwoNumbers( 3.4, 2.4 ), -- evaluates INT ( 3.4 ) + INT ( 2.4 ) SumTwoNumbers( "3.4", "2.4" ) -- evaluates INT ( "3.4" ) + INT ( "2.4" ) }
```
```
DEFINE FUNCTION SumTwoNumbers = ( a : VAL, b : VAL ) => a + b EVALUATE { SumTwoNumbers( 10, 20 ) }
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/introducing-user-defined-functions-in-dax)*
