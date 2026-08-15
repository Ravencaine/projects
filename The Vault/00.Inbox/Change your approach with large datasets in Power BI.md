---
title: "Change your approach with large datasets in Power BI"
source: "https://medium.com/data-science/change-your-approach-with-large-datasets-in-power-bi-ca488a5b1066"
author:
  - "[[Salvatore Cagliari]]"
published: 2021-10-05
created: 2026-08-12
description: "You can have problems when you try to load huge datasets with hundreds of millions of rows in Power BI Desktop because of the limits of your RAM. Let’s explore Dataflows to make this possible."
Processed: "Unprocessed"
---
## You can have problems when you try to load huge datasets with hundreds of millions of rows in Power BI Desktop because of the limits of your RAM. Let’s explore Dataflows to make this possible.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*H_yCaQk5EgHr2-h_)

Photo by Brad Starkey on Unsplash

## Starting Point

One of my clients has a table with 126 million rows and growing.  
His problem is how to load this data in Power BI Desktop with only 8 GB of RAM.

Moreover, he has no control over the data source. This lack of control means that he cannot create a database view with a Filter, to reduce the Dataset for the initial load into Power BI Desktop.

This challenge is problematic, to say the least. Maybe you have already experienced this in the past.

I had the idea to use Power BI Dataflows to solve this.

For this, I used my enlarged Contoso dataset:

![Original Dataset (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*40bALIuDuWOcm7AdclJndw.png)

Figure 1 — Original Dataset (Picture by the Author)

First, I will explain how the solution will look.

Then I show you the steps to set up the solution.

## Solution

The following diagram shows you the architecture of the solution:

![Architecture of the solution (Diagram by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lfb8tKhirnmCREsxt2GGhA.png)

Figure 2 — Architecture of the solution (Diagram by the Author)

As you can see, I’ve set up two data loads:

1. A load of the fact table directly in Power BI Service with Dataflow
2. A load of all Dimension tables into Power BI Desktop

The target of this is to avoid a load of millions of rows into Power BI Desktop.

I use a Preview Feature (Preview as the time of this writing) in Power BI Desktop, which allows me to combine a Live connection to a Power BI Dataset with other (imported) tables from another data source.

## Build the solution

The first step is to analyse the source data and find out how to filter the data.

The target is to reduce the amount of data to a minimum, as I have to load the data into Power BI Desktop once.

In my case, I can reduce the data in my two fact tables to load data for only one year in an easy way:

![Row-count of one year of data per table (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ShqMG9SAsU6FH12rB4baFA.png)

Figure 3 — Row-count of one year of data per table (Picture by the Author)

Next, I create a Dataflow on the Power BI Service.  
In my case, I use a Premium Per User Workspace to be able to use the [Large Dataset storage Format](https://docs.microsoft.com/en-us/power-bi/admin/service-premium-large-models):

![Create a new Dataflow in the Power BI Service (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*j5UStZjSy1iKNScWDJ-19A.png)

Figure 4 — Create a new Dataflow in the Power BI Service (Picture by the Author)

The next step is to select the action for the Dataflow:

![Select Action for the new Dataflow (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ylNpHu9Qx8gRW-5pgB5zig.png)

Figure 5 — Select Action for the new Dataflow (Picture by the Author)

In my case, I want to add new tables.

To add the new tables, I need to configure the source server and database:

![Datasource for new tables (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1228/format:webp/1*4Q7_usHi4aoz2xNpNor2-A.png)

Figure 6 — Datasource for new tables (Picture by the Author)

I installed the on-premises data gateway on my Azure VM. To store my sample database, I have SQL Server installed on the same VM.  
First, I have to configure the server and the database in the Gateway. Second, I have to select the Gateway in the Data source connection.

You can leave the Username and the Password as it is when you want to use the credentials stored in the Gateway connection, or you can enter other credentials for the data source.

Now you can use an interface, which looks very similar to the Power Query Editor in Power BI to select the needed tables and to add transformations to the data if you wish to do:

![Query Editor in the Dataflow (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Wkf9dyAdbF99G90Oh5zFSQ.png)

Figure 7 — Query Editor in the Dataflow (Picture by the Author)

I can add a Filter step to filter the data as described above:

![Filter the data in Power Query (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1176/format:webp/1*oZVelU_D8EUlxRB3jo6RLQ.png)

Figure 8 — Filter the data in Power Query (Picture by the Author)

This possibility is the beauty of Dataflow: I can add filters, like in Power Query, without downloading the data to Power BI Desktop. The data stays in the cloud.

As soon as you press Save & Close, you can start a data load. This process takes very little time, as I load only a small subset of the data.

Now, the Dataset is visible in my Workspace:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zBYzHWoi6I3pwHuurfhxxw.png)

Figure 9 — Dataflow in my Workspace (Picture by the Author)

The Prefix DF\_ stand for Dataflow, and I need a unique name, as I will create a dataset with the same name. But I cannot have two objects with the same name.

Unfortunately, it’s not possible to create a dataset Online.

You can find an entry on idea.powerbi.com about this issue: Data flow-based [Datasets in service](https://ideas.powerbi.com/ideas/idea/?ideaid=f25532c7-fb4d-49d2-999c-1b0d9b739e95)

For this reason, I have to create a dataset in Power BI Desktop.

I can select Power BI Dataflow as the source:

![Dataflow as Source in Power BI Desktop (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1308/format:webp/1*D1keCcGPjaH3Jjgl0ZkDZg.png)

Figure 10 — Dataflow as Source in Power BI Desktop (Picture by the Author)

I will add both tables to the Dataset and publish the Report to the Service as ContosoRetailDW\_Big\_BigFacts.

But this approach has a glitch, as I discovered at the end of the build. Please read to the end, as I left it to show one drawback of this specific approach.

The next step is to edit the Dataflow to remove the filter on both tables and refresh the data. I need to refresh the data in the Dataflow and the Power BI Dataset. This means that you have to store the same data twice.

At the moment, I don’t know a solution to this issue.

But you can configure Incremental Refresh to your Dataflow and your Dataset to reduce the refresh times: [Incremental refresh for datasets in Power BI — Power BI | Microsoft Docs](https://docs.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview)

To create the final Power BI report, I have to add the Dataset with the two Fact tables to the new Power BI report:

![Get Power BI Dataset from the cloud (Picture by the Author) — with the wrong name](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9pmG3W-iyfCDkFXqJlKm6A.png)

Figure 11 — Get Power BI Dataset from the cloud (Picture by the Author) — with the wrong name

In the Status bar at the bottom right, I can see that I’m using a live connection:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NRjKlo6qutwUXLW5mglheg.png)

Figure 12 — Status bar with the Live connection (Picture by the Author)

I need to enable a Preview feature for the next step:

![Enable Direct Query for PBI Datasets (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LWs-cEMyj88lgJt64n6few.png)

Figure 13 — Enable Direct Query for PBI Datasets (Picture by the Author)

Click on the “Learn more” link to go to the Documentation page. There you can find valuable information about this feature.

After enabling this feature and restart Power BI Desktop, the Status bar looks like the picture above.

As soon as I click on the Transform Data Button, I receive a message that the Live Connection will be changed to a Direct Query connection. This change allows me to add additional tables to the data model.

Now, the Status bar looks like that:

![Data Model in Direct Query mode (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Vrvpkb6198Cejiiv5TaIUw.png)

Figure 14 — Data Model in Direct Query mode (Picture by the Author)

The next step is to add all needed Dimension tables to the Data Model and all Relationships between the tables.

As soon as I tried to connect the second Fact table to the Date table, I got the following Error message:

![Error message for multiple Relationships (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1252/format:webp/1*bnLF7bi1awRTPivxyqhyMg.png)

Figure 15 — Error message for multiple Relationships (Picture by the Author)

It seems that I had to create two datasets: One per fact table  
Then add both datasets to the Report in Direct Query mode. Anyway, I would still be able to use the one Dataflow to prepare my data.

This way, my model is not perfect, but I can use it as a Prototype to show it to my Clients.

This issue is the glitch that I mentioned when I loaded both Fact tables into one Dataset.

## Conclusion

The most significant effect of this approach is visible when you start to compare the two Power BI files. One with the entire Dataset and the other with the Composite model, as described in this Article:

![Size comparison between full Dataset and the Composite model (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7daXSI0C8lAnUQbq9Z5qTw.png)

Figure 16 — Size comparison between full Dataset and the Composite model (Picture by the Author)

The size of the composite model is a little over 1/1000th of the original size.

And it takes only a few seconds to open this model. The data refresh of the Dimension tables takes a very short time as well.

The drawback is that it takes over one hour to perform a full load for the Dataflow and the Dataset with the Fact tables.

But you need to understand all possible implications when working with composite Data models.

SQLBI has published a video on YouTube on this topic:

The combination of Dataflows and Composite models opens an entirely new world for managing large Datasets. And you can reuse the data from the Dataflow or the Dataset multiple times in different Reports without the need to reload the data numerous times.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*rnulLqsCUKWkdD3K)

Photo by S Migaj on Unsplash

I hope that you can get new ideas from my approach.

If you appreciate my work, feel free to support me through

## [Salvatore Cagliari](https://buymeacoffee.com/salvatorecagliari?source=post_page-----ca488a5b1066---------------------------------------)

### I write technical articles about Data Analysis and Reporting with Power BI. In addition I love building and flying RC…

buymeacoffee.com

Or scan this QR Code:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*btH95UXO7gboS30eZMk6ug.png)

Any support is greatly appreciated.

Thank you.