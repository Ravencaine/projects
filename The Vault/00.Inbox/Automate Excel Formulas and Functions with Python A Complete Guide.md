---
title: "Automate Excel Formulas and Functions with Python: A Complete Guide"
source: "https://medium.com/@sirio1234/automate-excel-formulas-and-functions-with-python-a-complete-guide-e8eff4634d9e"
author:
  - "[[Alle Y]]"
published: 2026-07-10
created: 2026-08-04
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/0!PfvpQQvlWQehzubn.png.webp)

In modern data processing workflows, Excel formulas and functions are essential tools for performing calculations, analyzing data, and implementing business logic. However, manually entering and managing large numbers of formulas is not only time-consuming but also prone to errors. By automating Excel formula insertion and management with Python, developers can process spreadsheets in bulk, dynamically generate calculation logic, and ensure accuracy and consistency in data processing.

This article demonstrates how to use Python to insert various types of formulas and functions into Excel worksheets, including basic arithmetic operations, built-in functions, array formulas, and named ranges. These techniques are applicable to scenarios such as financial report automation, data analysis pipeline construction, and batch data processing.

## Environment Setup

First, install the Spire.XLS for Python library:

```c
pip install Spire.XLS
```

This library provides a comprehensive API for Excel file manipulation, supporting formula insertion, calculation execution, and file format conversion.

## Inserting Basic Formulas

Excel formulas begin with an equals sign (`=`) and can contain constants, cell references, operators, and function calls. When inserting formulas using Python, simply assign the formula string to the cell's `Formula` property.

The following example demonstrates how to insert various basic formulas into a worksheet:

