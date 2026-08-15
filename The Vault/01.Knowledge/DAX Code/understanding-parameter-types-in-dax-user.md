---
title: "Understanding parameter types in DAX user"
source: "https://www.sqlbi.com/articles/understanding-parameter-types-in-dax-user-defined-functions-udf"
author: "www.sqlbi.com"
date: "2026-08-11"
tags: [imported, reading-list, dax]
created: "2026-08-11"
---

> This article describes the parameter types available in DAX user-defined functions, focusing on the specialized reference types MEASUREREF, COLUMNREF, TABLE

Understanding parameter types in DAX user-defined functions (UDF) - SQLBI In a previous article, Introducing user-defined functions in DAX , we described the syntax for creating user-defined functions, including the two passing modes (VAL and EXPR) and the fundamental parameter types SCALAR and TABLE. In this article, we build on that foundation and focus on the complete type system, with particular attention to the reference types introduced in March 2026 that provide better documentation, stronger validation, and improved IntelliSense support. Before diving into the new types, let us briefly recap the full picture of parameter types and passing modes available in DAX user-defined functions. Parameter types and passing modes Each parameter of a user-defined function has two properties: a type, which describes what kind of value the parameter accepts, and a passing mode, which describes how the value is transferred from the caller to the body of the function. The following table summarizes all the valid combinations. Type Passing mode ANYVAL VAL / EXPR SCALAR (*) VAL / EXPR TABLE VAL / EXPR ANYREF EXPR MEASUREREF EXPR COLUMNREF EXPR TABLEREF EXPR CALENDARREF EXPR SCALAR (*) Subtype VARIANT INT64 DECIMAL DOUBLE STRING DATETIME BOOLEAN NUMERIC SCALAR and TABLE are the two types that work with both VAL and EXPR. When no passing mode is specified, the default is VAL for both. ANYVAL is an abstract type for SCALAR and TABLE. Despite the name, it does not exactly restrict the passing mode. You could use ANYVAL as a shortcut for VAL for any data type; we discourage using ANYVAL with EXPR because of the confusion it could generate. All the remaining types (ending with “REF”) force the EXPR passing mode. The passing mode keyword can be omitted for these types because only EXPR is valid. The types in the lower part of the Type/Passing Mode table (MEASUREREF, COLUMNREF, TABLEREF, and CALENDARREF) are specializations of ANYREF. They share the same passing mode, but they restrict the kind of expression the caller can provide. These are the types we focus on in the rest of this article. ANYREF and its limitations ANYREF declares a parameter that accepts any expression and is always passed as an expression. It is the most permissive reference type: the function accepts whatever expression the caller provides: a measure reference, a column reference, a table reference, or an arbitrary DAX calculation. The expression provided is substituted into the body of the function wherever the parameter appears. It is important to highlight that a DAX formula is accepted by ANYREF as a valid argument: ANYREF should not be interpreted as “a reference to any existing object” but rather “a reference to any expression”. Writing ANYREF implies EXPR: writing ANYREF with or without EXPR has the same meaning and produces the same effects. This flexibility comes at a cost. Because ANYREF accepts anything, the function author cannot make assumptions about the nature of the expression. Is it a measure that triggers a context transition? Is it a simple column reference? Is it an arbitrary calculation? With ANYREF, the answer could be any of these. The function code must therefore be defensive : whether the expression may or may not trigger a context transition, the function author should use an explicit CALCULATE to ensure consistent behavior if a context transition is needed – something that would not be necessary if the parameter passed were a measure reference. The lack of specificity also affects the caller’s experience. IntelliSense and other development tools cannot provide meaningful guidance when the parameter accepts just any expression. The developer who calls the function must rely on documentation, or on reading the function body, to understand what is expected. When a parameter is declared as ANYREF, we recommend using the suffix Expr in the parameter name: for example, amountExpr or targetExpr . For example, here is a model-dependent function that filters customers whose purchase amount (provided as ANYREF) is greater than a minimum value ( lowerAmount ): Function  The Local.TopCustomersAnyRefA function can be used in three different versions of the AnyRef A measure: as a measure reference, as an expression, and as an expression embedded in CALCULATE , respectively. The expression used is the same as that defined in the Total Quantity measure: Measure in Sales table  Measure in Sales table  Measure in Sales table  Measure in Sales table  The second version of AnyRef A , which has an expression not embedded in CALCULATE , returns the same values as Sales Amount because the Local.TopCustomerAnyRefA function returns all customers: the result of the amountExpr argument is evaluated without filtering the iterated customer, since the context transition is missing. We can fix the function by embedding the amountExpr parameter in a CALCULATE , which is redundant but harmless when the argument is a measure reference. However, this would prev

## Code / Examples

```
Local.TopCustomersAnyRefA = ( amountExpr : ANYREF, lowerAmount : DOUBLE ) => FILTER ( Customer, amountExpr > lowerAmount )
```
```
Total Quantity = SUM ( Sales[Quantity] )
```
```
AnyRef-A 1 = CALCULATE ( [Sales Amount], Local.TopCustomersAnyRefA ( [Total Quantity], 20 ) )
```
```
AnyRef-A 2 = CALCULATE ( [Sales Amount], Local.TopCustomersAnyRefA ( SUM ( Sales[Quantity] ), 20 ) )
```
```
AnyRef-A 3 = CALCULATE ( [Sales Amount], Local.TopCustomersAnyRefA ( CALCULATE ( SUM ( Sales[Quantity] ) ), 20 ) )
```
```
Local.TopCustomersAnyRefB = ( amountExpr : ANYREF, lowerAmount : DOUBLE ) => FILTER ( Customer, CALCULATE ( amountExpr ) > lowerAmount )
```


---
*Source: [www.sqlbi.com](https://www.sqlbi.com/articles/understanding-parameter-types-in-dax-user-defined-functions-udf)*
