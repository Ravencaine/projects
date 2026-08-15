---
uid: 2026-08-11-11-power-bi-tips-guy-in-a-cube
title: "Guy in a Cube - 11 Power BI Tips"
source: "https://www.youtube.com/watch?v=S6_HWtxywhg"
author: guy-in-a-cube
date: 2026-08-11
duration: 15:45
language: en
video_file: 99.System/Attachments/Video/11-Power-BI-Tips-Guy-in-a-Cube.mp4
tags: [video, power-bi, tips, guy-in-a-cube]
created: 2026-08-11
---
# Guy in a Cube - 11 Power BI Tips

![[11-Power-BI-Tips-Guy-in-a-Cube.mp4]]

## Transcript

[00:00:00.000] Yo, what is up everyone?
[00:00:03.160] Parvy eye people love to share tips.
[00:00:06.799] Some of them are genuinely useful.
[00:00:09.400] Some of them pretty clever.
[00:00:11.279] Some solve problems though that shouldn't exist in the first place.
[00:00:15.400] And a few of them are absolutely bananas.
[00:00:19.679] So I pulled together, one, two, three, five, six, seven, eight, nine, ten, eleven Parvy
[00:00:23.320] eye tips that people swear by and I rate them from eleven all the way to number one.
[00:00:29.519] I'm looking at how useful they are, how surprised they are and whether I actually use them
[00:00:35.679] in a real Parvy eye project.
[00:00:37.439] You know what we like to do?
[00:00:38.439] Let's get into this.
[00:00:40.000] Coming in at number eleven, turn off auto date time when you add a date column to a Parvy
[00:00:45.600] eye model.
[00:00:46.600] Parvy eye automatically creates these hidden date tables behind the scenes.
[00:00:50.200] And for a quick report, that's fine.
[00:00:52.439] But once you start building a real semantic model, you want to take control of your date
[00:00:57.560] table.
[00:00:58.560] And you can see how I have this full date column in my model.
[00:01:02.079] If I check it, you'll see I have all of these different values year, quarter, month,
[00:01:07.120] day.
[00:01:08.120] And if I go to booking date, you can see I have another one.
[00:01:10.560] If I go to get satisfaction, I have another date.
[00:01:14.640] And for every one of those, if I connect to DAC studio and it's creating these hidden
[00:01:20.159] two, three, four, five date tables for me, so how do you get rid of these?
[00:01:24.239] Well, there's a couple of things you can do.
[00:01:25.959] So if you go over to your model, the first thing you can do is create a date table, establish
[00:01:30.519] your relationship so you can use that central date table.
[00:01:32.840] That's a topic for another day.
[00:01:34.439] And if I right click right here, I can go to calendar options, say, market date table, turn
[00:01:40.280] it on, choose my full date, remember, we have five before I'm going to click save.
[00:01:44.760] You see how that went away right there?
[00:01:46.680] See how this is a date now.
[00:01:47.680] And if I go back to DAC studio, you can see, I'm down to four, one, two, three, four.
[00:01:51.920] How do I get rid of the other ones?
[00:01:53.319] Let's go back to part of your desktop.
[00:01:54.840] You can do a couple of things.
[00:01:56.120] You can go file options settings and options.
[00:01:58.920] And there's two locations.
[00:01:59.920] There's in the global and the current file, you can do data low and data low.
[00:02:03.480] So on data low, I can turn off auto date time in the global.
[00:02:06.959] That means for every subsequent part of your desktop file that I open, it's not going
[00:02:10.599] to create those hidden date tables for you.
[00:02:12.960] And if I do it right here, it's going to turn it off just for this local file.
[00:02:17.560] It's current file.
[00:02:18.560] So I'm going to uncheck it, click OK.
[00:02:20.560] And then if I go back here, they're all gone.
[00:02:22.680] Now, I'm going to turn it back on.
[00:02:24.400] You can see all my date tables are there.
[00:02:26.159] And so if I go here, right now, my relationship to my date table is on keys, integer values.
[00:02:32.000] But if I switch them up, because I actually have the dates, so if I switch this to stay
[00:02:36.280] date and I switch this to full date, which is my actual date, I click apply, and we go
[00:02:41.360] back to DAC studio, you'll see I'm down to three.
[00:02:43.639] And as I continue to iterate through this, it'll get rid of all those date tables.
[00:02:47.520] One warning, if you already use one of these automatic date hierarchies in a visual, turning
[00:02:53.360] this off, can break that visual.
[00:02:55.479] So don't just flip fly and switch and hope for the best, right?
[00:02:58.719] Check it out test validate.
[00:03:00.240] And this is good hygiene.
[00:03:01.319] It helps to reduce clutter.
[00:03:02.560] It gives you one consistent date table, and it puts you in control of the intelligence.
[00:03:07.000] Let's see what's next.
[00:03:08.560] Replace in those deeply nested if statements with switch in truth.
[00:03:13.800] I have a table here with property name.
[00:03:15.800] And so I have two measures.
[00:03:17.080] Then that's an if.
[00:03:18.080] It's pretty straightforward.
[00:03:19.520] If it's not in scope, if it's not at the property level, show portfolio total.
[00:03:24.240] But if I'm in the context of the property, if total revenue is greater than 35 million
[00:03:28.120] exceptional, 25 million strong, greater than the equal to 15 million moderate, otherwise
[00:03:32.719] displayed low.
[00:03:33.719] I'm going to add this to the table and you'll see, it's actually telling me something.
[00:03:37.240] I have some properties that are strong, moderate, low, exceptional, and you can see that if
[00:03:41.599] I'm not in the scope, it shows portfolio total.
[00:03:44.039] And this works.
[00:03:45.039] But imagine every time I add another if I get deeper and deeper in the if.
[00:03:51.120] So I'm going to replace this with the switch.
[00:03:53.840] So much easier to write, so much easier to understand.
[00:03:56.599] Here's my switch, here's my true.
[00:03:58.240] And so if it's not in scope, show portfolio total.
[00:04:00.800] Otherwise, follow the same rules.
[00:04:02.840] And if none of these conditions meet, show low.
[00:04:05.080] Right.
[00:04:06.080] So I'm going to add this and it does the exact same thing.
[00:04:08.919] There's one important detail here.
[00:04:11.520] The order matters.
[00:04:13.840] Switch stops at the first condition that evaluates the truth.
[00:04:17.759] So I need to start with the highest threshold and work my way down.
[00:04:21.279] So let's say my switch statement, I said, if total revenue was greater than 15 million,
[00:04:25.120] a property with 40 million would satisfy that condition.
[00:04:27.959] And parvy, I would return moderate.
[00:04:29.720] This one may not seem bananas, but once conditional logic starts growing and growing and growing,
[00:04:36.279] switch true makes the intent a whole lot easier to see.
[00:04:40.959] No DAX.
[00:04:41.959] DAX should not be the first answer to every problem you encounter.
[00:04:47.959] So take a look at my total revenue column.
[00:04:51.199] This works, but the business rule itself is absolutely static.
[00:04:55.759] The revenue is room revenue plus experience revenue plus other revenue minus discount amount.
[00:05:01.839] That role level calculation does not need filter context.
[00:05:05.000] So I can create that revenue upstream and sequel, power query on the warehouse.
[00:05:09.399] So if I go over to my sequel server, you can see I've created a computer column that
[00:05:14.959] does the exact same logic.
[00:05:16.720] Room revenue, experience revenue, other revenue minus discount amount.
[00:05:20.240] And then if I go to power query, I can go to booking and I can go find those columns.
[00:05:25.040] Room revenue, this and this and I can do some math and say some needs to then I can subtract
[00:05:30.720] that from it.
[00:05:31.720] And I get the exact same result regardless of the approach I take and I can do a new measure.
[00:05:36.160] So instead of writing that DAX, I can say total and I know already have one equals some
[00:05:42.480] net revenue.
[00:05:43.480] That's all I need to write measures, ratios, calculations that the pin on filter context,
[00:05:48.720] they belong in DAX, clean up static classification and repeatable role level business rules often
[00:05:55.600] belong upstream.
[00:05:56.600] I think it's roaches, maximum of maximums, roach and something like that.
[00:06:01.079] That distinction absolutely matters.
[00:06:04.079] Use power query parameters to move between development, test and production.
[00:06:08.439] Let's go over into power query, so I need to transform in the first thing we're going
[00:06:12.519] to do is create a couple of parameters, we're going to say manage parameters and we're
[00:06:16.000] going to do new, we're going to say server name, we're going to have another one called
[00:06:19.959] database name and I already have them.
[00:06:22.800] So the database name is not star public and then the server name, we're going to go over
[00:06:29.079] to management studio, not because I'm lazy, I'm just efficient and I'm going to copy this,
[00:06:33.639] okay, and then we're going to go back over here and we're going to paste this in.
[00:06:36.800] And one thing I like to do is really type KS, so I'm going to say this is text and this
[00:06:41.560] is text and what I'm going to do is say, okay, and then I'm going to go to view and we
[00:06:47.279] have to allow parameters, so you need to check that box and then we'll go back here,
[00:06:52.000] we're going to go to data source settings and we're going to change this source.
[00:06:55.600] And so instead of hard code of values, we're going to use parameter, server name, parameter
[00:07:00.480] database name.
[00:07:01.959] Like, okay, click close, it'll take a little bit, there we go, if we go into the advanced
[00:07:07.079] editor, what you'll see is server and database name changes it everywhere, you can go into
[00:07:11.160] each one.
[00:07:12.160] And if you take a look at the first step in the code, you'll notice that it's server and
[00:07:15.560] database name.
[00:07:16.560] Now, the query is not tied to one environment, but I need to move from development to test
[00:07:22.160] our production.
[00:07:23.160] I change the parameter value instead of rewrite in the entire query.
[00:07:26.360] This is not something that every report needs, but once you are working across multiple
[00:07:30.920] environments, hard code of connection information gets all really fast.
[00:07:35.480] When I'm developing my party eyes, manic models, I don't want every row from a very large
[00:07:41.079] table.
[00:07:42.079] I may only need enough to build a transformation, validate the model and make sure everything
[00:07:46.759] works.
[00:07:47.759] So what I do is I'm going to create a couple of parameters, I'm going to create one
[00:07:50.980] called test mode, and I make it true false, and I'm going to set it to false.
[00:07:56.079] And then I create another one called test row count.
[00:07:59.120] And then I'm going to make this one a decimal, and what I'm going to do is set it to 10.
[00:08:03.079] And click OK.
[00:08:04.079] And then what I'm going to do is I'm going to create a new blank query.
[00:08:06.879] And inside that blank query, all I'm going to do is paste the query that I've created.
[00:08:11.920] What you see, I'm using my server parameters, I'm doing a little M here, I said, if it's
[00:08:15.980] test rows, only show the first part of many rows I put in, in my case, 10.
[00:08:20.920] So if it's true, only show 10 rows, otherwise, return the entire table.
[00:08:25.600] So you can see it's returning lots of data right now.
[00:08:28.000] So what I'm going to do, I'm going to switch this from false to true, and watch what's
[00:08:32.559] going to happen.
[00:08:33.559] It only returned 10 rows.
[00:08:34.559] If I go here and switch this, it's only going to return 20 rows.
[00:08:39.000] Now I can work against a smaller data set while I'm developing, then turn test mode off
[00:08:44.000] before the full refresh.
[00:08:45.480] There is one important nuance.
[00:08:47.159] You need to pay attention to query folding and where the row reduction actually happens.
[00:08:51.399] If PowerPoint pulls the entire data set across the network, and only then keeps 20 rows
[00:08:58.000] or 10 rows, you didn't really save much.
[00:09:00.519] The goal is to push that reduction back to the source whenever the connector and transformation
[00:09:05.600] supports it.
[00:09:06.600] This is a small pattern.
[00:09:07.600] But on a large data set, it can save a lot of time waiting, coming in at number 6,
[00:09:13.919] the measure table.
[00:09:14.919] So in this model, I have measures spread across two tables.
[00:09:17.519] I have them on the guest satisfaction table, and I have them on my book and table.
[00:09:22.639] So let's go back here, let's go to modeling, and we're going to do a new table, and I'm
[00:09:27.440] going to call this measures equal data table.
[00:09:30.639] I'm going to say place older, make it an integer, and then inside of there, I'm going
[00:09:38.440] to do one, one messed up right here, integer comma.
[00:09:42.360] So this creates my table.
[00:09:43.879] Now, I'm going to go to my model view, and I can start moving my measures.
[00:09:47.879] And so I can go here, and I can say change this to measure, I hide this column, easy.
[00:09:53.120] There we go.
[00:09:54.120] And now I can move all my measures to this table.
[00:09:56.919] Nothing was wrong with having all my measures spread across the table.
[00:09:59.799] Now there are only one location, and if you start getting too many measures in a table,
[00:10:03.480] you can use display folders for revenue, for icons, and see for different things, some
[00:10:07.840] developers also prefer keeping measures within the related fact table.
[00:10:12.399] And that's a good thing.
[00:10:13.399] This does not make the model faster, but a clean model is a whole lot easier to what
[00:10:18.679] maintain.
[00:10:19.679] Getting to the good stuff, bulk editing in the model view.
[00:10:22.879] Look at this.
[00:10:23.879] I have several measures, room revenue, total revenue, total revenue, previous year.
[00:10:28.720] Now I can choose room revenue, and I can go to format, and then change it one at a time.
[00:10:32.759] But I can also do multi select, because I know these are all currencies, and I can say
[00:10:37.840] currency, and set my decimal place, and now if I select them individually, you can see
[00:10:42.840] that the formatting is applied, and now I can also do.
[00:10:45.919] Check this out.
[00:10:46.919] I'll go here and say select all measures.
[00:10:50.440] All my measures are selected, and I'm going to go to general, and I'm going to move all
[00:10:54.120] of them to my measure table.
[00:10:55.759] You can use this for other compatible properties beyond format, and display folders, summarizations,
[00:11:00.679] and other metadata.
[00:11:01.919] This can save a ridiculous number of clicks.
[00:11:05.159] Coming in at number four, it's the ability to use TimDil to stop rebuilding the same
[00:11:10.019] semantic model logic over and over again.
[00:11:12.860] Take a look at this.
[00:11:13.860] Here's my model.
[00:11:14.860] I have measures like ADR, total revenue, and RFPAR, and you can see I've already started
[00:11:20.179] building in some time intelligence, and you'll have to repeat building that logic over
[00:11:25.299] and over and over again.
[00:11:26.740] But take a look at this.
[00:11:27.740] Let me go over to my TimDil view, and I'm going to paste in some code.
[00:11:31.259] You can see I'm creating a calculation group.
[00:11:33.860] One thing you've got to do before you do this, you need to go over to the model view, and
[00:11:38.299] you need to discourage implicit measures.
[00:11:40.139] We're going to discourage implicit measures.
[00:11:42.419] You have this chunk of code.
[00:11:43.740] Now watch this when I apply this, and I need to refresh so my calculation group gets all
[00:11:48.179] the information.
[00:11:49.179] Now instead of doing this over and over again, watch, I'll get rid of this, add my calculation
[00:11:55.019] group to the column.
[00:11:56.659] That's okay.
[00:11:57.659] No fret.
[00:11:58.659] Then look.
[00:11:59.659] I have all the changes automatically built in.
[00:12:01.779] Think about it.
[00:12:02.779] I don't have to write that code over and over again if I get rid of this and say, look, let's
[00:12:05.779] just use this for bookings, it automatically works for bookings, or any other measure in
[00:12:09.659] my model.
[00:12:10.659] You still need to check the table names, column references, dependencies, and formats before
[00:12:14.700] applying anything, but the next model doesn't have to start from zero.
[00:12:18.379] You can keep reusing the TimDil start-of-blocks for the model objects you create over and over
[00:12:24.179] and over again.
[00:12:25.179] Review them, share them, and apply them where they make sense.
[00:12:28.379] All right.
[00:12:29.379] So when you may laugh at number three, and that's Control G in Power Query, hear me out.
[00:12:34.259] So go to Transform, and let's say you have this very large table like booking right here.
[00:12:40.620] And you can see there's lots of columns in booking, and I can go search for whatever column
[00:12:44.539] I'm trying to get to, but guess what?
[00:12:46.179] How many of you have done this?
[00:12:47.259] Control G.
[00:12:48.259] There's the columns.
[00:12:49.259] I want to go to stay date.
[00:12:50.259] I click OK.
[00:12:51.259] It automatically brings me that to that column.
[00:12:53.740] Control G.
[00:12:54.740] I want to go to Guest Key.
[00:12:55.740] It automatically brings me to that column.
[00:12:58.139] I want to find a column buried somewhere in the middle.
[00:13:00.659] I can keep scrolling until I eventually find it.
[00:13:03.460] I can just press Control G and there it goes up.
[00:13:06.100] Coming in at number two is Field Parameters.
[00:13:08.259] Field Parameters let the person using the report dynamically change, which dimensions are
[00:13:12.860] measures appear in a visual.
[00:13:15.620] Check this out.
[00:13:16.620] I have a Clustered Bar chart, and you can see I have Total Revenue by Property Name.
[00:13:21.100] But I want my users to switch this by Region, Property, Type, and Booking Channel.
[00:13:26.460] I could deal for visuals and try to fit them all on the page or I can go to Modeling.
[00:13:31.419] I can choose New Field Parameter, and then what I can do is I will choose, let me see,
[00:13:37.259] Property Name, Booking Channels, Choose Channel Name, let's get one more in here, Region.
[00:13:43.460] Search for Region, where's Region at?
[00:13:45.860] There we go.
[00:13:46.860] And I'm going to choose Region.
[00:13:48.220] Click Create.
[00:13:49.220] It's going to add that as a slicer.
[00:13:50.220] It's also small.
[00:13:51.220] We'll do a quick format of this, and so what I'm going to do is go here and it's
[00:13:56.419] instead of using Property Name, I should have gave my parameter a better name.
[00:13:59.620] I'm going to drop it right there, and now what I can do is choose Property Name, Choose
[00:14:03.899] Channel, choose Region, but it doesn't stop there.
[00:14:07.259] I can also go back to Modeling, and I can choose a New Field Parameter, I'm going to give
[00:14:11.740] this in the better name, and then what I'm going to do is go to my Measure Table because
[00:14:15.460] everything is in the right place, bookings, occupancy rate, Total Revenue, any of the measures
[00:14:21.379] I want to add.
[00:14:22.379] I click Create, and then instead of using Total Revenue, drop that right there, and then
[00:14:27.460] watch this.
[00:14:28.460] The entire thing is completely dynamic.
[00:14:31.460] Now, the user can change both the category and the calculation.
[00:14:36.460] I'm going to say it, this is insane, amazing.
[00:14:39.460] Drum roll, please.
[00:14:40.460] Do-do-do-do-do-do-do.
[00:14:41.460] Coming in at number one, Control, Shift, Al.
[00:14:45.299] Inside, Timkelview, or the DAX formulaeditat.
[00:14:48.659] So if we go here and do a quick search, you can see I have a few minutes.
[00:14:52.340] I have a few measures that are prefixed with AVG, and I want to rename them to Average.
[00:14:57.379] So I just so happen to have a script on my clipboard of all three of them.
[00:15:01.259] Watch this.
[00:15:02.259] I'm going to double click here.
[00:15:03.259] I'm going to do Control, Shift, Al.
[00:15:05.259] It highlights them all, and it changes them all, and then I say Apply, and then if I look
[00:15:11.179] for Average, all the abbreviations for all four measures went from AVG to Average, so
[00:15:18.019] bananas.
[00:15:19.340] You do need to pay attention to the exact text you select.
[00:15:22.700] If that text appears inside names, you did not intend to change.
[00:15:27.179] Power BI is going to select those for you.
[00:15:29.460] So be careful.
[00:15:30.460] And there is definitely someone who thinks one of these should not have made the list
[00:15:35.100] at all.
[00:15:36.100] But based on practical value, surprise, and how often I would actually use each one, that's
[00:15:41.899] my order.
[00:15:42.899] And as always, thanks for watching, and we'll see you in the cube.