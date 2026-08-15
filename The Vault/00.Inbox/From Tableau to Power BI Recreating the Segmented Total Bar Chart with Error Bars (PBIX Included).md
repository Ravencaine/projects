---
title: "From Tableau to Power BI: Recreating the Segmented Total Bar Chart with Error Bars (PBIX Included)"
source: "https://medium.com/learning-data/from-tableau-to-power-bi-recreating-the-segmented-total-bar-chart-with-error-bars-pbix-included-ff688f300fea"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2025-08-01
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
*A step-by-step guide to building Kevin Flerlage’s innovative visualization natively in Power BI*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*r37CRjVZtNv_f5ejPdnx3A.png)

Say no to Stacked Bar Charts

Have you ever found yourself staring at a stacked bar chart, feeling frustrated by its inherent limitations? You’re not alone.

As data visualization professionals, we frequently encounter fundamental problems with stacked bars: while it is easy to compare total values and segments aligned to the axis, comparing middle segments becomes nearly impossible due to their differing starting points.

This challenge led me on an exciting journey that started with discovering Kevin Flerlage’s brilliant alternative to stacked bar charts in Tableau and culminated in successfully recreating this innovative visualization natively in Power BI using a creative combination of clustered column charts, small multiples, and error bars.

## The Challenge with Traditional Stacked Bar Charts

Kevin Flerlage, a renowned Tableau Evangelist and Hall of Fame Visionary, has been vocal about the problems with stacked bar charts. As he explains: *“I don’t love stacked bar charts. Okay, okay, okay…I hate stacked bar charts. There are simply so many problems in reading and understanding them.”* [*1*](https://www.flerlagetwins.com/2025/04/the-best-alternative-to-stacked-bar.html)*.*

The core issues include:

- **Easy total comparison**: You can compare the grand total of bars
- **Easy axis-aligned comparison**: You can compare segments aligned to the axis
- **Difficult middle segment comparison**: Comparing segments not aligned to an axis becomes very challenging

## Discovering the Segmented Total Bar Chart

Flerlage’s solution, which he calls the **“Segmented Total Bar Chart,”** addresses these limitations by presenting segments distinctly without traditional stacking. This approach provides several advantages:

- **Clear segment visibility and comparison**
- **Maintained total context through outlined boxes**
- **Elimination of overlapping baselines** that confuse viewers
- **Better readability** for categorical data analysis

## My Power BI Implementation Strategy

After studying Kevin’s Tableau approach, I developed a native Power BI solution using:

- **Clustered Column Charts** as the foundation
- **Small Multiples** for category separation
- **Error Bars** creatively repurposed as segment containers
- **Strategic DAX measures** for precise control

Let me walk you through the complete implementation.

## Step-by-Step Implementation Guide

## Prerequisites

Before starting, ensure you have:

- Power BI Desktop (March 2022 or later for error bar support)
- Sample dataset with categories and segments (I’ll use regions and customer segments)
- Basic understanding of DAX measures
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*j0r_MovHB_3YqG_LVYIDhg.png)

The data is very simple. You can create it in Power BI itself by entering the data manually.

## Step 1: Prepare Your Data and Base Measures

For this example, I’m using a dataset with:

- **Regions**: East, West, Central, South
- **Segments**: Consumer, Corporate, Home Office
- **Values**: Revenue amounts

First, create your foundational measures:

```c
Region Total = 
CALCULATE(
    SUM('regions-segment-revenue-data'[Revenue]), 
    ALLEXCEPT(
        'regions-segment-revenue-data', 
        'regions-segment-revenue-data'[Region]
    )
)
```

Then create individual segment totals:

```c
Consumer Total = 
CALCULATE(
    SUM('regions-segment-revenue-data'[Revenue]),
    'regions-segment-revenue-data'[Segment] = "Consumer"
)
```
```c
Corporate Total = 
CALCULATE(
    SUM('regions-segment-revenue-data'[Revenue]),
    'regions-segment-revenue-data'[Segment] = "Corporate"
)
```
```c
Home Office Total = 
CALCULATE(
    SUM('regions-segment-revenue-data'[Revenue]),
    'regions-segment-revenue-data'[Segment] = "Home Office"
)
```

## Step 2: Create the Dummy Framework

The key insight is using dummy measures to create consistent bar heights. Since Consumer has the highest values in my dataset, I’ll use it as the baseline:

```c
Dummy 4 = [Consumer Total] * 1.1
Dummy 5 = [Consumer Total] * 1.1  
Dummy 6 = [Consumer Total] * 1.1
```

These create uniform column heights, giving us space to work with error bars.

Also, create the error bar baseline:

```c
Dummy = 0
```

## Step 3: Build the Base Clustered Column Chart

1. **Add a Clustered Column Chart** to your canvas
2. **Configure the Y-axis**: Add all three dummy measures (Dummy 4, Dummy 5, Dummy 6)
3. **Configure Small Multiples**: Add your Region field here
4. **Add Tooltip**: Include the Region Total measure

At this stage, you’ll see uniform gray bars across all regions.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*2QLAKvD9lZajqiPWtZZw_A.png)

The build section

## Step 4: Configure Small Multiples Layout

In the **Small multiples** formatting section:

- **Layout**: Set Rows = 1, Columns = 4
- **Padding**: Set all padding values to 5
- **Turn OFF**: Border, Title, and Background
- **Spacing**: This creates a clean separation between regions
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-cUH3tdoFYKDJI9X8-6Dfw.png)

Small Multiples Format Style

## Step 5: Format the Base Columns

In the **Columns** formatting section:

- **Colors**: Set all columns to gray (#808080 or similar)
- **Spacing**:
- Space between categories: 15%
- Space between series: 1%
- **Enable Series Overlap**: This option brings the columns closer together and hides the lines between them.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*fRXDtyCJ5uC2mtqpJsnRrQ.png)

Format Columns

## Step 6: Configure Data Labels Strategically

Here’s a crucial step for clean presentation:

- **Dummy 4**: Turn data labels OFF
- **Dummy 5**: Turn data labels ON (this will be our middle reference)
- **Dummy 6**: Turn data labels OFF

For Dummy 5 labels:

- **Value**: Use Region field
- **Details**: Use \[Region Total\] measure

This gives you region names positioned in the middle of your chart area.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*b4eDKE6ANrWWhwF4ig2cuQ.png)

Use ‘Do not Show for this series’ for both Dummy 4 and Dummy 6

## Step 7: The Magic — Configure Error Bars

Now comes the creative part. For each dummy measure, configure error bars in the **Analytics pane**:

**For Dummy 4 (Consumer segment):**

- **Upper bound**: Consumer Total measure
- **Lower bound**: Dummy measure (0)
- **Color**: Choose Consumer brand color (e.g., blue)
- **Bar width**: 10
- **Border width**: 2
- **Markers**: OFF
- **Error labels**: ON

**For Dummy 5 (Corporate segment):**

- **Upper bound**: Corporate Total measure
- **Lower bound**: Dummy measure (0)
- **Color**: Choose Corporate brand color (e.g., orange)
- **Bar width**: 10
- **Border width**: 2
- **Markers**: OFF
- **Error labels**: ON

**For Dummy 6 (Home Office segment):**

- **Upper bound**: Home Office Total measure
- **Lower bound**: Dummy measure (0)
- **Color**: Choose Home Office brand color (e.g., green)
- **Bar width**: 10
- **Border width**: 2
- **Markers**: OFF
- **Error labels**: ON
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*CVPlXO16DLI09kkn6YXpQg.png)

Use Similar technique for Dummy 5 and Dummy 6

## Step 8: Final Visual Polish

**Hide the Column Elements:**

- Make column colors very light or transparent
- The focus should be entirely on the error bars

**Adjust Error Bar Settings:**

- Ensure all error bars use “Absolute” values, not relative
- Fine-tune colors for brand consistency
- Verify bar widths create the desired visual impact

**Clean Up the Layout:**

- Remove unnecessary chart elements
- Adjust overall chart size for optimal viewing
- Add a clear title explaining the visualization

## The Result: A Clean Segmented Total Bar Chart

What you’ve created is a native Power BI visualization that:

✅ **Shows segment values clearly** without stacking confusion  
✅ **Maintains regional context** through small multiples  
✅ **Enables easy comparison** of segments across regions  
✅ **Uses only built-in Power BI features** — no custom visuals required  
✅ **Remains fully interactive** with standard Power BI functionality

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*I8TZTpP1RiMnsQ3dqhaQSw.png)

End Result

## Final Tips

✅Create a separate text box for the legend  
✅Use a Shape at the bottom of the chart to hide the 0 values of the lower bound of the error bars

## Advanced Tips and Variations

## Dynamic Scaling

For datasets where segment values vary significantly, consider dynamic dummy measures:

