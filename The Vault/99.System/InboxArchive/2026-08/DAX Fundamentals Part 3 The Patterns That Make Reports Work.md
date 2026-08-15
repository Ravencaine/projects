---
title: "DAX Fundamentals Part 3: The Patterns That Make Reports Work"
source: "https://www.youtube.com/watch?v=_McUlXEyWyg&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=_McUlXEyWyg&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Havens Consulting]]"
published: 2026-06-30
created: 2026-08-08
description: "You've learned how filter context and CALCULATE actually work. This is where it pays off. Part 3 of the DAX Fundamentals series covers the patterns you'll keep reaching for in real models, and why the"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=_McUlXEyWyg)

You've learned how filter context and CALCULATE actually work. This is where it pays off. Part 3 of the DAX Fundamentals series covers the patterns you'll keep reaching for in real models, and why they behave the way they do.  
  
We get into time intelligence (YTD, QTD, prior cycle, and why these functions return tables of dates rather than numbers), variables for cleaner and faster formulas, and SWITCH as the cure for nested IF chains nobody wants to maintain. Then inactive relationships and USERELATIONSHIP for when one fact table has two date columns fighting over the same date table.  
  
The pattern that saves the most pain is calculation groups. Write three base measures, add one calc group with YTD, Prior Cycle, and YoY%, and you've replaced nine measures (and growing) with something you maintain in one place.  
  
The video closes on the part most people skip: how the engine splits work between the Storage Engine and the Formula Engine, and why pushing work toward simple aggregations on a star schema is the difference between fast DAX and slow DAX.  
  
RELATED CONTENT 🔗  
DAX Patterns Guide (Series Part 3) -- https://go-ae.org/hc-yt-dax-guide-part-3  
  
BECOME A CHANNEL MEMBER 🎉  
\-- https://www.youtube.com/channel/UCjlfQwqb-0S40XQ8seYPLSw/join  
  
CHECK OUT OUR MERCH STORE 👕  
\-- https://havens-consulting.creator-spring.com/  
  
LET'S CONNECT! 🧑🏽‍🤝‍🧑🏽 🌟  
\-- https://www.linkedin.com/in/reidhavens  
\-- https://www.youtube.com/c/HavensConsulting  
  
BUSINESS PAGES 📄  
Home Page - http://www.havensconsulting.net/?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=\_McUlXEyWyg  
Blog -- http://www.havensconsulting.net/blog-and-media?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=\_McUlXEyWyg  
Blog Files -- http://www.havensconsulting.net/blog-files?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=\_McUlXEyWyg  
Files & Templates -- http://www.havensconsulting.net/files-and-templates?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=\_McUlXEyWyg  
Consulting Services -- http://www.havensconsulting.net/consulting-services?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=\_McUlXEyWyg  
Online Courses -- https://www.havensconsulting.net/online-courses?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=\_McUlXEyWyg  
Contact & Support - http://www.havensconsulting.net/contact-and-support?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=\_McUlXEyWyg  
Analytic Endeavors-- https://go.analyticendeavors.com/39dda7c7fe  
  
EMAIL US AT 📧  
info@havensconsulting.net  
  
#PowerBI #DAX #MicrosoftFabric #DataModeling #BusinessIntelligence

## Transcript

**0:00** · Hey data fans, Reed here. Today I'm here to close out the part three of my DAX foundation series where I was walking through the DAX fundamentals, some of the DAX functions, and now I'm going to go into a few of the DAX patterns as well. The goal of this was to be introductory to intermediate. So nothing too advanced, but collectively all of this will, I think, cover a lot of the basics and leverage a lot of the design methodologies that I wanted to do with providing uh a number of interactive guides and visual aids for this.

**0:28** · So with that being said, let's hop into PowerBI and get started.

**0:42** · So the focus of this one is going to be part three which will be DAX patterns focusing on time intelligence variables and other patterns beyond that. The powerful patterns that can help turn DAX knowledge into real world solutions. All right, getting started. I want to talk about building on context and what we've learned so far is a recap if you're joining in from some of the previous guides or videos that I've done on this.

**1:06** · So we built the foundation. And now it's time to put it to work. This one in this guide particular is going to focus on four things primarily. So time intelligence, variables, relationships, and also calculation groups. Let's go ahead and start with time intelligence.

**1:21** · So comparing data across time periods, one of the most common reporting needs.

**1:26** · DAX has a series of dedicated functions for you to do this so you don't have to do your own date math. But first though, there is a prerequisite for this stuff.

**1:33** · You do need a proper date table. Time intelligence functions need a table with contiguous dates which means that there is one row per date no gaps. Mark is a date table in your model and this will return a series of dates. I will also say you could either make it in power query. You could make it um using tools like Bravo. You can uh leverage it with DAX and copy it around with TimW. You can get it from a SQL database.

**1:57** · However you get it, you do need some type of a dim date, dim calendar or however you choose to name it. that a dedicated calendar table is uh necessary and required to be able to do time intelligence effectively and without error. Now moving on a little bit, I want to talk about some function references. There are a whole library of functions that are available for time intelligence and for DAX. I will cover just a few of them as some examples and a couple of patterns that I think are important to know. Now, each one of these is explorable and interactive.

**2:27** · If you expand this, scroll down a little bit, you can see some of the function references that we have, which will give you the patterns and a little bit of information and some examples about those as well. Same with any of the ones down below here. Now, the first three that we've seen up here, dates, year-to- date, quarter to date, and monthto date are all the same pattern except of how they reset. They reset at the year, the quarter, or the date.

**2:52** · Whereas date add will actually let you be able to travel forward or backwards in time and it shifts the entire date by a series of specified intervals. Now coming down into here, I like to build examples to allow you to explore and see how patterns work. So I have an interactive star date calendar here. And if I was to select date as an example, you can see over on the right side where numbers are starting to show up. Now month, quarter, and year to date are all going to be the same because we haven't reset any intervals yet.

**3:22** · If I come to February, we've now reset the month-to- date interval. If I come to March, still going to be the same thing. But now, if I go to April of 2226, I've reset the month and the quarter because both of them are brand new, but the year to date is still going. So, it helps to show you also by color coding it which things are being reset or not as I move around with some of these. So, hopefully that gives you a bit of an understanding of where those cumulative periods grow into the value. and then also reset.

**3:51** · Moving on to the next section as well, past time intelligence. And again, the goal of that one was to mention some of the things that are done and also the necessary items for it, which is again a date table. But now I want to talk about logic patterns, specifically going into switch and selected value and how to use these to make reports dynamic. So the switch is the equivalent of a better if chain. For people from SQL, that would be the equivalent of a case win. But previously, we would have if if and close close.

**4:21** · And if you've worked with this in Excel before, you're probably very familiar with how messy this can get, especially when it gets very nested. The switch cleans this up. It beautifies it and it lets use variables to clean this up. So, we can do a switch true where we can specify those and have a much cleaner pattern where it prints a lot better. And I will also say doing this declares it where as we've talked about in the previous uh section for guide part two that if we declare something it's only going to be called once.

**4:50** · So it's actually a performance increase as well to be able to reference it like this. So very important when you are ever calling revenue if it's going to be referenced multiple times with no filter modifications. Declaring it as a variable is going to be a performance improver on top of switch being just a better way to show the pattern from a visual perspective.

**5:11** · And order matters. So switch will like any if win or case statements will return the first match. So put restrictive conditions first and then storing in a variable means it gets evaluated once not multiple times. And a little bit of a note as well, field parameters do let users dynamically change which measure a column appears in a visual without any switch logic. So a lot of switch patterns and disconnected tables were replaced to a degree with field parameters. Not everything is, but there is a bit of overlap on when one versus another might be used.

**5:40** · So, field parameters are potentially an alternative solution in many cases for switch statements.

**5:49** · I also want to talk about selected value for slicer driven logic. So, selected value returns a value when a column is filtered to exactly one value. Multi select or no selection will return the fallback. So in this case as I'm selecting through these here you can see that if I make a single selection the output for something like a title is going to be producing that value.

**6:11** · Otherwise if you do select all it returns all cycles as mentioned down here with the concatenation between those. So these are what's being essentially returned depending on the selections. So common use cases are going to be for dynamic titles, what if parameters and or measure switching as you see over on the right.

**6:33** · Now moving on to the next topic, variables and DAXs. Write ones used many times cleaner code and better performance. And the biggest thing with variables I will say is going to be performance, readability, and debugability. Let's take a look at a canonical example where in the one that we have below us for revenue band we are declaring a variable for current revenue switching between those for three statuses of high medium low or no sales as the default fourth status and in this case it is switching that three different times declaring it once.

**7:04** · So it's not only performant it is also formatted in a way that is significantly more readable. So the variables capture the content at definition time when the variable is declared. So current revenue as we can see on the right is evaluated once and referenced in three switch conditions and without that it would be recalculated for each condition block and again why we use variables it's for performance it is for readability and it is for debugging.

**7:31** · The debugging part of it is you can swap out the result and the return for any of the variables in your switch list that you have um or better said any of the declared variables that you have in your formula.

