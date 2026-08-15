---
title: "How to Get Rows and Cells from an Excel Spreadsheet in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-get-rows-and-cells-from-an-excel-spreadsheet-in-power-automate-7031b180734f"
author:
  - "[[Cloudmersive]]"
published: 2024-10-08
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Modern Excel (XLSX) files are designed to be opened, manipulated, and extracted from programmatically through an assortment of applications and programming libraries.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IWT7E-Eyy8jEYpb2R16Oyg.jpeg)

In Power Automate, we can automate tons of useful Excel workflows— and we can do so without writing any code. All we need are the right APIs to interact with portions of our Excel documents in specific ways.

In this walkthrough, we’ll learn how to get rows and cells from an Excel spreadsheet using the **Cloudmersive Document Conversion** connector in Power Automate. The specific API we’ll use will retrieve text values, cell identifiers, cell style indices, and formulas from each cell in each spreadsheet, making it possible for us to easily manipulate that information or transplant it into another Excel document (or other document formats).

We’ll begin by creating an instant cloud flow and selecting the option to trigger it manually. We’ll use this option to control our data in a quick test.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*S5dmdOdA9zKdjR0yTegvaA.png)

Select the option to manually trigger a flow

Next, we’ll add a **Get file content** action to retrieve an Excel XLSX file from our system. I’ll be using the SharePoint version of that action; the file I’m retrieving is a generic employee expense report.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7abM-yw83b9tV4NOZqBPcw.png)

Retrieve an Excel file

Now we’ll add our row & cell retrieval action.

After we add a new action, we’ll type “Cloudmersive” into the connector search bar to bring up a list of Cloudmersive connectors. From this list, we’ll look for the **Document Conversion** connector with the green logo.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RGJUDZJ2xZjDU1S3YSuW8g.png)

Locate the Cloudmersive Document Conversion connector

We’ll click “See more” to view the actions list, and from here, we’ll search for an action called **Get rows and cells from an Excel XLSX spreadsheet, worksheet** (this action may show up twice on the list). We’ll select it once we find it.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*txh73h_oAuYKp1i3EfCZZw.png)

Locate the Get rows and cells from a Excel XLSX spreadsheet, worksheet action

We’ll notice these actions are labeled as “premium.” That means we’ll need a premium Power Automate license to access them. We can, however, make our Cloudmersive API calls for free (up to 800 API calls per month) with a free API key. To get one of those, we can head to the Cloudmersive website and create a free account.

After we create our connection with our API key, we’ll click “Show all” to view the advanced request parameters.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5EK6ZjIGQInJcbizIAv3YQ.png)

Open the advanced request parameters

After we add our Excel file bytes in the **InputFileBytes** parameter, we’ll take a moment review our other parameters.

We’ll notice we have the option to supply a worksheet path or a worksheet name in our request. Providing worksheet information allows us to iterate our **Get rows and cells** action across each worksheet in a multi-worksheet XLSX document.

To retrieve our worksheet name or path dynamically in our flow, we can add another **Cloudmersive Document Conversion** action — called **Get worksheets from a Excel XLSX spreadsheet** — before our **Get rows and cells** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*btKG1wDa6o3ROkcHilGr7A.png)

Use Get worksheets from a Excel XLSX spreadsheet to dynamically retrieve worksheet names and paths

This action retrieves the name and path of each worksheet in an Excel document. In my example flow, I’ve applied the **WorksheetName** value to my **WorksheetToQuery/WorksheetName** parameter (note that this caused Power Automate to wrap my **Get rows and cells** action in an **Apply to each** control).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*uLzajtTufi9hC2PfyyFnLA.png)

Use the WorksheetName (or WorksheetPath ) value in the Get rows and cells request

After we save and test our flow, we’ll find row and cell information for each worksheet in our original document structured as a JSON object array. I’ve included a small snippet of the response object array from Sheet1 of my two-worksheet Excel document.

![](https://miro.medium.com/v2/resize:fit:1384/format:webp/1*W70yXAGCpWvZgffTaY11fw.png)

Test the flow

![](https://miro.medium.com/v2/resize:fit:1176/format:webp/1*PCfY9W09oHhieG2FXuA8-Q.png)

Review the outputs

That’s all there is to it — now we can easily utilize Excel data in a structured way through a simple Power Automate flow.