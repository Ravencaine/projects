---
title: "I started using Python in Excel for boring tasks, and it completely changed my workflow"
source: "https://www.howtogeek.com/microsoft-excel-python-handle-spreadsheet-tasks-usually-put-off"
author: "www.howtogeek.com"
date: "2026-08-11"
tags: [imported, reading-list]
created: "2026-08-11"
---

> Python helped me replace fragile formulas and repetitive manual work with simple, reusable spreadsheet workflows.

I started using Python in Excel for boring tasks, and it completely changed my workflow Close Close By Tony Phillips Published Jul 27, 2026, 7:30 AM EDT Tony Phillips is an experienced Microsoft Office user with a dual-honors degree in Linguistics and Hispanic Studies. Prior to starting with How-to Geek in January 2024, he worked as a document producer, data manager, and content creator for over ten years, and loves making spreadsheets and documents in his spare time. Tony is also an academic proofreader, experienced in reading, editing, and formatting over 3 million words of personal statements, resumes, reference letters, research proposals, and dissertations. Before joining How-To Geek , Tony formatted and wrote documents for legal firms, including contracts, Wills, and Powers of Attorney. Tony is obsessed with Microsoft Office! He will find any reason to create a spreadsheet, exploring ways to add complex formulas and discover new ways to make data tick. He also takes pride in producing Word documents that look the part. He has worked as a data manager in a secondary school in the UK and has years of experience in the classroom with Microsoft PowerPoint. He loves to encounter problems in Microsoft Office and use his expertise and legal-level training to find solutions. Outside of the Microsoft world, Tony is a keen dog owner and lover, football fan, astrophotographer, gardener, and golfer. Sign in to your How-To Geek account Most people assume Python in Excel is something you use for complex data analysis. I found it useful for a much simpler reason: it helped me deal with the spreadsheet jobs I normally leave until later. Splitting messy names, comparing lists, and turning numbers into written insights became much easier without relying on complicated formulas or Power Query. What is Python in Excel, and why should you care? A simpler way to handle awkward spreadsheet jobs Close Python is built directly into Excel, meaning you don't need a separate Python installation to use the feature. When you run a Python formula, Excel executes the code in Microsoft's cloud infrastructure and returns the result straight to your cells. What's more, Python in Excel is designed to work with data from your worksheet or through Power Query, rather than accessing files directly from your computer. Python in Excel includes an Anaconda-provided environment containing popular libraries such as  , which makes manipulating and analyzing structured data much easier without requiring any setup. Think of Python in Excel less as learning a programming language and more as having another tool for handling the spreadsheet jobs that are difficult to solve with traditional formulas. While writing your own Python scripts takes some programming knowledge, you don't need that to get started. Every example below can be adapted to your own data, and I'll explain what each section of code does along the way. To try it out, you need a qualifying Microsoft 365 subscription and some data in your worksheet. Formatting your data as an Excel table ( Ctrl+T ) can make it easier to reference in Python, but you can also use cell ranges. Type  in a cell (or click Insert Python in the Formulas tab) to start writing Python code, then use  or  to bring your worksheet data into Python. Your results can then be returned directly to Excel cells. Python made my messy contact list easier to manage Handle the edge cases with ease Close One spreadsheet task I regularly found myself avoiding was splitting full names into separate first- and last-name columns. It sounds simple at first, but when the data includes middle initials, double-barreled names, or hyphenated surnames, things start to get messy. Traditional text formulas like LEFT, RIGHT, and FIND can handle straightforward examples, but the logic quickly becomes difficult to maintain when names don't follow the same pattern. Power Query is another option, but I found myself having to adjust the steps whenever the format of the names changed. Python gave me a way to define my own rules for this type of cleanup. This example uses a simple rule-based approach rather than attempting to handle every possible naming convention: Because I referenced an Excel table, the Python formula continues to use the updated table data. Add a new row to the table, and the result automatically refreshes to include it. Here's what's happening: Code What it does  Loads the standard data analysis library used for working with tables.  Pulls the Excel table named T_Names into Python.  Selects the first column of the imported table so Python can process each name individually.  Defines custom rules that treat the final word as the surname while preserving multi-word first names and hyphenated surnames.  Packages the final split names into two neat columns for Excel to display. Microsoft 365 Personal OS Windows, macOS, iPhone, iPad, Android Free trial 1 month Microsoft 365 includes access to Office apps like Word, Excel, and Pow

## Code / Examples

```
pandas
```
```
=PY(
```
```
xl("Table Name")
```
```
xl("Cell References")
```
```
import pandas as pd
```
```
df = xl("T_Names")
```


---
*Source: [www.howtogeek.com](https://www.howtogeek.com/microsoft-excel-python-handle-spreadsheet-tasks-usually-put-off)*
