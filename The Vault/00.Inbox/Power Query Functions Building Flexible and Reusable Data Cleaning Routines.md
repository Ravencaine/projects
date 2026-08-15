---
title: "Power Query Functions: Building Flexible and Reusable Data Cleaning Routines"
source: "https://medium.com/microsoft-power-bi/power-query-functions-building-flexible-and-reusable-data-cleaning-routines-1eab3c04f8c1"
author:
  - "[[Ethan Guyant]]"
published: 2024-08-29
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Enhancing Consistency and Efficiency with Customizable Power Query Workflows

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*U5IpfYXki8qBpZdL2G8fXw.png)

When extracting and transforming data in Power BI, we often repeat the same steps across different projects. This repetition raises the question: can these steps be generalized and reusable in future projects?

This post will explore a solution that breaks down these steps into flexible and reusable parameters and functions, eliminating the need to recreate these common steps across our projects. The solution leverages parameters, functions, and queries to standardize various parts of our data preparation process when CSV files in a SharePoint document library are the data source.

Don’t just read; get hands-on and view all the details in the template report available here:

## [GitHub - EMGuyant/power-query-functions: Power BI template to standardize the loading and…](https://github.com/EMGuyant/power-query-functions/tree/master?source=post_page-----1eab3c04f8c1---------------------------------------)

### Power BI template to standardize the loading and preparation of CSV files stored within a SharePoint site. The approach…

github.com

## Power Query Parameters

Parameters help keep our data preparation process as dynamic as possible. They provide a level of flexibility to our Power Query functions and allow us to modify their behavior without altering the underlying function definition. This flexibility enables this solution to adapt to different requirements and increases the reusability of our work.

In our solution, 7 parameters manage how data is loaded, cleaned, and transformed.

**SharePoint Site Url (Text):** specifies the SharePoint site URL where the CSV files are stored.

```c
https://yourcompany.sharepoint.com/sites/yoursite
```

**SharePoint Folder Path (Text):** defines the folder path within the SharePoint site where the CSV files are located.

```c
https://yourcompany.sharepoint.com/sites/yoursite/yourfolder/
```

**textColumns (Text):** a comma-separated list of column names that require text transformations.

```c
Column Name 1, Column Name 2, Column Name 3
```

**textFormatCase (Text):** a text value that specifies how text columns should be formatted. Options include Proper, Lower, and Upper case.

**columnDataTypes (Text):** a semicolon-separated list of column names paired with their corresponding data type description, used to dynamically set the data types of each column.

```c
Column Name 1,date; Column Name 2,whole number; Column Name 3,text; Column Name 4,text; Column Name 5,text; Column Name 6,whole number; Column Name 7,decimal number
```

**errorHandlingOption (Text):** sets how errors are handled within the dataset and provides the options of RemoveErrors, ReplaceErrors, or None.

**viewErrorSummary (TRUE/FALSE):** toggles between displaying a summary of rows that contain errors and returning the cleaned dataset.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*4LwkGubwQW2ASYi5)

Once we create our parameters and set their values, we can reference them throughout our functions and queries. This enables us to adjust the entire data transformation process by updating the parameter values.

## Supporting Utility Functions

To enhance the reusability of our Power Query solution, we first break down complex data transformations into smaller, modular functions. Each utility function handles a specific task, improving its maintainability and allowing us to apply them individually or collectively across different datasets.

**fxParameterToList**

```c
(parameterName as text) as list => 
List.Transform(Text.Split(parameterName, ","), each Text.Trim(_))
```

Many of our parameters in this solution are comma-separated strings that we must convert to list objects before using them in a list-based transformation within Power Query. Since many of our parameters and functions require this, creating a function allows us to repeat this operation easily.

The function has a single input parameter (parameterName), a comma-separated string of values. It then splits this input by commas, trims surrounding spaces, and converts the result into a list. This is used when calling and passing parameter values to other utility functions such as fxTransformTextFormat and fxTransformTextTrim.

**fxTransformTextTrim**

The fxTransformTextTrim function trims any leading and trailing spaces from text values in the specified columns. Trimming can be essential when cleaning user-entered data or other text extracted from external sources.

```c
(inputTable as table, columnsToTrim as list) as table => 
Table.TransformColumns(inputTable, List.Transform(columnsToTrim, each {_, Text.Trim, type text}))
```

This function has two input parameters:

- inputTable: a table containing the data to be trimmed
- columnsToTrim: a list of text columns that require trimming

The fxTransformTextTrim function applies Text.Trim to each column specified in columnsToTrim, ensuring our text data is clean and consistent.

**fxTransformTextFormat**

The fxTransformTextFormat function standardizes the case formatting of our text data depending on the caseType input parameter. Depending on our requirements, the function can convert text data to Proper Case, Lower Case, or Upper Case.

```c
(inputTable as table, columnsToTransform as list, caseType as text) as table =>
    let
        // Determine the transformation function based on caseType input
        CaseFunction = if caseType = "Proper" then Text.Proper
                       else if caseType = "Lower" then Text.Lower
                       else if caseType = "Upper" then Text.Upper
                       else error "Unsupported case type: Use 'Proper', 'Lower', or 'Upper'",

        // Apply the selected case transformation to each column in the list
        TransformTextCase = Table.TransformColumns(inputTable, List.Transform(columnsToTransform, each {_, CaseFunction, type text}))
    in
        TransformTextCase
```

This function has three input parameters:

- inputTable: a table containing the data to be transformed
- columnsToTransform: a list of columns that require text formatting
- caseType: a text value specifying the desired text format (Proper, Lower, or Upper)

Using the caseType parameter, the function identifies the transformation type and then applies the transformation to the specified columns.

**fxTransformRemoveDuplicates**

The fxTransformRemoveDuplicates is a straightforward function that removes duplicated rows within our dataset.

```c
(inputTable as table) as table => 
Table.Distinct(inputTable)
```

This function has a single parameter:

The function uses Table.Distinct to identify and remove duplicated rows and returns a table with each row being unique.

**fxTransformSetDataTypes**

The fxTransformSetDataTypes function maps a textual description of the data type to the Power Query data type. The function allows dynamically setting column data types based on our columnDataTypes Power Query parameter.

```c
(columnType as text) as type =>
    let
        lowerColumnType = Text.Lower(columnType),
        columnTypeResult = 
            if lowerColumnType = "decimal number" then type number
            else if lowerColumnType = "fixed decimal number" then type number
            else if lowerColumnType = "whole number" then Int64.Type
            else if lowerColumnType = "percentage" then type number
            else if lowerColumnType = "date/time" then type datetime
            else if lowerColumnType = "date" then type date
            else if lowerColumnType = "time" then type time
            else if lowerColumnType = "date/time/timezone" then type datetimezone
            else if lowerColumnType = "duration" then type duration
            else if lowerColumnType = "text" then type text
            else if lowerColumnType = "true/false" then type logical
            else if lowerColumnType = "binary" then type binary
            else type text // Default to text if the type is unrecognized
    in
        columnTypeResult
```

The function has a single input parameter:

This function helps us leverage common textual descriptions to set Power Query data types across our dataset columns.

**fxErrorHandling**

The fxErrorHandling function allows us to manage how our dataset handles errors based on our requirements. We can use the function’s input parameter to remove rows containing errors, replace error values with null, or retain the errors within the dataset.

```c
(inputTable as table, errorHandlingOption as text) as table =>
let
    ErrorRows = Table.SelectRowsWithErrors(inputTable),
    
    // Determine the action based on the error handling option provided
    ErrorHandlingResult = 
    if errorHandlingOption = "RemoveErrors" then
        // Remove rows with any errors
        Table.RemoveRowsWithErrors(inputTable)
    else if errorHandlingOption = "ReplaceErrors" then
        // Replace errors with a specified value (default is "Error" if replaceValue is not provided)
        let
            ReplaceErrorsStep = 
                let
                    // Get a list of column names
                    columnNames = Table.ColumnNames(inputTable),
                    // Create a list of replacement rules where each column is mapped to null in case of error
                    errorReplacementList = List.Transform(columnNames, each {_, null})
                in
                    Table.ReplaceErrorValues(inputTable, errorReplacementList)
        in
            ReplaceErrorsStep
    else
        // If the parameter is not set correctly, return the data as is
        inputTable,

    Output = if viewErrorSummary then ErrorRows else ErrorHandlingResult
in
    Output
```
- inputTable: a data table to be evaluated for errors
- errorHandlingOption: specifies how the errors within inputTable should be handled (RemoveErrors, ReplaceErrors, None)

The function also utilizes the viewErrorSummary Power Query parameter. This parameter can be set to TRUE/FALSE and determines whether to return an error summary or the cleaned dataset.

This function identifies rows with errors. Depending on the errorHandlingOption, it will remove the rows containing errors, replace the error values with null, or return inputTable without handling the errors.

If viewErrorSummary is set to TRUE, the function returns only the rows that contain errors, allowing us to inspect the errors further within our dataset.

## Core Function — TranformCSV

The fxTransformCSV function is the start of our standardized data processing solution, designed to handle our CSV files in a modular and reusable way.

