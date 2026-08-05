---
title: "More Power to Your Users with Field Parameters in Power BI"
source: "https://medium.com/microsoft-power-bi/more-power-to-your-users-with-field-parameters-in-power-bi-bfa948a315b2"
author:
  - "[[Isabelle Bittar]]"
published: 2023-10-18
created: 2026-07-29
description: "Unlocking Custom Visualizations: From Daily Bitcoin Prices to Multilingual Reports"
Processed: "Unprocessed"
---
## Unlocking Custom Visualizations: From Daily Bitcoin Prices to Multilingual Reports

![](99.System/Attachments/1!F4I1pybJzpIV458L4fY_ug.png.webp)

By KI Data Science

*PBIX file available for download at the end of this article.*

Ever since their debut in May 2022, field parameters have revolutionized the Power BI experience for both developers and consumers. They offer a greater degree of flexibility for report designers, enabling the creation of tailored views and visuals. Meanwhile, report users benefit from a wider array of data analysis options.

Here is an example of some of the cool visualizations that can be created thanks to this new feature. However, there are so many more options. I have even developed translated views in Power BI thanks to this feature. You can read my article **Enhancing Accessibility: Developing Translated Views in Multilingual Power BI Reports** on this [here](https://isabittar.medium.com/enhancing-accessibility-developing-translated-views-in-multilingual-power-bi-reports-5ca20d41217a):

![](99.System/Attachments/0!lk95vEAatDTwuvb0.png.webp)

Enhancing Accessibility: Developing Translated Views in Multilingual Power BI Reports

Building on my latest article **Power Up Your Power BI: Dynamic Color Coding for Bar Charts** (access [here](https://medium.com/p/97493e7cca05)) detailing how to assign colors to bars based on established thresholds, I will demonstrate how you can use field parameters to provide your audience with the capacity of viewing Bitcoin’s average price on a daily, weekly or monthly basis. Our starting point is the following graph:

![](99.System/Attachments/1!gSLGB9RG369S9WVQZ_434g.png.webp)

Starting Point Before Incorporating the Field Parameter

### Step 1: Integrate a Field Parameter

Under the **Modeling Tab**, click on **New parameter** and **select Fields**. A new window named **Parameters** will appear. Here, select the columns `Date`, `Week No.`and `Year & Month`. Click on **Create**.

![](99.System/Attachments/1!Z8TDbjjzF7A2jiNVPohOLQ.png.webp)

Steps to Add a Field Parameter

Once this is completed, a slicer will apear on your active report page, such as below.

![](99.System/Attachments/1!TsRH82EWamKUA872bAsu_A.png.webp)

Field Parameter Slicer

And there you have integrated a field parameter to your report! We will now format it and adjust the graph to provide the desired output.

### Step 2: Format the Slicer of the Field Parameter

Though optional, this step enhances the visual appeal. In the Visualizations pane of the slicer:

1. Opt for the Dropdown style.
2. Deactivate the Slicer header.
3. Employ the Segoe UI Semibold Font for Values.
![](99.System/Attachments/1!18PFvh-IES6PQpBoREBVEA.png.webp)

Steps to Format the Slicer of the Field Parameter

After these adjustments, position the slicer atop the graph. To its right, insert a text box stating: `View the average price:`.

For personalized slicer values, navigate to the calculate table of the Field Parameter. In the formula bar, replace the highlighted text with your preferred titles, such as `Weekly`, `Daily` and `Monthly`.

![](99.System/Attachments/1!sq7AzG2EjvXUD9mS0o4H8Q.png.webp)

Update Parameter Field Slicer Value Names

While the field parameter is not yet connected, the graph should be looking like the following at this point:

![](99.System/Attachments/1!t-lZ6dhLXzs4ZLQoyDnDuA.png.webp)

Graph in Progress

### Step 3: Integrate the Field Parameter to your Graph

In the visualization pane of the graph, drag and drop the `Parameter ` column into the **X-axis**.

![](99.System/Attachments/1!UTu1YOyQ_J9bvFToezwFSQ.png.webp)

This connects the graph to the parameter field, allowing users to sift through daily, weekly, and monthly data visualizations seamlessly.

![](99.System/Attachments/1!d4rzYb279Evkx0DdaHTZQA.png.webp)

Daily View

![](99.System/Attachments/1!ykezz4liAiZfs--MqPAdPQ.png.webp)

Weekly View

![](99.System/Attachments/1!c7bIZsvHgu_2WhbZc2iRXg.png.webp)

Monthly View

### Conclusion

Field parameters in Power BI represent a monumental shift towards personalized and user-centric reporting. By equipping users with the tools to mold data visualizations to their preferences, we not only enhance their experience but also enrich their analytical capabilities. As Power BI continues to evolve, it’s thrilling to ponder the endless possibilities that await. Whether you’re a developer or a consumer, there’s no doubt that these features hold the power to transform your data interaction journey.

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/file/d/1jEiE9KYxCYeNDV6ZQjl15We8G1Irq2lw/view?usp=sharing)**.**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)