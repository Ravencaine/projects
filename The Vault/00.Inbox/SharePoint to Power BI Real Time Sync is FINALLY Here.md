---
title: "SharePoint to Power BI Real Time Sync is FINALLY Here"
source: "https://www.youtube.com/watch?v=CyXO3u47QZs&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=CyXO3u47QZs&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Drop Materialized View]]"
published: 2026-07-15
created: 2026-08-08
description: "Learn how to set up real-time SharePoint Online list data in Power BI using the new Microsoft Fabric SharePoint Mirroring (Preview) and Direct Lake mode.00:00 Introduction00:37 Setting up a Connect"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=CyXO3u47QZs)

Learn how to set up real-time SharePoint Online list data in Power BI using the new Microsoft Fabric SharePoint Mirroring (Preview) and Direct Lake mode.  
  
00:00 Introduction  
00:37 Setting up a Connection to Sharepoint  
01:19 Mirroring Sharepoint Data into Fabric  
02:40 Writing SQL against a Sharepoint List  
03:59 Creating a direct Lake Semantic Model  
06:44 Testing Mirroring Speed  
  
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

**0:00** · In this video, I'm going to be showing you how you can mirror the contents of this SharePoint site into Microsoft Fabric so that way you can build out a direct lake Power BI semantic model that allows you to see SharePoint site or SharePoint data in Microsoft Power BI in near real-time. Now, if any of that sounds interesting to you or if you just enjoy business intelligence in general, if you could do me a favor, go on over, give this video a thumbs up, and then move on over and hit subscribe button.

**0:27** · It would mean a lot as it really helps the channel grow. All right, without further ado, let's jump into the computer so that way hopefully this video is pretty short and sweet. We're going to start off in Microsoft Fabric and we're going to make sure that we have a connection to our SharePoint site already configured. So, I'm going to go over here, hit this little settings button right here, and then go over here and hit manage connections and gateways.

### Setting up a Connection to Sharepoint

**0:51** · Now, I already have a connection to SharePoint configured. It's not probably appropriately configured for enterprise setting as I'm just using single sign-on, but for this video demo, I, you know, I think that works.

**1:04** · That said, if you are going to be using this in an enterprise environment, I would recommend not authenticating in under your own personal email. That said, again, all we need is a working connection. After that, we're going to go back into our workspace. We're going to hit the new item button, and then in the pop-up, we are going to search for mirrored SharePoint online list. Now, this is in preview at the time of recording this, so your admin might need to enable it for you. However, you know, it just popped up for me.

### Mirroring Sharepoint Data into Fabric

**1:33** · So, all I need to do is click this button, then uh click the connection that I already have set up in OneLake right here.

**1:45** · And then, once this has loaded, I can choose to either mirror specific data or specific item types or the entire site.

**1:55** · In this case, I'm going to choose to mirror the entire site, so I'm not going to really wait for this to load.

**2:00** · Although, here you go. Right, here's the list and then here's my document library. Uh I'm just going to simply hit connect.

**2:07** · And then I am going to say, "Hey, create a mirrored database." You can give this a name. I'm going to be creative and give it a name of SharePoint. And then I'm going to hit this create a mirrored database. Now, what this is going to do is this is going to create a mirrored database for the SharePoint site where I'll be able to see my documents as files and then my lists as tables. And it's also going to create a SQL analytics endpoint that we can use to create a semantic model. So, let's jump at the computer and let's get that all set up.

**2:35** · So, what you should now have is you should now have the actual mirrored database itself and then a SQL analytics endpoint. If you go into the mirrored database, you'll be able to see the document library if you hit the refresh, but you might not see any lists right away in my experience. So, let's see if we can't fix that. Let's go over here and let's hit this query in T-SQL button. And then let's uh query hit this new SQL query button. And then we're going to type over here select star from and it'll be SharePoint.dbo or the name of your mirrored database.

### Writing SQL against a Sharepoint List

**3:10** · And then and then the name of the list.

**3:11** · So, in this case, my list is named test.

**3:14** · And I'm going to go ahead and hit run.

**3:16** · Now, what this should do and we'll see if it throws an error is it should return the results of the list, which it did. So, now when we go on over here to schemas and then hit this old little refresh button right here and then expand DBO and then expand tables, we now have our list coming up as a table.

**3:37** · If we then flip back on over here into our mirrored database and then hit this refresh button, what we should then see now is we now have this list coming through. I'm not totally sure if this is an error or if it's just a timing thing and if I let it sit, it would eventually catch up. But, you know, this is what I do, and it works for me. Okay, now it's time to create our semantic model on top of our mirrored SharePoint database.

### Creating a direct Lake Semantic Model

**4:02** · Now, when we create the semantic model, we're going to be creating a direct lake semantic model. A direct lake semantic model is essentially a semantic model that's reading the parquet files directly out of Microsoft Fabric OneLake.

**4:15** · This is different than a standard import model or a direct query model. In the import model, it's taking the data and compressing it, and in a direct query model, it's actually executing SQL.

**4:29** · I probably way oversimplified this. I probably stated something slightly wrong, as this is very, very, very technical. However, at a high level, that's the general concept as I understand it. So, then, in order to create this direct lake semantic model, all you need to do is hit this little create a semantic model button. Now, in the pop-up, you'll be able to select what tables or views you want included.

**4:51** · However, you'll also get two options.

**4:52** · You'll get direct lake on OneLake or direct lake on SQL. Now, the difference between these two is a little confusing for me, so I had to look it up. Direct lake on SQL will fall back to the SQL endpoint. But, what that essentially means, from my understanding, is that you're limited to just, you know, files or tables in that SQL environment. So, like, for example, in this SharePoint site.

**5:18** · However, if you go direct lake on OneLake, you lose that direct query fall back, so you're completely dependent on the parquet files. However, what it means is that you can access any file or any other data source that is actually storing data in OneLake. I opted to build my semantic model using direct lake on OneLake. What this means is that I am constrained to how much data I can load into memory. I don't have that direct query fall back. It also means that I can't access views.

**5:47** · However, it gives me the advantage that I can then add additional data to blend with this SharePoint data. So, I'm going to give this a quick name of video demo, and then I'm going to go ahead and hit this confirm button and let Microsoft Fabric build out my semantic model. Then, once this is built, I should have a semantic model that I can either add more data to or I can build a report on top of.

**6:11** · So, for example, right here, if I click new report, it will pop up, ask me to log in, and then I should be able to build a new report with all of the columns from uh all of the columns from my SharePoint list. So, here, for example, we have these things coming in, right? So, here is the title and here is the test. So, right here, you know, creative high business impact visual going on right here. So, let's save this report, and then let's test some latency.

**6:40** · So, I'm going to title this video demo, and then we are going to go ahead and we're going to make a change on our SharePoint site and then see how long it takes to pop up in this report. Okay, so uh I've got something up and ready to edit on the SharePoint site. So, I'm going to go ahead and hit save and start at the same time, and we'll see how long it takes for it to appear in Microsoft Power BI.

### Testing Mirroring Speed

**7:06** · So, going back over here, let's go ahead and hit this refresh button.

**7:11** · I think there should be a latency of Oh, and there it was. So, that was uh 15 seconds that it appeared. So, I guess the latency is really pretty nonexistent. In my previous test, it was taking like 3 to 6 minutes, but maybe I just hit something right on the cache.

**7:27** · So, let's try that maybe one more time.

**7:31** · So, we had 15 seconds. I'm going to go ahead I hit the restart button right here. I'm going to add another item right here, and I'm going to go video demo two or three, I guess. Give it the same date.

**7:46** · Okay. Ready?

**7:49** · We got the start button here. This is kind of a balance. So, let's see.

**7:54** · And start. I don't know. I didn't hit Okay, there we go. So, add a second to that. So, it's now on SharePoint. Let's go back over here.

**8:01** · Refresh this one more time.

**8:04** · So, we're 6 seconds in. Previously, it took 15 seconds.

**8:08** · So, let's see.

**8:10** · 13 14 15 Okay, it's been 15 seconds. Still hasn't appeared.

**8:17** · Uh so, we called it video demos three.

**8:20** · Let's go back over here.

**8:23** · There it is. It just appeared 27 seconds. So, that's pretty good replication and pretty close to near real time. I'm going to say near real time so you know, it's not exactly real time, but I made a change, it appeared 30 seconds later. So, with that, you've made it to the end of this video. I hope you're excited about mirroring and mirroring SharePoint. And I hope you learned something. If you did, again, you know, consider giving this video a thumbs up and hitting the subscribe button. I'll talk to you in the next one. Bye.