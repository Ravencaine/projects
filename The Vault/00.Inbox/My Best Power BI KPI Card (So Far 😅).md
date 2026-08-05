---
title: "My Best Power BI KPI Card (So Far 😅)"
source: "https://medium.com/the-bi-corner/my-best-power-bi-kpi-card-so-far-deb7513ff3be"
author:
  - "[[Isabelle Bittar]]"
published: 2025-01-04
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!AHBe5KWyo3kn-n1R-IkvAQ.png.webp)

By Isabelle Bittar for KI Data Science

🎁 *PBIX available for download at the end of this article!*

### Introduction

Last year, I had the chance to work with a variety of different clients, and I find this so enriching because it exposes me to **different contexts** that push me to create **unique visuals**. Most of my clients are **large enterprises**, but in this case, it was a **community gym ⛹️** that wanted a dashboard to **track member engagement** and **identify potential churn factors**.

What was especially exciting about this project was that they had **image data** of their members! And I REALLY wanted to use it — since I’ve rarely (**never? 😅**) had the opportunity to work with **profile images** in a **real project**.

In this article, I’ll explain the **steps I followed** to create this **KPI card**. It dynamically displays:

- The **percentage of members** who went to the gym at least **3 times** during the **selected week**.
- The **profile images** of members with the **most visits**.

You can even **hover over the images** to see a **detailed list** of all members who attended **3+ sessions** that week!

### Anatomy of the KPI Card

Here’s an **overview** of how I structured the KPI card (including visuals, measures, and columns). As you’ll notice, most of the layout consists of **text boxes and shapes**, but the **highlight** (the **Top Members of the Week**) and its **tooltip** were built using the **HTML Content visual**.

![](99.System/Attachments/1!yv5seQAi1oR-68oBAk-Jqw.png.webp)

Anatomy of the KPI Card Created in Power BI

### 1\. The Dataset

![](99.System/Attachments/1!s57qPk56-m_wk3W5lmkN0A.png.webp)

Data Model to Create KPI Card in Power BI

This KPI card was developed using **mock data** generated with **ChatGPT**. It’s a **simplified version** of what I was working with in reality, but the **data model** contains **three key tables**:

- **GymLogs**: Logs each member’s **check-in and check-out times**.
![](99.System/Attachments/1!wLQxwJkTSbwQdi0OwSpzqg.png.webp)

GymLogs Table in Power BI

- **Members**: Stores **member names** and **profile images** (which I sourced from **Unsplash 🎉**).
![](99.System/Attachments/1!u1k3UKrZzUZRiZRPqYBeLw.png.webp)

Members Table in Power BI

- **Dates**: A **date table** I created in **Power Query** to support the **Week Range slicer** at the top of the KPI card.
![](99.System/Attachments/1!QNKKwKOk5F_8c-cn1D8Omw.png.webp)

Dates Table in Power BI

Note: I won’t dive too much into the data transformation steps here — they’re well-documented in the **Power Query code** in the download.

### Step 1: Building the Initial KPI Card Frame

![](99.System/Attachments/1!wsLT_yyZM2F2AL7d80f3Rw.png.webp)

Preparing the Initial KPI Card Frame in Power BI

1. **Preparing the Layout:** I started by designing the **background frame** for the KPI card:
- **Background Shape:** Added a **rectangle** with **rounded corners** and a **shadow**.
- **Text Boxes:** Placed text boxes for the **indicator descriptions**.

**2\. Adding a Date Slicer:**

- Added a **dropdown slicer** based on the **WeekRange** column from the **Dates table**.
- Since it’s a **text column**, I made sure it was **sorted** by the **StartOfWeek** to display weeks in the **correct order**.
![](99.System/Attachments/1!HYYYAVO__HFhnYkmOV5Z4g.png.webp)

Soring the WeekRange Column by the Dates\[StartOfWeek\] in Power BI

3\. **Custom Icon Button**: Finally, I added a **blank button** with a **custom SVG icon** I designed in **Figma**. While there’s **no action** tied to this button in the demo, it was linked to a **report section** with **detailed member activity** in the original dashboard.

![](99.System/Attachments/1!P4ZQXjyS65DHUajWxXqiyA.png.webp)

Adding a Custom Icon to a Blank Button in Power BI

### Step 2: Adding the Main Components

![](99.System/Attachments/1!2Wicyfocrwh6YMWSlA92MA.png.webp)

Adding the Main Components to the KPI Card in Power BI

Next, I created a few **straightforward DAX measures** to calculate the **percentage of members** who attended **3 or more sessions** during a **selected week**.

```c
Sessions = COUNTROWS('GymLogs')

Members = DISTINCTCOUNT('GymLogs'[Member])

Members with 3 Sessions or More = 
    CALCULATE(
        [Members],
        FILTER(
            'Members',
            [Sessions] >= 3
        )
    )

Percentage of Members with 3 Sessions or More = 
    DIVIDE(
        [Members with 3 Sessions or More],
        [Members]
    )
```

