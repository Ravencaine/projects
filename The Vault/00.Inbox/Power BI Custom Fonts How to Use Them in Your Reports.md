---
title: "Power BI Custom Fonts: How to Use Them in Your Reports"
source: "https://databear.com/power-bi-custom-fonts/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-07-06
created: 2026-08-04
description: "Use custom fonts in Power BI Desktop by editing theme files. Apply corporate branding and know the limitations when publishing reports."
Processed: "Unprocessed"
---
When building branded dashboards, many users wonder if they can use **Power BI custom fonts** in their reports. By default, Power BI Desktop offers a limited font selection, but with a simple theme file edit, you can apply any installed font to align your visuals with corporate branding. This guide explains how to set up Power BI custom fonts and what limitations you should consider when publishing.

If you want to deepen your Power BI expertise, check out this [Power BI training](https://databear.com/power-bi-training/) program for more advanced techniques and hands-on learning.

##### Why Use Custom Fonts in Power BI?

If you work in an enterprise environment or follow a strict corporate style guide, your organization may specify a particular font, such as Lato or another proprietary typeface, that is not included in Power BI’s default list.

Custom fonts help maintain consistent branding across all reports and dashboards. However, Power BI Desktop does not allow you to simply select any installed font from a dropdown menu.

That’s where **theme files** come into play.

##### How to Use Custom Fonts in Power BI Desktop

##### Check the Default Font Options

In Power BI Desktop, select a visual and open the Format pane. Under *Values > Font family*, you will see a dropdown with the available fonts. If your desired font is missing, proceed with the steps below.

##### Edit a Theme JSON File

Download or create a theme JSON file and set the `fontFamily` property to the name of your installed font. For example:

```json
{
  "name": "Custom Lato Theme",
  "textClasses": {
    "title": {
      "fontFamily": "Lato"
    }
  }
}
```

Save the JSON file to your computer.

##### Load the Theme in Power BI

In Power BI Desktop, navigate to *View > Themes > Browse for themes* and select your modified JSON file. The report should now use your specified font.

To verify, you can test with a distinctive font like Algerian or Comic Sans to ensure the change is applied.![Load the Theme in Power BI](99.System/Attachments/Load_the_Theme_in_Power_BI.png)

##### Publishing to the Power BI Service

When you publish the report to the Power BI Service, the custom font will display correctly only if the viewing machine has the font installed. If not, the Service defaults to a standard font.

For enterprise scenarios, this means you may need to ensure the font is deployed to all relevant user machines. On platforms like mobile apps or Macs, the font may not render properly.![Publishing to the Power BI Service](99.System/Attachments/Publishing_to_the_Power_BI_Service.png)

##### Limitations and Considerations

- This method is not officially supported by Microsoft. Use at your own discretion.
- All viewers need the font installed locally for it to display correctly.
- Cross-platform rendering may vary; unsupported devices may not show the custom font.

If you believe custom font support should be officially implemented, you can submit feedback through the Power BI Ideas forum.

##### Tools for Theme File Creation

You can use online tools like PowerBI.Tips Theme Generator to create a base theme file, then manually edit the JSON file to include your chosen font. This speeds up the process while allowing full customization.![Tools for Theme File Creation](99.System/Attachments/Tools_for_Theme_File_Creation.png)

##### Learn More About Power BI

Applying custom fonts is just one way to enhance your Power BI reports and deliver professional, branded dashboards. To improve your skills even further, explore this [Power BI training](https://databear.com/power-bi-training/) resource for in-depth, practical guidance.