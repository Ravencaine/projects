---
title: "⚡One UDF to Build All Your SVG Pills in Power BI"
source: "https://medium.com/microsoft-power-bi/one-udf-to-build-all-your-svg-pills-in-power-bi-43da8ca9058e"
author:
  - "[[Isabelle Bittar]]"
published: 2025-11-27
created: 2026-08-02
description: "A flexible, scalable way to generate beautiful SVG pills for statuses, priorities, and tags using Power BI’s new User-Defined Functions."
Processed: "Unprocessed"
---
## A flexible, scalable way to generate beautiful SVG pills for statuses, priorities, and tags using Power BI’s new User-Defined Functions.

![](99.System/Attachments/1!pZmaRfhr385MYhE4AJ1vnA.png.webp)

By Isabelle Bittar for KI Data Science

PBIX available at the end of this article 🎉!

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Introduction

Power BI’s new User-Defined Functions (UDFs) have opened up a whole new way to streamline and accelerate both team and individual report development. As I start to integrate them into more and more projects, some patterns are clearly emerging: a few UDFs end up being reused everywhere.

One of the use cases I keep coming back to is **SVG status pills** for table visuals.  
These tags can show up in almost every report:

- task status (Not started / In progress / Completed)
- project health (On track / At risk)
- departments or categories (Design / Development / Marketing)

The data fields change from project to project, but the visual style is almost always the same.

Here is a short demo:

In this article, I’ll share the **UDF** I now use to generate these SVG pills, and show how you can plug it into different measures (status, priority, etc.) across multiple reports. Examples of these pills are shown in the *Priority* and *Status* fields of the table visual of this cover image. They both use the same UDF.

## 1\. The UDFs

To generate SVG pills from any measure in your model, we actually need **two UDFs**:

1. `**UDF_EncodeSVG**`  
	→ URL-encodes the raw SVG string so Power BI can render it
2. `**UDF_SVGPillCanvas**`  
	→ draws the pill (background, border, text, optional dot)

You only need to define these once in your model, and then you can reuse them across every report.

### UDF #1 — SVG Encoder (UDF\_EncodeSVG)

Power BI visuals expect the SVG to be URL-encoded. Power BI can’t display raw SVG markup, so the SVG must be converted into a URL-encoded image string. `UDF_EncodeSVG` handles this conversion so the pill renders correctly inside your table visual.  
This helper UDF takes care of all the replacements for you:

```c
DEFINE
  FUNCTION UDF_EncodeSVG =
    ( svg : STRING ) =>
    VAR s0 = SUBSTITUTE(svg, "%", "%25")
    VAR s1 = SUBSTITUTE(s0 , "#", "%23")
    VAR s2 = SUBSTITUTE(s1 , "<", "%3C")
    VAR s3 = SUBSTITUTE(s2 , ">", "%3E")
    VAR s4 = SUBSTITUTE(s3 , """", "%22")
    VAR s5 = SUBSTITUTE(s4 , "'", "%27")
    VAR s6 = SUBSTITUTE(s5 , " ", "%20")
    VAR s7 = SUBSTITUTE(s6 , ":", "%3A")
    VAR s8 = SUBSTITUTE(s7 , "/", "%2F")
    VAR s9 = SUBSTITUTE(s8 , "?", "%3F")
    VAR sA = SUBSTITUTE(s9 , "=", "%3D")
    VAR sB = SUBSTITUTE(sA , "&", "%26")
    RETURN "data:image/svg+xml;utf8," & sB
```

This function is used inside every SVG-drawing UDF you create.

### UDF #2 — Pill Renderer (UDF\_SVGPillCanvas)

This UDF draws the actual pill:  
background, border, text, and (optionally) a dot.

```c
DEFINE
  FUNCTION UDF_SVGPillCanvas =
    ( label : STRING,
      bgColor : STRING,
      borderColor : STRING,
      textColor : STRING,
      showBorder : DECIMAL,   // 1 = border, 0 = no border
      dotColor : STRING,
      showDot : DECIMAL       // 1 = dot, 0 = no dot
    ) =>
    VAR fontSize     = 11
    VAR canvasWidth  = 200
    VAR canvasHeight = 28
    VAR leftPad      = 8

    VAR _pillH   = 24
    VAR _corner  = 12
    VAR _charW   = 6
    VAR _hPad    = 9
    VAR _textLen = LEN(label)

    /* ---------- Base paddings ---------- */
    VAR _baseTextPad = 8
    VAR _gapAfterDot = 6

    /* ---------- Dot geometry ---------- */
    VAR _dotR       = fontSize * 0.55 / 2
    VAR _dotOffsetX = leftPad + _baseTextPad
    VAR _dotOffsetY = canvasHeight / 2

    /* ---------- Text geometry ---------- */
    VAR _extraLeft =
        IF(
            showDot = 1,
            _baseTextPad + (_dotR * 2) + _gapAfterDot,
            _baseTextPad
        )

    VAR _pillW =
        _textLen * _charW + _hPad + _extraLeft

    VAR _rectY = (canvasHeight - _pillH) / 2
    VAR _textX = leftPad + _extraLeft
    VAR _textY = canvasHeight / 2

    /* ---------- Border logic ---------- */
    VAR _strokeColor =
        IF(showBorder = 1, borderColor, "none")

    VAR _strokeWidth =
        IF(showBorder = 1, "1", "0")

    /* ---------- SVG shapes ---------- */
    VAR _rect =
        "<rect x=""" & leftPad &
        """ y=""" & _rectY &
        """ width=""" & (_pillW - 1) &
        """ height=""" & (_pillH - 1) &
        """ rx=""" & _corner &
        """ fill=""" & bgColor &
        """ stroke=""" & _strokeColor &
        """ stroke-width=""" & _strokeWidth & """ />"

    VAR _svgDot =
        IF(
            showDot = 1,
            "<circle cx=""" & _dotOffsetX &
            """ cy=""" & _dotOffsetY &
            """ r=""" & _dotR &
            """ fill=""" & dotColor & """ />",
            ""
        )

    VAR _svgText =
        "<text x=""" & _textX &
        """ y=""" & _textY &
        """ dominant-baseline=""middle"" text-anchor=""start"" fill=""" & textColor &
        """ font-family=""Segoe UI"" font-size=""" & fontSize &
        "px"" font-weight=""400"">" &
            label &
        "</text>"

    VAR _svg =
        "<svg xmlns=""http://www.w3.org/2000/svg"" width=""" & canvasWidth &
        """ height=""" & canvasHeight &
        """ viewBox=""0 0 " & canvasWidth & " " & canvasHeight & """>" &
            _rect &
            _svgDot &
            _svgText &
        "</svg>"

    RETURN
        UDF_EncodeSVG(_svg)
```

### A few notes:

- `label` is the text inside the pill (“In Progress”, “High”, “Design”, etc.)
- `bgColor`, `borderColor`, `textColor`, and `dotColor` usually come from your **accent color measures**
- `showBorder` and `showDot` let you reuse the same UDF for:
- filled pills
- outline pills
- subtle pills with a dot
- clean pills without a dot
- …all without rewriting any SVG

Once both UDFs are defined in **DAX Query View**, make sure to click **Update model with changes** so your measures can call them.

![](99.System/Attachments/1!uqRsOz3t2rNH9bM2YGmEjQ.png.webp)

Updating Moding with UDFs in Power BI

## 2\. Using the UDF

The UDF only *draws* a pill. But by referencing measures when you call it, **you** decide the text label, background color, border color, dot color, and whether the border or dot should appear at all.

I like to store all my colors in dedicated measures, and then define in separate logic measures which colors should be used for each label. This keeps everything modular and makes the pills easy to reuse across reports.

Here are two examples: one for displaying project task statuses, and one for showing priority levels:

### 2.1 Task Status Pill

Here’s an example for the `Tasks[Status]` column:

```c
Task Status Pill :=
VAR _label =
    SELECTEDVALUE(Tasks[Status])

VAR _bgColor     = [Status Background Color]
VAR _borderColor = [Status Border Color]
VAR _textColor   = [_ColorTextDark]
VAR _dotColor    = [Status Border Color]

RETURN
    IF (
        ISBLANK(_label),
        BLANK(),
        UDF_SVGPillCanvas(
            _label,
            _bgColor,
            _borderColor,
            _textColor,
            1,          // showBorder
            _dotColor,
            0           // showDot = 0 → clean outline pill, no dot
        )
    )
```

Here `Status Background Color` and `Status Border Color` are simple SWITCH measures that map each status to one of your accent colors (Completed → mint, In Progress → blue, At Risk → red, etc.).

### 2.2 Task Priority Pill (with dot)

For priority, I like to keep the pill neutral and only use the dot color to signal intensity:

