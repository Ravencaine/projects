---
title: "How to use the ISOMITTED function in Microsoft Excel"
source: "https://search.app/SXnPi"
author: "search.app"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Build flexible Excel functions that automatically handle blanks, defaults, and overrides without messy nested IFs.

How to use the ISOMITTED function in Microsoft Excel Close Close By Tony Phillips Published Mar 15, 2026, 8:30 AM EDT Tony Phillips is an experienced Microsoft Office user with a dual-honors degree in Linguistics and Hispanic Studies. Prior to starting with How-to Geek in January 2024, he worked as a document producer, data manager, and content creator for over ten years, and loves making spreadsheets and documents in his spare time. Tony is also an academic proofreader, experienced in reading, editing, and formatting over 3 million words of personal statements, resumes, reference letters, research proposals, and dissertations. Before joining How-To Geek , Tony formatted and wrote documents for legal firms, including contracts, Wills, and Powers of Attorney. Tony is obsessed with Microsoft Office! He will find any reason to create a spreadsheet, exploring ways to add complex formulas and discover new ways to make data tick. He also takes pride in producing Word documents that look the part. He has worked as a data manager in a secondary school in the UK and has years of experience in the classroom with Microsoft PowerPoint. He loves to encounter problems in Microsoft Office and use his expertise and legal-level training to find solutions. Outside of the Microsoft world, Tony is a keen dog owner and lover, football fan, astrophotographer, gardener, and golfer. Sign in to your How-To Geek account Creating your own functions with LAMBDA is a major Excel power move, but these DIY tools lack the "smart" feel of Excel's built-in features. While functions like XLOOKUP often support optional arguments directly, LAMBDA functions don't automatically detect whether an argument is omitted—they usually have to rely on manual checks or additional logic. ISOMITTED bridges that gap. It gives your LAMBDA functions a way to spot missing arguments, allowing the formula to automatically pivot between standard defaults and custom overrides. To create custom functions for reuse, you must use the Name Manager in a desktop version of Excel or Excel for the web . Once defined, you can use them in the same workbook in Excel for Microsoft 365, Excel 2024, Excel for the web, and the latest versions of the Excel mobile and tablet apps. How the ISOMITTED function works It's a logical check At its core, ISOMITTED acts as a switch for your formulas. It checks whether a specific argument in your custom function is supplied or skipped. If the value is missing, the function returns TRUE; if it's present, it returns FALSE. Here's the syntax:  ISOMITTED can only be used inside a LAMBDA function —it can't be used on its own. The argument is the parameter from your LAMBDA function that you want to check. To use it effectively, follow these two rules: The brackets: To make an argument optional, wrap its name in square brackets inside the LAMBDA definition. This signals that the parameter can be omitted and allows ISOMITTED to detect when it isn't supplied. The double-check: Because users often point formulas to empty cells rather than leaving the argument truly missing, it's best practice to pair ISOMITTED with a blank check (="") using the OR function. ​​​​​ Let me show you a basic example before we look at some real-world use cases. Getting started with ISOMITTED The "hello world" example In this example, column A contains people's names, and in column B, you want to use a custom function to greet that person with "Hello, [name]". If there isn't a name in column A, you want the function to default to "Hello, Guest". Here are the steps you'll take: Open the Name Manager via the Formulas tab. Click New . In the Name field, name the custom function GreetUser , and in the Refers to field, type the following formula—which tells Excel to return "Hello, Guest" if the name argument is omitted, or "Hello, [name]" if it's present—and click OK :  Close However, if you then use this custom function in the Greeting column using a structured reference to the Name column ([@Name]), the formula doesn't revert to "Hello, Guest" in cell B3, even though A3 is blank.  This is because, on row 3, GreetUser technically has an argument—the reference to the Name column—so ISOMITTED returns FALSE. To fix this, in the Name Manager , you change the formula to:  Adding the OR function creates a two-tier safety net: ISOMITTED handles the structure: if you type =GreetUser() with no arguments, it returns TRUE and gives you the Guest default. name="" handles the content: if you point the formula to an empty cell, that check returns TRUE, triggering the same default. Close The temptation of one-off fixes When a specific row in your table needs a different calculation, your first instinct might be to simply click that cell and manually change the formula. However, this is considered bad practice for several reasons: If you need to update a column's logic later, you'll have to remember to find and manually fix every one-off cell you changed. It's almost impossible to spot a manual override in a table of 500 rows, leading to errors that are notoriously hard to audit. If you or a teammate accidentally drag a formula down from a standard row, your manual override will be overwritten and lost without warning. By using ISOMITTED, you keep your formulas 100% consistent across an entire column. You aren't breaking the formula for one row—you're teaching the formula how to handle different scenarios. Real-world use case 1: Defining a constant fallback value Handle optional modifiers without breaking your math ISOMITTED allows a function to perform a calculation using a hardcoded default value if a specific modifier is not provided in a helper column . Scenario: Most items in your table use a standard 8% tax rate. However, for the ergonomic mouse in the second row, you need to use the 10% rate in the TaxOverride column. First, create a New Name in the Name Manager called AddTax with the following formula in the Refers to field:  This tells Excel to multiply the price b

## Code / Examples

```
=ISOMITTED(argument)
```
```
=LAMBDA([name], IF(ISOMITTED(name), "Hello, Guest", "Hello, " & name))
```
```
=GreetUser([@Name])
```
```
=LAMBDA([name], IF(OR(ISOMITTED(name), name=""), "Hello, Guest", "Hello, " & name))
```
```
=LAMBDA(price, [rate], IF(OR(ISOMITTED(rate), rate=""), price * 1.08, price * (1 + rate)))
```
```
=AddTax([@Price], [@TaxOverride])
```
```
=LAMBDA(c_date, [buffer], IF(OR(ISOMITTED(buffer), buffer=""), c_date, c_date + buffer))
```
```
=GetShipDate([@CompletionDate], [@BufferOverride])
```


---
*Source: [search.app](https://search.app/SXnPi)*
