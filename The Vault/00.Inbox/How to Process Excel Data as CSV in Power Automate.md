---
title: "How to Process Excel Data as CSV in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-process-excel-data-as-csv-in-power-automate-5b61b007b281"
author:
  - "[[Cloudmersive]]"
published: 2025-02-12
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Converting Excel data to CSV is an integral part of every-day life for data wranglers. For most, [handling that conversion in a simple Power Automate flow](https://medium.com/me/stats/post/2a08ad108235) is more convenient than writing code — but what if we want to take subsequent programmatic actions with our CSV data, too?

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*o4-p6_4ejXG-AZqxF4Q_VQ.jpeg)

Thankfully, Power Automate gives us all the tools we need to process and utilize our CSV data in exciting programmatic workflows. Without even *really* scratching the surface of Power Automate’s capabilities, we can create complex workflows that, for example, filter, select, and automatically share CSV data from converted multi-worksheet Excel documents.

### Process Excel Data as CSV Content in Power Automate

Using **Cloudmersive Document Conversion** connector actions in conjunction with built-in Power Automate connectors (like the **Data Operation** and **Control** connectors) we can divide our Excel spreadsheets into a series of component worksheets, convert those worksheets to CSV, compose our CSV data, split our data line by line, and select the precise data we need from the original spreadsheet.

### Example Flow (Step-by-Step Walkthrough)

Let’s walk through a quick example to see how this works.

In this example, we’ll use an **Instant cloud flow** with a manual trigger, and we’ll create a manual file upload field within our trigger step.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Hoxzt-pogP8Y-I1DkAqHWA.png)

Next, we’ll use a **Cloudmersive Document Conversion** connector action to split our Excel file into a series of separate worksheets.

We can find the action we need by first searching for Cloudmersive connectors in the Power Automate library. When we find the **Document Conversion** connector with the green logo, we’ll click “See more” to view the full actions list.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IScMXtTP5ezCabGKg4f4FA.png)

From the actions list, we’ll look for an action called **Split a single Excel XLSX into Separate Worksheets**.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-TjCAkKQLG3YrQlxzYjTlw.png)

We’ll select this action, and we’ll then create our connection (we only need to create our connection once for this entire flow). To authorize our connection, we’ll need a free API key, and we can get one by creating a free account on the Cloudmersive website (this will allow up to 800 API calls/month with no commitment).

To configure our **Split Excel** request, we’ll pass file byte and file name values down from our manual file input trigger. We’ll then click “Show all” to view the **Advanced parameters**, where we’ll select “Yes” from the dropdown to return each worksheet’s file bytes directly to our flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BpjnlxidLIq2qGoFHuxIPg.png)

In our next step, we’ll convert each induvial Excel worksheet to CSV.

To handle this process, we’ll head back to the **Document Conversion** connector actions list and locate the **Convert Excel XLSX Spreadsheet to CSV** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eGEwvKAmhTnXlz-NbHQzGA.png)

After we select this action, we’ll configure our file input parameter by passing the **WorksheetContents** array down from the **Split XLSX** action, and we’ll pass the file name value from our manual file input trigger once again (note — the file name doesn’t *really* matter in this context).

We’ll notice that Power Automate wraps our **Convert Excel to CSV** action in a **For each** control to handle the **WorksheetContents** array. We’ll build the rest of our flow within this control.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UaN_fvxiPrD_NHjNbShdfQ.png)

Now that we’ve converted each individual Excel worksheet to CSV, we’ll use the **Compose** action from the **Data Operation** connector to structure our data and prepare it for consumption by a subsequent flow action. This isn’t strictly necessary, but it’s good practice.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YlqaekLRgjOJoRFL9UlX0g.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wRjXvhm8YOpAF1YIHLiYJA.png)

We’ll now split our composed CSV data into a series of independent lines. As we’re all likely aware, CSV files are just comma-delimited text files, and that means we can use text operators to split each newline.

In this case, we’ll use a convenient action called **Split a single Text file (txt) into lines** which we can find on the **Document Conversion** connector actions list.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aBNG3kUKzHvuqfyKyp6jwQ.png)

We’ll ask our **Split Text into lines** action to consume **Outputs** from our **Compose** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*neU8A5LE7Ca5a8tubYOi_A.png)

We’ve so far created a flow that converts all our original Excel data to CSV and splits that data into independent lines of text. Readying text data in this way is ideal for any downstream data processing action we’d like to take.

In this example, we’ll use a **Condition** control to filter lines of data containing a specific value.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bj2hOQRlzVY2PS3ZuQ3jYA.png)

Of course, the way we use our condition depends entirely on what we want to do with our data.

The Excel spreadsheet we’re using in this example flow has two worksheets with “Annual Expense” data from two separate timespans.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-NQV0n9uK7gc_RYZrY34xA.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*23RFW7rNrKY8vcnvVB0GkQ.png)

In our example, we’ll ask Power Automate to pull data for the years 2022 and 2012 and share that in a MS Teams message.

We’ll do that by asking our **Condition** to check if each individual **LineContents** value **contains** “2022” **or** “2012”.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wzkp64ePDxocAU2hkRb2tA.png)

We’ll then use the **Post message in a chat or channel** action from the MS Teams connector to send the relevant data to ourselves.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7-kkQJcXvXA2oyfYogOajA.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2aU-e-8lOG0f2FC6gWXBRg.png)

After we save our flow, we’ll select an Excel file from our system to run our test with.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5MCRd2PntmFnkLtRJlnMgw.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nyS0yhjKPU9qE0bZNWf_LA.png)

We should find that most conditions turned up false in our test run. In this example, we’ll find two MS Teams messages containing the information for 2022 and 2012 that we were looking for.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JaVLS92oGBnv8Skg3tgT9w.png)

We can filter our CSV data based on any column value we want, and we’ll always get the full line of data in our downstream process.

### Conclusion

In this article, we learned how to process multi-worksheet Excel documents as CSV files in Power Automate using **Cloudmersive, Data Operation** and **Control** connectors. We filtered our CSV data using a **Condition** and located specific data we needed.

The best part: we created reusable flow that will work for most Excel worksheets we need to pull specific data from!

If you’re looking for more interesting Power Automate ideas, remember to give this blog a follow and check back in each day!