It takes the raw contents of our CSV files, applies a defined set of transformations, and then outputs a clean data table ready for our analysis. This function leverages the utility functions discussed in the previous section.

```c
((FileContent as binary) =>
let
    //STEP 01: Importing CSV files
    ImportCSV = Csv.Document(FileContent,[Delimiter=",", Encoding=1252, QuoteStyle=QuoteStyle.None]),
    PromoteHeaders = Table.PromoteHeaders(ImportCSV, [PromoteAllScalars=true]),
    
    //STEP 02: Cleaning blank rows/columns
    //Clean blank rows
    RemoveBlankRows = Table.SelectRows(PromoteHeaders, each not List.IsEmpty(List.RemoveMatchingItems(Record.FieldValues(_), {"", null}))),
    //Clean blank columns
    RemoveBlankColumns = Table.SelectColumns(RemoveBlankRows, List.Select(Table.ColumnNames(RemoveBlankRows), each not List.IsEmpty(List.RemoveMatchingItems(Table.Column(RemoveBlankRows, _), {""," ", null})))),
    
    //STEP 03: Replace empty strings with  null
    ReplaceValue = Table.ReplaceValue(RemoveBlankColumns,"",null,Replacer.ReplaceValue,Table.ColumnNames(RemoveBlankColumns)),
    
    //STEP 04: Remove duplicates
    RemoveDuplicates = fxTransformRemoveDuplicates(ReplaceValue),

    //STEP 05: Text transformations
    // Convert the textColumns parameter into a list
    TextColumnsToTransform = fxParameterToList(textColumns),
    // Apply the TrimTextColumns function
    TrimTextColumns = fxTransfromTextTrim(RemoveDuplicates, TextColumnsToTransform),
    // Apply the TransformTextCase function for Proper Case (can also be "Lower" or "Upper")
    FormatTextColumns = fxTransformTextFormat(TrimTextColumns, TextColumnsToTransform, textFormatCase)

in
    FormatTextColumns
```

### Breaking Down fxTransformCSV

**STEP 01: Importing the CSV files**

The function begins by reading the contents of the CSV files and then promotes the first row to headers.

```c
//STEP 01: Importing CSV files
    ImportCSV = Csv.Document(FileContent,[Delimiter=",", Encoding=1252, QuoteStyle=QuoteStyle.None]),
    PromoteHeaders = Table.PromoteHeaders(ImportCSV, [PromoteAllScalars=true]),
```

**STEP 02: Cleaning blank rows/columns**

The next step, which begins our transformation steps, removes any empty rows or columns. By eliminating these blank rows or columns early in our process, we avoid potential issues downstream and reduce clutter in the dataset.

```c
//STEP 02: Cleaning blank rows/columns
//Clean blank rows
RemoveBlankRows = Table.SelectRows(PromoteHeaders, each not List.IsEmpty(List.RemoveMatchingItems(Record.FieldValues(_), {"", null}))),
//Clean blank columns
RemoveBlankColumns = Table.SelectColumns(RemoveBlankRows, List.Select(Table.ColumnNames(RemoveBlankRows), each not List.IsEmpty(List.RemoveMatchingItems(Table.Column(RemoveBlankRows, _), {""," ", null})))),
```

**STEP 03: Replace empty strings with null**

Empty strings can cause common issues in our analysis. This step replaces empty string values in the dataset with null, making the data more consistent, better understood, and easier to work with.

```c
//STEP 03: Replace empty strings with  null
ReplaceValue = Table.ReplaceValue(RemoveBlankColumns,"",null,Replacer.ReplaceValue,Table.ColumnNames(RemoveBlankColumns)),
```

**STEP 04: Remove duplicates**

Using the fxTransformRemoveDuplicates utility function, this step removes duplicated rows from the dataset.

```c
//STEP 04: Remove duplicates
RemoveDuplicates = fxTransformRemoveDuplicates(ReplaceValue),
```

**STEP 05: Text transformations**

The text transformations start with trimming our text values to ensure there are no leading or trailing spaces, using the fxTransformTextTrim utility function.

Then, the text values get standardized using the fxTransformTextFormat utility function to make our data more readable and consistent.

```c
//STEP 05: Text transformations
// Convert the textColumns parameter into a list
TextColumnsToTransform = fxParameterToList(textColumns),
// Apply the TrimTextColumns function
TrimTextColumns = fxTransfromTextTrim(RemoveDuplicates, TextColumnsToTransform),
// Apply the TransformTextCase function for Proper Case (can also be "Lower" or "Upper")
FormatTextColumns = fxTransformTextFormat(TrimTextColumns, TextColumnsToTransform, textFormatCase)Core Function — LoadCSVData
```

## Core Function — LoadCSVData

The LoadCSVData function is the layer connecting the different elements of our Power Query solution. It loads multiple CSV files from our SharePoint source, applies the fxTransformCSV function to each file, and handles final data preparations.

This function is adaptable by leveraging Power Query parameters, allowing us to easily modify the data preparation process to meet our project’s requirements (e.g. switching to different SharePoint sites or folders).

```c
() as table =>
let
    
    //STEP 01: Load files from SharePoint
    SharePointSite = SharePoint.Files(#"SharePoint Site Url", [ApiVersion = 15]),
    SharePointFolder = Table.SelectRows(SharePointSite, each ([Folder Path] = #"SharePoint Folder Path")),
    
    //STEP 02: Invoke the fxTransformCSV function for each file
    TransformCSVResult = Table.AddColumn(SharePointFolder, "TransformCSV", each fxTransformCSV([Content])),
    
    //STEP 03: Renaming and removing columns
    // Rename the "Name" column for clarity
    PrefixSouceName = Table.RenameColumns(TransformCSVResult,{{"Name", "source.Name"}}),
    // Remove other columns to focus on the transformed data
    RemoveColumns = Table.SelectColumns(PrefixSouceName,{"source.Name", "TransformCSV"}),
    
    //STEP 04: Expand the transformed CSV data
    ExpandTransformCSV = Table.ExpandTableColumn(RemoveColumns, "TransformCSV", Table.ColumnNames(TransformCSVResult{0}[TransformCSV])),

    //STEP 05: Set data types
    ColumnTypePairs = Text.Split(columnDataTypes, ";"),
    // Trim spaces and split each pair into a list of {column name, data type}
    ColumnTypeList = List.Transform(ColumnTypePairs, each 
        let
            PairParts = List.Transform(Text.Split(_, ","), Text.Trim),
            ColumnName = List.First(PairParts),
            ColumnType = fxTransformSetDataTypes(List.Last(PairParts))
        in
            {ColumnName, ColumnType}
    ),
    // Dynamically set the column data types
    SetDataTypes = Table.TransformColumnTypes(ExpandTransformCSV, ColumnTypeList),

    //STEP 06: Error handling
    ErrorHandlingOutput = fxErrorHandling(SetDataTypes, errorHandlingOption)
in
    ErrorHandlingOutput
```

### Breaking down fxLoadCSVData

**STEP 01: Load files from SharePoint**

The function begins by connecting to the specified SharePoint site using the SharePoint Site Url parameter. Then, it filters the files to those located within the specified SharePoint Folder Path. Using both parameters allows us to target the specific CSV files required for our analysis.

```c
//STEP 01: Load files from SharePoint
SharePointSite = SharePoint.Files(#"SharePoint Site Url", [ApiVersion = 15]),
SharePointFolder = Table.SelectRows(SharePointSite, each ([Folder Path] = #"SharePoint Folder Path"))
```

**STEP 02: Invoke the fxTransformCSV function for each file**

For each file in our SharePoint source, we add a new column and invoke our custom `fxTransformCSV` function. This step ensures each file is processed consistently.

```c
//STEP 02: Invoke the fxTransformCSV function for each file
TransformCSVResult = Table.AddColumn(SharePointFolder, "TransformCSV", each fxTransformCSV([Content]))
```

**STEP 03: Renaming and removing columns**

To improve the clarity of our columns, we renamed the Name column to source.Name, indicating that it represents the original file name. This clearly indicates what this column is while providing information on the file the row of data is associated with.

The function then removes unnecessary columns, and we keep only `source.Name` and `TransformCSV` columns.

```c
//STEP 03: Renaming and removing columns
// Rename the "Name" column for clarity
PrefixSouceName = Table.RenameColumns(TransformCSVResult,{{"Name", "source.Name"}}),
// Remove other columns to focus on the transformed data
RemoveColumns = Table.SelectColumns(PrefixSouceName,{"source.Name", "TransformCSV"})
```

**STEP 04: Expand the transformed CSV data**

We expand the TransformCSV column into individual files, which compiles all the transformed CSV data into a single table.

```c
//STEP 04: Expand the transformed CSV data
ExpandTransformCSV = Table.ExpandTableColumn(RemoveColumns, "TransformCSV", Table.ColumnNames(TransformCSVResult{0}[TransformCSV]))
```

**STEP 05: Set data types**

In this step, the function dynamically sets the data types for each column based on the columnDataTypes Power Query parameter. The TransformSetDataTypes function maps each column to its specified data type.

