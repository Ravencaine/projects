---
title: "Building a Cinematic Welcome Screen in Power BI with HTML + DAX"
source: "https://medium.com/microsoft-power-bi/building-a-cinematic-welcome-screen-in-power-bi-with-html-dax-7a0cdd7c78da"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2026-04-02
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
## Turning dashboards into experiences — not just reports

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*x44BAH_LFd5Ccvkx9nA-wQ.png)

Welcome Page

What if your Power BI report didn’t just *start* …  
but *introduced itself*?

A few weeks ago, I came across the work of Gus Bavia — and honestly, it changed how I think about dashboards.

His reports don’t feel like dashboards.  
They feel like **products**.

They open with cinematic intros.  
They guide the user.  
They create anticipation before showing data.

And that made me ask a simple question:

👉 *Why should storytelling begin only after the first visual loads?*

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## The Idea: A Welcome Page That Feels Alive

Instead of landing directly on charts, I wanted:

- A **video background**
- A **title reveal animation**
- A **narrative introduction**
- A **guided entry into the report**

Something that feels like:

> *🎬* “You’re about to explore something important.”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ALUtLIDZb0fs3K19WnWiSg.gif)

See the Intro Page in action

## What We’re Building

A fully animated welcome page inside Power BI:

- 🎥 Video background (hosted externally)
- 🌑 Dark cinematic overlay
- 🟡 Romania-themed branding
- 🧭 Navigation buttons (Page 1, 2, 3)
- ✨ Smooth fade + motion animations

All built using:

```c
DAX + HTML + CSS
```

No custom visuals. No JavaScript.

## Why This Technique Matters

## 1\. Power BI ≠ Just Charts anymore

We’re not limited to visuals. We can build **interfaces**.

## 2\. HTML Content visual = Full control

You control:

- Layout
- Animation
- Typography
- Interaction design

## 3\. Storytelling starts before data

This is the biggest shift.

Instead of:

```c
User → Dashboard → Data
```

We create:

```c
User → Experience → Story → Data
```

## The Inspiration (Real Talk)

Gus Bavia’s work made me uncomfortable — in a good way.

Because it exposed something:

> ***My dashboards were informative… but not memorable.***

His designs felt like:

- Apple product launches
- Netflix intros
- Premium UX

So instead of copying — I tried to understand:

👉 *How is this even possible inside Power BI?*

## Step 1: Understanding the Trick

The core idea is simple:

👉 Power BI can render HTML via the **HTML Content visual**

So if DAX returns HTML…

Power BI renders it like a mini web app.

That means we can use:

- `<video>` for background
- CSS animations (`@keyframes`)
- Flexbox layouts
- Absolute positioning

This is where things get interesting.

## Step 2: The Video Problem

This is where most people get stuck.

Power BI **cannot host videos internally**.

So we need:

```c
External hosting + public URL
```

## Step 3: My Investigation (Supabase Setup)

I tested multiple options:

- Google Drive ❌ (blocked embeds)
- GitHub ❌ (not reliable for video streaming)
- OneDrive ❌ (permissions issues)

Finally landed on:

👉 Supabase

## Why Supabase Works

- Free storage
- Public file URLs
- Fast CDN delivery
- No authentication needed

## How I Uploaded the Video

Follow this exact flow:

## 1\. Go to Supabase

Create a project

## 2\. Open Storage

Create a bucket:

```c
public-assets
```

## 3\. Upload video

Example:

```c
mp4
```

## 4\. Make it public

Toggle:

```c
Public bucket = ON
```

## 5\. Copy URL

You’ll get something like:

```c
https://xxxx.supabase.co/storage/v1/object/public/public-assets/video.mp4
```

That’s what we use inside HTML.

## Step 4: Embedding Video in DAX

This is the core piece:

```c
<video autoplay muted loop playsinline
style='width:100%;height:100%;object-fit:cover;'>
</video>
```

Key things:

- `autoplay` → starts instantly
- `muted` → required for autoplay
- `loop` → seamless experience
- `object-fit:cover` → fills screen

## Step 5: The Animation Layer

This is what makes it feel premium.

Example:

```c
@keyframes titleFade {
from { opacity:0; transform:translate(-50%,-45%) }
to   { opacity:1; transform:translate(-50%,-50%) }
}
```

Then applied like:

```c
animation: titleFade 1.5s ease forwards;
animation-delay: 4.8s;
```

👉 This creates **timed storytelling**

## Step 6: The Structure

Your entire intro is layered like this:

```c
Video (z-index 1)
↓
Overlay (z-index 2)
↓
Text (z-index 3)
↓
Navigation (z-index 4)
↓
Branding (z-index 5)
```

That’s why it feels like a real UI.

## Step 7: Navigation Trick (Important)

HTML buttons **cannot change Power BI pages**.

So here’s the workaround:

👉 Place transparent Power BI buttons on top

Map them like:

```c
🛣️ → Page 1  
🗺️ → Page 2  
🌍 → Page 3
```

Users think they’re clicking HTML —  
But actually clicking Power BI buttons.

## The Final Result

What you get:

- 🎬 Cinematic intro
- 🧭 Guided navigation
- 🧠 Strong first impression
- 📊 Better engagement

And most importantly:

> ***Your report feels like a product — not a file.***

[https://www.awesomescreenshot.com/video/50843449?key=8451121c16b1de668826ac8a4db2b8d2](https://www.awesomescreenshot.com/video/50843449?key=8451121c16b1de668826ac8a4db2b8d2)

## Common Issues (Quick Fixes)

## Video not playing

→ Ensure:

```c
muted + autoplay both present
```

## Black screen

→ Check:

```c
Supabase bucket is public
```

## Animation not triggering

→ Verify:

```c
animation-delay values
```

## Layout broken

→ Fix canvas size:

```c
1280 × 720
```

## Final Thoughts

This completely changed how I approach Power BI.

Because now I think:

- Not just *what data to show*
- But *how to introduce it*

Static dashboards are fine.

But experiences?

They’re remembered.

## Your Turn

Try this yourself:

1. Upload a video (Supabase)
2. Create an HTML measure
3. Add animation
4. Build a welcome screen

Start simple.

Then improve.

## Want It All Ready-Made?

If you’d rather not spend time adapting the code, **DM me on** [**LinkedIn**](https://www.linkedin.com/in/bandyopadhyay-ankan/), and I’ll send you:

- The complete HTML code
- The PBIX file with everything configured

I’m happy to share — but I promise you’ll learn more by building at least one yourself first.

If you build one, I genuinely want to see it.

And if you want, next, I can help you build:

👉 A **map animation intro (highway drawing effect)**  
👉 A **Netflix-style page transition inside Power BI**

Follow me for more Power BI techniques that push beyond visuals.

#PowerBI #DAX #DataStorytelling #HTML #UX #DataVisualization

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----7a0cdd7c78da---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization