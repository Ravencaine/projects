---
title: "How to Automate CSV Entries to a SharePoint List in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-automate-csv-entries-to-a-sharepoint-list-in-power-automate-975f144405e3"
author:
  - "[[Cloudmersive]]"
published: 2026-07-30
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8aPOmNZK1JDoWIwqKmCxrw.jpeg)

CSV exports wind up in SharePoint all the time. They might come from a CRM, HR system, event registration, vendor, or some customer-management platform.

In the original CSV format, their contents aren’t easily searchable or filterable in the SharePoint environment, but we can change that by automatically updating a SharePoint List with their contents.

In this brief walkthrough, we’ll use the SharePoint and Cloudmersive Document Conversion connectors in Power Automate to listen for new CSV uploads, convert their contents to JSON, and update list columns with elements from each JSON object.

### Automate CSV Entries to a SharePoint List

The first thing we need to do is build a SharePoint List which matches the expected structure of the CSV upload.

That’s easy to do; we’ll simply create a new List, start from scratch, and mirror each column from our CSV as a single-line text column.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6e1LVAgvdrB4QGrNFR9kTA.png)

If you’re wondering why we don’t just import the CSV to SharePoint as our List template, the reason has to do with how SharePoint handles columns with values like “Email”. SharePoint email columns will expect valid emails within the company directory, and if any email in the CSV isn’t recognized in that directory, the flow will fail.

It’s far easier to add a single-line text email column (like we have in our example) and then use the advanced settings to make the text in that column clickable.

![](https://miro.medium.com/v2/resize:fit:1282/format:webp/1*frGB8bcHu9djB5UCmaLdYQ.png)

We’ll now get started building our flow. We’ll create an **Automated Cloud Flow** using the SharePoint **When a file is created (properties only)** trigger.

We’ll provide our SharePoint site address, library name, and target folder. CSV files uploaded to that target folder will trigger our flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*l1Xj7E8I1ULG5qU1wkwfeQ.png)

Next, we’ll add the SharePoint **Get file content** action. We’ll provide the same site address, and we’ll then use the **Identifier** (file identifier) from our trigger to select the file that triggered our flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UM-I-5-1Qk12mRXhy-lTnw.png)

Now that we have access to CSV file content, we’ll convert that content to JSON using the **Cloudmersive Document Conversion** connector.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*C1cl3ZeHU1TQXFqn5BpE-A.png)

We’ll locate and select the **Convert CSV to JSON conversion** action, create our connection with a free API key (we can create one on the Cloudmersive website), and pass in **File Content** and **File name with extension** from earlier steps to satisfy our two parameters.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tYKkkfRWCN_pBV602m5hcQ.png)

This returns an array of JSON objects which mirror the original CSV columns; each CSV column is now an element of a JSON object. We now simply need to iterate through that array and pass each element from each object into the corresponding list column.

We’ll handle the iteration step with the **Apply to Each** control. This takes the array **Body** output from our conversion step.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oiiN6wdRtyXALXhbQAh6BA.png)

Within the loop we just created, we’ll now add the SharePoint **Create item** action, which is the correct action for updating SharePoint lists. We’ll provide the same site address we’ve been using throughout, select our list name from the dropdown, and open the **Advanced parameters** to begin mapping JSON elements to the corresponding list columns.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*u8YgXaHwZ8n-KI2-hTI3IA.png)

We’ll map each element using the **item** expression. The formatting for this expression is simple; we start with `item()?[‘*text*’]` and replace *text* with the name of the column in our original CSV.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7l06M-4iZzKLc71XvWA3hQ.png)

At this point, our flow is complete, so we’ll save it and run a test with an example CSV following the appropriate format. To trigger our test, we’ll drop that CSV into our target folder. In this example, we’ll be using the same CSV shown earlier in this article as our test document.

When our flow finishes running, we’ll first check that each step ran correctly:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5WeXVcM-zEvs6V0WXAWLdQ.png)

And then we’ll refresh our list, which should now contain each line of information from our input CSV:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ObvDhAa1AYGHAVrFWOcOjw.png)

If we included the JSON column formatting shown earlier on, we should find that each email is a clickable link which opens an Outlook message directly.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Y-Hh-E53D-REnytOV0iC9A.png)

And now we’re done — every CSV uploaded to that folder will now create a new item on our list. All it took was 3–4 actions after our trigger.