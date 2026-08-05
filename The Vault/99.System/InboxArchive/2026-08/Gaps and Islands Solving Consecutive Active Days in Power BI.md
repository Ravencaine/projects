---
title: "Gaps and Islands: Solving Consecutive Active Days in Power BI"
source: "https://medium.com/microsoft-power-bi/gaps-and-islands-solving-consecutive-active-days-in-power-bi-f409b3679559"
author:
  - "[[Md Mizanur Rahman Nayan]]"
published: 2025-10-06
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
Finding consecutive active days might sound simple, but when duplicates and missing dates appear, it becomes a true data puzzle. For quite some time, I am working with data in Power BI and SQL. Working with data sometimes feels like battlefield, where you need to come up with different strategies to get success. You can not expect to handle similar problems with same strategy that work earlier. Each battle of analytics has its own kind of complexity.

Recently I came across one challenge which seems deceptively simple. The challenge was posted by Maven Analytics in their [Monthly Data Drill](https://mavenanalytics.io/data-drills/streak-leaderboard?utm_source=linkedin&utm_campaign=datadrill_streakleaderboard_li_maven). The task was simple:

C **reate a leaderboard of the top 10 users, based on the longest daily active streaks.**

![This image shows a table of lesson activity for one user, Bobby Fairways. It lists lesson IDs and dates, highlighting two streaks of consecutive learning: a 3-day streak from September 10–12 and a 4-day active streak from September 25–28. A gap between these dates marks a break in the streak. The annotations help visualize user engagement and identify patterns in consistent learning behavior.](99.System/Attachments/This_image_shows_a_table_of_lesson_activity_for_one_user,_Bobby_Fairways._It_lists_lesson_IDs_and_da.webp)

This image shows a table of lesson activity for one user, Bobby Fairways. It lists lesson IDs and dates, highlighting two streaks of consecutive learning: a 3-day streak from September 10–12 and a 4-day active streak from September 25–28. A gap between these dates marks a break in the streak. The annotations help visualize user engagement and identify patterns in consistent learning behavior.

When you simply think of the task alone, it seems quite straightforward. There are many tutorials in YouTube and others blog posts which tackled similar problems. But when you looked at the data, then comes the main twist of the problem. Because the data was full of duplicates value of users and dates. Let us understand the problem so that we understand what we need to work with.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

### The Problem

To understand the problem better, we need to take a look at the dataset. The dataset contains data of a popular language learning company and have a table containing ~900,000 lesson completions, including the date, user, and lesson ID. Here is a snapshot of the dataset.

![](99.System/Attachments/1!fRCGo-fotgJMWJYrSWDv_Q.png.webp)

Each row represents a lesson completed by a user. Here’s the twist:

- Users could complete **multiple lessons per day**, meaning the same user-date pair appeared multiple times.
- Users didn’t necessarily complete lessons **every day**, so there were **gaps** in activity.

My objectives is to **Find the longest streak of consecutive active days per user.** The problem was not as straightforward as it sounds. But the solutions turned out to be an elegant solution of **Gaps and Island Theory**.

### Defining Gaps and Island Theory

Now lets understand what does we mean by Gaps and Island Theory.

> A data island refers to any ordered sequence in which each row is closely related to its neighboring rows. In certain types of data and analytical contexts, this “close proximity” often implies that the rows are consecutive. There is mainly two terms. “Island” and “Gap”

1. **Island:** These are consecutive sequences of data points that exist within a dataset. For example, a series of days where a user was logged in, or a range of consecutive order IDs.
2. **Gaps:** These are the periods or sequences where data is missing between islands. For instance, the days a user was offline, or the deleted order IDs from a sequential series.

For better understanding lets look at our data and take an example:

**For user 8226413, Aeris Stone, has the following activity:**

1. Active on May 1
2. Inactive from May 2–4
3. Active again from May 5–7
4. Inactive from May 8–20
5. Active again from May 21–23

This creates **three islands:**

1. May 1 → 1-day streak
2. May 5–7 → 3-day streak
3. May 21–23 → 3-day streak

And **two gaps**:

1. May 2–4

2\. May 8–20

**As we have understood the problem and the theory, lets find out the solution in DAX.**

### The Solution

Since we have unpacked the problem and theory to solve the problem, here’s the big question- **how are we going to make the islands of data?**

Here’s the trick.

- At first we need to get a unique set of data with dates and user id, removing the lesson id. This will provide the data of each day with each unique id.
- After we get the virtual table, we need to rank the consecutive sequence of the data. Then we would subtract the rank with the date which would provide us same date. For example,
![](99.System/Attachments/1!YU4QIW7h6oHE--ZK8kg32A.png.webp)

- In this step, subtract the rank with the date to get date — Rank pair. This is the Island of our data.
- Now we need to add two columns: one for the rank and one for the Island ID.
- After that, we will group by user and island ID to count how many days are in each streak.
- And finally, we will return the maximum streak length for each user.

### Step 1:

In this step we will summarize the lesson date and user id to get distinct user-date pairs. This removes duplicate lessons on the same day.

```c
SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date])
```

### Step 2:

In this step, we will add the ranking of the each distinct consecutive pairs. This would gives us the sequential number of active days. For example, if a user was active on May 1, May 5 and May 6, those dates would get ranks 1,2,3 respectively. For this we would add a column rank in our previous summarized table.

```c
"Rank", RANKX(
            FILTER(
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
            ),
            LessonStreaks[date],
            ,
            ASC
        )
```

### Step 3:

Now we got the ranking value, subtract the number from the date, to get a unique value for each streak. All dates in a streak will have the same result**.** In other words, all consecutive days for a user will end up with the same Island value, meaning they belong to the same streak group.

```c
"Island", LessonStreaks[date] - RANKX(
            FILTER(
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
            ),
            LessonStreaks[date],
            ,
            ASC
        )
```

### Step 4:

In this step we will add the two column we have created in step 2 and 3 with the table created in Step 1. The result of all 4 step, we would store the value in a variable.

```c
VAR _DistinctDates =
    ADDCOLUMNS(
        SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
        "Rank", RANKX(
            FILTER(
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
            ),
            LessonStreaks[date],
            ,
            ASC
        ),
        "Island", LessonStreaks[date] - RANKX(
            FILTER(
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
            ),
            LessonStreaks[date],
            ,
            ASC
        )
    )
```
![This image shows a table tracking a user’s daily activity over time. Each row includes a user ID, date, rank, and a calculated “island” value. The island column reflects the start of a streak by subtracting the rank from the date, helping identify clusters of consecutive activity. Gaps between dates signal breaks in engagement, making it easier to spot streaks and isolate patterns.](99.System/Attachments/This_image_shows_a_table_tracking_a_user’s_daily_activity_over_time._Each_row_includes_a_user_ID,_da.webp)

This image shows a table tracking a user’s daily activity over time. Each row includes a user ID, date, rank, and a calculated “island” value. The island column reflects the start of a streak by subtracting the rank from the date, helping identify clusters of consecutive activity. Gaps between dates signal breaks in engagement, making it easier to spot streaks and isolate patterns.

### Step 5:

So now, we have a table that shows each user, their active dates, and their Island group. Next, let’s summarize it to calculate the length of each streak.

```c
VAR Streaks =
    ADDCOLUMNS(
        SUMMARIZE(_DistinctDates, LessonStreaks[user_id], [Island]),
        "StreakLength", COUNTROWS(
            FILTER(_DistinctDates, 
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id]) &&
                [Island] = EARLIER([Island])
            )
        )
    )
```
![This image shows a table tracking user activity streaks. Each row includes a user ID, a date, and a streak length, indicating how many consecutive days the user was active. The data reveals patterns of engagement, with some users showing longer streaks and others appearing sporadically. This helps identify consistent behavior and gaps in participation over time.](99.System/Attachments/This_image_shows_a_table_tracking_user_activity_streaks._Each_row_includes_a_user_ID,_a_date,_and_a_.webp)

This image shows a table tracking user activity streaks. Each row includes a user ID, a date, and a streak length, indicating how many consecutive days the user was active. The data reveals patterns of engagement, with some users showing longer streaks and others appearing sporadically. This helps identify consistent behavior and gaps in participation over time.

Here for each user and island combination, we’re counting how many rows or how many days belong to that particular island. That gives us the length of each streak.

### Step 6:

In this last step, all we are left to get the max value of the StreakLength from the virtual strakes table.

```c
VAR _result= MAXX(_Streaks, [StreakLength])
```

So here is the full DAX solution.

```c
MaxConsecutiveDays = 
VAR _DistinctDates =
    ADDCOLUMNS(
        SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
        "Rank", RANKX(
            FILTER(
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
            ),
            LessonStreaks[date],
            ,
            ASC
        ),
        "Island", LessonStreaks[date] - RANKX(
            FILTER(
                SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])
            ),
            LessonStreaks[date],
            ,
            ASC
        )
    )

VAR _Streaks =
    ADDCOLUMNS(
        SUMMARIZE(_DistinctDates, LessonStreaks[user_id], [Island]),
        "StreakLength", COUNTROWS(
            FILTER(_DistinctDates, 
                LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id]) &&
                [Island] = EARLIER([Island])
            )
        )
    )

VAR _result= MAXX(_Streaks, [StreakLength])
RETURN
_result
```

### Conclusion

This challenge reminded me that data problems often hide their complexity beneath a simple surface. The **Gaps and Islands** pattern is one of those elegant tools that unlocks clarity from chaos. Understanding the theory behind your solution is what makes you a true data practitioner.

However if you need the solution in SQL as well, let me know in the comment.

[Md Mizanur Rahman Nayan](https://www.linkedin.com/in/mizan2390)  
\- PL-300 Certified

👏🏻 Clap 🔎 [Follow](https://medium.com/@mdrahmanmizan) 📩 [Subscribe](https://medium.com/@mdrahmanmizan/subscribe) ✍🏻Comment

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----f409b3679559---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX