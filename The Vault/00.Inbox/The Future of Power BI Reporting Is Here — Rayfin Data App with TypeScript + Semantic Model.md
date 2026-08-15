---
title: "The Future of Power BI Reporting Is Here — Rayfin Data App with TypeScript + Semantic Model"
source: "https://www.youtube.com/watch?v=i9Zd5kd0wL8&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=i9Zd5kd0wL8&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[RADACAD]]"
published: 2026-07-06
created: 2026-08-08
description: "Power BI reports have always been delivered the same way. You build a PBIX. You publish to a workspace. You share the link. Users need a Pro license to view it.That model is about to change complete"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=i9Zd5kd0wL8)

Power BI reports have always been delivered the same way. You build a PBIX. You publish to a workspace. You share the link. Users need a Pro license to view it.  
  
That model is about to change completely.  
  
In this video, I show you the Rayfin Data App template — and why the combination of a TypeScript/React frontend with a Power BI Semantic Model backend is one of the most significant shifts in how we deliver analytical experiences to end users.  
  
This is not just a technical demo. This is a fundamentally different way of thinking about Power BI report delivery — one that is more flexible, more cost-effective, and more powerful than anything we have had before.  
  
Chapters:  
0:00 Introduction — building an app with TypeScript frontend and Power BI semantic model backend  
0:52 Demo overview — what this frontend actually is  
2:01 What is Project Rayfin / Fabric App  
3:09 The Data App template explained  
3:21 Naming and creating the project  
4:40 Reviewing the project structure in VS Code  
5:34 Using AI to build the report — the prompt  
7:15 What happens behind the scenes — connecting to the semantic model  
7:57 Security note — dev workspace vs production  
8:57 Publishing the app with npx rayfin up  
9:56 Viewing the published app in Fabric  
11:04 The more refined version — nicer UI, charts, three pages  
11:33 The cost story — Power BI Pro licensing vs Fabric capacity  
12:35 Sharing the app through the workspace  
13:16 Demo — creating a user with no Power BI license  
14:33 Demo — that user viewing the live app with a free account  
15:53 The real cost comparison — F2 vs Pro licensing  
17:00 Two things that are genuinely changing  
17:12 Will this kill the Power BI report?  
17:49 Closing thoughts  
  
  
🎯 What you will learn in this video:  
✅ What the Rayfin Data App template is and how it works  
✅ How a TypeScript / React JS frontend connects to a Power BI Semantic Model backend  
✅ Why this changes the way we think about delivering analytics to audiences  
✅ Live demo — building a Rayfin Data App project from scratch  
✅ Enhancing the app using GitHub Copilot prompts — no manual coding  
✅ The cost story — why hosting on F2 (or any low F SKU) and sharing with free Fabric users is dramatically more cost-effective than paying a Power BI Pro license per user  
✅ What this means for the future of Power BI reporting and report distribution  
  
💰 The cost-effectiveness story:  
This is the part that changes the conversation for every organisation distributing Power BI reports at scale.  
Traditional model: every report viewer needs a Power BI Pro license. For a large audience — that gets expensive fast.  
Rayfin Data App model:  
  
Host the app on an F2 Fabric capacity (the lowest SKU available)  
Share the app with free Fabric users — no Pro license required per viewer  
  
The semantic model powers the data layer — governed, secure, trusted  
The TypeScript/React frontend delivers a fully custom application experience  
  
For large report audiences — the cost difference is significant. And the experience your users get is far richer than a standard Power BI report embedded in a browser.  
  
🔗 Resources used in this video:  
🛠️ Rayfin on GitHub: https://github.com/microsoft/rayfin  
📖 Fabric Apps documentation: https://learn.microsoft.com/en-us/fabric/apps/overview  
🤖 GitHub Copilot: https://github.com/features/copilot  
🖥️ VS Code: https://code.visualstudio.com  
  
📺 Watch Part 1 — What is Rayfin and Your First Fabric App:  
https://youtu.be/lqkxnfhBexY  
  
