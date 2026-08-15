---
title: "38 rows of DAX becomes 1 Line!  User Defined Functions Walkthrough"
source: "https://www.youtube.com/watch?v=kynJmgls6A4&t=5s"
video_url: "https://www.youtube.com/watch?v=kynJmgls6A4&t=5s"
creator: "[[Power BI Park]]"
published: 2025-09-16
created: 2026-08-13
description: "Learn about User Defined Functions in Power BI - and how they will change Power BI report development. This is a practical, step-by-step walkthrough of how I convert a 38 row measure into one final"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=kynJmgls6A4)

Learn about User Defined Functions in Power BI - and how they will change Power BI report development.  
  
This is a practical, step-by-step walkthrough of how I convert a 38 row measure into one final user-friendly function.  
  
💯 Join my Power BI Classroom:  
https://www.skool.com/powerbipark/about  
  
➡️Microsoft Documentation  
https://learn.microsoft.com/en-us/dax/best-practices/dax-user-defined-functions  
➡️SQLBI Article  
https://www.sqlbi.com/articles/introducing-user-defined-functions-in-dax/  
  
🕰️TimeStamps  
0:00 - Intro  
0:55 - The Reference Label  
1:33 - Where to Start  
3:59 - Making a function  
7:44 - Using the function  
8:05 - Creating the Format String  
14:57 - Creating the Deltas

## Transcript

### Intro

**0:00** · This is a KPI card inside of PowerBI.

**0:02** · And what's actually going on here is that this is an SVG which used to take me something like 275 different rows to actually make. But now with userdefined functions, this can actually be made with just one one function in couple of lines. And if you see here, I'm going to take the likes and change that to followers. And I'm going to make sure that I'm using a different hex code. And you'll see that likes has now changed into followers as an SVG.

**0:27** · And this is basically the value of userdefined functions, the reusability of incomplex DAX functions that we never had before. And I'm going to show you how you can get started and start making your own today. Now, this video isn't going to teach you how to make this SVG particularly. If you'd like to learn, you can absolutely check out my online classroom which has 40 odd hours and 18 different PowerBI files that you can just go ahead and grab.

**0:52** · But what I'd like to do is I'd like to actually take you on a journey where I'm going to show you how to use userdefined function. The actual use case we're going to do right now is reference labels for KPI cards. Now what you can see here is a KPI card that bas basically has the current year value and then the difference that flat delta against the past year and the percentage difference versus the past year as year-over-year growth.

### The Reference Label

**1:17** · This before used to take me um 38 different rows to actually make inside of a PowerBI DAX measure. But now with userdefined functions, I can take all of these rows and put it into just one singular function. A really good place to start is going to be the Microsoft documentation because it's going to give us everything that we need in order to identify where we can actually make functions, where they exist, etc.

### Where to Start

**1:40** · So there's actually two different ways that you can write uh userdefined functions which is inside of DAX query view and tindle as and you can actually see them inside of the model explorer as well.

**1:54** · The interesting thing here is that they are actually part of your PowerBI you know it's like semantic model but they are not inside of a specific u you know it's like table like a column or a measure they exist then this kind of the same way that calculation groups do kind of inside of the semantic model. So these are different things that can be used and reused. However, it doesn't actually tie like a specific measure to a a singular table.

**2:20** · This means that one of the best ways to basically reuse these functions is just going to be copying and pasting the actual functions inside of Tindle, which will be really great. However, what I'm going to do is I'm actually going to use tax query view because I actually think the syntax is just a little bit simpler and that's going to be useful for us in a lot of different ways. Okay. So, I think what we need to do first is I need to explain to you what's going on inside of this reference label.

**2:46** · A whole bunch of different things are happening, but essentially what we're doing is we're only taking the current year value and the past year value. And what we want to end up with is this, right? What's the flat difference? What's the percentage difference? and whether it's increasing or decreasing. Perfect. But there is a whole bunch of different parts and I think some of those parts are going to be reusable.

**3:08** · For example, this variable is going to identify how many digits do you have in your current year value and it's actually you know it's like something that is basically taking the current year value converting it into an integer which converts it into a string.

**3:24** · takes the actual length of characters, like how many digits are there of that string and if there's an error, it's going to convert that into zero. Sounds like a lot, right? So, I've actually put this into my test already. And you can kind of see this is what it's doing. So, here at the int level, it's going to get rid of all of the, you know, it's like decimals. At the string level, it's converting that into a string. And then at the length level, it's going to count how many different characters are there inside of the string. And if there's any errors, it's going to just return us zero.

**3:54** · So this is the first part and this is the first thing that we're going to make into a function. Now the function at the very top here is going to be what we actually use. And let me see if I can just bring this out for you. We're using DAX square view. Uh everyone's going to tell you to use Tim because you know it's like it is pretty nice and there's not really functionally that you know it's like much difference between using Tindle or DAX square view. I just like DAX square view so that's what I'm going to use. Um, so we're going to use DAX query view and first we have to have the define key fun uh key keyword.

### Making a function

**4:22** · If you don't use the define keyword, if you just write function, nothing's going to happen. So you always have to write define. Um, in Timle, I think that's going to be create or replace. Yeah, that's the one. So define function, the word right after the keyword function, uh, which defines that you're about to, you know, it's like write a function is the title of the function. So you see here, this is digits. And you can see that inside of the my model, we've got a lovely uh digit function.

**4:49** · Then we have the equals uh and you know it's like open parenthesis. So if I had just something like this, then you can see that that basically going to be the most basic way of writing a function, but it's incomplete. Functions need to have variables. Variables um or I think they're called parameters inside of the actual uh you know it's like documentation.

**5:14** · Yes, parameters. uh you know it's like are going to be the actual arguments that you use inside of your function. So you can define them by first writing the name and then you have space colon space and then you define the data. Now I'm not going to be talking too much about the data type no but I just want you to know that you can put in a table you can put in a scalar which is going to be something similar to a column and there are main types and subtypes.

**5:40** · So you have a main type of any val which is a scalar or table a scalar which accepts you know like an array of different values a table which obviously is a table and subtypes where you can have you know it's like the actual data type format.

**5:58** · So if it's a variant, an integer, a decimal, double string, etc. Um I really recommend if you're you know it's like more curious about this to go and check out the SQLBI uh what is it the SQLBI uh article about this actual you know it's like uh release because they have like a really nice table that you can look at which kind of tries to explain a little bit more as well but I you know I'm not going to spend too much time explaining that right now.

**6:23** · So you basically have all of these things and you have to define at least one parameter and once you do then you can actually have what it you have this equal and um open no closed parenthesis or equal less than value and then that's going to give you uh the space to actually create a function.

**6:44** · It can be any function and use any you know it's like values that exist inside of DAX including other userdefined functions and that's like the key important part that's why we are able to create multiple functions instead of just wrapping the whole you know it's like um measure inside of just one function and reusing it that way because that is honestly not that great

**7:08** · of you know it's like programming practice because if there are functions that we can reuse then we should keep reusing them instead of repeating that functionality everywhere else. So in this case what we're doing here is we have that you know it's like function and we've you know it's like um the parameter that we're calling is a numeric value that value is going to be placed into this functionality and you know it's like it's being referenced right here and you can see that the color is green as well indicating that it's a keyword that we've defined and

**7:40** · this is great because now I can go into our report view and with the test value instead of having all of this we're going to just write this we've got this value digits and we're going to put in this one singular number and this value shouldn't change it should just remain 10 and it does and it's like that's

### Using the function

**8:00** · that's the that's it that's the whole magic of functions uh we're going to keep on going uh we've got like suffix and commas so suffix is basically going to say if the number of digits is a specific value then you know we can get a specific value from it so if it's greater or equal to 13, we're going to get trillions. If it's greater or equal to 10, we're going to get billions. And that's what we expect. So if we throw that into test and uh hang on uh what's the actual value? We have number of digits.

### Creating the Format String

**8:32** · So uh so we were using 10 before in our you know it's a really big value.

**8:36** · So if we have number of digits is 10, then we should have billions and if this is six, we should have mil uh thousands etc. So perfectly fine. This is a separate function and what it's going to do is literally just say here exactly the same thing function the name of the function is going to be scale suffix. We are going to use digits as the keyword for a numeric value inside of the function.

**9:00** · Digits is going to be identified whether it's greater than 13 10 7 or 4 and identify or greater or equal to these numbers to identify whether it's trillions billions millions or thousands. And here it does the same thing with the number of commas. The number of commas might sound a little bit, you know, it's like strange, but the reason that's happening is because what we actually want to do is let's say we have uh what was that number that we Okay, so I'm going to go back and I'm going to keep this number because I think it's funny.

**9:31** · So we have this number, right? And what we can do is uh put it into variable x. So we have this fun number. Variable x is equal to this much. And then we're going to say return uh we're going to format this into a string. So we're going to format the number x into a specific string. So if we do a hashtag, what's going to happen is it's just going to give us the whole string basically. And that's uh a hashtag it's going to be the whole string without decimal places.

**10:00** · If you ident use the period and use another hashtag, it's going to give us u just one number. And the hashtags basically define the number of, you know, it's like positions that we have. But this is interesting. If I use hashtag, comma, you're actually Oh, sorry, that's wrong.

**10:19** · # comma, you're going to see that three numbers have disappeared and it's actually rounded up. And if I use two commas, six numbers have disappeared.

**10:29** · And uh those six numbers have disappeared. And if I use another one, nine numbers have disappeared. And this is basically going to you know it's like essentially say this is going to round up or down the actual number with uh and for each comma it's going to remove three digits and this will allow you to have this uh and digits x to actually show what the actual value should be.

**10:56** · So, uh I think this isn't going to work directly because what we want to do is digits x um is going to give us uh specific value. It's going to give us a number. No, the number is not what we want. We want to have uh what was the function? It was the function called scale suffix. So, we go back to test and we try scale suffix. And scale suffix is going to give us umot. Um that's not necessarily correct, I don't think.

**11:24** · And it actually is scale suffix here. Uh you may have seen it and I kind of you know just breezed over it has the dot zero. The dot0 is going to say give us the first decimal if there's no decimal because it's not a hashtag give us a zero. And now you can see that with this value and the scale suffix this is 6.5 trillions. And now what it's done is it's gotten rid of all these commas. But instead of writing it like this, what we can do is now scale comma count x and scale suffix x.

**11:55** · And that's going to give us um not exactly the right thing because um as you can see scale comma count, I think gives us a specific number of commas. It doesn't give us the actual you know it's like commas themselves. For that we have the function build compact format from digits where with the repeat function scale comma count digits inside of the the test. Let's let me show you what it's going to do is it's going to create four commas.

**12:24** · Now it's having uh a little bit of an issue because you know it's it's not identifying digits but that's because we should make that into x. And then we have uh four commas. So we want this is exactly what we wanted to have.

**12:38** · And um this still isn't quite enough. So this whole function basically builds all of this. And you can see that build compact format digits is going to give us inside of test and I put X in here.

**12:52** · It's going to give us this entire formula uh in entire format string that we want to use which looks very complex but it it's honestly not that bad at all. And what we're doing here is we're going to be putting X and formatting it with build compact format from digits X.

**13:11** · That's going to give us 0.0.

**13:14** · Uh is that correct? Or maybe instead of from digits, what I need is the first one from the value. And that's going to give me 6.5 billion. So this was actually in fact not trillion. This was supposed to be billions. So we have thousands, millions, billions, 6.5 billion. That makes sense. And I think you know it's like before the reason we had trillions was because we weren't properly removing the decimals. So that's what was happening. So now we have 6.5 billion just from this function.

**13:44** · But this already seems a little bit, you know, it's like much as well. So I think I'm pretty sure that I have somewhere down here um another function where everything gets brought in together. And here you can see the format is you know it's like uh format delta format year-over-year arrow format delta is actually formatting the delta right here. And I don't have this format pattern that I need to have in this test version. So absolutely fine.

**14:12** · That's completely you know it's like okay with me. So, if you've been still following me, you know, you can see that there are a lot of different aspects of the reference label like this part, like this part, like this part that we've already created. So, all of this has now been created into functions. What else do we need to do? We need to create uh actually calculate what is the current year minus last year and then format that flat delta.

**14:39** · And then we need to calculate what is the percentage difference between the current year and the last year. and then format that into a different delta.

**14:50** · So, in order to do that, um, inside of the functions, let's see where we are.

**14:54** · We've done all of this here, and then we're creating a function to calculate the year-over-year growth, uh, which is going to take the current value, the last year, divide that into current year minus last year divided by last year.

### Creating the Deltas

**15:06** · This is a very, very common, you know, it's like pattern. Um, let me see here.

**15:11** · What we're going to do is we're going to say, uh, year-over-year growth. This function is going to be the total interactions last year, which is what I'm using as my current year and total interactions past year. And if I calculate that, that will give us a not super nice looking value, I think, because here it's just showing 0.00, right? Um, this is the year-over-year growth.

