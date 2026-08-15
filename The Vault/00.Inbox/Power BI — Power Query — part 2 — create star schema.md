---
title: "Power BI — Power Query — part 2 — create star schema"
source: "https://medium.com/@michalmolka/power-bi-power-query-part-2-create-star-schema-ed730095666"
author:
  - "[[Michal Molka]]"
published: 2021-12-24
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

In the previous chapter we cleaned the data. Now, it is the time to create a **Star Schema**.

At the beginning, we create a \[**Date**\]dimension. Use the following DAX code.

```c
Date = 
ADDCOLUMNS(
    CALENDARAUTO(),
    "Year", YEAR([Date]),
    "Quarter", QUARTER([Date]),
    "Month", MONTH([Date]),
    "Month Name", FORMAT(MONTH([Date]), "mmmm"),
    "Day", DAY([Date])
)
```
![](https://miro.medium.com/v2/resize:fit:1170/format:webp/1*DQbLiU5feh1IDkJTaCTB9g.png)

The **CALENDARAUTO()** function examines all **date** type columns in the model. Then looks for a minimum and maximum date. At the end, the function creates a column containing continuous range of dates. This range is based on the min/max values. The column contains full years.

Now, we define a \[**Store\]** dimension. Firstly, we can create a new dataset from the original one by referencing it.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*jxskSToOAv_LU6HtbUOtHg.png)

Select columns: a Store Number, a Store Name, an Address, a City, a Zip Code, a Store Location, a County. And choose a **Remove Other Columns** position.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*RD6Jx4hWYPkdnBDeh9HkFA.png)

Group the remaining columns.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZTwA4cNbSbipxtZup6vJdQ.png)

After the grouping is added, we need to make sure that a comparison of grouped values are **case insensitive**. Power Query performs this transformation as **case sensitive** by default.

Change the code in Advanced Editor.

```c
#"Grouped Rows" = Table.Group(#"Removed Other Columns", 
  {"Store Number", "Store Name", "Address", "City", "Zip Code", "Store Location", "County"}, 
  {{"Count", each Table.RowCount(_), Int64.Type}}, null, 
  Comparer.OrdinalIgnoreCase)
```

I’ve added two arguments at the end of the code: “ **null, Comparer.OrdinalIgnoreCase** ”.

You can ask a question why I used a “ **Count rows** ” operation as opposed to “ **All rows** ”. The answer is, performance. “ **All rows** ” creates an additional column which stores all values for a group from columns not present in a grouping condition.

At this stage, we have a lot of duplicates. Caused by a different naming convention or null values present in a few columns. For the purpose of this example we won’t investigate which data is correct or not.

To mitigate this problem. We can sort the data with following code.

```c
#"Sorted Rows" = Table.Sort(#"Grouped Rows", 
    {{"Store Number", Order.Descending}, 
    {"Store Name", Order.Descending}, 
    {"Address", Order.Descending}, 
    {"City", Order.Descending}, 
    {"Zip Code", Order.Descending}, 
    {"Store Location", Order.Descending}, 
    {"County", Order.Descending}})
```

…and we need to create an index for every \[**Store Number**\]column group. We have to group the data again. But we want to keep the order. Use this code, it saves table into a memory.

```c
#"Buffered" = Table.Buffer(#"Sorted Rows")
```

We can group the data by the \[**Store Number**\] column.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZpNcX1qx27ZxsvZSY4AyiA.png)

Add a **Custom column** with an **Index** function and put here a \[**Data**\] column.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*QZoRmfnqSmgaqzV564HhXg.png)

Expand a column \[**Index By Store ID**\]

![](https://miro.medium.com/v2/resize:fit:1314/format:webp/1*_Gfh92QHrAJ1gbIJJ1UcIw.png)

Remove the \[**Store ID**\] and the \[**Data**\] columns.

Now we have records grouped and numbered by the \[**Store Number**\] column.

![](https://miro.medium.com/v2/resize:fit:1114/format:webp/1*s-EL3tpob21i9aZRcw5RSQ.png)

Filter the table by an \[**Index By Store ID.Store By Store ID**\] column, choose a “ **1”** value.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*LICOqQ6CqaB7i3whzxT3OA.png)

Remove an unnecessary column and rename other ones.

```c
#"Removed Columns2" = Table.RemoveColumns(#"Filtered Rows",{"Index By Store ID.Store By Store ID"}),

#"Renamed Columns" = Table.RenameColumns(#"Removed Columns2",
    {{"Index By Store ID.Store Number", "Store Number"}, 
    {"Index By Store ID.Store Name", "Store Name"}, 
    {"Index By Store ID.Address", "Address"}, 
    {"Index By Store ID.City", "City"}, 
    {"Index By Store ID.Zip Code", "Zip Code"}, 
    {"Index By Store ID.Store Location", "Store Location"}, 
    {"Index By Store ID.County", "County"}})
```

It is the time to back to a \[**Zip Code**\] topic from the previous post.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*O4KkwNoRKxX9aems9Gqojw.png)

We can safely assume that we can replace a **712–2** value in second row with the first one **51529**. It isn’t the best way of dealing with such a problem. The best solution is reach to a source and investigate, why it has happened. Whether it is an error on an intended action. But, for now, it fulfills our purpose.

```c
#"Replaced Value" = Table.ReplaceValue(#"Removed Columns2", 
    "712–2","51529",
    Replacer.ReplaceText,
    {"Index By Store ID.Zip Code"})
```

Convert a \[**Store ID**\] and a \[**Zip Code**\] columns to a **whole number** data type. The second dimension is ready.

We can examine the last an \[**Item**\]dimension table. Most of steps is similar, like in a \[**Store\]** dimension case, with one difference.

In many cases, one **Item** is assigned to more than one **Category**. So we need to create a composite key (\[**Vendor Number**\] & \[**Category**\] & \[**Item Number**\]) — it is better to do this after your data is grouped and sorted, before an index column is added.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Y6dCuhEgOlEXeFyZOhu0LA.png)

Use the following code to add a new \[**Item Key**\] column which is the mentioned **composite key**.

```c
#"Merged Columns" = Table.CombineColumns(
    Table.TransformColumnTypes(#"Removed Other Columns", 
    {{"Item Number", type text}, 
    {"Vendor Number", type text}, 
    {"Category", type text}}, "en-US"),
    {"Item Number", "Vendor Number", "Category"},
    Combiner.CombineTextByDelimiter("", QuoteStyle.None),
    "Item Key")
```

After this, you can sort/group data by the **composite key**: \[**Item Description**\] & \[**Vendor Name**\] & \[**Category Name**\], group it and create an index for every group.

At the end, we need to delete unnecessary columns from a **Fact table** — this table should be referenced from the original entity. We can safely delete columns moved to dimensions and keep only a \[**Store Number**\], an \[**Item Key**\] and a \[**Date**\] columns.

![](https://miro.medium.com/v2/resize:fit:1282/format:webp/1*Xd-oQuIJt8Yeh4IlOu7H6g.png)

It is also a good idea to:

- change some column names for more descriptive,
- hide certain in the report view,
- replace null values to more descriptive value, “ **Unknown** ” for example.

Now, we can create relationships between a fact table and dimensions tables.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*L24S2fdNGNl9Bq4tHDJdDw.png)

Here is a full **M** code used to do the job:

