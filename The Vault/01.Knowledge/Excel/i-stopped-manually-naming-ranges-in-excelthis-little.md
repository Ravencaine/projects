---
title: "I stopped manually naming ranges in Excel—this little"
source: "https://www.howtogeek.com/microsoft-excel-stopped-manually-naming-ranges-shortcut"
author: "www.howtogeek.com"
date: "2026-08-11"
tags: [imported, reading-list]
created: "2026-08-11"
---

> Create dozens of named ranges at once, write clearer formulas, and even update existing formulas automatically.

I stopped manually naming ranges in Excel—this little-known shortcut does it in seconds Close Close By Tony Phillips Published Aug 7, 2026, 6:30 AM EDT Tony Phillips is an experienced Microsoft Office user with a dual-honors degree in Linguistics and Hispanic Studies. Prior to starting with How-to Geek in January 2024, he worked as a document producer, data manager, and content creator for over ten years, and loves making spreadsheets and documents in his spare time. Tony is also an academic proofreader, experienced in reading, editing, and formatting over 3 million words of personal statements, resumes, reference letters, research proposals, and dissertations. Before joining How-To Geek , Tony formatted and wrote documents for legal firms, including contracts, Wills, and Powers of Attorney. Tony is obsessed with Microsoft Office! He will find any reason to create a spreadsheet, exploring ways to add complex formulas and discover new ways to make data tick. He also takes pride in producing Word documents that look the part. He has worked as a data manager in a secondary school in the UK and has years of experience in the classroom with Microsoft PowerPoint. He loves to encounter problems in Microsoft Office and use his expertise and legal-level training to find solutions. Outside of the Microsoft world, Tony is a keen dog owner and lover, football fan, astrophotographer, gardener, and golfer. Sign in to your How-To Geek account The best Excel formulas are the ones that explain themselves. That's why I use named ranges whenever I can. Creating them one by one, though, feels like unnecessary admin—especially in larger spreadsheets. Since discovering Ctrl+Shift+F3, it's become one of my most-used Excel shortcuts. I try to give everything in Excel a meaningful name Names make formulas easier to understand One of the biggest improvements I've made to my spreadsheets over the years is getting into the habit of replacing cryptic references with meaningful names wherever it makes sense. For Excel tables, I rely on structured references to give columns meaningful names. But for everything else, named ranges are often the better fit. It starts with small things. If I have a value that I reference throughout a workbook, I'll usually assign it a name instead of repeatedly referring to the same cell. In this example, I have a sales tax rate stored in an assumptions area of my workbook and want to use that rate to calculate the sales tax for each item in my data. A formula like:  works perfectly well, but I have to remember what $H$2 contains. After creating a name for that cell, the formula becomes:  Close Both formulas calculate the same result, but the second immediately tells me what that value represents, making the formula easier to review while helping others understand my workbook more quickly. Ctrl+Shift+F3 turns headings into named ranges A few seconds of setup can save minutes of manual work The one downside to named ranges is that creating them manually doesn't scale very well. If a workbook contains dozens of constants or reusable values, defining each one individually quickly becomes repetitive. That's where Ctrl+Shift+F3 comes in. Rather than typing every name one by one, Excel can generate them from the labels already added to the worksheet, provided each label sits directly beside the cell or range it describes. In this example, my worksheet contains several reusable values that I'll reference throughout my workbook. After selecting the entire range, labels included, I press Ctrl+Shift+F3 . Excel then asks where the labels are located. In my case, they're in the left-hand column, so I can check Left column and click OK . Close Within seconds, every label becomes a named range. To quickly check that everything worked correctly, I usually either open the Name Box drop-down or the Name Manager on the Formulas tab. Labels must follow Excel's naming rules Excel has fairly strict rules about what counts as a valid name, and in some cases, Create from Selection helps with this. As you can see in the example above, Excel automatically converted:  to:  However, there are some rules that the shortcut can't work around, so it's worth checking before you generate your names: Names must start with a letter or an underscore (_). After that, they can contain letters, numbers, periods, and underscores. Names can't look like cell references, like A1, R1C1, and Z100. Names can contain up to 255 characters, though that's unlikely to be a problem in most spreadsheets. Names aren't case-sensitive. Sales_Tax_Rate, SALES_TAX_RATE, and sales_tax_rate are all treated as the same name, so you can't create multiple names that differ only by capitalization. Writing formulas with names is much easier Excel even autocompletes them as you type Once the names are in place, I stop thinking about cell references altogether. Instead of remembering where a value lives, I simply refer to it by name. For example, if my table contains a colum

## Code / Examples

```
=D2*$H$2
```
```
=D2*Sales_Tax_Rate
```
```
Sales Tax Rate
```
```
Sales_Tax_Rate
```
```
Sales_Tax_Rate
```
```
Discount_Rate
```


---
*Source: [www.howtogeek.com](https://www.howtogeek.com/microsoft-excel-stopped-manually-naming-ranges-shortcut)*
