---
title: "Share Selected Power BI Report Pages with Specific Users"
source: "https://databear.com/share-selected-power-bi-report-pages-with-specific-users/"
author:
  - "[[Belinda Loseby]]"
published: 2023-06-18
created: 2026-08-04
description: "Learn how to share separate selected Power BI report pages with specific users through an App utilizing dashboards."
Processed: "Unprocessed"
---
## Sharing Specific Report Pages in Power BI through an App Dashboard.

In this article, we will delve into the topic of how to share selected Power BI report pages with specific users, using an App dashboard. When it comes to granting access to specific user groups, it can pose some challenges. However, fear not, as we will explore various workarounds. Our primary focus will be on an approach that entails developing an app utilizing dashboards, allowing users to effortlessly connect to specific reports that are relevant to them.

## Creating Separate Dashboards for User Groups

As an example, let’s consider a report with four pages. In this scenario, one user (user1) will have access to all pages and another user (user2) will have access to only the KPI’s Overview page.

![Example of hidden report pages](99.System/Attachments/Example_of_hidden_report_pages.png)

hidden report pages

Firstly, create a separate dashboard for each group of users. In our example, we have created two dashboards, one for user1 and another for user2. [You can learn how to create dashboards from reports in Power BI here](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-create).

![Image of Separate Dashboards listed](99.System/Attachments/Image_of_Separate_Dashboards_listed.png)

Separate Dashboards listed

Now we will use the tiles in each of the dashboards to link back to the report pages. In each Dashboard, create a separate tile for every report page you want to share through that dashboard, as follows:

1. While the dashboard is open, click **Edit** -> **Add tile**.
![Image of Editing a dashboard and adding a tile](99.System/Attachments/Image_of_Editing_a_dashboard_and_adding_a_tile.png)

Add a tile to a dashboard

2. Select “ **Image** ” as the source.
![Image of Selecting an image as a source for a tile](99.System/Attachments/Image_of_Selecting_an_image_as_a_source_for_a_tile.png)

Select image as source for a tile

The next step is to set up the Tile details:

3. Add a link to a related picture so that the user can easily understand the meaning of the tile;
4. Add a link that will lead to the report page.
5. Press Apply
6. Follow these steps for each of the report pages to be represented on this dashboard.
![Image of Details dialog](99.System/Attachments/Image_of_Details_dialog.png)

Tile Details dialog

As a result, we have a dashboard with four tiles for user1 with full access and a dashboard with only one tile for user2 with access to the first page only.

![Image showing User1 dashboard with four tiles to select report pages](99.System/Attachments/Image_showing_User1_dashboard_with_four_tiles_to_select_report_pages.png)

User1 dashboard with four tiles to select report pages

![Image showing User2 dashboard with one tile to select report page](99.System/Attachments/Image_showing_User2_dashboard_with_one_tile_to_select_report_page.png)

User2 dashboard with one tile to select report page

## Creating the App and Customizing the Audience Groups

Now it’s time to create the app. The app will include the two dashboards we just created and the report itself. [Learn how to create and publish an app in Power BI here.](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps)

1. The key step here is to set up the audience. We can create as many audience groups as needed. In this example, we create two audience groups. Each group will see only the visuals that we assign to them.  
	*Note that the report itself will be hidden from every group.*
![Image showing screenshot of selecting an audience when creating an App](99.System/Attachments/Image_showing_screenshot_of_selecting_an_audience_when_creating_an_App.png)

Selecting an audience when creating an App

2. You can hide and show specific app elements for every audience group by clicking on the eye icon.
![Image showing how to hide App elements](99.System/Attachments/Image_showing_how_to_hide_App_elements.png)

How to hide reports or App elements

## Granting Users Access to the Report

1. After creating the app and setting up the audience, you should also give users access to the report itself. [Learn how to give users access to reports here](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-request-access).  
	This allows users to access the content by clicking on the tiles in the dashboards.  
	**Note: Once you grant access to the report for users, they will have access not only to the app we created but also to the entire report. This is not the behaviour we are looking for, on the contrary, we want to limit access to show only specific pages.**
2. To overcome this drawback, we hide all pages in the report and leave only one page. This page could be a blank page where you can add some information to be shown.
![Image showing a report with hidden report pages](99.System/Attachments/Image_showing_a_report_with_hidden_report_pages.png)

Report with hidden report pages

And that’s it! Now your users have access to only specific pages of your report through the app. The only way the user can access the report is by selecting the tile in the dashboard which they have access to.

NOTE: When we share selected Power BI report pages with specific users this way, it is not entirely secure. For instance, if both user1 and user2 have no [Row Level Security](https://databear.com/dynamic-row-level-security-in-power-bi/) enabled, and user1 shares the link to a report with user2, the latter will gain access to user1’s report. Therefore, it remains crucial to establish the appropriate security levels at the database level.

![Image showing a report in App with hidden report pages](99.System/Attachments/Image_showing_a_report_in_App_with_hidden_report_pages.png)

Report in App with hidden report pages