---
title: "How to use the MAKEARRAY function in Microsoft Excel"
source: "https://search.app/YZp7T"
author: "search.app"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Switch from manual entries to automated generators that keep your spreadsheets clean, consistent, and error-free.

How to use the MAKEARRAY function in Microsoft Excel Close Close By Tony Phillips Published Mar 15, 2026, 7:30 AM EDT Tony Phillips is an experienced Microsoft Office user with a dual-honors degree in Linguistics and Hispanic Studies. Prior to starting with How-to Geek in January 2024, he worked as a document producer, data manager, and content creator for over ten years, and loves making spreadsheets and documents in his spare time. Tony is also an academic proofreader, experienced in reading, editing, and formatting over 3 million words of personal statements, resumes, reference letters, research proposals, and dissertations. Before joining How-To Geek , Tony formatted and wrote documents for legal firms, including contracts, Wills, and Powers of Attorney. Tony is obsessed with Microsoft Office! He will find any reason to create a spreadsheet, exploring ways to add complex formulas and discover new ways to make data tick. He also takes pride in producing Word documents that look the part. He has worked as a data manager in a secondary school in the UK and has years of experience in the classroom with Microsoft PowerPoint. He loves to encounter problems in Microsoft Office and use his expertise and legal-level training to find solutions. Outside of the Microsoft world, Tony is a keen dog owner and lover, football fan, astrophotographer, gardener, and golfer. Sign in to your How-To Geek account Imagine typing a single formula into cell A1 and watching it create a 100-cell grid without lifting a finger. No dragging, no clutter, no $ locking, and no errors. That's the power of MAKEARRAY. It uses a single, elegant formula to create dynamic, robust datasets in seconds. It's time to let Excel do the heavy lifting! MAKEARRAY is available in Excel for Microsoft 365, Excel for the web , and the most up-to-date Excel tablet and mobile apps. Understanding the MAKEARRAY function It's simpler than you think To use MAKEARRAY, think of it as telling Excel how big a grid to build and what value each cell should contain based on its row and column position. Excel then applies your logic to every coordinate in that grid. The syntax The MAKEARRAY formula is made up of these arguments:  where: rows and cols set the grid size. LAMBDA is the function applied to each cell in the grid. row and col are the parameter names (like r and c ) that track the current cell's position. calculation is the logic or math that determines the cell's value. The 10x10 grid example The best way to see MAKEARRAY in action is a standard multiplication table:  Excel fills the grid from row 1, column 1 (1 x 1) up to row 10, column 10 (10 x 10). Because MAKEARRAY is a dynamic array function, the result spills into adjacent cells , indicated by a blue line when you select the formula cell. Although Excel supports up to 16,384 columns and 1,048,576 rows , generating massive arrays with complex logic can cause performance lag. Example 1: Generating a random quality control batch Automating randomized data entry MAKEARRAY can populate a grid with randomized values or specific text labels. This is perfect for generating sample data, creating simulations, or testing templates. Scenario: You're a project manager who needs to create different-sized test grids of randomized quality control grades (A, B, or C) to simulate a batch inspection report. Instead of typing them manually, you can generate a new random set every time the sheet recalculates. Here's the formula:  Press Alt+Enter to split lengthy formulas over multiple lines , making them easier to write, read, and parse. This is what's happening: B1 and B2 reference cells containing the number of rows and columns. While you could hard-code these arguments, referencing them makes it easy to resize the grid without having to edit the formula. RANDBETWEEN(1, 3) picks a random whole number between 1 and 3 for every cell. Because RANDBETWEEN is a volatile function , the grid regenerates whenever Excel recalculates. CHOOSE maps each random number to a grade (1 = A, 2 = B, 3 = C). Example 2: Creating a tiered pricing grid Using external cell references for dynamic models MAKEARRAY can reference specific cells outside its own formula. This means you can build models in which changing a single input cell instantly updates the entire grid. Scenario A: You want to create a seating plan for a venue that charges different prices based on how close the seats are to the stage. A certain number of rows at the front are premium, and the remaining rows are standard. First, set up your parameters. Cell B1 contains the number of rows, B2 contains the number of seats per row, B3 indicates the number of premium rows, B4 contains the premium price, and B5 contains the standard price. Then, in cell D1 , enter this formula:  Close If the current row number is less than or equal to the value in B3 (premium rows), it returns the premium price ( B4 , $120.00). Otherwise, it returns the standard price ( B5 , $95.00). Scenario B: Let's imagine that you now want to offer a value tier to the back rows, so you tweak your parameters in column B to reflect this. To apply these parameters, the formula in cell D1 should be as follows:  Close This uses a nested IF statement to handle the extra logic: First, it checks if the row index ( r ) is less than or equal to B3 (premium rows). If true, it assigns the premium price ( B5 , $120.00). If false, it performs the second check: is the row less than or equal to B1-B4 ? This subtracts the number of discount rows ( B4 ) from the total rows ( B1 ) to find the mid-tier boundary. If true, it assigns the standard price ( B6 , $95.00). If both are false, it assigns the discount price ( B7 , $75.00). To make your price map easier to read, you can apply Conditional Formatting Color Scales ( Conditional Formatting > Color Scales ). However, Excel's "Applies to" field can't currently handle the dynamic spill operator (#), so to make it work, you'll need to anticipate the maximum size of 

## Code / Examples

```
=MAKEARRAY(rows, cols, LAMBDA(row, col, calculation))
```
```
=MAKEARRAY(10, 10, LAMBDA(r,c, r * c))
```
```
=MAKEARRAY(B1, B2,LAMBDA(r,c,CHOOSE(RANDBETWEEN(1, 3), "Grade A", "Grade B", "Grade C")))
```
```
=MAKEARRAY(B1, B2,LAMBDA(r,c,IF(r<=B3, B4, B5)))
```
```
=MAKEARRAY(B1, B2,LAMBDA(r,c,IF(r<=B3, B5, IF(r<=B1-B4, B6, B7))))
```
```
=MAKEARRAY(12,4,LAMBDA(r,c,1.05^((r-1)*c)))
```


---
*Source: [search.app](https://search.app/YZp7T)*
