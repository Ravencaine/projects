---
title: "Create calculation groups in Power BI"
source: "https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups"
author:
  - "[[kgremban]]"
published:
created: 2026-08-04
description: "Learn how to create calculation groups in Power BI."
Processed: "Unprocessed"
---
## Create calculation groups

Calculation groups can significantly reduce the number of redundant measures you have to create, by allowing you define Data Analysis Expressions (DAX) formulas as calculation items. Calculation items can be applied to existing measures in your model. More information about calculation groups is available in the [Calculation groups](https://learn.microsoft.com/en-us/analysis-services/tabular-models/calculation-groups) article.

## Add a new calculation group in model view

In **Power BI**, when editing a semantic model, navigate to **Model view** and select the **Calculation group** button in the ribbon. If you're not already in **Model explorer**, the **Data** pane opens to the **Model** view.

![Screenshot of calculation groups button in the ribbon.](99.System/Attachments/Screenshot_of_calculation_groups_button_in_the_ribbon.png)

Screenshot of calculation groups button in the ribbon.

If the **discourage implicit measures** property is turned off, you're prompted with a dialog window to turn it on to enabling creation of the calculation group.

![Screenshot of dialog window prompting you to enable implicit measures.](99.System/Attachments/Screenshot_of_dialog_window_prompting_you_to_enable_implicit_measures.png)

Screenshot of dialog window prompting you to enable implicit measures.

An *implicit measure* occurs when, in the **Report view**, you use a data column from the **Data** pane directly in the visual. The visual allows you to aggregate it as a `SUM`, `AVERAGE`, `MIN`, `MAX`, or some other basic aggregation, which becomes an implicit measure. When a calculation group is added to a model, Power BI discourages the creation of implicit measures by no longer showing the summation symbol next to the data columns in the Data pane, and blocks adding the data columns to the visuals directly as values. Existing implicit measures already created in visuals continue to work. The **Discourage implicit measures** property must be enabled because calculation items don't apply to implicit measures. Calculation items only apply to measures or explicit measures.

![Screenshot of Report view and creation of implicit measures.](99.System/Attachments/Screenshot_of_Report_view_and_creation_of_implicit_measures.png)

Screenshot of Report view and creation of implicit measures.

A measure or explicit measure occurs when you create a **New measure** and define the DAX expression to aggregate a data column. Explicit measures can also have conditional logic and filters, taking full advantage of what you can do with DAX. Tutorial: You can learn how to [Create your own measures in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-tutorial-create-measures).

Once you select **Yes** to enable the **discourage implicit measures** property, a calculation group is added and you can start defining the DAX expression of the first calculation item in the DAX formula bar. The dialog won't show if you already have **discourage implicit measures** enabled.

`SELECTEDMEASURE` is a DAX function that acts as a placeholder for the measure in the calculation item expression. You can learn about the [SELECTEDMEASURE DAX function](https://learn.microsoft.com/en-us/dax/selectedmeasure-function-dax) from its article.

![Screenshot of DAX formula bar and calculation group.](99.System/Attachments/Screenshot_of_DAX_formula_bar_and_calculation_group.png)

Screenshot of DAX formula bar and calculation group.

### Add a calculation group by using Power BI TMDL view

You can create a calculation group in the Tabular Model Definition Language or **TMDL view** of Power BI Desktop. Edit the semantic model and use this TMDL script.

TMDL

```tmdl
createOrReplace

    table 'Calculation group'

        calculationGroup
            precedence: 1

            calculationItem 'Calculation item' = SELECTEDMEASURE()

        column 'Calculation group column'
            dataType: string
            summarizeBy: none
            sourceColumn: Name
            sortByColumn: Ordinal

            annotation SummarizationSetBy = Automatic

        column Ordinal
            dataType: int64
            formatString: 0
            summarizeBy: sum
            sourceColumn: Ordinal

            annotation SummarizationSetBy = Automatic
```

## Time intelligence example

There's a Time Intelligence example of a calculation group available at in the [Calculation groups in Analysis Services tabular models](https://learn.microsoft.com/en-us/analysis-services/tabular-models/calculation-groups) article, which we can use to populate some calculation items. The example can be added to any model with a **Date** table, or you can download the Adventure Works DW 2020 PBIX from [DAX sample model - DAX](https://learn.microsoft.com/en-us/dax/dax-sample-model).

### Rename a calculation group

To rename the calculation group, double-click it in the **Data** pane, or you can select it and use the **Properties** pane.

![Screenshot of how to rename a calculation group.](99.System/Attachments/Screenshot_of_how_to_rename_a_calculation_group.png)

Screenshot of how to rename a calculation group.

### Rename a calculation group column

To rename the calculation group column, double-click it in the **Data** pane, or you can select it and use the **Properties** pane. The column you select is the column you use on visuals or in slicers to apply a specific calculation item.

![Screenshot of how to rename a calculation group column.](99.System/Attachments/Screenshot_of_how_to_rename_a_calculation_group_column.png)

Screenshot of how to rename a calculation group column.

### Rename a calculation item

The first calculation item was created as SELECTEDMEASURE() so it can be renamed by double-clicking or using the **Properties** pane as well.

![Screenshot of how to rename a calculation item.](99.System/Attachments/Screenshot_of_how_to_rename_a_calculation_item.png)

Screenshot of how to rename a calculation item.

### Create more calculation items

To create more calculation items, you can use the right-click context menu of the **Calculation items** section or the calculation group itself and choose **New calculation item**, or use the **Properties pane** of the **Calculation items** section.

![Screenshot of how to create a new calculation item.](99.System/Attachments/Screenshot_of_how_to_create_a_new_calculation_item.png)

Screenshot of how to create a new calculation item.

Once all the Time intelligence calculation items are added, the calculation group looks like the following image.

![Screenshot of calculation group with all time intelligence calculation items.](99.System/Attachments/Screenshot_of_calculation_group_with_all_time_intelligence_calculation_items.png)

Screenshot of calculation group with all time intelligence calculation items.

Notice the red triangle icons indicating errors. The errors are there because the example DAX expressions use the Date table called *DimDate*, so I need to update the DAX expressions to use the name *Date* instead. The following image shows the DAX expression before the correction.

![Screenshot of incorrect DAX expression.](99.System/Attachments/Screenshot_of_incorrect_DAX_expression.png)

Screenshot of incorrect DAX expression.

Once I make the correction to the DAX expression, the error disappears.

![Screenshot of corrected DAX expression.](99.System/Attachments/Screenshot_of_corrected_DAX_expression.png)

Screenshot of corrected DAX expression.

Once I make the corrections for each of the errors in the calculation items, the red triangle warning icons no longer appear.

![Screenshot of corrected DAX expressions in the calculation items area.](99.System/Attachments/Screenshot_of_corrected_DAX_expressions_in_the_calculation_items_area.png)

Screenshot of corrected DAX expressions in the calculation items area.

### Reorder calculation items

To reorder the calculation items in whatever logical way you prefer, you can select the **Calculation items** section in the **Properties** pane, or right-click context menu of the calculation item to move it up or down in the list.

![Screenshot of reordering calculation items.](99.System/Attachments/Screenshot_of_reordering_calculation_items.png)

Screenshot of reordering calculation items.

### Add a dynamic format string to a calculation item

Calculation items use the underlying measure formatting by default. We might want to instead display *YOY%* as a percentage. To do so, select the *YOY%* calculation item, then turn on **Dynamic format string** in the properties pane, which allows you to specify a DAX expression to create a format string. For this example, it doesn’t require any conditional elements, so simply *#,##0.00%* changes the format to a percentage when this calculation item is applied, as shown in the following image.

![Screenshot of changing format of underlying data items.](99.System/Attachments/Screenshot_of_changing_format_of_underlying_data_items.png)

Screenshot of changing format of underlying data items.

### Using the calculation group in reports

To use your new calculation group in a Report, go to the **Report** view, create a **Matrix** visual and add the following:

1. **Month** column from the **Date** table to the **Rows**
2. **Time Calculation** from the **Time Intelligence** calculation group to the **Columns**
3. **Orders** measure to the **Values**

`Orders = DISTINCTCOUNT('Sales Order'[Sales Order])`

The following image shows building a visual.

![Screenshot of using calculation groups in reports.](99.System/Attachments/Screenshot_of_using_calculation_groups_in_reports.png)

Screenshot of using calculation groups in reports.

Calculation items on the **Columns** in the **Matrix** visual are showing the measure **Orders** grouped by each of the calculation items. You can also apply an individual calculation item to multiple measures by adding the **calculation group column** to a **Slicer** visual.

![Screenshot of applying individual calculation items to multiple measures.](99.System/Attachments/Screenshot_of_applying_individual_calculation_items_to_multiple_measures.png)

Screenshot of applying individual calculation items to multiple measures.

### Using the calculation item in measures

You can create a new measure with an expression utilizing a calculation item on a specific measure.

To create an *\[Orders YOY%\]* measure, you can use the calculation item with CALCULATE.

DAX

```dax
Orders YOY% = 
    CALCULATE(
        [Orders],
        'Time Intelligence'[Time Calculation] = "YOY%"
    )
```

### Setting calculation group precedence

Finally, if you add more calculation groups to the model you can specify the order in which they apply to a measure with the precedence property. You can adjust the calculation group precedence in the **Calculation groups section** properties pane, as shown in the following image.

![Screenshot of setting calculation group precedence.](99.System/Attachments/Screenshot_of_setting_calculation_group_precedence.png)

Screenshot of setting calculation group precedence.

You can learn more about calculation groups precedence in the [Calculation groups in Analysis Services tabular models](https://learn.microsoft.com/en-us/analysis-services/tabular-models/calculation-groups) article.

## Selection expressions for calculation groups

You can set selection expressions for calculation groups to get fine-grained control over what the calculation group returns if users make multiple, invalid or no selections on the calculation group. See [selection expressions](https://learn.microsoft.com/en-us/analysis-services/tabular-models/calculation-groups/#selection-expressions).

## Considerations

### Model measures change to variant data type

As soon as a calculation group is added to a semantic model, Power BI reports use the **variant** data type for all measures. If afterwards, all calculation groups are removed from the model the measures revert to their original data types again.

The variant data type may cause [dynamic format strings for measures](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-dynamic-format-strings) using a measure for re-use to show an error. Use the [FORMAT](https://learn.microsoft.com/en-us/dax/format-function-dax) DAX function to force the variant measure to be recognized as a string data type again.

DAX

```dax
FORMAT([Dynamic format string], "")
```

Alternatively, you can re-use your expression for dynamic format strings with a [DAX user-defined function](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-user-defined-functions-overview) instead.

### Visuals error when a calculation item applies a math operation on a non-numeric measure

Non-numeric measures are commonly used for dynamic titles in visuals and in dynamic format strings for measures. The error **Cannot convert value... of type Text to type Numeric** shows on visuals impacted. The calculation item expression can avoid this error by adding a check to see if the measure is numeric before applying the math operation. Use the [ISNUMERIC](https://learn.microsoft.com/en-us/dax/isnumeric-function-dax) in the calculation item.

DAX

```dax
Calculation item safe = 
    IF ( 
        // Check the measure is numeric
        ISNUMERIC( SELECTEDMEASURE() ),
            SELECTEDMEASURE() * 2,
            // Don't apply the calculation on a non-numeric measure
            SELECTEDMEASURE()
        )
```