📖 Related resources on RADACAD:  
🔗 What is Microsoft Fabric: https://radacad.com/what-is-microsoft-fabric/  
🔗 Semantic Model in Microsoft Fabric: https://radacad.com/semantic-model-in-microsoft-fabric/  
🔗 Microsoft Fabric Licensing — An Ultimate Guide: https://radacad.com/microsoft-fabric-licensing-an-ultimate-guide/  
🔗 RADACAD Blog: https://radacad.com/blog/  
  
💡 Power BI / Fabric Ideas: https://ideas.fabric.microsoft.com  
  
💬 Microsoft Fabric Reddit: https://www.reddit.com/r/MicrosoftFabric/  
  
🌐 RADACAD Website: https://radacad.com  
🔗 Corporate Training: https://radacad.com/corporate-training/  
🔗 Power BI Training: https://radacad.com/power-bi-training/  
🔗 Microsoft Fabric Training: https://radacad.com/microsoft-fabric-training/  
  
#MicrosoftFabric #Rayfin #FabricApps #PowerBI #SemanticModel #TypeScript #ReactJS #PowerBIReporting #FabricDeveloper #GitHubCopilot #DataApp #PowerBIEmbedded #FabricAnalytics #NoCode #FuturePowerBI

## Transcript

**0:00** · you can build an application that the front end of that is TypeScript, React JS, the back end could be Power BI semantic model, meaning that you can have a fully visualization report in your application without this being a Power BI report, but based on a Power BI semantic model. Project Riven, which I explained in another video, is a good example of that. Riven data app can give you exactly this, which would change the way that we are sharing Power BI reports with our audience.

**0:30** · We might change the way that we distribute our reports. So, this is going to change the future of Power BI reporting. My name is Reza Rad, and in this video I'm going to talk about that using a demo.

**0:51** · So, as you can see here, I have a front end, which looks like a Power BI report, but it is not Power BI report. It is a front end TypeScript. You see, this looks like a nice report with different pages of it. It is loaded in my Fabric or Power BI website, but in fact, this is not a Power BI report. The data comes from a Power BI semantic model, but the front end is TypeScript. This is built using Project Riven. How does this work?

**1:24** · How this is going to change the way that we are going to build applications moving forward. So, for those of you new to Riven, Riven or Fabric app announced very recently at Microsoft Build. This is a way that we can go and build applications, end-to-end applications \[clears throat\] that works with the rest of our Fabric objects. You can build an application that writes data into a database. You can also build an application that reads data from a Power BI semantic model and visualize it.

**1:56** · That application is a specific template of this application we call it data app. So, if I got if I want to go and start with this, I'll go into my VS code here. I would go and start from a scratch so that you can see the process. So, I'm going to start by creating a Reefing project.

**2:18** · To create a Reefing project, you can start with npm create Microsoft slash Reefing latest. So, this would give you the latest version of Reefing project.

**2:36** · Uh Reefing project can come with templates or you can start with a blank one. You see here that I can have the option to use a template.

**2:45** · Let me use my zooming tool so that I can zoom whenever is needed.

**2:51** · So, here I can choose to have a template. For this, when you choose to have a template, uh then there are four templates already available. You can also build other templates and there will be a more templates in the future. In my other video, I explained the to-do temp to-do app template. Now, I'm going to talk about data app template, which is a template especially when you want to visualize something from a Power BI semantic model. So, I would use that template and then it asks, "What should I call this project?"

**3:20** · Let's call this project I'm going to use this name.

**3:27** · My first data app one because I already have created one. So, what it does is that this will go and create that application for me. I'm going to close some of these windows that are not necessary. So, this is going to create that application for me as you can see on the side. Here, it created a folder in that application. I'm in VS code, by the way.

**3:52** · I haven't explained those uh uh steps because I have explained it in another video, in the video that I explained about uh how do we use Rayfin, how do we could get started with the Rayfin. So, you would need VS Code, you would need to install uh some of these libraries for um these functions to get working, and after that you can use this. So far, I'm not using AI or LLMs.

**4:16** · I'm just using the terminal window inside VS Code, which you can access it using the terminal window, uh and then uh start building your uh projects from there. So, you would need basically VS Code or any development environment plus those installation process of Rayfin, which I have explained in another video. Once you go through this, once you install it, you will have this project started.

**4:46** · This is a fully fledged project. It has uh the project files of a web application. It is actually a web application, so it would have sections that are like including Rayfin YAML file, including the source, which also includes different sections. You would have a section for your apps and projects. All of these sections are available here.

**5:13** · Uh once this is built, this is the basic template. You can go and build on top of this. So, it has built the very first building um the very first template.

**5:24** · I can go and run it using this in dev environment, or I can start by um by asking AI to enhance this. So, first I'm moving to that project. I have to move into that project, so I'm going to to that project using CD. I'm not using AI yet, but from now on, I want to use AI. So, what I want to say is that I'm going to copy this prompt and bring it here so that you can see what I'm looking for. So, my prompt is this.

**6:00** · I'm saying that in my application, which is the data app template of Raven, I want front-end three report pages connecting to this semantic model in my workspace. This is a fabric workspace.

**6:20** · And I'm asking this to go and build this visualization. So, this will take a little bit time because first it has to use some of the ways that it can connect to the Power BI semantic model, analyze it, then it finds all the ways that we can visualize it. So, it has combination of options here working together so that this goes and build something for for you. Once it builds it, you can actually go and enhance it even more. You can say, "Well, I don't like this theme.

**6:52** · I want to change this theme to something else."

**6:56** · So, you can go and build it exactly the way that you want. Um I have built already a project using this, which I can share it with you, but I'm just going to wait for this very first edition to be finished so that I can upload it into the service and you can see how this is working. So, all in all, I've just created this project and I've just asked AI to connect it to already existing semantic model.

**7:24** · Uh it might ask you questions like this that would you allow running commands. You can do this, but be careful to do it only in workspaces that are, let's say, your development workspaces. You You don't want to go and give AI access to do any modification in the production workspace. So, it is quite critical to make sure that you have done that. And this will also go through a authentication process as well, because I have been through that already. It doesn't ask me to do it again.

**7:57** · As you can see, this is using leveraging different components to connect to that semantic model, get the list of tables and fields from that semantic model, combine with the power of LLMs and AI.

**8:12** · This is then going to try to consider which fields are good for building reports, because I didn't really give this much of a requirement saying that these fields are what I want to build in the report. So, I'm basically just throwing a prompt and getting the result. To get the best result, of course, you can provide as much as documentation in terms of like business requirements, in terms of field definitions, metadata information, and that would give you much better outcome, of course.

**8:44** · Okay, now the app is created with these changes that I've made. It created the app, which I can run that npm run dev and see it in the dev environment. Uh but let's skip that. Let's say I want to publish it, because I want to show this how this is going to be available in the Fabric environment. So, I would say NPX rayfin up.

**9:09** · This means that I'm publishing this into a Fabric workspace, which it would ask me which Fabric workspace I want to deploy it to. So, as you can see here, uh NPX rayfin up asks me which Fabric workspace. So, I'm going to say Fab test Radhika. This is the name of my test workspace in Fabric environment.

**9:33** · So, by doing this, uh it does all the publishing, it creates a web app, and it gives me information about that web app as well as as well as the URL of that web app as well, uh, which you can use to browse this.

**9:51** · So, here you can see the URL of that web app.

**9:56** · And if I go to my Fabric environment, so I'll bring this over here, you can see I already have an app which I'm going to show you a little bit later, but in my Fabric environment, so if here if I go and search for that my first data app, uh, this is the one that I just published. And when I click on it, I should be able to see that very first draft of whatever I created, which I'm just going to look at it right now because I haven't tested it before. So, this is what it has created for me.

**10:28** · Pretty simple report with sections for products and customers.

**10:33** · Uh, now it may not be fully, um, nice designed yet, but you see this front end is not a Power BI report. This front end is TypeScript front end, which is normal for a web application. Behind the scene is a Power BI semantic model.

**10:51** · So, you can play with this AI agents and continue sending prompts to build a, uh, better application, which I have done that, and this is the other application that I have built, which is kind of similar to this with the difference this time is that, uh, I have a nicer UI, I have some charts used in here, and three different report pages. Nothing in here is PBIR or Power BI report.

**11:20** · This is normal TypeScript web application front end. Now, the interesting thing about this is that this is something I can share with my with my users, which brings us to really interesting point because if you want to share a Power BI with your users, your users would need Power BI licenses.

