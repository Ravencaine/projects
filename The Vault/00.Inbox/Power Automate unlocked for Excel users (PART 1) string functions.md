---
title: "Power Automate unlocked for Excel users (PART 1): string functions"
source: "https://medium.com/@javidautomates/power-automate-unlocked-for-excel-users-string-functions-2dd27a0d2e2e"
author:
  - "[[Javid R.]]"
published: 2025-04-22
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*K2v25wOj2GvJ8jQ8nofz5Q.jpeg)

> Let’s be real for a moment. If you are reading this, you have probably spent countless hours in Excel doing the same things over and over again. Well, most of us have been there struggling with manual work sucking the life out of us. And again most of us have been there thinking “But there has to be a better way!”. The good news is: there IS a better way.

*To read the full story for free, click* [*here*](https://medium.com/@rzayevjavid/power-automate-unlocked-for-excel-users-string-functions-2dd27a0d2e2e?sk=4c85ee100264b299cbe62ad4634c95cc)*.*

Allow me to introduce you to: Power Automate. Microsoft’s this cloud-based automation platform can take your Excel expertise to the next level. I can list dozens of reasons to convince you to delegate your manual work in Excel to Power Automate, but I think you would just better research on your own a bit.

But know that, if you want to start to learn Power Automate, knowing Power Automate functions is important. Why? Because, a good flow design depends on preferring “functions” in your flows. And what I mean by design is not really about appearance because “actions” (*actions are basically steps in your flows* — *check here to S* [*tart a flow*](https://learn.microsoft.com/en-us/power-automate/overview-cloud) *+* [*Add an action*](https://learn.microsoft.com/en-us/power-automate/multi-step-logic-flow)) actually is better in terms of readability. But, after all you will realize preferring “actions” over functions affects your flows’ performance negatively.

To help you understand Power Automate functions, in this and next few blog posts, I will guide you through functions while drawing similarities with Excel functions. Let’s start with the string functions:

1. **Chunk**

Power Automate:

Splits text into equal-sized pieces.

```c
CHUNK(string, size)
```

Excel:

No direct equivalent. Either to use complex combination of functions or better — VBA in Excel.

2\. **Concat**

Power Automate:

Combines multiple strings.

```c
CONCAT(string1, [string2]...)
```

Excel:

CONCAT/CONCATANATE or & operator or TEXTJOIN

3\. **endsWith**

Power Automate:

Checks if string ends with specific characters.

```c
endsWith(string, searched_characters)
```

Excel:

IF(RIGHT(string; LEN(searched\_characters)) = searched\_characters; “True”; “False”)

4\. **formatNumber**

Power Automate:

Formats numbers with specific patterns.

```c
formatNumber(number, format, locale)
```

Excel:

TEXT

5\. **indexOf**

Power Automate:

Return the starting position of a text within another text.

```c
indexOf(text, searched_text)
```

Excel:

FIND (case-sensitive) or SEARCH (case-insensitive like indexOf)

6\. **isFloat**

Power Automate:

Checks if the string is a decimal number.

```c
isFloat(string, locale)
```

Excel:

IF(MOD(string,1)<>0; “True”; “False”)

7\. **isInt**

Power Automate:

Checks if the string is an integer number.

```c
isInt(string)
```

Excel:

IF(string=INT(string); “True”; “False”)

8\. **lastIndexOf**

Power Automate:

Return the starting position for the last occurrence of a text within another.

```c
lastIndexOf(text, searched_text)
```

Excel:

No direct equivalent. Either to use complex combination of functions or better — VBA in Excel.

9\. **length**

Power Automate:

Return the number of items/characters in a string.

```c
length(string)
```

Excel:

For strings: LEN.  
For arrays/ranges: COUNTA or COUNT

10\. **nthIndexOf**

Power Automate:

Return the starting position where the nth occurrence of a text appears in another.

```c
nthIndexOf(text, searched_text, occurrence)
```

Excel:

No direct equivalent. Either to use complex combination of functions or better — VBA in Excel.

11\. **replace**

Power Automate:

Replace character(s) with the new character(s), and return the updated text.

```c
replace(string, old_substring, new_substring)
```

Excel:

SUBSTITUTE

12\. **slice**

Power Automate:

Return a substring by specifying the starting and ending position.

```c
slice(text, start_index, end_index)
```

Excel:

MID

13\. **split**

Power Automate:

Return an array that contains substrings, separated by commas, from a larger string based on a specified delimiter character in the original string.

```c
split(text, separator)
```

Excel:

TEXTSPLIT

14\. **startsWith**

Power Automate:

Check whether string starts with a specific characters.

```c
endsWith(string, searched_characters)
```

Excel:

IF(LEFT(string; LEN(searched\_characters)) = searched\_characters; “True”; “False”)

15\. **substring**

Power Automate:

Return characters from a string, starting from the specified position.

```c
substring(text, start_index, length)
```

Excel:

MID

16\. **toLower**

Power Automate:

Return a string in lowercase format.

```c
toLower(string)
```

Excel:

LOWER

17\. **toUpper**

Power Automate:

Return a string in uppercase format.

```c
toUpper(string)
```

Excel:

UPPER

18\. **trim**

Power Automate:

Remove leading and trailing whitespace from a string, and return the updated string.

```c
trim(string)
```

Excel:

TRIM (only removes spaces unlike Power Automate function which removes all whitespace, like spaces, tabs, newlines)

Next in the series will be Collection Functions to deal with arrays.

*I will continue to show how to use Power Automate for your automation needs. If you find it interesting or you have questions, please let me know!*