I was then able to added the final measure `Percentage of Members with 3 Sessions or More` to a regular **card** visual.

![](99.System/Attachments/1!cHf9MT7FTa_wYbSxkeHKwA.png.webp)

Adding the Percentage of Members with 3 Session of More to a Card Visual in Power BI

I then created the following DAX measure, **Top Members**, to dynamically display the **top 5 members of the week** who attended **at least 3 sessions**. The visual also includes a **count of additional members** who met the same attendance criteria but didn’t make the top 5.

To make the design more engaging, I added **small circular badges** at the bottom-right corner of each profile picture, displaying the **number of sessions attended**. And then I went a bit extra 🙈 and also added **crowns 👑** to highlight the **members who attended the most sessions** during the week!

```c
Top Members = 

-- 1. Filter Qualified Members with 3+ Visits
VAR QualifiedMembers =
    FILTER(
        SUMMARIZE(
            'Members',
            'Members'[Member],
            "VisitCount", [Sessions]
        ),
        [Sessions] >= 3 -- Only include members with 3+ visits
    )

-- 2. Count Total Qualified Members
VAR QualifiedCount = COUNTROWS(QualifiedMembers)

-- 3. Get Top 5 Members with Tie Breaking
VAR Top5Members =
    TOPN(
        5, -- Limit to top 5 members
        QualifiedMembers,
        [VisitCount], DESC, -- Primary sort by VisitCount
        'Members'[Member], ASC -- Secondary sort by Member Name for tie-breaking
    )

-- 4. Count Remaining Members Beyond Top 5
VAR AdditionalCount = QualifiedCount - COUNTROWS(Top5Members)

-- 5. Generate HTML for Top 5 Members with Overlap Effect and Tilted Crown for Rank 1
VAR Top5Html =
    CONCATENATEX(
        TOPN(5, Top5Members, [VisitCount], DESC), -- Reverse Order Before Concatenation
        VAR _ImageURL = LOOKUPVALUE('Members'[Image], 'Members'[Member], [Member])
        VAR _VisitCount = [Sessions]
        VAR _Rank = RANKX(
            Top5Members, [VisitCount], , DESC, DENSE
        ) -- Calculate Rank within Top 5

        -- Tilted Crown for Rank 1
        VAR _Crown = IF(
            _Rank = 1, -- Only for Rank 1
            "<div style='position:absolute; top:-25px; left:-5px; font-size:28px; transform:rotate(-25deg);'>👑</div>",
            "" -- No crown for others
        )
        RETURN 
        "<div style='width:65px; height:65px; border-radius:50%; overflow:visible; border:2px solid white; box-shadow:0 0 5px rgba(0,0,0,0.15); margin-left:-8px; position:relative;'>

            " & _Crown & " <!-- Crown for Rank 1 -->
            <!-- Profile Image -->
            <img src='" & _ImageURL & "' style='width:100%; height:100%; object-fit:cover; border-radius:50%;' />
            
            <!-- Visit Count Badge -->
            <div style='position:absolute; bottom:-8px; right:-8px; width:24px; height:24px; border-radius:50%; border:1px solid #CBD5E1; background-color:white; color:#000000; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:10px;'>
                " & FORMAT(_VisitCount, "0") & "
            </div>
        </div>",
        "",
        [VisitCount], DESC -- Ensure Sorting
    )

-- 6. Add Grey Circle for Extra Members (Always Last, No Overlap)
VAR AdditionalCircle = 
    IF(
        AdditionalCount > 0, -- Only show grey circle if there are extras
        "<div style='width:65px; height:65px; border-radius:50%; background-color:#09B96D; color:white; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:16px; margin-left:-8px;'>

            +" & FORMAT(AdditionalCount, "0") & "
        </div>",
        ""
    )

-- 7. Final HTML Output (Fixed Order, Right-Aligned, Overlapping Profiles, No Scroll)
VAR FinalOutput = 
    "<div style='display:flex; align-items:center; justify-content:flex-end; overflow:hidden; max-width:400px; padding-top:20px;'>

        " & Top5Html & AdditionalCircle & "
    </div>"

RETURN FinalOutput
```

I then added the HTML Content visual to Power BI…

![](99.System/Attachments/1!08Lyh1EjMH1F9c7AWsWWIw.png.webp)

Adding the HTML Content Visual to Power BI

… and dropped the `Top members` measure in the field section.

![](99.System/Attachments/1!qQlEIvVu6M4I0BQgy2gmVA.png.webp)

Adding the Top Members Measure to the HTML Content Visual in Power BI

### Step 3: Creating the Tooltip with the Additionnal Members

![](99.System/Attachments/1!EpgljwrW1lnKn7rB2usRDQ.png.webp)

Creating the Tooltip with the Additionnal Members in Power BI

To display the **additional members** who attended **3 or more sessions** but didn’t make the **top 5**, I created the following **DAX measure** using **HTML code**.

```c
Extra Members Tooltip = 

-- 1. Filter Qualified Members with 3+ Visits
VAR QualifiedMembers =
    FILTER(
        SUMMARIZE(
            'Members',
            'Members'[Member],
            "VisitCount", [Sessions]
        ),
        [Sessions] >= 3 -- Only include members with 3+ visits
    )

-- 2. Get Top 5 Members
VAR Top5Members =
    TOPN(
        5,
        QualifiedMembers,
        [VisitCount], DESC,
        'Members'[Member], ASC
    )

-- 3. Identify Extra Members (Beyond Top 5) and Sort by Visits Descending
VAR ExtraMembers =
    TOPN(
        COUNTROWS(QualifiedMembers) - 5, -- Only extra members
        EXCEPT(QualifiedMembers, Top5Members),
        [VisitCount], DESC,
        'Members'[Member], ASC -- Tie-breaker by name
    )

-- 4. Generate HTML for Extra Members List
VAR ExtraHtml =
    CONCATENATEX(
        ExtraMembers,
        VAR _ImageURL = LOOKUPVALUE('Members'[Image], 'Members'[Member], [Member])
        VAR _Name = LOOKUPVALUE('Members'[Member], 'Members'[Member], [Member])
        VAR _VisitCount = [Sessions]
        RETURN 
        "<div style='display:flex; align-items:center; margin-bottom:6px;'>
            <!-- Profile Image -->
            <div style='width:30px; height:30px; border-radius:50%; overflow:hidden; border:2px solid #CBD5E1; box-shadow:0 0 5px rgba(0,0,0,0.15); margin-right:8px;'>
                <img src='" & _ImageURL & "' style='width:100%; height:100%; object-fit:cover;' />
            </div>
            <!-- Member Info -->
            <div style='font-size:12px; font-weight:bold;'>
                " & _Name & " <span style='color:grey; font-size:10px;'>(" & FORMAT(_VisitCount, "0") & ")</span>
            </div>
        </div>",
        ""
    )

-- 5. Final HTML Output
VAR FinalOutput =
    "<div style='font-family:Arial; padding:8px;'>
        " & ExtraHtml & "
    </div>"

RETURN FinalOutput
```

After creating the measure, I added it to a **new report page** and configured it as a **tooltip**. Here’s how I did it:

- Created a **new page** and set the **page size** under **Canvas Settings** to **Tooltip size** for a compact layout.
- Added an **HTML Content visual** to the page.
- Dropped the **Extra Members Tooltip** measure into the visual to dynamically display the data.
![](99.System/Attachments/1!uJfxZB60EVuuE2pXQA26bA.png.webp)

Changing the Canvas Size in Power BI

Going back to the to page with the KPI Card, I added a transparent card as a tooltip trigger by:

- Creating a **card visual** and adding the `Extra Members Tooltip` measure.
- Changed the **font color** of the callout value to a **transparent color** using the following measure:
```c
Transparent Color = "#00000000"
```
![](99.System/Attachments/1!IhNt4b2D2CGy1gYsKPdxOw.png.webp)

Adding the Transparent Card in Power BI

And finally I set the tooltip of this transparent card to use the **tooltip report page** created earlier. 🥳

![](99.System/Attachments/1!jo8-2gOpn5nilz3EYCy4Aw.png.webp)

Setting the Transparent Card’s Tooltip in Power BI

### Wrapping Up

While I **love** Power BI’s **core visuals**, I found that integrating **HTML elements** added an **extra layer of creativity** and **design flexibility** to this project.

This project also reminded me how much I **learn** when working in **new contexts** and **different-sized projects**.

I hope this article gives you some **ideas and inspiration** for your own projects — and maybe even encourages you to **experiment** with **HTML visuals** in Power BI!

Let me know if you try it out — I’d **love to hear about it!** 😊

**You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/drive/folders/16XEq8hJ6g2QLFZDB--vBi-PtqFwNTtgs?usp=sharing)**.**

If you interested in learning more about using HTML/CSS in Power BI, you can read more on it [**here**](https://medium.com/microsoft-power-bi/elevating-power-bi-reports-with-html-css-joining-forces-f90fbd654e8b):

## [Elevating Power BI Reports with HTML & CSS: Joining Forces 💪](https://medium.com/microsoft-power-bi/elevating-power-bi-reports-with-html-css-joining-forces-f90fbd654e8b?source=post_page-----deb7513ff3be---------------------------------------)

### In It to Win It 🤠: Part 2 of Participating in the FP20 Analytics Challenge on Data-Driven Education Management

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