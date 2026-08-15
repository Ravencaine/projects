---
title: "Power BI — Power Query — part 1 — data cleansing"
source: "https://medium.com/@michalmolka/power-bi-power-query-part-1-data-cleaning-b350c19c6e20"
author:
  - "[[Michal Molka]]"
published: 2021-12-10
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Most of ETL processes are performed on a database/file level. Processed data lands in a Data Warehouse or a Data Lake where you can use it in your Power BI model. I can say, that most of the work in terms of modelling is performed by an ETL team. A new approach is an ELT. Where most of the data are stored in files, partially prepared or not.

Today, we play around with a second approach. Let’s assume that our Data Integration team prepared a parquet file. Data wasn’t modelled, isn’t consistent and there are a few errors.

You can download a.csv source file here: [Iowa Liquor Sales | data.iowa.gov](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy)

A dataset domain is sales data of liquors in Iowa. The file includes 21.4 million records. A file size is 4.73 GB, after converting it to parquet, it’s size dropped to 715 MB.

Here is a dataset structure:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aQH4OzsV4isvl2v0_STg9w.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*J_mlANErgPzQZtVBC9oleg.png)

After import data into Power BI, a model size is 1.57 GB.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Y087JZSIFBa-CroTBdIRGg.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aXn4-ewHpZeRDaH4Ha3ekA.png)

In order to optimize our model, we need to wonder if some columns are unnecessary. In this case, an \[**Invoice/Item number**\] column can be safely removed. It is very rare to use an invoice number in analyses. And as you noticed it’s size is 1.3 GB.

![](https://miro.medium.com/v2/resize:fit:1344/format:webp/1*VO__QbfqDl8B7qpn-UYORw.png)

In the second step we check if Power BI assigned a proper data type to columns.

We can notice that a \[**Date**\], a \[**Zip Code**\], a \[**Item Number**\] are assigned as a string type. We want to have the \[**Date**\] column saved as **date** type, and a **whole number** in another two cases.

![](https://miro.medium.com/v2/resize:fit:1300/format:webp/1*WmKa5L-b8NyhY-DQjPFM4Q.png)

Let’s check if the \[**Date**\] column can be safely converted.

```c
EVALUATE
CALCULATETABLE (
    VALUES ( Iowa_Liquor_Sales[Date] ),
    IFERROR ( DATEVALUE ( Iowa_Liquor_Sales[Date] ), 1 ) = 1
)
```

As you see on the screen, all records are valid, so that, the column can be safely converted.

![](https://miro.medium.com/v2/resize:fit:1174/format:webp/1*7A2SraN4xiVbBFcBIdJ3CA.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*4zgjt73ZXXMLoCa9XKhLhQ.png)

In the case of the \[**Zip Code**\] and the \[**Item Number**\] columns we will use another code.

```c
EVALUATE
CALCULATETABLE (
    VALUES ( Iowa_Liquor_Sales[Zip Code] ), // [Item Number]
    IFERROR (
        VALUE (
            SUBSTITUTE (
                SUBSTITUTE (
                    SUBSTITUTE (
                        SUBSTITUTE ( Iowa_Liquor_Sales[Zip Code], // [Item Number]
                           "-", "some_word" ),
                            "/", "some_word"),
                            ".", "some_word"),
                            ",", "some_word")
        ), 1) = 1
)
```

The \[**Item Name**\] has one value which is a string type, based on anther records pattern, we can safely presume that the “x” prefix is invalid.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*4yV_S8DyVAjqO_ugzvdQcA.png)

Here is a Power Query code which solves the problem:

```c
#"Added Custom" = Table.AddColumn(#"Changed Type", "Item Number - clean", each Text.Remove([Item Number], {"a".."z", "A".."Z"}))
#"Changed Type1" = Table.TransformColumnTypes(#"Removed Columns1",{{"Item Number - clean", Int64.Type}}),
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*quPB94fx0XH4XwgfgS6IwA.png)

The \[**Zip Code**\] column is more interesting topic.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*AyLzoO3Ch27Ri6ZlwRwa5w.png)

You might wonder why I have used the **SUBSTITUTE()** function. Here is an answer. The **VALUE()** function converts valid string values to numeric ones. But if a string contains one of these chars: “**,**” or “**.**” Then the value is valid **numeric** type value. In case of these values: “ **/** ” or“ **\-** ” the value is a valid **date** type value and it can be converted to numeric data type.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ez94y0SWyTxZehLFdgDPJw.png)

We will deal with this topic in the next post: [Power BI — Power Query — part 2 — create star schema (medium.com)](https://michalmolka.medium.com/power-bi-power-query-part-2-create-star-schema-ed730095666), where we create dimensions for the model.