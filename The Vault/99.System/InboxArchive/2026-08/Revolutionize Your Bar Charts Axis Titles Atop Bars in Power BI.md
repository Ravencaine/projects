---
title: "Revolutionize Your Bar Charts: Axis Titles Atop Bars in Power BI"
source: "https://medium.com/microsoft-power-bi/revolutionize-your-bar-charts-axis-titles-atop-bars-in-power-bi-ca77edbd97e"
author:
  - "[[Isabelle Bittar]]"
published: 2023-09-20
created: 2026-08-02
description: "A Fresh Perspective on Data Visualization for Compact Dashboards"
Processed: "Unprocessed"
---
## A Fresh Perspective on Data Visualization for Compact Dashboards

![](99.System/Attachments/1!NVGjAzZ8dSCBC6GCeRrpTw.png.webp)

By KI Data Science

### Introduction

Sometimes, the traditional layout of charts can be limiting, especially when working with compact dashboards or when looking to give a fresh look to your reports. An interesting modification is to place axis titles directly on top of the bars in a bar chart. Here’s a guide, inspired by Bas from How To Power BI, that’ll walk you through this approach using Power BI.

### Dataset Overview

For the purpose of this example, we will be using data sourced from the [Quebec Ministry of Education Portal](http://www.education.gouv.qc.ca/fileadmin/site_web/documents/Postes-pourvoir-11-septembre-2023.pdf) on vacant teaching positions in the Quebec province of Canada.

Below is a quick glimpse of what our primary data table comprises:

![](99.System/Attachments/1!qj1kNg3E10gJ7oFiy_LyeQ.png.webp)

### Steps to Customize Your Bar Chart

### 1\. DAX Measure for Vacant Positions

Begin by defining a measure to calculate the total number of vacant positions. Add this measure to the Clustered bar chart visual with “Regions” as the Y-axis.

```c
Vacant positions = SUM('Postes vacants'[Valeur])
```
![](99.System/Attachments/1!-1SRB31NL4adF1Ec_Y-N4w.png.webp)

### 2\. Disable Default Axes

To give us room to showcase the customized axis titles, turn off both the Y-axis and X-axis. With this setup, our data labels will be the primary text presenters.

![](99.System/Attachments/1!LIjQPudoAhaGW2-RlTvFfQ.png.webp)

### 3\. Creating Space for Custom Titles

To create a spacing within our bar chart for inserting custom titles, define a DAX measure named “Empty”:

```c
Empty = 0
```

Subsequently, integrate this measure into the X-axis of your visual.

![](99.System/Attachments/1!YhD8hB5YDyyk6wvc2IViIQ.png.webp)

### 4\. Designing Custom Data Labels

To juxtapose the axis value with its related data, devise another DAX measure:

```c
Data label = 
VAR _Region = SELECTEDVALUE('Postes vacants'[Région administrative])
RETURN _Region &": " & [Vacant positions]
```

This measure fetches the name of the region and combines it with the number of vacant positions. Now, associate this measure with the “Empty” series you created. Toggle on the “Custom label” option, and then insert this measure into the “Field”.

![](99.System/Attachments/1!Dj1hA2qnnRNkNxSKfrMf2A.png.webp)

### 5\. Optimizing the Visual

Depending on the density of your data and your design preferences, you may need to adjust certain visual settings for better clarity and aesthetics:

- **Inner Padding**: Modifying this determines the space between individual bars.
- **Minimum Category Width**: Altering this affects how broad or narrow your bars appear. Experiment with these parameters until your data is showcased in a manner that’s both visually pleasing and clear to the audience.
![](99.System/Attachments/1!EP3lJimV9QRrr8diJBa7wg.png.webp)

### Conclusion

With these steps, you’ve transformed a standard bar chart into a more concise and innovative visual representation. This style can be especially effective for dashboards with spatial constraints or when aiming for a distinctive aesthetic appeal. Always remember, while aesthetics are essential, clarity remains paramount. Adjust the settings to ensure your audience understands the data you’re presenting.

To view how to dynamically create titles and subtitles for charts, you can see the step-by-step guide [here](https://isabittar.medium.com/elevate-your-power-bi-bar-charts-with-6-simple-improvements-70f88be53d10).

### Source

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)