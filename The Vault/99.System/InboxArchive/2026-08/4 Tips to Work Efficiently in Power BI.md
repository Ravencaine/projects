---
title: "4 Tips to Work Efficiently in Power BI 🛠️"
source: "https://medium.com/the-bi-corner/4-tips-to-work-efficiently-in-power-bi-%EF%B8%8F-5a691a460d5f"
author:
  - "[[Isabelle Bittar]]"
published: 2024-02-18
created: 2026-08-03
description: "In It to Win It 🤠: Part 4 (Last One!) of Participating in the FP20 Analytics Challenge on Data-Driven Education Management"
Processed: "Unprocessed"
---
## In It to Win It 🤠: Part 4 (Last One!) of Participating in the FP20 Analytics Challenge on Data-Driven Education Management

![](99.System/Attachments/1!SxXVAqhN0Sf9Wv2Kvp5Wag.png.webp)

By Isabelle Bittar for KI Data Science

*🎁PBIX file available for download!*

### Introduction

As I complete my participation in the FP20 Analytics Challenge on Data-Driven Education Management, I wanted to share with you a few tips on how I work to help me develop reports quickly and effectively.

I will be honest; I was a bit hesitant about submitting my project because it wasn’t up to the standard I like to bring things to completion. I think in total, I might have only spent 10 hours working on the project… Work and life, in general, got intense 🙃, but as you might have read in some of my previous posts, I’m a big believer that it’s always worth submitting something rather than nothing, function over perfection, B- changes the world, you get the point 😉.

However, in submitting my work, despite it not being fully completed to my standards, I wanted to share with you 4tips that enable me to develop reports quickly. I believe that these are generally good practices and beyond helping me work faster, I like to think they also demonstrate ‘cleanliness’ and ‘organization’. When I open someone else’s report and see that these tips aren’t applied, it does guide me in assessing their level of experience/expertise (read: I judge them a little bit 😎).

### 1\. Organizing Measures in Folders

![](99.System/Attachments/1!ORP3HT47F5hsgAKnMvBZKA.png.webp)

Organizing Measures in Folders in Power BI

Measures can quickly accumulate in any Power BI project, and it’s important to have a systematic way of keeping them organized. I know some enjoy keeping measures within their data tables, but I personally like to organize them within folders in a centralized location.

Here is how you can create this central area to store all your measures. You basically need to load an empty table, add a measure, and then delete any columns it contains. Here is how I normally do it:

1. I use the ‘Enter data’ function from the Home tab to create a table. I don’t add anything to it. I only rename it, usually to ‘\_ *Measures’* or something with a *‘\_* ’ before the name so that it appears at the top of my tables. After this, I click on load.
![](99.System/Attachments/1!2r8a2GUM1p9whzwCZZ-xsQ.png.webp)

Creating an Empty Table for \_Measures in Power BI

2\. Then I create a blank measure (or any measure) and store it within that table.

![](99.System/Attachments/1!_B6f-6lfCCX2DyyedDJXMw.png.webp)

Creating a Blank Measure and Storing it in the \_Measures Table in Power BI

3\. As a final step, I delete the existing column of that table by right-clicking on it and selecting ‘Delete from model’. The table then becomes a measures group.

![](99.System/Attachments/1!bGcX4sOPR20s9hsnBHcwMw.png.webp)

Deleting the Existing Column in Power BI

To organize measures with folders and subfolders in this group, all you need to do is go to the Model view in Power BI and under the ‘Properties’ panel, assign your different measures to a ‘Display folder’.

![](99.System/Attachments/1!PqNwSTqaInkZQKK5tf9jCw.png.webp)

Assigning a Measure to a Display Folder in Power BI

You can also create subfolders by using the “”, such as in the following example where the measure `Font Last Semester Average Score Variation` is in the subfolder “Visualization” of the folder “Average Score”.

![](99.System/Attachments/1!E7VQHeCX09nqCbgTZsvvCA.png.webp)

Assigning a Measure to a Sub-Folder in Power BI

### 2\. Organizing and Renaming Elements in the Selection and Bookmarks Panels

he minute my report has over 10 elements (whether it’s visualization, text boxes, or other shapes), I find it’s worth renaming them and organizing them within the Selection panel. Not only is it more organized for future reference, but I also find that this methodology speeds up a lot of development work.

To open the Selection panel, you need to go to ‘View’ and click on ‘Selection’. This is currently what my selection panel looks like.

![](99.System/Attachments/1!J_flnXYIFkGH4tFPNr04tg.png.webp)

Opening the Selection Panel in Power BI

As you can see, all elements have been renamed and sometimes even grouped together. Now that I am looking back at my file, I see I could have grouped categories even more.

To rename elements, you just need to double-click on them and retype their names. To group them together, you can select them, right-click and choose ‘Group’. Having elements properly organized in the selection panel also makes it easier to manage bookmarks.

Similar to the Selection panel, it’s also worth properly organizing your bookmarks in groups when you start having multiple. In this report, I used a lot of bookmarks 😅, see below:

![](99.System/Attachments/1!clLdlJv81wIsPeOr8voXkQ.png.webp)

Opening the Bookmarks Panel in Power BI

I For more information on how to use the Selection and Bookmarks panels in Power BI, you can view my previous article where I demonstrate how to build an interactive tutorial within your report leveraging these features:

## [Power BI Unleashed: Building Interactive Tutorials That Stick](https://medium.com/microsoft-power-bi/power-bi-unleashed-building-interactive-tutorials-that-stick-95f97da8eef0?source=post_page-----5a691a460d5f---------------------------------------)

### In It to Win It 🤠: Part 3 of Participating in the FP20 Analytics Challenge on Data-Driven Education Management

medium.com

### 3\. Logging All Additional Values in a Parameter File or Distinct Variables (No hard-coding through DAX!)

It’s good practice to avoid hard-coding any values that are not provided within your Power BI data model. For most data-related values, I like to store them in an excel parameter file that I then upload to my data model. For visualization values, I like to store them in distinct DAX measures. Here is how:

**Storing Values in a Parameter File**

For this project, the competition brief instructed us that some intervention groups could take on 10 students per teacher (tier 2), while others could take on only 5 students per teacher (tier 3). These values (5 and 10) are not part of the data model. Instead of hardcoding them in the DAX measures that were required to calculate the number of teachers needed for the intervention groups, I stored them in an Excel sheet.

![](99.System/Attachments/1!lh9I2L-REcCjs1ygyndwBQ.png.webp)

Storing Teaching Requirements Values in Excel

I then loaded this Excel sheet in Power Query and made no connection to this table (“Teaching Requirements”) to the data model. To retrieve the values, I then created the following DAX measures:

```c
Tier 2 Teaching Requirements = 
    CALCULATE(
        MAX('Teaching Requirements'[Students per teacher]),
        FILTER(
            'Teaching Requirements',
            'Teaching Requirements'[Group] = "Tier 2"
        )
    )

Tier 3 Teaching Requirements = 
    CALCULATE(
        MAX('Teaching Requirements'[Students per teacher]),
        FILTER(
            'Teaching Requirements',
            'Teaching Requirements'[Group] = "Tier 3"
        )
    )
```

Why do it this way? In real life, when values not part of a dataset are given by users (other examples: benchmarks, targets, etc.), there always is a chance that they change/evolve. To avoid having to republish your Power BI report when these changes occur, all you need to do is make the adjustment in your parameters file and refresh your data source within Power BI services. Not only does it facilitate updates, but it also enables the business users to bring updates to some of these types of variables without having to open the PBIX.

**Storing Visualization Values in Distinct Measures**

There is often a lot of visualization that is being handled within my measures in my Power BI reports, such as data label colors, text style, icons, etc.

For example, in my report, I use the colors red and green to outline good and bad variations or highlights across the data. The colors of metrics are determined by DAX measures.

![](99.System/Attachments/1!PGPk5R9cvH71ss7EOldUbg.png.webp)

Examples of Colors Being Rendered by a DAX Measure

Since I want to ensure consistency in always using the same shades of a color, I store them in DAX measures, like the following:

```c
Color Green = "#2C6D6A"

Color Red = "#D8404A"
```

I then reference these DAX measures when I want to apply the “Red” or “Green” color. Not only does it ensure consistency in the colors being used, but it also makes it easier if you need to bring updates to your report theme or its color palette (which is something I often do 😅).

### 4\. Don’t Start From Scratch Each Time

As you develop Power BI projects, you gain experience, expertise, and you start building your own working assets. These include, but are not limited to:

- Visualization templates
- DAX calculations
- Power Query data table creations and transformations

To give you an example, the measures I have stored under “HTML Setup” are some that I have developed only once and used multiple times.

![](99.System/Attachments/1!hpNi4IiifMNN13UfeKZ5aQ.png.webp)

HTML Set Up Measures I Created Once and Reuse Often

Bas from How To Power BI recently developed this cool video where he shows how he stores his project assets using GitHub. I currently have most of my stuff stored in “Master” Power BI files, but I’ve been slowly transitioning to GitHub 🤓…

### Conclusion

That’s all for this short post! The winners of the challenge should be announced this week. I will make sure to comment on this article which reports won for those that are curious!

🎁 [**Here is my Power BI file!**](https://drive.google.com/file/d/1ma8bb4PVvLNZuVdq9gywXkF3xKOowK6Q/view?usp=sharing)

In the meantime, what are your tips to work effeciently in Power BI? I would love to hear from you! 🤩

As well, if you have any suggestion on subjects you would like me to cover in the future, please let me know! Thank you so much for your readership! 🤗

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X (Formerly Twitter)***](https://twitter.com/KI_Datascience)