**7:42** · So, it's easy to test those from a report perspective if you need to. I will mention a caveat that with DAX query view, the need for that has gone down from a visual perspective and some of the smoke testing and other stuff you can do with LLMs, but it's still nice to have if you ever need to swap out the values in a matrix table or a table to see what some of the variables are actually declaring. Just as an FYI. Uh, and last little mention here, if you use Tabular Editor 3, there is a DAX debugger that is a very useful tool.

**8:08** · The world premiere of it a couple years back was done on the YouTube channel that I have for Havens Consulting with Daniel who created Tabler Editor. So, a little brief nod to go check that out if you are curious on some supplemental content and I'll link down in the description below that video.

**8:28** · And also, I want to show you how to step through the evaluation so we can see what's going to happen when using a variable. So, we're going to click next to walk through how a DAX evaluates the measure. Step one, there is the current total revenue. The engine evaluates total revenue in the current filter context and stores the result in the current revenue variable. The resulting switch statement will begin evaluating conditions top to bottom. So this one is going to get skipped because it does not meet the condition of greater than 5 million. So this condition is false.

**8:59** · Switch moves to the next. Current revenue though is greater than one. So that gets a mid category which returns and evaluates to the final result of revenue band equals mid. So we've seen how to step through and observed the sequential steps in actions of how the engine logically walks through from declaration of variable to the end result. Next I want to talk about is relationships and one of my favorite functions which is use relationship.

**9:27** · So when you have multiple date columns and one active relationship to your calendar table, this is what comes into play to let you swap those around. So here's the setup for that. An example, we have a trades table with a trade date and a delivery date. So both connect to star date, but Parva only shows and allows for one active relationship at a time between between two tables. Otherwise, you'll end up with circular dependencies and ambiguous paths where it doesn't know which relationship to use if both are active. So active versus inactive.

**9:59** · We can actually leveraging a measure with use relationships or a calculation group. We can actually toggle between these. So right now there's a measure for trade delivery path. That one is calculating the bar on the left which is teal or that trade date value. Now we can also have a measure that would activate using the use relationship function or delivery date, the orange bar in there. Both can be in the same visual, but this allows us to get different results leveraging each of those paths where one inside of the measure is turned on at a time. And again, you can do this inside of a measure.

**10:30** · You can also do it as a calculation group. But this way, you can have a single calendar table, multiple paths, and choose the path you want to turn on generally with one on already by default. Now, moving on, I want to talk about calculation groups. And in this case, it's going to be a pattern where we can write time intelligence once and use it as many times as we need to. So think of calculation groups as a modifier that wraps around any measure that can be at the report level, the page level or the visual level.

**10:55** · So you write your base calculations once and then you can have a cal group that applies transformations like year to date, prior year, year-over-year, all these things that you can see here at the bottom. So without a cal group, you can end up with with a significant number of measures. And with cal groupoups over here on the right, you can have those base measures paired with some type of a cal group repeatable logic. Very useful. been around since SQL Server analysis days, but a cornerstone of PowerBI development.

**11:21** · I'll also recommend checking out the blog post in my guide section on field parameters versus calculation groups. It digs a bit further into those. I'm approaching this from the perspective of how the DAX logic works for them, less about how the output works from the report layer. Now digging into this a little bit and scrolling down. Selected measure is a great example of what can be used with a calculation group within this because that's a specific function that will apply this to any measure.

**11:51** · You're not applying a count group to a single measure name. You're applying it to the selected measure which is anything in the visual on the page or in the report. So taking a look a bit with seeing something in action where our base measure in this case is total revenue and we we have a filter on our page. We have a slicer.

**12:08** · We've created a cal group with a series of actions where often if you're going to have something with a reset, your base count group is going to have some name where there's no modification, but then we can modify it for something for year to date, prior cycle, yearover-year, where it's taking

**12:26** · your selected measure that you have and applying those modifiers with some way, usually if you want as a slicer selection to reset it back to default, which would just be actual or base or whatever name that you might decide to keep it for this But that's essentially the goal of a calculation group is repeatable logic centralized locations for that. I will have a UDF post followed up following up probably in a part four for my DAX pattern series at some point, but for now that's outside of the scope of the guide that I made for this one.

**12:53** · All right, for the next section, I want to talk a bit about the engines inside of DAX and what is under the hood. Specifically, how your DAX engine processes your queries in two stages. So every time a visual renders, DAX runs a two-stage process with two engines. And understanding each will help to determine performance, especially when you're using tools like DAX Studio. So we have a storage engine, a formula engine, and a result.

**13:16** · So the storage engine is going to be your inmemory vera pack engine, which is the model itself, which is colmer compressed and parallelized, meaning it can do multiple things at the same time. It's very fast at being able to like run queries. The formula engine is what evaluates your DAX expressions is the calculate the iterators variables. It's singlethreaded.

