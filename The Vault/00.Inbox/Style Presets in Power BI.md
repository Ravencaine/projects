---
title: "Style Presets in Power BI"
source: "https://databear.com/power-bi-style-presets/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-05-04
created: 2026-08-04
description: "Save time and improve consistency using Power BI style presets—visual-level templates for fast, uniform formatting in your reports."
Processed: "Unprocessed"
---
Creating visually consistent Power BI reports just became much easier. With the March 2025 Power BI update, Microsoft introduced a powerful new feature: **style presets**. This feature lets you define and reuse formatting templates for specific visuals—saving time, reducing errors, and enabling consistent design at scale.

In this article, you’ll learn what style presets are, how they work, and how to implement them using JSON theme files. You’ll also see how to generate custom visual styles using a theme editor.

[Explore Power BI Training by DataBear](https://databear.com/power-bi-training/)

---

##### What Are Style Presets?

**Style presets** are reusable formatting templates for individual Power BI visuals, such as cards, column charts, or bar charts. Instead of adjusting properties manually for each visual, you can define formatting once in a theme file and apply it to any matching visual with a single click.

Think of them as themes, but at the individual visual level.

---

##### Benefits of Power BI Style Presets

- **Consistency** across visuals in your report
- **Efficiency** when formatting multiple charts
- **Accessibility** for beginners who may struggle to navigate the format pane
- **Scalability** since changes can apply automatically to all visuals using a preset

---

##### How to Use Style Presets in Power BI

##### Requirements

To access style presets, you must use **Power BI Desktop March 2025 or newer**. The feature is hidden by default unless defined in your theme’s JSON file. ![Power BI Desktop version 2.141.1754.0 from March 2025, which introduced the Power BI style presets feature.](99.System/Attachments/Power_BI_Desktop_version_2.141.1754.0_from_March_2025,_which_introduced_the_Power_BI_style_presets_f.png)

##### Step 1: Prepare Your Theme JSON File

Style presets are defined under the `visualStyles` section of your `.json` theme file. Each preset includes the name, target visual type (e.g., card, columnChart), and formatting settings.

##### Example JSON Snippet

```json
"visualStyles": {
  "card": {
    "*": {
      "stylePresets": {
        "RoundedCard": {
          "label": { "fontSize": 18 },
          "border": { "radius": 8, "color": "#D3D3D3" }
        }
      }
    }
  }
}
```

The asterisk `*` indicates the default preset to use.

---

##### How to Create Style Presets Easily

##### Use a Theme Generator

Although current theme generators don’t support style presets directly, you can still:

1. Build and export a theme using a tool like PowerBI.tips Theme Generator.
2. Open the exported theme in a text editor (e.g., VS Code).
3. Copy the relevant visual settings and paste them into the `stylePresets` section of your main theme.

This approach helps you avoid writing all settings from scratch.

![Power BI Theme Generator by POINT used to customize themes and prepare JSON settings for Power BI style presets.](99.System/Attachments/Power_BI_Theme_Generator_by_POINT_used_to_customize_themes_and_prepare_JSON_settings_for_Power_BI_st.png)

---

##### Applying Style Presets in Your Report

Once your theme JSON includes presets and is loaded into Power BI:

1. Add or select a visual.
2. Open the format pane.
3. Look for the **Style Presets** section.
4. Choose the desired preset to apply its formatting instantly.

If this option doesn’t appear, check that the preset applies to the correct visual type and is properly formatted.![Power BI style presets applied to a card visual showing a formatted currency value and selected demo preset](99.System/Attachments/Power_BI_style_presets_applied_to_a_card_visual_showing_a_formatted_currency_value_and_selected_demo.png)

---

##### Real-World Examples from the Demo

In the walkthrough, the presenter created several style presets for the **card** visual:

- **Rounded Card**: Adds a border radius and adjusts fonts to match a modern visual identity.
- **Value Only**: Strips down the card for use inside composite visuals like donut charts.
- **Dark Mode**: A high-contrast version for dark-themed reports.

Each preset was embedded in the JSON and made available in the format pane for quick toggling.

---

##### Tips for Working with JSON

- Use **Visual Studio Code** to view and edit your theme files.
- Use `Ctrl + K, Ctrl + 0` to collapse and navigate large JSON documents.
- Keep your presets organized by naming them clearly and separating visual types.
- Remember to update the `*` key to define the default preset.

---

##### Limitations and Recommendations

- Style presets are not visible unless explicitly defined in the theme.
- Each preset must be applied to a specific visual type.
- Beginners may struggle to locate or use this feature without guidance.

It would be highly beneficial if Microsoft made this feature accessible via the Power BI UI in the future—especially for new users who could gain the most value from it.

---

##### Conclusion

Style presets in Power BI are a powerful addition that can significantly improve your reporting workflow. Whether you’re a beginner trying to keep visuals clean or a seasoned developer managing multiple reports, using JSON-defined presets can ensure consistency, speed, and visual polish.

While this feature currently requires some knowledge of JSON, tools and templates can simplify the process. Once set up, style presets provide a professional look with minimal effort.

[Start your Power BI transformation journey with training from DataBear](https://databear.com/power-bi-training/)

---