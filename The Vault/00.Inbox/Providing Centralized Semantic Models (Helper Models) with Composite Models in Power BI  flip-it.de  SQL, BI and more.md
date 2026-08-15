---
title: "Providing Centralized Semantic Models (Helper Models) with Composite Models in Power BI | flip-it.de :: SQL, BI and more"
source: "https://www.flip-design.de/?p=1633&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-07-04
created: 2026-08-08
description:
Processed: "Unprocessed"
---
In my previous articles, I demonstrated how to create both a Date dimension and Calculation Groups directly in Power BI Desktop using TMDL.

A common challenge in real-world projects is making these reusable objects available to multiple report developers.

Especially in larger organizations, not every developer has the required knowledge to build and maintain Date dimensions or Calculation Groups. In addition, every enhancement or bug fix must often be implemented in numerous reports, resulting in unnecessary maintenance effort.

For this reason, it makes sense to maintain these shared components only once and reuse them across multiple Power BI projects.

One elegant solution is the use of **Composite Models**. If you are not yet familiar with this concept, I have already covered it in a previous article:

<iframe sandbox="allow-scripts" title="„Power BI composite models – a underestimated feature“ – flip-it.de :: SQL, BI and more" src="https://www.flip-design.de/?p=1278&amp;embed=true#?secret=FgfGXcXTbd#?secret=xhExbxadc9" width="500" height="264" frameborder="0"></iframe>

**Creating the Central Semantic Model**

For this example, I created a new Power BI file that contains only the shared components.

These include:

- a Date dimension
- a Calculation Group for time intelligence
- optionally, additional shared dimensions or Calculation Groups
![](https://www.flip-design.de/wp-content/uploads/2026/07/image.png)

The Calculation Group used here is the same one presented in my previous article:

<iframe sandbox="allow-scripts" title="„Accelerating Power BI Development with TMDL: Faster, Consistent, and Scalable Reporting“ – flip-it.de :: SQL, BI and more" src="https://www.flip-design.de/?p=1537&amp;embed=true#?secret=wVdjSz0a2Q#?secret=5uHpuvjCOc" width="500" height="292" frameborder="0"></iframe>

Of course, this model can contain many additional reusable components, for example:

- Date dimensions
- Product dimensions
- Organizational hierarchies
- Cost center dimensions
- Country or regional dimensions
- Calculation Groups
- Shared measures

Once completed, the model is published to a centrally managed Power BI workspace.

**Required Permissions**

To consume the model, report developers only require:

- Read permissions on the workspace
- Build permission on the semantic model
![](https://www.flip-design.de/wp-content/uploads/2026/07/image-1.png)

I also recommend assigning an **Endorsement** (*Promoted* or *Certified*) to the semantic model. This makes it much easier for developers to find and immediately identify it as an approved corporate model.

**Using the Model in a Report**

Next, I opened Power BI Desktop using a different user account.

In this report, only the fact data is imported.

The shared objects are then connected by selecting **Power BI semantic model**.

![](https://www.flip-design.de/wp-content/uploads/2026/07/image-2.png)

After selecting the previously published semantic model…

![](https://www.flip-design.de/wp-content/uploads/2026/07/image-3.png)

…the required tables can simply be added to the report.

![](https://www.flip-design.de/wp-content/uploads/2026/07/image-4.png)

the Model view, Power BI automatically highlights objects that originate from an external semantic model.

![](https://www.flip-design.de/wp-content/uploads/2026/07/image-5.png)

After creating a measure based on the fact table, it can immediately be used together with the centrally managed Calculation Group.

Naturally, this requires a relationship between the fact table and the shared Date dimension.

![](https://www.flip-design.de/wp-content/uploads/2026/07/image-6.png)

## Benefits of a Helper Model

Using a centralized semantic model offers several advantages:

- Centralized maintenance of shared dimensions
- Reusable Calculation Groups
- Reduced duplication of business logic
- Lower maintenance effort
- Consistent calculations across reports
- Standardized semantic models throughout the organization
- Reduced load on data sources because shared dimensions only need to be refreshed once
- **Translations, display names, descriptions, and other model metadata only need to be maintained once and are automatically available to all connected reports.**

In larger Power BI environments, this approach can significantly simplify both development and long-term maintenance.

## Current Limitations

At the time of writing, there are still a few limitations.

For example, **DAX User Defined Functions (UDFs)** cannot currently be shared through a centralized semantic model.

The same applies to measures or calculations that expose information such as the **last data refresh timestamp**. These calculations always belong to the semantic model in which they were created and therefore cannot be provided centrally.

Hopefully, Microsoft will remove these limitations in the future and allow even more reusable functionality to be delivered through centralized semantic models.

## Conclusion

Composite Models provide an excellent way to build reusable semantic components for an entire Power BI environment.

Shared Date dimensions, Calculation Groups, translations, and other commonly used semantic objects can be maintained in a single location and reused across multiple reports. This reduces maintenance effort, ensures consistent calculations, simplifies multilingual deployments, and makes report development much easier—especially for developers with limited modeling experience.

For larger Power BI implementations, I consider this one of the cleanest and most maintainable approaches for providing reusable semantic components across an organization.