---
title: "Deep dive into modern visual defaults and formatting your entire report (Preview)"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-modern-visual-defaults-and-formatting-your-entire/ba-p/5303513?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-07-21
created: 2026-08-08
description: "With the preview of modern visual defaults, your reports have a clean modern look following the fluent 2 design system out of the box. Create your"
Processed: "Unprocessed"
---
With the preview of modern visual defaults, your reports have a clean modern look following the fluent 2 design system out of the box. Create your visuals on a fresh report page and rely on us to start you out with polished visuals and presets to quickly get your job done on your data in your semantic model, whether it’s created locally or you live connect to one already available to you in the Power BI service.

We’ve also taken this one step further! With report themes, you can quickly style across all your visuals and report pages instead of updating each visual in its formatting pane. The new **Customize theme** formatting pane lets you make report-wide changes and see the impact immediately. When no visuals are selected on your page, a third tab appears that lets you **customize your report theme**. With on-object interaction preview enabled, you’ll find the following settings in the **customize theme** pane:

- **Theme settings**: Import, export, remove a custom theme and specify the base theme for your report.
- **Colors**: Brand the report to your colors so the color picker has the colors you need, no matter where you are formatting and includes built-in color palettes to choose from to quickly get you going.
- **Text**: Style the title, callout, label, and general text across your report instead of visual by visual, including new visuals added later.
- **Visual properties**: Add borders, corner rounding, shadow, background, padding, and even style header icons and tooltips for all new and existing visuals at once.
- **Page**: Define your new page size and adjust wallpaper and background settings for the entire report instead of page by page, while leaving any page specific updates alone.
- **Filter pane** and **Filter cards**: Get the exact look you want for your filter pane across your report, matching the per page settings.

When updates to the visual defaults become available, existing reports won't automatically pick them up. To apply the latest defaults to your report, select Update theme at the top of the pane. Especially during preview, and as part of report maintenance, be sure to check for the latest updates and apply them.

![DataZoe_0-1784310957494.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355873i62FB560BC3F18384/image-size/large?v=v2&px=999 "DataZoe_0-1784310957494.png")

*Figure: The Customize theme pane showing a notification that an updated base theme is available, with the option to apply the latest default styles.*

All these settings become the new visual default across your report. New visuals use these styles automatically and resetting a visual to its default formatting applies them as well. You can then focus visual-specific formatting only where it’s needed, while keeping everything else consistent and making future style updates easier.  

## Let’s walk through customizing your report theme

![DataZoe_1-1784311036466.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355874iC87F455E496C942B/image-size/large?v=v2&px=999 "DataZoe_1-1784311036466.png")

*Figure: A Power BI report showcasing bar chart variations, with the Customize theme pane highlighted in the Visualizations panel.*

