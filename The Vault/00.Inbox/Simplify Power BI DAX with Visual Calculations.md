---
title: "Simplify Power BI DAX with Visual Calculations"
source: "https://www.youtube.com/watch?v=VEwGH6i2aeE&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=VEwGH6i2aeE&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Havens Consulting]]"
published: 2026-07-28
created: 2026-08-08
description: "If you've ever written a running total in DAX, you know it's more work than it has any right to be. CALCULATE, FILTER, a column reference you have to get exactly right, and a quiet prayer that it beha"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=VEwGH6i2aeE)

If you've ever written a running total in DAX, you know it's more work than it has any right to be. CALCULATE, FILTER, a column reference you have to get exactly right, and a quiet prayer that it behaves at the subtotal level. Visual calculations let you write RUNNINGSUM(\[Sales\]) and get on with your day.  
  
They're a calculation layer that lives inside the visual itself, working on the data that's already been aggregated rather than querying the whole model. That's also why they're often faster, sometimes dramatically so on DirectQuery.  
  
I walk through the core functions (running totals, moving averages, PREVIOUS and NEXT for period comparisons, FIRST, LAST, INDEX, and RANK), then the hierarchy functions like COLLAPSE and EXPAND that make "% of parent" and "% of grand total" almost trivial. We also get into AXIS and RESET, which control the direction a calculation runs and where it restarts, because that's the part that quietly breaks people's running totals across years.  
  
One honest caveat. Yes, they're easier and faster. But because each one only lives in a single visual, they can fragment your business logic across reports if you're not careful, so I cover when a visual calc is the right call and when it really should be a centralized measure.  
  
RELATED CONTENT 🔗  
Visual Calculations Guide -- https://go-ae.org/hc-yt-visual-calc-guide  
  
BECOME A CHANNEL MEMBER 🎉  
\-- https://www.youtube.com/channel/UCjlfQwqb-0S40XQ8seYPLSw/join  
  
CHECK OUT OUR MERCH STORE 👕  
\-- https://havens-consulting.creator-spring.com/  
  
LET'S CONNECT! 🧑🏽‍🤝‍🧑🏽 🌟  
\-- https://www.linkedin.com/in/reidhavens  
\-- https://www.youtube.com/c/HavensConsulting  
  
BUSINESS PAGES 📄  
Home Page - http://www.havensconsulting.net/?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=VEwGH6i2aeE  
Blog -- http://www.havensconsulting.net/blog-and-media?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=VEwGH6i2aeE  
Blog Files -- http://www.havensconsulting.net/blog-files?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=VEwGH6i2aeE  
Files & Templates -- http://www.havensconsulting.net/files-and-templates?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=VEwGH6i2aeE  
Consulting Services -- http://www.havensconsulting.net/consulting-services?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=VEwGH6i2aeE  
Online Courses -- https://www.havensconsulting.net/online-courses?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=VEwGH6i2aeE  
Contact & Support - http://www.havensconsulting.net/contact-and-support?utm\_source=youtube-hc&utm\_medium=video&utm\_campaign=VEwGH6i2aeE  
Analytic Endeavors-- https://go.analyticendeavors.com/86d335734f  
  
EMAIL US AT 📧  
info@havensconsulting.net  
  
#PowerBI #DAX #DataVisualization #MicrosoftFabric #BusinessIntelligence

## Transcript

**0:00** · Hey data fans, Reed here. Today, I'm going to walk through another interactive guide that I made. This one's going to focus on the topic of visual calcs. So, one of my favorite features to come out for Power BI in the last couple of years, uh thanks to Yaron, um before he actually moved careers over to Tableau editor and moved back uh to Europe, but he was in charge of the product for this to basically bring DAX measures at the visual level into the visualizations in the report layer. Really fantastic feature, excited to walk you through the guide.

**0:28** · But, with that being said, let's go ahead, check out the guide, and get started.

