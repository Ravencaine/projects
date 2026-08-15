---
title: "Power Automate Desktop Tutorial: Building a Sequential Flow"
source: "https://medium.com/towardsdev/power-automate-desktop-tutorial-building-a-sequential-flow-21f0c4819ca5"
author:
  - "[[Mohamad Mahmood]]"
published: 2025-10-02
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*jTj0wpm_8093efVi)

**Power Automate Desktop (PAD)** is Microsoft’s tool for automating repetitive tasks on your computer. It allows you to build flows by dragging and dropping predefined actions such as opening files, reading data, clicking on buttons, or interacting with applications without writing code. PAD is especially useful for business users who want to save time and reduce errors by letting the computer handle routine steps automatically.

One of the most important concepts in PAD (and programming in general) is **sequential logic**. Sequential logic means that actions are executed in the exact order they are placed in the flow — top to bottom, step by step. Each step waits for the previous one to finish before starting. This is the simplest form of automation flow and is often the foundation upon which more complex branching (selection) or repetition (looping) logic is built.

## [Getting Started with Power Automate Desktop](https://medium.com/@mohamad.razzi.my/getting-started-with-power-automate-desktop-667f790b3b8a?source=post_page-----21f0c4819ca5---------------------------------------)

### Power Automate Desktop is a tool from Microsoft that allows users to automate repetitive tasks on their desktop. This…

medium.com

## Tutorial: Collect Name & DOB, Compute Age, Append to Log File in Power Automate Desktop

### Step 1: Initialize folder and file paths

Before writing to a file, it’s good practice to define the folder and file location as variables. This makes your flow easier to maintain (only one place to change if the folder moves).

- Action: **Set Variable** → `%FolderPath% = D:\pad`
- Action: **Set Variable** → `%FilePath% = %FolderPath%\users.log`

### Step 2: Ensure the target folder exists

If you try to write to a file in a folder that doesn’t exist, PAD will throw an error. This step guarantees the folder is created once.

- Action: **Create Folder** → Path: `%FolderPath%` → If folder exists: *Do nothing*.

### Step 3: Get user input (Name and DOB)

Use dialogs to ask the user for input. This ensures the automation collects information dynamically rather than hardcoding values.

- Action: **Display Input Dialog** → Title: `Enter your name` → Output: `%UserName%`
- Action: **Display Input Dialog** → Title: `Enter date of birth` → Message: `Enter in format YYYY-MM-DD` → Output: `%DobText%`

### Step 4: Convert DOB text into a date and get today’s date

Users will type DOB as plain text. To calculate age, you must convert it to a `DateTime` type. We also capture today’s date for comparison.

- Action: **Convert Text to Datetime** → Input: `%DobText%` → Format: `yyyy-MM-dd` → Output: `%Dob%`
- Action: **Get Current Date and Time** → Output: `%Today%`

### Step 5: Compute the user’s age

We now have two dates (`DOB` and `Today`). Subtract them to get age. PAD has a built-in function to compute the difference in years.

- Action: **Get Difference Between Dates** → First: `%Dob%` → Second: `%Today%` → Interval: Years → Output: `%AgeYears%`

*(Alternative: If your PAD doesn’t support “Years” directly, break down into year/month/day components and adjust for birthdays not yet passed this year.)*

At this stage, you can test the steps above by running the flow. Check the variable panel to see the values that have been collected and processed so far.

### Step 6: Check if the log file exists, create if missing

The file may not exist the first time you run the automation. By checking first, we avoid errors. Optionally, we can add a header row on first creation.

- Action: **If File Exists** → File: `%FilePath%` → Output: `%FileExists%`
- Action: **If** `%FileExists% = False`
- **Create File** → File: `%FilePath%` → Contents: `UserName,DateOfBirth,Age` (header)
- **End If**

### Step 7: Build the line and append to the file

Before writing, format the line as CSV (comma-separated). This makes the log file structured and easy to open in Excel later.

- Action: **Convert Datetime to Text** → `%Dob%` → Format: `yyyy-MM-dd` → Output: `%DobIso%`
- Action: **Set Variable** → `%Line% = %UserName%,%DobIso%,%AgeYears%`
- Action: **Append Line to Text File** → File: `%FilePath%` → Text: `%Line%`

### Step 8: Show success message

**Why:** Always give feedback at the end so the user knows the operation completed successfully and what was saved.

- Action: **Display Message** → Title: `Success` → Message: `Saved: %Line% to %FilePath%`

## Conclusion

In this tutorial, you learned how to create a simple **sequential flow** in Power Automate Desktop. Step by step, the flow collected user input (name and date of birth), performed a calculation (age), and saved the result to a text file — while ensuring the target folder and file existed. This exercise demonstrates the essence of sequential logic: actions executed one after another in a clear, linear order.