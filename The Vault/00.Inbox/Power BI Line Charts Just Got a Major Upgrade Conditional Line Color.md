---
title: "Power BI Line Charts Just Got a Major Upgrade [Conditional Line Color]"
source: "https://www.youtube.com/watch?v=9Qiyu0_SHoE&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=9Qiyu0_SHoE&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Drop Materialized View]]"
published: 2026-07-26
created: 2026-08-08
description: "In this video we talk about how to conditionally set the color of Line Chart and Legends in Power BI. This was released as part of the July 2026 Power BI Release. Video Chapters:00:00 Introduction"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=9Qiyu0_SHoE)

In this video we talk about how to conditionally set the color of Line Chart and Legends in Power BI. This was released as part of the July 2026 Power BI Release.  
  
Video Chapters:  
00:00 Introduction  
01:06 How to Conditionally set Line Color  
03:23 Introduction to Gradients in Line Charts  
06:02 My Dream Additional Feature  
  
July Release Blog: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-July-2026-Feature-Summary/ba-p/5303533  
  
File from video: https://github.com/edwardpcharles/Power-BI-Projects/blob/main/Line\_Chart\_Sample.pbix  
⸺⸺⸺  
🚀 WORK WITH ME  
Email: edward@enterprisedatastrategies.com  
  
📱 FOLLOW ME ELSEWHERE  
LinkedIn: https://www.linkedin.com/in/edward-charles-085025b1/  
YouTube: https://youtube.com/@DropMaterializedView  
  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
  
📚 BOOKS I USED TO LEARN BI  
\[SQL\]  
• SQL in 10 Minutes a Day: https://amzn.to/3VZztG2  
• T-SQL Fundamentals: https://amzn.to/3Pe5XbC  
• T-SQL Querying: https://amzn.to/3Pe5XbC  
  
\[POWER BI\]  
• Learn Power BI: https://amzn.to/49YiM3C  
• Definitive Guide to DAX: https://amzn.to/408zI3K  
  
💻 VIDEO & DESK GEAR  
• Keyboard (Keychron K10 Max): https://www.keychron.com/products/keychron-k10-max-qmk-wireless-mechanical-keyboard?ref=EDWARDCHARLES  
• Mouse: https://amzn.to/4tuIgPg  
  
Affiliate Disclosure: Some of the links in this description are affiliate links. I may earn a commission if you purchase through them at no extra cost to you.  
⸺⸺⸺

## Transcript

### Introduction

**0:00** · So, this past week, Microsoft released the new July version of Microsoft PowerBI, and there were some really, really cool features in there. However, one in particular really stood out to me, and that is the conditional formatting of legends and lines.

**0:18** · And in today's video, I'm going to be showing you why this is a bigger deal than, you know, it might seem on the surface, how it's going to be saving you a bunch of time, and one really fun, super cool use case, as well as maybe mentioning a feature that like, hey, you know, maybe if we could just add this one little additional conditional formatting thing would make me super duper extra happy. If any of that sounds exciting to you or if you're interested in business intelligence in general, do me a favor.

**0:49** · Go on over and first give this video a thumbs up and then move on over and hit the subscribe button cuz it really helps the channel grow. With that out of the way, let's jump into the computer and let's start learning. All right, let's start by framing the problem that this new feature solves. So, here I have a dashboard that I'm in the middle of building. It's primarily like a black and white themed dashboard.

### How to Conditionally set Line Color

**1:13** · But here I have two charts and they're showing the exact same values only I have customized the colors on this chart and I have not customized the colors on this chart. As you can see they are there's a bunch of different categorical columns here that I would have to go through and customize. Now, traditionally, what I would have to do is I would have to first switch to each categorical color, right?

**1:41** · And choose the color and then or each category and then go on to the next one and then the next one and then the next one. I would have to do this for pretty much every single chart that I wanted to conditionally set the color on. So, as you can imagine, this is a lot of work, especially if you have like 10, 15 charts throughout the entire report. I'm like obviously you could have customized the theme but like you know like not all of us build out custom themes. So this was a lot of work.

**2:08** · Now here's where this new feature comes in and how it's going to save you a bunch of time. So on this page right here I have two graphs and I have customized each of them by using the new conditional formatting.

