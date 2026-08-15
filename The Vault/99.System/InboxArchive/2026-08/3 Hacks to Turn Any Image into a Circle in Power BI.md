---
title: "3 Hacks to Turn Any Image into a Circle in Power BI"
source: "https://datatraining.io/blog/3-hacks-image-to-circle"
video_url: "https://www.youtube.com/watch?v=exTSUPJPSqE"
video_file: 99.System/Attachments/Video/3 Hacks to Turn Any Image into a Circle in Power BI-exTSUPJPSqE.webm
transcript: "[[3 Hacks to Turn Any Image into a Circle in Power BI - transcript]]"
author:
  - "[[datatraining]]"
published:
created: 2026-08-13
description: "You’re using images in your Power BI reports - but they show up as squares. What you want are clean, circular Images. Totally doable.In this blog, I’ll show you three different ways to do it."
Processed: "Processed"
---
![[3 Hacks to Turn Any Image into a Circle in Power BI-exTSUPJPSqE.webm]]

You’re using images in your Power BI reports - but they show up as squares. What you want are clean, circular Images. Totally doable. In this blog, I’ll show you three different ways to do it.

power bi visual images base64

Which one’s “easiest” depends on your situation (do you have the actual files or only URLs? fixed cards or scrolling tables?). Let’s have a look together.**  
  
Quick Decision Guide**

| **Situation** | **Best Option** |
| --- | --- |
| You have a handful of local image files and can update them once | A. Pre‑process images (PowerPoint or Python) |
| Images are always in a fixed position on the page (e.g., a card header) | B. Circular overlay (mask) |
| You only have image URLs, need images inside tables or lists, and content changes regularly | C. SVG measure with Base64 images |

![](https://lwfiles.mycourse.app/datatraining-public/a5b99bf283666a98c6b7c43aef452549.png)

**Circular Images in PowerPoint (when you have the files)**

**Ideal scenario**: you have direct access to the image files used in your report (not just URLs). Example: the images live on your laptop or a shared drive.**  
  
Steps:  
**1\. Open PowerPoint and insert the image.

2\. Go to Picture Format → Crop to Shape → Oval. (Resize as needed; hold Shift to keep it perfectly round.)

3\. Right click → Save as Picture… (PNG recommended). Repeat for the images you need.

4\. Host the new circular images where your model can reach them (e.g., Dropbox/OneDrive/SharePoint).

![](https://lwfiles.mycourse.app/datatraining-public/49c12017f1f3767057e9c6503b860ba2.png) ![](https://lwfiles.mycourse.app/datatraining-public/18da99fbbfc2898abd692332253c623e.png)

\- Original links column (example): Img Link

\- New links column (example): Img Circle Link

5\. Use the circular URLs in Power BI:

\- In Power BI Desktop → View/Column tools, set the Data category for Img Circle Link to Image URL.

\- In the Card (or another visual) turn Images = On → Image type = Image URL → click fx → Field value → select ImageURL\_Circle.

That’s it - your visuals now render the circular assets.**  
  
Pros**: quick, no code.

**Cons**: manual; not scalable for hundreds of images.

![](https://lwfiles.mycourse.app/datatraining-public/222ed3c6585b1c9c66272674b52aa8c9.png) ![](https://lwfiles.mycourse.app/datatraining-public/ba71d33d4c405702d6402b4ed57332c8.png) ![](https://lwfiles.mycourse.app/datatraining-public/00d61b206dd29a0b5f44547cc1f76b2a.png)

**Python Script (batch process many local files)**

When you’ve got lots of images, you can batch‑convert them to circles. You don’t need to “know Python” to run a simple script. You can just use Chatgpt or Claude to generate the script.  
Of course to do this, you need to have the right libraries installed but just prompt to write a python script to make all the images in the folder circular.

![](https://lwfiles.mycourse.app/datatraining-public/7cce1a87251bf77d3d6760e3d4638df8.png)

Now go to the command prompt, go to the folder and run the generated script. That is it, there we have the circular version of them. If you need to also generate a list of URLs programmatically, use a second small script.

![](https://lwfiles.mycourse.app/datatraining-public/5acd709be99e61d0d4b661d3ac3c1fb2.png)

Next, we do not have the files directly on the laptop. Then how do we approach? Here we have 2 routes – the easy way and a tricker one but flexible.  
  

Let’s look at the easy route first.  
  

**Circular Overlay (mask) in the report  
**  

In this variation, the donut frames an image, such as an employee photo or product icon, making the metric more personal or contextual.  
  
Let’s not over complicate it. If your images always show in the same position (e.g., in a profile card), a circular overlay can do the trick.

**Steps:**

1\. Create a mask PNG: white on the outside, transparent in the middle (a circular “hole”).

2\. In Power BI Desktop → Insert → Image, add the mask PNG, resize, and place it over the square image until it aligns.

**How to make the mask in PowerPoint  
  
**

1\. Draw a square/rectangle (slide size).

2\. Insert a circle where the image should show.

3\. Shape Format → Merge Shapes → Combine to punch the hole.

4\. Set Fill to match your report background (e.g., white). No outline. Save as PNG.

Note: This won’t work in tables/matrices - when you scroll, the overlay stays put while rows move. Use it for static placements only.

![](https://lwfiles.mycourse.app/datatraining-public/81d5c71f5e0c7f81f7662b1dc8bd4af9.png)

Once we overlay, it looks perfect when static as in first image here, however when we attempt to scroll (in table, etc.), it doesn't and so it takes us to our next option.  

![](https://lwfiles.mycourse.app/datatraining-public/c2037107035b3bb8d59c7387978dd2f6.png) ![](https://lwfiles.mycourse.app/datatraining-public/a32a4c08732d970b2ed26eef123a2e69.png)

**Image Circle Measure (SVG), when you only have URLs  
**  

What if you just have the image links? This is the trickier solution but very effective. If you only have image URLs and need circles inside tables/lists, use a DAX measure that renders an SVG with a circular clip.  
There’s one catch: Power BI typically blocks external URLs inside SVG. The workaround is to embed the image as Base64.

Convert URL → Base64 in Power Query

Home → New source → Blank query → **Advanced Editor** and write a function like:

![](https://lwfiles.mycourse.app/datatraining-public/913df5d00ad40740d7395dabfa2b8d6a.png)

- Invoke the function for your URL column to create a new Base64 column (e.g., ImageBase64) and then use this in the measure and check.

![](https://lwfiles.mycourse.app/datatraining-public/2abe4f197c520023c258b836131f5e6e.png)

- If your strings are too long (practical text limit ~32k characters), resize/compress before encoding (I use a external tool here) example shown below but it also depends on if you can use external tool for your case. But this is just another way to do. In my example, I have then modified the function to handle this by an external one.

![](https://lwfiles.mycourse.app/datatraining-public/b8e82c0a703b745d5b489f0d321914f5.png) ![](https://lwfiles.mycourse.app/datatraining-public/7ecb90346454f3f93be6ab2f65382a46.png)

Once the changes are made, we can use this in our measure and there we have the circular version of the image. We have to definitely double check if it's fine to use that external one with those images that you're visualizing.

**  
Wrap up**  
  
Pick the lightest option that fits your scenario. With a small, focused tweak, you’ll bring the look you expect to life.

**Hope you like it!**

Give it a try and see how it works for you! I’d love to hear what you think or see how you use this trick in your own reports.

How to Power BI