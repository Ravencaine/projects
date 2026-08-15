---
title: "Power BI and Power Automate — Send email at the end of the month"
source: "https://medium.com/@kibpat/power-bi-and-power-automate-send-email-at-the-end-of-the-month-7ee5a5eaa618"
author:
  - "[[Pataree Ngamwongwan]]"
published: 2024-11-22
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
If you have a published report and you want to send the email at the end of the month.

To do that go to power automate [https://make.powerautomate.com/](https://make.powerautomate.com/)

Then please read this article [https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-bookmarks?tabs=powerbi-desktop](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-bookmarks?tabs=powerbi-desktop) on how to create this scheduled cloud flow

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*g1pTvfIOFcRI-A2U0uObWw.png)

Now the part that I want to show is how to send at the end of the month

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*0DdEx0QCTKKFWDRSwtiVqA.png)

## Recurrence

Set this to run on a daily basis at the time of your choice

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*XI3HdOIHwyomMbih7YV43A.png)

## Today — Start of Month

Add an action after Recurrence

Select Compose

![](https://miro.medium.com/v2/resize:fit:1218/format:webp/1*jGYaz_Hhxb2spY_nEpPU8g.png)

Select Function

Use Search bar to look for startOfMonth, then utcNow

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_xp5hdtUUpdOFAu3f6cgPQ.png)

The Formula for the Compose — which is renamed to \[Today Start of the Month\] is

```c
startOfMonth(utcNow())
```

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ED7t2SJmH0e7tlnxuR2yig.png)

## Tomorrow Start of Month

Add an action after \[Today Start of Month\] compose action

Similar action the the previous step Select Compose

Select Function

Use Search bar to look for startOfMonth, addDays, then utcNow

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EDyT4vct8rM7pOoHyvIFdQ.png)

The Formula for the Compose — which is renamed to \[Tomorrow Start of the Month\] is

```c
startOfMonth(addDays(utcNow(), 1))
```

## Add Action — Condition

Condition — End of Month if Today Start of Month and Tomorrow Start of the Month is not the same

![](https://miro.medium.com/v2/resize:fit:1142/format:webp/1*Ss5MMlt_Wue47gZ6AQJQnA.png)

By selecting the output of Today Start of Month and out of Tomorrow Start of Month in the previous steps.

## TRUE EOM example:

- **Today Start of the Month for 30th Nov:** 1st November
- **Tomorrow Start of Month for 1st Dec:** 1st December (by adding one day to today’s date)
- **Conclusion:** 1st November!= 1st December

## FALSE EOM example:

- **Today Start of the Month for 15th Nov:** 1st November
- **Tomorrow Start of Month for 16th Nov:** 1st November ((by adding one day to today’s date)
- **Conclusion:** 1st November (15 Nov) == 1st November (16th Nov)
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*As85wlEB6wVP3wnf6CtdOw.png)

Based on the requirement, add additional actions to either \[TRUE\] or \[FALSE\] as required.

## Tip: Export to File for Power Reports

Under Advanced parameters

If only required a certain page to be sent out as attachment

Page name is not the Page or Sheet Name but the a part of the URL.

Example URL:  
[https://app.powerbi.com/groups/\<some long string>/\<another some long string before question mark>?experience=power-bi](https://app.powerbi.com/groups/d877dd9d-c92e-4d5b-9bd1-31c24b3263d3/reports/ba5d34df-3a46-4fe7-8ff3-cc0e388b919d/f38d622d699346beb9b3?experience=power-bi)

The page name is the [\<another some long string before question mark>](https://app.powerbi.com/groups/d877dd9d-c92e-4d5b-9bd1-31c24b3263d3/reports/ba5d34df-3a46-4fe7-8ff3-cc0e388b919d/f38d622d699346beb9b3?experience=power-bi)

![](https://miro.medium.com/v2/resize:fit:1214/format:webp/1*AchSd_RNCqaLD1ymmlJdzw.png)

Parameter for Include Hidden pages may need to be selected as No

![](https://miro.medium.com/v2/resize:fit:1214/format:webp/1*lrL3OBgsEd09whjxoiNwWw.png)

## Reference:

[https://make.powerautomate.com/](https://make.powerautomate.com/)

[https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-bookmarks?tabs=powerbi-desktop](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-bookmarks?tabs=powerbi-desktop)

[https://youtu.be/sNZXxJ-QrIE?si=jpIwp1krnqE4k\_Hn](https://youtu.be/sNZXxJ-QrIE?si=jpIwp1krnqE4k_Hn)