---
title: "Top 5 ways to show ACTIVE FILTERS in Power BI"
source: "https://www.youtube.com/watch?v=Nehyym4hPc8&t=204s"
video_url: "https://www.youtube.com/watch?v=Nehyym4hPc8&t=204s"
creator: "[[Power BI Park]]"
published: 2024-09-26
created: 2026-08-13
description: "This video comes with  a PBIX fileJoin my new PowerBI Classroom💯https://www.skool.com/powerbipark/about🔥 My Starter PBIX here➡️: https://github.com/PowerBIPark/PowerBITutorials🔥 Gustaw's"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=Nehyym4hPc8)

This video comes with a PBIX file  
  
  
Join my new PowerBI Classroom  
💯https://www.skool.com/powerbipark/about  
  
  
  
  
🔥 My Starter PBIX here➡️: https://github.com/PowerBIPark/PowerBITutorials  
  
🔥 Gustaw's Post: https://www.linkedin.com/posts/gustaw-dudek\_analytics-data-powerbi-activity-7244417358830739457-eKtL?utm\_source=share&utm\_medium=member\_desktop  
  
🔥 Said's Post: https://www.linkedin.com/posts/saidgamal\_microsoftpowerbi-microsoft-letsworkoutbi-activity-7244447275156934657-biWu?utm\_source=share&utm\_medium=member\_desktop  
  
🔥 Text formatter: https://textformatter.taplio.com/  
  
🔥 Dax Studio: https://daxstudio.org/  
  
Thanks for taking the time to watch this video.  
  
#PowerBI #DataAnalytics #BusinessIntelligence #powerquery

## Transcript

**0:00** · filters are some of the most important things inside of powerbi and today I'm going to show you five different techniques where you can display what filters are being used inside of a specific report from using a text box with different formatting options to using a multi-line card or a single line card as well as having uh the ability to show how many different C columns are being filtered as well as just adding

**0:24** · the filters to a tool tip these will be five different ways that are going to be inspired by by both Gustaf Dudek who posted the single line um method as well as s who has actually posted a really interesting method using svgs we're not

**0:39** · going to be using svgs we're going to replicate this using a text box but if you want to follow along you can go to my GitHub which will be in the description and just download this showing filter starter powerbi file which will have all of the different measures that I'm using it's not completely necessary but if you want to just build the actual report that I'm making this will be the easiest way the data I'm using is going to be the sample

**1:02** · data that exists inside of powerbi if you open up a blank reports and you just load sample data from the use sample data option it's going to give you these financials this is all I'm going to be using it's just a very simple data set that has I believe like 700 rows and it's just a single table that has some things like segment country product discount band Etc we're actually only going to be using these first four segment country product and discount band as the filters and we're just going

**1:30** · to try to make this uh in one go so let me just duplicate this from my existing report and I'm going to remove all of these values and we're just going to get started okay so I'm just moving to the actual starter file that's in my GitHub so that it's more consistent with what other people are doing okay so the main

**1:50** · thing to think about here is that we have these four different columns that are being used in slicers they're just regular slicers and there's nothing changed with them except for the fact that we've put on slicers settings and turned on the select all function now what we're going to do is you have to understand that when you want to show the actual um items that are selected in

**2:10** · your filter the easiest way to do this is to use external tools there's such a thing called Dax Studio which I will also Link in the description which is an amazing tool from sqlbi and that's why you might have seen um articles from sqlbi about how to actually show the

**2:28** · filters in your data and what you can do is if you go to you know it's like just open up DC studio right click on whichever table that you want and then there'll be an option here called Define filter dump measure or Define filter dump measure all tables if you do this Define filter dump measure what it's going to do is it's going to create a measure for you which is going to have essentially all of the Decks that you will need I'm going to take this and I'm going to copy this all the way up to you

**2:57** · know it's like here and I'm going to make a measure now we already have this measure in here but I'm going to just show you exactly what this does uh first what we have to do is we have to remove uh you know it's like the name we have to make the name proper and then you can actually see that this is code that you might have recognized from a whole bunch of different places because this is a very old technique you know it's it's been around for quite some time basically what it's doing is it's telling me that within a specific column or measure it's going to take all of the

