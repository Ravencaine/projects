---
title: "Power BI — TMDL — Tabular Model Definition Language"
source: "https://medium.com/microsoft-power-bi/power-bi-tmdl-tabular-model-definition-language-2cca06e87921"
author:
  - "[[Michal Molka]]"
published: 2026-02-01
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GU85qXVDzlsKQnmQyCtR3g.png)

In the last post, I touched on a control versioning topic in a Power BI context. Today’s subject is partially related. You can check it out before: [Power BI report — control versioning](https://medium.com/p/b71a45f16ca6) — we were working with a visualization layer back then. Today we are going to look at a model layer and how we can operate on it with a TMDL language.

So, we have a model.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EISVnvnaghy0xu6uJSuIag.png)

Like in the last post. I saved the report as a **.pbip** project. Thanks to this, we are able to look at TMDL files. You need to remember to have this option turned on.

![](https://miro.medium.com/v2/resize:fit:1396/format:webp/1*kixAyqcNwrmerRA5a72oiQ.png)

Let’s take a use case. I created a model where every table is sourced from a separate.csv file lying on a local drive. I want to change all the files to be sourced from OneDrive. A classic approach would take us to the Tabular Editor application or have us do the job in the Power Query window.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LZFUp8gYq-AFKuVRqwbQ2w.png)

With TMDL we have other ways to make it work.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

**The first option: Power BI Desktop — a TMDL editor.**

In the TMDL editor -> Script TMDL to -> Script tab

![](https://miro.medium.com/v2/resize:fit:1312/format:webp/1*kghGoq3UMXT2Vz5rfTpr-Q.png)

Then, we can edit most aspects related to the table through code.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*J5LRW98B24jopgYX1qAU5Q.png)

A change we want to apply is at the end.

```c
partition 'Fact Sale' = m
 mode: import
 source =
   let
       Source = Csv.Document(File.Contents("C:\Users\d******l\Downloads\iowa_csv\Iowa_FactSale.csv\part-00000-e1a14094-35f0-448c-b973-4bcf22858e25-c000.csv"),[Delimiter=",", Columns=17, Encoding=1252, QuoteStyle=QuoteStyle.None]),
       #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
       #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"ID", Int64.Type}, {"InvoiceItemNumber", type text}, {"Date", Int64.Type}, {"StoreID", Int64.Type}, {"CategoryID", Int64.Type}, {"VendorID", Int64.Type}, {"ItemID", Int64.Type}, {"Pack", Int64.Type}, {"BottleVolumeMl", Int64.Type}, {"StateBottleCost", type number}, {"StateBottleRetail", type number}, {"BottlesSold", Int64.Type}, {"SaleDollars", type number}, {"VolumeSoldLiters", type number}, {"VolumeSoldGallons", type number}, {"PartitionKeyYear", Int64.Type}, {"Inserted", type datetime}})
   in
       #"Changed Type"

annotation PBI_ResultType = Table
```

The source is a local.csv file. Let’s change it to OneDrive.

```c
partition 'Fact Sale' = m
 mode: import
 source =
   let
       Source = Csv.Document(Web.Contents("https://e***y.sharepoint.com/personal/m***e_onmicrosoft_com/Documents/iowa_csv/part-00000-e1a14094-35f0-448c-b973-4bcf22858e25-c000.csv"), [Delimiter = ",", Columns = 17, QuoteStyle = QuoteStyle.None]),
       #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
       #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"ID", Int64.Type}, {"InvoiceItemNumber", type text}, {"Date", Int64.Type}, {"StoreID", Int64.Type}, {"CategoryID", Int64.Type}, {"VendorID", Int64.Type}, {"ItemID", Int64.Type}, {"Pack", Int64.Type}, {"BottleVolumeMl", Int64.Type}, {"StateBottleCost", type number}, {"StateBottleRetail", type number}, {"BottlesSold", Int64.Type}, {"SaleDollars", type number}, {"VolumeSoldLiters", type number}, {"VolumeSoldGallons", type number}, {"PartitionKeyYear", Int64.Type}, {"Inserted", type datetime}})
   in
       #"Changed Type"

annotation PBI_ResultType = Table
```

After the change is applied, you get a confirmation.

![](https://miro.medium.com/v2/resize:fit:1234/format:webp/1*LIBrJ5fhtOrRKZNMhK2Tmw.png)

If there is an error, you will get proper information on what is wrong.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3u34A2DyyhEJ5KNNoEZ5bw.png)

If you don’t want to change every separate object in a different TMDL file, you can do it in a model script and handle everything in one place.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*M3VbQbPneW3SHy6LuZUFQA.png)

As a second example, we can add a measure with this code.

```c
createOrReplace

 ref table 'Fact Sale'

  measure Sale = CALCULATE(SUM('Fact Sale'[SaleDollars]))
   lineageTag: f01731e0-13e6-4536-abc7-081a3ce57f2d

   annotation PBI_FormatHint = {"isGeneralNumber":true}
```

Now, we can look at the **second option: Visual Studio Code** or any editor of your choice. In the case of VS Code, we can install a TMDL language extension.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8gi9YWhrTDvJCnJ52TzGJw.png)

Now, we are going to check how the measure is reflected in the project code.

When we open a **Fact Sale.tmdl** file, we can track the measure.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hC_RT3sj79Z3tCHvHbvApg.png)

…and make a change.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Kb1o_8HgQwx9LqG2ig0eJA.png)

Switch over to Power BI Desktop (restart it if the report is open). Then you can confirm that the change has been applied.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2nDP4y8bpN4iER-DL8TEYQ.png)

One key takeaway at the end: The functionality provides a better experience in the case of:

- version control,
- task automation,
- CI/CD,
- etc.

There is one perk I love the most: practically seamless movement of model objects between reports. It’s only a matter of copying a part of the code you are interested in, running it in another report, and it’s done.

If you want to check related topics out, you can look at: [Power BI — update dataset — ALM Toolkit](https://medium.com/p/f3e749f818f6)

and [Power BI assets — seamless PRs](https://medium.com/p/96582595af58)

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Model

**Tags:** Tutorial, Data Model