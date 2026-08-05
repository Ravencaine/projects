---
title: "Power BI What-If Analysis: Forecast Price, Cost & Volume"
source: "https://databear.com/power-bi-what-if-analysis-price-cost-volume-scenarios/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-07-27
created: 2026-08-04
description: "Learn Power BI What-If analysis to model price, cost, and volume changes using field parameters and DAX for better business forecasting."
Processed: "Unprocessed"
---
Understanding how future scenarios can affect your business is vital for informed decision-making. In this guide, you’ll learn how to perform **Power BI What-If analysis** to model changes in price, cost, and volume all without altering your core dataset or measures. Using field parameters, DAX calculations, and SELECTEDVALUE, you’ll gain the tools to dynamically simulate changes and see immediate results.

If you’re looking to build advanced Power BI skills, including hands-on scenario modeling and interactive report design, explore our [Power BI Training Programs](https://databear.com/power-bi-training/) at Data Bear. These professional courses are designed to take your Power BI capabilities to the next level.

##### What Are Power BI What-If Scenarios?

Power BI’s What-If parameters let you test business scenarios interactively. Whether you want to see the effects of a 10% price increase, a 15% cost reduction, or a 25% drop in volume, these scenarios can be modeled using numeric field parameters and slicers — no need to manually recode your reports.

##### Setting Up Your First What-If Parameter

To get started, go to the **Modeling** tab in Power BI and click on **New Parameter**. You’ll see two options:

- **Field Parameter**: Used to toggle between different fields in visuals.
- **Numeric Range Parameter**: Used for What-If analysis.

Choose **Numeric Range**, and define a range such as:

- Start: 0
- End: 20
- Increment: 1

This generates a DAX table using `GENERATESERIES(0, 20, 1)`, and Power BI automatically adds a slicer tied to this parameter.

##### Understanding Field Parameters (TV Remote Analogy)

Think of field parameters like a TV remote: you can change the “channel” (i.e., the value) without switching the whole system. Instead of creating separate reports for each variable, use field parameters as dynamic selectors.

##### Scenario 1: Modeling a Price Increase

To simulate a price increase:

1. Create a numeric parameter from 0% to 20% in 1% increments.
2. Add a slicer to your report using this parameter.
3. Create a DAX measure:
```
Adjusted Revenue = [Base Revenue] * (1 + SELECTEDVALUE('Price Increase Parameter'[Price]))
```

As you adjust the slicer, Adjusted Revenue updates in real time. This lets you visualize the impact of a price change instantly.![Modeling a Price Increase](99.System/Attachments/Modeling_a_Price_Increase.png)

##### Scenario 2: Simulating Cost Reductions

To analyze how cutting costs affects your financials, apply similar logic:

```
Adjusted Cost = [Total Cost] * (1 - SELECTEDVALUE('Cost Reduction Parameter'[Cost]))
```

This formula reduces your total cost based on the selected percentage from the slicer. You can easily reverse it to model cost increases by switching the subtraction to addition.![Simulating Cost Reductions Power BI What-If analysis](99.System/Attachments/Simulating_Cost_Reductions_Power_BI_What-If_analysis.png)

##### Scenario 3: Handling Volume Changes with Negative Values

Volume can increase or decrease, so this parameter needs to allow both positive and negative values. Use:

```
GENERATESERIES(-50, 50, 1)
```

Then calculate adjusted volume:

```
Adjusted Volume = [Base Volume] * (1 + SELECTEDVALUE('Volume Change Parameter'[Volume]))
```

This allows you to simulate anything from a significant reduction in sales volume to a surge in demand.![Handling Volume Changes with Negative Values Power BI What-If analysis](99.System/Attachments/Handling_Volume_Changes_with_Negative_Values_Power_BI_What-If_analysis.png)

##### Bringing It All Together: Dynamic Scenario Modeling

With all three scenarios in place price, cost, and volume you can start combining insights. Adjust multiple sliders simultaneously and observe how your KPIs react across the report.

##### Key Components Recap:

- **Field Parameters**: Provide flexible input ranges for your scenarios.
- **SELECTEDVALUE**: Dynamically picks the slicer input for use in measures.
- **GENERATESERIES**: Builds the range used by numeric parameters.
- **DAX Calculations**: Translates input values into meaningful business metrics.

##### Learn More with Data Bear’s Power BI Training

Want to gain a deeper mastery of Power BI scenario modeling, report interactivity, and advanced DAX? Our comprehensive [Power BI training courses](https://databear.com/power-bi-training/) are designed to give you real-world skills you can immediately apply. From business intelligence fundamentals to expert modeling techniques, you’ll learn everything you need to make Power BI work harder for your business.

##### Final Tips for What-If Analysis in Power BI

- Use clearly labeled slicers for user-friendly interactivity.
- Label your calculated measures for clarity (e.g., Adjusted Revenue, Adjusted Cost).
- Enable both positive and negative inputs where necessary.
- Visualize your results with intuitive visuals like bar charts, line graphs, or KPIs.

Mastering What-If analysis in Power BI equips you with the foresight to navigate complex business scenarios. Whether you’re planning for growth or preparing for risk, these tools make it easier to model the future with confidence.