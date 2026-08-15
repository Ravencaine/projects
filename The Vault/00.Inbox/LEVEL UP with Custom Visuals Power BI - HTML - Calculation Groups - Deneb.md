---
title: "LEVEL UP with Custom Visuals: Power BI HTML Calculation Groups Deneb"
source: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
video_url: "https://www.youtube.com/watch?v=QXMMpabHPS4&t=18s"
video_file: "99.System/Attachments/Video/LEVEL UP with Custom Visuals： Power BI HTML Calculation Groups Deneb-QXMMpabHPS4.webm"
transcript: "00.Inbox/LEVEL UP with Custom Visuals Power BI - HTML - Calculation Groups - Deneb.md"
creator: "[[Power BI Park]]"
published: 2023-02-15
created: 2026-08-13
description: "How to use: Dynamic Themes/Fonts/Icons using HTML, KPIs with context using Calculation Groups, and Deneb."
language: "en"
processed: "Processed"
---

![[LEVEL UP with Custom Visuals： Power BI HTML Calculation Groups Deneb-QXMMpabHPS4.webm]]
![](https://www.youtube.com/watch?v=QXMMpabHPS4)

How to use: Dynamic Themes/Fonts/Icons using HTML, KPIs with context using Calculation Groups, and Deneb.  
  
\=================================  
⭐Try the Dynamic Report here: https://www.novypro.com/project/gradients  
  
🔥Google Fonts: https://developers.google.com/fonts/docs/developer\_api  
  
🔥Flavio Meneses: https://bievolution.co.uk/customise-report-in-real-time/  
  
🔥Rui Romano- basis of calculation group: https://github.com/RuiRomano  
  
🔥Tabular editor : https://docs.tabulareditor.com/  
  
🔥Calculation groups: https://learn.microsoft.com/en-us/analysis-services/tabular-models/calculation-groups?view=asallproducts-allversions  
  
🔥Icon Pack: https://remixicon.com/  
  
🔥My Heatmap template: https://github.com/PowerBI-tips/Deneb-Templates/blob/main/templates/heatmap%20with%20bars%20-%20red%20themed.json  
  
🔥Deneb Documentation: https://deneb-viz.github.io/community/resources  
  
🔥Vega-Lite Examples: https://vega.github.io/vega-lite/examples  
\=================================  
  
  
Come find me on Linkedin: https://www.linkedin.com/in/injae-park/  
  
Thanks for taking the time to watch this video. I hope you learned something!  
  
#powerbi #powerbipark #microsoft

## Transcript

### Intro

**0:03** · hi everyone welcome my name is NJ and thanks for joining me today on my presentation I'm going to be talking a little bit about some custom visualizations and Niche techniques in power bi today I'm going to be talking about three main things which is HTML visuals

**0:22** · calculation groups and then it I want to warn you in advance that this presentation plays like a tutorial so it will get very technical so let's dive right into the first topic which is going to be HTML visuals in power bi I'm going to be covering fonts themes and icons

### Fonts

**0:47** · this is a little what the end result could look like everything on this page is an HTML visual including the text itself we're looking at fonts first so I'm going to show you that if I select a text and open up the filters pane you can see there are three different filters one is going to allow me to

**1:07** · change the font into basically anything I would like it to show there's a thousand four hundred of these fonts I'm also going to be able to change the font size

**1:25** · and I'm going to be able to change the color of the font so if I want it to be black I can do that if I want it to be a you know it's a gradient I can do that do that as well and you know if I wanted to be a single color I can change that as well which I'll show you a little bit more later on in the presentation

**1:47** · foreign this is the main Dax formula that I've been using and I'm going to walk you through how it actually works today and the first thing to understand is that this is a calculation group and this is and that's how the filter functionality

### Calculation Groups

**2:05** · actually occurs to create calculation groups you're going to need to have the external tool tabular editor you need to download it online which you know it's like will be in the description I think and once you've downloaded it you can open it directly from Power bi from the external tools tab which you can see right here

**2:29** · once you have the tabular editor open if you click on the table folder you can create a new calculation group just by right-clicking and from the calculation group you can basically right click again in order to create a new calculation item which will allow you to type in the actual code that you want for the calculation group right in the tabular editor external tool

### Google Font API

**3:00** · so going back to the decks the key thing here to note is that we're actually using the Google API that you see in this red box to actually bring in the HTML and to bring in the font into this HTML but there's a couple of things that we need to do in order to make this dynamic because that is in order to make this adjustable using the filters which is why we have these three variables

**3:31** · so let's take a look the first variable is the actual text that we want to show it's encapsulated in the measure which is what you usually use to put text into something like a card and you can change you can change this measure itself outside in order to modify what text you'd like to show you can also see that it's been altered to be formatted as a text

**4:00** · the second variable is the actual name of the font now logically if you want to have a number of different names in a filter you're going to have to have that within power bi somewhere and I'm going to show you the steps you need to take in order for that to happen what you can see right here is the developer Google font API

**4:23** · which is the web page you need to go to in order for this to happen on that page once you scroll down a little bit it it has this area with it has this button that says get a key which you can simply click and it will generate an API key that you can use and you're going to need to you have this API key because this is the URL that you're going to you know click input into Power bi and it don't it won't work

**4:52** · unless you have a valid API key once you've created an API key from Google you can simply replace this colored text in this URL and it's going to be something that you use in your you know it's like power bi to get the data simply select get data within power bi select the web option and paste the URL into the you know it's like window into the wizard box that you get so with the actual API key that you've generated and

**5:24** · once you hit OK what it's going to show is this table where basically it has a lot of different units like things from the API itself but all you need is the second column the one that's called items.family you don't need anything else so I usually tend to remove all of

**5:45** · the other columns and I replace rename the column name to font name or something like that and I'll rename the table itself to something like Google fonts and as you can see the actual second variable is the selected font so I do create another measure that will simply be something like selected value of the column that I still have

**6:15** · and then we have our third variable which is simply a numeric parameter from the modeling tab in power bi and you can see that I've just created a numeric range from 0 to 100 with an increment of one 100 you know it's like means that the maximum font size is up

**6:35** · to 100 but if you wanted to have larger font size is all you would need to do is change the maximum value to something much larger you can also see that in the actual tax uh variable a Dax measure it's been formatted as a text but also has the you know it's like PX value uh you know text right after it so that it will indicate that it fits like 100 pixels or something like that that's what the PX stands for

### Custom Fonts

**7:07** · now we've gone through the variables but I also want you to know that you don't necessarily need to have all of these steps in order to have a nice custom font for some text in your power bi if

**7:22** · you want to be able to have just some static text you don't need the you know it's like API key you don't need this numeric parameter and you can have the text value even right in the measure itself so I've shown that here you can

**7:38** · just put in the text value for the first variable the name of the font you'd like to use for the second variable and the font size I've made a mistake here you need to put in the PX you know to make sure that that works but uh once you've put that value in you can use this measure the same way I'm about to show you how to use the previous measure in order to get that custom font in your power bi

**8:08** · now before I before we go further I also want to talk about colors right now this code that I've been showing you only works in black and that's because the color value here is static and it only shows black at the moment that wasn't enough for me so I created a couple of more calculation items for the calculation group with some small adjustments this is the first one where I have a color variable that is

**8:38** · the simply a measure that I will show later on that is inputting a specific color into this uh it's like into this HTML code the color itself can be RGB it can be a named value I think hex codes also work but I'll show a little bit more of that in just a second and then because I as a person really love gradients I created another calculation item in the calculation group in order to show two used in order

**9:11** · to use two different colors to create a gradient so you can see like uh highlighted in the red boxes is the extra bit of code that I added to make this happen now the last piece of the puzzle is that

**9:28** · is you're going to need an HTML custom visual there's a lot of different you know it's like HTML custom visuals you can choose and you can you know it's like get them by simply clicking the get more visuals button from the visualizations pane which will open the app source and in the App Stores simply search for HTML and there's a whole bunch of them out there I use this one HTML content by Daniel

**9:55** · Marsh Patrick because he also created deneb but I understand there's uh some other ones where you could put in CSS separate from the HTML honestly I'm not very good with you know it's like um HTML at all this is probably one of the first um pieces of HTML code that I created and I don't know how to use CSS at all basically so that wasn't too useful for me but if this is something for you definitely check out the different options as well

### Dynamic Text

**10:28** · and it's all together by first placing an HTML custom visual into the power bi you know it's like reports and then you want to put in the actual value of the text so this is what would be the first variable into the values of the HTML custom visual this is what I showed earlier it said this is text and it's just that first variable that you put into the values and in order to get this

**10:59** · kind of you know it's like effect of Dyna of and in order to get this Dynamic effect basically what you're going to want to do is simply put in a couple of filters into the filters pane for the specific visual you need to put in the font which is the Google font a table that you you know created you're going to need to put in the numeric parameter so that it you can

**11:25** · alter the font size and then you're going to have to put in the column for the calculation group I haven't changed it so it's the default's name and this will alter how you actually select the colors this is once again the report and if we

**11:43** · select this value again open up the filters you can see that you know we have the fonts we have the color we have the font size and if I have the color font selected I can select any uh you know okay so it's not primary it's the secondary I can select any specific color and it will change the text into something else so I have currently Blues selected but I can exit out of Blues and I can put in any color

**12:16** · that I would like the text to be I can also change my settings so that if I wanted to change this color using rgbs then I can absolutely do that so I've got a slider for red green and blue and I can change what the color is going to look like in this way

**12:43** · the text itself of course if I want to have a gradient then it'll use both the primary and secondary to create a gradient and if I want it just to be black I can do that as well foreign

**13:00** · from you know it's like talking about the actual text itself the font and how we use this Dynamic genotic way to alter the colors and the size and instead oh no instead I'm going to start talking about everything else on this page everything else on this page is also you know it's like um part of what I would call the theme and I'm going to talk about how HTML can be used to create this Dynamic theme that you're seeing

**13:30** · so if I'm changing you know colors you can see you know it's like not only is the text changing but the icons and you know it's like the Border as well but let's focus on the border for now so I want to give praise where you know it's like praise is due uh a lot of this was built upon this idea that Flavio Meneses I really hope I'm pronouncing that correctly this is uh based on flavio's work where he created a report that's used exactly this concept of red

**14:02** · green and blue Sliders in order to affect what color should be used on the theme itself and the way that it works is that there are essentially three different numeric parameters uh one for red one for blue one for Green from zero to 255 which is the maximum for the color setting in RGB

**14:28** · having you know it's like these three different parameters you would need a measure to bring those parameters together and you know it's like from the selected values actually bring them together to create a text like this one that you see here

**14:45** · foreign is really really cool but I also thought you know as I thought that maybe you can use something else and it turns out in HTML you can put the name of certain colors and HTML will recognize that text itself so I found a table online that's you know it's like had a couple of these HTML colored names and I simply insert

**15:12** · them into Power bi as a table I had to do this manually with you know it's like copying the web page and pasting it into you know it's like the manual entry for power bi but I got it in there all the same

**15:30** · so something that I already mentioned is that I do love gradients and I wanted to expand a little bit on flavio's work so I wanted to have gradients but I also wanted to have a background color and that meant I needed three separate colors for three different sets of rgbs and that in itself was nine different parameters but

**15:55** · I also wanted to have specific colors that you I could choose to be named and that meant you know three different tables so I'm going to put it out there that this is maybe not a technique you want to copy for business purposes it's you know it's just something to showcase the kind of uh you know it's like things you can do in a custom tool but this is probably more effort than it's worth for most people

### RGB Table

**16:27** · now that I had two different ways of being able to input colors so I had the RGB and then I had the name I needed a way for power bi to understand which one to use so I created a table that had you know just this these two values RG these two values RGB a name and a

**16:49** · measure uh you know it's like for the actual color would based on which value was selected simply use a switch function to and input either the RGB value or the named color value

**17:08** · so let's take a look at the actual HTML code and how these you know it's like parameters actually are being used so like I mentioned this was one of my the first HTML codes that I wrote and when I say wrote I mean I Googled different parts of it until I managed to splice something together that worked

**17:31** · so this part here which is the variable for the color itself is what defines the color you know and you can actually see that there's a gradient for the color one and color two and there's another value which is the parameter color percentage value which is another numeric uh parameter from 0 to 100 to

**17:53** · indicate how much color exists for color one in comparison to color two so I'm going to show you that in the report in just a second and you'll understand immediately what it is

### RGB Border

**18:08** · and what that code actually is is this outer border right here it's actually this outer border and you can only see this you know it's like board the Border actually comes from the fact that we have one color in the background and then we have another uh HTML visual

**18:28** · on top of it to create this border like feeling so a little bit more about you know it's like how the input was created I needed a way to differentiate you know because I had two different methods of inputting what color to use this pale you know it's like uh this text uh you know

**18:50** · this named color method and the RGB method so the way that I decided to do it was using bookmarks basically by clicking the plus you could you know it's like navigates to you know it's like this one and from here pressing the minus would navigate back into this one and foreign that's basically the way that I decided to do it I wanted to have some smaller UI elements to make it a little bit simpler like for example the border is the color that has been selected and

**19:24** · um the buttons here at the top also show what color is being used you can even see that there is a parameter color percentage which is that other numeric parameter that I was talking about and even one more this Hue is also something based on flavio's work which allows me to have the background be a single monotone color with one uh you know color selected and a lighter color depending on this you know it's like value

**19:54** · and you can see that right here so if I had select the parameter color to be slightly different maybe I should change the secondary color to something more visible so if I have the color be you know it's like in this format you can actually see that if I change the parameter color percentage you can see that the level of the gradient you know it's like Alters depending on what value it is

**20:21** · I had to restart my PowerPoint presentation if you have a power bi embedded in your PowerPoint sometimes PowerPoint can decide that it doesn't recognize your credentials anymore so I had to re-log in and restart everything okay so you can see that the parameter color Alters what's uh level of color of

**20:44** · you know it's like the primary and secondary color there is and of course if you click on this minus or plus what is happening is that there is a hidden slicer depending on the bookmark that will indicate whether or not it is an RGB uh you know it's like bookmark or a named color bookmark and thereby change the you know it's like a selection of how the colors are currently being used

### Icons

**21:12** · so this is something that I you know to really enjoy and that basically covers how you know it's like I would use HTML within themes and here's a little bit of what the Hue might look like as well changing the colors a little bit all of you know it's like the gradient in the back but this code in itself is not something

**21:36** · strictly used uh something that is just strict for the you know say colors you can actually see as I'm working that's the icons themselves are changing so that's where we're going to go to next talking about icons and the way that it works is that this

**21:54** · variable for color is directly affecting what is actually being you know it's like the color settings for the HTML visual but the HTML visual shape it itself is simply being you know decided by what's in this red box and what's in this red box is simply a rectangle with slightly rounded Corner values so that means that the idea for the icons is if we change this specific text

**22:26** · to be something else to be an suvg for example then we can have icons that are dynamically changing color so I'm going to tell you about how I do icons in power bi from the very beginning I like to use this website remixicon.com

**22:48** · for two reasons the first is that you can use this uh website to download 2271 icons in one go which is really nice and you know it's like very convenient uh I'm actually going to you know it's like uh use this for a very specific reason which you'll see in just a second but I also like the fact that it's a free to use item and you know

**23:13** · it's like as long as you you don't even necessarily have to mention them but you know it's like they're grateful if you do I think it's wonderful that open source icons like this do exist for people to be able to use once you've downloaded the actual pack and you've unzipped it what you're going to want to do is you're going to want to get data in the folder option once you

**23:38** · do that and you select the folder that you downloaded just from remix icon.com you're going to get a table like this the table is not going to be usable immediately because you're going to have the actual SVG values in binary in order

**23:57** · to be able to use them in your HTML custom visuals you're going to need to transform them into text and you can do that very quickly in power query by right clicking on the content column selecting the transform option and transform to text and what you'll see afterwards is this table basically you

**24:19** · can remove almost everything else but you're going to want to keep the contents which is the actual SVG value itself and the name the names quite important and I'll show you why in just a second

**24:36** · so once you have an HTML custom visual you can put that into your you know it's like power bi report and once you do you can basically use the content column directly in the values in order to bring out a um an icon but in order to get the

**24:56** · gradient you you're going to need to do something a little bit extra and that extra part is this measure right here you can see that it's very very similar the first Parts in um with the measure that I was showing earlier for dynamic themes but instead I have added a tiny bit of you know it's like functions or Dax functions here to substitute the beginning of the SVG this

**25:26** · open uh I don't know what this is called Open Cross parentheses path with uh you know it's like this value where Open Cross parentheses path is there so it'll always have this initial you know it's like part defining the colors in the beginning of the SVG

**25:47** · and this is essentially what it looks like so if I select this one which is just the content column itself you can see that I'm actually filtering by the name and that's why keeping it as important because if you didn't have the name value and you were trying to filter by the actual SVG that's just not going to work it's really hard to parse so having the name itself is a lifesaver you want

**26:13** · might want to set some filter settings like you can only select one value and it once you do you can pardon me you can you know it's like select different items depending on what you'd like so there's two thousand of you know it's like icons that I put in here so it's got a lot of different things and if I wanted to look for something specifically I might be able to find it so unselect everything and I look for a

**26:45** · chart oh maybe this isn't the exact version that I have nevertheless that is you know it's like what it is and it's pretty nice to have you know it's like all of these different you know it's like items I even put in it's like reports that I'm making an information button where I have all of the different icons that I can very easily see

**27:11** · and this uh color graded icon as well is basically just using the measure instead of the content column and the same thing applies here I can simply just select different items based on the name and I'll have you know an icon that can very quickly change its color

**27:47** · that took a second okay so that was the part about HTML I'm going to move on to talking about calculation groups because there's one specific technique in calculation groups that I'd like to share with you and that is kpis with context basically what this looks like is here you can see three different values for sales profit and units sold calculation groups work on values by

**28:18** · essentially if you filter them if you filter the values with the calculation group it modifies what the actual values become and using this I can select a specific calculation group like this and it now shows not only the value but

**28:36** · the context in comparison to last year so right now it's showing the increase from last year and I can also do something else like here I have two different cards one's a little bit larger one's smaller and this calculation group is only affecting the lower values but if I select this now it's showing the current here the uh the Delta from

**29:02** · last year and the percent increase or decrease from last year and I'm going to show you how you can do this so this is the actual calculation group that I'm using to you know it's like achieve this effect there's four different variables that I'm going to walk through uh you know it's like one by one so hopefully you'll understand how to do this yourself

### Calculation Group

**29:29** · so the first variable is the selected measure selected measure is a specific function in uh calculation groups that's being used to call whatever measure is being filtered so in the case of kpis it's going to be the current year that's exactly how you should see it second variable is the last year so you

**29:52** · have calculate selected measure the same period last year and that's basically only going to work if you have a date table if you're going to try to use this text you might want to alter the dates table to be whatever you know the date column and the date table name is that you are using but this is generally you know it's like something that is views by most power bi developers and

**30:17** · date table it's not it's not crazy to have something like that but once you have the current year and the value last year calculated you can calculate the growth by uh dividing the current and not dividing dividing the current subtracted by last year by the last year value into showing the percentage value

**30:39** · we also have a fourth variable which is going to be another function you can only use in calculation groups called selected measure format string bit of a mouthful but this is going to bring the actual text format string to be used elsewhere in the actual calculation group and you can see it's it's used right here basically the value that I'm you

**31:07** · know it's like sending out is the current value so the select measure in its original format and if it's uh and if the growth is not zero then if the growth is positive put a upwards triangle and its percent and if it's negative you know it's like put a downwards triangle and a percent

**31:34** · but everything is not as easy as it seems if you were to use simply this calculate uh this calculation group and you want to filter a it's like value in this way it won't be nicely formatted as you see in the left what it's actually going to do is it's going to be not formatted at all as you can see on the right and this is a little bit because the um

**32:05** · the numbers themselves are you know it's like not being accepted as numbers in this values actually being considered as text and obviously this isn't ideal so I'm going to show you how to get from here to here just now

**32:24** · in calculation groups there is something called a format string expression this is something you can directly access in the tabular editor external tool and if you click on this basically what it's going to have is just an empty box but what's this empty box is is that you're going to be able to put in some code in order to modify how the form how the format of the selected measure operates

**32:53** · this is very cool because it allows us to directly modify how um the fourth variable itself selected measure format string and thereby also you know it's like affect how the the selected measure is formatted within this calculation group now I've actually tried a couple of different ways to make this work I've tried using logarithms natural logarithms but I only tried this at the

**33:24** · advice of Kane Snyder from agile analytics I believe and uh one thing that he posted on LinkedIn one day was that he was trying some different formatting options using calculation groups and he was able to generate the number of digits with a significantly optimized speed improvement from using logarithms by simply modifying the value into a string with no decimal so you

**33:53** · know converted into an integer finding the length of you know it's like that value and from the length identifying if it's in thousands millions billions or trillions and I've tried it as well it is indeed much faster than using logarithms definitely you know it's like very cool stuff but the credits to this goes to King

**34:18** · so that's basically most of the information you need in order to replicate this you know specific method and you can see that basically what I'm talking about here is that there are different

**34:35** · variations like for example in the very beginning I showed that there was a way to show current and last year percentage but also Delta and last year and in order to do that you simply change what you're showing in the measure from current to the growth flat which you simply calculate as the current value subtracted by last year and it works you know it's like pretty nicely and you can see that again here

### Calculation Group Variations

**35:11** · okay so that was the one technique using calculation groups I want to show and I'm going to take a little bit of time now to talk about denip which I think is the Forefront of custom Solutions in power bi as of now

### Deneb

**35:30** · deneb is this uh custom visualization from the app Source created by Daniel Marsh Patrick and it allows for the use of Vega and Vega light language in order to create custom you know it's like visualizations to be used in power bi the main reason that Daniel says he made this was to overcome some of the limitations of python and R visuals in

**35:57** · power bi and honestly I believe it does this really well the two main drawbacks of uh python or R visuals in power bi of when I was using them a couple years ago was that one they were quite slow but also they did not have the ability to interact uh with other you know you know it's like visualizations most visualizations in Power bi have you know interactions and they slice or filter other visuals but R

**36:31** · and python visuals don't have this keep capability however you can do this in denim it's a little difficult honestly for me and it gets like very difficult because I'm still very new to Vega and Vega light but it is possible which I think is a major major reason why you'd want to use this as a custom tool

**36:53** · this is some examples of you know it's like uh what the community has created in denim uh I'd like to point out that uh you can use this ivcs international business communication standards type of charts that you see here in the middle there are lots of gradients which I've already said I love and there's this one visual that I thought was very you know it's like nice because um this is a specific visual that I've

**37:22** · seen in a lot of Tableau reports where you have the how do you say the states of different states in America being represented as you know hexagons or you know it's like circles or something but now it's also impossible to bring in a visualization like that in power bi using Dev which I think is very cool foreign

**37:49** · actually look like for you know it's like the power bi developer when you first put deneb from you know it's like okay so once you've downloaded deneb from the app Source into your power bi desktop uh if you put that data visualization into your into your report this is what it's going to look like you need to actually put in some values into the values field in order for this

**38:15** · to open up and it's giving you exact information of what you need to do hover over you know it's like the visual click on the three you know it's like dots that appear at the top right and click edit in order to you know it's like essentially get started make sure you

**38:33** · have all of the different you know it's like fields or you know it's like measures whatever you want to actually show in the visualization in the values at the beginning and you might not know what you actually want to show you can change them you know it's like later on but you're going to need you know it's like the values there to be actually used in denim so once you you know say start uh start

**38:55** · it's going to ask you to create a new specification uh in here you're going to be able to choose what language you'd like to build the reporting uh the visualization and you whether you want to use figure lights whether you want to use Vega or maybe whether you want to import the value from a template I'll get into that in a sec but if you select Vega lights or Vega you'll have some options of you

**39:20** · know it's like some standard standard visualization so that you can input and if you select simple bar chart for example there there might be a visual showing what it looks like and you will be able to assign the values that your input into the values field into these specific fields to create

**39:43** · this visualization that's why you actually need to put in values into you know before you get to the stage because if you've only put in one value like I have previously you're not going to be able to fill both of these with that value so it's not going to work out but honestly I I've never actually used uh

**40:05** · the specifications for vehicle lights and Vega I've a hundred percent of the time imported from template and I advise you to do so as well because importing from a Json template is incredibly simple and is where the true power of deneb is import uh if once you select import from template and select the Json template you it's simply going to open up a navigation wizard where you can open you can find a Json template that you've

**40:34** · already downloaded and once you open it up it's going to allow you to you know it's like assign columns uh or measures to the fields just as before and you can hit create and it will generate uh you know it's like a different view for you that you can alter the visualization before it goes into your report there's three different parts to the edit screen that you see here the first part is the code area which has the

**41:04** · either the Vega or the Vega Lite code depending on what you've actually selected it has a preview of what the visualization will look like and it has a table area which will show the underlying data or logs or whatever you don't like want to see about the visualization itself one thing that I think is a little bit difficult is that it is I'll uh you know type a code based visualization so making changes to what

**41:35** · you know it's like the visual it needs to be done in the code editor that you see here that can be a little bit difficult for some people because uh obviously Vega or Vega like not so many people have used it and you might be essentially learning a new language in

**41:54** · order to do this but the documentation is pretty thorough and it was very easy to you know to get started and you know to make modifications based on what mine needs just by you know it's like using the simple well by using the documentation available online

### Documentation

**42:19** · there's a lot of resources for 10 app I've put just a couple of these uh here uh I really really like the fact that the deneb um documentation and the Vega documentation have you know it's a really great examples that you can use but there is also a lot of Microsoft MVPs such as Kerry such as Mike Carlo who are

**42:43** · maintaining their own you know it's like websites or repositories of denim templates that are very free to use if you'd like to see this uh heat map with bars that I've created you can find that in Mike Carlos repository as well okay

### Retrospective

**43:07** · so that was basically the three different parts I wanted to talk about for this presentation so I'd like to take a short moment to you know to end this talk with just a retrospective about custom Solutions in power bi and what does it look like for the future because in all honesty I think most people might have heard this if they're in the power guy space that Miguel Myers

**43:33** · has been you know it's like uh is now the program manager for visualizations in power bi and honestly visualizations in power bi have been mostly unchanged since power bi's release functionality wise and that

**43:53** · being the case a lot of the things that Miguel has said uh publicly whether it's been on some podcasts or you know it's a different user group meetings how you know tech means that a lot of the different techniques that I've shown you might become obsolete for example within

**44:10** · a podcast with power bi guy um Ben himself Miguel mentioned that uh he does intend to allow different fonts to be used in power bi right now there's only 26 native fonts but the intention is to you know include many more in the future which directly makes the you know it's like HTML fonts a little bit obsolete maybe

**44:36** · we'll see there's also something that he's mentioned that's cards will eventually Not So eventually very soon be able to hold multiple different elements which makes the calculation group method of showing context uh also going to be obsolete hopefully in the near future so it'll be more accessible for everyone and then uh he's also mentioned that he does plan to make themes uh Dynamic

**45:06** · something that you can do in power bi embedded is using the power bi apis uh within you know it's like the embedded module you are actually able to directly change what uh theme is being

**45:22** · placed over the visuals and he intends to bring something like that into Power bi so that you could essentially have something like a light theme and a dark theme without having to have all of the confusion that uh you know it's like nine parameters will give you an HTML now that I think makes a little bit of

**45:45** · this presentation you know it's like Obsolete and I'm okay with that because I although I really do enjoy custom unitec Solutions I really think that custom Solutions are a little bit difficult for the average developer and not having to do like jump through a

**46:03** · hundred Hoops to get you know it's like the effect that you want is where we should be does that mean that custom Solutions are going to go away I really don't think so I think that um Power bi is always going to have the need for you know it's like custom visuals I'm pretty sure that deneb is not going away anytime soon and I hope through this presentation that you have you know it's again gotten some inspiration on how to create some custom solutions for your own designs

### Outro

**46:37** · so thanks very much for your time I I hope you you know it's like learned something I hope you can take something away from this take care