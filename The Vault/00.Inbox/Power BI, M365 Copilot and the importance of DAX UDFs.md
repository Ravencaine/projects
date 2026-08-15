---
title: "Power BI, M365 Copilot and the importance of DAX UDFs"
source: "https://blog.crossjoin.co.uk/2026/07/26/power-bi-m365-copilot-and-the-importance-of-dax-udfs/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Chris Webb]]"
  - "[[View all posts by Chris Webb]]"
published: 2026-07-26
created: 2026-08-08
description: "DAX UDFs can be used my M365 Copilot for complex data analysis"
Processed: "Unprocessed"
---
This was a big week for Power BI Copilot with the announcement of a new direction for the feature. If you haven’t done so already, read the two announcement blog posts [here](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/The-future-of-conversational-analytics-in-Fabric/ba-p/5302562) and [here](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Bringing-Power-BI-Insights-to-Every-Copilot-User/ba-p/5309360) and check out this [demo video](https://www.youtube.com/watch?v=R1JIRc4KT7I). There are some pros and cons to this change (yes, you’re going to need an M365 Copilot licence to use it but no Fabric capacity is needed any more – this works with models in Pro workspaces too) and there are more features still to come and problems to be solved, but the bottom line is that all of the work you’ve done preparing your semantic models for Copilot is not wasted and while the existing Power BI Copilot worked pretty well, the combination of M365 Copilot and Power BI semantic models works much, much better.

Probably the biggest change is that whereas the existing Power BI Copilot can answer questions in a number of different ways, for example by constructing a Power BI visual, M365 Copilot usually just generates and runs DAX queries against the underlying semantic model. It’s very good at generating syntactically correct DAX queries and of course your model’s AI Instructions are respected, but two risks remain:

1. M365 Copilot generates a DAX query that returns the correct result but not necessarily one that is optimal in terms of performance or CU cost
2. Multiple end users want to do the same kind of analysis but don’t know precisely how it should be performed, give vague instructions or are inconsistent, so they might each get slightly different results

Both of these problems can be solved in different ways but as a semantic model developer I find that adding [DAX User-Defined Functions](https://learn.microsoft.com/en-us/dax/best-practices/dax-user-defined-functions) (UDFs) to your model is the easiest way to do so. This is something [I wrote about last year](https://blog.crossjoin.co.uk/2025/11/09/calling-dax-udfs-from-power-bi-copilot/) but I thought I would revisit the topic because of its importance in the new world of M365 Copilot. If you’re going to centralise all your business logic in a semantic model then that should include the definition of complex analytical operations, something that a DAX UDF that returns a table can handle better than a [DAX fragment embedded in your AI Instructions](https://blog.crossjoin.co.uk/2025/08/17/power-bi-copilot-ai-instructions-and-dax-query-templates/) or a text description of how your analysis should be performed.

Using the same semantic model containing [UK Land Registry Price Paid data](https://www.gov.uk/government/collections/price-paid-data) and the same ABC analysis UDF from that [previous post](https://blog.crossjoin.co.uk/2025/11/09/calling-dax-udfs-from-power-bi-copilot/), I ran a similar test to the one in that post in M365 Copilot. I only made one change to the AI Instructions for the semantic model, adding two new paragraphs highlighted below:

```
This semantic model contains a DAX user-defined function called ABC that does an ABC analysis on the data in the Transactions table. It takes three parameters defined as follows:
AUpperBoundary - an integer value which is the upper boundary of transactions in the A group
BUpperBoundary - an integer value which is the upper boundary of transactions in the B group
AnalysisDate: a datetime value which is the date to filter transactions on
The function returns a table which can be used in an EVALUATE statement in a DAX query.

If a user asks for an ABC analysis then you must **always** use this function. Do not add any other columns or totals or try to do any other calculations on what this function returns, just return the table that the function returns and nothing else.

If the user does not specify the values needed for the function parameters please ask the user for them - do not make any assumptions. Never try to generate the DAX for an ABC analysis yourself because it may result in incorrect or inconsistent results.

For example if I wanted to see the number of transactions which took place on 1st January 2025 divided into three groups:
A - transactions between £0 up to and including £250000
B - transactions above £250000 up to and including £700000
C - transactions above £700000
I could call the function as follows:
ABC(250000, 700000, DATE(2025,1,1))
```

I added the first new paragraph because I found M365 Copilot was trying to be too clever and adding extra columns and subtotals that I didn’t think were necessary, and running extra DAX queries in order to do so. I added the second one when I found that if I asked a vague question then Copilot made too many assumptions and didn’t use my UDF.

The following prompt:

```
Use this semantic model <insert URL of semantic model here> to do an ABC analysis. The upper boundary for the first group is £290000 and the upper boundary for the second group is £790000. Filter the transactions to just 20th January 2025.
```

…resulted in the following output:![](https://i0.wp.com/blog.crossjoin.co.uk/wp-content/uploads/2026/07/image-10.png?w=1296&ssl=1)

…which is exactly what I wanted. What’s more it worked consistently across all my tests and I could see that the only DAX queries run looked like this:

```
EVALUATE
ABC(290000, 790000, DATE(2025,1,20))
ORDER BY [ABC Group]
```

When I tried a vaguer prompt, like:

```
Use this semantic model <insert URL of semantic model here> to do an ABC analysis.
```

M365 Copilot asked me for the extra information it needed to do the ABC analysis:

![](https://i0.wp.com/blog.crossjoin.co.uk/wp-content/uploads/2026/07/image-11.png?w=708&ssl=1)

Interestingly when I deleted the AI Instructions above and pasted more or less the same text into the Description property of the UDF, I found that M365 Copilot did not use the UDF and instead it generated its own DAX query – which still gave the correct result but which included a number of additional measures from the semantic model that I didn’t think were relevant. So explaining in your AI Instructions what UDFs are present and what they should be used for is necessary.

Anyway, to reiterate my point, I think DAX UDFs are going to be more and more important in the future. Up to now they’ve been useful as a way of encapsulating and reusing logic across calculations inside a semantic model; Power BI, alas, doesn’t provide a way for a report to show the output of a table-valued UDF. As more users consume data from Power BI semantic models outside Power BI reports, in tools like M365 Copilot that can answer questions by generating any DAX query they want, then DAX UDFs provide a way for semantic model developers to specify how certain types of analysis should be performed to ensure consistency and performance.