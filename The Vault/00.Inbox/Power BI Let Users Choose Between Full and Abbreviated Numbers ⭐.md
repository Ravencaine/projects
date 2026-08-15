---
title: "Power BI: Let Users Choose Between Full and Abbreviated Numbers ⭐"
source: "https://www.youtube.com/watch?v=jQA33mjVJH0&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=jQA33mjVJH0&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[DAXJutsu]]"
published: 2026-07-20
created: 2026-08-08
description: "Want to give your users more control over how numbers are displayed? In this video, you'll learn how to use a slicer, dynamic format strings and  DAX User-Defined Functions to let users switch between"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=jQA33mjVJH0)

Want to give your users more control over how numbers are displayed? In this video, you'll learn how to use a slicer, dynamic format strings and DAX User-Defined Functions to let users switch between Auto display units and full values, making your reports more flexible and user-friendly.  
  
#PowerBI  
#MicrosoftFabric  
#powerbitips  
  
Sample PBIX  
https://1drv.ms/u/c/5f8ed775d41b4aac/IQDAbwuHr5jQTJuxLzHjcncjAXlR9wnwp-RK3sGh2Fkf2co?e=skYpYs

## Transcript

**0:05** · Hello I'm Dane welcome to another episode of Dark YouTube. In today's episode we'll discuss how to auto format and not auto format numbers.

**0:14** · So basically what we're going to do is we want to be able to switch between auto formatted and not auto formatted numbers.

**0:24** · So why do we want to do that?

**0:27** · Because sometimes if the number is too long it gets harder to read. For example um it says here 11,824 and have 40.

**0:43** · So sometimes it will be easier to read it as 11.82 million, right?

**0:49** · So what we're going to do is is we will not be using the format function because format function returns a text.

**0:56** · Instead we'll be using dynamic format strings. In this case I already have the format string prepared.

**1:16** · \[bell\] Oh, what is that?

**1:25** · Here we go.

**1:27** · So this is our format string. So this is what's going to do. If the absolute value whatever measure we will be applying the format string to is zero then return zero. If it's one but though it can just return uh can just return the decimal number. 100 1,000 and uh the trailing comma here denotes the number is to be divided by a factor of 1,000.

**2:16** · So, if you see two commas, then that will be here. If you see two commas, that will be a million. And if three commas, then a billion. So, let's try this one.

**2:30** · Copy this.

**2:32** · And let's select a measure, and we will try to apply this to sales. Go to dynamic and copy-paste that.

**2:56** · Format string.

**2:58** · And now our sales is formatted, but this is a bit manual because we'll have to apply the same formula for all the measures. So, instead of using instead of using the same formula, let's just create a DAX user-defined function. And the simplest way to do that is by going to the model view and model tab under data pane. And let's look for functions. I already have the function added here.

**3:47** · Oops.

**3:52** · I can just this one and paste. And you want to make sure that Okay, so want to make sure that we have this. So, this is a four This is a DAX UDF without any parameter.

**4:16** · Okay.

**4:17** · Undo.

**4:20** · So, we go back to that measure sales amount and format. Instead of using these rows of DAX formula, we'll be using FN number dynamic format string, which is the name of our measure. And So, it will be applied to sales. And we can do that for say quantity.

**4:54** · Dynamic FN Okay, so what if the user wants to see the absolute number, the numbers without formatting? So, what do we do?

**5:08** · So, we go back again to our uh function. And you will add it this. So, what are we going to do is we'll be adding parameters. And then we'll bind the that parameter to the slicer selection. So first we want to be able to select whether we want it formatted or not. So, I'm I'll be adding a format parameter.

**5:59** · And this will be a string with a default value of auto. And we will know what auto means later. Auto and Next is we will have our decimal place. Which is going to be an integer. And our default value is zero. So, it's up to us whether we want the numbers to have decimals or not. And then, our currency is we might want to add currency. And currency is a string.

**6:48** · And default value is none. So, it's up to us whether we want to have currency or not. And this one will be our auto. So, for example, if uh the slice selection or the value by format parameter is auto, then we return this value. If none, var none, then we create another format. So, what should we do? Hmm.

**7:37** · Let's say 0.

**7:48** · And we want to repeat You want to repeat a decimal by our decimal parameter. And return switch format auto then auto.

**8:32** · None then none.

**8:37** · And we add our currency to currency.

**8:57** · And this.

**9:01** · And of course this we can actually can go back to this or which one? Sales amount.

**9:21** · And format.

**9:23** · Now in our Uh let's go back. We have this currency. Let me just copy this and paste this in a text box. So, I can I have a reference of what the parameters are.

**10:05** · Builds them out.

**10:11** · Format a default is auto.

**10:15** · Let's say none.

**10:18** · What happens if we select that?

**10:20** · Right?

**10:21** · Not formatted.

**10:23** · And before got to add a comma. So, let's go back to our um function. And let's add a comma.

**10:45** · Mhm.

**10:48** · Okay, so what's wrong with our sales?

**11:04** · It's inverse.

**11:07** · Two.

**11:10** · Mhm.

**11:12** · A weird Now I know. This should be none and not none.

**11:25** · Okay.

**11:26** · There we go.

**11:29** · It says none.

**11:31** · Let's go back again.

**11:33** · Format, none.

**11:42** · And decimal, let's say two. And currency is dollar.

**11:52** · Okay?

**11:55** · So, what if you want to switch between auto and not auto formatted. So, I already have a table with a custom table that says format string auto and format string is none. And we'll be using this in a slicer. Let's add that to the slicer. Format \[snorts\] And let's make this single select.

**12:54** · Four selections, auto none. And we'll be binding our function or our format string to this slicer. Format selected value format string format string. For none auto none And we'll be applying the same format string to all other measures.

**13:50** · Cogs dynamic format profit dynamic format quantity quantity format All right. We don't need the dollar sign.

**14:39** · Okay.

**14:42** · So, this is how you auto format and not auto format your numbers. So, that's it from me. I hope you learned something. Thank you for staying with me and have a good one. Bye-bye.