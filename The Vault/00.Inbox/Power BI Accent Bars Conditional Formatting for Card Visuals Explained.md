---
title: "Power BI Accent Bars: Conditional Formatting for Card Visuals Explained"
source: "https://www.youtube.com/watch?v=b5hYSzDF-zs&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=b5hYSzDF-zs&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[PorcuBI - Valerie Junk]]"
published: 2026-08-04
created: 2026-08-08
description: "Want a subtle way to show whether a number is good or bad in Power BI, without shapes or workarounds? Accent bars on the card visual let you do exactly that. In this video I show you why conditional f"
language: "en-US"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=b5hYSzDF-zs)

Want a subtle way to show whether a number is good or bad in Power BI, without shapes or workarounds? Accent bars on the card visual let you do exactly that. In this video I show you why conditional formatting doesn't work the way you'd expect when you combine values into one card, and the simple fix of splitting them into separate cards. I also walk through setting up accent bars and applying conditional formatting using both rules and a DAX measure.  
  
Subscribe to stay updated on my new content!  
\---------------------------------  
⏰ TIMESTAMPS  
\---------------------------------  
00:00 Introduction  
00:47 Power BI demo of accent bars  
02:01 Setting up accent bars  
03:28 Conditional formatting options  
  
\---------------------------------  
😊JOIN  
\----------------------------------  
Website https://www.porcu.bi  
LinkedIn https://www.linkedin.com/in/valeriejunk/  
#PowerBI #DataViz #DataVisualization #CardVisual #ConditionalFormatting #PowerBITips #PowerBITutorial #DAX #PowerBIForBeginners #DataStorytelling

## Transcript

### Introduction

**0:00** · In this video, I want to show you how you can use conditional formatting for the accent bars in the card visual in Power BI, which is such an easy way to guide the attention of the user.

**0:12** · Because if you look at these accent bars, they are very subtle. You can put them at the top of the card visual, or at the bottom, or left, or right, and you can make them like two, three, four pixels wide, so they're not like in your face, something's wrong.

**0:29** · They're just a subtle way to show did we hit a target, how is this value compared to, for example, last year, and all these kind of things. So I want to show you how to create them.

**0:40** · So let's go into Power BI. And here you see a report where I actually did this, where I actually did that. You see, I have sales this year, target quantity, average sales price.

### Power BI demo of accent bars

**0:51** · And you see at the top I have these accent bars. I also have some little shapes here, but let's focus on these accent bars. Now, if I click on a category, for example headphones, you see they change, now they're all green. And office electronics, they're all bad because they're lower than last year. And office supplies, we see some of them are red, some of them are green. And of course, you could pick every color you want here. I used red and green. I use red and green because in the shapes that I have, I also have like an arrow up or down, so if someone couldn't see red or green, they still could see the context of what is going on.

**1:29** · Now when I tried this the first time, it didn't work because I chose the card visual. I click on this to show you. Actually, this is the card visual. And in the card visual you can add all kinds of values. The problem is, if you, I can show you, if you have your card visual here and let's say we add another value here, and we go to cards and accent bars, what happens is the conditional formatting that we can apply applies to everything. And that doesn't make a lot of sense because I want it to be applied for every card. So what's the workaround here?

### Setting up accent bars

**2:02** · I just create. So what's the workaround here? I create a card for all my values. Now that's not even that much extra work because, if you ever created the, if you ever use the new card visual, you know you need to apply everything for every card, every value, every detail, every reference level, reference label. If you ever use this card visual, you know that even if it looks very easy to add all these values, you need to click so many times to make changes to the detail, to the label, to everything. So you can just create four or five of these KPIs one by one. There's not that much extra work here, at least I don't change stuff by accident anymore.

**2:34** · So here I have this value, so here I have this card, and I can show you what I did before.

**2:37** · Before I knew this trick, I inserted a shape, like this, and then I put it behind the value, and then I would say shape style fill, and use the conditional formatting there.

**2:49** · And the tricky thing is, it never lines out completely, it always looks a little bit off.

**2:55** · So I was really wondering how to fix that. But you can do that with the accent bars.

**3:00** · So I click on my card visual and I go to cards in the format pane, and there you have accent bars. And you can say where you want the accent bars, or you could also have it at the bottom, at the right, at the left. Maybe at the left would also make some sense. I chose the top, just personal choice here, of course you would need to discuss this with the user. And you see I have a width of seven. You could do one, then it's super subtle, you can almost not see it.

**3:26** · Don't do that. So you can always, then you also can do one, and then it's super subtle, you can almost not see it. I chose seven because that's at least, you can see that, but it's not too much.

**3:26** · And then what's happening here is the conditional formatting. Conditional formatting, if I open this, you see I have it based on the field value. You can say gradient, rules, field value. You could say rules, for example sales difference: if the sales difference is above zero, I want a certain color, if it's below zero, I want a certain color. So you could totally do this rule based. I chose field value because I created a DAX measure that actually tells me which color to use. I can show you, I can show you, it's this one. What did I do there? It's a DAX measure. Let's increase this.

### Conditional formatting options

**3:59** · Well, I say if my sales difference, yes, yeah, in this example, is above zero, I want this color, and that's the green color that we see, otherwise I want the red color. And then I can do the conditional formatting field based. Like I said, you could totally do this also rule based. And the most important part is that you click on your card visual and you enable the accent bars. They're not enabled by default, you, so you need to enable them and then choose this rule.

**4:32** · And this makes it so much easier to see what's going on. And I thought, let's share this, because I worked for the longest time with the workaround using the shapes, grouping everything, and then it's never perfectly aligned. So let's share all the good stuff.