**3:26** · filters if the actual column is filtered it's going to find all the filters count them add them you know it's like take the top items from there concatenate them into a piece of text if it's more than a set number if it's more than three it's going to say uh a it's going to say there are the top three items and there's total of 10 items selected or something like that and then it's going to return the value with a new line so

**3:55** · what this actually looks like is if I create this um you know dump filters Financial value and I just put it in here and I let's make this into text box so it's a little bit easier to see you can actually see that right now it finds what items are selected so this is

**4:12** · really nice because you can see that if I select anything will identify which column has been selected as well as which items are being selected this is the base for this entire video and this has been around for a long time you don't need to use any selected values or anything like that it's just using using this specific pattern if the value is if the column is filtered find the filters and add them together now due to the fact that out of the box it does like

**4:40** · limit the number of things that are visible so if there's like more than three items you can see that what it does is says there's three items selected but actually four items are selected in total so we're going to go through how we can modify this to actually use it you know it's like in our actual data set um D Studio One

**4:58** · thing I will say is it's an external tool you just need to download it and it should show up in your external tools folder sometimes there are problems with it showing up but realistically you shouldn't have too much problems if you just tried downloading it okay so the first thing that we're going to do is we're going to show that the DAC Studio

**5:14** · original we've actually removed all of the different columns that aren't necessary for us so we've put in Country discount band products and segments and you can see that the dump filter you know it's like Financial throws out everything including things like cogs and dates and you know discounts these are actually sums or these are facts

**5:33** · inside this table and we're not going to be using them inside of the you know it's like filters so we can just remove those and I've just filtered I've just removed this uh so that it only shows the four different items that we want and we just throw that right in here sorry uh if we throw this in here and

**5:51** · into the table we'll see that it it's basically exactly the same thing there's no changes there and then what we're going to do is we're going to modify it a tiny bit to create uh you know to to show every single item in order to do that basically what we do is instead of having filters count rows top and concatenate X we simply need to remove

**6:10** · count rows on top end because we're no longer going to be trying to filter just to the top two or three items if you want to show everything all you need to do is just remove these two lines so once again remove the r and the T the count the rows and the top n table and in the um in this line here in the concatenate X just change the T to an f and it's just going to concatenate all of the filters as well as we're going to remove this item here this is if the row

**6:40** · number is larger than the max number of filters that you've placed then it's going to you know it's like output something else we don't need that and if we do that in the DAC Studio original for the country you'll be able to see that if we throw this in here again let's remove this let's just take a look at Country cuz that's the only one that we changed if we select multiple items we can see all of them that's that's all that I want because for intents and purposes that's what this does okay so

**7:06** · you can actually see that there's also a little bit of filtering that's been changed instead of looking like uh financials country I have changed it so that it just looks at country and things now you might ask why is this bold inside of the Dex and that's actually possible using a technique that you can actually use to modify your LinkedIn

**7:26** · posts as well and just for you to be able to see I'm using something called Tapo which is actually where I used to use a lot of my you know it's like LinkedIn posts where I would just write something and then you could modified to be bold italics underlined whatever but the cool thing about this is is that it's actually bold in Unicode and that allows you to basically copy this text which has been modified and place it inside of your let me copy that crl + c

**7:53** · contrl v and it makes the item bold this actually doesn't just happen inside your decks but you can actually see if I bring this into a table or a card let's just make it into a table for now the country value is actually bolded now and that is a very cool thing that you cannot do unless you do this little trick so that means that we can apply a little bit of formatting inside of this text and instead of using you know like square brackets we're using um you know just parenthesis okay so this is all

**8:23** · filters multi-line and it's multi-line because if I added more items you can see that's the different columns or the different filters apply start applied start at a new line but maybe you don't have that you know it's like amount of spacing and what you need to do is you need to put in all filters that will become change this back to a table just

**8:46** · so that you can see it that will just be in one single line now the benefits of doing this is be is that you don't actually want to show stuff like this inside of just a table there are different ways that you can show this inside of a table but I prefer using the

**9:01** · new cards and if we select the new cards let's just make these two right here we'll put one in here and we'll put the all filters we will go into call out values make the values much much smaller get like 20 or something 12 okay that that seems to be fine make the text wrapped oh God back to 12 uh change the

**9:21** · font you know it doesn't really matter too too much but um get rid of the labels and that's basically it we can also just make it you know it's like top laid out and that will basically show things on a new line each time that can be very nice but it might be that you don't have enough space what if you know it's like you only had like this much space and you're not showing all of the values those are things to think about when you're you know it's like making this kind of stuff but if we do this and instead of doing it just going to copy and paste this uh we'll also remove

**9:51** · background and the border that It just fits into the background here we click on an item use this uh you know it's like nice brush button here you can change the uh similar visuals to have the same formatting which is nice okay but if we move this here instead of having multi- line we use this one which is the all filter single line you can actually see now that this is slightly

**10:13** · different uh you know it's like it's a different flavor if you want to be able to show everything on one specific line now you don't necessarily have to do this but I do think you know it is something that could be useful for some people especially if you have something that's like a bit longer and you can you know if you want to put something in a

**10:32** · wider vertical space than a horizontal space this is probably a preferable way to do things okay but for now we're just going to move it back here okay so that that's totally fine now the one cool thing about this is that if you actually did want to make this look slightly different we

**10:49** · have this here where you know it's like the actual version here is just all colored slightly differently and we can do this inside of the new card if we decide to do something with the formatting so what we're going to do is we're going to actually take out the all filters uh single line it doesn't really matter what it is right now I'm just throwing in a blank uh measure where the

**11:10** · the measure just returns a blank value and I'm going to the call out values I'm turning off the values as well as the label and then I'm going to reference labels in the reference labels I'm adding blank as the label and the reason that I'm doing that is because what I want to do is I want to turn the title off but in the value I can set whatever value that I want so I'm here I'm going to put in current uh selection now you

**11:35** · can of course make this uh conditionally formatted it really doesn't matter too too much I'm going to make this Bold And once that's done I'm going to go back to callout values go to the layout and make this 0% call out size that will remove the top section so everything is just basically the reference label we'll also

**11:55** · go and turn off the visual borders and inside of the reference labels we will make sure that when all is selected turn off the background that's that's basically where I want to go now I'm going to go to the reference labels select the blank again and with the blank selected and the label selected to blank we can go down to details turn

**12:15** · this on and add data what I'm going to add is the single line and the reason that I want to do it in this way is because I want to add font color the font color that you can use here really doesn't matter you could just have like a you know specific font color let's let's just make take this one for example and then you know make the background and the font color something like this and this will be honestly good enough that you have a very nice you

**12:39** · know it's like different way of showing you know your current selection and let's say nothing is being selected right now you have these dashes that show up as you know it's like the regular um place for show blank as and you can take this show blankass and change that to nothing selected for example and that would also be fine in in order to show people that nothing has been selected no filters are applied okay so that is that and those are

**13:07** · couple different ways now I can show you the regular way because now we have some filters applied the most relevant way that people would be you know able to see filters is just the inbuilt way where we have this filter button and you can see all of these things you know it's like which item is being selected it is a popup kind of it it does take up

**13:27** · a lot of space so sometimes I don't really like using this and you know sometimes I have issues with the fact that it won't disappear but this is a different method to just show the data all of the time and one thing that you can do is you can take this a little bit further using text boxes now this is a technique that I don't always recommend but it is a way to get to see do

**13:52** · something like this um not sure how easy you yeah okay now it's visible this is from Z and he basically made this as the actual um as the way to show how many items there are and you can see that you know it's bolded there are different colors and things like that and although he says that he did this with svgs I'm going to show you a way you can do this just natively with uh text boxes so we're going to insert a text box so we go to insert we insert a text box and with a text box all that we really need to do is prepare a little bit so you can

**14:24** · see that right now we have you know it's like these different items and we're going to be doing this based on the multi-line but if we look at the multi-line what we actually need to do in order to get to a you know it's say formatted point is split all of this up so that we can see all of the different data sets uh like all of the different parts of the string so we can format them separately and for that purpose I've created different you know it's like parts of the measure which is basically you know it's like going to say is the item filtered so is country

**14:54** · filtered then we can show the country you know it's like tag if and the max filters have set to two to only show two different items and if there's more selected then you know it'll show certain number of items selected But Here We have basically country is two and basically return to me um the concatenation of these two item items and you know it's like this value and you don't actually need the X part here this this isn't being used so that's exactly what it should look like in our third measure we basically say if um it

**15:26** · is filtered and there are more than two items you know basically just concatenate all of these items and return the value of items subtracted by two so that you're basically showing the number of items so is it like two more or three more and then at the end we

**15:45** · have one parenthesis that will show up or not and this sounds a little bit convoluted because we're basically taking this item and just chopping it up into multiple pieces and the way to you actually include that inside of your text box is first we click on the value

**16:01** · and then we just have to search for this um measure so country one save and you can see this is country now this is a little bit annoying because if I click uh you know it's like again sometimes it will still reference the previous one so it can be a little bit difficult so the easiest way to deal with uh formatting all of this in my opinion is make this size 12 is just create new lines and uh

**16:25** · on the new line click on the value look for the second one Country 2 save so that's Canada France uh you know it's like go to the new line value Country Part three here it might not show anything which is okay because right now

**16:41** · it's not returning any value and then go to Country 4 if you write country and you know you don't see anything you can just click on show more and then for shows up and now all of these things we're going to make to size 12 we're going to make country this part here bold we're going to make uh this part here we're going to make that let's say dark blue as well as the parentheses at the end dark blue now this item here uh

**17:07** · we're going to make this red and bold and then at the end of all of this what we're going to do is we're going to go and I've clicked right here next to the country but you don't see the you know it's like text or anything that's fine just click here and click on delete that you are putting all of this into one line that's great that's exactly what I want so that now that we have if we have this set up for Country the end result is that if I click three items then it'll show two plus one more and they're all in different fonts now you can see

**17:39** · that when inside of the desktop when they're not selected there's this icon that shows up which you know it's like is a little bit uh looks a little bit weird but inside of the actual you know report that goes away so that you can see um when nothing selected there's just nothing there and that's what it looks like I'm going to do this for the rest of the items which is basically just you know find all of these different items and put them in here which is like value discount band One

**18:06** · save go to next line discount band two save uh discount band three and you can kind of see why I've called them you know it's like like this discount Band 2 3 4 Etc because it's just a lot easier to find what the next item is and you

**18:22** · can also kind of see that this is a lot of effort to you know like make them slightly uh look different whereas you know the text modification technique might be good enough for most people I'm just telling letting you know that this is a way that you can change everything at once and I I think it's really nice you know to be able to have this much um flexibility in how you want to show your data all right um let's keep going one

**18:48** · okay so now that I have all of the different items uh there I'm going to just make them all size 12 and I'm going to make all of them uh you know the right format make all of the titles bold now this is a little annoying because sometimes when you select this it doesn't necessarily show that it's selected very easily and you know say we can go here make the formats all proper and this just takes a little bit of time it's not it's honestly a lot of work for you know it's like what it is in my opinion but let let's take a look right

**19:19** · after we're done modifying everything I go here and now all we need to do is just make sure that formatting in the formatting we turn the background off this here and that's basically it right and looks really neat and is a very nice way to be able to show all of the different data sets but let's take a step back these are three different ways now let's show and you know it's like of course the other way is you know showing this so those are four different ways kind of but let's show you one other way where you can see you know it's like based on the tool tip this value so all

**19:52** · of these different things are filtered here right now and let's say you want to just show the tool tips if you have a new card for for example you have this area called tool tips and we can put in all filters multi-line here we're going to rename this to be called filters with a comma well not a comma with um with a colon and if we do that then what we can do is if you're hovering over this on you know it's like tool tips properties you can see that the filters here actually shows with bold as well sh the

**20:23** · different items now if you put in just the regular one like the daak studio original instead you can actually see the difference is you know it's like pretty substantial you actually see um that just the Bolding makes a big difference in the filters and I think it looks pretty nice and another thing that you can do with this is you can change uh the tool tip um values not the values

**20:44** · the way that it looks so let me take for example this dark item make it 5% transparent and turn all of the text white this is a very different look than how it usually is so instead of you know like just going white let me just throw it in here too so you can see the difference uh filters multiline turn on the tool tips so you know the standard one looks like this but you can make it look like this if you so chose you know

**21:06** · not a big deal but looks pretty cool and the final thing that I'm going to show you is this one thing that I've added here which for that we're going to need one well a couple different things first we're going to turn on a card we're going to put in blank data so nothing's showing we're going to turn off the background uh turn off the values and the label and what we're going to do is we're going to turn on the image and in the image we're going to change it to image URL because I have included a filter icon this is a bit of um you know

**21:38** · it's like a base 64 text of a filter and we're just going to take this image URL which is a filter icon which shows a simple filter that is going to just basically give us a little bit of extra information is there anything filtered right now there's not okay um

**21:59** · let's let's go to the cards and make everything turned off that's pretty nice what I want to do is I want to show people how many items are being filtered so if we go here we can actually see if one column is filtered it say shows one if nothing is filtered it just shows X and if we show that three things are filtered yeah that's the kind of interaction that I want so that I can show people how many things are filtered to show this what I have is a slicer

**22:24** · that shows number of filters I'm only using these four columns so I've basically just put put in if this is filtered count it as one if the other you know column is filtered count it as one add them all together and make it into text making it into text is important because what I'm going to do is I'm going to add a shape a circle well it's an oval but I'm going to make it into a circle and just make it very

**22:48** · very small right here just over that Circle in the icon and what I'm going to do is I'm going to change the shape style The Fill is going to a function so if the item is filtered if any items are filtered at all I want it to be transparent and if not I want it to be black and that's going to for the Border if anything is filtered I want it to be

**23:11** · otherwise I want it to be green or transparent so the fill I'm going to basically go into the conditional formatting field value and select is filtered green and for the Border I'm going to do the same conditional formatting the field value or is filtered black and this way this will basically disappear if nothing is filtered let's back and remove these

**23:32** · filters if nothing is filtered that shape disappears but if something is filtered that shape pops up and kind of Acts to tell me what it should be so the width for the Border I'm making this two and the text I'm turning on and the text is going to be the number of filters um okay it's white now let's make that text also is filtered black uh the color of the text just go into um field value or

**23:57** · filtered black and that's basically it I'm going to make this bold maybe so we have this item here now which shows one um you know column is filtered two columns are filtered three columns are filtered pretty simple straightforward way you can take this one step further by adding one more card making the card

**24:15** · blank again and uh you don't even have to make the card blank we can put in the filters multi-line into the field oh sorry that's a slicer let's make the new card not the slicer all filters multi-line we'll call filters we're going to go into properties turn on tool

**24:32** · tips as well as turning off everything else call out values turned off background is turned off in you know it's like the the card as well as everything else so when you hover over this the filters actually shows up and we can just go here and you can see that right now nothing selected so when you hover over it it uh you know it's like just shows this I think if you go to call out values turn on values and change this value do this yeah then it shows no filters right uh okay I'm not

**25:01** · 100% sure why that text oh no it's because values I turned it on okay so I can turn it off and it shows no filters great so now if I have this selected this way then it'll show the items that are being selected and those are all of the different ways that I'd like to show you today that you can set up your

**25:19** · different filters to show a whole bunch of different things these are really simple techniques that take a little bit of time to set up but once you do you can pretty much reuse them you know it's like however much you like and the nicest thing about this is that of course using the you know it's like Dax Studio it's really easy to make this you don't have to remember it at all you can just use da Studio once and just get everything out there okay so that was basically it I really hope you learned something from here that you can use this is I think a really nice UI detail that isn't so important but you know can

**25:52** · actually add a lot of value to it's like your different end users thanks for watching and take care oh \[Applause\] \[Music\]