The **theme settings** section lets you name your customizations and import or export the custom report json file. You can continue editing in your favorite code editor, such as VS code with Copilot, using the [custom report schema file](https://github.com/microsoft/powerbi-desktop-samples/tree/main/Report%20Theme%20JSON%20Schema) to help. You can also remove the custom theme and pick any base theme you need, which may be helpful for older custom theme json files. If you want to keep the base theme selection instead of always using the latest when you import the custom theme in another report, be sure to toggle on the Save base theme selection in custom theme option.  

![DataZoe_2-1784311071127.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355875iFA13DE8E8C769E73/image-size/medium?v=v2&px=400 "DataZoe_2-1784311071127.png")

*Figure: The Theme settings pane with the menu to import a custom report theme.*

The **Colors** section brings the most exciting update. Many previously built-in themes were simply color palettes. These color palettes can now be applied to any customizations you have made, theme you imported, or simply the visual defaults. Open the dropdown, preview the available color palettes, and pick one update your report instantly!

![DataZoe_3-1784311105754.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355876iA61EBC7865EBC072/image-size/large?v=v2&px=999 "DataZoe_3-1784311105754.png")

*Figure: A Power BI report with the Storm color palette selected in the report theme’s Colors settings.*

And you can adjust any **data color,** **structural color,** **sentiment color**, or **divergent color**. If you’re using the **Storm** color palette, for example, but one of the sentiment colors is a bit too dark, you can simply adjust it in the pane and all instances in the report are updated at once.

![DataZoe_4-1784311133913.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355877iF941AA18513AE239/image-size/large?v=v2&px=999 "DataZoe_4-1784311133913.png")

*Figure: The Colors settings pane with a custom color palette and divergent color options.*

You don’t have to adjust it visual by visual if they use the default formatting. If you format a visual in its formatting pane, that is unimpacted by the changes you make in the custom theme.

If you want to adjust the text styles across the report, use the **text** section to adjust all the titles to be a darker data color and different font and size. Make one change and all the visuals in the report, including any created afterward, inherit these styles. Easy to apply and easy to remove with the **Reset to base theme** at the bottom of the section.

![DataZoe_0-1784311233706.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355878iB9EBB2CF0DEA518A/image-size/large?v=v2&px=999 "DataZoe_0-1784311233706.png")

*Figure: The Text settings pane with report-wide title font, size, and color options.*

Now we get into the **visual properties** section where you can impact common visual properties, such as background, border, header icons, tooltip styling, shadow, and even the padding within the visuals. You can build a uniform, professional look in just a few steps!

![DataZoe_0-1784311316455.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355880iE67169B67EEA2AE7/image-size/large?v=v2&px=999 "DataZoe_0-1784311316455.png")

*Figure: The Visual properties settings pane with options for backgrounds, borders, header icons, tooltips, shadows, and visual padding.*

Next up are the page settings. You can now set the default size of new pages in your report. You can also adjust the background, wallpaper color, and transparency across all pages!

![DataZoe_1-1784311348932.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355881iA550328B7BE90B65/image-size/large?v=v2&px=999 "DataZoe_1-1784311348932.png")

*Figure: The Page settings pane with options to configure canvas size, page background, wallpaper color, and transparency.*

The size you specify becomes the new default, so even existing pages can be updated by resetting them to the default size.

Formatting the filter pane for all the pages in your report is also new, with all the same formatting options you have for individual pages.

![DataZoe_2-1784311380666.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355882i4EBE427B418C24A7/image-size/large?v=v2&px=999 "DataZoe_2-1784311380666.png")

*Figure: The Filter pane settings with report-wide options for text, input boxes, headers, search, borders, backgrounds, and filter cards.*

To use this in another report, go back to **Theme** **settings** and export the theme file to import in another report.

![DataZoe_3-1784311405944.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355883iC4CD64AA43E2FD28/image-size/medium?v=v2&px=400 "DataZoe_3-1784311405944.png")

*Figure: The Theme settings pane with the Export option selected for saving a custom report theme.*

The **themes** dropdown from the **View** ribbon is now a lot smaller! Themes that were simply color variations have been moved to **Color palettes**, making it easier to find the built-in themes with more substantial styling changes.

![DataZoe_4-1784311442722.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355884i8E4AB0499A7C67FE/image-size/medium?v=v2&px=400 "DataZoe_4-1784311442722.png")

*Figure: The report themes gallery showing the report’s current theme and the remaining built-in Power BI themes, with color-only themes moved to color palettes.*

These will also work with the base theme you have picked, and you can always return to the visual defaults by clearing any theme applied.

As you try out customizing your report, the undo function also works in case you make a change you don’t like. Use the arrows at the top left of the window or CTRL + Z.

## Next steps

The modern visuals defaults streamline your report creation by letting you focus on building your report instead of styling each visual. Styling across the report makes it easier than ever before to add in your branded colors and get the consistent visual styling you want.

- **Learn more**: Explore the [Visual defaults in Power BI reports](https://learn.microsoft.com/power-bi/create-reports/power-bi-reports-visual-defaults) and [Use report themes in Power BI](https://learn.microsoft.com/power-bi/create-reports/desktop-report-themes) documentation.
- **Earlier blog**: Check out the earlier [Deep Dive into Modern Visual Defaults](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-Dive-into-Modern-Visual-Defaults-and-Customizing-Theme/bc-p/5301692#M2381).
- **Turn it on**: Enable **Modern visual defaults and customizing theme improvements** in **File** > **Options and settings** > **Options** > **Preview features** in Power BI Desktop.
- **Provide feedback**: [Your feedback](https://forms.cloud.microsoft/r/w8djJXSR1A) is important during preview. Let us know what you think!