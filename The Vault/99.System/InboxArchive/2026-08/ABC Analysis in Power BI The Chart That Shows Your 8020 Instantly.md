---
title: "ABC Analysis in Power BI: The Chart That Shows Your 80/20 Instantly"
source: "https://www.youtube.com/watch?v=lvUELVwxdMI"
video_url: "https://www.youtube.com/watch?v=lvUELVwxdMI"
creator: "[[How to Power BI]]"
published: 2026-07-13
created: 2026-08-08
description: "👉 Want to master Power BI report design (in the age of AI)? Join my live 4-Week Power BI Design Transformation Program: https://datatraining.io/powerbidesigntransformation------------------------"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=lvUELVwxdMI)

👉 Want to master Power BI report design (in the age of AI)?  
Join my live 4-Week Power BI Design Transformation Program: https://datatraining.io/powerbidesigntransformation  
  
  
\--------------------------------  
📊 TRAININGS 📊  
\---------------------------------  
➡️ Power BI Design 4-Week Transformation Program in the AI Age  
https://datatraining.io/powerbidesigntransformation  
➡️ NEW! User-Defined Functions (UDF) Training  
https://datatraining.io/powerbi-udf-training  
➡️ Power BI Data Analyst + PL-300 Study Resources  
https://datatraining.io/powerbi-pl300  
➡️Power BI Business Users  
https://datatraining.io/powerbi-business-users  
  
  
\--------------------------------  
🎯 CONSULTING 🎯  
\---------------------------------  
  
➡️Need a Power BI expert to build or improve your report?  
https://datatraining.io/powerbi-consulting  
➡️Need a Fabric expert to build your data infrastructure?  
https://datatraining.io/fabric-consulting  
➡️ Custom or urgent training & consulting  
support@datatraining.io  
  
  
\---------------------------------  
🤩 JOIN 🤩  
\----------------------------------  
Newsletter https://datatraining.io/newsletter  
Join YT https://bit.ly/4b453bi  
Subscribe https://bit.ly/31MnQGO​  
Insta https://www.instagram.com/howtopowerbi/  
LinkedIn https://www.linkedin.com/in/basdohmen/  
TikTok https://www.tiktok.com/@how.to.power.bi  
X https://twitter.com/HowToPowerBI  
fb https://www.facebook.com/groups/howtopowerbi  
Threads https://www.threads.net/@howtopowerbi  
  
Thanks for being a part of this channel and all your support! 💪 🙏  
  
#HowToPowerBI​ #PowerBI​ #DataTraining​ #BasDohmen  
#powerbidesktop​ #powerbitraining​ #powerbideveloper​ #DAX #fabric #fabricai  
#PowerBI #PowerBIAI #Copilot #DataVisualization #design #designtransformation

## Transcript

**0:00** · In your analytical reports, you want to put focus on those products and those clients that matter the most. And usually, it's 20% that is driving 80% of your revenue or whatever KPI that you're looking at. Now, this is called the 20/80 rule or the Pareto principle. And based off this, you have ABC classification, which categorizes your items in three different buckets, ABC, based on how much they contribute. Now, this chart really nicely visualizes that. You have a Pareto line with the three buckets as an overlay.

**0:28** · And also, it's a super interesting one to build because it uses visual calculations and a few formatting tricks. So, let me walk you through the steps to set this up.

**0:40** · The main point of the visual that we're going to build is to see which products are the most important to us based on how much they contribute to over revenue. An ABC classification is a great way to do that. The A bucket or the A group contains all of those products that contribute together up to a certain percentage. Now, here I put that percentage to 40%. And then, all of those products that come after, that contribute the 40 to 80%, that's our B group.

**1:08** · And then, you probably have a bigger C group with all of those products that just contribute a little and maybe shouldn't deserve that much attention. Now, this is also a great example of how to use visual calculations in a very practical way.

**1:22** · Still quite underused by many Power BI developers. So, let's see how this works in action. Now, let's insert here a line and clustered column chart. I'm going to make it a little bit bigger.

**1:31** · All right, put it in the middle. And on top of it, on column Y-axis, I want to see total sales.

**1:38** · And on the X-axis, we're going to have a product breakdown. So, look for product.

**1:44** · Here we have product name, product ID.

**1:45** · I'm just going to go for product ID, and later on, we can swap it for whatever dimension that we like. Okay. Now that we have this, the next step is to calculate the percentage that they contribute of the total. Now, we can do this with a normal measure, but if this is something that you just need for this visual, then visual calculations are great. And that's the path that I'm going to take here. I'm going to put this on the line Y axis.

