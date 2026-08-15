---
uid: 2026-08-11-ai-power-bi-workflow
title: "AI Power BI Workflow - Drop Materialized View"
source: "https://www.youtube.com/watch?v=rDuHokI3YBQ"
date: 2026-08-11
duration: 00:04:41
language: en
video_file: 99.System/Attachments/Video/rDuHokI3YBQ.mp4
tags: [video, ai-power-bi, power-bi, dax, workflow]
created: 2026-08-11
---

# AI Power BI Workflow - Drop Materialized View

![[rDuHokI3YBQ.mp4]]

## Transcript

[00:00:00.000] Hey, all. My name's Ned. I'm a Microsoft MVP with a focus on Power BI and in today's video,
[00:00:04.799] I'm going to be showing you and talking about how AI is changing the way I build Microsoft Power BI
[00:00:10.320] reports because it is having a real impact on my day-to-day workflow. And the way I'm going to do
[00:00:15.439] that is with a really simple demo. Hopefully, you'll see and you'll be inspired to see if you can
[00:00:21.199] also implement in your own workflows. So with that, let's jump to the computer and let's take a look.
[00:00:26.320] Now, the real change for me is that it happened when Power BI introduced PBIR or Power BI enhanced
[00:00:33.439] report format as the default Power BI report format. What this means is that if you're in Microsoft
[00:00:39.759] Power BI and you want to save a report and you save it as a Power BI project file, you get to see
[00:00:48.000] all or the entire report definition in JSON in a different report structure. So this right here is a
[00:00:55.600] Power BI report that has been opened up in VS code. So as you can see, I have a definition folder
[00:01:03.200] and then within that definition folder, I have various JSON files that actually represent or
[00:01:09.040] make up the report. Now, this file format makes editing a Power BI report with an AI agent or code,
[00:01:16.159] really simple because when you open up one of the JSON objects, you'll have a schema up top,
[00:01:21.519] which the AI agent or code can point to to see exactly how a visual should be structured and
[00:01:29.150] then you can actually edit the visual by simply making a change to the code. With the new Power BI
[00:01:35.310] AI agent skills, you also now get a CLI that then allows you to reload the report based off of the
[00:01:42.909] code in real time by simply typing Power BI desktop space reload. And if you have Power BI open,
[00:01:50.349] it will automatically refresh the Power BI report in the background. So what that means is you can
[00:01:55.709] make a change, go Power BI desktop reload and then hit enter. Now, well, I am often having the
[00:02:02.349] actual AI agent make the change to the report. What I also am doing is I am creating things like
[00:02:08.509] PowerShell scripts. Now PowerShell scripts, if I have the AI agent right, it can automate certain
[00:02:15.150] kinds of design rules. So this, for example, is a PowerShell script that when I select a
[00:02:22.349] group in a Power BI object, will automatically create an evenly spaced shape around that group
[00:02:30.669] with the right amount of padding, which makes formatting really, really simple. So let me give you
[00:02:34.669] a quick demo as to how this works. So I'm going to delete these shapes. And then I can go into
[00:02:44.180] VS code here, hit run on the PowerShell script. And then it will ask me for a page ID, which I
[00:02:51.139] can get by simply right clicking and then going copy page ID, pasting in the object ID right there.
[00:03:00.099] And then go back and we're in it will ask me for a group ID, which I can get by right clicking
[00:03:04.580] and then going copy object name right here. And then giving it saying, hey, I want to shape with a
[00:03:10.900] padding of 30 picks around the group and hitting enter and then simply typing right here Power BI
[00:03:17.699] desktop reload at which point when we go back into Power BI desktop, we now have a nice evenly
[00:03:26.270] spaced shape. Now this is really cool because what I can then do is I can delete the shape back out.
[00:03:32.990] And let's just say these slicers were randomly placed over here. Right. So we're going to change
[00:03:39.120] the shape that I want. I can go ahead and hit save. And then I can simply rerun that by clicking
[00:03:46.610] this run again. Again, we'll just copy that same page ID from above right here. Copy that same
[00:03:54.610] group ID right here. And then saying, hey, I want padding of 20 picks and then going Power BI desktop
[00:04:04.719] reload. And just like that, I now have a different shaped box or border. So scripts like these are
[00:04:13.860] changing how I build reports, creating an perfectly evenly spaced shape like this previously would have
[00:04:20.180] probably taken me five, 10 minutes. Now it takes me 10 seconds and it's all because I have this
[00:04:24.980] really easy to use script that I built in a few minutes using a link this script down below on my
[00:04:30.740] GitHub and the video description, by the way. So with that, you've reached the end of today's
[00:04:34.500] video. I know it was a quick one, but if you enjoyed it, you don't give it a thumbs up and hit
[00:04:38.660] the subscribe button. And with that, I'll catch you in the next one.