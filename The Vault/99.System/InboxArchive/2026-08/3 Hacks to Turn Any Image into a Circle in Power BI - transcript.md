---
uid: 2026-08-13-3-hacks-image-to-circle-power-bi
title: "3 Hacks to Turn Any Image into a Circle in Power BI"
source: ""
date: 2026-08-13
duration: 12:48
language: en
video_file: 99.System/Attachments/Video/3 Hacks to Turn Any Image into a Circle in Power BI-exTSUPJPSqE.webm
tags: [video, power-bi, circular-image, image-url, svg, base64, decision-guide]
created: 2026-08-14
---

# 3 Hacks to Turn Any Image into a Circle in Power BI

![[3 Hacks to Turn Any Image into a Circle in Power BI-exTSUPJPSqE.webm]]

## Transcript

[00:00:00.000] You're using images in your Power BI reports, however, they show up squared.
[00:00:03.680] And what you're looking for are circular images. Now, how can you achieve that?
[00:00:07.200] In this video, I'm going to show you three different ways to do exactly that.
[00:00:11.040] Now, how easy these are, that depends on your situation. Let's have a look together.
[00:00:16.880] Well, let's start with the most ideal scenario where you have direct access to the image files that
[00:00:22.320] you're using in your Power BI reports. So, not just the image URLs, but really the files themselves,
[00:00:28.480] like on your laptop. Now, here you see the squared images. And we could simply make them circular.
[00:00:33.200] Now, how to do it? That probably depends on how many images you have.
[00:00:37.120] If you just have a few, then you could just go to Power Point, for example.
[00:00:41.520] Now, in Power Point, you could simply add your image, then go to picture format,
[00:00:45.520] and then use the crop to shape feature, and then choose a basic shape, like an oval.
[00:00:51.680] And that's it. Now, you can right-click on the image and save as picture.
[00:00:56.560] And then, once you have the circular versions of all your images, then of course,
[00:01:00.400] you need to update the links to these images in your data set.
[00:01:04.240] Now, over here, you see I'm using Dropbox. Here, I have a field of column with all the squared
[00:01:09.520] image links. And now, I add an extra column with all of the circular image links.
[00:01:15.200] And that's it. And then you use those in your Power BI reports.
[00:01:18.240] To my report, I could go to the new card visual, then formatting options,
[00:01:22.880] images you see it's done on. And then, here, I'm using image type and image URL.
[00:01:29.200] Then, click on the Abax button. And here, I can use that new column with the circular image links.
[00:01:36.400] So, field value, then here we have all data, I'm read data, and then I just scroll down to the
[00:01:44.000] image circle link. Okay. Now, another thing that you need to make sure of is that for that new field,
[00:01:49.200] image circle link, you have here data category image URL selected.
[00:01:54.800] All right. Now, this works if you have direct access to the images. Plus,
[00:02:02.000] if you just have a few, because if you have to do this for hundreds or maybe even thousands of
[00:02:05.600] images, this is not realistic. Although, you could also just run a Python script. And you don't
[00:02:11.920] even need to know Python really to run that script. You can use chat GPT or cloud. Let me show you.
[00:02:18.240] Here, just say, write a Python script that makes all the images in this folder circle. Of course,
[00:02:31.280] you need to have Python and the write libraries installed. And once you have that, you can just use
[00:02:36.960] exactly that script that it generates for you. So, now, I just open command prompt, go to that folder,
[00:02:43.520] and then run that Python script. And boom, that's it. And you see, if I would have had hundreds or
[00:02:50.560] thousands of images, now I have the circular version of them. And then of course, I could run another
[00:02:56.240] script to get the URL links to these images. All right. Now, but let's say that you don't have the
[00:03:03.040] convenience of having these images, these images files directly on your laptop. Then what can you do
[00:03:09.840] in that scenario? Well, in that case, we have an easy solution and a bit more difficult solution.
[00:03:15.120] Now, let's start with the easy one.
[00:03:31.760] Now, let's not overcomplicate it. If your images always show an exactly the same position,
[00:03:37.200] then you could just create an overlay that circular. So, let me show you. I can go over here to
[00:03:43.760] insert image. Now, here you see, I created a mask which is white on the outside and transparent
[00:03:50.160] in the middle that circle that you see. Now, that's the image I'm going to use. I'm just going to
[00:03:55.120] resize in a bit and then overlap it with the employee images. And then it's just the matter of
[00:04:02.640] positioning it correctly. And you see, boom, we have it showing circular. Even though that
[00:04:08.560] the real image is square, we now have a mask over it. Simple as that. If you don't know how to create
[00:04:14.320] an image like that, just check out the download files or again, you can use PowerPoint. You basically
[00:04:20.240] just draw a square. And then you insert a second shape which is going to be a circle. Now,
[00:04:26.240] let me give that circle a different color. And then you can combine the two shapes. So I select both
[00:04:31.680] of them. Go to shape format, merge the shapes. And you see, here we have the combined option.
[00:04:37.680] And the middle one created a hole and what we are left off with is just the outside. And the outside,
[00:04:43.120] you give the same color as what you have in your guard visual or whatever you're using it. So,
[00:04:48.240] in my case, white. And I don't want to have a borderline so no outline. And that's done the image
[00:04:53.680] that we can save. All right. Now, very simple but might be effective, especially if you don't have
[00:05:00.800] direct access to the files of these images. And so you get them through a URL or maybe you have
[00:05:09.200] new employees joining every time and you don't want to put every single new employee make this
[00:05:14.400] image circular. Then this could be a good option. However, this might not always work. For example,
[00:05:20.400] if you're using images in a table, right? As soon as you start scrolling, well, you will see that
[00:05:26.720] overlay. Now, let me show you over here. I have a table with the image link field. I would have
[00:05:33.120] my overlay. Now you see, now everything looks more or less fine. But if I start scrolling,
[00:05:38.640] you would see that there's an overlay, not very clean. So in this scenario, where an overlaying
[00:05:44.080] mask doesn't really work and you don't have access to the image files or they're just too many
[00:05:51.280] and new ones showing up every day. Well, what to do done? What if you just have the image links?
[00:05:56.720] Now, now we get to the trickiest option. However, can be very effective. Let me show you. We can actually
[00:06:02.880] create a measure that takes the image and makes them circular using SVG. So here you see I have
[00:06:09.520] a measure called image circle. Then here the first variable takes the image and then I'm going to
[00:06:15.840] use that variable inside of some SVG code. Now, the relevant part here is this. We create a clipping
[00:06:23.200] path with the ID circle view. Now, the parameters that you fill out here depend on how big the SVG and
[00:06:30.720] the image is going to be. And so over here, I put the radius a little bit lower than 50, half
[00:06:36.640] of 100. So let me have a bit of the outside got off. All right. And this I basically apply as a mask
[00:06:45.840] to that image. All right. Now, let's see if that works. So this measure I'm going to use
[00:06:53.040] here in my visual. So images have X, all data. And here I'm going to use that image circle measure.
[00:07:02.480] I see perfect. It is working. We have circular images of our employees. However,
[00:07:07.840] it is a bit more tricky than this. Now, let's go back to that measure. Now, here you see not a link,
[00:07:14.800] a URL link like we had before. You see I'm pointing to a column that's called image base64 compressed.
[00:07:23.360] Now, why is that? Why can't I just say here? I want to use that image URL. Now, let me show you
[00:07:30.720] what actually that would happen. If I look for my image link column, then now it doesn't work.
[00:07:38.800] Because Power BI I think is blocking external links that are being used in the SVG code. So
[00:07:46.240] what we have to do is stop in between. We have to take these images and convert them to base64,
[00:07:52.640] which is just a text version of the image. All right. So that you don't have to point to an external
[00:07:58.720] location, which also has the advantage if the link would have a break. You still have the images
[00:08:03.920] as text basically. All right. Now, but how can we do that? Now, the way to do that is either to use
[00:08:10.560] an external tool. That's one option. Or you can actually also do it in Power Query. Now,
[00:08:15.840] let me open Power Query. And here on the left-hand side, you see I created a custom function. Now,
[00:08:21.280] sounds fancy, but it's actually really easy to set up. So you would just have to go here to
[00:08:25.760] home, new source, blank query. All right. And then let's have a look at the code. Yeah, you see the
[00:08:32.160] formula bar, but I want to open up the advanced editor. Then you see that the function just takes the
[00:08:36.800] image around and then converts that to base64 for using one of the standards and functions. Now,
[00:08:45.760] here there's just still an if condition because if we are using base64 in Power BI,
[00:08:52.480] there still needs to be a prefix. And that prefix needs to have either PNG, GIF, or J back,
[00:08:59.680] depending on the image type. All right. So a little bit longer. Now, you can just take that code,
[00:09:05.200] right, and then use that for a new custom function. Now, give it a name, for example, URL to
[00:09:10.720] base64. And then you can invoke that custom function to create a new color. So add column,
[00:09:18.400] info, custom function. Now, here in my case, I've already done that. And you see the name of this
[00:09:23.920] column is image base64 function query URL base64. And then over here, the input, which is the image
[00:09:31.760] link. And that's it. And that creates a new column, which is this one over here. Let me select one
[00:09:38.560] sound. And you see the text version of that image. Now, does that work? Let's have a look. If I go
[00:09:46.080] back, of course, you need to load that query. And instead of using that original URL link,
[00:09:50.960] I'm going to point to that base64 image column that we just created. So here we have that field,
[00:09:58.880] image base64. And the result, a little bit disappointing. You see, as if it's loading the image,
[00:10:04.480] but only got halfway, or not even that. Now, what's going on is that these text banks are really
[00:10:11.040] long. So over 32,000 characters in this case. And in a cell with a text column at text data type,
[00:10:20.160] you can only have a maximum of about 32,000 characters. So we have to convert it to base64, but
[00:10:27.200] somehow get, you know, like a shorter version of it. So what we can do is compress it, change the
[00:10:35.760] dimensions so that this base64 text string is a bit shorter. And that's where it gets a little bit
[00:10:42.160] more complicated, because that standard image to base64 function that am has doesn't allow you to
[00:10:51.520] compress it or change the dimensions. Now, how did I solve it? Let me go back to our query. Now,
[00:10:57.680] here, I also created another function URL to base64 compression. All right. And there, if I open the
[00:11:04.640] advanced added term, that is beginning part is just specific for Dropbox. So if you're not using
[00:11:09.360] Dropbox, you can just ignore that. But you see, I'm using an external API from reserve.now. So basically,
[00:11:16.560] it's doing the same as this, I'm function from before. However, it also applies compression first
[00:11:22.720] and changes the dimensions to whatever you specify over here. So that we get a shorter text string.
[00:11:29.040] All right. Now, once you have that function, then you can go back to your data set.
[00:11:34.000] Now, here you see, follow those exact same steps. So you see, I invoke that custom function,
[00:11:39.360] but now using that URL to base64 compression function. And once you have done that,
[00:11:44.960] then you can go back to your measure and instead of that image base64 column, and now I'm going to
[00:11:52.000] point to the compressed version of it. And there are here, we have circular versions of our
[00:11:56.720] empty images. Now, definitely the most tricky one to implement. And you also have to double check
[00:12:02.720] if it's fine to use that external API with those images that you are visualizing. So that's another
[00:12:08.960] aspect to consider. However, it might fit exactly your scenario. So I give you three options,
[00:12:14.960] which one did you use in the past? Which one would you use going forward? And maybe you have some
[00:12:21.600] other ideas, share it in the comments section below. If you're interested in building reports
[00:12:26.080] together with me, learn all of my tips and tricks around really solid Power BI report development,
[00:12:31.680] then check out my upcoming Power BI design transformation course over here. We're just starting
[00:12:37.920] in September. If you just want to see more videos about everything related to Power BI,
[00:12:44.320] then check out these videos over here. Thank you for watching and see you in the next video.