```c
from spire.xls import *
from spire.xls.common import *

# Create a workbook
workbook = Workbook()
sheet = workbook.Worksheets[0]
# Set test data
sheet.Range["B2"].NumberValue = 7.3
sheet.Range["C2"].NumberValue = 5
sheet.Range["D2"].NumberValue = 8.2
# Insert string formula
sheet.Range["A4"].Text = '="hello"'
sheet.Range["B4"].Formula = '="hello"'
# Insert arithmetic formula
sheet.Range["A5"].Text = "=1+2+3+4+5-6-7+8-9"
sheet.Range["B5"].Formula = "=1+2+3+4+5-6-7+8-9"
# Insert multiplication operation
sheet.Range["A6"].Text = "=33*3/4-2+10"
sheet.Range["B6"].Formula = "=33*3/4-2+10"
# Reference other cells
sheet.Range["A7"].Text = "=Sheet1!$B$2"
sheet.Range["B7"].Formula = "=Sheet1!$B$2"
# Reference a cell range and calculate average
sheet.Range["A8"].Text = "=AVERAGE(Sheet1!$B$2:$D$2)"
sheet.Range["B8"].Formula = "=AVERAGE(Sheet1!$B$2:$D$2)"
# Save the file
workbook.SaveToFile("BasicFormulas.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

This example demonstrates:

- **String constants**: Text enclosed in double quotes
- **Arithmetic operations**: Support for addition, subtraction, multiplication, division, and operator precedence
- **Cell references**: Using the `$` symbol to create absolute references
- **Range references**: Using colons to specify continuous cell ranges

## Using Built-in Functions

Excel provides hundreds of built-in functions covering mathematics, statistics, date/time operations, logical operations, and text processing. Python allows flexible insertion of these functions.

## Mathematical and Statistical Functions

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
currentRow = 1
# COUNT function - count the number of arguments
sheet.Range[f"A{currentRow}"].Text = "=Count(3,5,8,10,2,34)"
sheet.Range[f"B{currentRow}"].Formula = "=Count(3,5,8,10,2,34)"
currentRow += 1
# SUM function - calculate sum
sheet.Range[f"A{currentRow}"].Text = "=SUM(18,29)"
sheet.Range[f"B{currentRow}"].Formula = "=SUM(18,29)"
currentRow += 1
# AVERAGE function - calculate average
sheet.Range[f"A{currentRow}"].Text = "=AVERAGE(12,45)"
sheet.Range[f"B{currentRow}"].Formula = "=AVERAGE(12,45)"
currentRow += 1
# MAX and MIN functions
sheet.Range[f"A{currentRow}"].Text = "=MAX(10,30)"
sheet.Range[f"B{currentRow}"].Formula = "=MAX(10,30)"
currentRow += 1
sheet.Range[f"A{currentRow}"].Text = "=MIN(5,7)"
sheet.Range[f"B{currentRow}"].Formula = "=MIN(5,7)"
currentRow += 1
# ROUND function - round numbers
sheet.Range[f"A{currentRow}"].Text = "=ROUND(7,3)"
sheet.Range[f"B{currentRow}"].Formula = "=ROUND(7,3)"
currentRow += 1
# SQRT function - square root
sheet.Range[f"A{currentRow}"].Text = "=SQRT(40)"
sheet.Range[f"B{currentRow}"].Formula = "=SQRT(40)"
currentRow += 1
workbook.SaveToFile("MathFunctions.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Date and Time Functions

Handling date and time data is a common requirement in Excel automation. The following code demonstrates how to use date and time functions:

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
# NOW function - current date and time
sheet.Range["A1"].Text = "=NOW()"
sheet.Range["B1"].Formula = "=NOW()"
sheet.Range["B1"].Style.NumberFormat = "yyyy-MM-DD HH:mm:ss"
# DATE function - construct a date
sheet.Range["A2"].Text = "=DATE(2024,1,15)"
sheet.Range["B2"].Formula = "=DATE(2024,1,15)"
sheet.Range["B2"].Style.NumberFormat = "yyyy-MM-DD"
# TIME function - construct a time
sheet.Range["A3"].Text = "=TIME(14,30,0)"
sheet.Range["B3"].Formula = "=TIME(14,30,0)"
sheet.Range["B3"].Style.NumberFormat = "HH:mm:ss"
# YEAR, MONTH, DAY functions - extract date components
sheet.Range["A4"].Text = "=YEAR(NOW())"
sheet.Range["B4"].Formula = "=YEAR(NOW())"
sheet.Range["A5"].Text = "=MONTH(NOW())"
sheet.Range["B5"].Formula = "=MONTH(NOW())"
sheet.Range["A6"].Text = "=DAY(NOW())"
sheet.Range["B6"].Formula = "=DAY(NOW())"
# HOUR, MINUTE, SECOND functions - extract time components
sheet.Range["A7"].Text = "=HOUR(NOW())"
sheet.Range["B7"].Formula = "=HOUR(NOW())"
sheet.Range["A8"].Text = "=MINUTE(NOW())"
sheet.Range["B8"].Formula = "=MINUTE(NOW())"
sheet.Range["A9"].Text = "=SECOND(NOW())"
sheet.Range["B9"].Formula = "=SECOND(NOW())"
workbook.SaveToFile("DateTimeFunctions.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Logical and Conditional Functions

Logical functions are used to implement conditional judgments and business rules:

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
# IF function - conditional judgment
sheet.Range["A1"].Text = '=IF(10>5, "Greater", "Less")'
sheet.Range["B1"].Formula = '=IF(10>5, "Greater", "Less")'
# AND function - logical AND
sheet.Range["A2"].Text = "=AND(TRUE, TRUE)"
sheet.Range["B2"].Formula = "=AND(TRUE, TRUE)"
# OR function - logical OR
sheet.Range["A3"].Text = "=OR(FALSE, TRUE)"
sheet.Range["B3"].Formula = "=OR(FALSE, TRUE)"
# NOT function - logical NOT
sheet.Range["A4"].Text = "=NOT(FALSE)"
sheet.Range["B4"].Formula = "=NOT(FALSE)"
workbook.SaveToFile("LogicFunctions.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Text Processing Functions

Text functions are used for string manipulation and data cleaning:

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
# LEN function - string length
sheet.Range["A1"].Text = '=LEN("Hello World")'
sheet.Range["B1"].Formula = '=LEN("Hello World")'
# MID function - extract substring
sheet.Range["A2"].Text = '=MID("Hello World",7,5)'
sheet.Range["B2"].Formula = '=MID("Hello World",7,5)'
# VALUE function - convert text to number
sheet.Range["A3"].Text = '=VALUE("123")'
sheet.Range["B3"].Formula = '=VALUE("123")'
workbook.SaveToFile("TextFunctions.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Using Array Formulas

Array formulas can perform calculations on multiple values and return either a single result or multiple results. This is particularly useful when executing matrix operations and batch data processing.

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
# Prepare data
sheet.Range["A1"].NumberValue = 1
sheet.Range["A2"].NumberValue = 2
sheet.Range["A3"].NumberValue = 3
sheet.Range["B1"].NumberValue = 4
sheet.Range["B2"].NumberValue = 5
sheet.Range["B3"].NumberValue = 6
sheet.Range["C1"].NumberValue = 7
sheet.Range["C2"].NumberValue = 8
sheet.Range["C3"].NumberValue = 9
# Insert array formula - LINEST function performs linear regression analysis
sheet.Range["A5:C6"].FormulaArray = "=LINEST(A1:A3,B1:C3,TRUE,TRUE)"
# Calculate all formula values
workbook.CalculateAllValue()
workbook.SaveToFile("ArrayFormulas.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

Key points:

- Use the `FormulaArray` property instead of `Formula` to insert array formulas
- Array formulas need to span multiple cell ranges
- Call the `CalculateAllValue()` method to ensure formulas are calculated correctly

## Using the SUBTOTAL Function

The SUBTOTAL function can perform aggregate calculations on data lists and ignore hidden rows, which is particularly useful when creating interactive reports.

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
# Prepare data
for row in range(1, 4):
    sheet.Range[f"A{row}"].NumberValue = row
    sheet.Range[f"B{row}"].NumberValue = row + 3
    sheet.Range[f"C{row}"].NumberValue = row + 6
# Insert different SUBTOTAL functions
# 1 represents AVERAGE
sheet.Range["A5"].Formula = "=SUBTOTAL(1,A1:C3)"
# 2 represents COUNT
sheet.Range["B5"].Formula = "=SUBTOTAL(2,A1:C3)"
# 5 represents MIN
sheet.Range["C5"].Formula = "=SUBTOTAL(5,A1:C3)"
# Calculate formulas
workbook.CalculateAllValue()
workbook.SaveToFile("SubtotalFormulas.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

The first parameter of the SUBTOTAL function specifies the calculation type:

- 1: AVERAGE
- 2: COUNT
- 3: COUNTA (count non-empty cells)
- 4: MAX
- 5: MIN
- 9: SUM

## Using Named Ranges and Formulas

Named ranges improve formula readability and maintainability. By replacing complex cell references with meaningful names, formulas become easier to understand.

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
# Set data
sheet.Range["A1"].Value = "10"
sheet.Range["A2"].Value = "20"
# Create a named range
namedRange = workbook.NameRanges.Add("SumRange")
namedRange.RefersToRange = sheet.Range["A1:A2"]
# Use the named range in a formula
sheet.Range["C1"].Formula = "=SUM(SumRange)"
# Alternatively, define a named formula directly
namedFormula = workbook.NameRanges.Add("TotalCalc")
namedFormula.NameLocal = "=SUM(A1+A2)"
sheet.Range["C2"].Formula = "TotalCalc"
workbook.SaveToFile("NamedRangeFormulas.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

The advantages of this approach include:

- **Improved readability**: `=SUM(SumRange)` is clearer than `=SUM(A1:A2)`
- **Easier maintenance**: Modifying the named range reference automatically updates all formulas using that name
- **Reduced errors**: Avoids manual entry of complex cell references

## Practical Tips

## Formatting Formula Cells

To distinguish formula cells from data cells, you can apply special formatting:

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
# Insert formula
sheet.Range["A1"].Formula = "=SUM(B1:B10)"
# Set background color for formula cell
sheet.Range["A1"].Style.Color = Color.get_LightYellow()
# Add borders
sheet.Range["A1"].Style.Borders[BordersLineType.EdgeTop].LineStyle = LineStyleType.Thin
sheet.Range["A1"].Style.Borders[BordersLineType.EdgeBottom].LineStyle = LineStyleType.Thin
workbook.SaveToFile("FormattedFormula.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Forcing Formula Calculation

In some cases, you may need to immediately obtain the calculated result of a formula rather than keeping the formula itself:

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]
sheet.Range["A1"].NumberValue = 10
sheet.Range["A2"].NumberValue = 20
sheet.Range["A3"].Formula = "=A1+A2"
# Calculate all formulas
workbook.CalculateAllValue()
# At this point, A3 value is already 30
result = sheet.Range["A3"].Value
print(f"Calculation result: {result}")
workbook.SaveToFile("CalculatedFormula.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Handling Cross-Sheet References

When formulas need to reference data from other worksheets, use the worksheet name followed by an exclamation mark:

```c
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
# Create two worksheets
sheet1 = workbook.Worksheets[0]
sheet1.Name = "Data"
sheet2 = workbook.Worksheets.Add("Calculation")
# Set data in the first worksheet
sheet1.Range["A1"].NumberValue = 100
sheet1.Range["A2"].NumberValue = 200
# Reference data from the first worksheet in the second worksheet
sheet2.Range["A1"].Formula = "=Data!A1+Data!A2"
workbook.CalculateAllValue()
workbook.SaveToFile("CrossSheetFormula.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Conclusion

This article has demonstrated various techniques for automating Excel formulas and functions using Python, including:

- Inserting basic arithmetic formulas and cell references
- Using mathematical, statistical, date/time, logical, and text processing functions
- Executing array formulas for complex calculations
- Leveraging the SUBTOTAL function for flexible aggregate calculations
- Improving formula readability and maintainability through named ranges

These techniques enable developers to:

- Generate spreadsheets with complex calculation logic in bulk
- Automate financial models and data analysis reports
- Dynamically build condition-based calculation formulas
- Improve consistency and accuracy in data processing

By combining Python’s programming capabilities with Excel’s calculation features, you can build powerful data processing automation solutions that significantly improve工作效率 and reduce human error.