**2:24** · So what that means is on this pie chart if I go on over here into the slicer section and then go down into slices and then go down into color while I have all selected I have set the color equal to this FX section right here and I've set it equal to the measure primary end use legend color and I've done the same on this line chart. So, if we select this line chart and then go down into lines and then go down into color, you'll see I have set the same FX uh button and I've set it equal to this measure.

**2:54** · Now, if we look at this measure, all this measure is is the really simple switch statement with all of the different legend colors that I want to customize.

**3:04** · And what this new feature means is that instead of having to individually go in and set each category in each every in each chart in the formatting pane, uh, all I need to do now is because I've set both equal to this measure is just update the measure to change the hex code color and the graph updates. Isn't that cool? So, that's going to be kind of the primary use of this new feature in my opinion. However, it also enables some really cool visualization stuff.

### Introduction to Gradients in Line Charts

**3:37** · So, let's take a look at some of that.

**3:40** · So, moving then here onto the line onto this second tab, we have this line graph right here. Now, in this line graph, we have the year on the x-axis, the production volume here on the yaxis, and then the country in the legend. Now, as you can see, this is actually a gradient.

**3:59** · And that's because if we go on over here, right, and then go down over here and lines and then color, you can see I have applied a gradient here based off of uh production, which again is what's in the yaxis. Now, you might be like, well, this is not very good. It's just all gray and it's really hard for me to see what's going on. But what you can then do is you can actually highlight kind of the last line.

**4:29** · So like the highest line here as of the last year and then you can kind of uh single out right like a single data point to highlight. So if we look at this what I've done is I've replicated that gray gradient uh in DAX and then I've said except for the highest value in the last year highlight that one as red.

**4:51** · So as you can see here uh here is the DA not that one here is the DAX that I'm doing to do that where I am actually calculating the gradient unless it's the highest color in the previous year in which case it's highlighting that red.

**5:11** · You also though can then play with the gradients. So for example this gray to this black is a very linear gradient.

**5:19** · Um, and you can make it exponential, which then means that you kind of have this much more interesting like kind of color blocking, which is really pretty fun. So here, right, we have kind of like this exponential gradient. As it gets closer to the max, it goes darker and as it gets lower, it stays lighter.

**5:38** · Now both of these are completely you know like like these are custom DAX formulas but the point is is having this conditional ability to set line or fill color really opens up a lot of features.

**5:53** · Now, I did say I would mention something that like if I could just have it uh would really add to that and that is is I would love if I could also conditionally set the sort order of the legend, right? Because in here the real advantage or like the real cool thing is that I am setting color based off of like volume here, right? So obviously I want the country with the most volume to be over here in the front. So it's obvious which one that is.

### My Dream Additional Feature

**6:22** · So like for example, if I play with this graph and whoopsie, I hit the window key. But if I play with this graph, right? So here we have Australia and then I add an Austria, Belgium, right? You could start to see these lines appearing, but Australia, right, as red is still sitting here at the very end where like, and let's just see if we can get it the top line to switch countries here off of Australia.

**6:51** · Um where's South Africa? Okay so like here for example I hit so now the top line is South Africa but like see this search South Africa is is not the first country. So ideally I would be able to also provide like a legend sort here and that would that would really make this top tier. So Microsoft if you're listening uh you know that is my one one wish.

**7:17** · But with that we've pretty much reached the end of this video. So, I've showed you how this feature works. We've uh, you know, covered it in its full depth.

**7:27** · I'll link this file that I'm showing down below in the video description. And if you read the blog post on Microsoft PowerBI's new July features, and there's another feature that you think is a bigger deal than this one, let me know down below in the video comments. With that, I'll catch you in the next one.

**7:45** · And if you want more of this, you know, again, don't feel give this video a thumbs up, subscribe. It means a lot.

**7:51** · All right, talk to you later. PS, if you're like still watching this and DAX that's generating the gradient was generated by AI, you know, take a look at it. It's pretty interesting. I don't think it's the most efficient way to do it, but for this demo, this video where I just need a quick demo, I honestly think it's it's pretty good. So, you know, look at that, too. Download this file. Take a look. All right. Now bye.