```c
Task Priority Pill :=
VAR _label =
    SELECTEDVALUE(Tasks[Priority])

VAR _bgColor     = [_ColorWhite]
VAR _borderColor = [_ColorAccent9Dark]
VAR _textColor   = [_ColorTextDark]

VAR _dotColor =
    SWITCH(
        SELECTEDVALUE(Tasks[Priority]),
        "High",   [_ColorAccent5Dark],
        "Medium", [_ColorAccent4Dark],
        "Low",    [_ColorAccent1Dark],
        [_ColorAccent9Dark]
    )

RETURN
    IF (
        ISBLANK(_label),
        BLANK(),
        UDF_SVGPillCanvas(
            _label,
            _bgColor,
            _borderColor,
            _textColor,
            1,          // showBorder = 1
            _dotColor,  // dot color carries the “signal”
            1           // showDot = 1 → dot visible
        )
    )
```

You can now drop **both measures** into your table visual:

- `Task Status Pill` in the **Status** column
- `Task Priority Pill` in the **Priority** column

…and you get something very close to the mock UI in the screenshot: clean, consistent pills driven by just a few measures.

## 3\. Setup Details

A few small details to ensure it works 😅:

- **Enable UDFs:** As of writing, DAX UDFs are still a preview feature. Make sure they’re enabled in **Options → Preview features** and that you’re using the new **DAX Query View**.
![](99.System/Attachments/1!X0retS8chSEYTu_4uVVt5A.png.webp)

Enable UDFs in Power BI

- **Update model with changes:** After pasting the `DEFINE FUNCTION` block, click **Update model with changes**. Otherwise, the function won’t be callable from measures.
- **Data category:** For each pill measure, set **Data category = Image URL**, as you would for any SVG DAX measure.
![](99.System/Attachments/1!uf_ldgaoASvTmICebzcAlw.png.webp)

Setting the Data Category of a Measure in Power BI

- **Image size:** In the table visual, under **Values → Grid → Image size**, set: Height = **28 px,** Width = **200 px**. These match the `canvasHeight` and `canvasWidth` constants inside the UDF. If you change them, update both places (visual and UDF) so the pill stays perfectly centered.
![](99.System/Attachments/1!DQHv6iyZjovWWIQH9ytQng.png.webp)

Setting the Image Size of the Table Visual in Power BI

If you are interested in learning more about using SVGs in your reports, here is my article on the topic:

## [Step Up Your Power BI Game With SVGs 🔥](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d?source=post_page-----43da8ca9058e---------------------------------------)

### Building a Crypto Market Watch Dashboard in Power BI Using SVGs

medium.com

## 4\. Want to Go Further?

Because the UDF is generic, you can reuse it for almost any pill use case:

- **Departments** (Design / Development / Marketing)
- **Project health** (On track / At risk / Blocked)
- **Tags** (Bug / Enhancement / Feature / Tech Debt)

All you do is change the measure that calls `UDF_SVGPillCanvas`:

- pick the label (`SELECTEDVALUE` of your column)
- map it to background, border, text, and dot colors
- decide whether you want a dot and/or a border

No extra SVG work. No copy-pasting huge strings into multiple measures.

If you’d like more ideas of reusable UDFs you can bring into your model, I’ve rounded up some favourites here:

## [⚡Power BI’s New User Defined Functions: 10 Must-Have You’ll Use in Every Report](https://medium.com/microsoft-power-bi/power-bis-new-user-defined-functions-10-must-have-you-ll-use-in-every-report-616523e70a65?source=post_page-----43da8ca9058e---------------------------------------)

### Fast, consistent DAX — packaged once, reused forever.

medium.com

## Lessons Learned

When I first started experimenting with SVG + UDFs, I kept putting way too much logic inside the function itself. Over time, a few principles emerged:

- **The UDF should only care about drawing.**  
	Geometry, padding, rounded corners, dot position, etc.
- **Measures decide the semantics.**  
	Which status uses which color, when the dot appears, which text is shown.
- **Keep colors in dedicated measures and not in the UDF.**  
	Having `[Status Background Color]`, `[Status Border Color]`, `[Priority Dot Color]`, etc., makes it easy to keep a consistent design system across reports, and not be limited to a fixed amounts of colors.
- **Design once, reuse everywhere.**  
	Once the UDF is in your model, every new pill is just a 10–15 line measure. That’s the real win.

[**Here is the PBIX**](https://drive.google.com/file/d/1bBUJOblUP3N41PBuUjGfvfqBkXPms5Ng/view?usp=sharing) **if you’d like to explore the full example and copy the pieces you need into your own reports 🎨📊**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----43da8ca9058e---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** DAX, Data Visualization

**Tags:** Tutorial, DAX, Data Visualization, PBIX