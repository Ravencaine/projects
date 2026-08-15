---
title: "How to Merge Excel Files in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-merge-excel-files-in-power-automate-049430fc78b7"
author:
  - "[[Cloudmersive]]"
published: 2024-09-30
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Manually assembling multi-worksheet Excel files from existing Excel documents tends to be a time-consuming and frustrating process.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eH5eqD0a_pJiVsbo9mAbIQ.jpeg)

Thankfully for us, it’s easy enough to automate this process without writing any code. We can simply build a quick flow in Power Automate that grabs Excel files from different folders in our system and combines them using a **Cloudmersive Document Conversion** connector action.

### Walkthrough

Below, we’ll walk through the process of setting up a manually triggered, instant cloud flow that combines Excel documents from three different folders in our system.

We’ll begin by selecting the **Instant cloud flow** option from the **Create** page and checking the option to trigger it manually.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9BAT7sAX7NL3qBkVph7wHg.png)

Create a manually triggered, instant cloud flow

On our flow diagram page, we’ll add one **Get file content** action for each Excel file we’re merging in this workflow. In my example flow, I’ve grabbed one file from my OneDrive file system and two files from my SharePoint team site.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*dd7HnnSZMIoeiPXV2MtgVQ.png)

Add multiple Get file content actions to retrieve multiple Excel XLSX files

Next, we’ll add a new action and search for Cloudmersive connectors. We’ll find several Cloudmersive connectors in our results; we’re looking for the **Cloudmersive Document Conversion** connector with the green logo.

![](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*2j1DrHjPsBhglcnQzHOVNw.png)

Search for Cloudmersive connectors

From here, we’ll click “See more” to view the actions list, and we’ll then search for an action called **Merge Multiple Excel XLSX** together.

![](https://miro.medium.com/v2/resize:fit:1214/format:webp/1*0l3BtGa4ECOVMOPfxXBAPA.png)

Find the Merge Multiple Excel XLSX action on the Cloudmersive Document Conversion connector actions list

After we select this action, we’ll be prompted to configure our Cloudmersive connection. We’ll need a premium Power Automate license to use Cloudmersive connectors in Power Automate, but we can create our API connection for free with a free Cloudmersive API key (this allows a limit of 800 API calls per month with no additional commitments).

We’ll now fill out our **Merge Multiple Excel XLSX** request parameters. We’ll fill the first pair of “input file” and “file name” parameters with dynamic content from our first two **Get file content** actions.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8a4c35P75xC2pZt0ASgN-w.png)

Configure basic request parameters for Excel merge

To include our third file, we’ll click “Show all” to view the advanced parameters. Here, we’ll find additional inputs for up to 10 more Excel files. We’ll now enter dynamic content from our third **Get file content** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hGSZrq7ZHZ7KyFVPd3OZcQ.png)

Configure advanced parameters for Excel merge

The **Merge Multiple Excel XLSX** action assembles the new Excel document in the exact order we entered our files. If our files contain multiple worksheets, those worksheets will follow the same order.

We’ll now add a **Create file** action to save our merged Excel document somewhere in our system. The dynamic content value **OutputContent** contains our new Excel document file bytes.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jfFR1Z2AzR9Y6W5QYZY_KA.png)

Create the merged Excel file using a Create file action

After we save and test our flow, we’ll find the merged Excel document in the folder we specified.

![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*m7RllsLpAVhKsQbBtRYZxg.png)

Save and test the flow

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*j8FMXJa6nQKHRg8fV483XQ.png)

Find the merged Excel document in the specified folder

And just like that, we’re all done!

In this walkthrough, we’ve successfully merged three Excel documents from different folders into one multi-worksheet Excel document — all without writing any code.