---
title: "How to Convert CSV to XLSX in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-convert-csv-to-excel-xlsx-in-power-automate-da0e40d9953d"
author:
  - "[[Cloudmersive]]"
published: 2024-09-27
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Converting Comma Separated Value (CSV) files to Excel spreadsheets (XLSX) is as common a task as it is a repetitive one. Technical folks typically prefer working with CSV for its simplicity, widespread compatibility, and overall efficiency, while client-facing business folks tend to appreciate the complex rich text formatting, mathematical capabilities, and data visualization features that XLSX offers.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*CgLAhbUiS73tXXy_MDcSEA.jpeg)

When we’re faced with a task as important and repetitive as converting CSV to XLSX at scale, automation is the best answer. Thankfully, automating CSV to XLSX conversions is extremely easy to pull off — especially in Power Automate.

In this quick walkthrough, we’ll learn how to convert a folder full of CSV files to XLSX using a **Cloudmersive Document Conversion** connector action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DEZhWwCmQ4KokOtfIFbrtg.png)

Folder with four CSV files

We’ll demonstrate this workflow in the context of a manually triggered, instant cloud flow. As shown above, I’ll be using a folder containing four example CSV files.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*n06q6JqLkF4k7wwlwGa4WA.png)

Build a manually triggered, instant cloud flow

We’ll start by bringing CSV files from the target folder into our flow. We’ll use a SharePoint connector action called **List folder**, which returns file identifiers to our flow for each file stored within a target folder. We’ll configure this action by selecting our SharePoint Site Address and File (in this case, “folder”) identifier.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9Lw5EulX1-Z7iMBHM0C-Yw.png)

Start the flow with a List folder action

Next, we’ll add the SharePoint **Get file content** action into our flow. We’ll retrieve our CSV files’ contents using the **Id** (file identifier) value returned by the **List folder** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oVVWg13NqzAe8fk-lanF1Q.png)

Use a Get File Content action to retrieve CSV file content

Once we include the **Id** value in our **Get file content** action, we’ll notice Power Automate automatically wraps our action in an **Apply to each** (i.e., **For each**) control. This ensures file contents are retrieved for each unique file identifier.

Within the **For each** control, we’ll add a new action and search for Cloudmersive connectors. Specifically, we’ll look for the **Cloudmersive Document Conversion** connector.

![](https://miro.medium.com/v2/resize:fit:1212/format:webp/1*OgCm3CWmb5hwQoj9u-YuxA.png)

Search for Cloudmersive connectors

We’ll click “See more” to view the actions list, and from here, we’ll search for an action titled **Convert CSV to Excel XLSX Spreadsheet**.

![](https://miro.medium.com/v2/resize:fit:1216/format:webp/1*vFZhuD-LO7BuJTf7cKyuxA.png)

Search for the Convert CSV to Excel XLSX Spreadsheet action

We’ll need a premium Power Automate license to access actions from this connector, but we can create our connection for free with a free Cloudmersive API key. This allows a limit of 800 API calls per month with zero commitments, and we can get one by creating a free account on the Cloudmersive website.

After we open this action and create a connection with our API key, we’ll add our CSV file contents and file names to our two request parameters.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SZbDBL1V4KYS3t5Eilsjzg.png)

Configure the conversion action with CSV file contents and display names

In our final step, we’ll add a SharePoint **Create file** action to generate our new XLSX documents in a relevant folder.

If we want, we can utilize the original CSV file name by creating a **Slice** function that trims “.csv” extensions from each **DisplayName** value. With the “.csv” extension removed, we can write “.xlsx” extension next to the trimmed version (this avoids creating files with double extensions, e.g. “file.csv.xlsx”).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Hz3c_NBROm6_md8wn8k1hQ.png)

Create XLSX files in a target folder using part of the original CSV file display name

After we save and successfully test our flow, we’ll find Excel versions of our original CSV documents in our target folder.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Amm_HECctQilxjf6Tk1y9w.png)

Successfully running the flow converts each CSV file to XLSX

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*omExGAYm_gkkLztKfl2quA.png)

The new XLSX files become available in the target folder

Just like that, we’ve instantly converted a group of CSV files to Excel worksheets.