```c
//STEP 05: Set data types
ColumnTypePairs = Text.Split(columnDataTypes, ";"),
// Trim spaces and split each pair into a list of {column name, data type}
ColumnTypeList = List.Transform(ColumnTypePairs, each 
    let
        PairParts = List.Transform(Text.Split(_, ","), Text.Trim),
        ColumnName = List.First(PairParts),
        ColumnType = fxTransformSetDataTypes(List.Last(PairParts))
    in
       {ColumnName, ColumnType}
),
// Dynamically set the column data types
SetDataTypes = Table.TransformColumnTypes(ExpandTransformCSV, ColumnTypeList)
```

**STEP 06: Error handling**

The function concludes by handling errors in the dataset according to the `errorHandlingOption` parameter. If the `viewErrorSummary` is set to true, the function returns a summary of rows that contain errors, otherwise it returns the cleaned dataset.

```c
//STEP 06: Error handling
ErrorHandlingOutput = fxErrorHandling(SetDataTypes, errorHandlingOption)
```

## Applying and Extending the Power Query Solution

We have explored and started constructing a flexible approach to standardize and ensure our data preparation steps are applied consistently within and across our Power BI projects.

The final query loaded to our Power BI data model is rpt\_SharePointCSVData. This query utilizes the fxLoadCSVData function to bring each step together and deliver a clean and consistent data set to our Power BI report.

```c
let 
   Source = fxLoadCSVData() 
in 
   Source
```

This simple query calls the fxLoadCSVData function, which loads and processes the CSV files according to previously defined transformations and parameters. The result is a clean, ready-to-use dataset.

This solution is designed to be adaptable and can be applied to different Power BI projects that require loading CSV files from a SharePoint source.

A Power BI template and sample data files are available at the link below to view an example of how this solution can be applied. This file can be used as a starting point for our Power BI projects, or you can copy and paste specific folders or elements of it into an existing project.

## [GitHub - EMGuyant/power-query-functions: Power BI template to standardize the loading and…](https://github.com/EMGuyant/power-query-functions/tree/master?source=post_page-----1eab3c04f8c1---------------------------------------)

### Power BI template to standardize the loading and preparation of CSV files stored within a SharePoint site. The approach…

github.com

To successfully apply this solution:

**Start with the Parameters:** define the parameters relevant to the project.

Open the template file and, when prompted, populate each parameter with the required information.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*8LMYlfXqWr9r8jQ5)

For example, the parameters can be set using the sample files to the following.

```c
SharePoint Site Url: 
https://yourcompany.sharepoint.com/sites/yoursite

SharePoint Folder Path:
https://yourcompany.sharepoint.com/sites/yoursite/yourfolder/

textFormatCase:
Proper

textColumns:
Event Name, Location, Organizer Name

columnDataTypes:
Event Date,date;Event ID,whole number;Event Name,text;Location,text;Organizer Name,text;Number of Attendees,whole number;Feedback Score,decimal number

errorHandlingOption:
ReplaceErrors

viewErrorSummary:
FALSE
```

Then, under the Load dropdown, select Edit to explore this solution in the Power Query Editor.

Once the data is loaded, you can modify the textFormatCase, error handling option, and viewErrorSummary parameters in the Power Query Editor to view the results when you select different options.

**Customize the Utility Functions:** if different projects have unique requirements, consider modifying or extending the utility functions.

**Leverage the modular structure:** This solution’s modular design makes adding or removing steps easy based on the project’s specific needs.

**Extend with new functions:** as our data processing needs evolve, we can extend this solution by adding new functions or adding more flexibility to our existing ones.

## Wrapping Up

This post explores a solution that leverages Power Query parameters, functions, and queries to streamline our data preparation process. Combining custom functions with parameters provides us with a framework that can be adapted to meet the demands of different projects.

The design approach used in this solution aims to enhance the maintainability and reusability of each of its components. As we continue to work with and expand this solution, we will build a library of reusable functions to increase our efficiency in future projects.

**Thank you for reading! Stay curious, and until next time, happy learning.**

And remember, as Albert Einstein once said, “Anyone who has never made a mistake has never tried anything new.” So, don’t be afraid of making mistakes, practice makes perfect. Continuously experiment, explore, and challenge yourself with real-world scenarios.

If this sparked your curiosity, keep that spark alive and check back frequently. Better yet, be sure not to miss a post by subscribing! With each new post comes an opportunity to learn something new.

## [Don't miss a story!](https://medium.com/subscribe/@emguyant?source=post_page-----1eab3c04f8c1---------------------------------------)

medium.com

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)