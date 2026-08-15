---
title: "Python Excel Automation: Batch Merge Multiple Excel Files"
source: "https://medium.com/@sirio1234/python-excel-automation-batch-merge-multiple-excel-files-ff2cee74f799"
author:
  - "[[Alle Y]]"
published: 2026-07-31
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Qds9Nm4Bk5sAl32w.png)

Merging Multiple Excel Files Using Python

In real-world work, data is often scattered across multiple Excel files — sales reports split by month, employee information organized by department, or order data tallied by region. When it comes time to consolidate and analyze, the first step is merging these files into a single workbook. Copying and pasting dozens of worksheets by hand is both time-consuming and error-prone; a single slip can lose formatting or miss data.

This article shows how to use Python to merge multiple Excel files (.xlsx and.xls) into one workbook. After merging, each source file’s worksheets are preserved under their original names and in their original order, with formatting and data fully intact — ready for sorting, filtering, or data analysis.

## Why Merge Excel Files with Code

Replacing manual merging with code brings three main benefits:

- **Batch processing** — Whether there are 3 files or 30, the process is identical, and everything completes in a single run
- **Format preservation** — Worksheets are copied along with cell styles, formulas, and other content, avoiding the formatting chaos caused by manual pasting
- **Reusable workflow** — The merging logic can be wrapped into a script and run on a weekly or monthly schedule, forming a stable data consolidation routine

## Environment Setup

This article uses the Spire.XLS for Python library, which can be installed with:

```c
pip install Spire.XLS
```

## Merging Multiple Excel Files

The core idea is simple: create a new workbook as the target, then load each source file in a loop and copy its worksheets one by one into the target workbook. The `AddCopy` method handles worksheet copying, and its second parameter, `WorksheetCopyType.CopyAll`, ensures that everything — data, formatting, formulas, and more — is copied along.

```c
from spire.xls import *
from spire.xls.common import *

# Files to merge
files = ["Sales_January.xlsx", "Sales_February.xlsx", "Sales_March.xls"]
# Create the target workbook and specify its version
newbook = Workbook()
newbook.Version = ExcelVersion.Version2013
# Clear the default worksheet to avoid a blank sheet in the result
newbook.Worksheets.Clear()
# Temporary workbook for loading source files one at a time
tempbook = Workbook()
for file in files:
    # Load the source file
    tempbook.LoadFromFile(file)
    # Copy each worksheet from the source file into the target workbook
    for sheet in tempbook.Worksheets:
        newbook.Worksheets.AddCopy(sheet, WorksheetCopyType.CopyAll)
# Save the merged result
newbook.SaveToFile("Merged.xlsx", ExcelVersion.Version2013)
newbook.Dispose()
tempbook.Dispose()
```

A few key points:

- A new `Workbook()` comes with an empty worksheet named "Sheet1"; calling `Worksheets.Clear()` removes it so the final file contains only the data actually merged in
- `LoadFromFile` automatically detects the.xlsx and.xls formats from the file content, so mixed-format files can be processed together
- Each loop iteration reloads a file and overwrites `tempbook`, so no matter how many files are merged, only one copy of source data stays in memory at a time
- Merged worksheets keep their original names and order, making it easy to tell where the data came from

## Merging Selected Worksheets

Sometimes you only need part of each file’s worksheets rather than all of them. Since the first argument of `AddCopy` accepts a worksheet object, you can grab the sheets you need by index and decide which ones to copy:

```c
from spire.xls import *
from spire.xls.common import *

newbook = Workbook()
newbook.Worksheets.Clear()
tempbook = Workbook()
# Load the first source file
tempbook.LoadFromFile("Sales_January.xlsx")
# Copy only the first two worksheets
newbook.Worksheets.AddCopy(tempbook.Worksheets[0], WorksheetCopyType.CopyAll)
newbook.Worksheets.AddCopy(tempbook.Worksheets[1], WorksheetCopyType.CopyAll)
newbook.SaveToFile("MergedSelected.xlsx", ExcelVersion.Version2013)
newbook.Dispose()
tempbook.Dispose()
```

This index-based approach suits scenarios where the file structure is fixed. If there are many source files with a uniform structure, you can also combine it with conditional logic to copy only the worksheets that meet certain criteria — for example, only sheets containing a specific keyword — enabling selective merging.

## Practical Tips

## Automatically Collecting Files with glob

Hard-coding the file list becomes cumbersome when there are many files. Instead, you can use the `glob` module from Python's standard library to match files by pattern:

```c
import glob

files = glob.glob("./reports/*.xlsx") + glob.glob("./reports/*.xls")
```

As long as you drop files into the specified directory, the script automatically collects all of them for merging — and you don’t need to touch the code when new files are added.

## Controlling the Output Version

The `ExcelVersion` enumeration controls the output format when saving: `Version2013` produces.xlsx files, while `Version2010` is compatible with Excel 2010 and later. If the merged result is going to colleagues who use older versions of Excel, choosing a lower version is the safer bet.

## Releasing Resources Promptly

`Workbook` objects consume system resources. In batch-processing scenarios, calling `Dispose()` after the work is done prevents memory from growing continuously during long-running processes.

## Conclusion

This article covered how to merge multiple Excel files with Python: create a target workbook and clear its default worksheet, load each source file in a loop, copy the worksheets into the target workbook with `AddCopy`, and finally save the result. This workflow fits common scenarios such as report consolidation and data archiving, bringing scattered data together into a single file.

Building on this foundation, you can also sort, filter, or format the worksheets before or after merging to create a more complete Excel automation pipeline.