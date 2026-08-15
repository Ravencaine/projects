---
title: "How to Process Excel Data as Plain Text in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-process-excel-data-as-plain-text-in-power-automate-d49ae6d51c9c"
author:
  - "[[Cloudmersive]]"
published: 2025-02-03
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fqhPh4wjR8PrTxfs697yVA.jpeg)

In Power Automate, we can read and utilize Excel data dynamically in a number of different ways.

We can, for example, convert Excel to a lightweight data type —like JSON or CSV — and create a schema for our outputs.

To involve even *less* processing, however, we can also convert our Excel data directly to plain text and subsequently divide that text into separate lines.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Tnl-Cw2PPA6mhTdoZMKs3w.png)

### Process Excel Data as Plain Text

Plain text data can be extremely useful in certain workflows thanks to its simplicity and flexibility. Imagine, for example, we have an “Annual Expenses” report like the below example:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Ly-GNuyChR8dawwlZTQgGA.png)

And from this report, we’d only like to return the expense value for a specific year (e.g., 2022):

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*YjHwjGajCil9dyl9EYQDqA.png)

After converting our spreadsheet to text & dividing that text into independent lines, we could find the string “2022” and return all data from only that line.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-YhAxbCuvqYYkPvYZp_kbA.png)

We could also find the string “780,000” and return the exact same line of text. Our result won’t be structured in a particularly pretty way, but it’ll get the job done perfectly.

### Example Flow

We’ll walk through a quick example **Instant cloud flow** that **1)** converts the above Excel spreadsheet data to text, **2)** splits that text into separate lines, **3)** composes (beautifies) the text, and **4)** returns **Total Expenses ($)** data from only one specific year.

We’ll use a pair of **Cloudmersive Document Conversion** connector actions to handle our Excel conversion and text-splitting steps respectively.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Jotwcad7A95AScr-ZVa-Lg.png)

### Get an example Excel file

We’ll start by using a **Get file content** action to retrieve our example Excel file.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JN50wc7vPiPWsfkqKsMT4Q.png)

### Find Cloudmersive Connectors

Next, we’ll add a new action and search for Cloudmersive connectors. We’ll find the **Cloudmersive Document Conversion** connector on the resulting list with a green logo.

![](https://miro.medium.com/v2/resize:fit:1260/format:webp/1*LFHTS-Jm1B8uMZGmaXXs0g.png)

### Locate the Excel to Text conversion action

After we click “See more” to view the entire actions list, we’ll locate an action titled **Convert Excel XLSX Spreadsheet to Text (txt)**.

![](https://miro.medium.com/v2/resize:fit:1254/format:webp/1*RdbB5JgTl6QRPDRNgbJSQQ.png)

### Create & authorize a Cloudmersive Document Conversion connection

We’ll select this action, and we’ll create our **Document Conversion** connection directly after. We only need to do this once for both actions in this flow. We’ll authorize our requests using a free Cloudmersive API key, which we can get by registering a free account on the Cloudmersive website (free API keys allow a limit of 800 API calls per month).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7AgToIpd2CV9tc5TziMXJA.png)

### Configure the Excel to Text request

We’ll then pass Excel file bytes and a random file name (e.g., “file.xlsx”) to each of our two request parameters. The real file name doesn’t matter here because we’re only using it to label our API request.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*caXW_99JrUV7U-bA3Lo8-Q.png)

### Find the Split Text action

Now that we have a text version of our Excel content available, we’ll head back to the **Document Conversion** connector actions list and find the **Split a single Text file (txt) into lines** action.

![](https://miro.medium.com/v2/resize:fit:1230/format:webp/1*v9bTSnmgmniG4H0_SVV9iw.png)

### Configure the Split Text request

We’ll configure this request exactly the same way as before — only this time, we’ll use the **body/TextResult** from our **Convert Excel to Text** action in our input file field.

We’ll also use the **trim()** function to remove leading and trailing whitespace from **body/TextResult**. Text strings from file conversions can get a little messy if we don’t use **trim()**.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MhJ86sh_JD1Ipi-E-AOC8g.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*apgHcFX9vb5gUzi-USMbgg.png)

### Loop through each text line with an Apply to each control

We’ll now incorporate an **Apply to each** control, and we’ll configure this action to take the **body/ResultLines** value from our **Split text into lines** response schema.

![](https://miro.medium.com/v2/resize:fit:1252/format:webp/1*4KOfK0StcmG4iqrdaZS7zg.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eCiqlDl6vuMgUPQC7H0uiw.png)

### Compose each text line

Within the **Apply to each** control, we’ll now add a **Compose** action to clean up the **LineContents** value from our **Split text into lines** action.

![](https://miro.medium.com/v2/resize:fit:1244/format:webp/1*hh58Nmr7UzLUIQdoG6jIRQ.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EUiWr_pZIgLG1nNWjsqt5Q.png)

### Use a Condition to check the composed text for a specific string

Beneath **Compose**, we’ll add a **Condition** control that checks the composed **Outputs** for a specific string value. In this case, our value will be the string “2022” (note — it’s important that we read any input we check as a string to avoid errors in our condition).

![](https://miro.medium.com/v2/resize:fit:1238/format:webp/1*gjcf_xTC5Qfn-VLaci2THw.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_tAAvJBfy2Hk2OJ2xXtIkQ.png)

### Send a Teams message with the selected text data

In the **True** branch of our condition, we’ll send a **Teams** message to some team member (in this case ourselves). We’ll include a simple message — like “Spending in the year” + Output + “dollars”.

![](https://miro.medium.com/v2/resize:fit:1216/format:webp/1*7RFwdGP0rrb5ei8u2BPtJw.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BFsfzxcti96WFXphe8qb1w.png)

### Test the flow and review the output

When we run this flow, we’ll receive a single **Teams** message for the total spending in 2022.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jOHrKJv31F1yP2z92BYMww.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6bYTd4c9sdh8-rvHuNSKZA.png)

All values other than the one containing “2022” will have been ignored in our condition.

![](https://miro.medium.com/v2/resize:fit:1244/format:webp/1*puDkHD8aLRw-mQue6KSmzg.png)

![](https://miro.medium.com/v2/resize:fit:1212/format:webp/1*PhSBvUA4FS_Fkg3XvQ_Vpg.png)

### Conclusion

In this walkthrough, we learned how to process Excel files as plain text using Cloudmersive connectors in Power Automate. We converted an Excel file to text, split that text into a series of separate lines, and used a condition to query each line for a specific value.

This is one easy way to leverage Excel data in a quick flow without converting to JSON or CSV first!

Remember to check back in on this blog for more Power Automate walkthroughs.