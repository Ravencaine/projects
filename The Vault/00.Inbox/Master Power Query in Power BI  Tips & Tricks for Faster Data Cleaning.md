---
title: "Master Power Query in Power BI | Tips & Tricks for Faster Data Cleaning"
source: "https://www.youtube.com/watch?v=i3AcR4BjpdI&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=i3AcR4BjpdI&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Zefas Bi and Analytics]]"
published: 2026-07-01
created: 2026-08-08
description: "Power Query Tips & Tricks | Power BI Project Review HubMissed the live session? Watch the replay as D.E. Okeh (Host) and Chiamaka Igwe (Guest), both Power BI Data Consultants, share practical Power"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=i3AcR4BjpdI)

Power Query Tips & Tricks | Power BI Project Review Hub  
  
Missed the live session? Watch the replay as D.E. Okeh (Host) and Chiamaka Igwe (Guest), both Power BI Data Consultants, share practical Power Query techniques for cleaning, transforming, and preparing data efficiently.  
  
In this session, you'll learn:  
  
Data cleaning best practices  
Data transformation techniques  
Query optimization tips  
Building a robust data model  
Common Power Query mistakes to avoid  
  
Whether you're just starting with Power BI or looking to improve your data preparation workflow, this session is packed with practical insights you can apply immediately.  
  
👍 If you found this video helpful, don't forget to Like, Comment, and Subscribe for more Power BI tutorials, project reviews, and data analytics content.  
  
Download Practice Data: https://drive.google.com/drive/folders/1-BnDkTcGT68QEMHCu-tRz\_Ybss6wm11o?usp=drive\_link  
  
Kindly Help Provide Feedback: link to survey to be shared after the class https://www.metricsthatmatter.com/url/u.aspx?7E0283CB2237285502  
  
#PowerBI #PowerQuery #DataAnalytics #BusinessIntelligence #MicrosoftFabric #PowerBICommunity #DataTransformation

## Transcript

**0:02** · I'm happy you to channel LinkedIn. You can reach out to me just by typing my name across this platform. So today we're going to be looking at um Power Query. I believe most of you you are not new with um Power Query. You must have heard about it. You must have used it to do one or two things.

**0:19** · So today basically our session is going to be um to show you some tips and tricks that you can add to your workflow that can help you while you are cleaning data with Power Query as well as doing some transformation with Power Query to help you with your process.

**0:38** · So let's um get right into it. Sharing my screen now to Power BI.

**0:58** · So we are here now. This is Power Query editor within Power BI side of things.

**1:06** · If you're coming from the Excel aspect of things, you still have Power Query in Excel as well.

**1:11** · So this is like the first page that you see when you open this app and when you go over to the view tab for instance, okay, before that let's just import our data so that here can be populated where you have the queries. So we're going to be importing an Excel file.

**1:30** · There are different data sources and when you go over to get data, Power BI will give you an opportunity for you to import your different data source. If you're working with SQL, OData and the likes of it. So it's going to give you that opportunity to do that. But for today majorly we'll be working with Excel files and CSV files.

**1:51** · So let's load that in.

**2:01** · So, the first thing that we're going to be looking at here is on the view tab, actually. Uh you have a whole lot of things going on. First, \[snorts\] you have the query settings, which shows the applied steps that we have here. You can turn this off or on over here. Then, we also have um formula bar, which is currently turned off. You can turn it on as well. This helps you to write M query, which is the language that we use within within Power BI generally. You have two languages.

**2:31** · The DAX that you use on the front end side of things and the M query that you use over here in Power Query side of things to be able to clean your data and all. You can write this M query here within the formula tab. You can also write it over here within the advanced editor side of things.

**2:51** · M query it's not that difficult, anyway.

**2:55** · Although, it can't be that easy. But, with the la- large language models that we have now, you can easily learn a whole lot of stuff and they can help you as well. You can pick up um some materials online for it and when you get into an issue, you can easily ask Claude or ChatGPT to help you out. So, back to the view that we have on currently.

**3:17** · Then, we have this monospace, actually.

**3:19** · When you turn this on, it changes the font of these and makes it clearer for you, if you wish to.

**3:25** · And the next one is um show white space. For this particular aspect, it helps you to know if there especially for categorical columns, which we have here, like the location states. And this categorical column, most times you know that you're going to be using them for your to be able to slice and dice your data set for on your slicer, for instance. And the major thing that you need to ensure while cleaning it up is to ensure there are all unique values within here.

**3:56** · So, so if they are duplicate in a way, not really like duplicated, if there is a white space in front of your cat- categorical column, it's going to show that you have two different locations while they're at the same location. This is what I mean by that.

**4:17** · When I click on this show white space, you can see that Miami here has this first row has a space in between between it and the line, actually. When you're going to use this on a slider, this will actually show as one different Miami while this will be showing as another Miami. And that is not what you want.

**4:37** · So, always turn on this white space to be able to inspect your categorical column. I have it here on the location aspect of things. I also have it on the I think that should be the patient type aspect of things. You can see that showing here as well. So, it means that we need to clean this up. In order to clean this up, we have a function within Power Query known as the trim.

**4:59** · \[snorts\] And with the trim function, you can enable that by just right clicking on the column of reference, transform, and trim. Usually, what I do, I trim and clean at the same time. The reason I do this, trim removes white space while clean removes any character that comes in between data, especially when you're importing data from a database.

**5:22** · So, it's advisable when you're cleaning up your data, all your categorical columns, just by default, trim and clean so that you remove anything that you can see and not see. So, right now, just trim and also you have clean. Okay, before I go to cleaning, let me do that also for the patient type. You can hold down the control key and select two at once and trim.

**5:53** · Then, I want to also clean them. So, I'm going to still hold down the control key, select patient side, then go over to location. Hold down control key. Now, I've selected the two. I am going to clean the two as well. Then, the next thing I'm going to be doing here within this particular column, you can also see that um we need it to be in proper case.

**6:17** · It has a whole lot of cases going on here. So, you can do that within Power Query by clicking on the format aspect of things. You have different options of changing all columns all all the values within that column to lower case, upper case, or capitalize each word, which is what we want to do in this case. I'm going to click on capitalize each word to get this done. And also on the patient side.

**6:43** · Okay, because I already held down the control key while I clicked on that, you can see that it's automatically applied to patient type as well. So, this is kind of um straightforward. Then, let's go over back to the view aspect of things. The next thing is going to be on \[snorts\] the column quality, which also help you to understand your individual columns.

**7:08** · This shows you the valid, number of valid, error, and empty per column. So, you can use it to inspect your columns to be sure that there is no valid, error, or empty. And also the column distribution as well.

**7:26** · This shows you the number of unique and distinct. And this is very nice for the identifier columns, which in our case is the appointment ID. In this case, it's expected that you don't have any um that you have more of distinct and unique IDs on it. So, right now, you can see that we have 977 distinct and 954 unique.

**7:51** · The major thing that I need to point out here is that when you look at down here, you have that this column profiling is based on top 1,000 rows. So, if your data set has a lot of data, it's just going to show you one to top 1,000. You can't Excuse me.

**8:11** · In order to actually inspect columns and the quality of that particular columns, you need to change this to entire data set so that you will be sure of what you are looking at in this case. So, the column profiling now is based on the entire data set and can use it to actually identify

**8:34** · and be sure that you have the exact categories that you're looking at anyway. So, in this case right now, we have 2,000 distinct and 194 unique. So, for this data set, right? It is showing that we might have a case of um, double entry.

**8:55** · But, to be sure of that, you need to inspect this particular one as like I can see here, \[snorts\] the appointment ID 1159 and 1159. This is supposed to always show one appointment ID per row. But, in this our particular case, probably from data entry side of things, um, the person entering the data probably made a mistake or something.

**9:22** · So, this is something that we need to inspect. But, this is telling us that we might have duplicate in this data. So, to be sure that this particular rule, that they are two different or two the same, there's a way for you to actually check. But, from what I can see here, we have whitening and extraction, two different things, right? So, to also inspect the data generally, we can just check all of them for duplicate values. So, to do that, I'll duplicate this particular dental data.

**9:54** · Then, use group by. I want to group this based on you have the basic and the advanced. The advanced will help you to select multiple columns. I want to group this based on my appointment ID, add grouping, appointment date, and also add another grouping. It's going to be the revenue, appointment revenue. Then, we want to count to be sure that that the rows that we are seeing if they are actually duplicates or not.

**10:35** · So, this we count based on the number of appearances per row. This is showing us that you have either one row showing or two. When you scroll down here, you have two. So, let's um select that of the two to show us the values that are duplicate. So, you can see that that particular um appointment number that we saw earlier did not appear here. So, showing that that particular appointment number is not a duplicate. So, rather a data entry error.

**11:04** · So, these are things that you can note down and reach out to the stakeholder of the particular data. This is what I'm noticing within your data.

**11:11** · But, these are the duplicates that exist within this particular data set. You can now go into your data and remove those duplicates, um those duplicate rows, right?

**11:25** · Then, the next thing is going to be on the column profiling. We've seen quality and distribution. Then, the column profiling aspect of things, you can just click on this to show the profile of a column. This shows the number of times um the particular value shows in the column. Shows the value distribution. Let me take this down a bit.

**11:47** · For this column, when I click on location, it tells me the distinct values that we have within the location category. You can see that and the number of times that they appear. It shows the count of this particular column, number of errors, empty, distinct, and unique. This is and even the mean and max, as the case may be. It is a numerical column that I click on, gives me the distribution of that column, right? You can also do table profiling.

**12:17** · This is on the column aspect of things. So, let me turn off this particular stuff so that we have space. But, table profiling, you can do that using M query. We don't have any UI to easily see table profiling. You can do that with M query by clicking on this aspect aspect on the function. Then, you have table .profile. So, you can see now the profile of this particular table that we've seen.

**13:02** · It tells us like you see a holistic view, just like you do on your Python and on your Python and SQL. So, you can see here that the appointment column gives you the mean, max, average, standard deviation, depending on the column type.

**13:19** · Then, appointment ID, it gives you the distribution, the statistical distribution of each particular column, which is nice for us to know about. That is that for that. Once you're done inspecting, you can now delete this particular step and continue with your um data cleaning proper. Then, over here on the transaction table that we have, we can see also that we have that issue of white spaces.

**13:51** · And within this particular column, we have not just white space, we also have some weird characters within. So, we need to also clean this up. The way for you to clean up, since we have these three columns that have white space issues, I can click on other ID, hold down the control key to product, right click, and trim and trim and clean like we did.

**14:25** · However, in order to remove this um weird characters in our product, there are two ways that you can do this. The first one, which is like the normal simple one that we know, you can split this column by delimiter. Select the custom delimiter, which is palm key in this case. Click okay. So, it automatically splits it to five um different columns across. You can see different columns that I splitted it to.

**14:59** · Then, I can now continue by removing these two product um columns. They obviously they don't have any values within them. Then, we I'm now left with these two. Rather, let me go back. I think I removed one that I'm not supposed to. Okay. So, I'm supposed to remove um um product. So, I'm product four, also product five because we don't have anything in this ones. Then we are now left with these two here.

**15:39** · Product one and product three, which we can now merge together. Like product one, hold up control key and product three. Merge the two columns together. You can see that we've cleaned that.

**15:55** · But, when you go over to your apply step, we changed here. Then we now cleaned as well, which is normal. Then you can see that in order to clean just one column, you need to apply like one, two, three, four steps. And in this case, I also need to rename cuz the name has changed.

**16:13** · So, product So, you can see that I did five three the five things in order to clean just one column. This can actually be done in just one step. Let me just cancel all these steps.

**16:31** · Back to this part. Then where you have the formula tab, you can see that we had Okay, it's on the trim aspect of things, not on the cleaned one. This is where we're going to do this because we want to remove the pound key.

**16:49** · And I can just add a simple M query within here. This is why I said that M query is a a tool that you need to also explore aside from DAX. There are simple ones that can help your process that you need to know. I know it can be complex when you go up.

**17:04** · Um there are simple ones that can help you. So, in this case now, it instead of just trimming to remove white space for this, I'm going to be adding a step for it to also remove the pound key. To do that, I will type here each text.script and trim bracket then parenthesis bracket underscore first. So, this underscore is more like it's going to an iterator.

**17:35** · It's going to look through each of the individual rows. Then parenthesis within that individual rows as you're looking for it remove any pound key that I can find there. Also, in this case, remove any space that you can find.

**17:59** · You can see that it has done that. So, instead of having multiple steps, you might be wondering, "Yes, why don't we just have multiple steps and do it the simple way?" You find that that when you are working with an enterprise data set which has millions of rows, that multiple step will slow down the refresh time for your report. So, try as much as possible to remove any unnecessary step.

**18:22** · If it's a step that I can reduce, try to reduce it so as to improve the performance of your queries. And next thing that we're going to be looking at is the add column aspect of things. Within add columns, there are different We can add different columns.

**18:39** · You can add custom column, which is another place where you can um write M query. So, let's look at Denta. For Denta in particular custom column if you want to within our data set, we have these two costs here. If you want to calculate the total total cost within this Denta clinic, I can click on custom column. Total cost and for the staff cost. Insert and plus is just addition.

**19:23** · Equipment cost.

**19:26** · Insert as well and click okay. So, that's this is a way for you to give some column. You can as well write uh something that requires you to write an inquiry. This is another place where you can write um inquiries to do your manipulations as well. Then you can also add conditional columns. Conditional column is like your if statement.

**19:47** · Right? So, for instance, if you want the revenue revenue flag, if you want to flag revenue that is more than 500 USD for instance, so you have the revenue USD. If it is greater than 500 USD, then give me greater than 500 USD. So, I can use this on my slicer. Else, give me less than 500 USD.

**20:23** · So, in order to be sure that this works, you can reorder your columns. Right now, we have the revenue here. We can reorder here. So, as to compare to be sure that this is giving us what it's supposed to give. Right now, you can see that this is less than 500 and this is greater than 500, which works well.