```c
Dynamic Dummy = 
VAR MaxSegment = MAX(
    MAX([Consumer Total]),
    MAX([Corporate Total]),
    MAX([Home Office Total])
)
RETURN MaxSegment * 1.1
```

## Color Coding Best Practices

- Use your organization’s brand colors for consistency
- Ensure sufficient contrast between segments
- Consider colorblind-friendly palettes
- Test visibility on different screen types

## Performance Optimization

- For large datasets, consider pre-aggregating at the region level
- Use variables in DAX measures to reduce computation
- Test performance with realistic data volumes

## Why This Approach Works

This Power BI implementation succeeds because it:

1. **Leverages native functionality** — no custom visuals to maintain
2. **Maintains interactivity** — filters and slicers work normally
3. **Scales effectively** — can handle additional segments or regions
4. **Follows Power BI design patterns** — familiar to end users
5. **Provides a clear visual hierarchy** — segments are easily distinguishable

## Limitations and Considerations

As data storytelling expert Brent Dykes notes, segmented total bar charts work best with limited segments — ideally two to four. Beyond this, the visualization can become cluttered.

**Best practices for implementation:**

- Limit to 2–4 segments maximum for clarity
- Ensure sufficient color contrast between segments
- Provide clear legends and contextual information
- Consider alternative visualizations for complex data scenarios
- Test with end users to ensure intuitive understanding

## Community Impact and Future Applications

The Power BI community has embraced creative error bar techniques, with numerous examples shared across professional networks. This demonstrates the platform’s flexibility and the community’s innovative spirit in finding new ways to visualize data effectively.

This technique proves particularly valuable for:

- **Sales analysis** by region and product category
- **Budget vs. actual comparisons** across departments
- **Performance metrics** segmented by business units
- **Customer satisfaction scores** by service areas

## Conclusion

Successfully recreating Kevin Flerlage’s segmented total bar chart in Power BI demonstrates the power of creative thinking within tool constraints. By combining clustered columns, small multiples, and repurposed error bars, we’ve created a compelling alternative to traditional stacked bar charts that addresses their fundamental readability issues.

This project exemplifies how the data visualization community continues to push boundaries, finding innovative solutions within existing tools. The technique provides Power BI users with a native method to create more intuitive and readable segmented visualizations.

Whether you’re presenting to executives, analyzing departmental performance, or exploring customer segments, this approach offers a powerful addition to your Power BI visualization toolkit. The key is always prioritizing clarity and user understanding over visual complexity — the best visualizations make complex data accessible and actionable for decision-makers.

## Now, as promised, here is the PBIX file

***📂*** [*PBIX and Other Useful Links*](https://drive.google.com/drive/folders/1C6HjOKWZfz3-2c-y2zD6EijsawqQ1iY_?usp=sharing)

*Have you tried implementing this technique? I’d love to see your variations and improvements. Share your results and let’s continue pushing the boundaries of what’s possible with native Power BI visualizations.*

**About the Author**: Hi, I’m **Ankan Bandyopadhyay,** a data visualization enthusiast/ Power BI Developer who believes that the best charts are the ones that disappear, leaving only the insights behind. Connect with me on [**LinkedIn**](http://www.linkedin.com/in/bandyopadhyay-ankan) to discuss data storytelling and visualization design.

***If you like my work, then*** [***buy me a coffee***](https://buymeacoffee.com/ankanbandyopadhyay) ***💓***

## References and Inspiration

- [Kevin Flerlage’s original Tableau implementation and blog post](https://www.flerlagetwins.com/2025/04/the-best-alternative-to-stacked-bar.html)
- [Power BI March 2022 feature summary introducing error bars](https://powerbi.microsoft.com/en-in/blog/power-bi-march-2022-feature-summary/)
- Community examples of creative error bar usage in Power BI
- Data visualization best practices from leading industry experts

*The contents of external submissions are not necessarily reflective of the opinions or work of* [*Maven Analytics*](http://mavenanalytics.io/) *or any of its team members.*

*We believe in fostering lifelong learning and our intent is to provide a platform for the data community to share their work and seek feedback from the Maven Analytics data fam.*

[*Submit your own writing here*](https://medium.com/learning-data/how-to-get-your-work-published-by-learning-data-with-maven-analytics-7df21e466a3e?sk=020dfac485597d602e218968d9ffb395) *if you’d like to become a contributor.*

*Happy learning!*

*\-Team Maven*