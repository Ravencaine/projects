---
title: "Power BI/Power Query: relative folder path for source files"
source: "https://medium.com/inteliaengineering/power-bi-power-query-relative-folder-path-for-source-files-e1b17befe333"
author:
  - "[[Hila Galapo]]"
published: 2026-07-17
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
This article is meant for anyone who had to change the folder name/file location of more than one table source in a Power BI model, when the model is based on files, not on a database.

### A disclaimer:

The code pattern below isn’t my invention. I’ve found it in a model I was asked to maintain, and I’ve found this so useful that I decided to share this code pattern with the rest of the universe.

### A disclaimer (2):

When I wanted to re-create the case & solution for this article, I’ve found an old project on my laptop which I started working on before I joined [intelia](https://www.intelia.ai/). The data source is from [Kaggle](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset), and the spelling mistake in the folder name was there in the first place, it wasn’t a deliberate mistake for educational purposes.

Now, let’s get started.

## The Problem

I created a Power BI model consisting of several files sitting in a folder, and now I need to change the folder’s name. This could be from all sort of reasons; in this case, there’s a spelling mistake in the name of the folder under which the files are residing:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*y45FpxxbO98wrf40_IQWeQ.png)

Image 1: A spelling mistake in the name of the folder, Musitc should be Music

The model is already created, and all the files are pointing to the folder with the spelling mistake:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2Z2syhpU_VJf2-IIPcLlKg.png)

Image 2: all the files are uploaded with a folder name that now has to be changed.

Now I need to go into 5 different data sources to change the full filename, otherwise, if I fix the folder’s name, the model wouldn’t refresh properly. Also note that the filename appears with its absolute path on 3 different rows; changing the “Source” line by itself wouldn’t solve the problem.

Power BI/Power Query cannot accept a *relative* network reference. I’ve made a spelling mistake and now I need to fix it.

So, how do I make the code point to a relative or root folder path, to minimize re-writing the code?

```c
let
  Source = path -- ????
```

## The Solution

So, we wish to point the Source to a root folder location.

I’ll create a new Blank Query:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*NAvza6UjHGKsd_mMBbT5xg.png)

For the time being, I’ll keep the name of the folder misspelt. I renamed the data source “Primary Dataset”, right click on “Advanced Properties” and wrote the following code:

```c
let
    Source = Folder.Files ("C:\Users\Test\Documents\Hila\Musitc Dataset\data")
in
    Source
```

This source shows all the files in the folder location:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*dTwr-4LWj-0ofR9ArQqdsw.png)

Since there’s no need for this this data to be loaded into the model, right-click on this source query and un-tick Enable Load:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*qGwvr3ysOiECFZm7tgrpXA.png)

Once the dataset Load is not Enabled its name is in Italics

Changing the source to the new source at this stage isn’t good enough — the exact filename populates in the consequent stages. Some more manipulation is required for this new data source to become the Source Query.

I Split the “Folder Path” Column by Delimiter (pick custom delimiter and specified \`\\\` ) and now I have all the folder path manipulated and the filename, type and content populated in the different columns:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*s6FefJTNZS7nGUOOx4P9ng.png)

After splitting “Folder File Name” by delimiter

Each data source points to a specific file, so filter by that filename (line 3 below), and use that new Filtered Row as a source to the content (line 4), so the code looks like this:

```c
let
    Source = #"Primary Dataset",
    #"Filtered Rows" = Table.SelectRows(Source, each ([Name] = "data.csv")),
    Content = #"Filtered Rows"{0}[Content],
    #"Imported CSV" = Csv.Document(Content,[Delimiter=",", Columns=19, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"valence", type number}, {"year", Int64.Type}, {"acousticness", type number}, {"artists", type text}, {"danceability", type number}, {"duration_ms", Int64.Type}, {"energy", type number}, {"explicit", Int64.Type}, {"id", type text}, {"instrumentalness", type number}, {"key", Int64.Type}, {"liveness", type number}, {"loudness", type number}, {"mode", Int64.Type}, {"name", type text}, {"popularity", Int64.Type}, {"release_date", type text}, {"speechiness", type number}, {"tempo", type number}})
in
    #"Changed Type"
```

As you can see, the full file path isn’t presented in this code, only the relevant filename.

**Important!**

- filter for the exact filename, not just the first one. This way, if new files are added, the table source doesn’t change.
- Note how the Power Query (in this instance) is longer. PQ changes all the time, so play around to check which version you need and note which steps are being referred to.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*81VTNbvcs7c0DMrCiKvDUw.png)

First step, Source, now points to #”Primary Dataset”

Once all connection strings are updated, hit “Close and Apply”, and the model is uploaded.

Now, I can change the folder name without repercussion:

![](https://miro.medium.com/v2/resize:fit:1238/format:webp/1*g2k9A3DdxltEkrj62UH_jw.png)

Correct folder name

Hitting Refresh would obviously fail, since I didn’t update the Source line (the foler name) in the Primary Dataset source:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*dvkVe0wpRapm5Otk4biJfw.png)

Just fix the data source with the correct folder name:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*U4c980wjoI3CHWK1gRannQ.png)

And then hit Close & Apply, and Ta-Da!

All the files are pointing to the correct folder, and the change had to be done once, not in several points.

### A variant: Reading all Files in a Folder

If you want to read all the files from a specific folder, assuming they all have the same structure:

I’ve placed two files identical in their structure (I took data\_by\_year and halved it), and placed it in a specific folder:

![](https://miro.medium.com/v2/resize:fit:1172/format:webp/1*i7AZ0p-jQV-gj1soZRH2BA.png)

A new folder with the two files

Now, the Primary Dataset table has values populated in the relevant “Folder Path” column:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9TsLztLhmU4XawaEnbCTeQ.png)

The table displaying the content of the folder is refreshed with the new folder and its data files

Filter for the folder, and pick Combine file (the arrows next to the “Content” column):

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*0RXkml3MsDUk-FM2RUpZCQ.png)

And then combine the files:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0HkZq2p3bDKRepAu4sVzLg.png)

And this is what the M code looks like:

```c
et
    Source = #"Primary Dataset",
    #"Filtered Rows" = Table.SelectRows(Source, each ([Folder Path.9] = "Year Data")),
    #"Filtered Hidden Files1" = Table.SelectRows(#"Filtered Rows", each [Attributes]?[Hidden]? <> true),
    #"Invoke Custom Function1" = Table.AddColumn(#"Filtered Hidden Files1", "Transform File", each #"Transform File"([Content])),
    #"Removed Other Columns1" = Table.SelectColumns(#"Invoke Custom Function1", {"Transform File"}),
    #"Expanded Table Column1" = Table.ExpandTableColumn(#"Removed Other Columns1", "Transform File", Table.ColumnNames(#"Transform File"(#"Sample File"))),
    #"Changed Type" = Table.TransformColumnTypes(#"Expanded Table Column1",{{"mode", Int64.Type}, {"year", Int64.Type}, {"acousticness", type number}, {"danceability", type number}, {"duration_ms", type number}, {"energy", type number}, {"instrumentalness", type number}, {"liveness", type number}, {"loudness", type number}, {"speechiness", type number}, {"tempo", type number}, {"valence", type number}, {"popularity", type number}, {"key", Int64.Type}})
in
    #"Changed Type"
```

## Best approach to implement this method

For a model consisting of files, not a database, use the following approach:

1. Instead of hitting the “upload data” or “import data” and linking directly to that file location, pick the “Blank Query” data source and point to the specific folder. This folder will be your Primary Dataset.
2. For every file that you wish to upload, first, create a reference to that Primary Dataset. Filter for filename and read the content of the file. Alternatively, if you need to read files in a specific sub-folder, filter using the relevant folder path(s) and combine the data.
3. Once done, changing the root folder name is easier, since the change is done once, in the Primary Dataset “Source” line.
4. If you have a database as a source, then changing the source is well-documented, for example in [this article](https://radacad.com/change-the-source-of-power-bi-datasets-dynamically-using-power-query-parameters/).

## In Summary

Power BI/Power Query can accept [many data source](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-sources?tabs=new-experience). They could be stored in a database, or they could be some csv files in a local/shared drive, SharePoint location or a cloud location. However, Power Query engine cannot accept a *relative* network reference.

In many programming languages, you could run a read file from a reference location or combine different roots of file paths. In Power BI this can’t be done. There had been requests in the past to enable a relative path, for example in [here](https://community.fabric.microsoft.com/t5/Fabric-Ideas/Support-relative-path-to-excel-csv-sources/idi-p/4441605) (from 2015, when Power BI was born), so the problem isn’t new.

This solution requires approaching creating a model from files in a different manner: first, define the root folder in which your files will reside. Create a connection to that folder and expose the complete paths to the files in it. Then, import files using this super-connection as a source (that’s your relative path) and the sub-folders and filename as parameters to be filtered. This way, you can bypass the fact that

> Power BI cannot define a root folder for its source files.

Now, upgrading and changing folder sources becomes much easier.