---
title: "Building Interactive Tutorials That Stick in Power BI"
source: "https://medium.com/microsoft-power-bi/power-bi-unleashed-building-interactive-tutorials-that-stick-95f97da8eef0"
author:
  - "[[Isabelle Bittar]]"
published: 2024-02-12
created: 2026-08-03
description: "In It to Win It 🤠: Part 3 of Participating in the FP20 Analytics Challenge on Data-Driven Education Management"
Processed: "Unprocessed"
---
## In It to Win It 🤠: Part 3 of Participating in the FP20 Analytics Challenge on Data-Driven Education Management

![](99.System/Attachments/1!tK0f6qdlgGMcXHC8LImKnQ.png.webp)

Report in Progress By Isabelle Bittar for KI Data Science

*🎁PBIX file available for download at the end of this article!*

### Introduction

I think one of the most frustrating parts after delivering a Power BI project to users or clients is discovering they aren’t using or had no idea about some of the really cool features that I worked very hard on developing. Features like drill-downs, applying slicers, and using tooltips are commonly missed by users, especially those with less experience navigating BI tools.

A solution I previously found to this common problem was building an info window that would provide navigation guidelines. However, let’s be real, it looks boring 🥱 and I am sure that many (if not most!) users rarely consult it AND read through EACH bubble 😥.

![](99.System/Attachments/0!S4cwb06DBIUnfQy0.png.webp)

M&A Planning Dashboard by Isabelle Bittar for KI Data Science

So, I found a way of developing an interactive tutorial that offers a more dynamic experience to users by going through one feature at a time in your Power BI report. Here is a short video of what the navigation looks like:

Achieving this is pretty simple! All we do is work with the ‘Selection’ and ‘Bookmarks’ panels (no DAX required!). In the following text, I will demonstrate how I built this for an analytics competition I am participating in: The FP20 Analytics Challenge on Data-Driven Education Management. Reports are due February 15, mine is still in progress, but the interactive tutorial section is working 😅.

### Good UX Practices to Consider

Before diving into how to technically achieve this in Power BI, I wanted to share some good practices I consider when building this type of interactive tutorial 🥸.

- **Use Images of People**: People like to listen or interact with people. Using persona images that are mimicking people can encourage the user to be engaged in the experience and read through the instruction.
- **Use Verbs**: While we want to favor short texts, it’s good to use verbs like “You can hover, click on this button, apply filters, etc.” to engage the user in the actions they can do.
- **Keep the Language Simple**: Use simple language and keep in mind your user’s vocabulary. For example, I’ve rarely heard a non-BI/developer person say “slicer”. Use the word “filter”, we know it’s not the same, but we’re not creating a whole tutorial on Power BI — just about how to make the report work for them.
- **Keep it Short**: I have nothing to prove it, but I’m sure there is an inverse relationship between how long your tutorial is and how likely the user will go through the whole thing, so keep it tight. Less work for you and everyone is happier!

The next section will focus on the steps I did in Power BI to achieve this interactive tutorial within my report.

### Step 1: Create the First Information Bubble

The first step was to create the initial information bubble I wanted to display when the tutorial started.

From the ‘Insert’ tab in Power BI, I added the following five elements on top of the current version of my report. Here is the anatomy of each one of my information bubbles:

![](99.System/Attachments/1!P_9SWKiUDSksw0DIxyKT_g.png.webp)

Anatomy of Custom Information Bubbles in Power BI

Since we are dealing with a lot of elements, it’s helpful to start using the ‘Selection’ panel to rename all objects to make it easier to manage. To achieve this, go into ‘View’ and click on ‘Selection’.

Once the ‘Selection’ panel is open, you can double-click on each object and start renaming them. Below is how I renamed the elements I was using for my first info bubble. I then grouped them by selecting them all, right-clicking, and then selecting ‘Group’. I named this first group ‘Info Filter’.

![](99.System/Attachments/1!KO-V1BWFpZTC1wLlKVdxqw.png.webp)

Opening the Selection Panel and Renaming Objects in Power BI

To view in detail the formatting steps applied to each element, you can download the Power BI file available at the end of this article.

### Step 2: Create the Subsequent Information Bubbles

With the first information bubble created, you can copy the group of elements and adjust them to create the next bubble. To do this, select the group and use your keyboard to copy-paste it (Ctrl + C and Ctrl + P). Once done, you will have two identical groups of elements. You can hide your initial group and then start modifying the second group based on the type of information you want to display.

In my case, the second information bubble was to explain how the date picker worked. I made the required adjustments to the picture and text box, finishing off by appropriately renaming my elements in the Selection panel.

![](99.System/Attachments/1!gs1_Ny86_5rBOpiSj79kwA.png.webp)

Creating the Subsequent Information Bubble in Power BI

You can then repeat this step for all the information bubbles you want to display within your tutorial. I had six in total for my report, all grouped under ‘Tutorial’ in the ‘Selection’ panel.

![](99.System/Attachments/1!DOX2X0mW3izyBIh5mjwrNA.png.webp)

Information Bubbles Grouped Under the Tutorial Heading in Power BI’s Selection Panel

### Step 3: Create Bookmarks to Display and Hide the Different Information Bubbles

The next step is to create the required bookmarks to show and hide the grouped elements of the different information bubbles. We will use these to assign them to the buttons of each information bubble.

Similar to the ‘Selection’ panel, open the ‘Bookmarks’ panel by selecting it from the view tab.

![](99.System/Attachments/1!xNDMgk2HA1PrmpAiCkKJ9A.png.webp)

Opening the Bookmarks Panel in Power BI

**Creating the First Bookmark: Tutorial Close**

The first bookmark I created was by selecting the group ‘Tutorial’, hiding it, and then inserting a bookmark that I called ‘Tutorial Close’. Then, by right-clicking on it, I deselected ‘Data’ and selected ‘Selected visuals’.

![](99.System/Attachments/1!T1Fdm3gITp-hakqhT81_4g.png.webp)

Creating the First Tutorial Close Bookmark in Power BI

The reason I deselected ‘Data’ was that I wanted this bookmark to ignore the way slicers or filters are currently applied (e.g., dates). Meaning, if the user had selected a different date, applying the ‘Tutorial Close’ bookmark wouldn’t revert the user’s date selection.

I also clicked on ‘Selected visual’ (instead of the default ‘All visuals’) because I only wanted the bookmark to capture the actions I was registering for the elements I had selected under the ‘Selection’ panel.

**Creating the Second Bookmark: Tutorial Filter**

The second bookmark I created was to display all the elements of the information bubble I titled ‘Info Filter’. To do this, I selected the elements of this group under the ‘Selection’ panel, made them visible, and then added a bookmark that I renamed ‘Tutorial Filter’. I also deselected ‘Data’ and selected ‘Selected visuals’ by right-clicking on this bookmark.

![](99.System/Attachments/1!L55KHectyh9PM2y_10OLKA.png.webp)

Creating the Second Tutorial Filter Bookmark in Power BI

**Creating the Subsequent Bookmarks for All the Other Information Bubbles**

I repeated this step for each information bubble to create a bookmark that made them visible. Here were all the bookmarks I created in Power BI. I selected them all, then right-clicked to group them under the ‘Tutorials’ heading.

![](99.System/Attachments/1!0dbw_0_aUd-cTJoitMvf8Q.png.webp)

All Tutorial Bookmarks Created in Power BI

### Step 4: Assigning the Bookmarks to the Buttons

This is where it all comes to life: assigning these bookmarks to the buttons in each information bubble to make the navigation interactive!

I first added a transparent button over the image and text on my report page. In the Format panel of this button, I turned on ‘Action’, assigned ‘Bookmark’ as its type, and selected the bookmark ‘Tutorial Filter’, so when the user clicks on this button, the first information bubble on the filter appears.

![](99.System/Attachments/1!UnToR7Hs3BHaKbLlqIKDrA.png.webp)

Assigning the First Bookmark to a Button in Power BI

Then, with the first information bubble ‘Info Filter’ open, I went on and assigned the bookmarks ‘Tutorial Close’ and ‘Tutorial Date’ to the ‘End tutorial’ button and ‘Next’ button, respectively.

![](99.System/Attachments/1!TV5Ozi1xpU7SY_XL400rEA.png.webp)

Assigning Bookmarks to Buttons for Info Bubbles in Power BI

I repeated this step for all the info bubbles, ensuring to apply the bookmark of the next info bubble I wanted to display to the ‘Next’ button.

### Wrapping Up!

As shown in this tutorial, you can showcase all the cool features in your Power BI reports you don’t want your users to miss by leveraging the ‘Bookmarks’ and ‘Selection’ panels.

I hope this was helpful or inspired you in creative additions you can include in your future projects 🧑🎨!

Let me know what you think and if you have any recommendations for future articles 🙏😁!

[**Here**](https://drive.google.com/file/d/1mSXZTR7BnRPK0Di_WWDNQ_1keeUbeh_g/view?usp=sharing) **is the PBIX file to see in more detail all my formatting options🙂.**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X (Formerly Twitter)***](https://twitter.com/KI_Datascience)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)