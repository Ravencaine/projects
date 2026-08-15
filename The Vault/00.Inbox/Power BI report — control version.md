---
title: "Power BI report — control version"
source: "https://medium.com/@michalmolka/power-bi-report-control-version-b71a45f16ca6"
author:
  - "[[Michal Molka]]"
published: 2026-01-01
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8C_7jpyoeeaf63QiM7UIIA.png)

From the begining of Power BI’s existence. Power BI reports were saved as **.pbix** files. The.PBIX file is nothing more than a binary file. When it comes to control version, binary files are less manageable compared to text files. Here are a few examples that come to mind:

- larger reports take up a lot of space in the repository (especially if you save the model’s data in the file),
- tracking changes is more difficult,
- CI/CD is harder to implement,
- edition outside of Power BI Desktop is problematic, to put it gently.

Probably, I could find a few more examples, but I think these are the most important. Some salvation can be a **.pbit** file, but it has its drawbacks as well. Without further ado, let’s get to the point.

Currently, Microsoft has released a new way of saving reports as a Power BI Project (**.pbip), w** hich saves the report as a series of text files.

Let’s do an exercise. I’ve created a simple report that contains three visualizations, one measure, and filtered out a few years on a slicer and a filter pane. Then, I saved it as a **.pbip** project.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2LixwP_oKMb_-bwE2RrhNw.png)

As all the saved files are in a textual format, we can use a text editor.

The report is decomposed into a set of files.