**11:44** · And this can be Power BI Pro licenses or Fabric capacities licenses that are considered as premium, meaning F64 or higher. We are talking about $5,000 a month for F64 or higher. Anything below F64, meaning that you have to pay pro account per users, which is $14. And I'm talking about US dollar here.

**12:10** · Uh so, if you have like 20 Power BI users, $14 per user, this makes it $280 a month to share this report with the users that are not self-service users. These might be just users wanting to browse this content. Whereas with this, with Rayfin Fabric app, which is a data app template, once I built this, I can share this throughout my workspace.

**12:39** · Now, a little bit later, this is like really preview edition, but a little bit later I would be able to share just the URL directly. But right now, if I want to share it, I can easily share that workspace with another user. So, I can go inside that workspace. I can go and say in the manage access of that workspace, and I can give access to a user. Uh it can be just a viewer access.

**13:07** · So, here you can see that I have given viewer access to a user, which is I called it no Power BI user.

**13:14** · Uh this is that user actually, no Power BI @redcat.com.

**13:20** · Now, because I already gave this access, you can see it here. Now, this user, if I bring the user detail also here, you can see that this user actually has no Power BI license. The only license that this user got is Microsoft Fabric free license. That means that this user can be part of a workspace, which is a Fabric workspace. It cannot consume Power BI content, but it can connect to this workspace.

**13:48** · And then what I've done is that on that semantic model that this workspace this app is connected to, I went to manage permissions of that.

**14:00** · And in that semantic model, I said that this user I'm going to give access to this user. So here you would just add that user. I've already done that this this step, but I'm just showing to you how this is possible. So I add that user and I would make sure that this user has the access to build content.

**14:22** · Again, this user just have Power BI free account. So once you do that, then you can actually get this user to log in into Power BI. This is This is that user. You can see this is that user opened an incognito web browser. I logged in with that user.

**14:43** · This user has a free account. It does not even have a trial account. You see the trial option is there. So no Power BI account, no paid account, just free account. But the app itself is in a workspace, which is uh Fabric capacity.

**15:01** · In my case, I'm using F2.

**15:04** · Right? And this user can see the app. So when the user come into that workspace and then search for the app, you see even the app that I just created is there, but that app that I've created before, the app is here. By By to different sections of the app, the user can see the data, live data here. What is the point point about this is that with this setup, I don't need to pay $280 if I have 20 Power BI users.

**15:36** · I just need to pay for that F2, which you can get it for $250 a month. And if you sign up for a yearly contract for that, it becomes even $156 a month. So, pretty much like half of the price of that.

**15:51** · And you would have your Power BI report sharing. Or if you have 100 users, the same. The load, of course, matters that F2 in some situation might not be good enough. So, you might need to go one level up. But the price point, I think, here would be much better compared to paying pro users if you have that situation. So, two things are available here.

**16:15** · One thing is that you can use this approach to share your reports with your audience in a much more cost-effective option, like the option that I mentioned to you. The other option is that I'm not really building Power BI reports here.

**16:31** · I'm building visual front ends that are TypeScript using AI agents, using LLMs. And this is something that is available now. This is something that in the past it would have taken us a lot of time to build it, but now using LLMs that they are really good at providing that HTML code and TypeScript code, they build that throughout the Raven project, then we host it and share it.

**16:58** · All of these combined together, in my point of view, is going to change the way that Power BI distribution and Power BI reporting, in general, would work in the future. It will not be the same.

**17:11** · Would this kill the Power BI report? I don't think so. There will There will be a still the need for Power BI report.

**17:18** · The self-service users, those users who want to have the self-service capability in every organizations, they would still use Power BI reporting because that is giving them the full flexibility. But for most of the users which are just report consumers, a platform like what I showed you using this data app works better and it would be much more cost-effective. So, the future of Power BI visualization is going to be in this way. My name is Reza Reza Rad. I hope you like this video.

**17:50** · If you like this video, go ahead and subscribe into our YouTube channel. We have weekly videos on Power BI, Microsoft Fabric, and especially these days how they work with the AI. Until the next video. Bye.