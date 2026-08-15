---
uid: 2026-08-11-5-power-bi-slicer-tricks-goodly
title: "Goodly - 5 Power BI Slicer Tricks"
source: "https://www.youtube.com/watch?v=sdyxtL1250E"
date: 2026-08-11
duration: 18:25
language: en
video_file: 99.System/Attachments/Video/5 Power BI Slicer Tricks To Build Professional Dashboards.mp4
tags: [video, goodly, power-bi, slicer]
created: 2026-08-11
---

# Goodly - 5 Power BI Slicer Tricks

![[5 Power BI Slicer Tricks To Build Professional Dashboards.mp4]]

## Transcript

[00:00:00.080] In this video, I'm going to talk about
[00:00:01.680] interesting slicer tricks that I believe
[00:00:04.000] that you could also benefit a lot from.
[00:00:08.880] All right, fellas. The first trick is
[00:00:10.800] default selection in the slicers. What
[00:00:13.759] do I mean by that? Take a look. So, here
[00:00:15.679] I have like a mock dashboard, like a
[00:00:17.680] pseudo dashboard. It's not even close to
[00:00:19.600] a dashboard, but please take a look. So,
[00:00:21.920] we have like a chart here and a card
[00:00:23.920] visual here. And on the left we have a
[00:00:26.080] slicer. The slicer has been built off
[00:00:28.080] the calendar table. Currently I have the
[00:00:30.640] year and the month in the slicer. Now
[00:00:32.800] let's say for example the report goes
[00:00:34.399] through a refresh. The next month the
[00:00:36.399] April data kicks in. And at the moment
[00:00:38.879] right now we have set the month to be
[00:00:40.640] March. But you would want the dashboard
[00:00:42.480] to auto update to the month of April on
[00:00:45.280] the next refresh. How is that going to
[00:00:47.840] be possible? Well, what you can do is
[00:00:49.440] you can set up a clever trick and make
[00:00:51.440] sure that the refresh date is actually
[00:00:54.160] selected in the slicer by default. I'm
[00:00:57.120] going to give you a rough idea as to how
[00:00:58.960] do you make it work, whether you want to
[00:01:00.559] make it work in Power Query or you want
[00:01:02.239] to make it work in DAX. The idea is
[00:01:04.239] pretty much the same. Let's just go take
[00:01:06.000] a look. So, I'm going to hop over to my
[00:01:07.840] calendar table right here. Pretty
[00:01:09.119] standard calendar table. Couple of
[00:01:10.479] columns, date, month, year, and quarter.
[00:01:12.880] And I would like to create one
[00:01:14.400] additional column right here. Let's just
[00:01:16.000] call this column as current month. And I
[00:01:18.560] first create a variable called the
[00:01:20.479] refresh date. This date could be today's
[00:01:22.320] date. This date could be the refresh
[00:01:24.000] date of your model. This date could be
[00:01:25.759] any date. For the moment, I'm just
[00:01:27.200] picking up 2001, the month of 10, and
[00:01:30.720] 1st of October. That's what I'm picking
[00:01:33.439] at the moment. Now, since I want that
[00:01:35.680] date to be formatted on in only the year
[00:01:38.079] and the month format, I have used a very
[00:01:40.000] simple format function right here. And
[00:01:42.000] I'm actually formatting the refresh date
[00:01:44.320] in mmmmm and y y y y y y y y y y y y y y
[00:01:45.840] y y y y y y y y y y y y y y y y y y y y
[00:01:46.000] y y y y y y y y y y y y y y y y y y y y
[00:01:46.079] y y y y y y y format order. Finally, I
[00:01:48.560] build a very simple check. In that
[00:01:50.640] check, all that I'm saying is that hey,
[00:01:52.720] why don't you pick up this particular
[00:01:54.320] date and for this particular date, you
[00:01:56.159] do the same formatting month and year
[00:01:58.159] and why don't you just check if that is
[00:02:00.240] equals to the format of the current
[00:02:02.159] date, the refresh date or not. If both
[00:02:04.079] the formats are matching, that means
[00:02:06.079] that we would like to be able to apply
[00:02:08.080] that month as default selected slicer.
[00:02:10.319] And finally I write the return
[00:02:11.920] statement. And after the return
[00:02:13.200] statement I say that hey if this
[00:02:14.640] particular check that means the current
[00:02:16.319] date and the refresh a month year is the
[00:02:19.360] same. Then I would like to mark that as
[00:02:22.000] the current month. Otherwise just give
[00:02:23.920] me the month column which is this
[00:02:25.520] particular column. That's pretty much
[00:02:26.800] about it. Press enter and we are good to
[00:02:28.959] go. All right I'm back on my slicer and
[00:02:31.120] that's where I have the year and the
[00:02:32.879] month. But hey, this time from the slice
[00:02:34.879] of visual that we have, we would like to
[00:02:36.800] be able to remove this particular month
[00:02:38.879] as a column and get the column that we
[00:02:40.959] have created instead. So I'm going to
[00:02:42.319] remove this. So I can go ahead and go
[00:02:46.640] right here and perhaps add the data and
[00:02:48.959] say that please I'd like to get the
[00:02:50.400] current month. Old habits do not go
[00:02:52.560] easy. Nevertheless, once we have the
[00:02:54.319] current month right here, you can see
[00:02:55.519] that the current month currently marked
[00:02:57.760] in our slicer is the current month right
[00:02:59.840] here, which is October at the moment.
[00:03:02.480] Let's just go and go ahead and I'm going
[00:03:05.760] to go ahead in my calendar table and try
[00:03:08.239] to change my date. So I'm back at my
[00:03:10.000] calendar table and now if I say that the
[00:03:12.319] current month has changed. Obviously
[00:03:14.159] this is going to be automatically
[00:03:16.000] detected through the today's date or
[00:03:17.760] your refresh date or whatever that might
[00:03:19.440] be. At the moment I'm picking up this
[00:03:21.280] particular date as a manual date, but
[00:03:23.360] I'm sure you can have a workar around
[00:03:25.360] for this date to be either today's date
[00:03:27.360] or the model refresh date. For now,
[00:03:29.120] let's just change this date from the
[00:03:30.720] month of 10 to the month of 11, which is
[00:03:33.440] November. And obviously, the current
[00:03:35.280] month has automatically changed. Now,
[00:03:36.879] the question is, if we go back to our
[00:03:38.959] visual, the dashboard should have
[00:03:41.120] automatically changed the current month
[00:03:43.040] from October to November. If I just go
[00:03:45.280] back and take a look at that, you can
[00:03:46.640] see that since I selected current month
[00:03:48.239] right here, October now has
[00:03:50.000] automatically been selected to the now
[00:03:52.080] current month, which is nothing but
[00:03:53.920] November. Now, this trick was obviously
[00:03:55.599] done in DAX. If you know the way to do
[00:03:57.439] that and if you set up calendar tables
[00:03:59.280] or date tables in Power Query, I'm sure
[00:04:01.280] you can figure out a way to do the same
[00:04:03.120] thing in Power Query as well. The logic
[00:04:05.920] remains the same. All that you have to
[00:04:07.439] do is create another column to mark the
[00:04:09.519] current date or the refresh date to
[00:04:12.000] check against the calendar. You know
[00:04:13.360] what's the hardest thing about learning
[00:04:14.879] PowerBI? It is translation. The ability
[00:04:18.239] to translate the DAX logic or the M
[00:04:21.519] logic or data modeling into your own
[00:04:23.919] scenario, your own industry with your
[00:04:26.240] own data is really hard. And if you
[00:04:29.040] learn that, that is when you have truly
[00:04:31.840] learned how to use PowerBI into your own
[00:04:34.720] business setting. And that is the reason
[00:04:37.520] why we are launching PowerBI case
[00:04:39.919] studies. These are case studies in HR,
[00:04:42.320] in logistics, in finance, in supply
[00:04:45.040] chain, every possible industry that you
[00:04:47.680] can imagine. We going to build a case
[00:04:49.520] study right from scratch. Understand the
[00:04:51.680] moving parts of that industry, how the
[00:04:53.520] data works, how the business logic
[00:04:55.360] works, and then how do you transform
[00:04:57.120] that into a working solution that you
[00:04:59.360] can implement into your own business
[00:05:01.840] setting. Apply all slices. If you take a
[00:05:04.320] look at my visual right here, I have
[00:05:06.080] product and I have region and I have
[00:05:07.600] this matrix visual. Assume that the
[00:05:10.000] current visual is somehow very very
[00:05:12.479] slow. The queries are running very slow.
[00:05:14.080] So what I want to do is I want to have
[00:05:15.840] all the slicers applied first and then I
[00:05:18.240] want to see the effect of those slices
[00:05:20.560] sliced into my visuals. Well, how do I
[00:05:22.960] do that? How do I pause the slicers?
[00:05:24.800] That's what I'm trying to say. So at the
[00:05:26.240] moment, if I just happen to click on a
[00:05:28.000] shampoo or a hair gel or a cream, the
[00:05:30.800] slicers get applied. But I don't really
[00:05:32.320] want to do that. I want to first apply
[00:05:33.680] all the slicers and then click on apply
[00:05:35.520] slicers. Well, there is a button to
[00:05:37.199] that. So, I'm going to go over to the
[00:05:38.880] insert tab. In the insert tab, I have
[00:05:40.800] the button right here. And I can click
[00:05:42.400] on the apply slicers button. And once I
[00:05:44.479] do that, I get this little button right
[00:05:46.479] here. And now, what I'm going to do is
[00:05:48.800] I'm going to start to apply the slicers.
[00:05:50.240] And you're going to see that the table
[00:05:51.199] is not going to change. So, I click on
[00:05:52.960] Mumbai. I click on the therapy shampoo.
[00:05:55.440] I click on the smoothe
[00:05:57.919] oil. So, all of these. And you can see
[00:05:59.520] that there is a little waiting icon next
[00:06:01.840] to every single slicer. That means these
[00:06:03.759] slicers are not applied yet. Now these
[00:06:06.639] are going to be applied only when I
[00:06:08.000] click on apply slices button and that is
[00:06:10.000] also highlighted and now the slicers are
[00:06:12.240] applied and you can see the change of
[00:06:13.919] that in the visual. This is very very
[00:06:15.919] helpful in case you are working with
[00:06:17.759] slower queries in your model. Well guess
[00:06:19.840] what there is also a clear slicers
[00:06:21.759] button available in PowerBI and you can
[00:06:23.919] do that to clear all the slicers off on
[00:06:26.240] the screen. So I'm going to go over to
[00:06:27.680] the insert once again again in the
[00:06:29.280] buttons dropdown and pick up the clear
[00:06:31.520] slicers button. I get that. I can place
[00:06:33.280] that right here. Now, as soon as you
[00:06:34.639] click right here on this particular
[00:06:36.319] button, you're going to clear off all
[00:06:37.919] the slicers off from the screen and the
[00:06:40.080] visual is going to be absolutely
[00:06:41.520] unfiltered. I just click that and you
[00:06:43.360] can see that all the slices are gone and
[00:06:45.039] the visual is absolutely unfiltered. The
[00:06:47.840] fields parameter trick. I'm sure
[00:06:49.680] everybody has worked with fields
[00:06:51.120] parameter that lets you pick up a few
[00:06:53.360] columns of your choice and add them as a
[00:06:55.840] slicer. But did you know that you can
[00:06:57.440] also add the values of those columns as
[00:06:59.599] a slicer? Let me help you understand
[00:07:01.360] what am I trying to say. So let's just
[00:07:02.720] say that I have this simple table visual
[00:07:04.720] right here and I have the first column
[00:07:06.160] is year, month and then the total sales.
[00:07:08.000] Now I would like to be able to slice
[00:07:10.080] this visual either by the channel or by
[00:07:13.120] the region. Both of these columns are
[00:07:14.720] there in my sales table. So if I just go
[00:07:16.319] take a look at my sales table, my region
[00:07:18.240] and my channel are two columns of my
[00:07:20.400] choice that I would like to place it as
[00:07:22.000] a slicer and that should appear in the
[00:07:23.840] slicer. So to do that I can obviously
[00:07:25.520] use something like a fields parameter.
[00:07:27.520] So in the insert tab, in the modeling
[00:07:29.120] tab, sorry, I'm going to go to the new
[00:07:31.120] parameter and I'll say fields parameter.
[00:07:33.199] And this is just going to be ask me to
[00:07:35.039] give a column name or a table name.
[00:07:36.720] That's what I have done. And choose the
[00:07:38.400] columns that I would want. So the first
[00:07:40.000] column of my choice is channel. The
[00:07:41.919] second column of my choice is region. I
[00:07:44.479] do that. Add a slicer to this page.
[00:07:46.160] Click on okay. And a slicer obviously
[00:07:48.240] gigantic one is added to the page. And I
[00:07:50.800] can push that off right here. Now
[00:07:52.240] obviously if I just happen to click,
[00:07:53.759] nothing is going to happen because this
[00:07:55.199] slicer is not there in the visual. So
[00:07:56.960] let's just add that. So I can just add
[00:07:58.560] the column slicer off to the visual
[00:08:01.440] right here and I can see all the regions
[00:08:04.400] if I happen to click on region or if I
[00:08:06.639] click on the channel. This is the
[00:08:08.319] standard stuff that everybody knows
[00:08:09.840] about. Now I would want to now add a
[00:08:13.280] secondary slicer which is where I want
[00:08:15.840] to take a look at the values of those
[00:08:18.000] channels underneath here in the slicer.
[00:08:20.400] Well, you can do that. So I can just
[00:08:21.919] click on the slicer and ctrl + ctrl +v
[00:08:24.240] and now I can change the properties of
[00:08:26.240] the slicer right click on the columns
[00:08:27.840] and I can say that hey instead of the
[00:08:29.520] choice between the two columns which is
[00:08:31.199] channel or the region I would want to
[00:08:33.360] have the choice between the values of
[00:08:35.599] those columns. So I can say show values
[00:08:37.680] of the selected field. Click on that.
[00:08:39.279] Now it is showing me the values in the
[00:08:41.440] channel column or the values in the
[00:08:44.080] region column and I can further filter
[00:08:46.320] down the values like that. This is
[00:08:48.560] pretty damn awesome.
[00:08:54.560] Now the default behavior of the slicer
[00:08:57.279] is to slice or filter the data. But you
[00:09:00.000] can also use the slicer to be able to
[00:09:02.000] highlight instead. Take a look. What do
[00:09:04.000] I mean by that? Here I have a simple
[00:09:05.839] table setup. So we have the products
[00:09:07.760] name right here and we have the total
[00:09:09.680] sales. On the right hand side I have a
[00:09:11.120] slicer right here and I picked up a few
[00:09:12.720] products right here. As soon as I click
[00:09:14.399] the value in the slicer, the table
[00:09:16.800] doesn't get filtered. However, it gets
[00:09:18.640] highlighted instead. So if I were to
[00:09:20.240] just maybe pick up another product right
[00:09:21.920] here, I'm going to have four rows
[00:09:23.440] highlighted. If I maybe keep on picking
[00:09:25.360] up the products right here, it gets
[00:09:27.440] highlighted instead. This can be very
[00:09:29.279] helpful to highlight elements in a table
[00:09:32.080] or in fact even in bar charts or column
[00:09:34.640] charts. Let's just see how this is done.
[00:09:36.560] All right, let's just start with the
[00:09:38.640] native table visual that we have which
[00:09:40.560] is the products and the total sales and
[00:09:42.480] a slicer which is on the products table.
[00:09:44.880] So if you look at the data model right
[00:09:46.480] here, in the data model we have the
[00:09:48.640] products table. Obviously we have the
[00:09:50.560] calendar table and the sales table. Any
[00:09:52.640] filter that comes in from the products
[00:09:55.200] table right here will have the ability
[00:09:58.080] to filter out the sales table. That
[00:10:00.240] means it will filter not highlight. If I
[00:10:03.120] were to just go back to my visual and
[00:10:04.959] pick up any value right here, it's
[00:10:06.880] actually going to filter down my table
[00:10:08.480] and not highlight. To overcome this
[00:10:10.399] problem, what we need is a disconnected
[00:10:12.399] table. And using that disconnected
[00:10:14.480] table, we're going to make a slicer.
[00:10:16.160] Let's just see how that is done. I'm
[00:10:17.680] going to go over to my data model right
[00:10:19.360] here. And on the right, I have kind of
[00:10:21.839] hidden this disconnected table, which I
[00:10:24.399] can place it right here. And if you take
[00:10:26.240] a look at the code for that disconnected
[00:10:27.920] table, it's very, very simple. All that
[00:10:30.079] I'm saying is that, hey, why don't you
[00:10:31.839] go over to the products table, which is
[00:10:33.839] this particular table. Go over to the
[00:10:35.519] products column, remove the blanks, and
[00:10:37.839] make a single column instead. and you
[00:10:39.839] will have the list of all the SKUs, all
[00:10:41.519] the product names right here. Now, since
[00:10:43.040] this particular table is not connected
[00:10:44.800] with any other table, any filters or
[00:10:47.600] slicers applied on this column will not
[00:10:50.880] be able to filter the sales table. And
[00:10:53.120] that is nice. I'm going to go ahead and
[00:10:54.800] revise my slicer to contain the column
[00:10:56.959] from the disconnected table instead. So,
[00:10:58.399] I'm just go right here in the visual,
[00:11:00.160] remove this, add the data from the
[00:11:02.399] disconnected table, and put the product
[00:11:04.399] right in there. And once we have the
[00:11:05.839] product, obviously if you were to now
[00:11:07.519] click on any one of the products, it is
[00:11:09.920] not going to filter the sales table or
[00:11:13.279] the products table right here. And that
[00:11:15.200] is nice. The second question comes is
[00:11:17.440] that at the moment the filter is not
[00:11:19.360] happening which is one problem that we
[00:11:21.360] overcame. But how do we then highlight
[00:11:23.279] it? How do we capture this particular
[00:11:25.440] value right here and make this value
[00:11:27.760] stand out in this table right here? For
[00:11:30.720] that we'll have to use conditional
[00:11:32.000] formatting and we'll have to write a
[00:11:33.279] measure and use it as a conditional
[00:11:34.959] formatting. Let's just go write that
[00:11:36.240] measure. I'm going to go over to the
[00:11:37.839] data and perhaps anywhere I can right
[00:11:39.920] click and I can say that I'd like to
[00:11:41.120] make a new measure. The name of the
[00:11:42.399] measure can be highlight and the code is
[00:11:45.120] reasonably logical. So I'm going to
[00:11:46.800] write something like hey I'd like to
[00:11:48.480] filter filter which table filter my
[00:11:50.880] products table which is connected by the
[00:11:52.880] way. And in this particular table, what
[00:11:54.959] I'm trying to do is I'm trying to see
[00:11:56.399] that how many of these products are
[00:12:00.079] selected in this particular table or
[00:12:02.399] not. So I'm going to use a selected
[00:12:04.000] value function and selected value
[00:12:05.839] function of the products table and the
[00:12:08.160] product column which is the product
[00:12:09.760] name. So essentially what I'm trying to
[00:12:11.440] do is I'm trying to check that if this
[00:12:13.839] particular product in the current filter
[00:12:15.600] context, the current selected product is
[00:12:17.519] that anywhere in the selected products
[00:12:20.079] in the slicer or not. And for that I'm
[00:12:22.160] going to use a very simple in function
[00:12:24.320] and I'm going to say hey why don't you
[00:12:25.760] check all the products which are there
[00:12:27.920] in this particular table the
[00:12:29.760] disconnected table this time. So
[00:12:31.040] products disconnected and the products
[00:12:33.120] and that is pretty good to go. Now at
[00:12:35.279] the moment if you take a look I just
[00:12:37.519] cannot return this measure in the in the
[00:12:40.399] table right here because filter function
[00:12:41.920] returns a table and you can't really
[00:12:43.360] have a table in the table in the
[00:12:45.040] measure. So I'm going to maybe wrap this
[00:12:46.639] around in the count rows function. I'll
[00:12:48.720] say, "Hey, why don't you count the
[00:12:49.920] number of rows in the formula that is
[00:12:52.399] returned by this function?" Close the
[00:12:54.560] bracket and press enter. At the moment,
[00:12:56.240] if I return the measure over to my
[00:12:57.920] visual, I'm going to get something like
[00:12:59.760] this. Every product that happens to be
[00:13:01.839] selected in the slicer is marked with
[00:13:05.360] one. That means yes, the products table
[00:13:07.519] is left with just one row of data if
[00:13:09.760] this particular bike wash dissolver is
[00:13:11.920] selected. Again in this particular
[00:13:13.519] filter context the products table is
[00:13:15.519] left with one row of data if this
[00:13:17.760] particular value is selected. So that's
[00:13:19.360] pretty easy to do. At the moment I can
[00:13:21.120] just make a very simple condition and
[00:13:23.040] the condition is something like this.
[00:13:24.720] Why don't we check? So let's just give
[00:13:25.920] it this a variable. So variable is going
[00:13:27.600] to be check and I am going to say
[00:13:29.760] something like hey does the check
[00:13:31.440] contain any more than one rows of table
[00:13:33.360] or not? If that contains any more than
[00:13:34.959] one rows of table I can use a color to
[00:13:36.880] highlight. So I can say something like
[00:13:38.320] return and I can say hey if the check is
[00:13:41.920] greater than equal to a one in that case
[00:13:44.320] why don't you just do something like an
[00:13:45.920] orange color else don't do any color
[00:13:48.720] press enter and this formula is already
[00:13:50.639] dragged at the moment I get the text as
[00:13:52.560] orange but I don't want the text as
[00:13:53.839] orange however I would want the color as
[00:13:56.160] orange I can remove this highlight from
[00:13:58.720] the visual right here and instead use
[00:14:00.720] the highlight in the conditional
[00:14:02.560] formatting I'm going to go over to the
[00:14:04.480] format in the format I'm going to go
[00:14:06.399] over to sell elements. In cell elements,
[00:14:09.040] I will activate the background color for
[00:14:11.199] total sales. Activate that. And here I'm
[00:14:13.680] going to use the FX to apply the color.
[00:14:15.680] So total sales is going to be applied
[00:14:18.079] with a field value. And the field value
[00:14:20.240] is nothing but highlight. I will check
[00:14:21.920] at that. Click on okay. And that gets
[00:14:23.680] highlighted. But I'd like to highlight
[00:14:24.880] the entire row. So I need to pick up the
[00:14:26.320] second field as well. And again, I will
[00:14:28.160] switch that over to the name of the
[00:14:29.519] product, which is the first column right
[00:14:30.880] here. I'm going to activate the
[00:14:32.399] background color. Again, go over to the
[00:14:34.399] field values. pick up the highlight
[00:14:36.639] measure that I've written. Click on okay
[00:14:38.560] and that is highlighted. Now if you were
[00:14:40.880] to pick up any particular value right
[00:14:42.639] here or even multiple values they get
[00:14:45.040] highlighted instead. The same technique
[00:14:47.199] can be used to highlight the bars of the
[00:14:49.519] bar chart or the column charts as well.
[00:14:51.519] Once you know the technique you can
[00:14:52.800] apply it anywhere that you like. In the
[00:14:54.800] next trick I'm going to talk about that
[00:14:56.160] how can you set hierarchies while
[00:14:58.560] working with field parameters. I'm sure
[00:15:00.560] you have worked with field parameters in
[00:15:02.000] the past. incredibly great feature to
[00:15:04.240] natively select the measures in the
[00:15:07.279] slicer. Let's just take a look at what
[00:15:09.120] do I mean by setting up hierarchies. So
[00:15:10.880] I have this table right here and in the
[00:15:12.480] table I have the name of the product
[00:15:14.079] against that I have some stupid
[00:15:15.440] measures. So I have total sales which is
[00:15:17.040] not so stupid. Then we have pseudo sales
[00:15:19.040] commissions and some more commissions
[00:15:20.480] right here. Now the first two I would
[00:15:22.639] like to categorize them as my sales and
[00:15:25.839] the second two I'd like to categorize
[00:15:27.839] them as my earnings and for which I can
[00:15:30.399] obviously set up let's say a fields
[00:15:32.079] parameter. So I can just go in right
[00:15:33.839] here and I can go over to the insert
[00:15:35.600] tab. Where is that? Sorry modeling tab.
[00:15:37.440] In the modeling tab I can click on new
[00:15:39.120] parameter and I can click on the fields
[00:15:41.040] parameter. In the fields parameter I can
[00:15:43.040] say that hey my parameter is going to be
[00:15:44.880] my KPI. That is the name and I can pick
[00:15:47.519] up all the four measures right here.
[00:15:49.120] Once you've picked up all the four
[00:15:50.480] names, total sales, these are my
[00:15:51.920] measures, total sales, pseudo sales,
[00:15:53.759] commissions, and more commission. I can
[00:15:55.519] obviously check on add the slicer to the
[00:15:57.279] page, and click on create. And that is
[00:15:59.279] going to create a little slicer right
[00:16:00.959] here, which I can place it anywhere.
[00:16:02.720] Once we have placed the slicer on the
[00:16:05.199] page for the slicer to have effect on
[00:16:07.839] this table, what we need to do is
[00:16:09.600] obviously pick up the element of the
[00:16:11.120] slicer and put that in the table. So for
[00:16:13.040] now if I just go to the table I have all
[00:16:14.880] of these four measures which I can
[00:16:16.240] remove from here and instead I can have
[00:16:18.399] the KPI that I have created which is
[00:16:20.399] nothing but the table. I can just place
[00:16:22.480] that table right here. Now that is
[00:16:24.959] nothing significant. I'm sure you know
[00:16:26.720] how to do that. And now the slicer takes
[00:16:28.560] an effect on the table. But what instead
[00:16:30.720] I would like to show you that in case I
[00:16:33.120] need to mark the first two measures as
[00:16:35.839] like in a folder or something and I'd
[00:16:37.920] like to visually show that these are my
[00:16:39.680] sales measures and the last two measures
[00:16:41.839] are my earning measures. Then how can we
[00:16:43.759] do that? Now whenever you try to create
[00:16:45.360] a fields parameter you obviously get the
[00:16:47.360] table right here and the table has got
[00:16:49.199] these three default columns the KPI the
[00:16:51.440] KPI fields and the KPI order. This is
[00:16:53.279] dependent upon what you wrote in the
[00:16:55.440] fields parameter. At the moment, if you
[00:16:56.959] take a look at this table, this table
[00:16:58.720] obviously is the first column is right
[00:17:00.880] here. That is nothing but the second
[00:17:02.800] column and that is nothing but the order
[00:17:05.120] which is not really visible. That is the
[00:17:06.959] third column. Now, nobody is stopping
[00:17:08.799] you from creating more columns in the
[00:17:10.559] table that we can instead use in the
[00:17:12.319] slicer. So if I were to just go ahead
[00:17:14.319] after the comma and say that this is
[00:17:15.919] nothing but my sales measure and perhaps
[00:17:17.919] copy that to the second row as well that
[00:17:20.640] is again my sales measure that is
[00:17:22.880] nothing but my earnings measure and I
[00:17:25.280] can copy that and that can also again be
[00:17:27.679] my earning measure. Now as I do that you
[00:17:30.000] can see that we have a value four
[00:17:31.760] created which obviously we can rename
[00:17:33.280] that to a tag and now that tag can be
[00:17:36.160] used to categorize slicers further. I
[00:17:38.240] can just go over to my visual in the
[00:17:39.919] KPI. I can have like a hierarchy. I can
[00:17:42.400] just put that right here. And you're
[00:17:44.160] going to see that the tag is at the
[00:17:45.679] bottom which I can bring it up on the
[00:17:47.440] top and put the KPI at the bottom. And
[00:17:49.919] that is done. And you can see that now
[00:17:52.480] we have earning and within earning we
[00:17:54.640] have the commission and more commission.
[00:17:56.480] And in the sales we have zero sales and
[00:17:59.120] the total sales. I can pick up anything
[00:18:00.960] to display that in my table. And that is
[00:18:03.600] a nice way to categorize your KPIs in
[00:18:06.240] case you would like to show them in a
[00:18:07.600] certain hierarchy or in a more
[00:18:09.600] folderized manner.
