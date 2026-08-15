---
title: "How to use the LAMBDA helper functions in Microsoft Excel"
source: "https://search.app/PDYaF"
author: "search.app"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Replace legacy formulas with MAP, BYROW, BYCOL, SCAN, and REDUCE to build secure, scalable, and automated spreadsheets.

How to use the LAMBDA helper functions in Microsoft Excel Close Close By Tony Phillips Published Feb 28, 2026, 11:30 AM EST Tony Phillips is an experienced Microsoft Office user with a dual-honors degree in Linguistics and Hispanic Studies. Prior to starting with How-to Geek in January 2024, he worked as a document producer, data manager, and content creator for over ten years, and loves making spreadsheets and documents in his spare time. Tony is also an academic proofreader, experienced in reading, editing, and formatting over 3 million words of personal statements, resumes, reference letters, research proposals, and dissertations. Before joining How-To Geek , Tony formatted and wrote documents for legal firms, including contracts, Wills, and Powers of Attorney. Tony is obsessed with Microsoft Office! He will find any reason to create a spreadsheet, exploring ways to add complex formulas and discover new ways to make data tick. He also takes pride in producing Word documents that look the part. He has worked as a data manager in a secondary school in the UK and has years of experience in the classroom with Microsoft PowerPoint. He loves to encounter problems in Microsoft Office and use his expertise and legal-level training to find solutions. Outside of the Microsoft world, Tony is a keen dog owner and lover, football fan, astrophotographer, gardener, and golfer. Sign in to your How-To Geek account Excel's LAMBDA helper functions are the future, but knowing which one to pick is the real challenge. This is your go-to whistle-stop guide for matching the function to the task and building spreadsheets that finally think for themselves. This article covers the five iterator and accumulator helper functions, which are available in Excel for Microsoft 365, Excel for the web , and the most up-to-date versions of the Excel mobile and tablet apps. SCAN is also available in Excel 2024. It doesn't cover the two other helper functions that serve different roles: MAKEARRAY (generator) and ISOMITTED (logical checker). The engine: A 30-second LAMBDA refresher Think of LAMBDA as a custom formula you write on the fly—instead of a fixed cell reference like A2*0.15, you define a parameter:  where: x is the parameter that represents the value the function will process. x*0.15 is the calculation you want Excel to perform on that parameter. On its own, this formula doesn't do much; it needs a driver to take that logic and apply it to your data. That's where the LAMBDA helper functions come into play. Excel tables don't support spilled results . If you try to place a dynamic array formula like MAP or SCAN inside one, you'll trigger a #SPILL! error . To avoid this, always place your LAMBDA helper functions in the standard grid. In this run-through, I'll use the following table—named T_Gadgets—as the data source and enter the formulas in regular cells next to or above it. The iterators (MAP, BYROW, BYCOL): Applying logic to every cell, row, or column Iterators walk through your table data and apply LAMBDA logic to each item. MAP: Apply logic to every single cell The syntax =MAP(array,LAMBDA(parameter,calculation)) The aim You want to calculate the revenue for each row in T_Gadgets and apply a 10% discount at the same time. The benefit The entire calculation lives in one place. This makes your logic more secure, as individual rows within the results can't be overwritten. Here's the MAP formula you need to type into cell F2:  where: Array: T_Gadgets[Units],T_Gadgets[Price] are the columns you want to process. Parameters: u,p are the parameters—a single unit and a price from each row. Calculation: u*p*0.9 multiplies the two values and applies a 10% discount. Use MAP to combine parallel columns; use BYROW (below) to treat each record as a single bundle of data. BYROW: Get a result for every row The syntax =BYROW(array,LAMBDA(row,calculation)) The aim You want to multiply the Units and Price in T_Gadgets horizontally to get the total revenue for each row (day). The benefit Instead of managing formulas across hundreds of rows, you manage one formula in a single cell that spills down, ensuring consistency across your dataset. The BYROW formula for cell F2 is as follows:  where: Array: T_Gadgets[[Units]:[Price]] is the range encompassing both columns. Parameter: row represents an entire horizontal row of data. Calculation: PRODUCT(row) multiplies every value found within that row. BYCOL: Get a result for every column The syntax =BYCOL(array,LAMBDA(column,calculation)) The aim You want a single formula that finds the maximum value for the Units and Price columns in T_Gadgets. The benefit By using BYCOL in a row above the table, you create a header summary. This saves you from having to scroll down to a Total Row at the bottom of a massive table, and condenses the logic into a single cell for security and consistency. Here's the BYCOL formula for cell A1:  where: Array: T_Gadgets[#Data] ensures the formula is horizontally scalable. If you add a new column, the formula detects it and spills further to the right. Parameter: col represents an entire vertical column. Calculation: IFERROR(MAX(col),"") finds the highest value in each column. The IFERROR wrapper is essential when using functions that trigger an error for text columns, such as AND and OR . Functions like MAX and SUM will often return 0 for a text column. To hide this value without breaking the formula's alignment, select the cell containing the zero, and in the Format Cells dialog (Ctrl+1), use the custom number format ;;; (three semicolons) to make the value invisible while keeping the cell functional. The accumulators (SCAN and REDUCE): Building results as you go Accumulators have memory, keeping a running tally as they move through your table. SCAN: Create a running total or running count The syntax =SCAN(initial_value,array,LAMBDA(accumulator,value,calculation)) The aim You want to see a daily running total of the Units column in T_Gadgets to track inventory

## Code / Examples

```
=LAMBDA(x,x*0.15)
```
```
=MAP(T_Gadgets[Units],T_Gadgets[Price],LAMBDA(u,p,u*p*0.9))
```
```
=BYROW(T_Gadgets[[Units]:[Price]],LAMBDA(row,PRODUCT(row)))
```
```
=BYCOL(T_Gadgets[#Data],LAMBDA(col,IFERROR(MAX(col),"")))
```
```
=SCAN(0,T_Gadgets[Units],LAMBDA(acc,val,acc+val))
```
```
=REDUCE(0,T_Gadgets[Units],LAMBDA(acc,val,IF(val>10,acc+val,acc)))
```


---
*Source: [search.app](https://search.app/PDYaF)*
