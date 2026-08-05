---
title: "🎨 New Power BI Style Presets"
source: "https://medium.com/the-bi-corner/new-power-bi-style-presets-75374036b5d9"
author:
  - "[[Isabelle Bittar]]"
published: 2025-04-17
created: 2026-08-03
description: "How the March 2025 update makes report formatting faster, cleaner, and more collaborative"
Processed: "Unprocessed"
---
## How the March 2025 update makes report formatting faster, cleaner, and more collaborative

![](99.System/Attachments/1!GUGds90xqsB2_EG5cVJt4Q.png.webp)

By Isabelle Bittar for KI Data Science, Design Inspired by Fireart Studio

🎁 *PBIX and JSON files available for download at the end of this article!*

Power BI’s new **style presets** are a real game changer. As part of the [March 2025 feature summary](https://powerbi.microsoft.com/en-us/blog/power-bi-march-2025-feature-summary/), Microsoft has introduced the ability to define multiple *visual styles* within a single JSON theme file, so that we can have the option of picking different pre-configured styles for visuals, a bit like what’s available for Table and Matrix visuals.

![](99.System/Attachments/1!hdGKpkaQNgK2rlhBEhm8Fg.png.webp)

Existing Style Presets for Table Visuals in Power BI

This update allows you to assign multiple predefined style configurations to any Power BI visuals, then toggle between them in Power BI Desktop. For anyone building multi-page, multi-purpose reports — or collaborating with other developers — this helps maintain a cleaner and more consistent design system while reducing manual effort.

As someone who frequently customizes JSON themes for client projects, I’ve already found this useful. For example, in most reports, I’ll use a simplified version of a visual (like a bar chart or line chart) when it’s presented below a KPI to show a trend, and a more detailed one when it’s meant to be a more focal point/for analysis. Or sometimes I’ll want to show column charts with data labels, and other times with only axis labels and gridlines. Until now, I had to manually adjust each instance that deviated from my default style. With style presets, I can now configure all of them once and reuse the variations throughout the report.

In this article, I explain how you can create you own style presets, based on my PBIX and JSONS files (available at the end).

### 🔧 Step 1: Make Initial Theme Customizations in PBIX and Export JSON File

![](99.System/Attachments/1!DAi4C2d9cflgrZM226YrAw.png.webp)

Make Initial Theme Customizations in PBIX and Export JSON File

1. Open your Power BI report and go to **View > Themes > Customize current theme**.
2. Make any modifications you want through the UI (e.g., colors, fonts) and make sure to click **Apply** at the end. Bring at least a few initial customizations to the current theme so that the option to **Save current theme** becomes available.
3. Export your theme via **View > Themes > Save current theme**.
4. Open the `.json` file in a code editor such as **Visual Studio Code** for easier editing.

### 🧠 Step 2: Add the Schema Reference for IntelliSense Support

Before doing anything else, add or update the `$schema` property at the top of your JSON file. This helps enable **IntelliSense** —a feature in code editors like Visual Studio Code that offers smart auto-complete, validation, and helpful suggestions as you type.

Here’s the current recommended schema URL for the March 2025 release. I added it directly under the `name` property:

```c
"$schema":"https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/refs/heads/main/Report%20Theme%20JSON%20Schema/reportThemeSchema-2.141.json"
```
![](99.System/Attachments/1!rmEB-xOM_pfK71XLfj-o6g.png.webp)

Screenshot of Where I Added the $schema of the JSON Theme File

**Where do you find the latest schema URL?**

In Power BI Desktop:

1. Go to **View > Themes > Customize current theme**.
2. Click the link at the bottom labeled **“How to create a theme”**.
3. This will redirect you to Microsoft’s documentation, specifically to the GitHub page here:  
	👉 [Power BI Theme Schema GitHub](https://github.com/microsoft/powerbi-desktop-samples/tree/main/Report%20Theme%20JSON%20Schema)
4. Look for the latest schema version (in this case, 2.141 for March 2025) and copy the corresponding URL to use in your `$schema`.

### 🎨 Step 3: Understand the Visual Style Hierarchy

Power BI uses a hierarchical system when applying styles via JSON themes.

```c
"visualStyles": {
        "*": {
            "*": {
                "background": [
                    {
                        "transparency": 0
                    }
                ],
                "border": [
                    {
                        "color": {
                            "solid": {
                                "color": "#F7F7F7"
                            }
                        },
                        "show": true,
                        "radius": 20
                    }
                ],
                "visualHeader": [
                    {
                        "foreground": {
                            "solid": {
                                "color": "#10181C"
                            }
                        },
                        "transparency": 100
                    }
                ],
                "visualTooltip": [
                    {
                        "themedTitleFontColor": {
                            "solid": {
                                "color": "#10181C"
                            }
                        },
                        "themedValueFontColor": {
                            "solid": {
                                "color": "#10181C"
                            }
                        },
                        "actionFontColor": {
                            "solid": {
                                "color": "#10181C"
                            }
                        }
                    }
                ],
                "visualHeaderTooltip": [
                    {
                        "themedTitleFontColor": {
                            "solid": {
                                "color": "#10181C"
                            }
                        }
                    }
                ]
            }
        },
```

Here’s how it works:

1. **Global Defaults**: Defined under `"visualStyles": { "*": { "*": { ... } } }`, these apply to all visuals—like background color, border radius, tooltip formatting, and visual headers.
2. **Visual Type Defaults**: Next, for each visual type (like `"clusteredColumnChart"` or `"lineChart"`), you define the default appearance using `"*"` within that visual’s block. These settings act as the **base style** for that visual type.
3. **Preset Overrides**: When you use a `stylePreset`, it overrides only the properties that are explicitly defined in the preset, while still inheriting any missing properties from the visual’s default or the global default.

### Example: Clustered Column Chart Defaults

Here’s the default configuration for all clustered column charts in the theme file:

```c
"clusteredColumnChart": {
  "*": {
    "categoryAxis": [{ "showAxisTitle": false, "fontSize": 9 }],
    "legend": [{ "fontSize": 9 }],
    "padding": [{ "left": 20, "right": 20, "bottom": 15, "top": 15 }],
    "title": [{ "fontSize": 12 }],
    "valueAxis": [{ "fontSize": 9, "showAxisTitle": false }],
    "stylePreset": [{ "name": "ColumnDetailedChartLabels" }]
  },
```

This means that **unless otherwise specified**, every clustered column chart will:

- Hide axis titles,
- Use a smaller font size for axis and legend,
- Apply uniform padding,
- And automatically use the `ColumnDetailedChartLabels` preset on load.

The `"stylePreset"` line here doesn’t contain the configuration itself—it’s just the assignment. The configuration lives in a sibling property, explained next.

### 🎛️ Step 4: Create Custom Presets for Visuals

Now that you’ve defined a default look for a visual type, you can add named style variations — or **presets** — under the same visual type section. Each preset is defined by its name and the set of visual formatting properties it should override.

Example: Three Column Chart Presets

This theme file includes three different column chart presets:

🔹 **ColumnDetailedChartLabels**  
Used for rich data displays where labels and gridlines are needed.

```c
"ColumnDetailedChartLabels": {
  "dropShadow": [{ "show": true, "transparency": 90 }],
  "labels": [{ "show": true, "bold": true }],
  "valueAxis": [{ "show": false }]
}
```
![](99.System/Attachments/1!TVTzSWFWI90Z9LduCbgadQ.png.webp)

ColumnDetailedChartLabels Style Preset in Power BI

🔸 **ColumnDetailedChartNoLabels**  
Useful when you want the structure of the chart but prefer a minimalist presentation.

```c
"ColumnDetailedChartNoLabels": {
  "dropShadow": [{ "show": true, "transparency": 90 }],
  "labels": [{ "show": false }],
  "valueAxis": [{
    "gridlineStyle": "dashed",
    "gridlineShow": true,
    "gridlineColor": { "solid": { "color": "#ACB5B9" } }
  }]
}
```
![](99.System/Attachments/1!FymraYSaIAOv7RKwRxGW6w.png.webp)

ColumnDetailedChartNoLabels Style Preset in Power BI

🔸 **ColumnSimpleChart**  
This preset is for small visuals or embedded visuals where minimalism is key — no labels, no title, no axis lines.

```c
"ColumnSimpleChart": {
  "background": [{ "show": false }],
  "border": [{ "show": false }],
  "categoryAxis": [{ "show": false }],
  "dropShadow": [{ "show": false }],
  "labels": [{ "show": false }],
  "padding": [{ "left": 0, "right": 0, "bottom": 0, "top": 0 }],
  "title": [{ "show": false }],
  "valueAxis": [{ "show": false }]
}
```
![](99.System/Attachments/1!9CIEigUGxOl8Koa9cCZnZA.png.webp)

ColumnSimpleChart Style Preset in Power BI

### 🔁 Step 5: Load the Theme and Use Style Presets in Power BI

![](99.System/Attachments/1!B0QxQU_97c0C0D9Ja0YkMQ.png.webp)

Load Your JSON Theme File Back to Power BI

1. Save your updated `.json` file.
2. In Power BI Desktop, go to **View > Themes > Browse for themes** to reload your theme.
3. Now when you click on a visual, look under **Format > Style preset**. Any custom presets you defined for that visual type will appear in the dropdown.
![](99.System/Attachments/1!-EwOiXuhzJWm_dHezODzKQ.png.webp)

Style Preset Options in Power BI

⚠️The Style preset option only appears if you’ve developed a custom format in your JSON file.

### ✅ Wrapping Up

The new Style Preset feature might look subtle but it is an incredibly powerful update for Power BI developers. It introduces a new level of design scalability and consistency.

To get myself started using style presets, I found Bas’ video on them really helpful!

**You can download my report and JSON theme file with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/1-sqXhfwIVZDJyhndLEi0OoLRk141y7OW?usp=sharing)**.** Let me know how you use this in your own reports — I’d love to see it in action!

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)