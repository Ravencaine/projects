---
title: "Power Automate unlocked for Excel users (PART 2): collection functions"
source: "https://medium.com/@javidautomates/power-automate-unlocked-for-excel-users-part-2-collection-functions-7cb477d51e51"
author:
  - "[[Javid R.]]"
published: 2025-05-16
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*N5TAFHTgXs3TeoyP3bXnOg.jpeg)

> Let’s be real for a moment. If you are reading this, you have probably spent countless hours in Excel doing the same things over and over again. Well, most of us have been there struggling with manual work sucking the life out of us. And again most of us have been there thinking “But there has to be a better way!”. The good news is: there IS a better way.

*To read the full story for free, click* [*here*](https://medium.com/@rzayevjavid/power-automate-unlocked-for-excel-users-part-2-collection-functions-7cb477d51e51?sk=101105d87e4dc8c296fa0d556e7bed5d)*.*

In previous post, we had chance to get to know [string](https://medium.com/@rzayevjavid/power-automate-unlocked-for-excel-users-string-functions-2dd27a0d2e2e) functions — now we will focus on collection functions. In Power Automate, collection functions allow you to efficiently work with arrays. Whether you are processing data from Excel tables, SharePoint lists, or any dataset, these functions may help you to manipulate data without complex looping structures. Let’s explore the essential collection functions with examples and their Excel equivalents:

1\. **Chunk**

Power Automate:

This function breaks an array into smaller sub-arrays of equal size. When working with large datasets in Power Automate, chunking allows you to process data in manageable batches, especially helpful for API calls with size limitations.

chunk(array, size)

```c
// Break an array into chunks of 2 elements each
 chunk(['A', 'B', 'C', 'D', 'E', 'F'], 2)
// Result: [['A', 'B]', ['C', 'D'], ['E', 'F']]
```

Excel:

Either to use complex combination of functions or better — VBA in Excel

2\. **Contains**

Power Automate:

This function searches for specific items within an array, returning TRUE if the item exists.

contains(array, “item”)

```c
// Check if 'Power Automate' exists in an array
 contains(['Power Pages', 'Power Automate', 'Power Apps'], 'Power Automate')
// Result: true
```

Excel:

IF(COUNTIF(array; ”item”)>0; “True”; “False”)

3\. **Empty**

Power Automate:

This function evaluates whether an array has no elements, returning TRUE for empty arrays.

empty(array)

```c
// Check if array is empty
empty([])
// Result: true

// Check if array has elements
empty(['Power BI', 'Logic Apps'])
// Result: false
```

Excel:

IF(COUNTA(range) = 0; “TRUE”; “FALSE”)

4\. **First**

Power Automate:

It retrieves the first element from an array.

first(array)

```c
// Get first item from array
 first(['Power Platform', 'Power Automate', 'Power BI'])
// Result: 'Power Platform'
```

Excel:

INDEX(array;1;1)

5\. **Intersection**

Power Automate:

This function returns elements that exist in both arrays, creating a new array with just the common elements

intersection(array1, array2)

```c
// Find common elements between two arrays
 intersection(['A', 'B', 'C'], ['B', 'C', 'D'])
// Result: ['B', 'C']
```

Excel:

UNIQUE(FILTER(array1; ISNUMBER(MATCH(array1; array2; 0))))

6\. **Item**

Power Automate:

You can access the current item in a loop using the item() function:

item()

```c
// In an 'Apply to each' loop, access the current item
 item()

// Access specific property of the current item
 item()?['PropertyName']
```

Excel:

INDEX(array; SEQUENCE(ROWS(array)))

7\. **Join**

Power Automate:

This function combines all elements in an array into a single string with the specified delimiter.

join(array, delimiter)

```c
// Join array elements with a comma
 join(['SharePoint', 'Power Automate', 'Power BI'], ', ')
// Result: 'SharePoint, Power Automate, Power BI'
```

Excel:

TEXTJOIN(delimiter; ignore\_empty; text1; text2;..)

8\. **Last**

Power Automate:

It retrieves the last element from an array.

last(array)

```c
// Get the last item from array
 last(['SharePoint', 'Power Automate', 'Power BI'])
// Result: 'Power BI'
```

Excel:

INDEX(array; COUNTA(array); 1)

9\. **Reverse**

Power Automate:

It returns array in reversed order.

reverse(array)

```c
// Reverse the items in array
reverse(['Power', 'Automate', 'Desktop'])
// Result: ['Desktop', 'Automate', 'Power']
```

Excel:

No direct equivalent. Use VBA in Excel

10\. **Skip**

Power Automate:

This function omits items as much as count stated from the start of collection.

skip(array, count)

```c
//Remove items from start
skip(['SharePoint', 'Power Automate', 'Power BI', 'Power Apps'], 1)
//Result: ['Power Automate', 'Power BI', 'Power Apps']
```

Excel:

Either complex combination of functions or VBA in Excel.

11\. **Sort**

Power Automate:

It arranges array elements in ascending order: numbers from lowest to highest, words in alphabetical order, etc. For sorting objects in an array, you can use second parameter as well.

sort(array, \[sortBy\])

```c
// Sort an array of integers
 sort([3, 1, 2])
// Result: [1, 2, 3]

// Sort an array of objects
sort([{"first": "Marcello", "last": "Mastroianni"}, {"first": "Federico", "last": "Fellini"}], 'last')
// Result: [{"first": "Federico", "last": "Fellini" }, { "first": "Marcello", "last": "Mastroianni"}]
```

Excel:

SORT(array; \[sort\_index\]; \[sort\_order\]; \[by\_col\])

12\. **Take**

Power Automate:

This retrieves first N elements from the start of collection.

take(array, count)

```c
//Take first N elements
take([1,2,3,4,5,6,7,8], 3)
//Result: [1,2,3]
```

Excel:

INDEX(array; SEQUENCE(n))

13\. **Union**

Power Automate:

It combines two arrays removing duplicates.

union(array1, array2)

```c
// Combine two arrays
 union(['A', 'B', 'C'], ['C', 'D', 'E'])
// Result: ['A', 'B', 'C', 'D', 'E']
```

Excel:

UNIQUE(VSTACK(array1; array2))

Next in the series will be Logical Comparison to deal with conditions and comparison of values and also we will check Math Functions to work with integers and floating point numbers.

*I will continue to show how to use Power Automate for your automation needs. If you find it interesting or you have questions, please let me know!*