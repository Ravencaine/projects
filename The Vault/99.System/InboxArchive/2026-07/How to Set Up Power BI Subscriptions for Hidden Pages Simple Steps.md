---
title: "How to Set Up Power BI Subscriptions for Hidden Pages: Simple Steps"
source: "https://medium.com/microsoft-power-bi/how-to-set-up-power-bi-subscriptions-for-hidden-pages-simple-steps-8990a13da9b4"
author:
  - "[[Janvi Gupta]]"
published: 2026-03-19
created: 2026-07-27
description: "More"
Processed: "Unprocessed"
---
Power BI does not allow subscriptions for hidden pages by default — but there is a simple workaround. Follow these 4 steps to schedule email reports for hidden pages without permanently exposing them.

## Prerequisites

- Power BI Desktop installed,
- A Power BI Pro or Premium license, and
- Report with at least one hidden Page.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Step 1: Unhide the Page in Power BI Desktop

![](99.System/Attachments/1!8jyddZXewmZ165pBsAKEBw.png.webp)

Open your.pbix file in Power BI Desktop. Right-click on the hidden page tab at the bottom and select Show page. The page will now be visible — this is required so Power BI Service can recognize it for subscriptions.

## Step 2: Publish the Report to Power BI Service

![](99.System/Attachments/1!5PfhHOiaGEw82wFLwmCiPw.png.webp)

![](99.System/Attachments/1!Fc7MlLIn6yPwFsQzIyxaUA.png.webp)

![](99.System/Attachments/1!6jlzTuHrKVr-nK56mmyvRg.png.webp)

In Power BI Desktop, go to the Home tab and click Publish. Select your workspace and wait for the success confirmation. Your report — with the now-visible page — is live in Power BI Service.

## Step 3: Create the Subscription in Power BI Service

![](99.System/Attachments/1!Se2Nqw-9dwfGsi5AWV0AYA.png.webp)

Open the report in Power BI Service (app.powerbi.com). Click the three-dot menu and select Subscribe to report. Click Add new subscription, choose the previously hidden page from the Page dropdown, set your recipients, schedule, and frequency — then click Save.

![](99.System/Attachments/1!rnOctv-xBTDB3AdrUuh1zg.png.webp)

## Step 4: Re-hide the Page and Save the Report

Go back to Power BI Desktop, right-click the page tab, and select Hide page. Publish the report again to Power BI Service.

The page is now hidden from regular viewers — but your subscription is already saved and will continue to send on schedule without any changes needed.

![](99.System/Attachments/1!c03l4pvL8k16D8SmWY7wTQ.png.webp)

Just Hide the Page and Re-Publish it!

![](99.System/Attachments/1!O6FkCa9wk6U_KX1C2XrLKw.png.webp)

Got the Subscription Mail

## Why Does This Work?

Power BI subscriptions are saved with a reference to the page’s internal ID — not its visibility state. Page visibility is a display-layer setting that only affects what report viewers see in the browser.

The subscription engine bypasses this layer entirely, so re-hiding the page after saving the subscription has zero effect. The emails will keep coming on time, every time.

This simple 4-step workaround lets you deliver Power BI subscriptions for hidden pages on schedule — without permanently exposing them to all report viewers. It is perfect for executive dashboards, confidential KPIs, or any page you want to share selectively via email.

If you have any questions, please share them in the comments below, or **connect with me on LinkedIn —** [**Janvi Gupta**](https://www.linkedin.com/in/janvisgupta/) **😊**

**You can also schedule a call on Topmate: J** [**anvi Gupta**](https://topmate.io/janvigupta)

![](99.System/Attachments/0!pFA8x1hMdpQf2Er2.gif)

Dream big, but start small..!

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----8990a13da9b4---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Tips & Tricks

**Tags:** Tips & Tricks