**0:41** · And I'll start with the question of what are visual calculations. So, DAX measures live inside of the semantic model itself, and they are ran against the actual model. Now, visual calcs will live in the visual layer, and that is going to have things such as special functions for like running averages, moving averages, previous and next, but they are visual by visual, stored essentially in the report layer, calculated inside of the visualizations.

**1:10** · So, let's see the differences in action.

**1:12** · Below what we have is a base table with a visual calc added that we can see for running total, which is a running sum that was added, in this case, to a visualization, likely a table or a matrix visual.

**1:25** · Now, some of the core functions, as I mentioned, there are a unique set of functions built in to visual calcs that are meant to be calculated at the visual level. So, one example is a running sum, which will give you a running sum of everything basically either left and right on the axis or top-down on a table that will just total up the values, whether or not it's by period or by category, it doesn't really matter, it will calculate these up. You can also calculate moving averages as well.

**1:50** · So, as you can see with the function here, that will actually do a moving average per the number of previous rows um that you have inside of the visual or along the axis.

**2:05** · Moving on, you have previous or next which basically just goes to the prior or the next row that is built into the visualization.

**2:12** · First and last which will just grab the first or the last again from essentially the data grid that you have inside of the visual.

**2:19** · We have index and row number so that will go to the position that you've specified within again the data grid.

**2:26** · And look up or look up with totals which will allow you to basically fetch a specific value from anywhere inside of the visual matrix or data frame as I'm calling it where look up will inherit the current rows other dimensions which can be really great for um same time period comparisons whereas look up with totals will ignore them and pulls from the total which can be perfect for a comparative fixed baseline.

**2:53** · And finally, we also have rank which would allow you to pull in the rank and determine instead of having to have a DAX measure for this the rank of these values compared to the other ones inside of the data frame for that particular visual.

**3:06** · And moving on from this there's also hierarchy functions that pertain to matrix tables themselves. So the collapse function for hierarchies will aggregate the values to the parent level in a hierarchy with the key function being for the percent of parent in calculations for matrix visuals. We have collapse all which will aggregate all the way to the grand total regardless of the hierarchy depth which is perfect for percentage of grand total calculations.

**3:32** · We have expand or expand all which will drill down to the child level values in a hierarchy and expand moves one level down to the immediate children while expand all goes all the way down to the lowest leaf level as you can see in some of the examples that we have here.

**3:48** · And in the example you can see that it's grabbing the first row from the below it at the subtotal level.

**3:55** · Now, is that level is a test similar to other if conditions where it will test whether a column sits at a current level in a hierarchy. Essentially, what this is is this is a visual calc version of is in scope but meant to be a function only used by visual calcs.

**4:11** · Continuing on, let's talk a little bit about also axis and reset parameters which allow you to control the calculation direction and whether or not you want to restart certain behaviors.

**4:21** · Now, the reason that these come into play as functions is because generally speaking, there are default directions that certain running totals will calculate. This allows you to control, especially in a matrix grid, which directions that calculation will go between rows, columns, row and column pairs, or column and row pairs, none, or even highest and lowest parents. So, all of this is a little cheat sheet here at the top and then digging into some examples. So, here's it without reset where you explicitly specify that you want a running sum for sales to calculate down on your rows.

**4:51** · Now, you can also apply a reset using highest parent in this case where you can see that for 2023, it calculates the running total, but then it resets at the highest parent, which is year, and that automatically resets it for 2024 onwards for those. So, really it's just giving you some framework to understand that some of these functions can be further specified to allow you to shape how these calculations go down or across and also potentially reset in combinations with each other.

**5:23** · Now, here's a little breakdown kind of a visual calcs versus DAX measures essentially to help you understand various things. As an example, first row here, the scope, visual calcs are single visual only versus DAX measures which are the entire semantic model. The reusability, visual calcs aren't particularly reusable with some caveats being as you can copy the visuals to different workbooks and there's a way to do some reuses with these. Injay Park has done a couple of videos of making visual calc template visuals.

