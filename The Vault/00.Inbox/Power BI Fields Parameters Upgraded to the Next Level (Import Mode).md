---
title: "Power BI Fields Parameters Upgraded to the Next Level (Import Mode)"
source: "https://medium.com/microsoft-power-bi/power-bi-fields-parameters-upgraded-to-the-next-level-import-mode-fb4545d83ed2"
author:
  - "[[Mateusz Mossakowski]]"
published: 2025-01-16
created: 2026-08-12
description: "What if I told you that you can actually build fields parameters tables as imported ones instead of calculated ones? Of course, I didn’t discover this myself. I read about it in Owen Auger’s blog. Regardless, this approach can significantly facilitate the creation and maintenance of these tables, in my view."
Processed: "Unprocessed"
---
## What if I told you that you can actually build fields parameters tables as imported ones instead of calculated ones? Of course, I didn’t discover this myself. I read about it in Owen Auger’s blog. Regardless, this approach can significantly facilitate the creation and maintenance of these tables, in my view.

While creating and maintaining fields parameters tables as calculated tables is usually not an issue at all, it can become a bit problematic once you expand the table with some additional columns that are responsible for adding grouping layers to the fields parameters. For instance, you might want to group measures by topic (one bucket for absolutes, another for indices versus year ago and one more for the absolute difference versus year ago), and by currency. Instead of implementing a SWITCH in your measures, you might prefer to have separate local currency, USD, and EUR measures, where currency selection is driven by a currency column added to the field parameters definition.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*MM87zdH0Oi64xz5CTzplzg.png)

expanded fields parameters table “generator” in Excel 😊

Once you’re dealing with an expanded table like the one above, just imagine maintaining it directly within the semantic model through DAX definition. I would say you might start to dislike your job pretty quickly if you have to stick with that for a longer period. To avoid this frustration, you might consider storing the DAX definition somewhere outside the Power BI semantic model (even a SharePoint Excel file could work) 🙃. However, this means you would need to copy and paste the DAX code each time you make adjustments, such as adding or removing measures. But when you realize that you can actually import the table and that you don’t need to generate any DAX at all, you might just jump for joy!

There are actually two major steps that you need to perform within the imported table to make this happen. You need to set the JSON ***ParameterMetadata*** for the Field Parameter column and add the ***Group By*** setting to the Field Name column (it needs to be grouped by the Field Parameter column). Of course, it doesn’t hurt to also add proper sorting and to hide everything apart from the Field Name column😊

Below, you can see a completely dummy import table created solely for demonstration purposes. At this point, there’s nothing special about this imported table. None of its columns will act as field parameters for now.

![](https://miro.medium.com/v2/resize:fit:1176/format:webp/1*lzhwFnDjguwD3tfNIAzjXg.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*zyV14qxGWeUISAG7jXW2_Q.png)

To make it work, we need to:

(1) Set the JSON ParameterMetadata for the Field Parameter column.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*BhSnZjQn9B1Y_1MggMIUsw.png)

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*1RuSns20_nZsrgkDrKWWrQ.png)

(2) add the Group By setting to the Field Name column (it needs to be grouped by the Field Parameter column).

![](https://miro.medium.com/v2/resize:fit:1250/format:webp/1*s-6Yvhpn91_v9UfJSsNowQ.png)

Once the above changes are made, you will have a fully functional field parameter table that is an imported table. Hurray!

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*CszoSPuRDWu--YOTbWVQJw.png)

Before you start looking at the world through rose-colored glasses, let me present a scenario where you might still have some concerns. Imagine that someone changed the measure name from “test measure ***2*** ” to “test measure ***3*** ” or simply deleted it in the semantic model, but this change was not reflected in the imported fields parameters table input.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*dAKW6aIHK5lKYP1NoekAzg.png)

before measure rename

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*p8yXUr43TAabwVjYt8k2xQ.png)

after measure rename

How can we prevent this? We can actually add another layer here. This time, it will be a calculated table built on top of the imported one. The primary purpose of this table is to limit its content to only those objects (measures and columns) that currently exist in the semantic model. To achieve this, we can make use of the wonderful INFO.VIEW functions to retrieve a list of all columns and measures present in the current semantic model.

Below you can find the DAX code responsible for the calculated table:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rCiHJRKiQVmrHacRvqgEuA.png)

*¯\\\_(ツ)\_/¯ No surprise here: you will also need to perform steps related to the JSON extended property and ensure proper grouping by.*

Once this is done, you can start using the fields parameters column from the new calculated table. This time, the report will still function properly, even if someone mistakenly renames an object to a name that does not exist in the model or simply deletes it, and this deletion is not reflected in the external fields parameters input. It won’t result in broken visuals, even if there is a discrepancy between the objects in the semantic model and those provided in the field parameters table input. The “discrepancy” object would simply not be present in the visual.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*dfs_XZVNIMk5-lGCJZAI-Q.png)

adjusted approach — no broken visuals

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*jya15edZwFla3f4D)

Of course, you can perform all the above-mentioned steps manually, but I’m offering a more convenient one-click approach for that. 😊 You can save the C# script below as a Tabular Editor macro and reuse it across multiple tables in different models (if needed).

What does the code do? It creates (or overwrites) a calculated table on top of the imported fields parameter table, adds the JSON extended property, and sets the proper grouping by, making this a fully functional field parameters table. Additionally, it completely hides the import table, ensuring that it is not accessible to any of the semantic model consumers by default.

```c
// Define crucial column names for the calculated fields
var field_name = "FieldName";
var field_parameter = "FieldParameter";
var field_sort = "FieldSort";

// Get the currently selected table and its name
var selected_table = Selected.Table;
var selected_table_name = selected_table.Name;

// Construct the name for the calculated fields parameters table
var calculated_table_name = selected_table_name + " calc FP";

// Hide the original imported table from the model view
selected_table.IsHidden = true;

// Generate DAX expression for the calculated table
// This expression returns only objects that exist in the model
var calculated_table_dax = @"
VAR _available_columns = 
SELECTCOLUMNS(
    FILTER(
        INFO.VIEW.COLUMNS(),
        [Type] = ""Data""
    ),
    ""FullyQualifiedName"", [Table] & ""["" & [Name] & ""]""
)
VAR _available_measures = 
SELECTCOLUMNS(
    INFO.VIEW.MEASURES(),
    ""FullyQualifiedName"", ""["" & [Name] & ""]""
)
VAR _available_objects =
UNION(
    _available_columns,
    _available_measures
)
VAR _result = 
FILTER(
    '" + selected_table_name + @"',
    '" + selected_table_name + "'[" + field_parameter + @"] IN _available_objects
)
RETURN
    _result";

// Check if the calculated fields parameters table already exists in the model
// If it does, delete it to ensure a fresh creation
bool tableExists = Model.Tables.Any(t => t.Name.Equals(calculated_table_name));

// Declare a variable to hold the calculated table
Table table = null; 

if (tableExists)
{
    // Delete the existing table and recreate it
    Model.Tables[calculated_table_name].Delete();
    table = Model.AddCalculatedTable(calculated_table_name, calculated_table_dax);
}
else 
{
    // Create a new calculated table based on the DAX expression
    table = Model.AddCalculatedTable(calculated_table_name, calculated_table_dax);
}

// Configure advanced properties for the fields parameter table
var field_name_column = table.Columns[field_name];
var field_parameter_column = table.Columns[field_parameter];
var field_sort_column = table.Columns[field_sort];

// Set sorting and grouping for the relevant columns
field_name_column.SortByColumn = field_sort_column;
field_name_column.GroupByColumns.Add(field_parameter_column);
field_parameter_column.SortByColumn = field_sort_column;

// Set extended properties for metadata and hide unnecessary columns
field_parameter_column.SetExtendedProperty("ParameterMetadata", "{\"version\":3,\"kind\":2}", ExtendedPropertyType.Json);
field_parameter_column.IsHidden = true;
field_sort_column.IsHidden = true;
```

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----fb4545d83ed2---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee