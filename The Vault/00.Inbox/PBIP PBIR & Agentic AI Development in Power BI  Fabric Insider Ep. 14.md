---
title: "PBIP PBIR & Agentic AI Development in Power BI | Fabric Insider Ep. 14"
source: "https://www.youtube.com/watch?v=-YH-Yue_pPY"
video_url: "https://www.youtube.com/watch?v=-YH-Yue_pPY"
creator: "[[RADACAD]]"
published: 2026-08-07
created: 2026-08-13
description: "PBIP and PBIR are becoming the default project format for Power BI. And they are the foundation for something much bigger — agentic AI development directly inside Power BI.In this episode of Fabric"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=-YH-Yue_pPY)

PBIP and PBIR are becoming the default project format for Power BI. And they are the foundation for something much bigger — agentic AI development directly inside Power BI.  
  
In this episode of Fabric Insider, I sit down with Rui Romano — from the Power BI team at Microsoft, working on agentic development and the PBIP/PBIR project format — for a deep dive into what these formats actually are, why they matter, and how they are becoming the backbone of AI-driven Power BI development.  
  
If you have heard the terms PBIP and PBIR but are not sure why they matter — or if you are already using AI agents to build Power BI content and want to understand the architecture underneath — this episode is for you.  
  
📌 What we cover in this episode:  
  
📁 What is PBIP and PBIR — and why should users care?  
🚀 PBIP/PBIR going GA and becoming the default format  
🤖 The impact of PBIP on AI-driven development  
🧠 How AI is changing semantic model creation and development  
🔌 The full agentic stack — MCP Server (Authoring), Skills, PBIP, and the IPC Bridge working together  
✍️ Customizing skills — naming conventions and team standards  
🗺️ What is coming next  
  
🎙️ Fabric Insider Series — direct conversations with Microsoft product team members on what is new, what is coming, and what matters most in Microsoft Fabric and Power BI.  
  
🔗 Rui Romano on LinkedIn: https://www.linkedin.com/in/ruiromano/  
  
📺 Full Fabric Insider Playlist: https://www.youtube.com/playlist?list=PLMXQvYI7QV6f8vUxtlFuGzQk-tYj3uOTn  
  
🎧 Fabric Insider on Spotify: https://open.spotify.com/show/4eJrCr5UOWZ7ggmrVUce6l?si=Jx18sgdaScCgR3P1oDz-dw  
  
📚 Fabric Insider Blog Series: https://radacad.com/category/fabric-insider-2026/  
  
💡 Power BI / Fabric Ideas: https://ideas.fabric.microsoft.com  
💬 Microsoft Fabric Reddit: https://www.reddit.com/r/MicrosoftFabric/  
  
📌 Previous Fabric Insider Episodes:  
🎙️ Ep. 1 — Wilson Lee: Fabric Mirroring, Copy Job & SAP Integration  
🎙️ Ep. 2 — Zoe Douglas: Power BI Visualization Updates & Roadmap  
🎙️ Ep. 3 — Miguel Escobar: Power Query, Dataflows & What's Next  
🎙️ Ep. 4 — Santhosh Kumar Ravindran: Fabric Spark Performance & Custom Live Pools  
🎙️ Ep. 5 — Christian Wade: What's Hot and New for Power BI Semantic Models  
🎙️ Ep. 6 — Yitzhak Kesselman: Real-Time Intelligence & Fabric IQ  
🎙️ Ep. 7 — Rie Merritt: Everything About the Microsoft MVP Program  
🎙️ Ep. 8 — Hasan Abo-Shally: Fabric MCP Servers, CLI & AI Agents  
🎙️ Ep. 9 — Wee Hyong Tok: Data Integration, Migration & Future of ETL  
🎙️ Ep. 10 — Mohammad Ali: The Next Evolution of Power BI  
🎙️ Ep. 11 — Sachin Patney: Fabric Apps & Rayfin Deep Dive  
🎙️ Ep. 12 — Josh Caplan: OneLake Updates & Vision  
🎙️ Ep. 13 — Kay Unkroth: DAX UDFs, Query REST API & Outbound Access Protection  
  
📖 Related resources:  
🔗 Power BI Agentic Development Overview — Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/developer/agentic/power-bi-agentic-overview  
  
🔗 No-Code Power BI Report Authoring with GitHub Copilot + Fabric Skills + Power BI Desktop Bridge: https://youtu.be/LdAl8Ar7E5M  
  
🔗 Teach Claude Your Power BI Standards — Custom Skills for the Power BI Modeling MCP Server: https://youtu.be/t36exxydktU  
  
🔗 No-Code Power BI: How to Use Claude and the Power BI Modeling MCP Server: https://radacad.com/no-code-power-bi-how-to-use-claude-and-the-power-bi-modeling-mcp-server/  
  
🔗 RADACAD Blog: https://radacad.com/blog/  
  
🌐 RADACAD Website: https://radacad.com  
🔗 Corporate Training: https://radacad.com/corporate-training/  
🔗 Power BI Training: https://radacad.com/power-bi-training/  
🔗 Microsoft Fabric Training: https://radacad.com/microsoft-fabric-training/  
  
#PowerBI #PBIP #PBIR #AgenticAI #MCPServer #MicrosoftFabric #FabricInsider #RuiRomano #PowerBIDeveloper #AIAgents #SemanticModel #FabricAnalytics #BusinessIntelligence #GitHubCopilot #NoCodePowerBI

## Transcript

**0:00** · Hello everyone, welcome to another episode of Fabric Insider. This time we have the pleasure to be with Rui Romano from Power BI and Fabric larger team here. Hey Rui, how are you doing?

**0:12** · Hey Reza, I'll I'm good. Hope you as well and thank you for inviting me. Great to be here.

**0:20** · Thanks for thanks for being here.

**0:24** · \[music\] Now before we talk about what are focus areas of you, can we talk a little bit about yourself? Can you give us some introduction who you are, where do you live, what part of the product you own and how long you've been with Microsoft?

**0:45** · So okay, my name is again my name is Rui. I live in Portugal in Porto.

**0:52** · So this is actually the Power BI Porto user group which is a user group that I helped co-found and we are very proud of it. And I did the journey from consulting to to product. So I started as a Microsoft not even even before Power BI always focused in data and and from like SQL Server and I started I think was SQL Server 2000. So the first actually I think it was a second analysis services.

**1:22** · There was something before that but I didn't do that. So like I think 15 years on consulting in a company called Dex scope here in in Portugal.

**1:32** · And and then I I moved to Microsoft to the cat team where where I got the pleasure to work with the superstars of of Power BI and legends like Chris Webb and Phil Seamark and Matthew Roche. So I learned a lot there and actually it was it was a really nice team to to work uh and uh and then I got the opportunity to uh because because the CAT team is still in the product.

**2:03** · So, it's it's kind of uh uh like the voice of the customer within the product. And uh and then I got the opportunity to move to uh feature PM uh and and live the dream because uh I got the opportunity to lead and drive features like the the Power BI developer mode, the Power BI project, and the TMDL, uh the or TIM the and the PBIR, which

**2:33** · uh if you know me from back in the day in consulting and I was also a Microsoft MVP, I was talking about and and I did a lot of talks and uh I I think I I I went to Definity Yes, yeah.

**2:45** · and and the the the talk I did there was the Power BI hacks, which \[laughter\] which was all about like how how how you can do source control, but without in an unsupported way or unsupported manner.

**3:02** · And uh And it was like uh I don't know, the strange coincidence that I got the opportunity to to implement those features. And um and yeah, I'm really proud of that, especially about the uh seeing the impact that we had with uh especially with pro dev developer teams uh because I literally felt that pain.

**3:25** · Uh and um and yeah, so and and these days And uh and by the way, I'm a product manager on the Power BI team. So, that within Fabric. Uh and uh and these days I'm uh a lot more focused and agentic and how to um how we can make uh Power BI accessible and addressable by AI agents from uh not not very focused on the consumption side.

**3:52** · So, that's the Fabric IQ and which is one of the IQs of the Microsoft IQ, Work IQ, Fabric IQ, Foundry IQ. So, Fabric IQ is what can give you the the the state of your business. So, the ability of the knowledge to your agents about the data that lives within Fabric and and in particular semantic models.

**4:14** · Um I am more focused on the giving agents the tools, the skills uh to so they can create, so they can do things for you. Uh there was something that I learned from uh my mentor who I which I don't know if you know him. Uh his name is Ric Cantina. I don't know if you remember him. He He was also a a Microsoft MVP.

**4:39** · All right.

**4:40** · And he always told me in the beginning of my career like like we should be lazy and and we should lazy is a good thing.

**4:47** · So, we should not be accept that we we have this repetitive task and we just do it just for the sake of fun or just because someone told us. Uh so, we should always be lazy and I and I I look at a gen tick today and it's the perfect opportunity to be lazy because you now you can just you have just have this uh uh fleet of agents that you can train yourself by yourself. You can you can give them and that's the beauty, right?

**5:17** · It's you can give these agents this your style, how you like to do things.

**5:25** · You can how your team likes to do things. And uh and then they do they just do it for you. And um and uh and and we did a lot in the last year or so. So, with the MCP, with the skills, with the PBIP. Uh but there are there are still things that we need to do and uh and we are doing uh to make again the ability to to give the AI agents the ability to um to just do more, but it's not just doing.

**5:55** · It's doing and verifying and and testing and and and allowing you to create the e-vals that you can make sure that whatever the agent is doing, it's it's up to the standard that you define as a professional or as a team.

**6:13** · Uh so yeah, this was a little bit more than an introduction, but \[laughter\] No, that's that was perfect. Yeah, I do remember your talk in the Finity conference which was Power BI hacks and and I have to say that you are like the perfect fit for this role in Microsoft because you've been talking about how we just at PBI X we could manage to do these hacks. Now you are building the product and shaping it in a way that can cover all of these.

**6:39** · Fantastic. Now It has its pros and cons, okay? It has its pros and cons. So I think that the pro is that it is definitely I felt the pain and I can be very passionate, but sometimes it's it's also um it's also good to just think outside of the box. And uh and uh Yeah, that's right. Yeah.

**7:01** · And it's And again, yeah, hav- having the experience and having the like feeling the pains of of the of the product on the on the misses, it's it is a good thing, but I learned and I learned in the good way that Yeah, it's it's sometimes what we feel that it's really important, in the end it's not.

**7:24** · In the end, like you like you you think that okay, everyone is going to use this feature or this thing that you feel is really important because you you are very like you you you you felt that pain or you you you you you felt that problem, but in the end it's I don't know, you have like 500 people from 3 million 30 million using it and

**7:45** · and then you need to learn the the right way to really okay, maybe that was not as important as I as I thought and uh and we are very very data-driven on the team and um but it's Yeah, it's it's It it has it's definitely has its pros, but but it it also has its advantages when and we do have some actually have quite a bit of PMs that they don't have the the background of implementing Power BI solutions and and you might think that's

**8:18** · that's bad, but that's also good because they can bring different ideas and different scope and different perspectives that that perhaps someone that it's worked on the with the product for so many years it wouldn't even have thought about it.

**8:34** · Correct. Yeah, that is that is also important to think out of box. Awesome. Now, one of the first thing that you worked or maybe one of the most let's say famous things that you worked in the area of Power BI was Power BI project file PBIP PBIR and that's been announced for some time.

**8:56** · It is a still working progress. Now, for some of our audience who might not be familiar with this like they are still using PBIAX and they are happy with it.

**9:06** · They might think that what is this PBIP?

**9:08** · What is this PBIR? What is the benefit of that? Can you tell us a little bit about that?

**9:14** · Yeah, so PBIP stands for Power BI project files. It's also known as Power BI developer mode and it's all about let's say we can say that it's the code behind Power BI. Like a Power BI report and a Power BI model. So, when you create a Power BI report and a semantic model, there is some code and that code for many years, and this is not going away.

**9:46** · So, I'm just want I want to make it very clear because \[laughter\] I also learned from the hard way. I did a blog post a few I think a year ago or a few months ago about the making the PBIR, which we are going to talk about it.

**10:01** · Oh, yeah. And everyone then said, "Oh, I want PBIAX."

**10:05** · PBIAX is going away and no, it's not. So, the PBIAX is it's it is and I still believe it's going to be the main file format going forward. Because if you think like if I want to if I create a Power BI report or a Power BI semantic model or some analysis, data analysis in Power BI, I want to share it with you.

**10:26** · A PBIAX is the best format. I can just put it in OneDrive and I send you the file. I can even attach it in an email, which I don't recommend, but I can do it.

**10:35** · With a PBIP, that's not it because a Power BI project is a folder and it's a folder with sub folders. And if I want to share that, I need to zip it and it's not as intuitive and it's also a little bit more scary for many users. And And the PBIAX, the mental model comes from Office. Like just like you have an Excel spreadsheet with a XLS uh file or a PowerPoint with a PPTX file, uh the same thing happened with Power BI. But and the code was is inside of that PBIAX, okay?

**11:11** · Uh and uh but it's it's encoded inside of that PBIAX. So, it's not easy for you to look at the code uh and to version that code in source control. And to to make changes to it with scripts or now with AI. Uh so, the PBIP, it's all about uh it's the code behind of the Power BI.

**11:33** · And uh and it's all about two to three things like the first one and the the primary motivation of the PBIP was to just give customers and specially pro developers and enterprise customers that work in a team so they are not like just one data analyst working alone so they work with a team of BI professionals.

**11:58** · They need to work together. They need to collaborate with each other. They need to one is working on one table and the other is working on fixing a measure and the other another developer is working on fixing a report. So they need a way to collaborate and that's simply not possible with the PBIAX and because we also don't have yet a co-authoring story.

**12:19** · So I cannot I cannot just open a semantic model in the web or in desktop and we are both just like in words or in PowerPoint we are both editing the same thing and I can see what you are doing and you can see what I'm doing. So the answer for that is source control and get and and that was what the primary motivation behind the PBIP was to just uh, give customers a source control um, experience and and a co-development experience with with Power BI.

**12:52** · Then second again is making a lot the the the the code behind and and the code of Power BI make being a lot more transparent. So PBIP and one of the reasons it also took us and and it's still in preview and we are on the road to GA and and we will GA this year. It's also on the public road map.

**13:16** · But we never really documented the the the code of Power BI. So if you everything that worked and and there were a lot of thoughts from the community that created and and people like Matthias Thierbach that created that amazing tool called PBI tools that was able to unpack and and the PBX and make changes with and pack it again. That thing was completely unsupported.

**13:42** · So, the PBIP also forced the Power BI team to document, to support everything that is inside the the PBX and the PBIP allowing you to make changes to it in a supported manner and more important hardening what we call by that Power BI hardening which is assuming that we are not the only tool making changes to the semantic model metadata or the report metadata. And that's big.

**14:17** · And what's funny was that we did that with the motivation of source control. And and and also external tools like any external tool that can be tabular editor or PBI tools or a script that runs against the the semantic model report to make changes and not break Power BI desktop or the Power BI in the service. But, guess what? Then agents came along.

**14:44** · And all that hardening work which was not done with which was not done because of a genetic because when we started PBIP, there was no cloth. That this didn't exist or it was very in the in the early stages.

**15:04** · But, it's really nice to see that because we work on that fundamental we it it but but I remember talking with Christian Wade about it and uh and and and and we said something to each other like, "Hey, there are many other things that will come out of this work." that was in a very expensive work in terms of engineering this hardening and making sure that desktop does simply don't blow up because it's missing an annotation.

**15:32** · Uh we knew that uh uh good things a lot of good things will come out of it that we don't even know.

**15:39** · Energetic is one example of that, right?

**15:41** · Because now AI agents it it just go crazy to the to changing the semantic model metadata sometime hallucinating and if we haven't done that hardening work and the team and the engineers they did an awesome work with that uh things would just blew up as they were blowing up before uh but before it was not supported. Now it needs to be supported.

**16:03** · So again PBIP is the code behind. It's what allows you to have code development, source control uh and also and very importantly it's what allows you to make changes at the scale to your semantic models and reports and do it with code and do it with AI uh and uh and do it and and and be be in the supported realm because before uh everything was uh it was simply not supported.

**16:34** · So if we if the support team if you raise the a ticket with our support team and we detected that you touched the model uh we could just say and we didn't but we could say that okay this is not supported and you cannot use that that tool to make it to make those changes. You need to use Power BI Desktop. That that cannot happen anymore because of the PBIP. So that fundamental uh is uh is really important. Like okay so the PBIP the Power BI project is a code behind semantic model and report.

**17:05** · Inside of the semantic model you have the TMDL language the Timed language uh which is something that uh I'm also really proud of uh especially because it was born from the community. So, this was a a project that started with Matthias Thierbach. He worked with the product team, with our architects, with our developers, and we created this amazing language that is a like a declarative representation and textual representation of your semantic model.

**17:35** · So, that lives within the the semantic model. And for the report, we have the Power BI enhanced report format. We also call it PBIR, which is going away from it's switching from a single JSON that that was really bad for source control, really bad for agents to make edits to it because it was using like inline JSON within the JSON. So, it was never built for anyone other than the Power BI tools to look at it.

**18:11** · And and the PBIR, so it's basically making that source control ready and also again supported to make changes to it.

**18:23** · And to be honest and transparent with you guys, so the PBIR is the main reason why we haven't GA PBIP because if you think we want to move we only want to have one report format. So, unlike the semantic model where you can have thin doll and team soul and they are both pretty supportive and that's that's fine. You can choose between the two.

**18:48** · In the report, we don't because the the previous format was was always like an internal format. It was never a public thing. So, we don't want to support that and and we want to move all the reports into PBIR. And if you think this all the reports, this is pretty scary and I also learned that through the project because there are millions and millions of reports out there.

**19:11** · And there are millions of situations that can happen with a report and and hundreds of features that we had to change because of the report. And that's why it took us so long to to GA. It's not because again, so PBIP is pretty safe for you to use even if it is in preview.

**19:34** · Again, it's very stable and we are in the final stages of what we called and I I and I made an an announcement. I think it was on the June the June or the May blog of RBI. We called it the the default on of PBIR. So, which means that every time you create a report, it will be default into PBIR. If you edit an existing report, we will upgrade you to PBIR.

**20:01** · And and that's happening now. So, the the next release of desktop will be default will default on in PBIR. So, it's still a preview feature and you as a customer, if you don't want to use preview feature, you can just disable it and that is a tenant setting and a and a desktop setting. And and that's the final gate for us to GA.

**20:22** · And and hopefully it will happen in the in the next in the next few months. And and yeah, so in the PBIR is the it's the it's the it's the the report part the the code of the of the report. So, you can think of like it's one file per visual, one file per one one folder per page. So, everything which is also a nice thing about the Power BI project in general is that uh you can just inspect things.

**20:51** · Like if you want to know how many pages your report has or one how many tables, you don't need to open the tool. You can just open the folder and you can just navigate and that's that's a strong advantage because you can also copy things around. You can if you want to delete all the pages of of your report uh and you have like 50 pages, uh you don't need to open desktop, wait a few minutes, and then click uh \[snorts\] 50 times or with a I'm not sure if it we support multi-select. You can just just drop the folders and you are done.

**21:24** · Yeah.

**21:25** · \[clears throat\] Yeah, that's right. So, thank you. So, so basically, the PBIP PBIR combined with Tim Dell, all of these are giving us the support of collaborative Power BI development, the CICD, the Agantic, of course, and this is becoming the default option to save it in this format. Hopefully, in uh sometime soon. Now, you talked about also the Let let let's make that clear. The default is only for the PBIR.

**21:58** · And it's it's in both the PBIP and PBIX. PBIP honestly, I don't think it will ever be the format. The PBIP and we we know we know from the numbers. We have uh I don't want to say the wrong number, but we have like many millions Power BI developers like creating uh things, but do you we only have a few hundred thousands uh of users actually using the PBIP.

**22:26** · And that's normal because who cares about the PBIP are normally the professionals, the the people that care about this laziness and this ability to co-develop with others and scripting and AI. And that's a a subset of the of the the Power BI developers out there.

**22:46** · if someone save PBIX, still the reporting part of it would be I mean, in the future when it becomes default, the reporting part of it would be saved as PBIR?

**22:58** · Is that what you are saying?

**22:59** · Yes.

**23:00** · Right. Okay.

**23:00** · Today, so in a in the July release, uh uh if you create a you open Power BI Desktop and you just like use the sample data or you just bring connect to some database and you save the PBIX. Inside the PBIX, there will be a folder with a PBIR format.

**23:21** · That is cool.

**23:23** · and in the fullness of time, I hope that both the PBIP and PBIX they are exactly the same. The only difference is that the PBIX is just a zip of the PBIP.

**23:33** · Just a zip, huh?

**23:33** · That's that's something that we need we need to hear you guys on how you how important you feel that is, but we we hope to to to go in in that direction.

**23:45** · Awesome. That's that's amazing. This also means that in the future, uh even if we save PBIX because inside that it is using PBIR, so report altering using AI would be a lot simpler a lot easier because underneath is PBIR.

**24:04** · Yeah.

**24:04** · \[laughter\] Fantastic. Now Although although if you if if you want to use AI, if you want to use AI, you should you should use the PBIP.

**24:12** · Yeah.

**24:13** · Of course that you can have an AI agent and zipping the PBIX and and and making changes to it and zipping it back, but but I think you are just adding risk to something going wrong in there and if if that's your goal, just use the Power BI project. But it's an opt-in to Power BI project.

**24:33** · Yes.

**24:33** · Yeah, that sounds good. And talking about the AI, this is a good introduction to that part as well. You mentioned that your other focus area is how to make Power BI AI addressable so that we can create and author Power BI semantic models and Power BI solutions \[clears throat\] basically using AI and using agents. Can you tell us more about that?

**24:59** · Yeah, so uh again, what I mean by making a Power BI AI addressable for the creators is is basically just uh giving agents um the tools. And the tools are could be or are like the MCP.

**25:15** · So, we have the modeling MCP um that we we will rebrand as the authoring MCP and to to make it to be able to expand the scope to other things outside of modeling because there are things like setting a schedule refresh or setting a certain setting in the service or even having some report functionalities that are not necessarily modeling. So, we want to rebrand that as the authoring MCP.

**25:43** · So, anything to do with authoring a Power BI solution would be included in that, right? That is cool.

**25:49** · So, we have tools like MCPs. We just shipped uh in June and the PM for Line is PM for that is Harleen Kaur.

**25:59** · Uh the IPC the the the the report skill that includes uh the what we call a bridge between IPC bridges between desktop and applications. And applications could be an AI agent. Uh and and this is a tool that is very important because it's it's what allows AI or even yourself to just instruct desktop, "Hey, just reload the code.

**26:27** · Just I made changes to the code. I made changes to the PBI P. Just reload that into into desktop." And why is that important? That is important because for you to really be successful in agentic and using AI it's not just doing. It's not It's not just creating a page or just creating a measure. You need to be able to observe, to test that, to make sure that it's working. And the IPC bridge is what gives Basically, it's a it's a it's an API that is running in desktop that gives the the functionality to reload and also to test.

**26:59** · Like, hey, take me take a screenshot and give me that screenshot.

**27:05** · I'm talking as I I was the AI, so I I'm the AI, I make the change, and then I'm going to take the screenshot. And and with that screenshot, I'm going to validate if the changes that I did or the intent that my human told me to do is following the what the it is is going in the good direction. So, the the these tools they are fundamental for that.

**27:32** · And again, this is this is also making Power BI tools like Power BI desktop more addressable to AI because this this didn't exist before. So, if you made a change to the Power BI project, then you had to restart desktop. So, the the agent could see that change.

**27:51** · And there was not even a way to communicate with desktop saying, hey, give me a screenshot of that of that report because the Yes, that you have the the full code in the PBIP, but but you don't have the engine that can render that because it's not an HTML report. So, the PBIR is a proprietary format. It's open, but it's a proprietary format, but uh but you cannot you cannot just render it.

**28:18** · So, for that, you need to have the report engine, and that's going to live in desktop. And the same thing happens with the semantic model uh Um you can see the measures and the tables, but if you want to test the measure and and verify it's returning the right results, you need an analysis services engine, and that's also running in in desktop.

**28:40** · So, tools So, doing tools uh and and that's that's a big focus of my team is to create these tools and and make sure that they work and play well together with AI, but also non-AI, because again, you might then I and I still see a lot of value in creating scripts for doing things that are repetitive and and and you know and perhaps the tool is not does not let you do it in the in a very efficient way.

**29:14** · Um and and it will be also efficient for you.

**29:19** · Perhaps use AI to describe what you want, verify that the agent AI did what you what you what what you wanted, but but in the end you can always say, "Hey, now generate me a script, a Python script, a PowerShell script, a .NET script, whatever it is. Uh so you don't need to write the code so I can have this when I can and I can run it later and then become deterministic.

**29:43** · You don't need to burn tokens to do something that you already did before and you can transform into a deterministic script. Uh so you can still run scripts and and you can also take advantage of this IPC bridge and the Power BI Desktop CLI to reload those changes.

**30:06** · So even if for example if you're using source control, you can pull a latest change for from a colleague, you still have Power BI Desktop and perhaps perhaps your semantic model and report is very large so it takes a lot of time to restart desktop, you can still leverage the the bridge to just reload the the code and um uh without without having to to to restart restart desktop.

**30:36** · Yeah, this bridge is helpful actually. I remember a couple of months ago I was trying to like build something using AI inside Power BI, but after this build it, I had to like close it and reload it, open it again, which is now possible through the desktop itself using that bridge, which is amazing.

**30:57** · Yeah.

**30:58** · So, and that's that's the first part of making Power BI AI addressable. The second part is and also another thing on the tools um is also APIs, right? So, we also need because in desktop, we need an API to communicate with desktop and that's the IPC bridge, but when you are in the service and then we need APIs and and we already have um a good amount of APIs for for Power BI.

**31:30** · Um and we are creating new APIs. Um so, we already have an API that allows you to get the code of a semantic model or a report and update the code or create a new semantic model or or a report just with the code. That didn't exist a few years ago.

**31:46** · Uh but of course that we we can also make those tool those APIs better. We can making make them more granular um and and that's also something that that we are working on.

**32:00** · But but but again, tools, it's like this combination of of things that we can do on the product side and only we can do it because it's it's inside of the product. Uh so, so AI and and and and humans can interact with to to be more more efficient. And the second part is knowledge, right?

**32:20** · So, another thing that that surfaced and and and in this AI world was the skills, uh which was a big big innovation

**32:35** · in and the skills it's what allow allow us from the product team to create the necessary context so AI knows how to create a semantic model or how to modify a semantic model and how to create a report and how to modify a report, how to understand what are what are the steps that the AI should follow whenever is tasked to do such a thing.

**33:04** · Um, and I tried and we tried on the product side to make these skills not very complex and also to to making make it more like a something that that it will work on the majority of the

**33:25** · scenarios but also something that you can customize because I do believe that the real value so you can get started with the Microsoft skills or the community skills there are many community skills like from tabular editor the the and Kurt um uh that uh that are really great and they use their own tools and they and and I think that the community is is doing an awesome job in here but I in my opinion what really makes

**33:55** · and and we and I can get started with these skills so please if you are getting started with the AI just use one of these skills you can use the the the the ones from Microsoft in the skills for fabric repo uh you can also try with the community ones uh but then what what I think it really makes the difference is when you take the time to

**34:17** · customize these skills and adapt it adapt those skills to your own reality because for example in the in the semantic model authoring skill there is a a reference file in there that describes naming conventions which in my opinion the most important thing you can do, you should do when you are modeling a semantic model, is to be consistent. It's not about the rule.

**34:38** · So, I might want to do all everything uppercase, or my customer want to do everything uppercase, or everything lowercase, or with camel case, or with Pascal case, or with snake case, whatever it is. So, whatever is the rule, what is important is whoever is going to use that semantic model to be comfortable and understand and something that is comfortable for them, for the end user. But, the most important thing is consistency. And and and And this is something that AI is really good at.

**35:10** · It's detecting You can just ask, "Hey, can you go and analyze the naming convention and tell me where where if anything is not consistent with the names that I'm using." And it will tell me, and then it can fix that for me.

**35:25** · Um and the naming convention that I have in the skill, or we we have in this in the uh in the semantic model authoring skill, is just an example. That does not mean that that should be your naming convention in your team. Uh and uh and it's perfectly fine if you go and customize it.

**35:40** · Or, if you don't want to change the skill from Microsoft, you can create another skill and just instruct the agent, "Hey, I want to use the skill from Microsoft, but here's some special rules that uh that that apply only to my that that might that I care about that should supersede uh and overlap the whatever is in the in the Microsoft skill or the community skill."

**36:06** · Uh because to me, the I still remember I think it I think it was last year, early last year, when I was starting to play with a gigantic and and the thing that uh um that was like this lightning bolt for me was when I was able At the time, it was not with skills, but with the necessary with the right context, I was able to describe how I think as a semantic model

**36:34** · developer, and then I realized that the agent and I looked at the end result, and it was something like as if I I was the one creating that, and that's and that's amazing. It's when you that's and with skills this is a lot easier, and it's definitely worth the investment not only starting with something that was already built, but then also spending some time on adapting those skills to whatever

**37:04** · fits my team guidelines and my team like quality bar and how I how I do stuff. So, again, knowledge and this is in the skills, that's also something that we are working on to not only be successful in this space and and allow just a customer to spin up GitHub

**37:28** · Copilot and in the future even within the product and just express yourself and you define, okay, this is what I want to do, this is the data source, this is the analysis I want to build, just build that for me and kind of be more like in the steering wheel and not actually uh implementing everything from scratch and spending days and and weeks creating semantic models and and and and another thing really interesting that only AI made that thing possible is the the ability to go back, right?

**37:59** · Because one of the things that whenever we implemented a BI solution was always we had a lot of and I'm sure you did this many times, like you you did we did like that initial analysis, we created a document, and we made sure that this is what the customer wanted and then we start the implementation and then if there is if the customer wanted to change to a different direction and perhaps the customer did not want did not knew what he really

**38:30** · wanted in the beginning because he was not seeing anything was not exploring the model and then he wanted to make a change it was very hard not hard also hard for the it was hard for the customer because he had to pay more more money and but it was also hard for the developer because then you you start to have a relationship with that code right so you you you spend weeks creating something it's not easy for you to go back and that with AI that that that does not exist anymore so you can actually implement three flavors of the same project and and see the one that

**39:02** · works better and and if the customer changes mind you can like if you have everything implemented with AI with specs and and the right context you can just okay now let's change the direction into this new direction and let's see how it goes so it's not a you don't get as intimate with a with a code as you as you were back back then but um but yeah this this new world also opens

**39:31** · the the possibilities to to the for the for the developer to to be a lot more focused on on the customer and not so focused on the technical side of things and I think that that's a good thing Correct yeah and I like the example you mentioned that we don't have to like just take skills as it is

**39:55** · and we better to go and customize it with our naming conventions with our standards which is really interesting point and also the fact that this age of AI is changing so fast like tools that we didn't had few months ago now we have it new APIs new capabilities which which is amazing and that is how the agentic AI is progressing in our day-to-day work Power BI development and everywhere else. Now, can you also tell us about what is coming in this area?

**40:29** · What should be looking forward to?

**40:32** · Yeah, so again, you can you can expect more and better tools and like a better version of the MCP. I already told you that we want to move away from modeling and more authoring. This This also means expanding the the MCP to to do other things that are not necessarily only modeling. I also want to say that we want to GA that MCP so because it's in preview since November.

**41:06** · So it's pretty stable and it we we we got amazing feedback and and and really good user stories on how that that it works so we should GA that. But we can we should also evolve it and and keep evolving it to to fit other needs and and authoring I think it's a it's a good direction in that.

**41:29** · Um One thing that we I even said that in a in a presentation I believe last year but it is coming very very soon and I'm really excited about that. I'm not the PM for it. So the PM driving it is Setareh Slamini my colleague and uh which is finally that the Power BI project will if you made a change desktop will just pick that change and reload desktop automatically.

**42:07** · So this is something coming really soon and and this is something that we always wanted to do and and it was part of the road map and finally we we got we got to do it and and this is all related with the IPC bridge and and then again working with the fundamentals makes a ton ton of difference here. So then these things become a lot easier.

**42:32** · So and uh and and going back to the knowledge also the evolution of the the the fabric skill the skills for fabric to bring more skills and enhance the existing skills.

**42:46** · So in terms of the agentic I would say and I I don't I don't want to be specific because again that we are doing many things and and there are things that might not go might not ship. So I don't want to I want to set the right expectations. What you what you can expect from the from

**43:06** · the Power BI agent from the team that is working or my team that is working on the agentic space of Power BI is really to work on deliver the tools and deliver the knowledge so they AI agents can can be successful with Power BI. And again there are a few gaps that we need to address. We need to make sure that everything from the semantic model and the report is editable and not only is editable but is also editable in a consistent way.

**43:37** · So it's not it's not good when certain things you can edit with the MCP and certain things you can only edit with the PBIP and then there are things things that you can test and things that you need to reload desktop so you can you can test them and the AI agent can observe the changes.

**43:58** · So those are the things that you can expect Uh, and uh, and again also expect the the GA of MCP and the GA of PBIP and PBIR, um, which is also important especially for for enterprise customers that uh, that cannot uh, or cannot use preview preview features.

**44:22** · Fantastic. I'm I'm like myself, I'm quite excited about all these like agentic capabilities that we have in Power BI in Microsoft Fabric and yeah, I'm looking forward to all these new uh, new features coming along. Now, uh, that's amazing. Thank you. I'm going to put your LinkedIn URL down in the description below for people to reach out, but what other channels are best for them to get in touch with you if they have feedback, if they have any questions?

**44:55** · Yeah, so let me just paste something in here.

**44:59** · Um, so this is the best The last months I launched a new documentation page called uh, Power BI agentic where it's it's uh, it aims to be like this hub where you can learn the the most important things about Power BI agentic, the tools, the skills, and how to get started. So, you should put the link somewhere below or above. Um, and \[laughter\] And uh, how to reach me.

**45:29** · So, you can reach me on LinkedIn. I'm usually active there and responsive. So, and I'm always uh, available to learn and and and and hear feedback and take that feedback to the team.

**45:47** · So, I really appreciate if there is anything that is uh, not working out which as it should or anything that can be better, just please reach out and um, I'll be happy to to follow up and yeah, so I think LinkedIn is a is a good channel to to reach me.

**46:10** · Amazing. Awesome. Yeah, we'll put all those links down in the description below. Thank you for your time, Rui. It was great. It was really insightful and yeah, we're really looking forward to all those new features. Thank you for you and the team to do all these interesting stuff behind the scene, which would then enable us to build our solutions much easier.

**46:32** · Thank you everyone for joining us. This was another episode of Fabric Insider and hopefully we'll see you in the next one. Until the next one. Bye.

**46:40** · Bye-bye.

**46:44** · \[music\]