```c
// Fact - Iowa_Liquir_Sales

let
    Source = Parquet.Document(File.Contents("D:\Iowa_Liquor_Sales.parquet")),
    #"Removed Columns" = Table.RemoveColumns(Source,{"Invoice/Item Number"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Removed Columns",{{"Date", type date}}),
    #"Added Custom" = Table.AddColumn(#"Changed Type", "Item Number - clean", each Text.Remove([Item Number], {"a".."z", "A".."Z"})),
    #"Removed Columns1" = Table.RemoveColumns(#"Added Custom",{"Item Number"}),
    #"Changed Type1" = Table.TransformColumnTypes(#"Removed Columns1",{{"Item Number - clean", Int64.Type}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type1",{{"Item Number - clean", "Item Number"}}),
    #"Removed Columns2" = Table.RemoveColumns(#"Renamed Columns",{"Store Name", "Address", "City", "Zip Code", "Store Location", "County Number", "County", "Category Name", "Vendor Name", "Item Description"}),
    #"Merged Columns" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns2", {{"Item Number", type text}, {"Category", type text}, {"Vendor Number", type text}}, "en-US"),{"Item Number", "Category", "Vendor Number"},Combiner.CombineTextByDelimiter("", QuoteStyle.None),"Item Key"),
    #"Changed Type2" = Table.TransformColumnTypes(#"Merged Columns",{{"Item Key", Int64.Type}}),
    #"Renamed Columns1" = Table.RenameColumns(#"Changed Type2",{{"Store Number", "Store Key"}})
in
    #"Renamed Columns1"
    
// Dimension - Item

let
    Source = Hub,
    #"Removed Other Columns" = Table.SelectColumns(Source,{"Item Number", "Item Description", "Vendor Name", "Vendor Number", "Category Name", "Category"}),
    #"Grouped Rows" = Table.Group(#"Removed Other Columns", {"Item Number", "Item Description", "Category", "Category Name", "Vendor Number", "Vendor Name"}, {{"Count", each Table.RowCount(_), Int64.Type}}),
    #"Merged Columns" = Table.CombineColumns(Table.TransformColumnTypes(#"Grouped Rows", {{"Item Number", type text}, {"Category", type text}, {"Vendor Number", type text}}, "en-US"),{"Item Number", "Category", "Vendor Number"},Combiner.CombineTextByDelimiter("", QuoteStyle.None),"Item Key"),
    #"Removed Columns" = Table.RemoveColumns(#"Merged Columns",{"Count"}),
    #"Sorted Rows" = Table.Sort(#"Removed Columns", {{"Item Key", Order.Descending}, {"Item Description", Order.Descending}, {"Category Name", Order.Descending}, {"Vendor Name", Order.Descending} }),
    #"Buffered Table" = Table.Buffer(#"Sorted Rows"),
    #"Grouped Rows1" = Table.Group(#"Buffered Table", {"Item Key"}, {{"Data", each _, type table [Item Description=nullable text, Category Name=nullable text, Item Key=text, Vendor Name=nullable text]}}),
    #"Added Custom" = Table.AddColumn(#"Grouped Rows1", "Indexed Item Key", each Table.AddIndexColumn([Data],"Indexed Item Key", 1, 1)),
    #"Expanded Indexed Item Key" = Table.ExpandTableColumn(#"Added Custom", "Indexed Item Key", {"Item Description", "Category Name", "Item Key", "Vendor Name", "Indexed Item Key"}, {"Indexed Item Key.Item Description", "Indexed Item Key.Category Name", "Indexed Item Key.Item Key", "Indexed Item Key.Vendor Name", "Indexed Item Key.Indexed Item Key"}),
    #"Removed Columns1" = Table.RemoveColumns(#"Expanded Indexed Item Key",{"Item Key", "Data"}),
    #"Filtered Rows" = Table.SelectRows(#"Removed Columns1", each ([Indexed Item Key.Indexed Item Key] = 1)),
    #"Removed Columns2" = Table.RemoveColumns(#"Filtered Rows",{"Indexed Item Key.Indexed Item Key"}),
    #"Reordered Columns" = Table.ReorderColumns(#"Removed Columns2",{"Indexed Item Key.Item Key", "Indexed Item Key.Item Description", "Indexed Item Key.Category Name", "Indexed Item Key.Vendor Name"}),
    #"Renamed Columns" = Table.RenameColumns(#"Reordered Columns",{{"Indexed Item Key.Item Key", "Item Key"}, {"Indexed Item Key.Item Description", "Item Description"}, {"Indexed Item Key.Category Name", "Category Name"}, {"Indexed Item Key.Vendor Name", "Vendor Name"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Item Key", Int64.Type}})
in
    #"Changed Type"

// Dimension - Store

let
    Source = Hub,
    #"Removed Other Columns" = Table.SelectColumns(Source,{"Store Name", "Store Number", "Address", "City", "Zip Code", "Store Location", "County"}),
    #"Grouped Rows" = Table.Group(#"Removed Other Columns", {"Store Number", "Store Name", "Address", "City", "Zip Code", "Store Location", "County"}, {{"Count", each Table.RowCount(_), Int64.Type}}, null, Comparer.OrdinalIgnoreCase),
    #"Removed Columns" = Table.RemoveColumns(#"Grouped Rows",{"Count"}),
    #"Sorted Rows" = Table.Sort(#"Grouped Rows", {{"Store Number", Order.Descending}, {"Store Name", Order.Descending}, {"Address", Order.Descending}, {"City", Order.Descending}, {"Zip Code", Order.Descending}, {"Store Location", Order.Descending}, {"County", Order.Descending}}),
    #"Buffered" = Table.Buffer(#"Sorted Rows"),
    #"Grouped Rows1" = Table.Group(Buffered, {"Store Number"}, {{"Data", each _, type table [Store Number=nullable number, Store Name=nullable text, Address=nullable text, City=nullable text, Zip Code=nullable text, Store Location=nullable text, County=nullable text, Count=number]}}),
    #"Added Custom" = Table.AddColumn(#"Grouped Rows1", "Index By Store ID", each Table.AddIndexColumn([Data], "Store By Store ID", 1,1)),
    #"Expanded Index By Store ID" = Table.ExpandTableColumn(#"Added Custom", "Index By Store ID", {"Store Number", "Store Name", "Address", "City", "Zip Code", "Store Location", "County", "Store By Store ID"}, {"Index By Store ID.Store Number", "Index By Store ID.Store Name", "Index By Store ID.Address", "Index By Store ID.City", "Index By Store ID.Zip Code", "Index By Store ID.Store Location", "Index By Store ID.County", "Index By Store ID.Store By Store ID"}),
    #"Removed Columns1" = Table.RemoveColumns(#"Expanded Index By Store ID",{"Store Number", "Data"}),
    #"Filtered Rows" = Table.SelectRows(#"Removed Columns1", each ([Index By Store ID.Store By Store ID] = 1)),
    #"Removed Columns2" = Table.RemoveColumns(#"Filtered Rows",{"Index By Store ID.Store By Store ID"}),
    #"Replaced Value" = Table.ReplaceValue(#"Removed Columns2","712-2","51529",Replacer.ReplaceText,{"Index By Store ID.Zip Code"}),
    #"Renamed Columns" = Table.RenameColumns(#"Replaced Value",{{"Index By Store ID.Store Number", "Store Number"}, {"Index By Store ID.Store Name", "Store Name"}, {"Index By Store ID.Address", "Address"}, {"Index By Store ID.City", "City"}, {"Index By Store ID.Zip Code", "Zip Code"}, {"Index By Store ID.Store Location", "Store Location"}, {"Index By Store ID.County", "County"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Store Number", Int64.Type}, {"Zip Code", Int64.Type}}),
    #"Renamed Columns1" = Table.RenameColumns(#"Changed Type",{{"Store Number", "Store Key"}})
in
    #"Renamed Columns1"
```

At the end, turn off an **Include in report refresh** and an **Enable load** option for a **Hub** dataset (all created tables have been referenced from this dataset).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*OiONP5dgIPP-FUiqCU1J4g.png)

Currently our model is 107 Mb size. It contains 3 dimension tables and one fact table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WUvBw_Pz9nSpYaBFpeuAKA.png)