**13:40** · So it's basically the way I like to think about it is the storage engine is the retriever and constructor to a degree getting stuff out of your model. anything that is all not already in storage that needs to be like assembled ends up getting handled by the formula engine which can slow things down.

**14:01** · So as much as possible as many things that you can natively retrieve from your model without DAX having to do like looking up values or um smashing things together, the better the performance is going to be. So that's a thing to kind of think about is you you want the model shape to do as much work as possible. So your formulas are as simple as possible. A sum of a column, a calculate with a basic filter.

**14:27** · The more advanced the DAX often the slower it's going to get because it has to think more in real time essentially.

**14:35** · So fast versus slow patterns, storage engine friendly and fast. The things that are going to uh push more towards the storage engine are simple aggregations like sums, counts, mins or maxes. Having a star schema with those clean uh having a star schema with those clean foreign keys as I mentioned direct column references. Basic calculates with table filters. Things that will end up making the storage or things that will end up making the formula engine heavy or slower.

**15:03** · Complex iterators like sums with nested logic. nested calculates inside of other nested calculates, rowby row processing patterns, often any type of an X or iterator function. Um, and many to many relationships without bridge tables. Um, as a little bit of an anecdote around the Vertipek engine, relationships one to many or one to one have dictionaries, meaning it has a saved mapping rowby row of what relates to what. Many to many relationships don't actually have that.

**15:33** · They used to be referred to as weak relationships because that assembly of understanding the paths doesn't exist in any type of a cache or a dictionary or mapping. So it needs to be figured out in real time.

**15:46** · It's almost like a real time lookup happening with those. So that's why a lot of people avoid many to many relationships.

**15:53** · Now a performance rule of thumb push as much work to the storage engine as possible. Star schema plus simple aggregations will equal fast complex and flat tables is slow. So when in doubt, simplify the model and or push the logic into the model design and the shape with tables and relationships or columns rather than the DAX measure.

**16:13** · If I had to error on the side of a slightly bigger model with a few more tables, but the DAX is going to be faster and my compute cost when I'm using Fabric or PowerBI is less, that's still better at the end of the day. It's still going to be a cost saver. It's an art and a science between the two of them, but that's a general rule of thumb to try to think about. Now some key takeaways across all of the guides that I've done. So time intelligence returns tables.

**16:36** · So the date add function same period last year and friends similar to it will return date tables that calculate uses as filters not scalar values. So it basically puts inside of the calculate a filtered table to calculate the measure against your total sales year to date. There's a table inside of the calculate filter function. Variables capture context at definition. So you write it once, you use it many times, but it's also frozen when the variable is declared, not when it's referenced.

**17:08** · So you cannot calculate a variable and add another filter because it's already been declared and cached. Therefore, there's no way to add additional modifiers of filter context to it. Using relationship activates inactive path. So one active relationship per pair of tables. So that means if you have two relationships to a table and you activate one that was inactive, it will automatically turn off conflicting relationships. So it will deactivate the other one. There is no notus relationship because it implicitly turns off ones that would conflict with it.

**17:39** · Calculation groups eliminate duplication. So one calc group with items such as the ones you see listed here can reduce dozens of nearly identical measures. Pushing work to the storage engine when possible meaning the model design. when I say pushing work to the storage engine. So the better your model design for natural paths for DAX to find relationships and be being able to crunch the numbers the better in terms of performance just overall bar none outside of exceptions. And these patterns that I've talked about build on context.

**18:11** · Every technique here from time intelligence to variables, relationships, calc groups, they all rely on filter context and calculate foundations from part one and two. So, I built the guides to layer on top of each other. A couple of tool references for next steps. So, I would recommend that DAX Studio, the links, all of these, by the way, are links to go to places. DAX Studio is a free tool um made by Darren who now works at Microsoft. DAX query view and performance analyzer are built into PowerBI desktop, but they're great ways to do further analysis. So, I'd recommend checking all of those out for some additional resources.

**18:42** · And just mentioning, good job. You worked through all three parts. Hopefully, you've gotten a lot of good concepts out of everything collectively that's built upon each other. At some point, I'm sure I'll have a part four that will come with maybe some more advanced things such as UDFs and a few other topics, but I think this is a good starting point for my foundation series to build on all of these before I continue on with maybe some more advanced topics. As always, if you liked the video, uh, drop some comments down below. Check out some of our related content here in the upper left.

**19:12** · Liking, commenting, sharing the video or the guide helps to get a lot of exposure for us. and uh just shares good content with the community.