---
title: "Design Meets Data: A Guide to Building Engaging Power BI Report Navigation"
source: "https://medium.com/microsoft-power-bi/design-meets-data-a-guide-to-building-engaging-power-bi-report-navigation-d7cca15def4c"
author:
  - "[[Ethan Guyant]]"
published: 2024-10-02
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Streamlined report navigation with built-in tools to achieve functional, maintainable, and engaging navigation in Power BI reports.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VQd3qtuS1dX2gnLx_lWxdA.png)

Before we begin developing the navigational element of our reports, we must decide what tools to use. The Design Meets Data series started with two previous posts in which we explored two approaches: using Figma to design and customize our navigation and using Power BI’s built-in shapes, bookmarks, and buttons to create a similar experience with native tools.

## [Design Meets Data: A Guide to Building Interactive Power BI Report Navigation](https://medium.com/microsoft-power-bi/design-meets-data-a-guide-to-building-interactive-power-bi-report-navigation-1ce2046282f9?source=post_page-----d7cca15def4c---------------------------------------)

### From Sketch to Screen: Bringing your Power BI report navigation to life for an enhanced user experience.

medium.com

## [Design Meets Data: Crafting Interactive Navigations in Power BI](https://medium.com/@emguyant/design-meets-data-crafting-interactive-navigations-in-power-bi-1779593e65ad?source=post_page-----d7cca15def4c---------------------------------------)

### User-Centric Design: Next level reporting with interactive navigation for an enhanced user experience.

medium.com

This post will explore using Power BI’s Page Navigator to simplify our navigation setup. Each approach has its own level of flexibility and ease of maintenance, so it’s important to choose the right method based on the project’s requirements.

## The Power BI Page Navigator

Power BI’s Page Navigator lets us create a dynamic and interactive navigation menu in our reports. It is an out-of-the-box solution that simplifies the navigation experience.

Since the Page Navigator is a native feature, it requires minimal setup and automatically adjusts when new pages are added to the report. However, some adjustments may still be needed, such as resizing or formatting changes to accommodate report updates.

To add a Page Navigator to our report, we go to the Insert tab in Power BI Desktop, then select Navigator > Page navigator under the Buttons dropdown.

**Customization Options**

Power BI provides various options to customize the appearance of our Page Navigator, such as changing the font, colors, shapes, borders, and even what pages are listed. This allows us to create a navigational element that fits seamlessly within our report’s aesthetic.

Although the design flexibility is not as extensive as in our previous example using Figma, the Page Navigator option strikes a balance between ease of use and visual appeal.

## Building the Navigation Pane

Now that we have covered the basics of the Page Navigator, we can begin building the navigation pane for our report. The navigation pane will be located on the left-hand side of our report and will serve as both the page navigation and container for our page slicers.

Below, is the final product. Follow the detailed step-by-step guide provided to create your own navigation pane

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*_c7C3CJZHIpyVmHB)

## Building the navigation pane

We begin building the navigational pane on the left-hand side of our report canvas. First, we add a rectangle to the report canvas and style it to meet our needs. The navigation pane has a height equal to the report canvas and a width of 140. We set the fill color to dark blue, which is our Theme 1, 50% darker.

Next, we add a rectangle at the top of the navigation pane to provide an accent and space for displaying an organizational logo within our report. This rectangle has a height of 40 and a width of 140, and its fill color is set to the accent color of our report theme.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*AVj-EoijNkpf3JHf)

With the basic structure of our navigation pane in place, we then move on to adding the Page Navigator.

## Formatting the Page Navigator

We begin by selecting the Insert tab on the main ribbon. Then, under the Button dropdown, select Navigator > Page navigator.

Once the Page Navigator is added to the report canvas, go to the Format pane and select Vertical from the Orientation dropdown under the Grid layout property.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*kgOnMOG27ttyKYc1)

Under the Pages property, we find options to control what pages are displayed within our report navigation. In the Options group, we can set general options such as Show hidden pages, Show tooltip pages, and Show all by default. Additionally, in the Show group, we can explicitly set which pages are shown in the navigation by using the toggles next to each report page.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*-GJhERdaTxqG3ihG)

Once our navigation displays the required pages, we adjust the width of the navigator object to 130 and the height to 105. Note that the height should be adjusted based on the number of pages in the navigation. In this example, we use a basic calculation to calculate the height by multiplying the number of pages by 35 ( 3 pages x 35 = 105).

Lastly, we set the horizontal position of the navigator object to 10 and the vertical position to 100.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*8nBJubU4ZOcGtsnd)

## Styling the Page Navigator

Once we finish the basic formatting, we customize the navigator to match the look of our report. Our aim with the styling is to make it easier to identify the current page.

We do this by adjusting the Style properties of the Page Navigator and using the Apply settings to State dropdown.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*T35LFwhQX52lC37A)

Below are the key differences between our page navigator's Default, Hover, Press, and Selected states.

**Default**  
Text > Font: Segoe UI  
Text > Font Color: light blue, Theme color 1, 60% lighter  
Text > Horizontal alignment: left  
Text > Padding: left 5 px  
Fill > Color: dark blue (#06435F)  
Border: off  
Shadow: off  
Glow: off  
Accent bar: off

**Hover**  
Text > Font: Segoe UI Semibold  
Text > Font Color: white  
Text >Horizontal alignment: left  
Text> Padding: left 5 px  
Fill > Color: dark blue, Theme color 1, 25% darker  
Border: off  
Shadow: off  
Glow: off  
Accent bar: off

**Press**  
Text > Font: Segoe UI Semibold  
Text > Font Color: dark blue, Theme color 1, 50% darker  
Text >Horizontal alignment: left  
Text> Padding: left 5 px  
Fill > Color: white  
Border: off  
Shadow: off  
Glow: off  
Accent bar: off

**Selected**  
Text > Font: Segoe UI Semibold  
Text > Font Color: dark blue, Theme color 1, 50% darker  
Text >Horizontal alignment: left  
Text> Padding: left 5 px  
Fill > Color: white  
Border: off  
Shadow: off  
Glow: off  
Accent bar > Position: right  
Accent bar > Color: accent green (#6CBE4B)  
Accent bar > Width: 6px

After configuring all the styling options, our report page will have an engaging and interactive navigation panel.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*pVDOP3V0xVdkoWVS)

## Comparing the Approaches

When building a navigational component within our reports, we have a wide variety of options and approaches to choose from. Each report has unique requirements, so it’s important to compare and contrast these different approaches based on performance, ease of maintenance, and design flexibility.

**Performance Comparison**

[Figma](https://medium.com/microsoft-power-bi/design-meets-data-a-guide-to-building-interactive-power-bi-report-navigation-1ce2046282f9): Our Figma-based designs require importing images into Power BI. This can improve the load time of our reports because the report does not have to render each shape and component independently.

[Power BI Native Shapes and Buttons](https://ethanguyant.com/2024/05/07/design-meets-data-crafting-interactive-navigations-in-power-bi/): This option has the advantage of only requiring our development work to occur in Power BI. However, each shape and component added to build our navigation pane has to be loaded each time our report page is viewed.

Page Navigator: This offers a fully integrated approach with minimal overhead. However, we lose full control over design and aesthetics.

**Ease of Maintenance**

[Figma](https://ethanguyant.com/2024/02/15/design-meets-data-a-guide-to-building-interactive-power-bi-report-navigation/): Our Figma-based approach is the most complex to maintain. Every design update requires going back to Figma, redesigning, re-exporting from Figma, and re-importing and integrating into our Power BI report.

[Power BI Native Shapes and Buttons](https://ethanguyant.com/2024/05/07/design-meets-data-crafting-interactive-navigations-in-power-bi/): This approach has the advantage of only using Power BI to maintain our navigational element but still requires manual updates when adding or removing pages from our report.

Page Navigator: This is the easiest option to maintain because the page navigator updates with any page additions or changes. However, the size of the object may still need to be adjusted.

**Design Flexibility**

[Figma](https://ethanguyant.com/2024/02/15/design-meets-data-a-guide-to-building-interactive-power-bi-report-navigation/): Offers the highest level of design customization. We can create any design we can think up, however, this comes with added complexity and time requirements.

[Power BI Native Shapes and Buttons](https://ethanguyant.com/2024/05/07/design-meets-data-crafting-interactive-navigations-in-power-bi/): Provides us more flexibility than the page navigator, allowing us to customize our design and layout. However, we may still encounter design limitations depending on the options provided by Power BI.

Page Navigator: The most straightforward to implement but offers limited customization options, which restricts design flexibility. It prioritizes ease of maintenance over complex designs.

## Final Thoughts

Deciding on the proper navigation for our Power BI reports depends on balancing design flexibility, ease of maintenance, and performance. Leveraging Figma allows for fully custom designs but comes with more complex maintenance. Power BI offers various native tools to help design navigational elements, although building a custom navigational pane will still require manual updates. Power BI’s Page Navigator stands out for its simplicity, dynamic updating, and minimal maintenance effort. However, the cost of the simplicity is limited customization and design flexibility.

The Design Meets Data series explored three approaches to building a Power BI report navigational pane.

## [Design Meets Data: A Guide to Building Interactive Power BI Report Navigation](https://medium.com/microsoft-power-bi/design-meets-data-a-guide-to-building-interactive-power-bi-report-navigation-1ce2046282f9?source=post_page-----d7cca15def4c---------------------------------------)

### From Sketch to Screen: Bringing your Power BI report navigation to life for an enhanced user experience.

medium.com

## [Design Meets Data: Crafting Interactive Navigations in Power BI](https://medium.com/@emguyant/design-meets-data-crafting-interactive-navigations-in-power-bi-1779593e65ad?source=post_page-----d7cca15def4c---------------------------------------)

### User-Centric Design: Next level reporting with interactive navigation for an enhanced user experience.

medium.com

There are seemingly endless other approaches to creating this critical part of our Power reports. How do you approach your report’s navigation?

**Thank you for reading! Stay curious, and until next time, happy learning.**

And, remember, as Albert Einstein once said, “Anyone who has never made a mistake has never tried anything new.” So, don’t be afraid of making mistakes, practice makes perfect. Continuously experiment, explore, and challenge yourself with real-world scenarios.

If this sparked your curiosity, keep that spark alive and check back frequently. Better yet, be sure not to miss a post by subscribing! With each new post comes an opportunity to learn something new.

## [Don't miss a story!](https://medium.com/@emguyant/subscribe?source=post_page-----d7cca15def4c---------------------------------------)

medium.com

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----d7cca15def4c---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee