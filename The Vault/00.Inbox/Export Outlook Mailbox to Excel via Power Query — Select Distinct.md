---
title: "Export Outlook Mailbox to Excel via Power Query — Select Distinct"
source: "https://medium.com/@simon.harrison_Select_Distinct/export-outlook-mailbox-to-excel-via-power-query-select-distinct-465641ec9ab2"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2026-03-31
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*abB9nZMtdbNA8JT7.png)

Handling large volumes of mailbox data can quickly become overwhelming, especially when you’re trying to analyse patterns, track communication behaviour, or build organisation-wide insights. Fortunately, Excel’s **Power Query** provides a powerful, repeatable, and user‑friendly way to transform mailbox data into a clean, analysis‑ready structure — no coding required.

In this guide, we’ll walk through exactly how to load existing mailbox data into Excel using Power Query, transform the columns, clean up senders and recipients, and build a dataset ideal for dashboards or reporting. Whether your source data comes from Outlook, Exchange, or a compliance tool, the steps below will give you a consistent and efficient framework.

## Why Power Query Is the Best Tool for Mailbox Analysis

Mailbox datasets are rarely perfect.

They often contain:

- Duplicate fields
- Unstructured folder paths
- Mixed time formats
- Boolean values stored as text
- Multiple versions of email addresses
- Extra whitespace or system values

Power Query is built for this. With it, you can:

- Clean all fields in seconds
- Split or merge columns
- Convert date/time formats
- Normalise email addresses
- Create reusable transformations
- Refresh data automatically

Once your steps are created, you never have to repeat manual clean up again — just refresh the query whenever new mailbox data is available.

## Step 1: Load Mailbox Data Directly into Excel

Start by loading your mailbox file into Excel:

1.Open Excel → Blank Workbook

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*sqvKgYt3G5KWd05A.png)

2\. Go to the **Data** tab

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*xWwhxJ7suzwXtqsi.png)

3\. Select **Get Data**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*uqfkSx28-adzzwvv.png)

4\. Choose **From Other Sources** → **From Microsoft Exchange**

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*xUjEuBPl7pSiKESF.png)

5\. Enter your **Mailbox Address**

![](https://miro.medium.com/v2/resize:fit:1116/format:webp/0*hsMnqvWvXZQcnYrz.png)

6\. **Sign-in** if prompted to

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Ic52oihxgMZSk5wS.png)

7\. Click **Mail** table

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*s4cDUejYEHOL1k9e.png)

8\. Select **Transform** **Data**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*S-QqlIBg1m2IP3zz.png)

This opens the **Power Query Editor**, where all transformation steps will take place.

## Step 2: Review & Format Column Headers

When your data loads, check that the headers appear correctly.

If Power Query hasn’t automatically promoted them:

**Home → Use First Row as Headers**

Next, set the appropriate data types

Correct data types ensure accurate reporting and avoid issues in PivotTables later.

## Step 3: Split the Sender Into Name and Email Address

Before analysing your mailbox data, it’s helpful to break the Sender record into separate Name and Email Address fields so each part can be used independently.

Mailbox data often includes the **Sender** column as a record containing two pieces of information:

To separate these into their own columns, locate to Navigation (within Applied Steps):

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*szbYS9ilrxIg9zW6.png)

1.Click the **expand icon** (two arrows) beside the Sender column

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*eCCbWQW4oVyDiR45.png)

2\. In the menu that appears, tick the fields you want to extract:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*ZERp88k1JXTchTjT.png)

3\. Select **OK**

This will create two new columns, making it easier to filter, sort, and analyse sender information.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*QA3htSt2eupLnPOM.png)

## Step 4: Split the Email Address into Name and Domain

Once the Sender’s email address is available as a single text field, the next step is to split it into the mailbox name and the domain to make grouping and filtering much easier

You may want to separate the email address into two useful parts:

- **The mailbox name** (everything before the @)
- **The domain** (everything after the @)

To do this:

1.Select the **Sender.Address** column

2\. Go to **Home** → **Split Column** → **By Delimiter**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*GaXtT3U-0-zNShOh.png)

