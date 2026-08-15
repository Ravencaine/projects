---
title: "How to Change a Measure in Power BI SAFELY"
source: "https://www.youtube.com/watch?v=4nGEx1qnoBw&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=4nGEx1qnoBw&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Guy in a Cube]]"
published: 2026-07-23
created: 2026-08-08
description: "Learn how to identify and manage dependencies when changing a core measure in Power BI semantic models to avoid breaking business logic and reports.Changing ..."
language: "en-US"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=4nGEx1qnoBw)

## Transcript

### Revenue Redefinition Shock

**0:00** · Yo, what is up everyone?

**0:02** · Imagine it's Friday afternoon, you're getting ready to head home for the weekend when an email from the CEO lands in your inbox.

**0:09** · Starting Monday, I want revenue to mean gross revenue.

**0:12** · Discounts should be reported separately.

**0:14** · At first, that sounds pretty simple.

**0:17** · Open one measure, make a quick change, save the model, and call it a day.

**0:21** · But if you've been building semantic models for a while, like me, you know it's usually not that simple because in a semantic model, a measure isn't just a formula, it's a business definition, and that definition can be used by dozens of other calculations throughout the model.

**0:37** · If I make this change without understanding what depends on it, I might not break anything technically, but I could absolutely change business meaning in places I never, ever intended.

**0:50** · So before I touch a single line of DAX, I wanna answer one question: what else depends on this definition of revenue?

**0:58** · Let's find out.

### Find the Revenue Measure

**0:59** · The first thing I need to do is find where revenue is actually defined.

**1:03** · In this model, the definition lives in a single measure called total revenue.

**1:08** · Right now, total revenue adds room revenue, experience revenue, other revenue, and it subtracts discount amount.

**1:16** · That one line is what makes revenue mean net revenue throughout the entire semantic model.

**1:22** · But there's something else to pay attention to: the description.

**1:26** · And so if we take a look, it tells the exact same story.

**1:29** · Total revenue generated from room, bookings, experiences, and property services after discounts.

**1:36** · That's important because the CEO didn't ask me to change a report.

**1:41** · They changed the business definition of revenue.

**1:44** · Right now, the calculation and the documentation, the description, and the measure, they actually agree with each other.

**1:50** · So on the surface, this still looks like a one-line change.

**1:53** · But before I make that change, because I'm a diligent modeler, I need to understand everything that's built on top of that definition.

### Map Dependencies Fast

**2:02** · So what I'm gonna do is I'm gonna go in the desktop, and I'm gonna switch over to the TMDL view, and I'm gonna select semantic model, and I'm gonna drop it.

**2:09** · And all I need to do is do a quick control F if the find isn't there, and put total revenue.

**2:15** · And if you look at all the yellow spots, you can see the measure is referenced in a lot of places.

**2:21** · But a text search only tells me a little, tiny part of the story.

**2:26** · I can go through and look and look and look, but I can switch over into the service if I have Fabric, and I can ask a question.

**2:35** · Please list all the objects in this model that depends on the total revenue measure.

**2:47** · Go for it, Copilot.

**2:49** · Now, it may take a little bit because it's gotta search the entire model, but it'll come back So you can see it returned a, a list of ten measures, but it's saying, "Hey, there's a measure that transitively depends on total revenue," total revenue year-over-year percent.

### Direct vs Indirect Links

**3:07** · Let me go look at that measure 'cause when I was doing my search, I didn't see it.

**3:11** · Hmm, that's interesting.

**3:12** · When I open this measure up, I can see that it depends on total revenue year-over-year change, which… Let me go take a look at that measure.

**3:24** · Ah, it depends on total revenue.

**3:27** · Now, that's an important distinction because some dependencies are direct and others are indirect.

### Validate with DAX Tools

**3:34** · But what I wanna also do is I wanna verify this in my semantic model, so I'm gonna go back to the desktop.

**3:42** · In my DAX view, you can see I've written a, a query that uses the INFO calc dependency function, and you can see I'm creating a table.

**3:49** · I'm filtering that table down to only measures, and particularly only the total revenue measure.

**3:54** · So I'm selecting from that table only these four columns, and I'm ordering it by this.

**3:59** · And if I run this, what you'll see is that I get those 11 rows.

**4:02** · Notice, you know, if I wouldn't have used Copilot, I probably wouldn't have found out about the indirect dependency.

