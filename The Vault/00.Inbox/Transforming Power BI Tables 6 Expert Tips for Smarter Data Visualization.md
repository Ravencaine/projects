---
title: "Transforming Power BI Tables: 6 Expert Tips for Smarter Data Visualization"
source: "https://medium.com/the-bi-corner/transforming-power-bi-tables-6-expert-tips-for-smarter-data-visualization-7dc7068870ff"
author:
  - "[[Isabelle Bittar]]"
published: 2024-09-19
created: 2026-08-03
description: "Boost User Experience with These Power BI Table Enhancements"
Processed: "Unprocessed"
---
## Boost User Experience with These Power BI Table Enhancements

![](99.System/Attachments/1!w4k5Y5qIEQJiE3Wg5MGYIA.png.webp)

By Isabelle Bittar for KI Data Science

🎁 *PBIX available for download at the end of this article!*

Data tables are very common in Power BI reports and dashboards. While they usually serve the purpose of accessing more granular data presented by preceding KPIs, there are ways of improving them visually to make it easier for users to quickly see certain outstanding elements and navigate/sort through them.

In this article, I will walk you through how I started off with this table data:

![](99.System/Attachments/1!vYae-Cb6anXtFzAH5nNM1g.png.webp)

Initial Data Table in Power BI

and transformed it to this:

![](99.System/Attachments/1!t44i3vYG5jxzkd9UB-QrYg.png.webp)

Revised Data Table in Power BI

The revised data table was built using Power BI’s native table visual and using a bit of SVG magic 🪄. I also designed the background of the report in Figma.

Here are some of the key improvements I brought in the revised table:

![](99.System/Attachments/1!VxoAor1KjIWxF5S4s7Ljkg.png.webp)

Key Improvements Brought to the Intial Data Table

I will take you through how I implemented these six different improvements in the next sections.

### 1\. Combining Important Information Together

![](99.System/Attachments/1!d5h30ELrBpTXmslc5IKrwA.png.webp)

Combining Important Information Together in Power BI Tables

The original table had all the right details, but with information scattered across multiple columns, it could feel overwhelming. By grouping key data points based on their importance, I’ve restructured the table to ensure that primary information stands out, while secondary details don’t clutter the view. This not only simplifies the table but also makes it more intuitive for users.

To achieve this, I added calculated columns to the data table containing all the invoice data, then combined the necessary values together and used SVG code to apply the desired formatting.

For example, the **Invoice Information** column now includes:

- The name of the customer (primary information)
- The invoice number (secondary information)
- The invoice date (secondary information)

I created the `Invoice Info SVG` column using the following DAX code, which also integrates some SVG formatting:

**Preliminary Measures:**

```c
_Color dark grey = "#959EB5"
SVG Set Up = "data:image/svg+xml;utf8, <svg width='120' height='40' xmlns='http://www.w3.org/2000/svg'>"
```

**Column**:

```c
Invoice Info SVG = 
VAR _CustomerName = 'InvoiceData'[Customer Name]
VAR _InvoiceID = 'InvoiceData'[Invoice ID]
VAR _InvoiceDate = 'InvoiceData'[Invoice Date]
VAR _InvoiceInfo = _InvoiceID & " " & UNICHAR(8226) & " " & _InvoiceDate

RETURN 
[SVG Set Up] & "
    <!-- Customer Name in bold -->
    <text x='5' y='10' font-family='Segoe UI Semibold' font-size='10'>" & _CustomerName & "</text>
    
    <!-- Invoice ID in grey -->
    <text x='5' y='30' font-family='Segoe UI' font-size='10' fill='" & [_Color dark grey] & "'>" & _InvoiceInfo & "</text>
</svg>"
```

You’ll notice that I created this as a column instead of a measure because I wanted to tie the sorting logic to existing elements in the data table. For instance, in this case, I wanted the **Invoice Info SVG** column to be sorted based on the existing **Invoice ID** column.

![](99.System/Attachments/1!qhU-AFayt0bFekRjnT1lcg.png.webp)

Sorting a Column Based on Another Column in Power BI

If you are new to using SVG in Power BI, [here](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d) is an article I’ve written to help you get started 🚀.

## [Step Up Your Power BI Game With SVGs 🔥](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d?source=post_page-----7dc7068870ff---------------------------------------)

### Building a Crypto Market Watch Dashboard in Power BI Using SVGs

medium.com

### 2\. Adding Visual Cues

![](99.System/Attachments/1!xEu22n6fZNoYXXyApXWR4g.png.webp)

