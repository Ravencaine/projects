---
title: "5 Power BI Slicer Tricks To Build Professional Dashboards"
source: "https://www.youtube.com/watch?v=sdyxtL1250E&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=sdyxtL1250E&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Goodly]]"
published: 2026-07-22
created: 2026-08-08
description: "Learn how real Power BI solutions are built, from messy business data to the final dashboard - https://products.goodly.co.in/power-bi-dashboardsIn this video, I share 5 useful Power BI slicer tricks"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=sdyxtL1250E)

Learn how real Power BI solutions are built, from messy business data to the final dashboard - https://products.goodly.co.in/power-bi-dashboards  
  
In this video, I share 5 useful Power BI slicer tricks that can make your dashboards more dynamic and easier to use. You’ll learn how to automatically select the current month after a refresh, use Apply All and Clear All Slicers buttons, display column values using Field Parameters, use a slicer to highlight data instead of filtering it, and create slicer hierarchies for your measures.  
  
These Power BI tips use practical features such as DAX, disconnected tables, conditional formatting, field parameters, and dynamic slicers that you can apply to your own reports.  
  
  
\===== ONLINE COURSES =====  
✔️ Grab My Power Query Book -  
https://products.goodly.co.in/power-query-book/  
  
✔️ Master 'M' in Power Query -  
https://products.goodly.co.in/learn-m-powerquery/?  
  
✔️ Mastering DAX in Power BI -  
https://products.goodly.co.in/learn-dax-powerbi/  
  
✔️ Power Query Course -  
https://products.goodly.co.in/learn-power-query/  
  
✔️ Master Excel Step-by-Step-  
https://products.goodly.co.in/learn-excel/  
  
  
\===== LINKS 🔗 =====  
Blog 📰 - https://www.goodly.co.in/blog/  
Corporate Training 👨‍🏫 - https://www.goodly.co.in/training/  
Need my help on a Project 💻- https://www.goodly.co.in/consulting/  
Download the Practice File ⬇️ - https://www.goodly.co.in/secret-behind-professional-dashboards  
  
  
\===== TIMESTAMP 🕛 =====  
0:00 - Intro  
0:09 - Trick 1  
5:02 - Trick 2  
6:49 - Trick 3  
8:55 - Trick 4  
14:55 - Trick 5  
  
  
\===== CONTACT 🌐 =====  
Twitter - https://twitter.com/chandeep2786  
LinkedIn - https://www.linkedin.com/in/chandeepchhabra/  
Email - goodly.wordpress@gmail.com  
  
  
\===== WHO AM I? =====  
A lot of people think that my name is Goodly, it's NOT ;)  
My name is Chandeep. Goodly is my full-time venture where I share what I learn about Excel and Power BI.  
Please browse around, you'll find a ton of interesting videos that I have created :) Cheers!

## Transcript

### Intro

**0:00** · In this video, I'm going to talk about interesting slicer tricks that I believe that you could also benefit a lot from.

**0:08** · All right, fellas. The first trick is default selection in the slicers. What do I mean by that? Take a look. So, here I have like a mock dashboard, like a pseudo dashboard. It's not even close to a dashboard, but please take a look. So, we have like a chart here and a card visual here. And on the left we have a slicer. The slicer has been built off the calendar table. Currently I have the year and the month in the slicer. Now let's say for example the report goes through a refresh. The next month the April data kicks in. And at the moment right now we have set the month to be March.

### Trick 1

**0:40** · But you would want the dashboard to auto update to the month of April on the next refresh. How is that going to be possible? Well, what you can do is you can set up a clever trick and make sure that the refresh date is actually selected in the slicer by default. I'm going to give you a rough idea as to how do you make it work, whether you want to make it work in Power Query or you want to make it work in DAX. The idea is pretty much the same. Let's just go take a look. So, I'm going to hop over to my calendar table right here. Pretty standard calendar table. Couple of columns, date, month, year, and quarter.

**1:12** · And I would like to create one additional column right here. Let's just call this column as current month. And I first create a variable called the refresh date. This date could be today's date. This date could be the refresh date of your model. This date could be any date. For the moment, I'm just picking up 2001, the month of 10, and 1st of October. That's what I'm picking at the moment. Now, since I want that date to be formatted on in only the year and the month format, I have used a very simple format function right here.

**1:40** · And I'm actually formatting the refresh date in mmmmm and y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y y format order. Finally, I build a very simple check. In that check, all that I'm saying is that hey, why don't you pick up this particular date and for this particular date, you do the same formatting month and year and why don't you just check if that is equals to the format of the current date, the refresh date or not. If both the formats are matching, that means that we would like to be able to apply that month as default selected slicer.

**2:10** · And finally I write the return statement. And after the return statement I say that hey if this particular check that means the current date and the refresh a month year is the same. Then I would like to mark that as the current month. Otherwise just give me the month column which is this particular column. That's pretty much about it. Press enter and we are good to go. All right I'm back on my slicer and that's where I have the year and the month. But hey, this time from the slice of visual that we have, we would like to be able to remove this particular month as a column and get the column that we have created instead.

**2:40** · So I'm going to remove this. So I can go ahead and go right here and perhaps add the data and say that please I'd like to get the current month. Old habits do not go easy. Nevertheless, once we have the current month right here, you can see that the current month currently marked in our slicer is the current month right here, which is October at the moment.

**3:02** · Let's just go and go ahead and I'm going to go ahead in my calendar table and try to change my date. So I'm back at my calendar table and now if I say that the current month has changed. Obviously this is going to be automatically detected through the today's date or your refresh date or whatever that might be. At the moment I'm picking up this particular date as a manual date, but I'm sure you can have a workar around for this date to be either today's date or the model refresh date. For now, let's just change this date from the month of 10 to the month of 11, which is November.

**3:33** · And obviously, the current month has automatically changed. Now, the question is, if we go back to our visual, the dashboard should have automatically changed the current month from October to November. If I just go back and take a look at that, you can see that since I selected current month right here, October now has automatically been selected to the now current month, which is nothing but November. Now, this trick was obviously done in DAX. If you know the way to do that and if you set up calendar tables or date tables in Power Query, I'm sure you can figure out a way to do the same thing in Power Query as well. The logic remains the same.

**4:05** · All that you have to do is create another column to mark the current date or the refresh date to check against the calendar. You know what's the hardest thing about learning PowerBI? It is translation. The ability to translate the DAX logic or the M logic or data modeling into your own scenario, your own industry with your own data is really hard. And if you learn that, that is when you have truly learned how to use PowerBI into your own business setting.

**4:34** · And that is the reason why we are launching PowerBI case studies. These are case studies in HR, in logistics, in finance, in supply chain, every possible industry that you can imagine. We going to build a case study right from scratch. Understand the moving parts of that industry, how the data works, how the business logic works, and then how do you transform that into a working solution that you can implement into your own business setting. Apply all slices.

**5:01** · If you take a look at my visual right here, I have product and I have region and I have this matrix visual. Assume that the current visual is somehow very very slow. The queries are running very slow.

### Trick 2

**5:14** · So what I want to do is I want to have all the slicers applied first and then I want to see the effect of those slices sliced into my visuals. Well, how do I do that? How do I pause the slicers?

**5:24** · That's what I'm trying to say. So at the moment, if I just happen to click on a shampoo or a hair gel or a cream, the slicers get applied. But I don't really want to do that. I want to first apply all the slicers and then click on apply slicers. Well, there is a button to that. So, I'm going to go over to the insert tab. In the insert tab, I have the button right here. And I can click on the apply slicers button. And once I do that, I get this little button right here. And now, what I'm going to do is I'm going to start to apply the slicers.

**5:50** · And you're going to see that the table is not going to change. So, I click on Mumbai. I click on the therapy shampoo.

**5:55** · I click on the smoothe oil. So, all of these. And you can see that there is a little waiting icon next to every single slicer. That means these slicers are not applied yet. Now these are going to be applied only when I click on apply slices button and that is also highlighted and now the slicers are applied and you can see the change of that in the visual. This is very very helpful in case you are working with slower queries in your model. Well guess what there is also a clear slicers button available in PowerBI and you can do that to clear all the slicers off on the screen.

**6:26** · So I'm going to go over to the insert once again again in the buttons dropdown and pick up the clear slicers button. I get that. I can place that right here. Now, as soon as you click right here on this particular button, you're going to clear off all the slicers off from the screen and the visual is going to be absolutely unfiltered. I just click that and you can see that all the slices are gone and the visual is absolutely unfiltered. The fields parameter trick. I'm sure everybody has worked with fields parameter that lets you pick up a few columns of your choice and add them as a slicer.

### Trick 3

**6:55** · But did you know that you can also add the values of those columns as a slicer? Let me help you understand what am I trying to say. So let's just say that I have this simple table visual right here and I have the first column is year, month and then the total sales.

**7:08** · Now I would like to be able to slice this visual either by the channel or by the region. Both of these columns are there in my sales table. So if I just go take a look at my sales table, my region and my channel are two columns of my choice that I would like to place it as a slicer and that should appear in the slicer. So to do that I can obviously use something like a fields parameter.

**7:27** · So in the insert tab, in the modeling tab, sorry, I'm going to go to the new parameter and I'll say fields parameter.

**7:33** · And this is just going to be ask me to give a column name or a table name.

**7:36** · That's what I have done. And choose the columns that I would want. So the first column of my choice is channel. The second column of my choice is region. I do that. Add a slicer to this page.

**7:46** · Click on okay. And a slicer obviously gigantic one is added to the page. And I can push that off right here. Now obviously if I just happen to click, nothing is going to happen because this slicer is not there in the visual. So let's just add that. So I can just add the column slicer off to the visual right here and I can see all the regions if I happen to click on region or if I click on the channel. This is the standard stuff that everybody knows about. Now I would want to now add a secondary slicer which is where I want to take a look at the values of those channels underneath here in the slicer.

**8:20** · Well, you can do that. So I can just click on the slicer and ctrl + ctrl +v and now I can change the properties of the slicer right click on the columns and I can say that hey instead of the choice between the two columns which is channel or the region I would want to have the choice between the values of those columns. So I can say show values of the selected field. Click on that.

**8:39** · Now it is showing me the values in the channel column or the values in the region column and I can further filter down the values like that. This is pretty damn awesome.

**8:54** · Now the default behavior of the slicer is to slice or filter the data. But you can also use the slicer to be able to highlight instead. Take a look. What do I mean by that? Here I have a simple table setup. So we have the products name right here and we have the total sales. On the right hand side I have a slicer right here and I picked up a few products right here. As soon as I click the value in the slicer, the table doesn't get filtered. However, it gets highlighted instead. So if I were to just maybe pick up another product right here, I'm going to have four rows highlighted.

### Trick 4

**9:23** · If I maybe keep on picking up the products right here, it gets highlighted instead. This can be very helpful to highlight elements in a table or in fact even in bar charts or column charts. Let's just see how this is done.

**9:36** · All right, let's just start with the native table visual that we have which is the products and the total sales and a slicer which is on the products table.

**9:44** · So if you look at the data model right here, in the data model we have the products table. Obviously we have the calendar table and the sales table. Any filter that comes in from the products table right here will have the ability to filter out the sales table. That means it will filter not highlight. If I were to just go back to my visual and pick up any value right here, it's actually going to filter down my table and not highlight. To overcome this problem, what we need is a disconnected table. And using that disconnected table, we're going to make a slicer.

**10:16** · Let's just see how that is done. I'm going to go over to my data model right here. And on the right, I have kind of hidden this disconnected table, which I can place it right here. And if you take a look at the code for that disconnected table, it's very, very simple. All that I'm saying is that, hey, why don't you go over to the products table, which is this particular table. Go over to the products column, remove the blanks, and make a single column instead. and you will have the list of all the SKUs, all the product names right here.

**10:41** · Now, since this particular table is not connected with any other table, any filters or slicers applied on this column will not be able to filter the sales table. And that is nice. I'm going to go ahead and revise my slicer to contain the column from the disconnected table instead. So, I'm just go right here in the visual, remove this, add the data from the disconnected table, and put the product right in there. And once we have the product, obviously if you were to now click on any one of the products, it is not going to filter the sales table or the products table right here.

**11:13** · And that is nice. The second question comes is that at the moment the filter is not happening which is one problem that we overcame. But how do we then highlight it? How do we capture this particular value right here and make this value stand out in this table right here? For that we'll have to use conditional formatting and we'll have to write a measure and use it as a conditional formatting. Let's just go write that measure. I'm going to go over to the data and perhaps anywhere I can right click and I can say that I'd like to make a new measure. The name of the measure can be highlight and the code is reasonably logical.

**11:45** · So I'm going to write something like hey I'd like to filter filter which table filter my products table which is connected by the way. And in this particular table, what I'm trying to do is I'm trying to see that how many of these products are selected in this particular table or not. So I'm going to use a selected value function and selected value function of the products table and the product column which is the product name.

**12:09** · So essentially what I'm trying to do is I'm trying to check that if this particular product in the current filter context, the current selected product is that anywhere in the selected products in the slicer or not. And for that I'm going to use a very simple in function and I'm going to say hey why don't you check all the products which are there in this particular table the disconnected table this time. So products disconnected and the products and that is pretty good to go.

**12:33** · Now at the moment if you take a look I just cannot return this measure in the in the table right here because filter function returns a table and you can't really have a table in the table in the measure. So I'm going to maybe wrap this around in the count rows function. I'll say, "Hey, why don't you count the number of rows in the formula that is returned by this function?" Close the bracket and press enter. At the moment, if I return the measure over to my visual, I'm going to get something like this. Every product that happens to be selected in the slicer is marked with one.