**20:51** · \[snorts\] Then the next thing actually is the fact that you need to always try to batch um your steps and applications, especially the similar ones. For instance, within this particular report, let me say that when I got to change type for instance, I changed them I renamed some columns. Okay, let me just rename this just treatment type without the underscore.

**21:22** · Yeah.

**21:23** · I have a rename column here. Then I come down here again. You can see this in most um legacy report or something. Come down here again and I have um wait time. Someone is renaming another thing. So, you tend to see like rename columns multiple times within your query.

**21:43** · So, it's advisable for you to always do that. Try as much as possible to do that in one step. You can see now that it's showing me another rename column. This is increasing the number of steps that we have on our applied step. And then our goal is to always have lesser number of steps so that our query will run faster and load faster, which will really improve our user experience. So, instead of having these two things here, you can have rename at just one particular part. I can do the renaming that I did here, which is this um wait time.

**22:16** · Instead of having it here, have it here. Wait time. Do all your renaming here. Instead of having it down there. You can see that it's showing me here.

**22:34** · If I rename multiple things, all of them will show here. And this will also help in maintenance if someone is maintaining your report. You don't need to have um necessarily be named. And you can also Sometimes when I see some reports also, I will see replace columns. Replace column one, replace column two. Try as much as possible to do that in one step. Okay, I think that was pointlessly mixed this. I'm just deleting reorder Okay.

**23:05** · So, that is basically that for new me. Always try to batch your process all in one. Don't break down the step. So, the next thing actually, within this add columns, you have some transformations. You can see the extract transformation here. I find out that you also have it in transform.

**23:26** · In transform column, ex- extract and um some extractions as well. So, what this actually means is that you might be wondering at what point do I do the add column aspect as well. At what point do I do the transform aspect of things?

**23:41** · Um for the transform actually, if I do any transformation with this extract aspect of things, it does not create a new column for me. If I do that within the add column side of things, it creates a new column. What I mean by that if I want to in my customer name, I don't want the last name. I can do this extract here. Text before the limiter. The limiter in this case is space.

**24:12** · Right? You can see that it it's worked on that particular column. But, if I want the first name to be a different column apart from my full name that I'm seeing, probably I need that different column to send email messages. You know, when you're sending email messages, you send to first names. I want just the first name as a separate column. So, you can do that with add column. And to do that over here that we have the extract text before the limiter.

**24:46** · We have it here. Now, I can rename this here as first name. So, that's the difference between the at colon and the first name colon. So, let's go over to this next table and look at some transformation.

**25:08** · So, within this column, right? In order to clean this up, we already have um change type. You know, by default, most times, Power BI promote headers and change type for us, right? But, here within this particular table, it doesn't make sense that doesn't really change type. So, I'll remove this and also the promoted header aspect of things because my first two rows, I need to remove them. If you scroll down, you can see that they are null. It's just because it's coming from Excel. So, my first three rows, I need to remove them.

**25:40** · And to do that, I'll click on home, remove rows, top rows, first three rows, click okay. Now, I can promote header. Use first row as header. Now, it has still changed type for us, but I don't want to change type yet.

**26:03** · It's always advisable, especially for change type, don't do change type at the beginning of your query except it's important for that particular step. If it is not important within queries, try to do your change type at the end of your query because Power BI will keep on changing type. And you'll find out that if I not delete this change type and I do another step that requires change type, it will continue change type one, change type two, and all of that. So, you can always push this change type to be like the last part of the query.

**26:32** · But, before we even go forward, I'll just delete this for now. Now, within this particular query, we have um different columns that are empty. This column, this column, as well as this column. These are empty because of the way our Excel file is, right? So, to remove columns, usually, the default one that we know, we just click on column three, column five, and um Okay, I want to remove just column three and column five.

**27:08** · Then also the total in this case, because within Power BI, you can always do your measure calculation. Remove columns. And here it's going to reference column three and column five. Um as column removed. But the issue with this particular method is the fact that if within my data, this is the data now, if within my data, this column three and column five, someone comes in, especially for Excel data set, someone comes in and deletes them.

**27:43** · Then let me delete column five, for instance. Then within my report, refresh.

**27:52** · Refresh all.

**28:01** · Okay, I didn't save that.

**28:08** · Refresh all.

**28:13** · Now you can see that my code has broken because my column five is no longer there. And because it's referenced directly within my query. So, this is something that you experienced. There are two ways to always remove columns so that it will not break your report. The first one in this case is either going back \[snorts\] Let me go back and All right, let me just start with this first one, which is actually adding

**28:44** · um the M query aspect of things. When you type a comma, you see a missing field option over here. So, we have the missing field. ignore. So, it actually means if this particular field is missing, ignore this particular field.

**29:01** · You can see now that even though I did not go back to add that query and it to add that column, because of the missing field. ignore, it's going to ignore that particular column that I know that it was null. And even if someone deletes it, it's not going to break my stuff.

**29:17** · Another way you can be able to do this, aside just removing it this way, which is the best one that I prefer, is just to go over here and choose columns. So, then remove this particular step.

**29:32** · Then choose columns.

**29:37** · So, I want column rep rep name rep name, region, Q1, Q2, Q3. I don't want total. So, what this does is that these are the ones that I know that we always have data.

**29:51** · And it's not And the ones that I removed are not referenced in my um query. So, even if someone deletes them, it's not going to break down my stuff. So, this is like a failsafe for you to be able to like always ensure that your query is um your query is uh it's not going to break when you load it. And over here, you can see that it's remove other columns. So, you remove the ones that you don't need. You only selected the ones that you need.

**30:14** · And still on that particular choose columns as well, you can also look at the go to column aspect of things. This particular one is good, especially if you have a table that has multiple columns. For instance, this particular one that you need to slide in order to get a particular column. You can go to If you want to get get a particular column that you need, you can use this part.

**30:44** · Go to column. I want to get to wait time without scrolling left and right, especially if I have um a table with multiple columns. It automatically gets to that for you.

**30:57** · And within this, you can If you want to see the values of all the rows at once instead of sliding back and forth as well, you can just click on this um the row and you have like a vertical view of everything within that row when I take this up. So, it shows you vertically, which is easier to read than scrolling left or right.

**31:27** · And the next thing that we're going to look at, remember that I said within the quarterly sales, that is always advisable for you to change type at the end of your reports, right? Which in this our particular like it's that I'm done with my transformation here, I can now change type. My rep name is text and region is still text. Q1 sales is um fixed decimal, Q2 sales is fixed decimal, and Q3 sales is fixed decimal.

**31:57** · This is one way to go about change type instead of having multiple change type. Then another way, because by default, when you load your data into Power BI, Power BI automatically change type and promote header for you. But if you don't want that to always happen within your data, you can control that by going over to the prof um options and settings, which is in front part of Power BI file, options and settings, options.

**32:33** · Scroll down. So, you have here the global aspect. Global actually means that if I set this change here, all the files I open even in the future, they will all take the same shape. So, you can go over to this part and check on never detect column types as headers for unstructured sources. So, this will actually stop it from automatically detecting for you. Do that and click okay. You can also find these settings on data load.

**32:59** · On when you uncheck this particular one as well, it will stop detecting types for you. You can do that manually and be sure that it's the data type that you need that it it gave you.

**33:13** · Then, let's move forward. We have the regional sales data. On this particular data, within Power BI, you see um Power Query, you have opportunity to pivot and on pivot as well like you do on your Excel. So, for this data set that we have um sales person, region, January, February, March, and all. And Power Query does well with longer tables and wider tables. So, in this case, we want to on pivot this.

**33:39** · I'll click on January, and hold down the shift key to June, right-click, and on pivot columns. So, this actually helps me. Now, I have my sales amounts and the month name, which is easier for you to work with when you're loading your data. Then, the next data set that we can look at is the product data set here.

**34:18** · So, for this actually, before we look at this, let me remove the bottom rows. You can see that these bottom rows are empty and it's actually because of Ex- Excel. So, I'm going to remove bottom rows. Just like we did for top, we can remove bottom three rows.

**34:37** · So, this is actually This occurs when you're working with timeline data, especially Excel data set that are merge and center kind of data set of which you find in projects. So, you find out that week one and week two is supposed to be and even week three is supposed to be planning and assessment for these and all. So, we need to fill left and right. Within Power Query, you can fill up and down. We have that option just like we do in Excel, but you don't have the option of filling left or right.

**35:08** · But, there's a way that you can actually achieve this. I'll go back to transform. The first thing I'm going to do right now that we have headers off, I'll first of all demote headers. And so, that would be on use first row as header. So, use um header as first row. So, it's demote headers. Then, next thing I'm going to do is to transpose.

**35:42** · So, now that we have transposed, you can now see that I can now be able to fill up and down for this in order to fill them. So, I'll right click. I will click on this. Hold down the control key or rather the shift key in this case cuz I want to fill down a lot of things. Scroll to the end, which is column 10.

**36:03** · Right click.

**36:04** · Fill down in this case. Then, now that I'm able to fill down, I can now go back and transpose again. Then, finally use first row as header. So, you can see that this works now. With that limitation that we had earlier, this is the way for you to if you have an issue with filling if you want to fill left and right, this is a way for you to be able to achieve that.

**36:37** · The next is actually on a new data set. When you are importing a CSV data set for instance, so let's import a CSV file. We have the CSV file here.

**36:57** · Click okay.

**37:04** · So, within the source file you have Sometimes when you import CSV file, it shows you the delimiter and also shows you the columns the number of columns within this. So, we have 16 columns, right?

