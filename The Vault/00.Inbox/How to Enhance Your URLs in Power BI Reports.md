---
title: "How to Enhance Your URLs in Power BI Reports"
source: "https://databear.com/urls-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-06-02
created: 2026-08-04
description: "In today's post, we will explore various ways you can utilize URLs in your Power BI reports."
Processed: "Unprocessed"
---
In today’s post, we will explore various ways you can utilize URLs in your Power BI reports. Adding hyperlinks to your Power BI reports is a powerful method to provide additional resources and insights to your users, linking them to external sites, documentation, and more. This feature can significantly enhance the user experience by enabling seamless access to valuable information.

In this post, we’ll walk you through the steps to set up [URLs in Power BI](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-hyperlinks-in-tables?tabs=powerbi-desktop) and demonstrate some creative ways to use them, including creating dynamic URLs and using them to open your email client. Let’s dive in!

### Why Use URLs in Power BI Reports?

Adding hyperlinks to your Power BI reports allows you to:

- **Provide Additional Resources**: Link to external documentation, websites, or other resources that can provide more context or detailed information.
- **Enhance Interactivity**: Make your reports more interactive by allowing users to easily access relevant web pages with a single click.
- **Simplify Navigation**: Direct users to specific sections of your website or external tools, improving the overall user experience.

### Basic URL Setup in Power BI

#### Step 1: Creating a Basic URL Link

1. **Add URL to a Column**: Start by ensuring you have a column in your dataset that contains the full URLs you want to link to.
2. **Change Data Category**: Select the column in your data model, go to the “Modeling” tab, and change the data category to “Web URL”. This will format the text as clickable links.

#### Example

Imagine you have a list of boroughs in London with their respective URLs. By converting the column containing these URLs into a “Web URL” data category, Power BI will display these as clickable links in your report.

![Creating a Basic URL Link URLs in Power BI Reports](99.System/Attachments/Creating_a_Basic_URL_Link_URLs_in_Power_BI_Reports.png)

### Using URL Icons in Tables and Matrices

To make your URLs more visually appealing:

1. **Use URL Icons**: Instead of displaying the full URL, you can toggle the “URL icon” option in the table’s formatting settings. This will replace the full text with a clickable link icon.
2. **Conditional Formatting**: Apply conditional formatting to integrate URLs within other columns, such as names. This makes the URLs blend seamlessly into your report’s design.

![Using URL Icons in Tables and Matrices](99.System/Attachments/Using_URL_Icons_in_Tables_and_Matrices.png)

### Creating Dynamic URLs in Power BI

Dynamic URLs are useful when you need to construct URLs based on data in your report. For instance, if you only have the relative paths and need to create full URLs dynamically:

1. **Create a Measure**: Use DAX to create a measure that concatenates the root URL with the relative path.
	DAX
	`Link = "https://example.com/" & MAX(Table[RelativePath])   `
2. **Change Data Category**: Again, set the data category of this measure to “Web URL”.

### Using Buttons, Shapes, and Images in Power BI

You can also add URLs to various visuals like buttons, shapes, and images to create interactive elements in your reports:

1. **Insert a Button**: Go to the “Insert” ribbon and choose a button. Enable the “Action” property and set it to “Web URL”.
2. **Conditional Formatting**: Use the link measure you created to ensure the button dynamically redirects to the correct URL based on the data context.

### Adding URLs to Text Boxes in Power BI

While you can’t dynamically create URLs in text boxes, you can still add static hyperlinks:

1. **Insert a Text Box**: Add a text box to your report and type your desired text.
2. **Insert Link**: Highlight the text you want to turn into a link, click the link icon, and enter the URL.

![Screenshot of a text box, highlighting the hyperlink field.](99.System/Attachments/Screenshot_of_a_text_box,_highlighting_the_hyperlink_field.png)

### Using URLs to Open Mail Clients in Power BI

You can also create mailto links that open the user’s email client with a pre-filled email address:

1. **Create a Mailto Measure**: Use DAX to create a measure that prefixes email addresses with “mailto:”.
	DAX
	`MailTo = "mailto:" & MAX(Table[Email])   `
2. **Change Data Category**: Set this measure’s data category to “Web URL”.

### Conclusion

Adding URLs in Power BI reports is a simple yet powerful way to enhance their functionality and interactivity. Whether you are linking to external resources, creating dynamic links, or enabling email functionality, URLs can significantly improve the user experience of your reports.

Thank you for reading! If you found this post helpful, make sure to check out our [training page](https://databear.com/power-bi-training/) for more tips, tricks, and best practices on Power BI. Our training page offers a wealth of resources to help you master Power BI and make the most of its powerful features.