---
title: "A SIMPLE Way AI is changing my POWER BI workflow"
source: "https://www.youtube.com/watch?v=rDuHokI3YBQ&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=rDuHokI3YBQ&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Drop Materialized View]]"
published: 2026-07-04
created: 2026-08-08
description: "In this video I demo a PowerShell script that automatically creates a perfectly shaped box around a group. The Script is here for you to download: https://github.com/edwardpcharles/Power-BI-Projects"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=rDuHokI3YBQ)

In this video I demo a PowerShell script that automatically creates a perfectly shaped box around a group.  
  
The Script is here for you to download: https://github.com/edwardpcharles/Power-BI-Projects/blob/main/Scripts/Add-GroupShapeBorder.ps1  
  
00:00 - Introduction  
02:06 - Scripts in Power BI  
  
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

**0:00** · Hello, my name's \[clears throat\] Ned.

**0:01** · I'm a Microsoft MVP with a focus on Power BI and in today's video I'm going to be showing you and talking about how AI is changing the way I build Microsoft Power BI reports because it is having a real impact on my day-to-day workflow.

**0:14** · And the way I'm going to do that is with a really simple demo. Hopefully, you'll see and you'll be inspired to see if you can't also implement in your own workflows.

**0:23** · So, with that let's jump to the computer and let's take a look. Now, the real change for me is that it to happen when Power BI introduced PBIR or Power BI enhanced report format as the default Power BI report format. What this means is that if you're in Microsoft Power BI and you want to save a report and you save it as a Power BI project file, you get to see all or the entire report definition in JSON in a different report structure.

**0:53** · So, this right here is a Power BI report that has been opened up in VS Code. So, as you can see I have a definition folder and then within that definition folder I have various JSON files that actually represent or make up the report.

**1:09** · Now, this file format makes editing a Power BI report with an AI agent or code really simple because when you open up one of the JSON objects you'll have a schema up top which the AI agent or code can point to to see exactly how a visual should be structured and then you can actually edit the visual by simply making a change to the code.

**1:31** · With the new Power BI AI agent skills, you also now get a CLI that then allows you to reload the report uh based off of the code in real time by simply typing Power BI Desktop space reload. And if you have Power BI open, it will automatically refresh the Power BI report in the background. So, what that means is you can make a change, go Power BI Desktop reload, and then hit enter.

**1:58** · Now, while I am often having the actual AI agent make the change to the report, what I also am doing is I am creating things like PowerShell scripts. Now, PowerShell scripts, if I have the AI agent write it, can automate certain kinds of design rules.

### Scripts in Power BI

**2:16** · So, this for example, is a PowerShell script that when I select a group in a Power BI object, will automatically create an evenly spaced shape around that group with the right amount of padding, which makes formatting really, really simple. So, let me give you a quick demo as to how uh this works. So, I'm going to delete these shapes.

**2:41** · And then, I can go into VS Code here, hit run on the PowerShell script, and then it will ask me for a page ID, which I can get by simply right clicking, and then going copy page ID, pasting in the object ID right there,

**3:00** · and then go back and when it'll ask me for a group ID, which I can get by right clicking, and then going copy object name, right here, and then giving it saying, "Hey, I want a shape with a padding of 30 px around the group." and hitting enter, and then simply typing right here, Power BI Desktop reload.

**3:20** · At which point, when we go back into Power BI Desktop, we now have a nice evenly spaced shape. Now, this is really cool because what I can then do is I can delete the shape back out, and let's just say these slicers were randomly placed over here, right? So, we're going to change the shape that I want. I can go ahead and hit save, and then I can simply rerun that by clicking this run again.

**3:48** · Again, we'll just copy that same page ID from above, right here.

**3:53** · Copy that same group ID right here.

**3:59** · And then saying, "Hey, I want padding of 20 pics."

**4:03** · And then going Power BI Desktop reload.

**4:06** · And just like that, I now have a different shaped box or border. So, scripts like these are changing how I build reports. Creating a perfectly evenly spaced shape like this previously would have probably taken me 5 10 minutes, now it takes me 10 seconds, and it's all because I have this really easy-to-use script that I built in a few minutes using AI. I'll link the script down below on my GitHub in the video description, by the way.

**4:32** · So, with that, you've reached the end of today's video. I know it was a quick one, but if you enjoyed it, you know, give it a thumbs up and hit the subscribe button. And with that, I'll catch you in the next one.