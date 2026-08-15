---
uid: 2023-02-15-level-up-custom-visuals-power-bi
title: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
source: ""
date: 2023-02-15
duration: 46:49
language: en
video_file: 99.System/Attachments/Video/LEVEL UP with Custom Visuals： Power BI🔹HTML🔹Calculation Groups🔹Deneb-QXMMpabHPS4.webm
tags: [video, power-bi, html-visual, calculation-groups, deneb, custom-visuals]
created: 2026-08-13
---

# Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb

![[LEVEL UP with Custom Visuals： Power BI🔹HTML🔹Calculation Groups🔹Deneb-QXMMpabHPS4.webm]]

## Transcript

[00:00:00.000] Hi everyone, welcome.
[00:00:05.920] My name is Injay and thanks for joining me today on my presentation.
[00:00:09.760] I'm going to be talking a little bit about some custom visualizations and niche techniques in Power BI today.
[00:00:19.840] I'm going to be talking about three main things: HTML visuals, calculation groups, and Deneb.
[00:00:29.760] I want to warn you in advance that this presentation plays like a tutorial, so it will get very technical.
[00:00:36.800] So let's dive right into the first topic, which is going to be HTML visuals in Power BI.
[00:00:45.440] I'm going to be covering fonts, themes, and icons.
[00:00:52.320] This is a little what the end result could look like.
[00:00:57.280] Everything on this page is an HTML visual, including the text itself.
[00:01:02.720] We're looking at fonts first, so I'm going to show you that if I select a text and open up the filters pane, you can see there are three different filters.
[00:01:15.680] One is going to allow me to change the font into basically anything I would like it to show.
[00:01:22.400] There's a thousand four hundred of these fonts.
[00:01:26.720] I'm also going to be able to change the font size.
[00:01:31.840] And I'm going to be able to change the color of the font.
[00:01:37.280] So if I want it to be black, I can do that. If I want it to be a gradient, I can do that as well.
[00:01:44.640] And you know, if I wanted to be a single color, I can change that as well, which I'll show you a little bit more later on in the presentation.
[00:01:57.920] This is the main DAX formula that I've been using, and I'm going to walk you through how it actually works.
[00:02:05.760] The first thing to understand is that this is a calculation group, and that's how the filter functionality actually occurs.
[00:02:15.040] To create calculation groups, you're going to need to have the external tool Tabular Editor.
[00:02:22.080] You need to download it online, and once you've downloaded it, you can open it directly from Power BI from the external tools tab.
[00:02:32.480] Once you have the Tabular Editor open, if you click on the table folder, you can create a new calculation group just by right-clicking.
[00:02:42.720] And from the calculation group, you can basically right-click again in order to create a new calculation item, which will allow you to type in the actual code that you want for the calculation group right in the Tabular Editor external tool.
[00:03:05.280] Going back to the DAX, the key thing here to note is that we're actually using the Google API to bring in the HTML and the font into this HTML.
[00:03:16.320] But there's a couple of things that we need to do in order to make this dynamic and adjustable using the filters, which is why we have these three variables.
[00:03:28.480] So let's take a look.
[00:03:32.000] The first variable is the actual text that we want to show. It's encapsulated in the measure, which is what you usually use to put text into something like a card.
[00:03:42.400] You can change this measure itself outside in order to modify what text you'd like to show.
[00:03:49.120] You can also see that it's been altered to be formatted as text.
[00:03:56.000] The second variable is the actual name of the font.
[00:04:00.640] Logically, if you want to have a number of different names in a filter, you're going to have to have that within Power BI somewhere.
[00:04:09.600] This is the developer Google Font API, which is the web page you need to go to in order for this to happen.
[00:04:18.560] On that page, once you scroll down a little bit, it has this area with a button that says "Get a Key," which you can simply click, and it will generate an API key that you can use.
[00:04:31.520] You're going to need this API key because this is the URL that you're going to input into Power BI, and it won't work unless you have a valid API key.
[00:04:43.360] Once you've created an API key from Google, you can simply replace this colored text in this URL.
[00:04:51.200] With the actual API key that you've generated, and it's going to be something that you use in Power BI to get the data.
[00:04:59.840] Simply select Get Data within Power BI, select the Web option, and paste the URL into the wizard box that you get.
[00:05:15.040] Once you hit OK, what it's going to show is this table where basically it has a lot of different units from the API itself.
[00:05:24.480] But all you need is the second column, the one that's called items.family.
[00:05:31.200] You don't need anything else, so I usually tend to remove all of the other columns.
[00:05:38.080] And I rename the column name to Font Name or something like that, and I'll rename the table itself to something like Google Fonts.
[00:05:50.240] As you can see, the actual second variable is the selected font.
[00:05:56.320] So I do create another measure that will simply be something like SelectedValue of the column that I still have.
[00:06:08.480] And then we have our third variable, which is simply a numeric parameter from the Modeling tab in Power BI.
[00:06:18.240] You can see that I've just created a numeric range from 0 to 100 with an increment of one.
[00:06:26.720] 100 means that the maximum font size is up to 100, but if you wanted to have larger font sizes, all you would need to do is change the maximum value to something much larger.
[00:06:39.520] You can also see that in the actual DAX measure, it's been formatted as text but also has the PX value right after it, so that it will indicate that it fits like 100 pixels or something like that. That's what the PX stands for.
[00:07:04.000] Now, we've gone through the variables, but I also want you to know that you don't necessarily need to have all of these steps in order to have a nice custom font for some text in your Power BI.
[00:07:15.040] If you want to be able to have just some static text, you don't need the API key, you don't need this numeric parameter, and you can have the text value even right in the measure itself.
[00:07:30.080] So I've shown that here. You can just put in the text value for the first variable, the name of the font you'd like to use for the second variable, and the font size.
[00:07:42.400] I've made a mistake here. You need to put in the PX to make sure that that works.
[00:07:48.640] But once you've put that value in, you can use this measure the same way I'm about to show you how to use the previous measure in order to get that custom font in your Power BI.
[00:08:08.640] Now, before we go further, I also want to talk about colors. Right now, this code that I've been showing you only works in black, and that's because the color value here is static and it only shows black at the moment.
[00:08:22.880] That wasn't enough for me, so I created a couple of more calculation items for the calculation group with some small adjustments.
[00:08:32.000] This is the first one where I have a color variable that is simply a measure that I will show later on that is inputting a specific color into this HTML code.
[00:08:46.400] The color itself can be RGB, it can be a named value. I think hex codes also work, but I'll show a little bit more of that in just a second.
[00:08:56.960] And then, because I as a person really love gradients, I created another calculation item in the calculation group in order to show two used in order to use two different colors to create a gradient.
[00:09:12.800] So you can see like, highlighted in the red boxes, is the extra bit of code that I added to make this happen.
[00:09:25.600] Now, the last piece of the puzzle is that you're going to need an HTML custom visual.
[00:09:33.600] There's a lot of different HTML custom visuals you can choose, and you can get them by simply clicking the "Get More Visuals" button from the visualizations pane, which will open the App Source.
[00:09:46.400] In the App Store, simply search for HTML, and there's a whole bunch of them out there.
[00:09:53.760] I use this one, HTML Content by Daniel Marsh Patrick, because he also created Deneb.
[00:10:02.400] But I understand there's some other ones where you could put in CSS separate from the HTML.
[00:10:10.400] Honestly, I'm not very good with HTML at all. This is probably one of the first pieces of HTML code that I created, and I don't know how to use CSS at all, basically.
[00:10:22.720] So that wasn't too useful for me, but if this is something for you, definitely check out the different options as well.
[00:10:32.320] And it's all together by first placing an HTML custom visual into the Power BI report, and then you want to put in the actual value of the text.
[00:10:43.520] So this is what would be the first variable into the values of the HTML custom visual.
[00:10:50.880] This is what I showed earlier. It said "This is text," and it's just that first variable that you put into the values.
[00:10:59.840] And in order to get this Dynamic effect, basically what you're going to want to do is simply put in a couple of filters into the filters pane for the specific visual.
[00:11:13.440] You need to put in the font, which is the Google Font table that you created.
[00:11:19.520] You're going to need to put in the numeric parameter so that it can alter the font size.
[00:11:26.720] And then you're going to have to put in the column for the calculation group, which I haven't changed, so it's the default name.
[00:11:35.840] This will alter how you actually select the colors.
[00:11:41.440] This is once again the report, and if we select this value again, open up the filters, you can see that we have the fonts, we have the color, we have the font size.
[00:11:54.560] And if I have the color font selected, I can select any specific color, and it will change the text into something else.
[00:12:02.720] So I have currently Blues selected, but I can exit out of Blues and put in any color that I would like the text to be.
[00:12:12.640] I can also change my settings so that if I wanted to change this color using RGBs, then I can absolutely do that.
[00:12:21.440] So I've got a slider for red, green, and blue, and I can change what the color is going to look like in this way.
[00:12:35.520] The text itself, of course, if I want to have a gradient, then it'll use both the primary and secondary to create a gradient.
[00:12:45.120] And if I want it just to be black, I can do that as well.
[00:12:53.600] So, from talking about the actual text itself, the font, and how we use this dynamic cosmetic way to alter the colors and the size, instead, I'm going to start talking about everything else on this page.
[00:13:09.600] Everything else on this page is also part of what I would call the theme, and I'm going to talk about how HTML can be used to create this dynamic theme that you're seeing.
[00:13:23.360] So if I'm changing colors, you can see not only is the text changing, but the icons and the border as well.
[00:13:32.640] But let's focus on the border for now. So I want to give praise where praise is due.
[00:13:39.200] A lot of this was built upon this idea that Flavio Meneses — I really hope I'm pronouncing that correctly — this is based on Flavio's work where he created a report that uses exactly this concept of red, green, and blue sliders in order to affect what color should be used on the theme itself.
[00:14:02.560] And the way that it works is that there are essentially three different numeric parameters: one for red, one for blue, one for green, from zero to 255, which is the maximum for the color setting in RGB.
[00:14:18.560] Having these three different parameters, you would need a measure to bring those parameters together, and from the selected values, actually bring them together to create a text like this one that you see here.
[00:14:38.560] This is really, really cool, but I also thought, you know, as I thought that maybe you can use something else, and it turns out in HTML you can put the name of certain colors, and HTML will recognize that text itself.
[00:14:52.480] So I found a table online that had a couple of these HTML colored names, and I simply inserted them into Power BI as a table.
[00:15:03.680] I had to do this manually with copying the web page and pasting it into the manual entry for Power BI, but I got it in there all the same.
[00:15:16.000] So something that I already mentioned is that I do love gradients, and I wanted to expand a little bit on Flavio's work.
[00:15:25.280] So I wanted to have gradients, but I also wanted to have a background color, and that meant I needed three separate colors for three different sets of RGBs, and that in itself was nine different parameters.
[00:15:40.320] But I also wanted to have specific colors that you could choose to be named, and that meant three different tables.
[00:15:49.440] So I'm going to put it out there that this is maybe not a technique you want to copy for business purposes.
[00:15:56.320] It's just something to showcase the kind of things you can do in a custom tool, but this is probably more effort than it's worth for most people.
[00:16:08.640] Now, that I had two different ways of being able to input colors — so I had the RGB and then I had the name — I needed a way for Power BI to understand which one to use.
[00:16:22.240] So I created a table that had just these two values: RGB, a name, and a measure for the actual color that would, based on which value was selected, simply use a Switch function to input either the RGB value or the named color value.
[00:16:49.280] So let's take a look at the actual HTML code and how these parameters actually are being used.
[00:16:57.760] So like I mentioned, this was one of the first HTML codes that I wrote, and when I say "wrote," I mean I Googled different parts of it until I managed to splice something together that worked.
[00:17:13.760] So this part here, which is the variable for the color itself, is what defines the color.
[00:17:20.960] And you can actually see that there's a gradient for color one and color two, and there's another value which is the parameter color percentage value, which is another numeric parameter from 0 to 100 to indicate how much color exists for color one in comparison to color two.
[00:17:40.480] So I'm going to show you that in the report in just a second, and you'll understand immediately what it is.
[00:17:49.600] And what that code actually is, is this outer border right here.
[00:17:55.680] It's actually this outer border, and you can only see this border. The border actually comes from the fact that we have one color in the background, and then we have another HTML visual on top of it to create this border-like feeling.
[00:18:18.240] A little bit more about how the input was created: I needed a way to differentiate because I had two different methods of inputting what color to use — the named color method and the RGB method.
[00:18:32.640] So the way that I decided to do it was using bookmarks.
[00:18:38.080] Basically, by clicking the plus, you could navigate to this one, and from here, pressing the minus would navigate back into this one.
[00:18:47.360] And that's basically the way that I decided to do it.
[00:18:52.480] I wanted to have some smaller UI elements to make it a little bit simpler.
[00:18:58.240] Like, for example, the border is the color that has been selected.
[00:19:04.640] And the buttons here at the top also show what color is being used.
[00:19:10.400] You can even see that there is a parameter color percentage, which is that other numeric parameter that I was talking about.
[00:19:18.560] And even one more: this Hue is also something based on Flavio's work, which allows me to have the background be a single monotone color with one color selected and a lighter color depending on this value.
[00:19:36.480] And you can see that right here. So if I select the parameter color to be slightly different — maybe I should change the secondary color to something more visible.
[00:19:46.400] So if I have the color be in this format, you can actually see that if I change the parameter color percentage, you can see that the level of the gradient alters depending on what value it is.
[00:20:05.280] I had to restart my Power BI presentation. If you have a Power BI embedded in your PowerPoint, sometimes PowerPoint can decide that it doesn't recognize your credentials anymore, so I had to re-log in and restart everything.
[00:20:21.280] OK, so you can see that the parameter color alters what level of color of the primary and secondary color there is.
[00:20:35.680] And of course, if you click on this minus or plus, what is happening is that there is a hidden slicer, depending on the bookmark, that will indicate whether or not it is an RGB bookmark or a named color bookmark, and thereby change the selection of how the colors are currently being used.
[00:20:59.200] So this is something that I really enjoy, and that basically covers how I would use HTML within themes.
[00:21:09.760] And here's a little bit of what the Hue might look like as well, changing the colors a little bit, all of the gradient in the back.
[00:21:19.360] But this code in itself is not something strictly used for just say colors.
[00:21:26.560] You can actually see as I'm working that the icons themselves are changing.
[00:21:33.120] So that's where we're going to go to next: talking about icons.
[00:21:39.040] And the way that it works is that this variable for color is directly affecting what the color settings are for the HTML visual.
[00:21:51.200] But the HTML visual shape itself is simply being decided by what's in this red box, and what's in this red box is simply a rectangle with slightly rounded corner values.
[00:22:06.400] So that means that the idea for the icons is: if we change this specific text to be something else — to be an SVG, for example — then we can have icons that are dynamically changing color.
[00:22:22.880] So I'm going to tell you about how I do icons in Power BI from the very beginning.
[00:22:30.240] I like to use this website, Remix Icon, for two reasons.
[00:22:36.640] The first is that you can use this website to download 2,271 icons in one go, which is really nice and very convenient.
[00:22:46.080] I'm actually going to use this for a very specific reason, which you'll see in just a second.
[00:22:52.160] But I also like the fact that it's free to use, and as long as you don't necessarily have to mention them, but they're grateful if you do.
[00:23:02.240] I think it's wonderful that open source icons like this do exist for people to be able to use.
[00:23:10.240] Once you've downloaded the actual pack and you've unzipped it, what you're going to want to do is you're going to want to Get Data in the Folder option.
[00:23:21.280] Once you do that and you select the folder that you downloaded from Remix Icon, you're going to get a table like this.
[00:23:29.440] The table is not going to be usable immediately, because you're going to have the actual SVG values in binary.
[00:23:37.280] In order to be able to use them in your HTML custom visuals, you're going to need to transform them into text.
[00:23:44.800] And you can do that very quickly in Power Query by right-clicking on the Content column, selecting the Transform option, and Transform to Text.
[00:23:55.840] And what you'll see afterwards is this table. Basically, you can remove almost everything else, but you're going to want to keep the Contents, which is the actual SVG value itself, and the Name.
[00:24:09.920] The names are quite important, and I'll show you why in just a second.
[00:24:16.480] So once you have an HTML custom visual, you can put that into your Power BI report.
[00:24:23.680] And once you do, you can basically use the Content column directly in the Values in order to bring out an icon.
[00:24:33.600] But in order to get the gradient, you're going to need to do something a little bit extra, and that extra part is this measure right here.
[00:24:43.360] You can see that it's very, very similar to the measure that I was showing earlier for dynamic themes.
[00:24:49.920] But instead, I have added a tiny bit of DAX functions here to substitute the beginning of the SVG.
[00:24:58.880] This open cross parentheses path with — I don't know what this is called — with this value where open cross parentheses path is there, so it'll always have this initial part defining the colors in the beginning of the SVG.
[00:25:27.840] And this is essentially what it looks like. So if I select this one, which is just the Content column itself, you can see that I'm actually filtering by the name.
[00:25:38.720] That's why keeping it is important, because if you didn't have the name value and you were trying to filter by the actual SVG, that's just not going to work. It's really hard to parse.
[00:25:50.240] So having the name itself is a lifesaver.
[00:25:55.680] You might want to set some filter settings, like you can only select one value, and once you do, you can select different items depending on what you'd like.
[00:26:05.440] So there's 2,000 of icons that I put in here, so it's got a lot of different things.
[00:26:12.320] And if I wanted to look for something specifically, I might be able to find it.
[00:26:17.600] So unselect everything, and I look for a chart.
[00:26:25.760] Oh, maybe this isn't the exact version that I have. Nevertheless, that is what it is.
[00:26:34.080] And it's pretty nice to have all of these different items.
[00:26:40.000] I even put in reports that I'm making, an information button where I have all of the different icons that I can very easily see.
[00:26:51.680] And this color-graded icon as well is basically just using the measure instead of the Content column, and the same thing applies here.
[00:27:01.280] I can simply just select different items based on the name, and I'll have an icon that can very quickly change its color.
[00:27:15.360] That took a second.
[00:27:25.280] So that was the part about HTML. I'm going to move on to talking about calculation groups.
[00:27:35.200] Because there's one specific technique in calculation groups that I'd like to share with you, and that is KPIs with context.
[00:27:46.240] Basically, what this looks like is: here you can see three different values for sales, profit, and units sold.
[00:27:54.560] Calculation groups work on values by essentially if you filter the values with the calculation group, it modifies what the actual values become.
[00:28:08.800] Using this, I can select a specific calculation group, and it now shows not only the value, but the context in comparison to last year.
[00:28:22.560] So right now it's showing the increase from last year.
[00:28:28.000] And I can also do something else, like here I have two different cards, one's a little bit larger, one's smaller, and this calculation group is only affecting the lower values.
[00:28:42.240] But if I select this now, it's showing the current, the Delta from last year, and the percent increase or decrease from last year.
[00:28:55.680] And I'm going to show you how you can do this.
[00:29:02.560] So this is the actual calculation group that I'm using to achieve this effect.
[00:29:08.800] There are four different variables that I'm going to walk through one by one, so hopefully you'll understand how to do this yourself.
[00:29:18.560] So the first variable is the selected measure. Selected measure is a specific function in calculation groups that's being used to call whatever measure is being filtered.
[00:29:32.800] So in the case of KPIs, it's going to be the current year. That's exactly how you should see it.
[00:29:40.160] Second variable is the last year, so you have Calculate SelectedMeasure, same period last year.
[00:29:49.760] And that's basically only going to work if you have a date table.
[00:29:56.320] If you're going to try to use this text, you might want to alter the dates table to be whatever the date column and the date table name is that you are using.
[00:30:07.040] But this is generally something that is used by most Power BI developers and date table.
[00:30:15.200] It's not crazy to have something like that.
[00:30:19.200] But once you have the current year and the value last year calculated, you can calculate the growth by dividing the current subtracted by last year by the last year value, and showing the percentage value.
[00:30:38.400] We also have a fourth variable, which is going to be another function you can only use in calculation groups called SelectedMeasureFormatString.
[00:30:50.560] Bit of a mouthful, but this is going to bring the actual text format string to be used elsewhere in the actual calculation group.
[00:31:01.120] And you can see it's used right here basically. The value that I'm sending out is the current value, so the SelectedMeasure in its original format.
[00:31:13.120] And if it's and if the growth is not zero, then if the growth is positive, put an upwards triangle and its percent.
[00:31:24.480] And if it's negative, put a downwards triangle and a percent.
[00:31:31.040] But everything is not as easy as it seems.
[00:31:36.320] If you were to use simply this Calculate this calculation group and you want to filter a value in this way, it won't be nicely formatted as you see in the left.
[00:31:49.120] What it's actually going to do is it's going to be not formatted at all as you can see on the right.
[00:31:56.800] And this is a little bit because the numbers themselves are not being accepted as numbers. Actually being considered as text, and obviously this isn't ideal.
[00:32:08.480] So I'm going to show you how to get from here to here just now.
[00:32:16.320] In calculation groups, there is something called a Format String Expression.
[00:32:23.040] This is something you can directly access in the Tabular Editor external tool.
[00:32:29.440] And if you click on this, basically what it's going to have is just an empty box, but what's this empty box is is that you're going to be able to put in some code in order to modify how the format of the selected measure operates.
[00:32:46.240] This is very cool because it allows us to directly modify how the fourth variable itself, SelectedMeasureFormatString, and thereby also affect how the SelectedMeasure is formatted within this calculation group.
[00:33:07.360] Now, I've actually tried a couple of different ways to make this work. I've tried using logarithms, natural logarithms.
[00:33:15.840] But I only tried this at the advice of Kane Snyder from Agile Analytics, I believe.
[00:33:23.520] And one thing that he posted on LinkedIn one day was that he was trying some different formatting options using calculation groups.
[00:33:33.440] And he was able to generate the number of digits with a significantly optimized speed improvement from using logarithms by simply modifying the value into a string with no decimal, so converted into an integer, finding the length of that value, and from the length identifying if it's in thousands, millions, billions, or trillions.
[00:34:03.040] And I've tried it as well. It is indeed much faster than using logarithms.
[00:34:09.760] Definitely very cool stuff, but the credits to this goes to Kane.
[00:34:17.280] So that's basically most of the information you need in order to replicate this specific method.
[00:34:25.440] And you can see that basically what I'm talking about here is that there are different variations.
[00:34:32.960] Like, for example, in the very beginning, I showed that there was a way to show current and last year percentage, but also Delta and last year.
[00:34:44.000] And in order to do that, you simply change what you're showing in the measure from current to the growth flat, which you simply calculate as the current value subtracted by last year.
[00:34:56.960] And it works pretty nicely, and you can see that again here.
[00:35:04.480] Okay, so that was the one technique using calculation groups I want to show.
[00:35:11.680] And I'm going to take a little bit of time now to talk about Deneb, which I think is the forefront of custom solutions in Power BI as of now.
[00:35:25.120] Deneb is this custom visualization from the App Source, created by Daniel Marsh Patrick.
[00:35:32.960] And it allows for the use of Vega and Vega-Lite language in order to create custom visualizations to be used in Power BI.
[00:35:44.640] The main reason that Daniel says he made this was to overcome some of the limitations of Python and R visuals in Power BI.
[00:35:55.360] Honestly, I believe it does this really well.
[00:35:59.520] The two main drawbacks of Python or R visuals in Power BI that I was using a couple years ago were that one, they were quite slow.
[00:36:08.480] But also, they did not have the ability to interact with other visualizations.
[00:36:16.320] Most visualizations in Power BI have interactions, and they slice or filter other visuals.
[00:36:23.040] But R and Python visuals don't have this capability.
[00:36:28.000] However, you can do this in Deneb. It's a little difficult, honestly, for me, and it gets like very difficult, because I'm still very new to Vega and Vega-Lite.
[00:36:39.680] But it is possible, which I think is a major reason why you'd want to use this as a custom tool.
[00:36:47.680] This is some examples of what the community has created in Deneb.
[00:36:54.400] I'd like to point out that you can use the IBCS International Business Communication Standards type of charts that you see here in the middle.
[00:37:04.960] There are lots of gradients, which I've already said I love.
[00:37:10.720] And there's this one visual that I thought was very nice, because this is a specific visual that I've seen in a lot of Tableau reports.
[00:37:20.640] Where you have the states of different states in America being represented as hexagons or circles or something.
[00:37:28.320] But now it's also impossible to bring in a visualization like that in Power BI using Deneb, which I think is very cool.
[00:37:39.680] Actually, let me show you what it looks like for the Power BI developer when you first put Deneb in.
[00:37:49.440] So once you've downloaded Deneb from the App Source into your Power BI Desktop, if you put that data visualization into your report, this is what it's going to look like.
[00:38:02.080] You need to actually put in some values into the Values field in order for this to open up.
[00:38:08.640] And it's giving you exact information of what you need to do.
[00:38:14.080] Hover over the visual, click on the three dots that appear at the top right, and click Edit in order to get started.
[00:38:22.400] Make sure you have all of the different fields or measures whatever you want to actually show in the visualization in the Values at the beginning.
[00:38:32.160] And you might not know what you actually want to show. You can change them later on, but you're going to need the values there to be actually used in Deneb.
[00:38:41.760] So once you say start, it's going to ask you to create a new specification.
[00:38:47.520] In here, you're going to be able to choose what language you'd like to build the reporting visualization with, and whether you want to use Vega-Lite, whether you want to use Vega, or maybe whether you want to import the value from a template.
[00:39:05.120] I'll get into that in a sec, but if you select Vega-Lite or Vega, you'll have some options of some standard visualizations.
[00:39:15.040] So that you can input, and if you select simple bar chart, for example, there might be a visual showing what it looks like.
[00:39:23.520] And you will be able to assign the values that your input into the Values field into these specific fields to create this visualization.
[00:39:34.720] That's why you actually need to put in values into before you get to the stage.
[00:39:40.640] Because if you've only put in one value like I have previously, you're not going to be able to fill both of these with that value, so it's not going to work out.
[00:39:51.200] But honestly, I've never actually used the specifications for Vega-Lite and Vega.
[00:39:58.400] I've a hundred percent of the time imported from template, and I advise you to do so as well.
[00:40:05.120] Because importing from a JSON template is incredibly simple, and is where the true power of Deneb is.
[00:40:13.760] Import: once you select Import from Template and select the JSON template, it's simply going to open up a navigation wizard where you can find a JSON template that you've already downloaded.
[00:40:27.680] And once you open it up, it's going to allow you to assign columns or measures to the fields just as before.
[00:40:36.000] And you can hit Create, and it will generate a different view for you that you can alter the visualization before it goes into your report.
[00:40:46.880] There's three different parts to the edit screen that you see here.
[00:40:52.640] The first part is the code area, which has either the Vega or the Vega-Lite code, depending on what you've actually selected.
[00:41:02.880] It has a preview of what the visualization will look like.
[00:41:07.520] And it has a table area, which will show the underlying data or logs or whatever you want to see about the visualization itself.
[00:41:17.440] One thing that I think is a little bit difficult is that it is a code-based visualization.
[00:41:24.800] So making changes to what the visual needs to be done in the code editor that you see here.
[00:41:32.000] That can be a little bit difficult for some people, because obviously Vega or Vega-Lite, not so many people have used it.
[00:41:41.600] And you might be essentially learning a new language in order to do this.
[00:41:47.200] But the documentation is pretty thorough, and it was very easy to get started and to make modifications based on what your needs just by using the documentation available online.
[00:42:03.680] There's a lot of resources for Deneb. I've put just a couple of these here.
[00:42:10.080] I really, really like the fact that the Deneb documentation and the Vega documentation have really great examples that you can use.
[00:42:20.480] But there is also a lot of Microsoft MVPs, such as Kerry, such as Mike Carlo, who are maintaining their own websites or repositories of Deneb templates that are very free to use.
[00:42:35.200] If you'd like to see this heat map with bars that I've created, you can find that in Mike Carlo's repository as well.
[00:42:44.480] Okay, so that was basically the three different parts I wanted to talk about for this presentation.
[00:42:53.280] So I'd like to take a short moment to end this talk with just a retrospective about custom solutions in Power BI and what it looks like for the future.
[00:43:10.080] Because in all honesty, I think most people might have heard this if they're in the Power BI space.
[00:43:17.760] That Miguel Myers has now become the program manager for visualizations in Power BI.
[00:43:24.960] And honestly, visualizations in Power BI have been mostly unchanged since Power BI's release functionality-wise.
[00:43:34.400] And that being the case, a lot of the things that Miguel has said publicly, whether it's been on some podcasts or different user group meetings, how you know, this means that a lot of the different techniques that I've shown you might become obsolete.
[00:43:55.840] For example, within a podcast with Power BI Guy, Um, Ben himself, Miguel mentioned that he does intend to allow different fonts to be used in Power BI.
[00:44:07.200] Right now, there's only 26 native fonts, but the intention is to include many more in the future, which directly makes the HTML fonts a little bit obsolete, maybe.
[00:44:19.680] We'll see. There's also something that he's mentioned, that cards will eventually — not so eventually, very soon — be able to hold multiple different elements, which makes the calculation group method of showing context also going to be obsolete.
[00:44:36.160] Hopefully in the near future, so it'll be more accessible for everyone.
[00:44:42.400] And then, he's also mentioned that he does plan to make themes dynamic.
[00:44:48.640] Something that you can do in Power BI Embedded is using the Power BI APIs within the embedded module.
[00:44:57.600] You are actually able to directly change what theme is being placed over the visuals.
[00:45:05.440] And he intends to bring something like that into Power BI so that you could essentially have something like a light theme and a dark theme without having to have all of the confusion that nine parameters will give you with HTML.
[00:45:22.240] Now, that I think makes a little bit of this presentation obsolete, and I'm okay with that.
[00:45:30.080] Because although I really do enjoy custom niche solutions, I really think that custom solutions are a little bit difficult for the average developer.
[00:45:42.400] And not having to jump through a hundred hoops to get the effect that you want is where we should be.
[00:45:50.880] Does that mean that custom solutions are going to go away?
[00:45:56.480] I really don't think so.
[00:45:59.520] I think that Power BI is always going to have the need for custom visuals.
[00:46:04.640] I'm pretty sure that Deneb is not going away anytime soon.
[00:46:10.400] And I hope through this presentation that you have gotten some inspiration on how to create some custom solutions for your own designs.
[00:46:21.600] So thanks very much for your time.
[00:46:25.440] I hope you learned something.
[00:46:28.320] I hope you can take something away from this.
[00:46:31.520] Take care.
