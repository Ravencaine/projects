---
title: "What Does the “??” Really Do in Power Query M?"
source: "https://www.youtube.com/watch?v=YxzLS4KG-Yg&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=YxzLS4KG-Yg&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Goodly]]"
published: 2026-07-29
created: 2026-08-08
description: "Learn more about my M language Course - https://products.goodly.co.in/learn-m-powerqueryPower Query’s M language uses the question mark in a very useful way. In this video, I explain how a single q"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=YxzLS4KG-Yg)

Learn more about my M language Course - https://products.goodly.co.in/learn-m-powerquery  
  
  
Power Query’s M language uses the question mark in a very useful way. In this video, I explain how a single question mark can stop your query from breaking when a column or row is missing, and how double question marks can return an alternative value when the result is null.  
  
You’ll see practical examples of missing columns, row access, null handling, custom columns, and how to make your Power Query steps more robust and reliable. This is especially useful when working with changing or inconsistent data.  
  
  
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
Download the File ⬇️ - https://www.goodly.co.in/question-marks-in-power-query  
  
  
\===== CONTACT 🌐 =====  
Twitter - https://twitter.com/chandeep2786  
LinkedIn - https://www.linkedin.com/in/chandeepchhabra/  
Email - goodly.wordpress@gmail.com  
  
  
\===== WHO AM I? =====  
A lot of people think that my name is Goodly, it's NOT ;)  
My name is Chandeep. Goodly is my full-time venture where I share what I learn about Excel and Power BI.  
Please browse around, you'll find a ton of interesting videos that I have created :) Cheers!

## Transcript

**0:00** · Power Query is M language uses a lot of symbols and one such symbol is the question mark. In this video, I'm going to talk about that how can you use the question mark symbol creatively in your queries to make your queries a lot more robust. Not only I'm going to talk about one question mark, but I'm also going to talk about the use of two question marks. We'll talk about the concepts at the start and then we will learn the applications and examples of these concepts a bit later in this video.

**0:25** · If you happen to work a lot with Power Query and you would like to make your queries robust and dynamic, do not miss the video and watch it until the end.

**0:37** · Chapter number one. Let's just start with the question mark and what does it exactly do? The simple way to understand what the question mark symbol does in Power Query is that it tests the value.

**0:50** · If the value is not found, it would just return a null. It would be interesting to take a look at a practical example of that. Let's just start with a simple example where we have a three columnar table and of the three columns that we have right here, I would like to extract column three from this particular table.

**1:05** · How do I do that? I'm going to make a new step and that is the name of the table in the previous step and from this table I would like to extract column three. So, I will just write column three, press enter and sure enough column three gets extracted. Now, just in case if I just go back to the previous step, happen to delete column three, click on them, insert, and step is inserted which is where column three has been removed. If I come back to the next step, obviously it's going to return me an error because column three was obviously not found.

**1:28** · Now, what we are trying to do is in this particular step right here, I'm trying to get to column three and if not found, I would like to return the value as null so that my query does not break. So, all that I can do is put a little question mark in the end and it just says that, "Hey, check if you do find column three and if you don't find it, just return a null."

**1:50** · And all of that meaning is communicated by that question mark. If you don't find it, just return a null. I press enter and it just gives me a null value, and the query still works okay, but you kind of get a null value. You can also apply multiple instances of question marks one layer after the other. Interesting example, take a look at that as well.

**2:09** · I'm going to get rid of the removed column step right here, and delete that, and come back to the navigation step, which is where I have column three.

**2:16** · Therefore, I get the list, which is where all the values of column three have been extracted. Now, let's just say I'm trying to get to the 10th row, and obviously there are not 10 rows here, but I'd like to get to the 10th row, which doesn't exist, but I'd like to get there. So, I would want to write something like this. So, first this particular table, that's part one, then this particular column, which is found, that is part two, then I would want to write in the curly bracket that go to the 10th row, which is obviously not there.

**2:44** · Now, because I have a question mark after that, it is not going to return me an error because row number 10 is not found. Should I remove the question mark, and if I now press enter, it is going to give me an error, but if I apply the question mark, it is not going to give me an error. Now, just in case, if I also happen to remove column three, just delete that right here, you can now put two question marks, one after column three, and one after row number 10, that if you don't find it, then search for this value. If none of them are found, then give me the value as null.

**3:15** · Press enter, and it doesn't return you an error.

**3:22** · Now, this is an example, and obviously you wouldn't want to do such things inside of your queries. It's not very helpful, although they're helpful to understand what the question mark is doing, but not particularly helpful in a real-time query. So, let's just take a look at one example of this. One of the common places that you can apply the question mark technique is while applying filters or doing any checks against couple of columns. Take a look at this simplistic example, and I'm sure you can put it to more practical use when you use that in your own data sets.