**5:50** · But natively, I would say no, normally they're not reusable to that degree. They're kind of one-off calculations per visual for the most part. Whereas DAX measures, of course, are very reusable. Data context, so the visual calcs can only read what is inside of the visual for the aggregated matrix, basically the data frame for the visual. It is calculated after the initial data loads where a full filter context, full model context is available for DAX measures.

**6:19** · Complexity, visual calcs aren't designed to be that complex. Yes, they have a series of functions, but they're meant to be simpler and intuitive. Obviously, you have the full library of DAX functions available when you are using regular measures.

**6:32** · Continuing down for performance, visual calcs are often faster because they are calculated post aggregation and after the model has already processed data into the data frame, whereas measures can be faster or slow depending on what the model query itself is and the the query plan is for those. Model impact, visual calcs are report layer only where DAX measures are changes to the semantic model. And last but not least, best for quick analysis and prototyping for visual calcs.

**6:59** · And again, one-off type things where DAX measures are more centralized business logic for those. Some takeaways of using visual calcs when quick running totals, moving averages, row comparatives are a big one.

**7:11** · When the calculation is specific to a visual and you want to prevent model bloat, great way to leverage those without having to add a bunch of extra measures. You can use DAX measures generally when most of the historical stuff that we're familiar with with those. When the you want repeatable calculations that will be needed for multiple visuals.

**7:29** · And governance consideration, it can fragment business logic a bit, so just be careful on that cuz it is scoped all the way down to the very end of the pipeline at the visual level. So a little bit harder for people upstream to manage those and also know if the numbers are right if you were doing these ad hoc. So, something to keep in mind.

**7:46** · Uh now some performance benchmarks as well. So, this comes from Boaz at datatraining.io how to Power BI. He did find that there were some performance considerations between the two of them um with a couple of things. So, in import mode he found that Pareto and cumulative was about 4x faster, moving averages was about 5x faster. Leveraging direct query because that calculates after the fact, so these are calculated locally rather than from the core system. So, it actually in some cases was significantly faster in some scenarios.

**8:16** · So, things to consider and also the link in the guide will take you to information around that if you'd like to check that out. Um but some useful facts on this that I think help to give us the understanding that visual calcs aren't just for single use calculations, they actually can help with some performance improvements. So, due to the fact that they have post aggregation processing, this happens after the initial model data is loaded from whatever system that's coming from.

**8:43** · They, as we can see, have some direct query benefits because SQL or any other direct query sources normally aren't that good at aggregating data compared to say the semantic model. So, in direct query scenarios this can have a performance benefit. And sometimes these can be a bit of a performance sweet spot, a nice little um bridge of two worlds and a nice little middle ground to allow for some optimization when needed.

**9:06** · Now, a couple of other callouts that I want to present on some community contributions for these. Um so, I had one where I helped use visual calcs to create a dynamic vertical waterfall chart. So, I have a video and tutorial you can watch there for that. Um there is also one from NJ Park where he does visual calculation templates. So, I'd recommend checking out some of his stuff if you want to explore a bit more of those. Um IBCS style variance charts as well.

**9:32** · So, visual calcs can be a great way to add some of those IBCS type of columns in visuals to be able to have some of those red green variances and other stuff like that linked below to also give you some more information on what IBCS is and some of the communication standards they have around visualizations.

**9:50** · They also can be used for simplified conditional formatting. Marco and Alberto over at SQL BI wrote a great article on that with a link as well to provide for that. Um, they are really good for indicator positioning techniques where you can use a line and stacked combo chart with visual calculations for precise indicator positioning which pairs well with field parameters. That was done by MK Feldman, uh, the BI accountant and a blog link for her.

**10:14** · And last but not least, I'll just say as a general fun pattern, the Pareto analysis pattern. Combining the running sum with a collapse all, you can actually do a very great Pareto chart leveraging visual calculations as well.

**10:25** · All right, so some tips and gotchas.

**10:27** · These are great to leverage to be able to combine for conditional formatting.

**10:31** · Often for bars and color rules, visual calcs are really good for that.

**10:35** · Or use order by for sorting control, meaning use running sum or order by to control calculation order independent of the visual sort if you're trying to fix that regardless of sort order of the visual.

**10:47** · Referencing other visual calcs, so you can build these in stages. It doesn't just have to be one, you can have multiple visual calcs all paired nicely with each other.

**10:56** · You can also test with small data, so explore it, double confirm the numbers.

**11:00** · It's easy to miss the forest for the trees when you're going through some of this stuff, so make sure you are, uh, testing for performance reasons cuz you don't want to accidentally deploy this to a large model that ends up actually becoming potentially ill performance. Um, there are still exceptions where visual calcs can end up becoming costly depending on your scenario.

**11:20** · Graduate to DAX when needed, so as upstream as possible, downstream as necessary for Matthew Roche's maxim.

**11:27** · When and you find out a pattern when you're starting to use visual calcs and you've noticed you've the same one repeatedly for this for multiple different visuals. If possible, consider turning it into a DAX measure.

**11:38** · And you can also combine these with field parameters. They are very useful to combine with a lot of stuff to create dynamic measures and switching values in a table, matrix, or visualization.

**11:49** · Now, some core limitations. There is no reusability across visuals, as I mentioned before. You cannot filter or slice by these. They only exist in the visual. You cannot add it as a visual level filter on top of one of them. And you also cannot put them into a slicer.

**12:05** · There's also no data export, so when you export the data from the visualization, you will not get the visual calcs that come with it.

**12:11** · And there's also no dashboard pinning for this for the very small amount of you who still use dashboards today in Power BI.

**12:18** · A couple of other ones to mention.

**12:20** · Unless explicitly fixed or added into the visual calc, sort order dependency for certain functions such as running some previous and next do depend on the visual sort order, so you should order by if you need explicit control for that.

**12:33** · Field parameter conflicts can happen, so if a field parameter exists in the visual, the new visual calculation button may disappear.

**12:40** · Unsupported visual types. So, there are a few types of visuals today that are unsupported. This list might change with time, but things such as slicers, Python visuals, key influencers, and a few others currently do not support visual calculations.

**12:53** · And there is no publish to web option with these for functionality for public-facing reports, at least as of today.

**12:59** · A couple of other edge and advanced scenarios.

**13:02** · No relationship functions built into visual calcs.

**13:06** · There is no self-referencing, so a visual calculation cannot reference itself even indirectly through another visual calc that points back to it.

**13:13** · Otherwise, you'll end up with a recursion error.

**13:16** · There's no drill-through or personalization that comes through as a feature for those related to visual calcs, so those two features cannot see them. And last but not least, some platform-specific limitations. So, SSAS live connections will require SQL Server 2025 or later.

**13:31** · Power BI Embedded has no IntelliSense, just FYI, for visual calcs. So, authoring does happen blind for these, and check your target platform before relying on them.

**13:41** · And last but not least, there will be a quick reference guide with some references for all of your visual calculations at glance, and some things at the bottom for some optional parameters as well to determine direction and where the logic gets processed for some of those running calculations.

**13:55** · But, overall, I hope you found this guide useful. Visual calcs are a great feature, and this gets a good introduction and intermediate walk-through of a lot of the families of functions that are built into visual calcs and some of the use cases you have for them. So, hopefully, it's something that you can take with you and maybe get started in some of the development that you might have for it. But, otherwise, drop any comments or suggestions for future videos down in the comment section down below. Check out some of our related videos here on the upper left, and as always, liking, commenting, and subscribing will help the channel grow. With that being said, I'll see you in the next video.