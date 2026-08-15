---
title: "You need to know what the hash sign does in Excel formulas"
source: "https://search.app/NK22j"
author: "search.app"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Smash the hash in a flash!

You need to know what the hash sign does in Excel formulas Close Close By Tony Phillips Published Mar 2, 2026, 2:09 PM EST Tony Phillips is an experienced Microsoft Office user with a dual-honors degree in Linguistics and Hispanic Studies. Prior to starting with How-to Geek in January 2024, he worked as a document producer, data manager, and content creator for over ten years, and loves making spreadsheets and documents in his spare time. Tony is also an academic proofreader, experienced in reading, editing, and formatting over 3 million words of personal statements, resumes, reference letters, research proposals, and dissertations. Before joining How-To Geek , Tony formatted and wrote documents for legal firms, including contracts, Wills, and Powers of Attorney. Tony is obsessed with Microsoft Office! He will find any reason to create a spreadsheet, exploring ways to add complex formulas and discover new ways to make data tick. He also takes pride in producing Word documents that look the part. He has worked as a data manager in a secondary school in the UK and has years of experience in the classroom with Microsoft PowerPoint. He loves to encounter problems in Microsoft Office and use his expertise and legal-level training to find solutions. Outside of the Microsoft world, Tony is a keen dog owner and lover, football fan, astrophotographer, gardener, and golfer. Sign in to your How-To Geek account Summary Excel spilled range operator (#) allows formulas to automatically adjust to changes in the spilled range size. You need to be using Excel for Microsoft 365 on Windows or Mac to make use of this handy tool. Well-known functions like UNIQUE, COUNTIF, and SORTBY can be used with the spilled range operator to generate dynamic, sortable lists. Using a hash symbol (#)—also known as a spilled range operator—in an Excel formula is a way to tell the program to consider all results in a spilled range. As a result, even if the spilled range grows or shrinks, the formula containing the # will automatically reflect this change. You can only take advantage of Excel's spilled range operator if you're using Excel for Microsoft 365 on Windows or Mac. Let's imagine you run an animal sanctuary, and your spreadsheet contains a formatted Excel table called Animals_Admitted, which shows the animals currently under your care. So that you can make the best use of the space you have at the sanctuary, you need to know how many of each type of animal you have, and how many different types of animals you have overall. Because the functions you're about to use produce spilled arrays, and spilled arrays don't work in formatted Excel tables, you need to type the formulas in areas of your spreadsheet that are not formatted as an Excel table. To see how many of each animal are currently in your sanctuary, in cells D1 and E1 (the cells above where your first spilled arrays will go), type the column headers Animal and Count , respectively. Now, in cell D2, type:  where UNIQUE is the Excel function that lists unique items in a range, Animals_Admitted is the name of the table where the original data sits, and [Animal] is the name assigned to the third column of that table. When you press Enter, you get a spilled array that lists each unique item in the Animal column. You know this is a spilled array because a blue line surrounds the result whenever you select one of the affected cells. The result of the UNIQUE function is sorted according to the order in which each item first appeared in the original data. Now, it's time to make Excel count how many of each animal there are in your original table, and this is where using the hash sign makes life a lot easier. To do this, you'll need to use the COUNTIF function . However, because you want Excel to count all the animals returned by the UNIQUE function in column D—even if certain animals are added to or removed from this list later on—you need to add a hash sign after the criteria reference. So, in cell E2, type:  where COUNTIF is the function that counts the number of occurrences, Animals_Admitted[Animal] is the range containing each animal in your original table, and D2# tells Excel that the criteria for the COUNTIF function are a spilled array starting in cell D2 and, thus, may change size. Instead of typing the formula manually, if you use your mouse to select the cells for each argument, the formula will automatically adopt the column names (also known as structured references ) and, where applicable, add the hash sign. Now, let's imagine that a hedgehog is brought into your sanctuary, and this hedgehog will be the only one currently under your care. To add an extra row to a formatted table, click and drag the handle in the bottom-right corner downwards. Because you referenced a formatted table heading in column D and used the spilled range operator in your COUNTIF formula in column E, the hedgehog is automatically added to the list in column D, and the hedgehog count in column E correctly shows as "1." Now, you want to create a list that sorts the animals by count. After typing the above headers into cells F1 and G1, in cell F2 type:  where SORTBY is the Excel function that sorts a range according to values in another range or array, D2#:E2# tells Excel that the array—which occupies columns D and E—contains two columns of spilled arrays starting at cells D2 and E2, E2# is the spilled array to sort on, and -1 tells Excel to sort the data in descending order. The result of the SORTBY function is first sorted according to the order you specified in the SORTBY formula. However, if any variables have the same values after this initial sort, they'll then be sorted according to the order in which each item first appeared in the original data. Because you used those hash signs in the formula, you can rest assured, safe in the knowledge that your lists will expand and contract dynamically according to the data in your original table. Finally, you also need a basic count of the

## Code / Examples

```
=UNIQUE(Animals_Admitted[Animal])
```
```
=COUNTIF(Animals_Admitted[Animal],D2#)
```
```
=SORTBY(D2#:E2#,E2#,-1)
```
```
=COUNTA(D2#)
```
```
=Sheet2!A1#
```


---
*Source: [search.app](https://search.app/NK22j)*