**3:49** · So, I've got the same data, column one, two, and three, and perhaps I'm trying to make a new column trying to check that if the value is greater than 15 or not. For which I can go over to the add columns tab, create a custom column, and I can perhaps write a check in here. And the check is going to be something like, "Hey, why don't you take a look at the value of column 3 and check if that is greater than equal to 15 or not." And for which I am expecting to get two trues, which is the first one and the second one and perhaps this one as well.

**4:16** · I click on okay and we have one, two, and three trues, of course. Now, let's just say that if I happen to go back to the source tab and if I happen to delete column 3, delete that, click on insert.

**4:26** · Now, column 3 against which the check was performed is gone. Not anymore. So, if I just come back to the add custom step, obviously I am going to get an error. So, for which I can just go ahead and write something like, "Hey, why don't you take a look at column 3 and if you don't find it, {question mark}."

**4:41** · Now, this is going to nullify the entire column 3 because it is not found. And null greater than equal 15 is obviously going to give you null null null as a response. But, the error is kind of gone and you have no errors whatsoever. The problem at this stage, however, is that the only thing that the question mark has been able to solve for us is that the query did not break. But, is the null any useful? Are you able to do anything with it? Are you able to make something out of the null? The answer is no.

**5:10** · We're still at this stage where it's kind of useful, but not particularly helpful. So, we need to raise the bar and learn about not one, but two question marks. If you're liking this video thus far and you believe tricks like these are going to be super helpful, then do not forget to click the subscribe button. Also, showing some love and click that like button as well.

**5:30** · Let's just start with chapter number two on double question marks and how do you use that. Again, a three simple table query, column 1, column 2, column 3. And we have known that if I try to search for column 4, which doesn't exist, I am going to run into errors. And the way to resolve that error is one single question mark. So, let's just kind of base that as our existing learning and build on top of that. I'm going to click on the FX button right here to make a new step. I will put in the square bracket and I will say column four, which obviously doesn't exist, and I will put a question mark after that and I'll press enter.

**6:00** · And this obviously returns me a null value, which is okay for the query not to break, but not particularly helpful. So, what I'm going to do is now is that if I now put in the space and use double question marks, this double question marks simply means that if whatever is this, if this operation expression returns a null, then in that case, you can specify anything after this and I will execute that. So, double question marks checks for the null value and if the value is null, it can do anything.

**6:31** · So, for instance, I can write, "Hey, just write a zero." And it'll just give you a zero.

**6:36** · Or I can say something like more explanatory, which is something like not found. You can do that. Now, at the moment I am declaring numbers and text values here, but you can literally do anything after this. I mean, you can even write a formula or reference the entire table and it is just going to give you the table instead. So, the double question mark takes a look at the expression before that and the expression in case returns a null value, it will do anything that you have mentioned after that. Now, let's just take a look at the practical example of this.

**7:04** · We're working again with the same example just a while ago where we said that, "Hey, in case the column three, which we have just deleted in the previous step, if it is not found, then please consider this entire thing as null." And when the null value is compared against 15, obviously that is going to return in null in every single cell. Now, you could be content with that or perhaps you might want to return some value checking against the null.

**7:27** · And that is exactly how the double question mark is going to help you. So, I'm going to go back to this added custom step right here and that is my formula. Now, one thing to note in this entire formula is that I just can't start writing double question mark and then start writing the value here. I have to encapsulate this entire thing in the brackets right here because this entire thing is giving you a null value.

**7:50** · There is also like a sign in between, like a mathematical operator in between, and all of this needs to be encapsulated within the parentheses, and therefore it starts to realize that what is going to return the null value. So, therefore, I'm just going to go in here, I'm just going to use the brackets in here, and a brackets in here. Now, this entire thing is going to be tested against the null value. And in case if it is a null, then you can write a text or a really large number or something.

**8:13** · Maybe I'm writing a thousand here, or you could also do completely different operation whatsoever, like a table or something that you might want to do. So, click on okay, and that is a thousand. You could also have written some kind of formula in here, which could be a literal use case in your scenarios. But that is the use of a single and a double question mark.

**8:35** · In case you would like to learn the M language right from scratch, understand how Power Query works, how complicated transformation works in this particular example and more examples like this, I highly recommend that you take a look at my M course in Power Query, which is where I talk about a lot of simple to complicated fundamental concepts that you have to learn first, and then we build on discussing more complicated problems and solutions as well. In case you're interested, the link is going to be down in the description of the video.

**9:02** · \[music\] Yeah.

**9:08** · Yeah.

**9:08** · \[music\]