**15:35** · But I think if I go to this and I make the call out value have more um decimal places, that should, you know, it's like still show us the actual value. Yes. So, you can see that if I, you know, increase the actual decimal places, the actual value does show up.

**15:52** · Not amazing. Uh, you know, it's like percentage- wise, but let's also make that into a percent. So, you can see that it's 0.4%.

**16:00** · Okay. Yeah, sure. So, that seems to work just fine. And then we have that 0.4% as the growth. As we can see here, let's go back and do some more. After we have that growth, we're going to format it with this format string. Now, I haven't talked so super much about format strings as of yet, and I think it's about time um that I, you know, it's like explain what the semicolons do. So, we have this year-over-year growth, right? And that's going to go into our growth. Let's just say variable growth is equal to this.

**16:33** · And then here what we've done is we're formatting it so that growth is going to be formatted with this specific string and then we're adding year-over-year at the very end of it as text. Right? So let's get rid of this for now. That's not super important. But here what it's going to do is it's going to take the value of growth and it's going to say give always give us a zero and always just give us a zero as the first you know it's a value and the first decimal point.

**16:57** · And if those values are just zero, just show me 0.0 all the time so that I can know that, you know, it's still formatted in this way. But if it's positive, I want you to put a string of this, a string, a space, a pipe, a space, as well as an upward. You know, it's like arrow. And if it's negative, show me this. That's because format strings usually have something like this where you have a positive side, a negative side, and what if the value is zero or blank and something like this.

**17:30** · So this would be a legitimate uh you know format string and it's always three different parts. If those parts aren't mentioned, then it usually just defaults to the first item. And you can also do something like this which would mean that if it the value was negative it would show a blank. So this is just how format strings work. And because of that we're using the you know it's like functionality of format strings to say if there's nothing there's if there's no growth if it's actually zero just don't add anything to it.

**18:01** · But if it is you know it's like exists then you know we're going to say it goes up or it goes down. And this is quite nice because here now you can see this is the secondary part.

**18:15** · We can put back the and year-over-year.

**18:18** · That's the complete last part. And now all we need to do is in another function just add the last part together. So we've got format delta where we're going to use the current value and this uh you know it's like past year value subtract those two items and then the format pattern is going to be whatever format pattern we put into this function as a string and finally all of that comes together where we have the current value and the past year value. Current value and the past year value is going to flow into growth to calculate what's the percent of the year-over-year growth.

**18:54** · Then we build the actual format string for the year-over-year growth using the current value and the number of digits from the current value. And it's going to do all of those comma things as well as all of those, you know, it's like um digit things that we talked about earlier. And then if growth is not equal to zero, we're going to format delta in a specific way. what is the current year minus last year in the format that we want and then format year-over-year arrow which is going to show the growth in the year-over-year format that we want and if it's blank give us a zero.

**19:29** · All of those things together seems like a lot, but that is what allows us to have this test.

**19:36** · say year-over-year growth reference for the current value which is uh total interactions and then the past year which is total interactions past year and then we have this value and just so that you can see that it's uh you know it's like nicely you know it's like set up total interactions is actually something that I have which is just counting the you know it's like rows on a specific interaction type so I can make that from chats emails escalations

**20:04** · it's just oh you know It's like fully functional, fully, you know, it's like filterable. It's just something that works nicely. And I definitely recommend you to check it out because this specific measure is something that I use in almost all of my reports because I think that adding reference labels is just a very powerful tool. The way that we throw this into, you know, it's like a reference label is, of course, if you're using the new KPI card, then we just have reference labels that we can just throw in and it's perfect. and I'd like to use this all of the time.

**20:35** · I think the user uh the value of userdefined functions really stems from the fact that now I have a bunch of different custom functions that I can use to you know it's like calculate and reformat measures as I please in a way that uh works for my specific reports.

**20:55** · But here's the thing if I'm working inside of an organization it's very likely that I will be using and reusing these format strings. you know, it's like all the time. So, I don't need to go back, look for that specific measure and try to, you know, like copy and paste it and put and, you know, like change all the measures. No, from now on, I can do this. Thanks for watching.

**21:15** · I really hope you learned something new today. If you're interested, uh, like I said, in making that SVG, definitely uh, you know, type check out the description for my online classroom.

**21:26** · Otherwise, have a great day and I'll see you next time. Peace.

**21:33** · \[Applause\] \[Music\]