**37:20** · And as you can see here, this number of columns is hardcoded. So, meaning that if in the future we have 17 columns, 20 columns, this is going to break. So, in to ensure that this is actually dynamic and it doesn't break in the future, when you import CSV file, go back to the source and remove this columns import soon.

**37:45** · So, it imports. No matter the number of columns that you have in the future, it will always run whenever you load the query. It's not going to break. Then, the next part actually also within Power BI apps Power Query this gives um let's match, just like you do your joins in SQL. So, we have a Superstore. We have these two tables, manager and orders. So, within the orders table, you have this particular row, which is region.

**38:45** · Right, central, east, west, and um south. Then, in manager aspect, we also have the region table as well as the manager that is responsible for that. So, we want to merge these two tables together in the sense that each manager that is responsible, you can be able to trace the transaction that occurred in the by that manager and be able to like perform your analysis as you go forward.

**39:10** · So, I'll use first rows as header for this. Then, on the orders table, I'm going to merge. We have merge queries. You can merge as new that is creating a new table. You can merge on top of the one that you already have. And you have the manager here.

**39:36** · So, you're going to be merging based on the on the same columns that are present in these it's two tables, which is the region in our case actually. Just like you do joins in SQL.

**39:53** · Then, you have different join, left outer join, everything from this first table and corresponding from second, right outer, the same thing, everything from this and corresponding from this first one. Then, you have the full, the both tables, everything from both tables in and just the matching. So, in this case, I want it to be left outer.

**40:16** · Then, click okay.

**40:18** · And within here, you can expand the table. This is a symbol for expansion. And over here, use original column name as prefix. This help you to be able to trace which table that this particular column is coming from. And within this table, we want just the manager to show because we already have region.

**40:37** · And click okay.

**40:40** · However, we have the manager now showing here for each region. However, I am not really a fan of merge queries cuz I've worked with enterprise data set that it takes time to load when you merge a lot of queries. And if you are working with multiple rows, so it's better instead of doing this, just import the two tables into Power BI and create a star schema.

**41:05** · This is your dimension or just region, that is your fact table. The other is your fact table. Manager is a dimension. Just create a star schema. Having merge queries, especially when you have multiple merge queries, affect performance. But this is one way if you are working on a smaller project that you feel that you don't need to import a whole lot of things, you can just do one merge query and import.

**41:26** · All right. Then the next one is append queries. This particular one, let's import another data set for this. We have There are people that store their data set by years. So in this case, we have online sales data for 2023, 2024.

**41:46** · \[clears throat\] Excuse me.

**41:48** · So I want to import the 2023 and 2024 for instance. So I'll click on 2023.

**42:02** · Click okay.

**42:07** · Then new still excel workbook.

**42:12** · 2024.

**42:25** · Click okay as well. So, now for append queries, you need to have the same number of columns as well as the same type so for this to work. So, basically, right? We want to like have one master data that will have whenever I just like you can see here, you have 2023, right? If you have 2024 data, let it all be in that one master data. If you have 2025, let's also join that as well.

**42:57** · And so, in this case now that you have this first one, you can click on the append query aspect of things. You can append as new and append on top of that. In this case, I want to append on top of the one that is currently existing. So, I'll click on this append query.

**43:14** · Select the table that I want to append, which is 2024. If you have 2025, 2026, and all, you can select all of them as well. You have the option of selecting three or more tables.

**43:24** · Then, click okay.

**43:27** · So, now initially, let me go back to the first step. When you look at the dates here, we had just 2023 year. But, when you look at the appended aspect of things, you now have 2024. So, that is the way for you to like create a master data set for yourself.

**43:48** · Now that we have merged query, we've appended, find out that there are some queries that you don't need to load into your Power BI front end of things to prevent confusion if you're not using them. For instance, this others table now is the one that is now our major. For our manager, we don't need that in our front end. In order to ensure that doesn't occur, you can right-click on this and disable load.

**44:13** · And ensure that it's always on the include reports in report refresh. What this does is that you it's always refreshed when your report refreshes.

**44:24** · Then, the next one here on 2024, we don't need that again because we have appended the data in here. So, we can also disable load as well. You can see that both now are in italics because we don't need two of them again. They're not being loaded, but they're still on the Power Query aspect of things.

**44:45** · The next thing now that we are going to do \[clears throat\] is to add um parameter, which is a good practice, actually. Parameter for your uh data sources. For this first set of data source that I've imported, you can see that they were all from same data source, which is this particular data.

**45:06** · I can add a parameter for it within um Power Query. To do that, I'll go back to this part, right-click on this, and copy path.

**45:18** · Copy as path.

**45:21** · And go back to Power Query side of things.

**45:24** · Home.

**45:26** · And um transform in this is not transform. Let's go back. It's home. Manage parameters, yeah. Manage parameters, new parameter.

