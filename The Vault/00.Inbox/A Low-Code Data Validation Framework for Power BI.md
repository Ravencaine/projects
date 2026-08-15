---
title: "A Low-Code Data Validation Framework for Power BI"
source: "https://medium.com/towardsdev/a-low-code-data-validation-framework-for-power-bi-b9fd72738a17"
author:
  - "[[Islam Taha]]"
published: 2025-08-02
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
## A practical guide for data engineers to automate data quality checks and de-risk deployments without leaving the Power BI ecosystem.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*tnheWD7LddiVrPFT-AUXcQ.png)

Data engineers spend countless hours building robust pipelines in Power BI. Intricate dataflows are created, semantic models are fine-tuned, and powerful datamarts are deployed. Yet, a critical question often remains: “Is the data *correct*?” A single upstream error can corrupt a dashboard, erode user trust, and lead to hours of manual debugging.

Power BI is a premier tool for transformation and visualization, but it lacks a native, declarative framework for data validation. The common alternatives are manual spot-checks or complex, one-off Power Query logic that is difficult to manage and scale.

This article introduces a centralized, scalable, and low-code data validation framework built directly within Power BI, using only a Dataflow and two SharePoint lists.

## The Challenge: The Data Validation Gap in Power BI

A proper validation system needs to automatically answer critical data quality questions:

- Is the total sales amount for today within an expected range?
- Are there any `NULL` values in a `CustomerID` column?
- Does the row count in the development version of the `FactSales` table match the production version?

Performing these checks manually is not a **scalable solution**. An automated engine is required to run these tests and provide a clear report of any failures.

## The Framework: A Two-Part Solution

This framework consists of two simple but powerful components:

1. **The Rule Engine (Two SharePoint Lists):** A centralized list where every validation rule is defined. It specifies *what* to test.
2. **The Validation Engine (A Power BI Dataflow):** A single dataflow that reads the rules from SharePoint, executes them against Power BI artifacts (Dataflows, Semantic Models, Datamarts), and reports the results. It specifies *how* to test.

## Part 1: The Rule Engine via SharePoint

The foundation of this framework is a set of two SharePoint lists that act as the “rule engine.” This two-list approach separates the high-level *what-to-test* configuration from the low-level *how-to-test* rules, making the system cleaner and easier to manage.

### List 1: Validation Settings

This primary list is designed to be simple, containing only a single item that tells the dataflow which artifacts to validate for the current run. This is where the user specifies the validation job.

**Columns:**

- **Artifact1Name** (Text): The name of the source artifact to be validated (e.g., “Sales Staging Dataflow”).
- **Artifact1Type** (Choice: `Dataflow Gen1`, `Datamart (Preview)`, `SemanticModel`): The type of the source artifact.
- **Artifact1Workspace** (Text): The name or ID of the Power BI workspace for the source artifact.
- **Artifact2Name** (Text): (Optional) The name of the target artifact for comparison (e.g., “Sales Production Dataflow”).
- **Artifact2Type** (Choice: `Dataflow Gen1`, `Datamart (Preview)`, `SemanticModel`): (Optional) The type of the target artifact.
- **Artifact2Workspace** (Text): (Optional) The name or ID of the workspace for the target artifact.

**Logic:**

- If the **Artifact2** columns are left empty, the framework runs in **single-artifact validation mode**. It will validate the tables in Artifact 1 against the predefined rules in the `Validation Rules` list.
- If the **Artifact2** columns are filled, the framework runs in **comparison mode**, validating Artifact 1 against Artifact 2 on a rule-by-rule basis.

### List 2: Validation Rules

This list contains the specific, granular rules that will be applied to the artifacts defined in the `Validation Settings` list.

**Columns:**

- **ArtifactName** (Text): The name of the artifact this rule applies to. This must match the name used in `Validation Settings`.
- **TableName** (Text): The specific table or query within the artifact to be validated.
- **ColumnName** (Text): The column to which the aggregation will be applied.
- **AggregationType** (Choice: `Sum`, `CountBlank`, `CountNull`, `Average`, `Max`, `Min`): The aggregation function to execute on the specified column.
- **ExpectedValue** (Text): A flexible text field defining the success criteria. This is only used in single-artifact validation mode.

### Defining ExpectedValue Rules

The `ExpectedValue` column is designed to be highly flexible by parsing text-based conditions. This allows for a wide range of validation scenarios without changing the underlying M code. The framework can be built to interpret the following formats:

![](https://miro.medium.com/v2/resize:fit:1396/format:webp/1*q3oK6jMbu3jjXsak1o4I6g.png)

This two-list setup provides a robust and scalable foundation for the validation framework, clearly separating the high-level configuration from the detailed rule definitions.

Of course. Here is the updated “Part 2” section, rewritten to align with the two-list setup and the specific columns you defined.

## Part 2: The Validation Engine via Power BI Dataflow

A single Power BI Dataflow orchestrates the entire validation process. It acts as the engine that reads the configuration, connects to the data sources, executes the rules, and generates a final report. The logic inside the dataflow follows these steps:

1. **Ingest Configuration and Determine Mode  
	**The process begins by connecting to the `ValidationSettings` SharePoint list. Since this list contains only one item, the dataflow reads that row to get the key attributes: `Artifact1Name`, `Artifact1Type`, `Artifact1Workspace`, and the optional Artifact2 details. The engine immediately checks if `Artifact2Name` is empty. This determines whether to run in single-artifact validation or two-artifact comparison mode.
2. **Load Rules and Access Artifacts  
	**Next, the dataflow connects to the `ValidationRules ` list. It filters this list to retrieve only the rules where the `ArtifactName` column matches the `Artifact1Name` from the settings list. Using custom M functions, the dataflow then dynamically connects to the specified Power BI artifacts (Dataflow, Datamart, or Semantic Model) to access the tables targeted by the rules.
3. **Execute Validation Logic  
	**This is the core execution step, where the logic diverges based on the mode:  
	**• In Single-Artifact Mode**: For each rule, the engine applies the specified `AggregationType` (e.g., `Sum`, `CountNull`) to the `ColumnName` within the `TableName`. The resulting value is then validated against the condition in the `ExpectedValue` column (e.g., checking if the sum is `>=100`).  
	**• In Comparison Mode**: For each rule, the engine performs the same aggregation on the same table and column in **both** Artifact 1 and Artifact 2. The `ExpectedValue` column from the rules list is ignored. The validation simply checks if the result from Artifact 1 is identical to the result from Artifact 2.
4. **Generate a Unified Report  
	**The final step is to consolidate the results into a single, clean output table. This table serves as the source for a monitoring dashboard and clearly shows the outcome of each test. The output typically includes columns like `TableName`, `ColumnName`, `AggregationType`, the actual result from Artifact 1, the expected/comparison result from Artifact 2, and a final status (e.g., “Passed” or “Failed”).

## Core Framework Functions (M Code)

The heart of the validation engine is a set of reusable Power Query functions. Below are code snippets of the key functions that drive the framework.

### Data Access Functions

These functions connect to a given artifact and list its tables/queries. Below are three functions to cover Power BI Dataflows Gen1, Datamarts, and Semantic Models.

```c
// GetDataflowTables: Connects to a dataflow and returns a list of its tables.
(WorkspaceName as text, dataflowName as text) => let
  Source = PowerPlatform.Dataflows([]),
  Workspaces = Source{[Id = "Workspaces"]}[Data],
  CurrentWorkspace = Table.SelectRows(Workspaces, each [workspaceName] = WorkspaceName),
  Dataflows = CurrentWorkspace{[]}[Data],
  UpstreamDataflow = Table.SelectRows(Dataflows, each [dataflowName] = dataflowName),
  Tables = UpstreamDataflow{[]}[Data],
  Output = Table.RenameColumns(
    Table.SelectColumns(Tables, {"entity", "Data"}),
    {"entity", "Name"}
  )
in
  Output
```
```c
// GetDatamartTables: Connects to a datamart and returns a list of its tables.
(workspaceName as text, datamartName as text) => let  
  Source = PowerBI.Datamarts(null),
  Datamarts = Source{[workspaceName = workspaceName]}[Data],
  Datamart = Table.SelectRows(Datamarts, each [displayName] = datamartName),
  Tables = Datamart{[]}[Data],
  Output = Table.RenameColumns(
    Table.SelectColumns(Tables, {"Item", "Data"}),
    {"Item", "Name"}
  )
in
  Output
```
```c
// GetSemanticModelTables: Connects to a semantic model and returns its tables.
(WorkspaceName as text, ModelName as text) => let
  // Connect to the database
  Databases = Table.FromRecords({
    [WorkspaceName = "Workspace1", Database = AnalysisServices.Databases("powerbi://api.powerbi.com/v1.0/myorg/Workspace1")],
    [WorkspaceName = "Workspace2", Database = AnalysisServices.Databases("powerbi://api.powerbi.com/v1.0/myorg/Workspace2")]
  }),
  Workspace = Databases{[WorkspaceName = WorkspaceName]}[Database],
  Database = Workspace{[Name = ModelName]},
  // Connect to the semantic model
  Model = Database[Data],
  // Connect to the folder
  Folder = Model{[Id = "Model"]}[Data],
  // Connect to the cube
  Cube = Folder{[Id = "Model"]}[Data],  
  // Return the list of tables
  Tables = Table.SelectColumns(Cube.Dimensions(Cube), {"Name", "Data"})
in
  Tables
```

### Summarization Functions

These functions iterate through the rules and apply them to the target tables.

```c
// SummarizeDataflow: Applies validation rules to a specified dataflow's tables.
(ValidationRules as table, ArtifactName as text, ArtifactWorkspace as text) =>
let
  // Get all tables within this dataflow
  AllTables = GetDataflowTables(ArtifactWorkspace, ArtifactName),
  // Join tables' data with validation rules
  AllTablesWithData = Table.SelectColumns(
    Table.Join(
        ValidationRules, {"TableName"},
        AllTables, {"Name"}
    ),
    {"Id", "TableName", "ColumnName", "AggregationType", "Data", "ExpectedValue"}
  ),
  // Apply the aggregation function/operator
  AddAggregated = Table.AddColumn(AllTablesWithData, "Result", each AggregateColumn([Data], [ColumnName], [AggregationType]), type number),
  // Remove extra columns
  Output = Table.RemoveColumns(AddAggregated, {"Data"})
in
  Output
```
```c
// SummarizeDatamart: Applies validation rules to a specified datamart's tables.
(ValidationRules as table, ArtifactName as text, ArtifactWorkspace as text) =>
let
  // Get all tables within this datamart
  AllTables = GetDatamartTables(ArtifactWorkspace, ArtifactName),
  AllTablesWithData = Table.SelectColumns(
    Table.Join(
        ValidationRules, {"TableName"},
        AllTables, {"Name"}
    ),
    {"Id", "TableName", "ColumnName", "AggregationType", "Data", "ExpectedValue"}
  ),
  AddAggregated = Table.AddColumn(AllTablesWithData, "Result", each AggregateColumn([Data], [ColumnName], [AggregationType]), type number),
  Output = Table.RemoveColumns(AddAggregated, {"Data"})
in
  Output
```
```c
// SummarizeSemanticModel: Applies validation rules to a specified semantic model's tables.
(ValidationRules as table, ArtifactName as text, ArtifactWorkspace as text) =>
let
  // Get all tables within this semantic model
  AllTables = GetSemanticModelTables(ArtifactWorkspace, ArtifactName),
  AllTablesWithData = Table.SelectColumns(
    Table.Join(
        ValidationRulesWithSummary, {"TableName"},
        AllTables, {"Name"}
    ),
    {"Id", "TableName", "ColumnName", "AggregationType", "Data", "ExpectedValue"}
  ),
  AddAggregated = Table.AddColumn(AllTablesWithData, "Result", each AggregateColumn([Data], "[" & [TableName] & "].[" & [ColumnName] & "].[" & [ColumnName] & "]", [AggregationType]), type number),
  Output = Table.RemoveColumns(AddAggregated, {"Data"})
in
  Output
```

### Core Logic Functions

These are the fundamental building blocks for executing a single validation test.

```c
// AggregateColumn: Applies a specified aggregation (e.g., Sum, Max, Count) to a table column.
(tbl as table, colName as text, op as text) as any =>
let
    // Extract the column
    colRaw = Table.Column(tbl, colName),
    // Convert to number if needed
    colNumeric = List.Transform(colRaw, each try Number.From(_) otherwise null),
    // Choose the appropriate column based on operator
    col = if List.Contains({"Sum", "Average", "Min", "Max"}, op) then colNumeric else colRaw,
    // Apply the aggregation function
    result = 
        if op = "Sum" then List.Sum(col)
        else if op = "CountBlank" then List.Count(List.Select(col, each _ = ""))
        else if op = "CountNull" then List.Count(List.Select(col, each _ = null))
        else if op = "Average" then List.Average(col)
        else if op = "Max" then List.Max(col)
        else if op = "Min" then List.Min(col)
        else null
in
    result
```
```c
// ValidateRecord: Compares the actual result to the expected value(s) from a rule.
(result as number, expectedValue as text) => let
  // Validate the result based on the rule \`expectedValue\`. Here's some examples of the supported rules and their meaning:
  // Rule Format    | Meaning
  // >=100          | Greater than or equal to 100
  // <50            | Less than 50
  // =75            | Equal to 75
  // 50-100         | Between 50 and 100 (inclusive)
  // >=50 and <=100 | Compound condition (inclusive range)
  rule = Text.Trim(expectedValue),
  
  // Check for compound condition
  isCompound = Text.Contains(rule, "and"),
  isRange = Text.Contains(rule, "-") and not isCompound,

  // Handle compound condition
  compoundParts = if isCompound then Text.Split(rule, "and") else {},
  compoundCheck = if isCompound then
    List.AllTrue(List.Transform(compoundParts, each 
      let
        part = Text.Trim(_),
        op = Text.Start(part, Text.PositionOfAny(part, {"0".."9"})),
        val = Number.FromText(Text.Range(part, Text.PositionOfAny(part, {"0".."9"})))
      in
        if op = ">=" then result >= val
        else if op = "<=" then result <= val
        else if op = ">" then result > val
        else if op = "<" then result < val
        else if op = "=" then result = val
        else false
    ))
    else null,

  // Handle range like "50-100"
  rangeParts = if isRange then Text.Split(rule, "-") else {},
  rangeCheck = if isRange then
    let
      lower = Number.FromText(rangeParts{0}),
      upper = Number.FromText(rangeParts{1})
    in
      result >= lower and result <= upper
  else null,

  // Handle simple condition
  simpleOp = Text.Start(rule, Text.PositionOfAny(rule, {"0".."9"})),
  simpleVal = Number.FromText(Text.Range(rule, Text.PositionOfAny(rule, {"0".."9"}))),
  simpleCheck = if not isCompound and not isRange then
      if simpleOp = ">=" then result >= simpleVal
      else if simpleOp = "<=" then result <= simpleVal
      else if simpleOp = ">" then result > simpleVal
      else if simpleOp = "<" then result < simpleVal
      else if simpleOp = "=" then result = simpleVal
      else false
    else null
in
  if isCompound then compoundCheck
  else if isRange then rangeCheck
  else simpleCheck
```

### Master Validation Query

This master query orchestrates the entire validation process. It connects to the SharePoint lists, determines if it’s a single artifact validation or a two-artifact comparison, and then uses the previously defined functions to generate a final summary output.

```c
let
    // 1. Connect to the SharePoint site holding the configuration lists
    Source = SharePoint.Tables("https://your-company.sharepoint.com/sites/your-site", [ApiVersion = 15]),

    // 2. Load the main validation settings (specifies which artifacts to test)
    // Replace 'your-validation-settings-list-id' with the actual GUID of your settings list
    ValidationSettings = Source{[Id="your-validation-settings-list-id"]}[Items],

    // 3. --- Process the First Artifact (Source) ---
    Artifact1Name = Table.First(ValidationSettings)[Artifact1Name],
    Artifact1Workspace = Table.First(ValidationSettings)[Artifact1Workspace],
    Artifact1Type = Table.First(ValidationSettings)[Artifact1Type],
    
    // Load the validation rules for the first artifact
    // Replace 'your-validation-rules-list-id' with the actual GUID of your rules list
    ValidationRules = Source{[Id="your-validation-rules-list-id"]}[Items],
    ValidationRules1 = Table.SelectRows(ValidationRules, each ([ArtifactName] = Artifact1Name)),
    
    // Summarize the first artifact using the appropriate function based on its type
    // Note: SummarizeArtifact would be a wrapper function that calls SummarizeDataflow, SummarizeDatamart, etc.
    Artifact1Summary = SummarizeArtifact(ValidationRules1, Artifact1Name, Artifact1Workspace, Artifact1Type),

    // 4. --- Process the Second Artifact (Target/Comparison) ---
    Artifact2Name = Table.First(ValidationSettings)[Artifact2Name],
    Artifact2Workspace = Table.First(ValidationSettings)[Artifact2Workspace],
    Artifact2Type = Table.First(ValidationSettings)[Artifact2Type],

    // If a second artifact is defined, generate its rules by replacing the name from the first set
    ValidationRules2 = if Artifact2Name <> null then Table.ReplaceValue(ValidationRules1, Artifact1Name, Artifact2Name, Replacer.ReplaceValue, {"ArtifactName"}) else null,
    Artifact2Summary = if Artifact2Name <> null then SummarizeArtifact(ValidationRules2, Artifact2Name, Artifact2Workspace, Artifact2Type) else null,

    // 5. --- Compare Results and Format Output ---
    Result = if Artifact2Name = null then
        // --- SINGLE ARTIFACT VALIDATION ---
        // The result is compared against the 'ExpectedValue' from the rules list
        Table.RenameColumns(
            Artifact1Summary,
            {{"Result", "ActualValue"}, {"ExpectedValue", "ExpectedValue"}}
        )
    else
        // --- TWO ARTIFACT COMPARISON (e.g., Dev vs. Prod) ---
        // Join the two summaries on the rule keys
        let
            Comparison = Table.NestedJoin(
                Artifact1Summary, {"TableName", "ColumnName", "AggregationType"},
                Artifact2Summary, {"TableName", "ColumnName", "AggregationType"},
                "ComparisonData",
                JoinKind.LeftOuter
            ),
            Expanded = Table.ExpandTableColumn(Comparison, "ComparisonData", {"Result"}, {"Artifact2Result"}),
            Renamed = Table.RenameColumns(Expanded, {{"Result", "Artifact1Result"}})
        in
            Table.SelectColumns(Renamed, {"Id", "TableName", "ColumnName", "AggregationType", "Artifact1Result", "Artifact2Result"}),

    // 6. --- Add Final Validation Status Column ---
    AddIsMatchColumn = Table.AddColumn(
        Result,
        "IsMatch",
        each if Artifact2Name = null then
                 // For single artifact, validate the actual value against the expected value from the rule
                 ValidateRecord([ActualValue], [ExpectedValue], null, [AggregationType])
             else
                 // For two artifacts, check if their results are identical
                 [Artifact1Result] = [Artifact2Result],
        type logical
    ),

    // 7. --- Set Final Column Types for the Output ---
    FinalOutput = Table.TransformColumnTypes(
        AddIsMatchColumn,
        {
            {"TableName", type text},
            {"ColumnName", type text},
            {"AggregationType", type text}
        }
    )

in
    FinalOutput
```

## Key Use Cases Unlocked 🚀

This framework is incredibly flexible and supports two primary use cases.

### 1\. Continuous Data Quality Monitoring

By scheduling the validation dataflow to run after main ETL pipelines, it provides an automated check on production assets. If a row count in a critical table suddenly drops by 50%, the system will flag it immediately, often before business users are impacted.

### 2\. Pre-Deployment Sanity Checks (Dev vs. Prod)

Before deploying changes from a development workspace to production, the framework can validate the new version against the old one. Rules can be configured to compare artifacts, for example:

- Check if the `CountBlank` of `Table_DEV` equals the `CountBlank` of `Table_PROD`.
- Validate that the `Sum` of a key metric column is within a small variance (e.g., +/- 2%) between the dev and prod semantic models.

This process drastically reduces the risk of deploying a change that introduces data errors.

## Why This Approach Shines 🌟

- **Centralized & Scalable:** All rules live in one place. As the data estate grows, one simply adds rows to SharePoint, not complexity to dataflows.
- **Low-Code:** Business analysts or data stewards can add new validation rules without writing M code.
- **Native & Cost-Effective:** It uses tools already available within the Power BI ecosystem.
- **Flexible:** It works across the most common Power BI artifacts: Dataflows, Datamarts, and Semantic Models.

By investing a small amount of time to set up this framework, organizations can shift from a reactive “fire-fighting” approach to data quality to a proactive, automated one that builds trust and saves valuable engineering time.