**4:08** · But what this also tells me is that this depends on a metric view.

**4:13** · It's one of the field parameters in the model that references total revenue.

**4:16** · Now, there are excellent third-party tools that can visualize dependency trees and take this kind of analysis even further down the road.

**4:24** · But for this change, everything I needed was already built in the Power BI desktop.

**4:29** · Now, I have a complete picture.

**4:31** · I understand the direct, the indirect dependencies, and I understand the other model objects that are affected, and now I can make this change with confidence.

### Rename to Gross Revenue

**4:41** · The first thing I'm gonna do is rename the total revenue measure to gross revenue.

**4:47** · That's simple Now, what's interesting is, let's go take a look at one of the measures in the field parameter.

**4:55** · For example, revenue per booking.

**4:58** · Notice how the measure automatically updated.

**5:01** · I didn't have to go do it.

**5:02** · Or if we go take a look at the field parameter, the technical reference inside the field parameter, it changed, but the business-facing label didn't change, and we'll come back to that.

**5:14** · Power BI can update object references automatically.

**5:17** · It can't decide what the business should call them.

**5:20** · I also have a few related measures that still use total revenue in their names, and I'll clean those up.

### Keep Both Definitions

**5:26** · But before I do that, I need to make an architectural decision.

**5:31** · Now I have to decide how I'm going to implement this business logic.

**5:35** · I could simply change the existing calculation, but if I do that, the original business definition disappears.

**5:42** · Someone may still need after discounts.

**5:46** · So instead of replacing that definition, I'm going to preserve it.

**5:49** · Right now, gross revenue still is subtracting discounts.

**5:53** · That means the name changed, but the business definition, the business meaning didn't.

**5:57** · So let's fix this.

**5:58** · I'm gonna get rid of that.

**6:00** · So now that I removed that, I need to create a measure called net revenue.

**6:05** · And net revenue is gonna be something really easy.

**6:08** · So what I'm gonna do is go into this folder, 'cause I wanna keep it in my revenue metrics folder.

**6:13** · I'm gonna call it net revenue equals gross revenue minus the sum of discount.

**6:21** · Now I have both business definitions available: gross revenue before discounts, net revenue after discounts.

### Document and Expose Metrics

**6:27** · And this is the part that's easy to overlook.

**6:31** · Changing the DAX isn't enough.

**6:34** · If someone opens this semantic model, let's say six months, a year down the road, they shouldn't have to reverse engineer what these measure names mean.

**6:42** · I need to update the descriptions to fully bring that business logic to my semantic model.

**6:48** · Let me go back to the model, and I'm gonna go to gross revenue, and I'm gonna change this to gross revenue Before discounts.

**6:57** · And then I'm gonna copy this, and I'm gonna go to my net revenue, and I'm gonna add a description, net revenue after discounts.

**7:08** · And what I'm gonna do is I'm gonna format this to currency and change this to two decimal places.

**7:15** · And I just wanna make one more change.

**7:18** · And where is my metrics view?

**7:20** · There's my metric view.

**7:21** · And you can see right here, I just have total revenue.

**7:24** · That's gross.

**7:25** · So I'm gonna name that gross revenue.

**7:27** · And now I can go modify my field parameter.

**7:29** · I can go down here and add another one for net revenue if I want to, and make it exposed.

### Clean Up Model References

**7:34** · So there's a few measures that I know still have the name total revenue.

**7:39** · So I'm gonna manually change these, right?

**7:41** · And it's not gonna hurt much.

**7:43** · Gross revenue.

**7:47** · I'm gonna fix those really quick.

**7:48** · So now I have those fixed, and I created an abbreviated TMDO script that contains all the measures that's referencing total revenue in the description.

**7:58** · So what I'm gonna do is I'm gonna select total revenue, Control+Shift+L, and I'm gonna change it to gross revenue.

**8:06** · I click Apply.

**8:07** · All my definitions are updated.

**8:09** · Now the calculations, the names, the documentation are all telling the same story.

### Repeatable KPI Change Process

**8:15** · Every time someone asks me to change a KPI, I follow the same process.

**8:20** · First, understand the change, then I need to measure the blast radius, measure the impact, decide how to implement that change, and finally, make sure the semantic model tells the same story as the business.

**8:32** · Power BI helped me safely update the technical references, but deciding what revenue actually means, that's still my responsibility.

**8:41** · We'll see you in the Cube!