---
title: "The Ultimate Time-Saver: Style Presets in Power BI"
source: "https://datatraining.io/blog/style-presets"
author:
  - "[[datatraining]]"
published:
created: 2026-08-13
description: "Styling visuals consistently in Power BI just got easier and smarter. If you're tired of manually tweaking formatting for every visual, Style Presets are your new best friend.You probably already know about presets from tables and matrix visuals. But now, with the March 2024 update, you can define your own style presets for any visual type - saving time and ensuring design consistency across your reports."
Processed: "Unprocessed"
---
Styling visuals consistently in Power BI just got easier and smarter. If you're tired of manually tweaking formatting for every visual, Style Presets are your new best friend. You probably already know about presets from tables and matrix visuals. But now, with the March 2024 update, you can define your own style presets for any visual type - saving time and ensuring design consistency across your reports.

power bi dax style presets visual theme

**What Are Style Presets?****  
  
Style Presets** let you define a set of visual properties (like background color, border, corner radius) and apply them with one click to visuals of the same type.  
This means:

- Less manual formatting
- More consistent design
- Easier collaboration across teams

![](https://lwfiles.mycourse.app/datatraining-public/5ff6153c2475905e4229149bb7534b75.png)

**Step 1: Set Up a Theme in Power BI**  
  
To start, use Power BI Desktop (March 2024 or later).

1. Insert a **visual** (like a table or bar chart).
2. Go to the **View** tab → Select a base theme.
3. Click **Customize current theme.**

![](https://lwfiles.mycourse.app/datatraining-public/78b1a9ac334cb70d766d36c666d379a7.png)

4\. Give it a name (e.g. “Demo Theme”).  
5\. Go to **Visuals** and define formatting:

- Background color
- Border color
- Corner radius (e.g. 20px)

![](https://lwfiles.mycourse.app/datatraining-public/5db53f80f6cf65a0151793faf68ebb75.png)

Click **Apply** and see your changes reflected on all visuals.

**  
Step 2: Export the Theme as JSON**  
  
Now we take it a step further:  

1. Export the theme: **View → Save current theme**
2. Save it as demo-theme.json
3. Open it in a code editor (Visual Studio Code recommended)

To make it readable, **right-click → Format Document.**

**  
Step 3: Add a Schema Reference  
**  
For IntelliSense and validation, insert the Power BI theme schema at the top:

![](https://lwfiles.mycourse.app/datatraining-public/a9ca96ac2d49a7cc1afe612fd2c84a96.png)

"$schema": [https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/refs/heads/main/Report%20Theme%20JSON%20Schema/reportThemeSchema-2.140.json](https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/refs/heads/main/Report%20Theme%20JSON%20Schema/reportThemeSchema-2.140.json)  
  

You can find the latest schema link in [Microsoft's documentation](https://learn.microsoft.com/power-bi/create-reports/desktop-report-themes) and [schema repository.](https://github.com/microsoft/powerbi-desktop-samples/tree/main/Report%20Theme%20JSON%20Schema)

**  
Step 4: Define Custom Presets for Visuals**  
  
Inside the visualStyles section, you’ll define presets for a specific visual type (e.g., clusteredBarChart).

1. Use the visual type name as the key.
2. Within it, define multiple presets by name.
3. Set formatting options for each.

![](https://lwfiles.mycourse.app/datatraining-public/8c040797b2b08b6d1679d578507e1d9f.png)

**Step 5: Import and Test in Power BI**

1. Save the JSON file.
2. Go to **View → Browse for themes → Import your modified JSON.**

Once imported:

- Go to a visual’s **Format pane**.
- Under **Style Presets**, you'll now see your custom styles.

![](https://lwfiles.mycourse.app/datatraining-public/8216af418cd634fc88aaafda0937a2b6.png)

Switching between them applies all settings instantly.  
  
**Bonus: Default Preset Behavior**

If you click **Reset to default,** Power BI uses the preset defined as "default" in your theme file. However, note: sometimes this might not apply visual formatting unless you explicitly select the preset. This may be a bug or a nuance to be aware of.

![](https://lwfiles.mycourse.app/datatraining-public/8c4a3e3bc44e5a1f1c15a4b3355e08fb.png)

**Why This Matters  
  
**With custom style presets, you can:

• Define branding and design guidelines once.

• Reuse them across visuals and reports.

• Speed up development significantly.

• Promote **visual consistency** across your team or organization.  

Imagine one theme file containing presets for **bar charts, line charts, pie charts, cards**, and more - all selectable with one click.

**Hope you like it!**

Give it a try and see how it works for you! I’d love to hear what you think or see how you use this trick in your own reports.

How to Power BI

![](https://www.youtube.com/watch?v=nwk9Gi9B_Mg)