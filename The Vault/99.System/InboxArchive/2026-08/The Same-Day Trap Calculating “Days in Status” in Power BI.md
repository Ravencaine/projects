---
title: "The Same-Day Trap: Calculating “Days in Status” in Power BI"
source: "https://medium.com/microsoft-power-bi/the-same-day-trap-calculating-days-in-status-in-power-bi-4fe5a903111d"
author:
  - "[[Md Mizanur Rahman Nayan]]"
published: 2026-03-18
created: 2026-08-02
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!iqyfUtcNVR3Zbmr1ZvFnQA.png.webp)

While building any reports for Sales, Customer Service or Supply chain, the higher ups would eventually ask you this question:

> **“How long do our items stay in each stage?”**

While reporting for sales in the pipeline, an unresolved customer service complaint or a delivery in transit, monitoring the duration between status change of these each KPIs is crucial for the managers.

While browsing through the [Microsoft Fabric Community](https://community.fabric.microsoft.com/t5/DAX-Commands-and-Tips/Calculate-days-spent-in-the-same-status-date-in-same-column/m-p/5133526#M187395) discussion boards, I came across an interesting problem regarding this. An user was facing problems to find out the days interval between seven different status or checkpoints. It seems simple and easy at a glance with DAX. You need to find out the date of current status, get the date of the next status and use DATEDIFF using these two dates. Hurrah!!! you get the answer. or NO???

However, while its basically the main logic, but there’s more to consider. With out that you may fall in “The Same Day Trap”.

Lets dissect the problem. When an status created, updated, and closed all on the same date, standard DAX date would struggle to identify the order of status, then calculate the date difference. In this article I am going to explain how we solved the same-day status change problem using DAX.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## The Scenario

Let’s have a close look on what we are working on here. We have a standard opportunity\_status table. We have an ID, a Start Date, and a Status. If you look closely in the table, you will see that the statuses are easily numbered (e.g., “1. Preparation”, “2. Discussion”) which is going to be our saving grace.

![Data Table.](99.System/Attachments/Data_Table.webp)

Data Table.

Pay close attention at **March 16th, 2024**. Opportunity #24 was in “2. Discussion with Prospect” and updated to “7. Did not proceed” on that exact same day.

If we use a standard DAX formula to find the next date (`MIN(start_date) > CurrentDate`), it completely ignores the same-day change because the dates are identical. It evaluates both rows as happening at the exact same time, returning incorrect durations.

## The Solution: Using Status Numbers as a Tie-Breaker

Since we lack a precise timestamp to tell DAX the chronological order, we can use the numbers in the status names as our secondary sort order, our tie-breaker. Here is how to build this in two steps.

### Step 1: Extract the Step Number

First, we need Power BI to recognise the step numbers as actual integers so it can evaluate which step is logically “greater” than the other.

Create a calculated column to extract the number before the period:

```c
Step_Number = 
// Extracts the number before the period (.). 
// If there is no period or the status is blank, it assigns a 0.
IFERROR(
    VALUE(LEFT('opportunity_status'[status], 
    FIND(".", 'opportunity_status'[status]) - 1)),
    0
)
```
![](99.System/Attachments/1!SYOQ9YWCtSYLIzQIpB2cKw.png.webp)

### Step 2: The “Days in Status” Calculated Column

Now we build our duration logic. We want to find the date of the *next* status.

To do this, we filter the table for the same Opportunity ID where the date is in the future **OR** if the date is the exact same date, but the `Step_Number` is higher.

Create a new Calculated Column with this DAX:

```c
days_in_status = 
VAR _currentID = sheet1[opportunity_id]
VAR _currentDate = sheet1[start_date]
VAR _currentStep = sheet1[Step_Number]

// 1. Create a virtual table of all FUTURE statuses for this specific Opportunity ID
VAR _futureSteps = 
    FILTER(
        sheet1,
        sheet1[opportunity_id] = _currentID &&
        (
            // The date is strictly in the future
            sheet1[start_date] > _currentDate || 
            
            // OR the date is the exact same, but the step number is higher
            (sheet1[start_date] = _currentDate && sheet1[Step_Number] > _currentStep)
        )
    )

// 2. Find the earliest date from that future list
VAR _nextDate = MINX(_futureSteps, sheet1[start_date])

RETURN
// 3. Calculate the difference
    IF(
        ISBLANK(_nextDate),
        DATEDIFF(_currentDate, TODAY(), DAY),
        DATEDIFF(_currentDate, _nextDate, DAY)
    )
```
![](99.System/Attachments/1!BU_CCGdRZx_L2kiqetMZZw.png.webp)

## How The Logic Works

Let’s go back to our same-day problem on **March 16th, 2024**:

- When DAX evaluates **“2. Discussion”**, it looks at the future steps. It sees “7. Did not proceed” happens on the exact same date, but **7 > 2**. It grabs that exact same date as the “Next Date”, resulting in a perfect **0 days** spent in Step 2.
- When DAX evaluates **“7. Did not proceed”**, it checks for future steps. Since 7 is the highest step for that day, it ignores the tie and looks for the next chronological date in the dataset (July 14th), correctly resulting in **120 days**.

*(Note: Because we use* `*TODAY()*` *for the latest open status, your "days in status" for currently active opportunities will dynamically increase every time you refresh your dataset, perfect for live reporting).*

## Bonus: Flagging “Overdue” Opportunities

Once you have your `Days_in_Status` working, the natural next question from stakeholders is:

> **"Can you highlight the opportunities that have been stuck in the same stage for too long?"**

We can easily flag opportunities that are currently active, are the absolute latest status for that ID, and have been sitting there for too long.

```c
Overdue_in_Status = 
VAR _currentID = sheet1[opportunity_id]
VAR _currentDate = sheet1[start_date]
VAR _currentStep = sheet1[Step_Number]
VAR _days= 30

// 1. Check if this is the absolute latest status
VAR _futureSteps = 
    FILTER(
        sheet1,
        sheet1[opportunity_id] = _currentID &&
        (
            sheet1[start_date] > _currentDate || 
            (sheet1[start_date] = _currentDate && sheet1[Step_Number] > _currentStep)
        )
    )

VAR _nextDate = MINX(_futureSteps, sheet1[start_date])
VAR _isLatestStatus = ISBLANK(_nextDate)

// 2. Define which statuses are considered "Active"
VAR _activeStatuses = {
    "1. Preparation", 
    "2. Discussion with Prospect", 
    "3. Submitted", 
    "4. Accepted"
}

RETURN
// 3. Evaluate the conditions
IF(
    _isLatestStatus = TRUE() && 
    sheet1[status] IN _activeStatuses && 
    sheet1[days_in_status] > _days,
    TRUE(),
    FALSE()
)
```
![](99.System/Attachments/1!YmcMi64T8qhWlBeO9V-hzA.png.webp)

## The “Going Backwards” Warning

There is one edge case to consider with this DAX approach.

> **what if opportunities move backward (e.g., from 3. Submitted back to 2. Discussion)?**

If an opportunity moves backward on ***different days***, this DAX works perfectly. DAX just looks for the next chronological date. However, if an item moves backwards on the **exact same day**, this formula will assume standard forward progression because of our tie-breaker logic. If same-day backward jumps happen frequently in your business logic, you will ultimately need to add an Index Column in Power Query or request accurate DateTime stamps from your database to establish true chronological order.

## Final Thoughts

Handling duration in Power BI is rarely as simple as `**Date A - Date B**`. Understanding the granularity of your data and what happens when multiple events occur within that same grain is the key to building accurate and robust data models.

With the built-in business logic of your status naming conventions, you can solve complex sequencing issues entirely within DAX. The Microsoft Fabric Community is an incredible place to find these kinds of real-world puzzles, and I highly recommend browsing it the next time you are stuck.

*Have you encountered the Same-Day Trap before? Let me know how you solved it in the comments!*

Want to know more about such interesting topics? Follow me.  
Want to connect with me? Lets connect in [LinkedIn](https://www.linkedin.com/in/mizan2390/).

Md Mizanur Rahman Nayan

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----4fe5a903111d---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX