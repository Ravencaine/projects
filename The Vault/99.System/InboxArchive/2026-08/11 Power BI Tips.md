---
title: "11 Power BI Tips"
source: "https://www.youtube.com/watch?v=S6_HWtxywhg&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=S6_HWtxywhg&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Guy in a Cube]]"
published: 2026-07-16
created: 2026-08-08
description: "After watching this video, you'll be able to apply practical Power BI tips that improve your data modeling, report building, and overall Power BI project eff..."
language: "en-US"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=S6_HWtxywhg)

## Transcript

### Introduction and Overview of 11 Power BI Tips

**0:00** · Yooo, what is up everyone?

**0:03** · Power BI people love to share tips.

**0:06** · Some of them are genuinely useful.

**0:09** · Some of them, pretty clever.

**0:10** · Some solve problems though that shouldn't exist in the first place, and a few of them are absolutely bananas.

**0:19** · So I pulled together one, two, three, four, five, six, seven, eight, nine, ten, 11 Power BI tips that people swear by, and I ranked them from 11 all the way to number one.

**0:29** · I'm looking at how useful they are, how surprising they are, and whether I'd actually use them in a real Power BI project.

**0:37** · You know how we like to do.

**0:38** · Let's get into this.

### Tip 11: Turn Off Auto Date Time and Manage Date Tables

**0:39** · Coming in at number 11, turn off auto date time.

**0:43** · When you add a date column to a Power BI model, Power BI automatically creates these hidden date tables behind the scenes.

**0:50** · And for a quick report, that's fine, but once you start building a real semantic model, you wanna take control of your date table.

**0:58** · And you can see how I have this full date column in my model.

**1:01** · If I check it, you'll see I have all of these different values, year, quarter, month, day.

**1:07** · And if I go to booking date, you can see I have another one.

**1:10** · If I go to guest satisfaction, I have another date.

**1:14** · And for every one of those, if I connect to DAX Studio, and it's creating these hidden two, three, four, five date tables for me.

**1:22** · So how do you get rid of these?

**1:24** · Well, there's a couple of things you can do.

**1:25** · So if you go over to your model, the first thing you can do is create a date table, establish relationships, so you can use that central date table.

**1:32** · That's a topic for another day.

**1:34** · And if I right-click right here, I can go to calendar options, say, mark as date table, turn it on, choose my full date.

**1:42** · And remember we had five before.

**1:43** · I'm gonna click Save.

**1:44** · You see how that went away right there.

**1:46** · See how this is a date now.

**1:47** · And if I go back to DAX Studio, you can see I'm down to four, one, two, three, four.

**1:51** · How do I get rid of the other ones?

**1:53** · Let's go back to Power BI Desktop.

**1:54** · You can do a couple of things.

**1:55** · You can go File, Option Settings and Options, and there's two locations.

**1:59** · There's in the global and the current file, you can do data load and data load.

**2:03** · So on data load, I can turn off auto date time in the global.

**2:06** · That means for every subsequent Power BI Desktop file that I open, it's not gonna create those hidden date tables for you.

**2:12** · And if I do it right here, it's going to turn it off just for this local file, this current file.

**2:18** · So I'm gonna uncheck it, click OK.

**2:20** · And then if I go back here, they're all gone.

**2:22** · Now, I'm gonna turn it back on.

**2:24** · You can see all my date tables are there.

**2:25** · And so if I go here, right now, my relationship to my date table is on keys, integer values.

**2:31** · But if I switch them up, because I actually have dates, so if I switch this to stay date, and I switch this to full date, which is my actual date, I click Apply, and we go back to DAX Studio, you'll see I'm down to three.

**2:43** · And as I continue to iterate through this, it'll get rid of all those date tables.

**2:47** · One warning, if you already use one of these automatic date hierarchies in a visual, turning this off can break that visual.

**2:55** · So don't just flip-flop and switch and hope for the best, right?

**2:58** · Check it out, test, validate.

**3:00** · And this is good hygiene.

**3:01** · It helps to reduce clutter.

**3:02** · It gives you one- Consistent date table, and it puts you in control of the intelligence.

**3:06** · Let's see what's next.

### Tip 10: Replace Nested IFs with SWITCH TRUE in DAX

**3:08** · Replacing those deeply nested if statements with SWITCH and TRUE.

**3:13** · I have a table here with property name, and so I have two measures.

**3:16** · One, that's an IF.

**3:18** · It's pretty straightforward.

**3:19** · If it's not in scope, if it's not at the property level, show portfolio total.

**3:23** · But if I'm in the context of the property, if total revenue is greater than thirty-five million, exceptional.

**3:28** · Twenty-five million, strong.

**3:30** · Greater than or equal to fifteen million, moderate.

**3:32** · Otherwise, display low.

**3:33** · I'm gonna add this to the table, and you'll see it's actually telling me something.

**3:37** · I have some properties that are strong, moderate, low, exceptional, and you can see that if I'm not in the scope, it shows portfolio total, and this works.

**3:44** · But imagine every time I add another IF, I get deeper and deeper in the IF.

**3:50** · So I'm gonna replace this with a SWITCH.

**3:53** · So much easier to write and so much easier to understand.

**3:56** · Here's my SWITCH.

**3:57** · Here's my TRUE.

**3:58** · And so if it's not in scope, show portfolio total.

**4:00** · Otherwise, follow the same rules, and if none of these conditions meet, show low, right?

**4:05** · So I'm gonna add this, and it does the exact same thing.

**4:08** · There's one important detail here.

**4:11** · The order matters.

**4:13** · SWITCH stops at the first condition that evaluates to TRUE, so I need to start with the highest threshold and work my way down.

**4:21** · So let's say in my SWITCH statement I said, "If total revenue is greater than fifteen million," a property with forty million would satisfy that condition, and Power BI would return moderate.

**4:29** · This one may not seem bananas, but once conditional logic starts growing and growing and growing, SWITCH TRUE makes the intent a whole lot easier to see No DAX.

### Tip 9: Avoid Unnecessary DAX by Calculating Upstream

**4:43** · DAX should not be the first answer to every problem you encounter.

**4:47** · So take a look at my total revenue column.

**4:50** · This works, but the business rule itself is absolutely static.

**4:55** · The revenue is room revenue plus experience revenue, plus other revenue, minus discount amount.

**5:01** · That row-level calculation does not need filter context.

**5:04** · So I can create net revenue upstream in SQL, Power Query, or the warehouse.

**5:09** · So if I go over to my SQL Server, you can see I've created a computed column that does the exact same logic.

**5:16** · Room revenue, experience revenue, other revenue, minus discount amount.

**5:20** · And then if I go to Power Query, I can go to Booking, and I can go find those columns.

**5:24** · Room revenue, this, and this, and I can do some maths and say sum these two, then I can subtract that one from it, and I get the exact same result.

**5:33** · Regardless of the approach I take, then I can do a new measure, so instead of writing that DAX, I can say total, and I know I already have one, equals SUM net revenue.

**5:43** · That's all I need to write.

**5:44** · Measures, ratios, calculations that depend on filter context, they belong in DAX.

**5:50** · Cleanup, static classification, and repeatable row-level business rules often belong upstream.

**5:57** · I think it's Roach's maxim or Maxim's Roachum, something like that.

**6:00** · That distinction absolutely matters Use Power Query parameters to move between development, tests, and production.

### Tip 8: Use Power Query Parameters for Environment Switching

**6:08** · Let's go over into Power Query.

**6:10** · So we're gonna choose Transform.

**6:11** · And the first thing we're gonna do is create a couple of parameters.

**6:13** · We're gonna say Manage Parameters, and we're gonna do New, and we're gonna say Server Name.

**6:18** · We're gonna add another one called Database Name.

**6:20** · And I already have 'em, so the database name is Northstar Public, and then the server name, we're gonna go over to Management Studio, not 'cause I'm lazy, I'm just efficient.

**6:32** · And I'm gonna copy this, okay?

**6:33** · And then we're gonna go back over here, and we're gonna paste this in.

**6:36** · And one thing I like to do is really type cast.

**6:39** · So I'm gonna say this is text, and this is text.

**6:42** · And what I'm gonna do is say OK.

**6:44** · And then I'm gonna go to View, and we have to allow parameters, so you need to check that box.

**6:50** · And then we'll go back here.

**6:51** · We're gonna go to Data Source Settings, and we're gonna change this source.

**6:55** · And so instead of hard-coded values, we're gonna use Parameter, Server Name, Parameter, Database Name.

**7:01** · Click OK.

**7:02** · Click Close.

**7:03** · It'll take a little bit.

**7:04** · There we go.

**7:05** · If we go into the advanced editor, what you'll see is server and database name.

**7:09** · Changes it everywhere.

**7:10** · You can go into each one, and if you take a look at the first step in the code, you'll notice that it's server and database name.

**7:16** · Now, the query is not tied to one environment.

**7:19** · When I need to move from development to test or production, I change parameter value instead of rewriting the entire query.

**7:26** · This is not something that every report needs, but once you are working across multiple environments, hard-coded connection information gets old really fast.

### Tip 7: Use Test Mode Parameters to Limit Rows During Development

**7:35** · When I'm developing my Power BI semantic models, I don't want every row from a very large table.

**7:41** · I may only need enough to build a transformation, validate the model, and make sure everything works.

**7:47** · So what I do is I'm gonna create a couple of parameters.

**7:50** · I'm gonna create one called Test Mode, and I make it true/false, and I'm gonna set it to false.

**7:55** · And then I create another one called Test Row Count, and then I'm gonna make this one a decimal.

**8:01** · And what I'm gonna do is set it to 10, and click OK.

**8:03** · And then what I'm gonna do is I'm gonna create a new blank query.

**8:06** · And inside that blank query, all I'm gonna do is paste the query that I've created.

**8:11** · And what you'll see, I'm using my server parameters.

**8:13** · I'm doing a little M here.

**8:15** · I say, "If it's test rows, only show the first however many rows I put in," in my case, 10.

**8:20** · So if it's true, only show 10 rows.

**8:23** · Otherwise, return the entire table.

**8:25** · So you can see it's returning lots of data right now.

**8:27** · So what I'm gonna do, I'm gonna switch this from false to true, and watch what's gonna happen.

**8:33** · It only returned 10 rows.

**8:34** · If I go here and switch this, it's only gonna return 20 rows.

**8:38** · Now I can work against a smaller data set while I'm developing, then turn Test Mode off before the full refresh.

**8:45** · There is one important nuance.

**8:47** · You need to pay attention to query folding and where the row reduction actually happens.

**8:51** · If Power Query pulls the entire data set across the network and only then keeps 20 rows or 10 rows, you didn't really save much.

**9:00** · The goal is to push that reduction back to the source whenever the connector and transformation supports it.

**9:06** · This is a small pattern, but on a large data set, it can save a lot of time waiting Coming in at number six, the measure table.

### Tip 6: Create a Dedicated Measure Table for Organization

**9:15** · So in this model, I have measures spread across two tables.

**9:17** · I have them on the guest satisfaction table, and I have them on my booking table.

**9:22** · So let's go back here.

**9:24** · Let's go to modeling, and we're gonna do a new table, and I'm gonna call this measures equal data table, and I'm gonna say place folder.

**9:34** · I'm gonna make it an integer.

**9:35** · And then inside of there, I'm gonna do one, one.

**9:39** · I messed up right here.

**9:41** · Integer, comma.

**9:42** · So this creates my table.

**9:43** · Now, I can go to my model view, and I can start moving my measures.

**9:47** · And so I can go here, and I can say change this to measure.

**9:51** · I hide this column.

**9:52** · Easy.

**9:53** · There we go.

**9:53** · And now I can move all my measures to this table.

**9:56** · Nothing was wrong with having all my measures spread across the table.

**9:59** · Now they're all in one location.

**10:01** · If you start getting too many measures in a table, you can use display folders for revenue, for occupancy, for different things.

**10:07** · Some developers also prefer keeping measures within the related fact table, and that's a good thing.

**10:13** · This does not make the model faster, but a clean model is a whole lot easier to what?

**10:18** · Maintain.

**10:19** · We're getting to the good stuff.

### Tip 5: Bulk Edit Measure Properties in Model View

**10:20** · Bulk editing in the model view.

**10:23** · Look at this. I have several measures.

**10:24** · Room revenue, total revenue, total revenue previous year.

**10:28** · Now, I could choose room revenue, and I can go to format and then change it one at a time.

**10:32** · But I can also do multi-select, 'cause I know these are all currencies, and I can say currency and set my decimal place.

**10:40** · And now if I select them individually, you can see that the formatting is applied.

**10:44** · Now what I can also do… Check this out.

**10:46** · I'll go here and say select all measures.

**10:49** · Right?

**10:50** · All my measures are selected, and I'm gonna go to general, and I'm gonna move all of them to my measure table.

**10:55** · You can use this for other compatible properties beyond formatting, like display folders, summarizations, and other metadata.

**11:01** · This can save a ridiculous number of clicks.

### Tip 4: Reuse Semantic Model Logic with TMDL Calculation Groups

**11:04** · Coming in at number four is the ability to use TMDL to stop rebuilding the same semantic model logic over and over again.

**11:12** · Take a look at this.

**11:13** · Here's my model.

**11:14** · And I have measures like ADR, total revenue, and RevPAR.

**11:18** · And you can see I've already started building in some time intelligence.

**11:22** · And you'll have to repeat building that logic over and over and over again.

**11:26** · But take a look at this.

**11:27** · Let me go over to my TMDL view, and I'm gonna paste in some code.

**11:30** · And so you can see that I'm creating a calculation group.

**11:33** · One thing you gotta do before you do this is you need to go over to the model view, and you need to discourage implicit measures.

**11:39** · So we're gonna discourage implicit measures.

**11:41** · Now you c- you have this chunk of code.

**11:43** · Now watch this when I apply this, and I need to refresh so my calculation group gets all the information.

**11:48** · So now, instead of doing this over and over again, watch, I'll get rid of this.

**11:53** · I'll add my calculation group to the column.

**11:56** · That's okay.

**11:57** · No fret.

**11:57** · And then look.

**11:58** · I have all the changes automatically built in.

**12:01** · Think about it.

**12:02** · I don't have to write that code over and over again.

**12:04** · If I get rid of this and say, "Look, let's just use this for bookings," it automatically works for bookings or any other measure in my model.

**12:10** · You still need to check the table names- Column references, dependencies, and formats before applying anything.

**12:15** · But the next model doesn't have to start from zero.

**12:18** · You can keep reusing the Temdo starter blocks for the model objects you create over, and over, and over again.

**12:24** · Review them, share them, and apply them where they make sense.

### Tip 3: Use Control G Shortcut to Quickly Navigate Columns in Power Query

**12:28** · All right.

**12:28** · Some of you may laugh at number three, and that's Control G in Power Query.

**12:33** · Hear me out.

**12:34** · So go to Transform, and let's say you have this very large table, like Booking right here, and you can see there's lots of columns in Booking, and I can go search for whatever column I'm trying to get to, but guess what?

**12:46** · How many of you have done this?

**12:47** · Control G. There's the columns.

**12:48** · I wanna go to Stay Date.

**12:50** · I click Okay.

**12:50** · It automatically brings me that, to that column.

**12:53** · Control G, I wanna go to Guest Key.

**12:55** · It auto-magically brings me to that column.

**12:58** · I wanna find a column buried somewhere in the middle.

**13:00** · I could keep scrolling until I eventually find it, or I can just press Control G and there it goes.

**13:05** · Coming in at number two is field parameters.

### Tip 2: Use Field Parameters for Dynamic User-Controlled Visuals

**13:08** · Field parameters let the person using the report dynamically change which dimensions or measures appear in a visual.

**13:15** · Check this out.

**13:16** · I have a clustered bar chart, and you can see I have total revenue by property name, but I want my users to switch this by region, property type, and booking channel.

**13:26** · I could build four visuals and try to fit them all on the page, or I can go to modeling.

**13:31** · I can choose new field parameter, and then what I can do is I will choose… Let me see.

**13:37** · Property name, booking channels.

**13:39** · Choose channel name.

**13:40** · Let's get one more in here.

**13:42** · Region.

**13:43** · Search for region.

**13:44** · Where's region at?

**13:45** · There we go, and I'm gonna choose region.

**13:48** · Click Create.

**13:48** · It's gonna add that as a slicer.

**13:50** · It's oh-so small.

**13:51** · We'll do a quick format of this.

**13:53** · And so what I'm gonna do is go here, and instead of using property name, I should have gave my parameter a better name.

**13:59** · I'm gonna drop it right there.

**14:01** · And now what I can do is choose property name, choose channel, choose region.

**14:05** · But it doesn't stop there.

**14:07** · I can also go back to modeling, and I can choose a new field parameter.

**14:11** · I'm gonna give this one a better name.

**14:13** · And then what I'm gonna do is go to my measure table, 'cause everything's in the right place.

**14:16** · Bookings, occupancy rate, total revenue, any of the measures I wanna add, right?

**14:22** · Click Create, and then instead of using total revenue, drop that right there, and now watch this.

**14:28** · The entire thing is completely dynamic.

**14:31** · Now, the user can change both the category and the calculation.

**14:36** · I'm gonna say it, this is insane amazing.

**14:39** · Drum roll, please.

### Tip 1: Use Control Shift L to Bulk Rename in DAX Editor

**14:41** · Coming in at number one, Control Shift L. Inside Temdo View are the DAX formula editor.

**14:48** · So if we go here and do a quick search, you can see I have a few measures that are prefixed with AVG, and I wanna rename them to Average.

**14:57** · So I just so happen to have a script on my clipboard of all three of them.

**15:01** · Watch this.

**15:02** · I'm gonna double-click here.

**15:03** · I'm gonna do Control Shift L. It highlights them all.

**15:07** · And it changes them all.

**15:08** · And then I say apply, and now if I look for average, all the abbreviations for all four measures went from AVG to average.

**15:18** · Bananas.

**15:19** · You do need to pay attention to the exact text you select.

**15:22** · If that text appears inside names you did not intend to change, Power BI is going to select those for you, so be careful.

### Conclusion and Final Thoughts

**15:30** · And there is definitely someone who thinks one of these should not have made the list at all, but based on practical value, surprise, and how often I would actually use each one, that's my order.

**15:42** · And as always, thanks for watching, and we'll see you in the queue.