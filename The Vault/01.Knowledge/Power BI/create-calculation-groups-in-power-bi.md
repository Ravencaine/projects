---
title: "Create calculation groups in Power BI"
source: "https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups"
author: "learn.microsoft.com"
date: "2026-08-11"
tags: [imported, reading-list, reading-list]
created: "2026-08-11"
---

> Learn how to create calculation groups in Power BI.

Create calculation groups in Power BI - Power BI | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Reading mode Table of contents Read in English Add Add to Plans Edit Copy Markdown Print Note Access to this page requires authorization. You can try signing in or changing directories . Access to this page requires authorization. You can try changing directories . Create calculation groups Feedback Summarize this article for me Calculation groups can significantly reduce the number of redundant measures you have to create, by allowing you define Data Analysis Expressions (DAX) formulas as calculation items. Calculation items can be applied to existing measures in your model. More information about calculation groups is available in the Calculation groups article. Add a new calculation group in model view In Power BI , when editing a semantic model, navigate to Model view and select the Calculation group button in the ribbon. If you're not already in Model explorer , the Data pane opens to the Model view. If the discourage implicit measures property is turned off, you're prompted with a dialog window to turn it on to enabling creation of the calculation group. An implicit measure occurs when, in the Report view , you use a data column from the Data pane directly in the visual. The visual allows you to aggregate it as a  ,  ,  ,  , or some other basic aggregation, which becomes an implicit measure. When a calculation group is added to a model, Power BI discourages the creation of implicit measures by no longer showing the summation symbol next to the data columns in the Data pane, and blocks adding the data columns to the visuals directly as values. Existing implicit measures already created in visuals continue to work. The Discourage implicit measures property must be enabled because calculation items don't apply to implicit measures. Calculation items only apply to measures or explicit measures. A measure or explicit measure occurs when you create a New measure and define the DAX expression to aggregate a data column. Explicit measures can also have conditional logic and filters, taking full advantage of what you can do with DAX. Tutorial: You can learn how to Create your own measures in Power BI Desktop . Note Calculation item expressions can be written to ignore a measure by the name, or by data type, for scenarios when you have measures you don't want the calculation item to change. Once you select Yes to enable the discourage implicit measures property, a calculation group is added and you can start defining the DAX expression of the first calculation item in the DAX formula bar. The dialog won't show if you already have discourage implicit measures enabled.  is a DAX function that acts as a placeholder for the measure in the calculation item expression. You can learn about the SELECTEDMEASURE DAX function from its article. Add a calculation group by using Power BI TMDL view You can create a calculation group in the Tabular Model Definition Language or TMDL view of Power BI Desktop. Edit the semantic model and use this TMDL script. Time intelligence example There's a Time Intelligence example of a calculation group available at in the Calculation groups in Analysis Services tabular models article, which we can use to populate some calculation items. The example can be added to any model with a Date table, or you can download the Adventure Works DW 2020 PBIX from DAX sample model - DAX . Rename a calculation group To rename the calculation group, double-click it in the Data pane, or you can select it and use the Properties pane. Rename a calculation group column To rename the calculation group column, double-click it in the Data pane, or you can select it and use the Properties pane. The column you select is the column you use on visuals or in slicers to apply a specific calculation item. Rename a calculation item The first calculation item was created as SELECTEDMEASURE() so it can be renamed by double-clicking or using the Properties pane as well. Create more calculation items To create more calculation items, you can use the right-click context menu of the Calculation items section or the calculation group itself and choose New calculation item , or use the Properties pane of the Calculation items section. Once all the Time intelligence calculation items are added, the calculation group looks like the following image. Notice the red triangle icons indicating errors. The errors are there because the example DAX expressions use the Date table called DimDate , so I need to update the DAX expressions to use the name Date instead. The following image shows the DAX expression before the correction. Once I make the correction to the DAX expression, the error disappears. Once I make the corrections for each of the errors in the calculation items, the red triangle warning icons no longer appear. Reorder calculation items To reorder the calculation items in whatever logical way you prefer, 

## Code / Examples

```
SUM
```
```
AVERAGE
```
```
MIN
```
```
MAX
```
```
SELECTEDMEASURE
```
```
Orders = DISTINCTCOUNT('Sales Order'[Sales Order])
```


---
*Source: [learn.microsoft.com](https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups)*