**13:05** · That means yes, the products table is left with just one row of data if this particular bike wash dissolver is selected. Again in this particular filter context the products table is left with one row of data if this particular value is selected. So that's pretty easy to do. At the moment I can just make a very simple condition and the condition is something like this.

**13:24** · Why don't we check? So let's just give it this a variable. So variable is going to be check and I am going to say something like hey does the check contain any more than one rows of table or not? If that contains any more than one rows of table I can use a color to highlight. So I can say something like return and I can say hey if the check is

**13:41** · greater than equal to a one in that case why don't you just do something like an orange color else don't do any color press enter and this formula is already dragged at the moment I get the text as orange but I don't want the text as orange however I would want the color as orange I can remove this highlight from the visual right here and instead use the highlight in the conditional formatting I'm going to go over to the format in the format I'm going to go over to sell elements. In cell elements, I will activate the background color for total sales. Activate that. And here I'm going to use the FX to apply the color.

**14:15** · So total sales is going to be applied with a field value. And the field value is nothing but highlight. I will check at that. Click on okay. And that gets highlighted. But I'd like to highlight the entire row. So I need to pick up the second field as well. And again, I will switch that over to the name of the product, which is the first column right here. I'm going to activate the background color. Again, go over to the field values. pick up the highlight measure that I've written. Click on okay and that is highlighted. Now if you were to pick up any particular value right here or even multiple values they get highlighted instead.

**14:45** · The same technique can be used to highlight the bars of the bar chart or the column charts as well.

**14:51** · Once you know the technique you can apply it anywhere that you like. In the next trick I'm going to talk about that how can you set hierarchies while working with field parameters. I'm sure you have worked with field parameters in the past. incredibly great feature to natively select the measures in the slicer. Let's just take a look at what do I mean by setting up hierarchies. So I have this table right here and in the table I have the name of the product against that I have some stupid measures. So I have total sales which is not so stupid. Then we have pseudo sales commissions and some more commissions right here.

### Trick 5

**15:20** · Now the first two I would like to categorize them as my sales and the second two I'd like to categorize them as my earnings and for which I can obviously set up let's say a fields parameter. So I can just go in right here and I can go over to the insert tab. Where is that? Sorry modeling tab.

**15:37** · In the modeling tab I can click on new parameter and I can click on the fields parameter. In the fields parameter I can say that hey my parameter is going to be my KPI. That is the name and I can pick up all the four measures right here.

**15:49** · Once you've picked up all the four names, total sales, these are my measures, total sales, pseudo sales, commissions, and more commission. I can obviously check on add the slicer to the page, and click on create. And that is going to create a little slicer right here, which I can place it anywhere.

**16:02** · Once we have placed the slicer on the page for the slicer to have effect on this table, what we need to do is obviously pick up the element of the slicer and put that in the table. So for now if I just go to the table I have all of these four measures which I can remove from here and instead I can have the KPI that I have created which is nothing but the table. I can just place that table right here. Now that is nothing significant. I'm sure you know how to do that. And now the slicer takes an effect on the table.

**16:28** · But what instead I would like to show you that in case I need to mark the first two measures as like in a folder or something and I'd like to visually show that these are my sales measures and the last two measures are my earning measures. Then how can we do that? Now whenever you try to create a fields parameter you obviously get the table right here and the table has got these three default columns the KPI the KPI fields and the KPI order. This is dependent upon what you wrote in the fields parameter.

**16:55** · At the moment, if you take a look at this table, this table obviously is the first column is right here. That is nothing but the second column and that is nothing but the order which is not really visible. That is the third column. Now, nobody is stopping you from creating more columns in the table that we can instead use in the slicer. So if I were to just go ahead after the comma and say that this is nothing but my sales measure and perhaps copy that to the second row as well that is again my sales measure that is nothing but my earnings measure and I can copy that and that can also again be my earning measure.

**17:27** · Now as I do that you can see that we have a value four created which obviously we can rename that to a tag and now that tag can be used to categorize slicers further. I can just go over to my visual in the KPI. I can have like a hierarchy. I can just put that right here. And you're going to see that the tag is at the bottom which I can bring it up on the top and put the KPI at the bottom. And that is done. And you can see that now we have earning and within earning we have the commission and more commission.

**17:56** · And in the sales we have zero sales and the total sales. I can pick up anything to display that in my table. And that is a nice way to categorize your KPIs in case you would like to show them in a certain hierarchy or in a more folderized manner.