**2:06** · This is the icon for visual calculations, and let's call this one percent of total is equal to where we want to divide the total sales, and this we want to divide by the total overall sales. Now, to calculate that, we need the collapse all function, and we want to get the total sales where we collapse whatever we have on rows.

**2:32** · Now, you see I'm not hard coding product ID or product name, no rows, because this offers more flexibility. When we change the chart to a different breakdown dimension, then this will still work. Okay. Now, we can close our divide, and there you go. We now have the percentage of total sales, but this is just an in-between step, because the next thing that I want to have is that little Pareto line, the cumulative sum these percentages, the running sum. So, I'm going to go back here to the line Y axis, click on add data, visual calculation.

**3:04** · Let's call this one running sum is equal to, and there's a running sum function. I want to have the running sum of percentage of total.

**3:14** · All right. And then, on the axis we have just rows.

**3:18** · Again, I'm not using product ID here, because I want to keep it flexible. Now, order by. Here, don't make the mistake that you say order by percentage of total total sales. What you need to do is order by function, and then you can say percentage of total or total sales.

**3:37** · Doesn't really matter here, and I want that in ascending or descending order. Now, we want to have descending, and then close the order by function, and close the running sum function. And there you go.

**3:50** · We have our little Pareto line. Now, you might think, okay, now I can get rid of that calculation from before, that running sum. However, don't do that because for visual calculations, you can only use the values that are coming from measures or other calculations that are on your visual. All right? So, if it's just living there in your data pane, but you didn't add it to the visual itself, you cannot use those measures. All right? So, that's the same thing that we have over here. But, if you don't want to show it in the visual, you can just hide it. All right?

**4:19** · So, over here with that little eye icon, you can hide or show a visual calculation. Perfect. So, this probably looks familiar. This is kind of like more that traditional Pareto chart. But, let's not end here. I want to take that one step further. I want to show still that Pareto line, but now overlay these three different buckets, the A, B, C classification buckets. Now, let's see how we can do that. Now, I'm going to go back to our visual.

**4:46** · Now, one thing that's going to be different is that we are not going to show the individual total sales bars anymore because the focus is going to shift to which group do you belong to, which bucket, A, B, or C. So, I want to get rid of total sales, but not delete it because we are still using it in those visual calculations.

**5:03** · So, what I'm going to do instead is add it to the visual calculation and hide it from the visual. Now, what's happening?

**5:10** · Over here, sorting seems to be off. We are not sorting anymore by total sales because when a field is hidden, hm, you cannot sort by it. Hm, not a good solution. So, let's go back again. I'm going to unhide it, \[clears throat\] and instead of that, I'm going to drag and drop it onto tooltips.

**5:27** · Go back, and now you see we can sort by total sales. All right, and it's not visible in the visual. Okay, so now we have only that line. I'm just going to put a filter in place on the category, so let's look for category.

**5:43** · Put it there, and let's select one so that we don't have that many. And I also want to clean it up a little bit, so let's go to formatting. And here you see we have not percentages, but just decimal values. Now, to fix that, we have to go to properties, data format.

**5:58** · You see, over here we can change the data format for visual calculations. So, I'm going to select here the percent of total decimal number percentage formatting with zero decimals. And I do the same thing for that running sum. So, I'll say here decimal number format percentage zero decimal places. Okay, so now you see we have nicely the percentages showing up. Then let's also go back to the visual formatting for the line. I want it to show maybe just in black. Let's keep it simple, black.

**6:29** · Now, the next part is going to be really interesting because how do we get these shaded areas in? Well, for that we need again visual calculations plus a few formatting tricks. Now, building really good Power BI report isn't about simple tricks or making things look pretty. It's about knowing exactly what needs to go in your Power BI reports and how to best visualize it.

**6:51** · And of course, having the technical skills to do so. Now, my team and I have helped hundreds of companies across all different kinds of industries build effective Power BI reporting solutions.

**7:01** · Now, if you want to learn all of our processes, frameworks, and get our templates of how we do it, then check out our upcoming Power BI design transformation over here. Now, I hope to see you there. Let's go back to the video.

**7:12** · Let's go over here to our visual. Let's add now on the column Y axis a visual calculation. And this one we can call group A, which is going to be equal to and I want to check if the running sum is uh lower than or equal to 0.4, then return 0.4. Okay. And otherwise, nothing. And then we just copy that and do it two more times for group B and C.

**7:40** · So, over here column Y axis, then also over here, we need that same formula, but for group B.

**7:49** · And here we want to check if it's equal to a lower than 0.8, then return 0.8.

**7:54** · And then one more time for group C. And over here I want to have the cutoff point to be one, so I can just simply return always one. Okay, now let's go back. Let's go here to the filters and just choose a different category for the moment because over here that first product straight away had more than 40%.

**8:14** · All right, so therefore I'm just switching to, let's say, electronics.

**8:18** · Okay, now this looks not so pretty.

**8:20** · However, with few formatting tricks, we can convert this into shaded areas. Now, let me show you. Let's open up the formatting panel. Let's go to columns.

**8:30** · Make sure that series is selected all.

**8:33** · And then over here on the layout, we're going to turn overlap on. Then here we have the space between the series. And if you put this one to 100% and the space between the categories to 0%, boom, you have one big shaded area. Of course, I'm hoping for three. So, we have to flip the overlap or alternatively, you can also change the order over here, whatever you prefer.

**8:54** · So, over here it's probably easier to just use that flip overlap button. You see now we have exactly those three shaded areas. We have the blue, the light blue area up to 0.4%, the dark blue up to 80%, and then the remaining part gets the orange. Now, these are maybe not the prettiest colors, so I'm I'm just going to change that. For group A, I'm going to make that more intense green. Group B, I have a lighter shade.

**9:22** · And for group C, I have an even lighter shade. All right, perfect. Now the lines somehow changed more to purple. I thought I chose black.

**9:30** · Let's just change it quickly back to black. All right, good. Now you can also add maybe a few markers. So, if we go here to markers and then here turn them on.

**9:41** · And I only want to have them for that line, but not that big. And the line itself, let's put the width to two pixels. I believe they're also grid lines still turned on, which I don't need. I'm going to turn them off. Okay.

**9:55** · So, now we're pretty close to that end visual that we were going for. However, there's one more thing left. And that is we have to well, classify the groups with a label. We have to still label them A, B, and C. Now, also here visual calculations and a small trick. This one was actually a little bit more tricky than I expected it to be because you have to figure out which one which product is the last one in its bucket.

**10:22** · All right. So, to do that, let's add over here on the line Y axis a visual calculation. And let's first try it out for bucket B.

**10:31** · All right. I used a next function. Now, the next function just returns the next value that you have on rows. So, if I would just say next, everything looks a little bit messed up, but just focus here on column B. The next sales for B1 would be B2, which is 542,000.

**10:50** · Yep. So, that one is correct. Okay.

**10:52** · However, it is using the next one based on product ID. Hmm, and that's not really what I want. We need a different sorting order. Okay. So, if we go back, also here the next function it allows you to, first of all, change the steps what you have on the axis, okay, rows.

**11:11** · But then the important part, that's order by. And here you need to use again that same trick as before, order by and then say total sales, or actually not total sales, the running sum. Running sum. All right. And we can close that function. Okay. So, now it's working. Let me just swap it from column Y axis to line Y axis. Okay, now that looks a little bit weird because let's go back.

**11:39** · I am returning total sales here. I don't want to have the total sales. I want to have the running sum. So, now you see it is working. We shifted our line basically to the left. If you look here at the first product, it returns here for the purple line the value of the next product. Okay, so we fixed that sorting issue. Now, let's make an adjustment however because I don't want to have the running I'm going to swap that now simply with the group B value. All right, so let's see what this does. And now you see we have the limit of the bucket that the products belong to for all items except the last one.

**12:11** · And now we can set up a rule. So, here we can go back and we could say something like if group B value minus what we just returned and is bigger than zero, then return zero. And you see we now have there at the bottom. Yep, you have to watch very closely a point for only the last one in that group. Now, why go through so much effort? Because then we can just apply a label to it and that's it and make that little dot disappear.

**12:41** · Here on the lines B, we can make it disappear. Okay, and then we have to do the same thing for the marker as well. Make it disappear.

**12:51** · And then here for the data label for only that one, I return it on. So, data labels on. Everything else and we're going to hide and then for B, we leave it on.

**13:02** · Now, here you see the label. It doesn't show the right thing though. So, therefore title on, value off. And then we can make title a little bit bigger.

**13:11** · Boom.

**13:12** · Okay, now we just have to repeat that same thing two more times for group A and for group C. All right, and it's done. I also cleaned everything up a little bit and here we have the end visual that we were going for. Now, what happens if you change your mind and you don't want to have product ID, but product name or whatever you want to show? Let's try it out. You see, it still works because inside of the visual calculations, we were using rows, not hard coding any product fields. Okay, now of course, the next thing that we need to do is clean up the tooltips and make it look a little bit nicer.

**13:43** · However, that's the whole idea. Now, I hope this is something that you can use in practice and that you learn a little bit more about visual calculations and a few formatting tricks. Now, if you want to learn all of my tips and tricks and about my whole report development process, also how I integrate AI now into that process, then check out my upcoming design transformation program over here. Thank you for watching and see you in the next video.