**45:40** · Data source.

**45:52** · What is the current value?

**45:55** · You paste that particular file path that you copied.

**46:04** · And click okay.

**46:07** · So, the reason I did this and which is nice and a good practice, especially for the fact if you're working with Excel file and you want to share this particular report to someone, you can see that this is already the data source is within this first one. If you look at the data source aspect of things, it's referencing my own system. It's not like an online data source that I someone can connect with and it automatically refreshes.

**46:33** · So, if someone tries to like open the Power BI aspect of things, the person will see error. So, what you I we did now by creating this data source so that when the person gets this, cuz of course when you are sharing the Power BI report, you're sharing the data source with the person separately. So, the person can easily copy their own file path from their data and put in here.

**46:52** · So, to ensure that this is now going to work within this first five um queries that we created, we can go over there and reference them. So, instead of it being hardcoded this way, you can now select a parameter, which is the data source that we've created, and click okay. So, when you go back to Let's go back to the advanced editor. You can see that it's referencing Excel workbook and the data source parameter.

**47:28** · So, when someone gets this data set, I mean this report, the person can easily go in here, change their own um file path, and then tell that data data it refreshes and shows. You can also do the same for transaction, go over to the data source, and do the same step that we did up until the fifth one. All the reports All the tables that are referencing it, you can as well do that.

**47:55** · Then, the next thing that we're going to look at is proper documentation.

**48:00** · Um documentation really help you, especially when you're working in an organization where you have other developers and you tend to like share files around. For people to actually understand what you did and the reason you did what you did. And there are ways that you can do documentation. The first part is on the applied step level. Just like here that we started step before delimiter. If I want to add um the reason actually what did we get?

**48:30** · Okay, we inside a step in order to create first name. So, the reason we did this, if I want to add it is like a complex step that you want to explain the reason you did. And it will also help you because there are times that you go back to the report that you created. You'll not be asking yourself, what did I do here? Why did I do it? So, when you do these documentations, it helps you to like remember as well as help people to maintain your report. So, right click on this and you have these properties aspect of things.

**48:56** · Here now, I can say that I created first name. So, that is why I did this particular step. So, when I hover on it, you can see this symbol that is showing that there's an information. When I hover on it, I can remember what I did. So, you can also add applied step, I mean a documentation on folders. But before we do the folder aspect of things, you need to rearrange this. We know that we got all these particular one from this data source.

**49:25** · So, we can create a folder and add all these to this data source in order to arrange things. So, I'll hold on the data source, select all these. Up until this big tool. Right click and multi group. So, Like just say first data or something.

**49:57** · And you can also see that okay, now that we have them in the folder and this is actually well arranged. Within that folder, I can add the description. You have option here of adding description first data that I worked with or something. Description that will tell the person looking at this what this queries are for. Then over here you have the major data set that you loaded as well as the supporting. So, I can rename this. I can um group this as supporting data sets.

**50:36** · Select this one.

**50:40** · Move to a group. New group because I'm not going to load them.

**50:46** · Supporting queries.

**50:52** · You can describe it as queries not loaded or something. Something descriptive that can help someone to actually understand your process. So, these ones that I described now, when you hover on it, you can actually see the this description will show first data or queries not loaded. You can also add description on a particular query aspect of thing. Just like if I select grocery for instance, you also have that properties.

**51:23** · To have description on that particular query and what it is doing, right?

**51:30** · Documentation is actually key. It has really helped me a lot and it's something that you should imbibe in your workflow. And final thing that we are going to be looking at is how to I need to create a new Power BI Desktop limit one. How to copy one query from one report to another.

**51:47** · Assuming you are working on a report that has similar queries and you don't want to start recreating all the applied steps one after the other. If you are working in that scenario, and um transform data.

**52:39** · So, it's coming up. Okay, we have this support here on this screen. Let me drag this down. So, we have two power queries open. I have this one here and I have this one. And where you going to Okay.

**52:58** · So, I have this is So, probably you have like you need data set that you run the same query from let's say the first part, which is our dental data, and you've applied a whole lot of steps. You don't want to do that from beginning for this. You can easily go back to the \[clears throat\] We have the advanced editor. Click on the advanced editor.

**53:23** · Select copy.

**53:26** · Well, for this case, you will need to first of all create the data source. So, I'm not going to be taking this. This is not like a good example. Let me just take the one that I did not create data source because that first one you need to create the parameter first and before you copy. So, let me just take this that I did not do that for now and then I'm going on to this time. So, I want this query, just click on This is a fresh report. I can click on new source instead of starting from beginning my Excel and all of that.

**53:57** · I can click on blank query. Open up the advanced editor of that one. Clear of this and paste. That same applies there. So, you can easily do this from one report to another fresh one without any processing. Then you can now rename your query. So, that is all that I have for you guys today.

**54:32** · Time for questions.

**54:42** · Okay, this was you know, when you say something is when you're trying to advertise a product and you place an advice for a product and get to get a product and to see if you got what you what you bargain for like exactly the best advertisement of what we got in so far. Like you said, Power Query tips and tricks and everything we had here is just Yeah, honestly there are some tricks I didn't actually know that existed here.

**55:14** · Like I learned a lot of tricks today.

**55:16** · Like I'm just I'm just looking at it and I'm trying to say to myself, "Okay, next time when I'm going to work on Power Query, I'll pay attention to some of these tricks cuz that's me I've been doing some things like I'm guilty cuz I really didn't pay much attention to steps. I just felt like, "Okay, if I'm able to just get the data clean, I really don't care the amount of steps I've actually applied. All I'm interested in is just to get it clean sometimes. I didn't really pay attention to some of these tricks and all that.

**55:49** · Thank you very much. We really appreciate We appreciate and thank you for these tricks we've learned. So, it's one thing to learn, it's another thing to make sure you put these tricks into practice when you're creating your reports, right? So, it's really really important. Thank you very much. So, if there's any question, you can actually just unmute yourself and ask the question.

**56:09** · But, one request has already been made and theirs is if I get to upload the video, we'd also want this data set so we can actually practice everything you um um taught us, right? While watching the video. So, we'd really appreciate if you help us with the data set so watch and practice along. Once again, thank you very much for these amazing tips and tricks.

**56:34** · They're really tricks, actually, cuz you're not really going to see a content about Power Query and data, but it's these tricks like this. You're So, we really appreciate and thank you for your time. So, if you don't have any questions, we'll be ending the session, but if you have any question, you can actually just unmute and ask your question.

**56:58** · Hello everyone, can you hear me?

**57:01** · I can hear you.

**57:02** · Yeah, we can hear you.

**57:03** · Thank you very much for chairman. I really appreciate this. Man, the part you talked about uh you know when you talk about that renamed columns and change type. I've never seen anybody talk about that thing like the way you said it before. I really appreciate it. It makes sense to me so much.

**57:19** · And another one that I like that you talked about was the because I usually use query parameter, but not I've not seen this kind of case scenario. Like I've not even thought about that part, never. When when you talked about uh that you got copy the parts. Uh so, when somebody else get the file, they also copy the same part in the query parameter.

**57:38** · Exactly.

**57:39** · And they can use that to So, so instead of all these errors everywhere, Uh yeah. Just one.

**57:44** · I've never God will bless you.

**57:46** · Makes sense to me so much. Thank you. Thank you. I've learned something from here.

**57:50** · Yeah.

**57:51** · I appreciate it. Thank you.

**57:52** · Yeah. Thank you.

**57:57** · Yeah, you know that you know that missing part, right?

**58:01** · \[laughter\] \[gasps\] Well, yeah.

**58:05** · When you go back, so sometimes, if you need to make a change in the original data set, you just ask someone, "Please, don't go back or rename. Just leave it the way it is." Look In fact, you know, you know, if, for example, you say you're not going to use that column anymore, do you know sometimes you just say, "Okay, don't worry. You're not going to use the column, but don't touch it in the main data set itself. That's your data. Leave it there. Just leave it there the way it is." But How missing rule?

**58:30** · The missing field.ignore, you can also use it cuz I already did it here for remove rows. You can also use it for rename. You can also use it for reorder. Yeah, reorder columns. So, you can explore that as well. So, if someone goes and reorder, once you add it, it's kind of it will automatically even if they are reordering, it's none of your business. So, you can just explore that aspect as well.

**58:56** · Yeah, it's really really great. You're really great. Yep. We enjoyed every bit of the session. I'm going to put the video out there and share it with everyone that you registered for the session. I told you before, maybe the time zone allowed some persons to join, but I've already gotten a request about about the beta, so they can actually watch the video and practice along. And thank you very much from RBI Project View Hub. We appreciate you.

**59:23** · These tips and tricks are very important cuz whatever you're going to do in Power BI, right? Everything is relying on your model and for you to have a good model, that means you must have a clean data.

**59:34** · You just can't ignore it. The reason is you having a clean model and a clean data the goal. You can have a um your numbers can be correct and maybe your visuals are not really well presented, but your numbers are correct. It's even much more better. I think I can accept that than having the wrong numbers and having a very great dashboard or report and the numbers are all wrong. So, this tips and tricks we appreciate and thank you very much. Hope next time we get to invite you again. But for now, thank you for honoring our invitation.

**1:00:06** · We appreciate this. Thank you very much.

**1:00:10** · All right. You're welcome. All right, then. Bye, everyone.

**1:00:13** · All right, guys. All right. Bye.