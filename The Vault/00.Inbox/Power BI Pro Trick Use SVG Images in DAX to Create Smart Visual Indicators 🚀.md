---
title: "Power BI Pro Trick: Use SVG Images in DAX to Create Smart Visual Indicators 🚀"
source: "https://medium.com/learning-data/power-bi-pro-trick-use-svg-images-in-dax-to-create-smart-visual-indicators-5bd03c6fce6f"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2025-12-22
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Power BI visuals are powerful, but sometimes **a simple visual cue can communicate more than a chart ever will**.

If you’ve been following Power BI’s recent updates, you know Microsoft has been consistently pushing boundaries with new visuals and capabilities.

Today, I’m excited to share a powerful technique that combines **SVG images**, **DAX measures**, and the **new Image visual** to create dynamic visual indicators that respond to slicer selections.

This isn’t just another tutorial — it’s a game-changer for creating intuitive, visually appealing dashboards that communicate selection states instantly to your end users.

![](https://miro.medium.com/v2/resize:fit:1280/format:webp/1*803wu5tO-q4W1qjkLyKBLA.gif)

Video Demo: Showing different categories using the Image visual

In one of my earlier Medium posts, I showed how to [**highlight multiple months in a chart without filtering the data**](https://medium.com/@ankan.ab21/power-bi-pro-trick-highlight-months-with-conditional-formatting-no-filtering-5d3150fcc41b) using conditional formatting.  
In that example, I worked with three product categories:

- **Apparel**
- **Electronics**
- **Furniture**

👉 If you haven’t read that post yet, I strongly recommend starting there:  
🔗 [*Power BI Pro Trick: Highlight Months with Conditional Formatting (No Filtering)*](https://medium.com/@ankan.ab21/power-bi-pro-trick-highlight-months-with-conditional-formatting-no-filtering-5d3150fcc41b)

In this article, we’ll **extend that same dataset and idea** — but this time, we’ll add something new and exciting:

> ***SVG-based images rendered dynamically using DAX, powered by the new Image visual in Power BI.***

## Why Visual Indicators Matter

Slicers are great, but they’re not always obvious — especially for business users who consume reports rather than build them.

Instead of forcing users to *look at slicers*, we can:

- Show **which categories are selected**
- Provide **instant visual feedback**
- Improve report clarity and user experience

And we’ll do all of this **without bookmarks, buttons, or complex layering**.

## Meet the New Image Visual in Power BI 🖼️

Power BI recently introduced a **new Image visual**, and it’s a big upgrade from the old Image URL workaround.

What’s special about it?

- It supports **dynamic images**
- It can read images directly from **measures**
- It works beautifully with **SVG strings**
- It supports **states and formatting**

This makes it perfect for building **smart visual indicators**.

## The Idea: Category Selection as a Visual Cue

We’ll use:

- A **Category slicer** (Apparel, Electronics, Furniture)
- An **Image visual**
- A **DAX measure** that returns different SVG images based on slicer state

## The image will change based on:

- ✅ Single category selected
- ✅ Two categories selected
- ✅ All categories selected
- ✅ No selection (default)

This gives the end user a **clear, intuitive signal** of what they’re looking at — without reading slicer values.

## The Magic Ingredient: SVG Images

Before we dive into Power BI, let’s talk about SVGs (Scalable Vector Graphics). Unlike raster images (PNG, JPG), SVGs are:

- **Text-based**: They’re essentially XML code describing shapes and paths
- **Scalable**: They maintain quality at any size
- **Editable**: You can modify colors, sizes, and properties programmatically
- **Lightweight**: Much smaller file sizes than traditional images

Most importantly for our use case — **they can be embedded directly into DAX measures as text strings**.

## Step 1: Find and Prepare Your Images 🌐

First, you need to source your images. Here are excellent free resources for icons and graphics:

- [**The Noun Project**](https://thenounproject.com/) — Massive library of icons for every concept
- [**Freepik**](https://www.freepik.com/) — High-quality vectors and illustrations
- [**Flaticon**](https://www.flaticon.com/) — Simple, clean icon sets
- [**IconFinder**](https://www.iconfinder.com/) — Searchable icon database
- [**SVG Repo**](https://www.svgrepo.com/) — Free SVG vectors and icons

Download icons that represent your categories. For our example, I used simple, recognizable icons for apparel (t-shirt), electronics (charger), and furniture (cupboard).

## Step 2: Convert Images to SVG Using Figma 🎨

Here’s where Figma becomes your best friend. Figma is a free design tool that makes extracting SVG code incredibly simple.

**The Process:**

1. **Open Figma** (create a free account if you don’t have one)
2. **Create a new design file**
3. **Import or paste your image** into Figma
4. **Select the image** you want to convert
5. **Right-click on the image**
6. **Navigate to Copy/Paste as → Copy as SVG**
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EtgM_qMIHdYCB8Zrm9ymuA.jpeg)

Save any image as SVG on Figma

That’s it! The SVG code is now on your clipboard. Figma automatically converts the visual representation into clean SVG XML code.

> ***P.S.: Similarly, for combination images, you can create a group with two or more image and convert them into SVG codes using the above-mentioned technique.***

## Step 3: Make the SVG Power BI-Ready

When you paste the copied SVG code into a text editor, you’ll see something like this:

```c
<svg width="225" height="219" viewBox="0 0 225 219" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M112.5 45.2C125.3 45.2..." fill="black"/>
</svg>
```

This is pure text — and that’s exactly what we need for Power BI. Power BI can render SVGs — but **only if the string is valid**.

To make it work inside DAX:

### You must:

1. Convert every `"` to `""`
2. Add this prefix at the beginning:
```c
data:image/svg+xml;utf8,
```

### Example (simplified):

```c
Apparel_SVG =
"data:image/svg+xml;utf8,
<svg width=""100"" height=""100"" viewBox=""0 0 100 100"">
  <rect width=""100"" height=""100"" fill=""black"" />
</svg>"
```

## Step 4: Tell Power BI This Is an Image

This step is **critical**.

Once your SVG measure is created:

1. Select the measure
2. Go to **Model view**
3. Set **Data Category** → **Image URL**

Without this, Power BI will treat the SVG as plain text.

## Step 5: Use the New Image Visual

Now the fun part 🎯

1. Insert the **Image visual**
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*uprn0ByAaLQp5Hy5rKi5-Q.jpeg)

The new image visual

2\. Set **Image source** → *Select from data*

3\. Drop your **SVG DAX measure** into the Data field

4\. Resize and position the visual as needed

![Use the new image visual to show the images as per the state of the slicer](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*R6TWgX8t2W1riNfsp0aYzg.jpeg)

Use the new image visual to show the images as per the state of the slicer

Your SVG will now render **perfectly inside Power BI**.

## What About Slicer Logic?

In this post, we focused on:

- SVG creation
- Image rendering
- Using the new Image visual

📌 **In the next blog**, I’ll walk through:

- How to detect slicer states in DAX
- Handling single vs multi-select
- Creating combination images
- Managing ALL / NONE selections cleanly
- Writing scalable, readable DAX for this pattern

That deserves a dedicated deep dive — and it’s coming next 😉

## Final Thoughts

This approach opens up **a whole new design space** in Power BI:

- Visual slicer indicators
- Status icons
- Smart legends
- Interactive storytelling
- IBCS-style visuals using SVGs

And the best part?

👉 **No custom visuals. No external tools. Just DAX and native Power BI.**

If you found this useful, please clap (***you can give me 50 claps👏 at a time***)

## About the Author:

Hi 👋 Thanks so much for reading! My name is **Ankan Bandyopadhyay,** a data visualization enthusiast/ Power BI Developer who believes that the best charts are the ones that disappear, leaving only the insights behind. Connect with me on **LinkedIn** to discuss data storytelling and visualization design.

☕ If you enjoy my articles and want to support me in writing more, you can [***buy me a coffee***](https://buymeacoffee.com/ankanbandyopadhyay) — every contribution means a lot and keeps this content going.

## Stay Tuned:

Make sure to [**follow me on Medium**](https://medium.com/@ankan.ab21) to access all my articles on advanced techniques in Power BI visualization.

## Connect or Follow Me Here:

- [***Medium***](https://medium.com/@ankan.ab21)
- [***LinkedIn***](https://www.linkedin.com/in/bandyopadhyay-ankan/)

Now go build something amazing! 🚀

*The contents of external submissions are not necessarily reflective of the opinions or work of* [*Maven Analytics*](http://mavenanalytics.io/) *or any of its team members.*

*We believe in fostering lifelong learning and our intent is to provide a platform for the data community to share their work and seek feedback from the Maven Analytics data fam.*

[*Submit your own writing here*](https://medium.com/learning-data/how-to-get-your-work-published-by-learning-data-with-maven-analytics-7df21e466a3e?sk=020dfac485597d602e218968d9ffb395) *if you’d like to become a contributor.*

*Happy learning!*

*\-Team Maven*