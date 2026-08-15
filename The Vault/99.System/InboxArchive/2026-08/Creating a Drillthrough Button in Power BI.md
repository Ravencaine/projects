---
title: "Creating a Drillthrough Button in Power BI"
source: "https://databear.com/create-a-drillthrough-button-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2023-06-03
created: 2026-08-04
description: "Learn how to optimize your data analysis in Power BI using the drillthrough button. Explore the step-by-step guide to creating drillthrough pages, navigating through reports with ease, and gaining valuable insights into specific values."
Processed: "Unprocessed"
---
All functions in Power BI are designed to improve work efficiency and effectiveness, and the drillthrough is no exception. It simplifies navigation through a report by allowing you to jump from one page to another with just a few clicks. With the drill through button, you can select specific values in a visual and drill through to a different page that provides detailed information about those values.

## How to drillthrough a Page in Power BI

There are two ways to drillthrough a report in Power BI: by right-clicking on the visual or by creating a drillthrough button. The button not only increases the likelihood of finding essential drill through scenarios but also allows you to customize the appearance and functionality of the buttons.

## Why drillthrough a page in Power BI?

To create a drillthrough button, you must establish a valid drillthrough page in your report. After creating the page, create a button using drillthrough as the action type and defined page as the destination.

To illustrate this Power BI function, we shall use the Zebra BI Sales dashboard, which has drillthrough already integrated into it. This report has two ways of navigating from the main page to the other page.

On the landing page, you could right-click the category (mobile) and then select the desired drill-through page, which in this case, is the country, as shown below.

![Create a drillthrough button in Power BI](99.System/Attachments/Create_a_drillthrough_button_in_Power_BI.png)

Alternatively, you can create a drillthrough button manually and then use it; whichever option you select, you will always land on the selected destination, which shows the details for the selected values, and this makes it easy to analyze and determine the source of the negative or positive variance in the report.

## Add a new page to the report for the drillthrough.

Add a page by using the + icon. Also, you have to rename the report and hide it; this ensures that the user can only access it using the drill-through function and not by selecting it from the list of available pages.

![Create a drillthrough button in Power BI](99.System/Attachments/Create_a_drillthrough_button_in_Power_BI.png)

Use the prefix (DT) to the table’s name, to indicate the dimension used. It makes it easy to find the page in a report.

![Create a drillthrough button in Power BI](99.System/Attachments/Create_a_drillthrough_button_in_Power_BI.png)

## Add visuals to the page.

After creating the page, adding visuals and designing it as you desire is easy. In this case, we have added a Zebra BI Sales table that compares actual and plans data per salesperson as illustrated below.

![Add visuals to the page.](99.System/Attachments/Add_visuals_to_the_page.png)

## Define the dimension for the drillthrough page

After adding visuals, you have to establish the dimensions for which the page will drillthrough. The dimensions can be added to the drill-through filters in the page settings. It is important to note that adding the fields automatically creates a back button.

![Create a drillthrough button in Power BI](99.System/Attachments/Create_a_drillthrough_button_in_Power_BI-1.png)

## Functional drillthrough button on the page.

The drillthrough page has now been successfully created, as illustrated below. The selected value on the landing page, which is (-30), is also the total shown on the drillthrough page. The difference is that the drill through page is split by the salesperson.

![Create a drillthrough button in Power BI](99.System/Attachments/Create_a_drillthrough_button_in_Power_BI.gif)

## Conclusion

The drill-through function in Power BI allows for seamless navigation between pages. Providing users with detailed insights and analysis of specific values. By using right-click or drill-through buttons, you can easily explore relevant information in your report. By following the steps outlined in this guide, you can effectively utilize the drill-through function in Power BI.

You can visit the rest of our [blog](https://databear.com/blog/) posts for more insightful information on everything related to Power BI.

Learn more about Power BI by taking our training [course](https://databear.com/power-bi-training/).