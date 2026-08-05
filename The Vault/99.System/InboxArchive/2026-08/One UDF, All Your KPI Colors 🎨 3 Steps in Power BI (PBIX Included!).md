---
title: "One UDF, All Your KPI Colors 🎨: 3 Steps in Power BI (PBIX Included!)"
source: "https://medium.com/microsoft-power-bi/one-udf-all-your-kpi-colors-3-steps-in-power-bi-pbix-included-c1f96f0ab6f2"
author:
  - "[[Isabelle Bittar]]"
published: 2025-10-06
created: 2026-08-02
description: "Learn how to use Power BI’s new UDFs to simplify conditional formatting and standardize KPI colors across your dashboards"
Processed: "Unprocessed"
---
## Learn how to use Power BI’s new UDFs to simplify conditional formatting and standardize KPI colors across your dashboards

![](99.System/Attachments/1!2VJuzKlBfVYut1uCT5dnFg.png.webp)

By Isabelle Bittar for KI Data Science

***PBIX available at the end of this article 🥳!***

## Introduction

User Defined Functions (UDFs) are still very fresh in Power BI — and as we experiment with them, new use cases are popping up everywhere.

Building on my previous article [**⚡Power BI’s New User Defined Functions: 10 Must-Have You’ll Use in Every Report**](https://medium.com/microsoft-power-bi/power-bis-new-user-defined-functions-10-must-have-you-ll-use-in-every-report-616523e70a65), here’s an additional UDF I’ve started using a lot: **Color Indicators**.

Why? Because almost every dashboard has some form of conditional color formatting. Whether it’s showing KPIs, trends, or exceptions, consistent colors make your insights clearer and more professional.

This idea actually came from the community (thank you Sumesh for your comment 👋) and from my own projects where clients expect intuitive, color-coded indicators.

Here is a short demo of the dashboard presented in the cover image:

In this article, I’ll walk you through:

1. How to set up reusable color codes in your model
2. How to integrate the UDF into your report
3. How to use it for multiple indicators (cash flow, income, expenses)
4. Some adjustments you can bring to make it even more practical

## [⚡Power BI’s New User Defined Functions: 10 Must-Have You’ll Use in Every Report](https://medium.com/microsoft-power-bi/power-bis-new-user-defined-functions-10-must-have-you-ll-use-in-every-report-616523e70a65?source=post_page-----c1f96f0ab6f2---------------------------------------)

### Fast, consistent DAX — packaged once, reused forever.

medium.com

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Step 1: Setting Up The Color Codes in DAX Measures

One of the practices I’ve adopted across my reports is to store colors as **DAX measures** — not just in the JSON theme.

Why?

- It makes the palette **easy to reuse** across reports.
- You can copy measures between projects (via DAX Studio or Tabular Editor).
- Your UDF stays **theme-agnostic**: swap the color measures, keep the same UDF.

Here’s the baseline set I use:

- `_Color Dark Green` = **positive font color** 🟢
- `_Color Light Green` = **positive background** 🟢
- `_Color Dark Red` = **negative font color** 🔴
- `_Color Light Red` = **negative background** 🔴
- `_Color Text Secondary` = **neutral font** ⚪

👉 In my PBIX (download link at the end), you’ll find these in the **\_Constants/Variations** folder.

![](99.System/Attachments/1!xQYGkn536OHRqMd5jShz4A.png.webp)

Color Codes in DAX Measures in Power BI

👉 For neutral background, I’ve defaulted to white (#FFFFFF), but you can replace it with a measure too.

## Step 2: Adding the UDF to Your Report

Here’s the UDF itself. Paste it into **DAX Query View (DQV)**, click *Update model with changes*, and you’re good to go:

```c
DEFINE
    // UDF: Status Color for % Variations
    FUNCTION StatusColorPct =
        ( _value : NUMERIC, _inverse : BOOLEAN, _mode : STRING ) =>
        VAR _Normalized =
            IF ( _inverse, -_value, _value )  // flip if inverse relationship
        RETURN
            SWITCH (
                TRUE(),
                _Normalized > 0 && _mode = "Font",        [_Color Dark Green],
                _Normalized > 0 && _mode = "Background",  [_Color Light Green],
                _Normalized < 0 && _mode = "Font",        [_Color Dark Red],
                _Normalized < 0 && _mode = "Background",  [_Color Light Red],
                _Normalized = 0 && _mode = "Font",        [_Color Text Secondary],
                "#FFFFFF"   // fallback 
            )
```
![](99.System/Attachments/1!KoOWHVcGXLgZGdPFy47r7A.png.webp)

Integrating the UDF to Your Power BI Report

After updating the model, check under **TMDL → Functions**: you should see *StatusColorPct* listed. ✅

![](99.System/Attachments/1!rLpKyUDluGzpNMYv135EOQ.png.webp)

✅ Checking that the UDF has Been Added to the Power BI Report

### Step 2.5: How the UDF Works

Even though the function looks short, there are a few key design choices baked in.

1. **Normalize the value**
```c
VAR _Normalized =
    IF ( _inverse, -_value, _value )
```

This is where the `**_inverse**` **argument** comes into play. Not all metrics follow the same logic:

- For **income** → increase = ✅ positive (green)
- For **expenses** → increase = ❌ negative (red)

By flipping the sign when `_inverse = TRUE`, the UDF stays flexible across very different indicators.

👉 Think of `_inverse` as your toggle:

- `FALSE` → “higher is better” (default)
- `TRUE` → “lower is better”

**2\. Switch by condition**

```c
SWITCH (
    TRUE(),
    _Normalized > 0 && _mode = "Font",        [_Color Dark Green],
    _Normalized > 0 && _mode = "Background",  [_Color Light Green],
    _Normalized < 0 && _mode = "Font",        [_Color Dark Red],
    _Normalized < 0 && _mode = "Background",  [_Color Light Red],
    _Normalized = 0 && _mode = "Font",        [_Color Text Secondary],
    "#FFFFFF"   // fallback
)
```
- `SWITCH(TRUE())` evaluates multiple logical tests in sequence.
- Positive → green, Negative → red, Zero → neutral.
- `_mode` tells the function whether to return a font color (dark shades) or background (light shades).

**3\. Return a color code**  
Each branch outputs a **hex code** from your palette measures. Because visuals in Power BI accept “Format by Field value”, you can apply this directly to cards, tables, and charts.

💡 We keep colors in separate measures (not hard-coded) so the UDF is theme-independent — you can reuse it across reports, swap palettes, and stay consistent.

```c
Metric Value
                  │
           ┌───────┴────────┐
           │ Inverse? (TRUE)│
           │  Flip sign     │
           └───────┬────────┘
                   │
        ┌──────────┼──────────┐
        │                       │
   Normalized > 0          Normalized < 0
        │                       │
┌───────┴───────┐       ┌───────┴───────┐
│ Font = Dark Green │   │ Font = Dark Red│
│ Bg   = Light Green│   │ Bg   = Light Red│
└──────────────────┘   └──────────────────┘
                   │
           Normalized = 0
                   │
      Font = Grey, Bg = White
```

## Step 3: Start Using the UDF

Once the UDF has been integrated, you can start using it across your measures. In this report, I used it to define the colors of the background and font of the following 3 indicators: cash flow, income, expenses.

For example, for cash flow variation, the font color was defined in this one-liner:

```c
Font Color Cash Flow Variation = StatusColorPct([Cash Flow % Variation],FALSE,"font")
```

and the background color too:

```c
Background Color Cash Flow Variation = StatusColorPct([Cash Flow % Variation],FALSE,"Background")
```

It was then pretty straight forward to assign these measures to the different visuals font and background colors.

![](99.System/Attachments/1!lhV-SVSuB2hIryfB2_JD0A.png.webp)

🟢 Assigning the Font Color of the Cash Flow Variation to the Card Visual in Power BI

## 💡 Other Adjustments You could Bring to this UDF

This is where it gets interesting. Depending on your reporting standards, you could extend the UDF to:

- Add a **tolerance band** (e.g. ±2% = neutral/grey) so small fluctuations don’t trigger red/green.
- Return **icons** along with colors (`UNICHAR(9650)` ▲ for up, `UNICHAR(9660)` ▼ for down).
- Centralize thresholds or alternate palettes (e.g. corporate blue/orange instead of green/red).
- Handle **both font + background** in one call by returning a table with two values (advanced trick).

## Bonus: Combining with Other UDFs

In my demo PBIX, you’ll also find a UDF called `CompareOverPeriodRange`, which calculates YoY/QoQ/MoM/WoW values, prior value, delta, and percentage variation.

Together with `StatusColorPct`, you have a full framework for:

- calculating deltas
- formatting them consistently
- reusing across multiple projects

That’s the real power of UDFs: **define once, reuse everywhere**.

## Conclusion

As you can see, UDFs can quickly become real **accelerators** in Power BI development. They help you eliminate repetitive logic, ensure consistency across reports, and build a foundation of reusable building blocks.

If you haven’t started yet, this is the perfect time to begin creating your own **UDF library** — a collection of ready-to-use functions that reflect your style and best practices. Over time, it’ll become one of your greatest productivity assets.

Hopefully this color UDF becomes a useful addition to your toolbox. I’d love to hear what other UDFs you’ve started creating or reusing — share them in the comments! I’m still expanding my own library too 😅.

**🎁 You can download my Power BI report** [**here**](https://drive.google.com/file/d/1ZLDrA6NlrYn3PfCA0WLQQzR9JQOFvSwW/view?usp=sharing)**!**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

## Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

## Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)

👏🏻 Clap 🔎 [Follow](https://isabittar.medium.com/) 📩 [Subscribe](https://isabittar.medium.com/subscribe) ✍🏻Comment

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----c1f96f0ab6f2---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX, Data Visualization

**Tags:** Tutorial, PBIX, DAX, Data Visualization