Adding Visual Cues in Power BI Tables

To help users quickly identify customers with multiple outstanding invoices, I included customer profile pictures in the invoice section. This small addition has a big impact, allowing users to spot patterns faster without needing to scan through rows of text. For example, in this dashboard, users can quickly see that customers Mei Li and Luis Hernandez have multiple outstanding invoices.

There are different ways to add pictures to table visuals in Power BI. In this case, I had a picture URL stored in my data table under the **Customer Picture** column. All I needed to do was ensure that the data category for this column was set to **Image URL** in the table view.

![](99.System/Attachments/1!p1GjQPG-rzDXquBno0HElg.png.webp)

Changing a Column’s Data Category in Power BI

Once that’s set, you can simply add the column as a field in your table visual, and the images will be displayed accordingly.

### 3\. Integrating Table-Specific Slicers

![](99.System/Attachments/1!7LYFvVZWnhmoicigcy97rQ.png.webp)

Tailored Slicers for the Table in Power BI

While report-wide slicers are useful, there are times when users want to filter data within a specific table without affecting the rest of the dashboard. To address this need, I designed the table to integrate slicers that are exclusive to it, giving users full control over what they’re filtering without altering the broader report view.

To achieve this, I added the necessary slicers and made sure to disconnect them from other visuals by using the **Edit Interactions** option under the **Format** tab for each slicer.

![](99.System/Attachments/1!xRzC3ao14s0TuBCZ6M81Fg.png.webp)

Disconnecting Slicers from Visuals in Power BI

Visually, I also ensured it was clear that these slicers were tied to the table by incorporating a custom design (background created in Figma) that distinguishes them as part of the table’s visual layout.

![](99.System/Attachments/1!8ZFjgCLiAovl8E5GIkEhDA.png.webp)

Power BI Table Background Created in Figma

To get inspired and learn on how to elevate your Power BI reports with Figma, you can read my article [here](https://medium.com/microsoft-power-bi/figma-meets-power-bi-revolutionizing-report-design-420cce760aa7)! 🎨

## [Figma Meets Power BI: Revolutionizing Report Design](https://medium.com/microsoft-power-bi/figma-meets-power-bi-revolutionizing-report-design-420cce760aa7?source=post_page-----7dc7068870ff---------------------------------------)

### Unleashing Creativity and Efficiency in Data Visualization

medium.com

### 4\. Conditional Formatting for Clarity

![](99.System/Attachments/1!2SDCY_8qkbpfJE0yVwKzkQ.png.webp)

Conditional Formatting for Clarity in Power BI Tables

I believe that statuses, whether they relate to timelines (e.g., in progress, delayed) or risk levels (e.g., high, medium, low), should always be highlighted through color-coding to immediately capture users’ attention🚦. In this case, I applied color-coding to the background and text of each invoice status. Additionally, for partially paid invoices, I included a note indicating the remaining balance due.

To achieve this, I created the additional column `SVG Invoice Status` in the data table using a combination of DAX and SVG code, similar to the approach outlined in point 1.

**Preliminary Measures:**

```c
_Color light blue = "#E6EBFA"
_Color light green = "#EBFAF4"
_Color light red = "#FAECEC"
_Color light yellow = "#FDF8EB"
_Color dark blue = "#2252D4"
_Color dark green = "#42D09B"
_Color dark red = "#EC3636"
_Color dark yellow = "#E3A313"

Invoice status = FIRSTNONBLANK(InvoiceData[Invoice Status],1)
```

**Column:**

```c
SVG Invoice Status = 
VAR _FontColor = 
    SWITCH(
        TRUE(),
        [Invoice status] = "Paid", [_Color dark green],
        [Invoice status] = "Partially Paid", [_Color dark blue],
        [Invoice status] = "Overdue", [_Color dark red],
        [Invoice status] = "Unpaid", [_Color dark yellow]
    )

VAR _BackgroundColor = 
    SWITCH(
        TRUE(),
        [Invoice status] = "Paid", [_Color light green],
        [Invoice status] = "Partially Paid", [_Color light blue],
        [Invoice status] = "Overdue", [_Color light red],
        [Invoice status] = "Unpaid", [_Color light yellow]
    )

-- Calculate the width of the rectangle based on the length of the text
VAR _TextLength = LEN([Invoice status])
VAR _RectangleWidth = 28 + (_TextLength * 3.5)

-- Calculate the starting x position of the text to center it
VAR _TextX = (_RectangleWidth / 2) - ((_TextLength * 3))

-- Add a small note if the status is "Partially Paid"
VAR _BalanceNote = 
    IF(
        [Invoice status] = "Partially Paid", 
        "<text x='12' y='32' font-family='Segoe UI' font-size='10' fill='" & [_Color dark grey] & "'>Balance due: " & FORMAT([Balance due], "$#") & "</text>", 
        ""
    )

VAR _Visualization = 
    [SVG Set Up] & " 
<rect x='5' y='0' width='" & _RectangleWidth & "' height='20' rx='4' ry='4' style='fill:" & _BackgroundColor & "'/>
<text x='13' y='14' font-family='Segoe UI Semibold' font-size='10' fill='" & _FontColor & "'>" & [Invoice status] & "</text>
" & _BalanceNote & "
</svg>
"
RETURN _Visualization
```

### 5\. Making Sorting Intuitive

![](99.System/Attachments/1!XNFQ8xF85OA-xxTMpStV0g.png.webp)

Making Sorting Intuitive in Power BI Tables

Sorting shouldn’t be a guessing game 🤔. Power BI visuals are powerful, but many users may not fully realize all the interactive features available. To make it more obvious that columns can be sorted, I added small sorting icons to the background of each column header through a custom design created in Figma.

To ensure that these icons were visible, even behind the table, I turned off the background of the table visual. This allowed the sorting icons to show through and guide users to the functionality, enhancing the table’s interactivity without adding unnecessary complexity.

![](99.System/Attachments/1!X42yTPRPdtcPaM0V8adi3g.png.webp)

Removing the Background from Power BI Tables

### 6\. Adding More Context to Dates

![](99.System/Attachments/1!mPXMbk0Mjzfh0YoEiiZS3A.png.webp)

Adding More Context to Dates in Power BI Tables

Time is everything when it comes to unpaid invoices ⌛. For invoices that are not fully paid, I introduced a reference that displays how many days past due they are or how many days remain until the invoice is due. This added layer of detail gives users a clearer sense of timing, making it easier to identify and prioritize invoices that have been overdue the longest.

To achieve this, I once again used a combination of DAX and SVG to create the additional calculated column `SVG Due Date` in the dataset.

**Preliminary Measures:**

```c
Invoice due date = FIRSTNONBLANK(InvoiceData[Due Date],1)
Today = Today() / -- In the downloadable file, I fixed it to: DATE(2024,09,17)
```

**Column:**

```c
SVG Due Date = 
VAR _FirstText = 
    SWITCH(
        TRUE(),
        [Invoice due date] = [Today], "Today",
        [Invoice due date] = [Today] - 1, "Yesterday",
        [Invoice due date] = [Today] + 1, "Tomorrow",
        [Invoice due date] < [Today], ABS(DATEDIFF([Today], 'InvoiceData'[Due Date], DAY)) & " days ago",
        [Invoice due date] > [Today], "in " & DATEDIFF([Today], 'InvoiceData'[Due Date], DAY) & " days"
    )

-- Bold FirstText only when the status is not "Paid"
VAR _BoldFirstText = 
    IF(
        [Invoice status] <> "Paid",
        "<tspan x='5' font-weight='bold'>" & _FirstText & "</tspan>",
        ""
    )

-- Calculate the y position dynamically based on whether _BoldFirstText exists
VAR _DueDateY = IF([Invoice status] <> "Paid", 30, 10)

-- Render Invoice due date
VAR _InvoiceDueDateText = 
    "<tspan x='5' y='" & _DueDateY & "' fill='" & [_Color dark grey] & "'>" & [Invoice due date] & "</tspan>"

-- Combine both parts for the final SVG
VAR _FullText = 
    _BoldFirstText & _InvoiceDueDateText

-- Render the SVG
VAR _Visualization = 
    [SVG Set Up] & " 
<text x='5' y='10' font-family='Segoe UI Semibold' font-size='10' >
" & _FullText & "
</text>
</svg>
"

RETURN _Visualization
```

### Conclusion

I will say it before you 😅. Yes, this approach:

- is a bit more complexe and requires more effort
- combines the use of different tools and may increase the heaviness of the report
- may require more maintenance effort

… but I think it’s worth it and the outcome is not only visually appealing, but also helpful to users.

Let me know what you think!! 🙂

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/1CfSJ4ci2DcEooq0pK2Fgo-00XWr8IMaH?usp=sharing)**.**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X (Formerly Twitter)***](https://twitter.com/KI_Datascience)