3\. Choose @ as the delimiter

4\. Select **At the right-most occurrence of the delimiter**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*1jX5u9F248A_OrMX.png)

5\. Click **OK**

Power Query will create two new columns:

- **Sender.Address.1** — the part *before* the @ (e.g. ryan.patel, joe.bloggs, laura.benson)
- **Sender.Address.2** — the domain portion (e.g., example.com, sample.co.uk)

This makes it easy to group by mailbox name or analyse domain usage across your dataset.

![](https://miro.medium.com/v2/resize:fit:1274/format:webp/0*95kzRxbD5YkAfQ2p.png)

Optional: Rename the field names to a suitable name

![](https://miro.medium.com/v2/resize:fit:1246/format:webp/0*FHPDdj7A527_bc4P.png)

**Close and Load** these changes in Power Query

Best of all, you can refresh this table anytime:

**Data → Refresh All**

Every transformation step will be applied to the updated mailbox file instantly.

## Step 5: Analyse Your Data with a Pivot Table

Once your transformed mailbox data has been **Closed & Loaded** back into Excel, you can begin analysing it straight away. One of the quickest and most powerful ways to do this is by creating a **Pivot Table.**

A Pivot Table lets you easily group emails by sender domain, sender name, importance, dates, or any other fields you cleaned in Power Query.

To create a Pivot Table:

1.Click Add New Sheet in Excel

![](https://miro.medium.com/v2/resize:fit:1310/format:webp/0*dknxdS4UEVfbTD8T.png)

2\. Go to Insert → PivotTable

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Vd5rdR5YHL6ddrOV.png)

3\. Select the Data Table range

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*CeOudg3ZaijhZTlM.png)

4\. Click **OK**

## Visualising Email Activity

You can build a visual breakdown of your email activity.  
For example, to analyse which domains send you the most messages:

1\. **Drag & Drop Sender.Domain** into the **Rows area**

2\. **Drag & Drop Sender.LocalPart** underneath it

3\. **Drag Id** into the **Values area**

4\. Set **Values** to **Count of Id**

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*jcmQbVr5znDMQLY7.png)

You can now sort these descending based on the Count of Id and see a summary like this:

- Top domains grouped together
- Individual mailbox names nested underneath
- A count of how many emails came from each sender

Click the + icon next to each domain to drill down into individual senders

![](https://miro.medium.com/v2/resize:fit:1122/format:webp/0*eEfbHem5RzE91Oeb.png)

This provides an instant overview of where your email volume is coming from and highlights the most active senders in each domain.

This approach works beautifully when combined with the split fields you created earlier, letting you drill down from domain → mailbox → individual messages in just a few clicks.

## Practical Use Cases

This approach to analysing mailbox data in Excel is useful in a variety of scenarios:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*WNkTWziHWQVFMLvS.png)

- **Low-Cost CRM:** Identify your most active customers and suppliers by message volume without needing specialized software
- **Inbox Hygiene:** Target “no-reply” senders and high-frequency newsletters to systematically reduce digital clutter
- **Behavioural Trends:** Map internal vs. external communication patterns to see exactly where your team’s time is spent
- **Security & Audit:** Detect sudden spikes in activity or unusual sender domains to perform light-touch compliance checks
- **Spam Mitigation:** Group by Sender.Domain to isolate and block persistent low-value sources at the root.
- **Attachment Tracking:** Filter by the HasAttachments field to monitor high-volume file transfers and ensure important client documents are never overlooked.

## Final Thoughts

Power Query transforms messy mailbox data into a polished, reusable dataset you can analyse in minutes. By loading your mailbox file directly into Excel, performing structured cleanup, and refreshing it as needed, you eliminate repetitive manual work and build a reliable reporting pipeline.

**Ready to take your data further?**

This process can easily be extended with additional Power Query steps, dashboards, or automation depending on your needs.

Visit our [**Business Analytics Blog**](https://www.selectdistinct.co.uk/business-analytics-blog/) for more tips on automating your workflows and turning raw data into actionable insights