![](https://miro.medium.com/v2/resize:fit:1286/format:webp/1*Zg8G_Jg170JbNlOsvwirfA.png)

Let’s start with the model. I connected the report to an MS Fabric Data Warehouse semantic model. When we go to the **definition.pbir** file, we can find the connection properties.

```c
{
  "version": "4.0",
  "datasetReference": {
    "byPath": null,
    "byConnection": {
      "connectionString": "Data Source=powerbi://api.powerbi.com/v1.0/myorg/Iowa_Sales;Initial Catalog=eightfive_warehouse;Access Mode=readonly;Integrated Security=ClaimsToken",
      "pbiServiceModelId": null,
      "pbiModelVirtualServerName": "sobe_wowvirtualserver",
      "pbiModelDatabaseName": "e6bb1319-08bd-4304-8a3b-a0ad87d9729f",
      "name": "EntityDataSource",
      "connectionType": "pbiServiceXmlaStyleLive"
    }
  }
}
```

More interesting is the **report.json** file, where we can find all the visualizations, filters, etc.

Let’s change a few things and check whether they are reflected in Power BI Desktop.

Here is the entire file before changes.

```c
{
  "config": "{\"version\":\"5.59\",\"themeCollection\":{\"baseTheme\":{\"name\":\"CY24SU10\",\"version\":\"5.60\",\"type\":2}},\"activeSectionIndex\":0,\"modelExtensions\":[{\"name\":\"extension\",\"entities\":[{\"name\":\"iowa_sale\",\"extends\":\"iowa_sale\",\"measures\":[{\"name\":\"SumOfSales\",\"dataType\":3,\"expression\":\"CALCULATE(SUM(iowa_sale[SaleDollars]))\",\"errorMessage\":null,\"hidden\":false,\"formulaOverride\":null,\"formatInformation\":{\"formatString\":\"0\",\"format\":\"NumberDecimal\",\"accuracy\":0,\"thousandSeparator\":false,\"currencyFormat\":null,\"dateTimeCustomFormat\":null}}]}]}],\"defaultDrillFilterOtherVisuals\":true,\"linguisticSchemaSyncVersion\":0,\"settings\":{\"useNewFilterPaneExperience\":true,\"allowChangeFilterTypes\":true,\"useStylableVisualContainerHeader\":true,\"queryLimitOption\":6,\"exportDataMode\":1,\"useDefaultAggregateDisplayName\":true,\"useEnhancedTooltips\":true},\"objects\":{\"section\":[{\"properties\":{\"verticalAlignment\":{\"expr\":{\"Literal\":{\"Value\":\"'Top'\"}}}}}]}}",
  "layoutOptimization": 0,
  "resourcePackages": [
    {
      "resourcePackage": {
        "disabled": false,
        "items": [
          {
            "name": "CY24SU10",
            "path": "BaseThemes/CY24SU10.json",
            "type": 202
          }
        ],
        "name": "SharedResources",
        "type": 2
      }
    }
  ],
  "sections": [
    {
      "config": "{\"relationships\":[{\"source\":\"a0da5558d754ac5777e0\",\"target\":\"3a9f33a4245bce257e9e\",\"type\":3}]}",
      "displayName": "Page 1",
      "displayOption": 1,
      "filters": "[{\"name\":\"8a2958150a92ff3a4de0\",\"expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Entity\":\"iowa_date\"}},\"Property\":\"CalendarYear\"}},\"filter\":{\"Version\":2,\"From\":[{\"Name\":\"i\",\"Entity\":\"iowa_date\",\"Type\":0}],\"Where\":[{\"Condition\":{\"Not\":{\"Expression\":{\"In\":{\"Expressions\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i\"}},\"Property\":\"CalendarYear\"}}],\"Values\":[[{\"Literal\":{\"Value\":\"null\"}}],[{\"Literal\":{\"Value\":\"2012L\"}}],[{\"Literal\":{\"Value\":\"2013L\"}}],[{\"Literal\":{\"Value\":\"2014L\"}}]]}}}}}]},\"type\":\"Categorical\",\"howCreated\":1,\"objects\":{\"general\":[{\"properties\":{\"isInvertedSelectionMode\":{\"expr\":{\"Literal\":{\"Value\":\"true\"}}}}}]}}]",
      "height": 720.00,
      "name": "b3eb616fd263265c2422",
      "visualContainers": [
        {
          "config": "{\"name\":\"3a9f33a4245bce257e9e\",\"layouts\":[{\"id\":0,\"position\":{\"x\":10.003500573931307,\"y\":0,\"z\":0,\"width\":240.08401377435135,\"height\":440.1540252529775,\"tabOrder\":0}}],\"singleVisual\":{\"visualType\":\"pivotTable\",\"projections\":{\"Rows\":[{\"queryRef\":\"iowa_store.County\",\"active\":true}],\"Values\":[{\"queryRef\":\"iowa_sale.SumOfSales\"}]},\"prototypeQuery\":{\"Version\":2,\"From\":[{\"Name\":\"i1\",\"Entity\":\"iowa_store\",\"Type\":0},{\"Name\":\"i\",\"Entity\":\"iowa_sale\",\"Schema\":\"extension\",\"Type\":0}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i1\"}},\"Property\":\"County\"},\"Name\":\"iowa_store.County\",\"NativeReferenceName\":\"County\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i\"}},\"Property\":\"SumOfSales\"},\"Name\":\"iowa_sale.SumOfSales\",\"NativeReferenceName\":\"SumOfSales\"}]},\"drillFilterOtherVisuals\":true}}",
          "filters": "[{\"name\":\"cfb5af870a9e236650b4\",\"expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Entity\":\"iowa_store\"}},\"Property\":\"County\"}},\"filter\":{\"Version\":2,\"From\":[{\"Name\":\"i\",\"Entity\":\"iowa_store\",\"Type\":0}],\"Where\":[{\"Condition\":{\"Not\":{\"Expression\":{\"In\":{\"Expressions\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i\"}},\"Property\":\"County\"}}],\"Values\":[[{\"Literal\":{\"Value\":\"null\"}}]]}}}}}]},\"type\":\"Categorical\",\"howCreated\":0,\"objects\":{\"general\":[{\"properties\":{\"isInvertedSelectionMode\":{\"expr\":{\"Literal\":{\"Value\":\"true\"}}}}}]},\"isHiddenInViewMode\":false,\"isLockedInViewMode\":true}]",
          "height": 440.15,
          "width": 240.08,
          "x": 10.00,
          "y": 0.00,
          "z": 0.00
        },
        {
          "config": "{\"name\":\"9380674a354113dca2ee\",\"layouts\":[{\"id\":0,\"position\":{\"x\":250.08751434828267,\"y\":98.03430562452681,\"z\":1000,\"width\":657.5634377264179,\"height\":297.43741706489084,\"tabOrder\":1000}}],\"singleVisual\":{\"visualType\":\"clusteredColumnChart\",\"projections\":{\"Category\":[{\"queryRef\":\"iowa_date.CalendarYear\",\"active\":true}],\"Y\":[{\"queryRef\":\"iowa_sale.SumOfSales\"}]},\"prototypeQuery\":{\"Version\":2,\"From\":[{\"Name\":\"i1\",\"Entity\":\"iowa_date\",\"Type\":0},{\"Name\":\"i\",\"Entity\":\"iowa_sale\",\"Schema\":\"extension\",\"Type\":0}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i1\"}},\"Property\":\"CalendarYear\"},\"Name\":\"iowa_date.CalendarYear\",\"NativeReferenceName\":\"CalendarYear\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i\"}},\"Property\":\"SumOfSales\"},\"Name\":\"iowa_sale.SumOfSales\",\"NativeReferenceName\":\"SumOfSales\"}],\"OrderBy\":[{\"Direction\":2,\"Expression\":{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i\"}},\"Property\":\"SumOfSales\"}}}]},\"drillFilterOtherVisuals\":true,\"hasDefaultSort\":true,\"objects\":{\"labels\":[{\"properties\":{\"show\":{\"expr\":{\"Literal\":{\"Value\":\"true\"}}},\"labelOrientation\":{\"expr\":{\"Literal\":{\"Value\":\"0D\"}}}}}]}}}",
          "filters": "[]",
          "height": 297.44,
          "width": 657.56,
          "x": 250.09,
          "y": 98.03,
          "z": 1000.00
        },
        {
          "config": "{\"name\":\"a0da5558d754ac5777e0\",\"layouts\":[{\"id\":0,\"position\":{\"x\":1129.0617647777135,\"y\":0,\"z\":1001,\"width\":150.7194086472317,\"height\":422.81462425816324,\"tabOrder\":1001}}],\"singleVisual\":{\"visualType\":\"slicer\",\"projections\":{\"Values\":[{\"queryRef\":\"iowa_date.CalendarYear\",\"active\":true}]},\"prototypeQuery\":{\"Version\":2,\"From\":[{\"Name\":\"i\",\"Entity\":\"iowa_date\",\"Type\":0}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i\"}},\"Property\":\"CalendarYear\"},\"Name\":\"iowa_date.CalendarYear\",\"NativeReferenceName\":\"CalendarYear\"}]},\"drillFilterOtherVisuals\":true,\"objects\":{\"data\":[{\"properties\":{\"mode\":{\"expr\":{\"Literal\":{\"Value\":\"'Basic'\"}}}}}],\"general\":[{\"properties\":{\"orientation\":{\"expr\":{\"Literal\":{\"Value\":\"0D\"}}},\"filter\":{\"filter\":{\"Version\":2,\"From\":[{\"Name\":\"i\",\"Entity\":\"iowa_date\",\"Type\":0}],\"Where\":[{\"Condition\":{\"In\":{\"Expressions\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"i\"}},\"Property\":\"CalendarYear\"}}],\"Values\":[[{\"Literal\":{\"Value\":\"2015L\"}}],[{\"Literal\":{\"Value\":\"2016L\"}}],[{\"Literal\":{\"Value\":\"2017L\"}}]]}}}]}}}}]}}}",
          "filters": "[]",
          "height": 422.81,
          "width": 150.72,
          "x": 1129.06,
          "y": 0.00,
          "z": 1001.00
        }
      ],
      "width": 1280.00
    }
  ]
}
```

Change the tab name from ‘Page 1’ to ‘Iowa\_report’.

```c
"displayName": "Page 1"
--->
"displayName": "Iowa_report"
```

Measure: change SUM to AVERAGE.

```c
CALCULATE(SUM(iowa_sale[SaleDollars]))
--->
CALCULATE(AVERAGE(iowa_sale[SaleDollars]))
```

Change the filtered-out values for a Date slicer from the Filters pane.

```c
[{\"Literal\":{\"Value\":\"2013L\"}}]
--->
[{\"Literal\":{\"Value\":\"2019L\"}}]
```

Same thing, but directly on the slicer.

```c
[{\"Literal\":{\"Value\":\"2017L\"}}]
--->
[{\"Literal\":{\"Value\":\"2020L\"}}]
```

Label orientation for a bar chart.

```c
\"labelOrientation\":{\"expr\":{\"Literal\":{\"Value\":\"0D\"}}}
--->
\"labelOrientation\":{\"expr\":{\"Literal\":{\"Value\":\"1D\"}}}
```

According to expectations, all the changes are reflected in the report.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Cvv9rou9i4TF95V5LQoADg.png)

If you want to check related topics out, you can look at: [Power BI — TMDL — Tabular Model Definition Language](https://medium.com/p/2cca06e87921)

and [Power BI — update dataset — ALM Toolkit](https://michalmolka.medium.com/power-bi-update-dataset-alm-toolkit-f3e749f818f6)

and [Power BI assets — seamless PRs](https://medium.com/p/96582595af58)