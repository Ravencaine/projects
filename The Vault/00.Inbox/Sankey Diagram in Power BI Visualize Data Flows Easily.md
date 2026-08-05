---
title: "Sankey Diagram in Power BI: Visualize Data Flows Easily"
source: "https://databear.com/sankey-diagram-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-06-25
created: 2026-08-04
description: "Learn how to use the Sankey diagram in Power BI. Follow a step-by-step guide to visualize data flows and relationships using custom visuals."
Processed: "Unprocessed"
---
If you’re looking for a compelling way to visualize data movement or relationships between categories, the **Sankey diagram in Power BI** is a fantastic tool. Often overlooked, this powerful custom visual can illustrate data distribution and flow in a way that’s intuitive and easy to understand.

In this guide, you’ll learn how to:

- Install and use the Sankey diagram in Power BI
- Transform your dataset to fit the Sankey format
- Add multiple flow layers (e.g., year → priority → status)
- Customize your diagram for deeper insights

Let’s dive in and bring your data to life with flow visualizations.

##### What is a Sankey Diagram?

A **Sankey diagram** is a type of flowchart that visually represents how data moves from one category (source) to another (destination). The **width of each flow** represents the volume or weight of data, making it easy to see major contributors and bottlenecks at a glance.

For example, a company’s support ticket data can be visualized by year, department, and ticket status—clearly showing how volumes shift over time or across categories.

##### Step 1: Prepare Your Data in Power BI

Let’s start with a typical support ticket dataset that includes:

- Created Date
- Ticket Priority
- Ticket Status
- Department

This flat data structure is great for bar charts or tables, but **not ideal for a Sankey diagram**, which requires data in a source-destination-weight format.![Prepare Your Data in Power BI](99.System/Attachments/Prepare_Your_Data_in_Power_BI.png)

##### Step 2: Add the Sankey Diagram to Power BI

The Sankey diagram is a **custom visual**, not included by default. To add it:

1. Go to the **Visualizations pane** in Power BI Desktop.
2. Click the **ellipsis (⋯)** → **Get more visuals**.
3. Search for “Sankey” and import it from AppSource.
4. You’ll now see the Sankey diagram icon in your visualizations panel.![Add the Sankey Diagram to Power BI](99.System/Attachments/Add_the_Sankey_Diagram_to_Power_BI.png)

##### Step 3: Create a Source-Destination Table

To build the Sankey diagram, you need a table that includes:

- **Source** (e.g., Year)
- **Destination** (e.g., Priority)
- **Weight** (e.g., Count of Tickets)

Use DAX to create a new table:

```
SankeyData = 
SUMMARIZE(
    Tickets,
    Tickets[CreatedYear],
    Tickets[Priority],
    "Count", COUNT(Tickets[TicketID])
)
```

This generates a simple source-destination-weight table.

![Create a Source-Destination Table](99.System/Attachments/Create_a_Source-Destination_Table.png)

##### Step 4: Build the Sankey Visual

1. Create a new page in Power BI.
2. Add the Sankey visual.
3. Drag in:
	- `CreatedYear` → **Source**
		- `Priority` → **Destination**
		- `Count` → **Weight**

You’ll now see the flow of tickets from year to priority level visualized as

![Build the Sankey Visual](99.System/Attachments/Build_the_Sankey_Visual.png) Sankey paths.

##### Step 5: Add More Layers with UNION

To visualize flows across multiple dimensions (e.g., Year → Priority → Status), use multiple `SUMMARIZE` functions and combine them with `UNION`:

```
SankeyData = 
UNION(
    SUMMARIZE(Tickets, Tickets[CreatedYear], Tickets[Priority], "Count", COUNT(Tickets[TicketID])),
    SUMMARIZE(Tickets, Tickets[Priority], Tickets[Status], "Count", COUNT(Tickets[TicketID]))
)
```

Each additional flow layer adds depth and insight to your visualization.![Add More Layers with UNION](99.System/Attachments/Add_More_Layers_with_UNION.png)

##### Step 6: Explore and Analyze

With your Sankey diagram in place, you can:

- Click on a category to highlight specific flows
- Analyze bottlenecks or high-volume transitions
- Add tooltips or filters to enrich the analysis

The Sankey visual supports interactivity, making it great for dashboard use or exploratory data analysis.![Explore and Analyze](99.System/Attachments/Explore_and_Analyze.png)

##### Why Use Sankey Diagrams in Power BI?

- **Visual clarity**: Track how values flow across multiple categories.
- **Data storytelling**: Ideal for illustrating processes, funnels, or workflows.
- **Interactive analysis**: Filter and highlight segments for root-cause investigation.

Despite its power, the **Sankey diagram in Power BI** is underused—mainly because many users don’t know how to format their data correctly. With this guide, you can confidently add it to your visualization toolbox.

##### Learn More About Advanced Power BI Visualizations

Want to explore more custom visuals and advanced techniques? Check out the [Advanced Power BI Boot Camp](https://databear.com/power-bi-training/), where you’ll learn best practices for data modeling, visual storytelling, DAX, and automation.