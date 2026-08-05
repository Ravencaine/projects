---
title: "Bookmarks in Power BI for Enhanced Report Interactivity"
source: "https://databear.com/bookmarks-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-03-24
created: 2026-08-04
description: "Bookmarks in Power BI are an incredible feature that can significantly enhance the interactivity and user experience of your reports."
Processed: "Unprocessed"
---
### Introduction

Bookmarks in Power BI are an incredible feature that can significantly enhance the interactivity and user experience of your reports. They allow you to create customizable views and scenarios within your Power BI reports, providing a dynamic way to present data insights. In this blog post, we will delve into everything you need to know about bookmarks in Power BI, including how to create them, customize them, and why they are essential for taking your reports to the next level.

### Understanding Bookmarks

A [bookmark in Power BI](https://learn.microsoft.com/en-us/power-bi/consumer/end-user-bookmarks) is essentially a snapshot of a specific configuration of your report page. It captures the current state of filters, slicers, visuals, and other settings, allowing you to save and later present the report in that exact state. For example, if you have a report with sales data by country represented in both pie and bar charts, bookmarks can help you toggle between different views (like focusing on one chart over the other) without manually adjusting the filters and visuals each time.

### Creating a Bookmark in Power BI: A Step-by-Step Guide

Creating bookmarks in Power BI is a straightforward process that can significantly enhance the interactivity of your reports. Here’s a detailed guide on how to create a bookmark in Power BI Desktop:

#### Step 1: Open Your Report in Power BI Desktop

- Start by opening the Power BI Desktop application.
- Load the report file you want to work with. Ensure all the data and visuals are correctly displayed and updated.

#### Step 2: Adjust Your Report View

- Arrange your report to display the exact view you want to bookmark. This step is crucial as the bookmark will capture everything as it appears on the screen at the moment of creation.
- For example, if you’re focusing on sales data by country, you might have a pie chart and a bar chart. If the pie chart is too small and causing category labels to be truncated (indicated by three dots), you might decide to expand it for a clearer view.
- Resize and reposition the visuals as needed. Make sure all relevant information is visible and legible.

![Adjust Your Report View](99.System/Attachments/Adjust_Your_Report_View.png)

#### Step 3: Enable the Bookmarks and Selection Panes

- Go to the ‘View’ tab on the Power BI Desktop ribbon.
- In the ‘Show’ section of the ‘View’ tab, find and check the boxes for ‘Bookmarks’ and ‘Selection’ panes. This action will display both panes on the side of your Power BI window.
	- The Selection Pane allows you to manage the visibility and order of visuals on your report page.
		- The Bookmarks Pane is where you will create, manage, and apply bookmarks.![Enable the Bookmarks and Selection Panes](99.System/Attachments/Enable_the_Bookmarks_and_Selection_Panes.png)

#### Step 4: Create the Bookmark

- With your report view set and the necessary panes open, you can now create the bookmark.
- In the ‘Bookmarks’ pane, click on ‘Add’. This will capture the current state of your report, including the size and position of visuals, applied filters, and any slicer selections.
- The new bookmark will appear in the ‘Bookmarks’ pane, listed as “Bookmark 1” by default. You can rename it by double-clicking on the name and typing a new, descriptive title (e.g., ‘Expanded Pie Chart View’).![Create the Bookmark](99.System/Attachments/Create_the_Bookmark.png)

#### Step 5: Customize and Save the Bookmark

- After adding the bookmark, you can customize it further using the options in the ‘Bookmarks’ pane. For example, you can decide whether the bookmark should save the current data view, display state, or both.
- To finalize the bookmark, ensure all settings are as desired, then click on the ‘Save’ icon (if available) or simply close the bookmarks pane to retain the changes.

### Customization Options for Bookmarks in Power BI

Bookmarks in Power BI not only allow you to save the state of your report but also offer several customization options to enhance the user experience. These options enable you to control what aspects of your report are preserved and how they are displayed when a bookmark is applied. Let’s delve into the three primary customization options for bookmarks: Showing/Hiding Visuals, Data Preservation, and Display Settings.

#### Showing/Hiding Visuals

- **Purpose**: This option lets you control the visibility of different visuals in a bookmarked view. It is useful for focusing the user’s attention on specific parts of the report or simplifying the view to avoid information overload.
- **How to Use:**
	- Open the ‘Selection’ pane alongside the ‘Bookmarks’ pane.
		- In the ‘Selection’ pane, you will see a list of all the visuals present on your current report page.
		- Click the eye icon next to each visual to toggle its visibility. A closed eye means the visual will be hidden in the bookmarked view, while an open eye means it will be visible.
		- After adjusting the visibility settings, update or create the bookmark to save these changes.

![](99.System/Attachments/Showing-Hiding-Visuals1.png)

#### Data Preservation

- **Purpose**: This feature allows you to decide whether the bookmark should save and restore the current filters and slicers’ states. It’s essential for creating interactive reports where the user might want to explore different scenarios or data segments without losing the context of their analysis.
- How to Use:
	- When you create or edit a bookmark, you can choose whether to preserve the data state (including filters and slicers).
		- In the ‘Bookmarks’ pane, select a bookmark, then click on the ellipsis (…) to access options.
		- Ensure the ‘Data’ option is checked if you want to preserve the current filters and slicers in that bookmark. Uncheck it if you want the bookmark to only affect visibility or display settings without changing the data context.

![Data Preservation](99.System/Attachments/Data_Preservation.png)

#### Display Settings

- **Purpose**: These settings allow you to control how certain elements of the report behave when the bookmark is activated. For example, you can decide if activating a bookmark should bring a visual into focus with the ‘Spotlight’ feature or if certain visuals should be selected or deselected.
- **How to Use**:
	- Display settings are managed through the ‘Bookmarks’ pane when editing or creating a bookmark.
		- With the bookmark selected, look for options like ‘Spotlight’ or ‘Selection’ to control these features.
		- Checking these options means that the spotlight or selection state of visuals will be remembered and restored when the bookmark is applied.

![Display Settings](99.System/Attachments/Display_Settings.png)

### Integrating Interactive Elements with Bookmarks in Power BI

Interactive elements like buttons can significantly enhance the navigation and usability of Power BI reports, especially when combined with bookmarks. These elements allow users to switch between different views or states of the report seamlessly. Here’s how to integrate interactive elements with bookmarks in Power BI:

#### Adding and Configuring Buttons

- **Add Buttons to Your Report**
	- Navigate to the ‘Insert’ tab in Power BI Desktop.
		- Select ‘Button’ and choose the type of button you want to add, like a blank button or one with a specific icon.
		- Place the button on your report canvas and resize it as needed.
- **Label Buttons**
	- With the button selected, go to the ‘Visualizations’ pane.
		- Under the ‘Button text’ section, enter the label for the button (e.g., ‘Bar Chart’, ‘Pie Chart’).
		- Customize the font, color, and alignment to make the button visually appealing and consistent with your report’s design.
- **Assign Bookmarks to Buttons**
	- Select the button, then go to the ‘Format’ pane and find the ‘Action’ section.
		- Turn on the ‘Action’ option and select ‘Bookmark’ from the dropdown menu.
		- Choose the bookmark that corresponds to the view or state you want this button to activate.

![Assign Bookmarks to Buttons](99.System/Attachments/Assign_Bookmarks_to_Buttons.png)

#### Advanced Bookmark Features

- **Grouping Bookmarks**
	- Grouping related bookmarks can simplify navigation and organization within your report.
		- To group bookmarks, select multiple bookmarks in the ‘Bookmarks’ pane (use Ctrl or Shift to select more than one), right-click, and choose ‘Group’.
		- Name the group appropriately for easy identification.

![Grouping Bookmarks](99.System/Attachments/Grouping_Bookmarks.png)

- **Bookmark Navigator**
	- The Bookmark Navigator is a powerful tool for creating a more dynamic and integrated user experience.
		- To add a Bookmark Navigator, go to the ‘Insert’ tab and select ‘Buttons’, then choose ‘Bookmark Navigator’.
		- This navigator will automatically create a panel with buttons for each bookmark, or grouped bookmarks, allowing users to easily cycle through the different views.
- ![Bookmark Navigator](99.System/Attachments/Bookmark_Navigator.png)

### Conclusion

Bookmarks in Power BI are a powerful tool to enhance the interactivity and user-friendliness of your reports. By effectively utilizing bookmarks, you can provide a dynamic and engaging experience for your users, making it easier to explore and interact with the data. Whether you’re presenting sales trends, financial forecasts, or market research, mastering bookmarks will undoubtedly elevate your Power BI reporting game.

Hope this blog post has given you a understanding of how to use bookmarks in Power BI. Should you have any inquiries or require additional clarification, please don’t hesitate to visit our [training page](https://databear.com/power-bi-training/) for more resources and support.