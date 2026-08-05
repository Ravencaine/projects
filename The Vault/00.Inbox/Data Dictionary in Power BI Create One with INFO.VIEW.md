---
title: "Data Dictionary in Power BI: Create One with INFO.VIEW"
source: "https://databear.com/data-dictionary-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-07-18
created: 2026-08-04
description: "Create a data dictionary in Power BI with INFO.VIEW DAX. Document tables, columns, measures, and relationships clearly and efficiently."
Processed: "Unprocessed"
---
One of the most important habits for any data professional is to document your work. In this tutorial, we’ll show you how to quickly create a **data dictionary in Power BI Desktop** using just a few DAX functions.

A well-documented model helps everyone from report developers to stakeholders understand what the data represents, how to interpret it correctly, and where it comes from. Thanks to the new `INFO.VIEW` DAX functions introduced in October 2024, documenting your model is now faster and easier than ever.

##### What Is a Data Dictionary?

A **data dictionary** is essentially a table that captures key information about your model, such as:

- Tables, columns, and measures
- Relationships between tables
- Definitions and calculations
- Key characteristics of your data

Having a single, centralized data dictionary ensures consistency and transparency across your reports.

##### Why Documentation Matters

There are several reasons to document your Power BI models:

- Ensures everyone is using the same definitions and language
- Helps stakeholders and end users interpret data accurately
- Serves as a single source of truth, particularly for complex or industry-specific metrics

##### New INFO.VIEW DAX Functions

The `INFO.VIEW` DAX functions allow you to programmatically extract metadata about your model directly in Power BI Desktop. There are four variations:

- `INFO.VIEW.MEASURES` lists all measures with their definitions and DAX code
- `INFO.VIEW.TABLES` details all tables and their attributes
- `INFO.VIEW.COLUMNS` lists columns, data types, and categories
- `INFO.VIEW.RELATIONSHIPS` shows how tables are related, including cardinality and filter direction

You can use these functions in new tables within your model to generate the foundation of your data dictionary.![New INFO.VIEW DAX Functions](99.System/Attachments/New_INFO.VIEW_DAX_Functions.png)

##### Step-by-Step: Build a Data Dictionary

##### Documenting Measures

1. Open Power BI Desktop and go to your report.
2. In the model view, select **Table Tools > New Table**.
3. Enter this formula:
	```
	ModelMeasures = INFO.VIEW.MEASURES()
	```
4. Power BI will create a table listing all measures, their DAX expressions, and metadata.![Documenting Measures ](99.System/Attachments/Documenting_Measures_.png)

##### Adding Descriptions

You can enhance your data dictionary by adding descriptions to measures:

- In model view, select a measure.
- In the Properties pane, enter a clear description.
- Refresh your `ModelMeasures` table to see the updated description appear.![Adding Descriptions data dictionary in Power BI](99.System/Attachments/Adding_Descriptions_data_dictionary_in_Power_BI.png)

##### Documenting Tables, Columns, and Relationships

Repeat the process with the other `INFO.VIEW` functions:

```
ModelTables = INFO.VIEW.TABLES()
ModelColumns = INFO.VIEW.COLUMNS()
ModelRelationships = INFO.VIEW.RELATIONSHIPS()
```

Each of these creates a table with relevant metadata.

##### Combine Metadata Into One Table

For a more advanced approach, you can combine all four tables into a single, dynamic data dictionary using `SELECTCOLUMNS` and `UNION`. This allows you to filter and explore all components of your model in one place.

Here’s an outline of how the DAX works:

- Define variables for measures, columns, tables, and relationships using `INFO.VIEW` functions.
- Use `SELECTCOLUMNS` to extract only relevant fields.
- Add a `Type` column to distinguish between components.
- Combine them with `UNION` into one table called `DataDictionary`.

This single table can then power a report page with interactive slicers and visuals.

##### Create a Data Dictionary Report Page

Finally, create a new report page to expose your data dictionary:

- Add table visuals showing names, descriptions, and expressions.
- Add a text slicer to allow users to search by measure name or keyword.
- Optionally, include a slicer to filter by type (Measure, Table, Column, Relationship).

This creates an interactive, dynamic way for users to explore your documentation directly within the report.![Create a Data Dictionary Report Page data dictionary in Power BI](99.System/Attachments/Create_a_Data_Dictionary_Report_Page_data_dictionary_in_Power_BI.png)

##### Why Use INFO.VIEW Functions?

These new DAX functions make your documentation dynamic. As you add, edit, or remove components in your model, the data dictionary tables automatically update, saving time and reducing errors.

##### Final Thoughts

The `INFO.VIEW` functions in Power BI Desktop are a powerful addition for maintaining clear, up-to-date documentation of your models. A well-constructed data dictionary improves trust, transparency, and usability of your reports all without leaving Power BI.

For more Power BI tutorials and training resources, visit:  
[Power BI Training at DataBear](https://databear.com/power-bi-training/)