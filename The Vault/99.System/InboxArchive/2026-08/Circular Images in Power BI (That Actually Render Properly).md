---
title: "🟠 How to Create Circular Images in Power BI (That Actually Render Properly)"
source: "https://medium.com/microsoft-power-bi/how-to-create-circular-images-in-power-bi-that-actually-render-properly-6d51849415d6"
author:
  - "[[Isabelle Bittar]]"
published: 2025-12-11
created: 2026-08-04
description: "The solution: a robust approach using Power Query + SVGs"
Processed: "Unprocessed"
---
## The solution: a robust approach using Power Query + SVGs

![](99.System/Attachments/1!vp_SGNFlxpINKj_O6BEHIA.png.webp)

By Isabelle Bittar for KI Data Science

*PBIX available for download at the end of this article!🥳*

## Introduction

So I’ve been running into this problem (or challenge) for a while: cropping images — profile pictures, avatars, property images, and more — into circular shapes for table visuals. The image data I usually have access to comes in rectangular or square formats, but for many of my designs, it just *feels* like these images would look much better if they were circular.

Since this was an aesthetic improvement — and definitely not a priority when delivering projects 😅 — I never spent **too** much time trying to figure out a proper solution.

But now… I did! 😁  
And I’m happy to share it with you, in case this is also something you’ve been wanting to improve in your data table visuals.

![](99.System/Attachments/1!ZGmU3M1xX4n9irzpxwYRGg.png.webp)

Here is a short demo video of the visual in the cover picture in action:

🟠 How to Create Circular Images in Power BI That Actually Work

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## The problem: Power BI doesn’t support image masking

Here’s the core issue:

- Power BI images are **often rectangular**
- There is **no built-in image masking or cropping**
- You can’t simply say “make this image a circle”

So naturally, many of us turn to SVGs — because SVGs *do* support masks and clipping paths.

My first instinct to handle this was to do something like this, combine with a circular clipPath.

```c
<image href="https://my-image-url.jpg" />
```

But it didn’t work 😅.. I always would get a broken image icon.

The reason is simple (and frustrating):

> ***Power BI blocks external image URLs referenced from inside SVGs.***

So while SVG *supports* it, Power BI doesn’t reliably allow it.

That’s the root of the problem.

## The robust pattern (key concept)

After some trial and error, here’s the pattern that *actually* works consistently:

**Circular image =**

1. ✅ Image stored as **Base64**
2. ✅ SVG used *only* for **shape and layout**
3. ✅ SVG returned as a `data:image/svg+xml` string

Once you separate **image data** from **presentation**, it works 🙌. Below are the two steps you need to complete for it to also work for you 😁:

## Step 1 — Convert images to Base64 (Power Query)

The first step happens in **Power Query**.

Instead of keeping a raw image URL, we:

- download the image
- convert it to Base64
- store it as text

This is a *one-time preparation step*.

To do this, I first created the following function in Power Query:

```c
// fxImageToBase64
let
    fxImageToBase64 = (ImageUrl as text) as text =>
    let
        Source      = Web.Contents(ImageUrl),
        AsBase64    = Binary.ToText(Source, BinaryEncoding.Base64),
        // change jpeg/png if needed
        DataUrl     = "data:image/jpeg;base64," & AsBase64
    in
        DataUrl
in
    fxImageToBase64
```

Then, in the table where I had the Image URL data, I created a custom column invoking this function.

In my case, it was in my `Employees` table:

1. **Added Column → Invoke Custom Function**
2. Function: `fxImageToBase64`
3. Argument: `Employees[Image]` (your current URL column)
4. Name the new column: `ImageBase64`

Now `Employees[ImageBase64]` contained values like `data:image/jpeg;base64,/9j/4AAQSk…`.

This approach:

- works for JPGs and PNGs
- is ideal for internal assets or demo datasets
- avoids all external-call issues inside SVGs

⚠️ A quick note:

- Base64 strings can get large
- It’s best used with reasonably sized images
- For massive image libraries, you’ll want to be mindful of model size

(For demo files and controlled datasets, it’s perfect.)

## Step 2 — DAX SVG: the circular mask

Now comes the fun part 😁

In DAX, we generate an SVG that:

- defines a circular `clipPath`
- places the Base64 image inside it
- handles scaling and centering correctly

In my case, here was my DAX measure:

```c
Profile Image (SVG) = 
VAR ImgDataUrl =
    SELECTEDVALUE ( 'Employees'[ImageBase64])
RETURN
IF (
    NOT ISBLANK ( ImgDataUrl ),
    "data:image/svg+xml;utf8," &
    "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 150 60"">" &
        "<defs>" &
            "<clipPath id=""clipCircle"">" &
                "<circle cx=""50"" cy=""50"" r=""50"" />" &
            "</clipPath>" &
        "</defs>" &
        // Optional light grey background circle
        "<circle cx=""50"" cy=""50"" r=""50"" fill=""#eeeeee"" />" &
        "<image href=""" & ImgDataUrl & """ " &
            "x=""0"" y=""0"" width=""100"" height=""100"" " &
            "preserveAspectRatio=""xMidYMid slice"" " &
            "clip-path=""url(#clipCircle)"" />" &
    "</svg>"
)
```

Key SVG concepts doing the heavy lifting:

- `clipPath` → circular crop
- `preserveAspectRatio="xMidYMid slice"` → smart centering
- optional background circle → cleaner loading and contrast

Once returned as an SVG data URL, Power BI renders it perfectly inside tables.

⚠️ When inserting the measure in your data table, make sure the selected data format is Image URL and adjust the image size of the table visual to match what was in the measure.

![](99.System/Attachments/1!6FUkDrbhvxYN0TcYe1_bMw.png.webp)

Setting the Data Format of the Measure to Image URL and Adjusting the Table Visual’s Image Size in Power BI

If you are interesting in learning more about using SVGs in Power BI, [**here**](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d) ’s is my article on the topic.

## [Step Up Your Power BI Game With SVGs 🔥](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d?source=post_page-----6d51849415d6---------------------------------------)

### Building a Crypto Market Watch Dashboard in Power BI Using SVGs

medium.com

## Reusing the same pattern

This is where the approach really shines 🌟

The *exact same logic* can be reused for:

- employee avatars
- building photos
- product images
- asset previews

No new logic.  
No new visuals.  
Just a different image source.

That’s what makes this feel less like a “hack” and more like a **design pattern** you can adopt across reports.

## Optional enhancements (UX candy 🍬)

Once you’re comfortable with SVGs, it’s very easy to go further:

- colored borders by status
- category rings (like department or type)
- image padding for different densities
- fallback shapes or initials when images are missing
- consistent sizing across all tables

This is where Power BI starts feeling less like a reporting tool…  
and more like a **UI framework** 😉.

In my case, I went a step further and developed a measure that integrated also the employee name and their email address within the same table cell:

```c
Profile Card (SVG) = 
VAR ImgDataUrl =
    SELECTEDVALUE ( 'Employees'[ImageBase64] )
VAR _Name  =
    SELECTEDVALUE ( 'Employees'[Member] )
VAR Email =
    SELECTEDVALUE ( 'Employees'[Email] )

VAR NameEsc  = SUBSTITUTE ( _Name,  "&", "&amp;" )
VAR EmailEsc = SUBSTITUTE ( Email, "&", "&amp;" )

RETURN
IF (
    NOT ISBLANK ( _Name ),
    "data:image/svg+xml;utf8," &
    "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 320 60"">" &

        // --- Avatar mask ---
        "<defs>" &
            "<clipPath id=""clipCircle"">" &
                "<circle cx=""30"" cy=""30"" r=""24"" />" &
            "</clipPath>" &
        "</defs>" &

        // Optional avatar background (light grey circle)
        "<circle cx=""30"" cy=""30"" r=""24"" fill=""#eeeeee"" />" &

        // Avatar image
        IF (
            NOT ISBLANK ( ImgDataUrl ),
            "<image href=""" & ImgDataUrl & """ " &
                "x=""6"" y=""6"" width=""48"" height=""48"" " &
                "preserveAspectRatio=""xMidYMid slice"" " &
                "clip-path=""url(#clipCircle)"" />",
            ""
        ) &

        // --- Text styles ---
        "<style>" &
            ".name  { font-family:'Segoe UI Light', sans-serif; font-size:14px; font-weight:600; fill:#111111; }" &
            ".email { font-family:'Segoe UI Light', sans-serif; font-size:11px; fill:#888888; }" &
        "</style>" &

        // Name (bold)
        "<text x=""70"" y=""26"" class=""name"">" &
            NameEsc &
        "</text>" &

        // Email (grey, under name)
        "<text x=""70"" y=""42"" class=""email"">" &
            EmailEsc &
        "</text>" &

    "</svg>"
)
```

### The Final Visual

![](99.System/Attachments/1!_NksXJP0MMwXAxPcRLLeSA.png.webp)

Department SVG Pill Developed with a Reusable UDF

If you like the SVG Pill used to illustrate employees department, I actually built it using a reusable UDF for any SVG pills. You can access it with the full tutorial [**here**](https://medium.com/microsoft-power-bi/one-udf-to-build-all-your-svg-pills-in-power-bi-43da8ca9058e).

## [⚡One UDF to Build All Your SVG Pills in Power BI](https://medium.com/microsoft-power-bi/one-udf-to-build-all-your-svg-pills-in-power-bi-43da8ca9058e?source=post_page-----6d51849415d6---------------------------------------)

### A flexible, scalable way to generate beautiful SVG pills for statuses, priorities, and tags using Power BI’s new…

medium.com

## Final thoughts

This was never a *priority* feature in my projects — and probably shouldn’t be 😅.  
But I’m really happy I figured it out — small visual details add up, especially in tables people interact with every day.

If circular images are something you’ve wanted to improve in your Power BI tables, I hope this helps 🙌

👉 **PBIX file available** [**here**](https://drive.google.com/file/d/1oiV-jshB2pWYJivmOKGdUpv-DH7Cdevl/view?usp=sharing) if you want to explore or reuse the pattern.

Happy building! 🎉

## Enjoy building attractive tables in Power BI? ✨📋

If you are like me and appreciate UI and UX friendly data tables 🤓, you might enjoy these articles:

## [Better UX for Large Data Tables in Power BI](https://medium.com/the-bi-corner/better-ux-for-large-data-tables-in-power-bi-292d4dfc6862?source=post_page-----6d51849415d6---------------------------------------)

### Because even the most boring tables deserve great design

medium.com

## [Transforming Power BI Tables: 6 Expert Tips for Smarter Data Visualization](https://medium.com/the-bi-corner/transforming-power-bi-tables-6-expert-tips-for-smarter-data-visualization-7dc7068870ff?source=post_page-----6d51849415d6---------------------------------------)

### Boost User Experience with These Power BI Table Enhancements

medium.com

## About the author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or follow me here:

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

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----6d51849415d6---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization