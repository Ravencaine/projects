---
title: "Things I Wish I Knew When I Started Using Power Query — Building the Foundation for Scalable…"
source: "https://medium.com/@harsh_goel/things-i-wish-i-knew-when-i-started-using-power-query-building-the-foundation-for-scalable-fb71ee402e56"
author:
  - "[[Harsh Goel]]"
published: 2026-08-02
created: 2026-08-04
description: "More"
Processed: "Unprocessed"
---
**Things I Wish I Knew When I Started Using Power Query — Building the Foundation for Scalable Workflows**

When I started learning Power Query, I found many amazing resources that taught me how to build data connections, transform data, use a row as headers, merge datasets, and automate repetitive tasks. These tutorials were incredibly valuable. They helped me understand the technical side of Power Query and showed me what was possible.

However, as I started using Power Query in real-world situations, I realized that the biggest challenges were not always the complicated transformations. The things that slowed me down the most were the small details — the mistakes that are easy to make but difficult to troubleshoot.

This became especially important when working with healthcare-related data, where information often comes from multiple sources and needs to be refreshed consistently. Whether it is operational reporting, provider data, claims information, or quality metrics, a scalable framework depends on building processes that work reliably every time new data arrives.

As they say, 20% of the problems take up 80% of your time. While I am not sure these issues accounted for 80% of my time, I do know they consumed quite a bit, which is why I wanted to share three lessons I learned along the way, along with the solutions that helped me build more reliable Power Query workflows.

**1\. Be Careful When Entering Data Outside Power Query**

One of the first lessons I learned was that Power Query only controls the data that flows through the query. Any information added manually outside of the Power Query output is separate and will not automatically follow the same filters, transformations, or refresh logic.

For example, imagine you have a Power Query report containing provider information. You apply a filter to exclude inactive providers or specific provider IDs. That filter will work perfectly for the data coming through Power Query.

Data entered manually outside the Power Query output is not part of the query transformation process. Because Power Query only refreshes and applies logic to the data included in the query, manually added values can easily become disconnected from the automated workflow.

![](99.System/Attachments/1!ADi6U4vX7UuZYu7H6oDz-Q.png.webp)

Filter unable to capture data outside the Query

The solution is simple: If you need to add manual adjustments or exceptions, treat them as a separate process. Either:

- Add the information to the original data source before refreshing Power Query, or
- Apply separate Excel filters and controls to any manually entered data.
![](99.System/Attachments/1!9OWm2HkWKbu3QNvXMdMyfA.png.webp)

Seperate filter Applied for Data Outside the query

When building scalable healthcare reporting frameworks, minimizing manual intervention is critical. The more steps that happen outside the automated workflow, the more opportunities there are for inconsistent results.

**2\. Do Not Open Power Query Using “From Table/Range” Unless You Intend to Create a New Query**

This was another mistake I made early in my Power Query journey.

When you select a table in Excel and click: Data → From Table/Range

This creates a new query based on the selected table. It does not open the existing query that produced the table output. If you are trying to edit a query that already exists, opening it this way can create duplicate queries and unnecessary confusion. You may think you are modifying your report logic when you are actually creating a separate workflow.

![](99.System/Attachments/1!sz6k-0aZ1GRtBmSBfzaoyg.png.webp)

Instead, open your existing query through: Data → Queries & Connections

The Queries & Connections panel will appear on the right side of Excel. Find the name of your existing query and double-click it to open the Power Query editor.

**3\. Filtering Rows in Power Query: Thinking Differently From Excel**

This was probably one of the most confusing concepts when I first started. Removing columns is straightforward:Select the column → Right-click → Remove

But what about removing rows? In Excel, many users think about deleting rows manually. Power Query works differently.

Instead of deleting rows, you usually create a transformation step that tells Power Query which rows to keep or exclude every time the data refreshes.

There are two possible approaches.

**Option 1: Remove the Rows from the Source Data**

The simplest approach is to remove unwanted records from the original data source and refresh Power Query. For example, if a provider record should no longer appear in your report, you could remove it from the source system before refreshing.

However, this is not always practical. In many healthcare environments, source data should remain unchanged because it serves as the official record. In those situations, filtering within Power Query is usually the better approach.

**Option 2: Filter Out Rows Directly in Power Query**

Suppose you want to exclude a specific provider ID, such as FAC0001, from your report. Open Power Query and locate the column containing the identifier. In this example, select the dropdown filter for the ‘Provider\_ID’ column.

![](99.System/Attachments/1!sjx4zZ1jfMpfnX9AvQVP1w.png.webp)

Uncheck FAC0001 and click OK.

![](99.System/Attachments/1!bL-_PaVqV1-hRN6yggQuvg.png.webp)

FAC0001 filtered out

Power Query will now create a transformation step that excludes that identifier from the output. When you refresh the data in the future, Power Query will automatically apply the same rule.

Finally, select Home → Close & Load to return the updated results to Excel.

**Final Thoughts**

The biggest lesson I learned from Power Query is that the tool itself is not just about cleaning data — it is about creating repeatable processes.

In healthcare and other data-heavy industries, the goal is rarely to fix one spreadsheet. The goal is to build a framework that can handle new data, new reporting requirements, and future changes without requiring constant manual work.