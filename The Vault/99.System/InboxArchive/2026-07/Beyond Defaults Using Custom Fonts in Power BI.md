---
title: "Beyond Defaults: Using Custom Fonts in Power BI"
source: "https://medium.com/microsoft-power-bi/beyond-defaults-using-custom-fonts-in-power-bi-b2b341fd323e"
author:
  - "[[Isabelle Bittar]]"
published: 2023-09-25
created: 2026-07-29
description: "Enhancing User Experience Through Thoughtful UI and Tailored Typography in Power BI"
Processed: "Unprocessed"
---
## Enhancing User Experience Through Thoughtful UI and Tailored Typography in Power BI

![](99.System/Attachments/1!CQQAaVcjUj0IysW4JeWS4g.png.webp)

Custom Font Samples from Envato Elements

Power BI, by default, offers a select palette of font options. While these fonts are legible and professional, sometimes, there’s a need to step outside the default range — either to align with branding guidelines or to add a distinctive aesthetic touch to your reports. But as with all UI decisions, integrating custom fonts should be approached with care. Good UI isn’t just about looking good; it’s about enhancing the user’s experience, facilitating understanding, and ensuring accessibility. This guide will take you through the process of integrating custom fonts into your Power BI reports, keeping in mind the principles of effective UI design.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

Here is a step by step guide to integrate custom fonts to your Power BI report.

### Step 1: Prepare a Dummy Theme

Launch Power BI Desktop.

Navigate to the `View` tab. Under the `Themes` section, choose `Customize current theme`.

![](99.System/Attachments/1!FqiltFde4OiCtcakaPvQKg.png.webp)

Open Customize theme options

In the `Customize theme` window, select `Text`.

Change the default `Font family` for each subsection: `General`, `Title`, `Cards and KPIs`, and `Tab headers`. For this guide, let’s switch from "Segoe UI" to "Corbel".

![](99.System/Attachments/1!10q1uDX9W7bM26LLh_chUA.png.webp)

Change default font family

Click on `Apply` after adjusting each section.

![](99.System/Attachments/1!s_b85QfiQOYsykoEWW03cQ.png.webp)

Click on Apply

### Step 2: Add Your Custom Font to the Theme

Under the `View` tab, within `Themes`, select `Save current theme`.

![](99.System/Attachments/1!jgr1dr4RZuXG2-kD04VaXA.png.webp)

Saving dummy theme

This will export the dummy theme you created in a JSON File. Rename it and save it on your PC.

Once it has been saved, open it using Notepad or your prefered code editor. This is what you should see:

![](99.System/Attachments/1!Igq6S7sAiHaazOxnKmpVVg.png.webp)

Initial JSON File

You will notice that the dummy font you assigned, in our case “Corbel” appears at multiple places. Replace this font name by the custom font you would like to use. Please note that this new font needs to already be installed on your PC.

You can even set different fonts for headers, titles, etc., as per your requirements. But for a consistent user experience, limit the number of custom fonts.

In our case, we will be replacing the Corbel font with one of my favorites: **Poppins**. After replacing Corbel by Poppins at each instance, here is what the JSON file now looks like:

![](99.System/Attachments/1!zHStHd1-wlW54IF72rj8KA.png.webp)

JSON File with correct custom font

Once the changes are done, save your edited JSON file.

### Step 3: Replace the current theme with your updated JSON File

Return to Power BI Desktop.

Go to `View` > `Themes` > `Browse for themes`.

Navigate to and select the recently edited JSON file.

![](99.System/Attachments/1!SKIaobhrcps1vECre8WY3g.png.webp)

Select Browse for themes to select the updated JSON File

Upon successfully importing, Power BI should provide a confirmation message.

![](99.System/Attachments/1!JSICohBmZVIv77Yg6fL6jw.png.webp)

Confirmation of successful font upload

You can now test with different visuals to make sure that this new font is working appropriately.

In my case, I selected a text box and started writing. As you can see, the custom font Poppins is applied by default.

![](99.System/Attachments/1!bSReOVVAzlJGqHwNAz-wRA.png.webp)

Testing custom font

### Limitations

1. **User-side Font Installation**: For users to see the custom font on Power BI Service, the font must be installed on their systems. Otherwise, they’ll see a default font. This is normally not an issue if you are using your company’s default theme.
2. **Mobile Compatibility**: Check your report in mobile view if it’s commonly accessed via mobile devices. Custom fonts might not always render correctly. A workaround could be to choose a similar-looking standard Power BI font for the mobile view of your report.

### Conclusion

Integrating custom fonts can significantly elevate the visual appeal of your Power BI reports. However, always anchor your design choices in solid UI best practices. Fonts should be legible, consistent, and complement the data being presented. Remember, a report’s primary goal is to convey information efficiently; its design should support this aim, not overshadow it. By carefully selecting and integrating custom fonts, you ensure that your reports not only stand out but also remain user-centric, facilitating seamless interpretation and understanding of the data. In the realm of data visualization, where clarity is paramount, striking the right balance between aesthetic appeal and functionality is the key to success.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-end) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----b2b341fd323e---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy