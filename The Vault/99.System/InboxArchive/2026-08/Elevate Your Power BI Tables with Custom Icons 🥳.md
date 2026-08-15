---
title: "Elevate Your Power BI Tables with Custom Icons 🥳"
source: "https://medium.com/the-bi-corner/elevate-your-power-bi-tables-with-custom-icons-8fc36bad794b"
author:
  - "[[Isabelle Bittar]]"
published: 2024-12-31
created: 2026-08-03
description: "Step-by-Step Guide with PBIX to Embedding Custom Icons in Your Power BI Reports"
Processed: "Unprocessed"
---
## Step-by-Step Guide with PBIX to Embedding Custom Icons in Your Power BI Reports

![](99.System/Attachments/1!lgdNOa1T1jC3fNl6Y3oH6w.png.webp)

By Isabelle Bittar for KI Data Science

🎁 *PBIX available for download at the end of this article!*

### Introduction

Power BI tables are amazing. They offer many customization options through various methods. While I often rely on SVG measures/columns to create the look and feel I want, I recently started using a method that’s much lighter on visual load times and avoids other challenges such as column sorting.

This approach involves embedding custom icons (svgs, png/jpeg images, GIFs, etc.) directly into the JSON theme file and applying them through **conditional formatting of cell elements** in tables. This method ensures faster performance, avoids sorting issues, and provides a polished look without extra columns.

In the following article, I will take you through how I added the following icons in the **Shop Name** column of this table.

![](99.System/Attachments/1!uoPW0cD0VJOQqaNhjsS2YQ.png.webp)

Custom Icons Added to Shop Names in Power BI

### 1\. Getting Started

Here’s my initial data table in Power BI before I added the custom icons to the Shop Name column. The data is fictitious, generated with ChatGPT, and includes images of real products for illustrative purposes — so don’t overanalyze it 😅.

![](99.System/Attachments/1!yuvm2eWe2dp0ObiuxraNGw.png.webp)

Initial Data Table in Power BI

I created the icons for the Shop Name column in Figma and then exported them to SVG to get the code. However, SVGs aren’t the only option you can use. Power BI also supports other formats, such as **PNG**, **JPEG**, **GIFs**, **Unicode characters**, and even **emoji symbols** as icons. For example, **Base64-encoded PNGs or JPEGs** can be embedded, or you can use **Font Awesome** icons and Unicode symbols directly in DAX measures.

For this tutorial, I used SVGs because they are scalable, lightweight, and highly customizable. But if you’re looking for simpler or animated options, **Base64-encoded images** and **GIFs** are great alternatives.

To get started, you can find free SVG icons in libraries like [**SVG Repo**](https://www.svgrepo.com/) or design your own in tools like [**Figma**](https://www.figma.com/design/LWgbUnkaFL1Blu7uEOAip2/Custom-Icons?node-id=0-1&p=f&t=nlHMgYN6pZ1bRFng-0).

![](99.System/Attachments/1!HyB89QCRrdkEWqSE1oKNWA.png.webp)

Custom Icons Created in Figma

For example, the SVG code for the first blue icon is the following:

```c
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="12" cy="12" r="12" fill="#DCE7F2"/>
<path d="M8.04336 7.62053C8.2978 7.25329 8.76497 7.09938 9.18786 7.24347L16.7732 9.82794C17.2907 10.0043 17.5706 10.5635 17.4017 11.0835L15.7512 16.1631C15.6174 16.5751 15.2334 16.8541 14.8002 16.8541H9.19984C8.76661 16.8541 8.38266 16.5751 8.24878 16.1631L6.44679 10.6171C6.35031 10.3202 6.39805 9.99525 6.57586 9.73861L8.04336 7.62053Z" fill="#293D61"/>
</svg>
```

The code for each icon will then be added in the Power BI’s JSON theme file so that we can retrieve the icons through conditionnal formatting.

### 2\. Updating the Power BI JSON Theme File

To integrate the custom icons, you first need to **export your current theme file**:

1. Go to **View** → **Themes** → **Save Current Theme**.
2. Save it locally and rename it (e.g., ProductTheme.json).
![](99.System/Attachments/1!tL8nr6DJmd9k5kc7i-9W_A.png.webp)

Saving the Current Power BI Theme

Open the saved JSON file using a text editor such as **Visual Studio Code** (or even Notepad).

If you use VS Code, once you open the file, it will look like this:

![](99.System/Attachments/1!PfXCZpxuLlWLHvl0ueyVOw.png.webp)

Power BI Theme File Opened in VS Code

To format it, you can Press `Shift + Alt + F` (Windows/Linus) or `Shift + Option + F` (Mac).

You’ll see sections defining colors, fonts, and styles. Scroll to the bottom, and **add an Icons section** like this:

```c
"icons": {
  "IconName": {
    "url": "data:image/svg+xml;utf8,<svg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><circle cx='12' cy='12' r='12' fill='%23DCE7F2'/><path d='M8.04336 7.62053C8.2978 7.25329 8.76497 7.09938 9.18786 7.24347L16.7732 9.82794C17.2907 10.0043 17.5706 10.5635 17.4017 11.0835L15.7512 16.1631C15.6174 16.5751 15.2334 16.8541 14.8002 16.8541H9.19984C8.76661 16.8541 8.38266 16.5751 8.24878 16.1631L6.44679 10.6171C6.35031 10.3202 6.39805 9.99525 6.57586 9.73861L8.04336 7.62053Z' fill='%23293D61'/></svg>"
  }
}
```
![](99.System/Attachments/1!erAtTCKgFYe83MGYY2xeGg.png.webp)

Adding the Icon Section in the Power BI Theme File

When adding the SVG code to the url, here are some key transformation steps that need to be brought:

1. **Replace Double Quotes (“) with Single Quotes (‘)**.
```c
Original SVG Code: 
<circle cx="12" cy="12" r="12" fill="#DCE7F2"/>

Transformed Code:
<circle cx='12' cy='12' r='12' fill='#DCE7F2'/>
```

2\. **Escape Special Characters:** Replace `#` with `%23` and spaces with `%20`.

```c
Original SVG Code: 
fill="#DCE7F2"

Transformed Code:
fill='%23DCE7F2'
```

3\. **Remove Line Breaks and Whitespace:** Optimize for inline usage.

```c
Original SVG Code:
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
 <circle cx="12" cy="12" r="12" fill="#DCE7F2"/>
 <path d="M8.04336 7.62053C8.2978 7.25329 8.76497 7.09938 9.18786 7.24347L16.7732 9.82794C17.2907 10.0043 17.5706 10.5635 17.4017 11.0835L15.7512 16.1631C15.6174 16.5751 15.2334 16.8541 14.8002 16.8541H9.19984C8.76661 16.8541 8.38266 16.5751 8.24878 16.1631L6.44679 10.6171C6.35031 10.3202 6.39805 9.99525 6.57586 9.73861L8.04336 7.62053Z" fill="#293D61"/>
</svg>

Transformed Code:
<svg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><circle cx='12' cy='12' r='12' fill='%23DCE7F2'/><path d='M8.04336 7.62053C8.2978 7.25329 8.76497 7.09938 9.18786 7.24347L16.7732 9.82794C17.2907 10.0043 17.5706 10.5635 17.4017 11.0835L15.7512 16.1631C15.6174 16.5751 15.2334 16.8541 14.8002 16.8541H9.19984C8.76661 16.8541 8.38266 16.5751 8.24878 16.1631L6.44679 10.6171C6.35031 10.3202 6.39805 9.99525 6.57586 9.73861L8.04336 7.62053Z' fill='%23293D61'/></svg>
```

4\. **Add Prefix:** Append `data:image/svg+xml;utf8,` before the SVG code.

```c
Final Output: 
data:image/svg+xml;utf8,<svg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><circle cx='12' cy='12' r='12' fill='%23DCE7F2'/><path d='M8.04336 7.62053C8.2978 7.25329 8.76497 7.09938 9.18786 7.24347L16.7732 9.82794C17.2907 10.0043 17.5706 10.5635 17.4017 11.0835L15.7512 16.1631C15.6174 16.5751 15.2334 16.8541 14.8002 16.8541H9.19984C8.76661 16.8541 8.38266 16.5751 8.24878 16.1631L6.44679 10.6171C6.35031 10.3202 6.39805 9.99525 6.57586 9.73861L8.04336 7.62053Z' fill='%23293D61'/></svg>
```

5\. **Embed in Power BI JSON Theme File.**

![](99.System/Attachments/1!jBbPfEEPdf-QrQUMoBqXEg.png.webp)

Embedding SVG Code for Custom Icons in Power BI’s Theme File

### 3\. Updating the Theme File in Power BI

Reload your updated theme file into Power BI (View → Themes → Browse for Themes).

![](99.System/Attachments/1!XnCmj-AwsxULIz7Q1tN-oQ.png.webp)

Updating the Theme File in Power BI

### 4\. Retrieving the Custom Icons Through Power BI’s Table Cell Element Formatting

And finally, you can now access these icons through cell element formatting of the table.

![](99.System/Attachments/1!1-x5O5LULt9sjn7QT2M2dQ.png.webp)

Retrieving the Custom Icons Through Power BI’s Table Cell Element Formatting

In my case, it looked like the following:

![](99.System/Attachments/1!-IH6PpPi7_S8AjqSZRkDdA.png.webp)

Cell Element Formatting for Shop Names

And the icons appear once you hit OK. 🥳

![](99.System/Attachments/1!fkq68OqeInQbjjxst7ZSpw.png.webp)

Updated Power BI Table with Custom Icons

### Advantages of this approach:

- **Lightweight**: It’s a lot less heavy on your visual compared to image data or SVGs.
- **Sorting Compatibility**: Adding these custom icons don’t impact column/field sorting (this is a challenge when using SVGs).
- **No Additional Columns**: You don’t need to create an additionnal column (like with image data).
- **Flexible Design**: It works seamlessly with JSON themes.

### Limitations in this approach:

- **Icon Sizing**: The icons will always be relatively small, so it’s better to avoid creating very detailed custom icons (for example pills that include text), using this approach.
- **Adding Icons to Numerical Values**: One limitation of conditional formatting is that it requires both a minimum and maximum value to be set, which can make it less flexible in certain scenarios. For instance, if you want to use custom icons to indicate upward or downward trends based on price variations, you’d need to define a minimum value (e.g., greater than 0) and a maximum value (e.g., less than 1000). This can become problematic if your dataset contains values that exceed these limits. To work around this, you can create a text measure that outputs “positive” or “negative” based on the price variation and then apply custom icons to this measure instead. However, this approach does require an extra step 🫤.

### Wrapping Up

Power BI tables are great because there are different approaches we can leverage to add visual cues to them, wether through image data, SVG or custom icons. What I like about custom icons is that they don’t compromising performance. Give it a try and let me know how it works for your reports! Don’t forget to download the PBIX file! 😊

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/152SdqnqtJNci2KrlHM2IV4HsTOB7Pb0X?usp=sharing)**.**

If you interested in learning more about using SVGs in Power BI, you can read more on it [**here**](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d):

## [Step Up Your Power BI Game With SVGs 🔥](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d?source=post_page-----8fc36bad794b---------------------------------------)

### Building a Crypto Market Watch Dashboard in Power BI Using SVGs

medium.com

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)