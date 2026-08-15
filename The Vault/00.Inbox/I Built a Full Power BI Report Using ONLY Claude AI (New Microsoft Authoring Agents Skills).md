---
title: "I Built a Full Power BI Report Using ONLY Claude AI (New Microsoft Authoring Agents Skills)"
source: "https://www.youtube.com/watch?v=oIzuGgNEH-0&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=oIzuGgNEH-0&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Analytical Guy]]"
published: 2026-07-10
created: 2026-08-08
description: "Microsoft just released new AGENTIC skills for Fabric — and they let an AI agent build a real Power BI report for you. In this video I connect Claude to Powe..."
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=oIzuGgNEH-0)

## Transcript

### What we're building (the finished report)

**0:00** · I created this four-page report in Power BI using Cloud without creating even a single visual by myself. So, if you see on the overview page, you have four data cards. Then, we have line chart. Then, we have column chart, bar charts, metrics table. We have some toggles as well, page toggles. So, I can go from overview to product and from product to sales or sorry, stores. And then, from stores, I can go to customers. So, we have a navigation as well.

**0:30** · We have the AI-generated overview as well. You can see over here. So, it says computers leads at 35% of sales. United States is the top market, 40% for 58.3% overall margin, right? And I can filter through year as well. So, you can apply various filters. You can have multiple data cards. You can have multiple visuals depending on how you want to have that.

**0:58** · And then, you can have multiple pages with navigation, everything using Cloud.

**1:03** · Or you can use any other AI. For my use case, I have utilized Cloud for it. So, this is the objective. We will start from scratch. We will have a data set.

**1:13** · So, this is a retail data set which I have used. So, from that, we will create this report using Cloud in 15 to 20 minutes. So, let's get started. But before we move ahead, I just want to mention that we will be using authoring agent skills that have been updated few weeks ago in Power BI June 2026 feature summary. So, if you see in the content, you will have one option as AI-powered Power BI reporting from design to deployment in with agent skills.

### The announcement — what Microsoft shipped

**1:45** · So, if I click here, so what it says is the capabilities of what this skill can do. So, it can build complete reports from blank canvas to or update reports all through conversation. So, this is what we are going to do today.

**2:00** · Get expert design recommendations grounded in data visualization best practices tailored to your audience and KPIs. We will do this as well. Go from vague goal that like, "Hey, I need a executive dashboard." to a locked approved reports back with guided Q&amp;A. So, all these capabilities are possible and then we will be utilizing this as well. So, the end-to-end reporting workflow looks like this. So, if you see here, so this is you, Power BI developer, right? So, you are doing the conversation with LLM.

**2:31** · And \[snorts\] the first step would be to gather requirements. For that, you would be needing Power BI report planner. So, using that you will gather requirements, define audience, and lock a report specification. And then comes the designing part. This is the most important part because otherwise it becomes so vague and very straightforward. So, you will select page archetypes, chart types, color palettes, and accessibility standards.

**2:58** · So, once you have designed, that's when the Power BI report authoring comes into the picture. This is the very important skill. And what it does is it generate report definition files, pages, visuals, filters, themes, and then in validation it reload the Power BI desktop and capture screenshots for visual review. So, we will see this live when we are using Claude. So, what it does is So, it reloads whatever it has created and it will reassess. So, it will see itself and see if whatever it created is right or wrong.

**3:30** · And if Claude feels that whatever it has created is not correct, then it will redo. So, it will be like a loop, right? And then once the things are satisfactory, the deployment happens. So, these are the steps and very important that I mean this is a game-changer. So, if you are a Power BI developer and you were doing drag and drop creating visuals from scratch. I mean, that will still be important, but you don't have to do it everything from scratch, for sure.

**4:04** · Also, one more thing is this currently only works with your local PBIP file.

**4:09** · So, if you don't know PBIP file, I have already created a video on this. I'll share the link. And very important, you can't do it with desktop file. So, you need to have project file for that. And you can have a documentation, which is given in Microsoft. So, I'll share all these links so that you can work on these skills. Very important. So, let's get straight to creating the dashboard.

**4:32** · If you have not already subscribed to the channel, I would request you to subscribe. I will be creating more videos on how to utilize AI to create Power BI reports. Then also, in future videos, I'm creating videos on Fabric apps. That's the new feature in Fabric.

**4:49** · So, more and more features are coming in. I'll be trying to cover all those topics. So, please do subscribe so that you don't have to come back, and you will get the notifications whenever the video is uploaded. And the video which I was talking about Cloud Code was this one. So, this is one I created the video on Power BI MCP server with Cloud and with VS Code as well. So, you can refer to these videos on how to install. And then, this was a video on how to create Power BI report using AI.

**5:21** · That was full automation, and this was more about what we are doing now without authoring skills. So, this is also very handy video if you want to watch. All right, so let's get back to the video. All right, so one more thing before we deep dive in is first of all, I will start with the existing skills that the skills that we already have in Cloud, the one we used in the previous videos as well.

### Building Power BI WITHOUT the AUTHORING skills (it breaks)

**5:46** · So, using those skills, we will try to create the complete Power BI report end-to-end without me creating any visual. So, you will see that it creates a visual uh reporting, but it is not great. It is just a basic one like having four to five visuals, but not good-looking one, right? Once we do that, once we establish that, second step would be to install the authoring agent skill that we have now from Microsoft.

**6:17** · So, once I install that in Claude, then we will see the advancements. Then we will see the upgrade that we have in Power BI reporting with design or with semantic modeling and various other things, right? So, \[snorts\] the reason I'm doing both of them is to make you understand the differences and why this Power BI update is really good. This update is outstanding, right? So, let me start with that. And for example, if you have already worked on that, so you can skip for next 2-3 minutes and straight away go to authoring skills in this video.

**6:51** · All right. So, first of all, let's have a PBIX file. So, as you can see, we are on Power BI Desktop, and if I go to table view, you should be able to see all the tables that we have in this particular data model. So, you have dimension customers, then dimension date, dimension products, and dimension stores. And finally, we have one fact table, which is sales.

**7:12** · So, you can see fact sales fact sales have order number, then line item, order date, delivery date, customer key, store key, product key, quantity, currency code. So, we have all these keys to connect with all the dimensions. So, if we go to dimension customers, we have the details for each and every customer.

**7:33** · And if I go to the model view, there would be a good relationship between all these tables.

**7:41** · So, if you see over here, let me make it smaller and make it better.

**7:51** · So, as you can see here, so we have one fact table and four dimensions. So, we have one-to-many relationship. So, currently we have built this semantic model. We have five tables and these are all connected perfectly fine.

**8:05** · Right. So, the next step is to create some KPI cards. So, they would be a DEX measure, so we don't have anything. So, it is all null right now. Right? So, that is the primary uh step to get the KPI cards in our Power BI report as well. Right? So, that would be one thing that Cloud will do. Second thing would be it will create all the visuals over here. So, as you can see, currently we just have page one, which is all empty. We don't have multiple pages. So, first of all, let me convert my Power BI Desktop file into PBIP file.

**8:39** · So, what I'll do is I'll go to file.

**8:44** · Then, I'll go to save as.

**8:51** · And over here, in save as type, I can change to PBIP.

**8:55** · And my location would be a new one. So, in today's scenario, I am creating a new folder altogether, retail dataset\_youtube\_demo.

**9:06** · So, if I select this and add this PBIP file, let me change this to demo YouTube. So, the file name is retail sales demo yt.pbi file. So, I'll just save this.

**9:22** · Right? So, we have created a dedicated workspace, which is the one which I have created right now, and it will have just PBIP file. So, if I go there, you will see this folder which we have created, and this will have our PBI P file. So, PBI P file is there, then semantic model and report. So, this is the structure that we have anatomy of PBI P that we have understood as well, right? So, in report you will have definition PBI status static resources and definition.

**9:53** · And then if we go to semantic model, you will have Tim Dale scripts and then a definition as well, right?

**10:03** · So, this is how the structure would be.

**10:05** · Now, the next step is to connect Claude on this workspace, right? So, I'll just go straight to Claude.

**10:14** · So, this is the Claude and so, I've created a new session in Claude code.

**10:20** · So, if \[snorts\] you have not worked on Claude and you don't have knowledge of how to connect through Power BI MCP server or you don't know how to connect directly and work on this. I have already created a video.

**10:33** · Please watch that before going ahead because that is very important to understand how we are connecting Claude code with Power BI desktop file or PBI P file, right? So, now we have connected to Claude code and the location you can see over here. This is retail sales.

**10:51** · It's not shown here. I can open it again.

**10:57** · So, I'll go to projects and then in Power BI I have retail data set YouTube demo. This is what we are using today and it has further folders and PBI P file. So, I have connected this, right?

**11:11** · So, now I will do the conversation with Claude.

**11:17** · Can you connect with Power BI file?

**11:22** · The name of Power BI file is retail sales demo YT.

**11:28** · Retail sales demo YT.

**11:32** · It is uh a BIP file.

**11:38** · Once you connect, I want you to create Dax measures for various KPI cards.

**11:55** · All the measures should be in a separate folder.

**12:05** · After that, I want you to create one page retail sales executive report.

**12:24** · So, once I give this, it will try to understand what it has to do, and it will go to Power BI MCV server, and it will try to authenticate, and once it authenticates, then we would be able to connect with our Power BI uh project file as well. And once we connect, then it will try to create KPI measures. Once Dax measures are created, then it will try to create some visuals.

**12:48** · As I've said, like create just one page, so it should create just one page.

**12:53** · And here, to make it faster, instead of accept, I can make it bypass permissions.

**12:59** · So, to make it easier. And if you want to go for coffee breaks, and if you want to keep things at risk.

**13:08** · So, yeah. So, let's wait. Once this is done, I can minimize this.

**13:22** · So, you can see there is Entropic Skill Power BI Connect, so it tries to use that to connect. And it is checking for running Power BI Desktop instance. So, it has found. That's a good news. Let me connect. All righty.

**13:36** · So, it uses Power BI modeling MCP. Now, it says connected. Good news. Now, let me profile the model to understand the schema before writing measures. Let me get the table schemas. All right.

**13:50** · So, it will read all the files. So, Tim Dale file will have all the tables in this particular model. So, it will read all the tables. So, currently it is reading fact sales. It says it has quantity, but it has no price. So, price is likely in dim products. Let me read dimension tables. This is what it's doing. Now, it is checking the relationship to confirm the model wiring and verifying the date range in the data. So, ideally if like as a data analyst for Power BI, you tend to work on these steps itself, right? And this is what Claude is doing for you.

**14:22** · So, now it says, let me run a quick DAX query to understand the data range and magnitude before writing measures.

**14:30** · So, it is using now DAX query operations under Power BI modeling MCP.

**14:41** · Now, it says measures are created and persisted. Now, let me build the report.

**14:46** · Let me invoke the reporting skills and inspect the existing report structure.

**14:50** · All right. So, now it says it has created KPI cards. Now, the trend line chart, all those things. It says all 12 visuals are written. Everything is in place. Here's a summary of what's done.

**15:02** · So, it says connected to running Power BI Desktop instance retail sales demo YT. And then it says 10 DAX measures created. Sales amount, total cost, total profit, all those things. And then all validated against live model. And it says one page of executive summary is also created.

**15:20** · And then all 14 reports the JSON files validated as well-formed all good. And now it says reload this PBIP file in Power BI Desktop to see the new measures in executive summary page. All right.

**15:33** · So, what I'll do is I'll quickly have this Power BI Desktop close. So, I'll close this.

**15:40** · And remember, so this is PBIP. Remember, don't need to save.

**15:45** · Click don't save.

**15:47** · So, once you do that, so in order to reopen the PBIP file, I'll just go to this location. So, this location in YouTube demo, I will open this file, right? So, let me open this file.

**16:06** · And with what Claude said, it created one page and it also created some measures. So, it should have all those information.

**16:20** · And yes, it has the executive summary, all those things.

**16:29** · Right. So, we have one page with five data cards, some filters, and then we have these visuals, right? Some bar charts, line line chart, and then performance by category as well. So, and where is the measure? So, if I go back to my Claude, the measure name is sales amount.

**16:51** · So, I'll just search sales amount.

**16:55** · And it is in KPI measures.

**16:58** · So, if I go to this KPI measures and sales amount has been created as fact sales quantity multiplied by related to dimension products unit price in USD.

**17:11** · So, all right. So, so you have sales amount, sales amount last year, all those measures are already here. But, ideally this folder should be outside and it currently it is in the fact table.

**17:22** · That's fine. We can instruct that create a separate measures table and have this folder inside that. But, that's fine.

**17:29** · Currently it's not hindering anything.

**17:31** · But now, so this was the way we used to do through cloud when there was no authoring skill. So, remember this report. Remember this. We will come back um to this uh if this was good or if we can make it better. Right? So, let me take a screenshot of this.

**17:52** · And I will come back to this one. All right. So, now the real Yep, done. So, now the real agenda of this video comes in using the authoring skills. Right?

**18:13** · All right. So, now we will go straight away to the announcement and uh we will click on AI-powered Power BI reporting.

### Adding the plugin/skill in Claude

**18:20** · And this is where we have the documentation. This currently only works with PBIP and explore our documentation.

**18:25** · Once I click on documentation, that will redirect me to GitHub link and it will have skills for Fabric. And then we have skill MD file for Power BI reporting authoring as well. So, this is description is create and modify Power BI report files in PBIR or PBIP format using Power BI report author and Power BI desktop CLIs. Right? So, this is something that that we will be utilizing. And if I shorten this link, this is what it is. github.com Microsoft skills for Fabric. Right?

**18:55** · So, this is the link that we we will be using to install. All right? So, if I just copy this link, microsoft/skills for Fabric. Right? And now if I go to cloud, And if I open my session and go to customize, in customize, I want to add a plugin, right? So, I'll click on plus icon and click on add and click on add marketplace.

**19:27** · So, I will click on add from repository.

**19:31** · So, this is a repository, right? Like we have GitHub repository. So, I'll click here and then I will search and paste it over here.

**19:40** · So, I will use this one and click on sync.

**19:46** · So, once we sync, it will show us the list of all the skills inside that.

**19:52** · Right? So, you can see over here.

**19:54** · All we want is Fabric authoring.

**19:58** · Then I want Power BI authoring.

**20:00** · Then these are all added automatically.

**20:04** · And that's it. So, once we have So, you can have Fabric skills as well. That's fine. So, now once we have these Fabric authoring skills installed, and you can see the notification, Fabric authoring skill installed and ready to be used.

**20:19** · So, what I can do is I can close this and it should show me on the left-hand side in personal plugins. So, if I go here, Power BI authoring, so this has Power BI report planning. It has Power BI report design. It has Power BI report authoring. So, these are three skills which are most important for us right now. And definitely it will use check updates for the first time. So, whenever you install and then you use them, it will automatically take it for the first time as well.

**20:49** · So, but we have these three as most important skills that we are using in this one. So, now that we have installed, we will mention these skills that, "Hey, whenever you're using working on Power BI reporting, use these skills." Right? So, first of all, so what are these skills? So if I have for example open the report design, so I can click on that and I can open that and you will see over here in report design.

**21:21** · So it was added by Power BI authoring, then it was last updated on 8th of July and then it has description like generate Power BI report visual design guidance blah blah blah and then we have the skill. Then what is the must, what is prefer and avoid. So must is inspect the semantic model or available fields before making decision about designing.

**21:43** · Prefer is ask only for mission design inputs that materially affect the output. Avoid is do not create pages, visuals, filter themes or PBI files directly. So it has to ask. Right? So it has all the logic, all the information.

**21:59** · So whatever we are doing with this skill, it will be most probably very specific. So it won't give you generic answers, right? So you can modify that as well. So if you click on edit and you will have option to edit with VS code.

**22:12** · So if you click on VS code, it will open in VS code. You can edit the skill the way you want. So you your company has a particular way of working with Power BI reporting, so you can update these skills as well, right? So once you're done, you're good to go. You can copy the skill or you can try and chat as well, right? Similarly with various other skills like report management or the report authoring which is important for us, right? So now I'll go back to my cloud code in the same text chat, I'll say hey first of all, I'll write this Power BI.

**22:49** · Where is my authoring?

**22:52** · So let me search like authoring.

**22:56** · Oh, it's not showing up. So what I can do is I can go back to customize in plugins.

**23:05** · So, I'm looking for Power BI authoring.

**23:09** · This one, right? So, if I click here, just copy this.

**23:15** · And let me go back to my main page and let's try now.

**23:25** · Use this scale now to create four page report in the same PBIP file.

**23:39** · You can delete any existing page if you want.

**23:47** · In these four pages, I want executive summary.

**23:55** · Then, second page should be about product analysis.

**24:05** · Third page should be about store analysis and fourth page should be about total sales comparison, let's say.

**24:27** · Right?

**24:29** · So, once you have built, I want you to create navigation so that I can navigate various pages from the report itself.

**24:53** · All right. So, we are using Power BI report authoring scale for this.

**24:57** · So, now it says Power BI report authoring scale is not recognized.

**25:03** · So, it says some commands only work in Cloud Code Terminal. We are in Cloud Code. Strange.

**25:08** · All right. So, what we can do is maybe we can restart, but let me go back here in customize.

**25:21** · So, if we see here, this is marketplace for Fabric.

**25:30** · This is a different one.

**25:34** · This is different. So, what actually should happen, this should directly work. This is updated. This is up enabled.

**25:45** · So, I don't think there is any problem.

**25:48** · I'll see connector.

**25:53** · So, this is also fine.

**25:57** · All right.

### Creating the report from a single prompt

**26:00** · So, what I can do is I can quickly Oops. Uh create a new snipping tool.

**26:12** · What I'll say is to Cloud Code.

**26:18** · Copy this. Go back to the chat.

**26:25** · I have pasted the skills. I can see these skills added.

**26:33** · I just added using GitHub plugin.

**26:40** · Why can't you recognize?

**26:45** · Let's see what Cloud Code says about it.

**27:05** · All right. So, now it says is the skill is installed under fabric collection plug-in that we know that. So, plug-in scope its name. So, registered skill name is likely Power BI authoring Power BI report authoring. All right. So, that was it. So, first to answer your question that the skill is recognized issue is slash command versus skill invocation. That's good. Skill is more rigorous than the one I used before. It drives to to official Microsoft CLIs.

**27:31** · That's what we want and mandates using modern visual types. Let me verify the tooling is available. All good. So, now it's it checks for the node and both Power BI CLIs. So, now it says both CLIs are installed.

**27:50** · That's good.

**28:00** · So, it says page navigator is available. So, that's clean way out to add in report navigation. Let me describe the key visual types I'll use. So, I bind rows correctly. All good. All right. So, after roughly 10 minutes, let's see what Cloud has done for us. So, if I scroll down, so it was saying page navigator to have those navigation and it was there. So, it is available.

**28:25** · So, that's good. And then if I scroll down at one go, it said used Power BI MCP and it failed because it was not there. But then connection was dropped. Then it tried again. So, it reconnected. And it says all the measures were intact and everything is fine. It uses page 2.1.0 in desktop imported as visual this.

**28:49** · And then it created four pages. All four pages generated. Now, let me validate with CLI. And then it also read the report JSON file. There were some errors and then it rectified that. And now this is what the authoring skill does beautifully. This is the agentic way that we were discussing. Desktop already sees all four pages. So, it sees four pages. Let me reload and capture screenshots to verify real rendering.

### Refining it conversationally

**29:18** · So, it says screenshot captured and let me review each pages rendering. So, page one is executive summary. This is what it shows. So, you can see yourself like how it has changed from what we had previously. Right? And second page is store analysis. This is how it shows. Then total sales comparison is the third one.

**29:41** · So, these are the three pages it beautifully created. And the point is it took the screenshot and if it feels like something is odd, it will say that something is odd and it will rework on that. So, now it says only three prerequisite theme errors remain. My pages are clean. Let me screenshot the executive summary to check the navigator. The navigator bar now renders. I can see all four buttons in the header.

**30:07** · So, executive summary had highlighted in blue, then product analysis, store analysis, total sales comparison. The layout orientation enumeration was indeed breaking it.

**30:17** · This single page capture came out zoomed out. So, let me take full-size screenshots of all the pages to confirm everything is consistent. So, it is re-screenshotting all the pages full size. So, this is where I don't have to do anything. And also I have already applied bypass permission. So, it's not asking me anything to do. So, literally it is doing itself, rechecking the work it has done, and you know, re-evaluating and doing it again. So, So, all right.

**30:46** · So, again we have to wait for some few more minutes to see how it works. And at the end we will capture how many tokens it used for the complete session and see how much compute, how much money it took uh to generate these four pages. This is also important going forward because ultimately we have to compare if these four pages were created by a human versus if these are created by Claude, how much the worth it is, you know, reducing.

**31:16** · Because it's important because see, all these reports are easily created by human. So, Claude is doing nothing fancy or something or that human cannot create. So, human can do anything, but it is doing it quickly, but it is taking a lot of tokens. All righty. So, it is still checking. All right. So, it has done the screenshot again and it works fine and it says everything is verified and complete. Let me give you the rundown.

**32:03** · Four-page report built and verified. So, these are the four pages. These are the KPI cards. These are the visuals and then navigation is also working. So, what we will do is I'll straight away go to Power BI and reopen that file. This is my file.

**32:19** · Right. So, click here PBIP. And this time there should be four pages with the updated version. We should have navigation as well. So, let's see if uh Claude has already created that for us.

**32:41** · Looks like it. So, we have in the bottom we can see executive summary, then product analysis, store analysis, and total sales comparison. So, currently we are on executive summary. You can see on the top we have the toggle bar as well. So, we have five data cards, then we have sales trend by month. I can change the year to let's say select one year for now, and things should change. And then sales by category, category performance, all those things. For example, if I want to go to product analysis, then it is also working.

**33:12** · And if I go to total sales comparison, it is also working.

**33:17** · All right, so that's good. So, what we have already achieved in 15 minutes is we created four pages without me creating any visual myself, right? So, this is beauty. Because once we have created a semantic model, we can validate it once, just for our sanity, but once we have a good semantic model, once we have all good DAX measures, all these visuals should ideally be fine.

**33:45** · So, we don't have to worry much about it. All right, so if I go back to my cloud, so what I want is I want to try one more thing. So, I want to try to change the theme of this uh page. So, currently it is looking good, not bad, right? But, I just want to experiment just to see how deep it can go. Right?

### Design inspiration from a folder (re-skin)

**34:05** · So, if I go back to cloud, so here I have to add one more file. So, if I go to my folder again, and if I go back to the previous folder where I experimented earlier, so I had a JSON file retail IQ light JSON. Right? So, if I open that, open with code.

**34:49** · So, if you see here So, what it says is it has some data colors. It has the definition for good, neutral, bad, etc. Then we have background, second background, all those things. So, the color coding is already there. So, then we have all these visual styles.

**35:08** · So, So, what it does is it defines how it should look like, right? So, this is the way for example, if we as a brand, if we as a company have our own colors of different branding, so we can mention that and we can provide this JSON file to Cloud. Right, so what I do want to do is I will copy this and I will go back to my existing or main folder YouTube demo and paste it over here.

**35:37** · So, \[snorts\] once I paste it, what I'll do is I'll go back to Cloud. I'll say Or I can attach as well. I have this JSON file in the folder.

**35:51** · Can you update the Power BI design using this?

**36:00** · Or you can say design after getting inspiration from this file. So, just remember, currently we have uh reports looking like this. So, let me take a screenshot.

**36:29** · Right, so let's see. Once we have the updated one, we'll compare how it looks like. So, this is the executive summary we have taken screenshot off. And now if I go back to Claude, it will run and it might take a few minutes. And once it's done, we can check the output.

**36:52** · So, it says it's a proper Power BI theme, warm light editorial palette of white canvas. The right way to apply this is twofold. Register the JSON as the report's custom theme, then re-sweep my per visual hardcoded visuals to match the new palette. So, it says there are two things that has to be done to implement this. So, it will now read the report.json to register the theme correctly.

**37:19** · All right, so once I provided this JSON file, it extracted the registration structure. So, the plan was to copy the theme into static resources and then register it in report.json, then re-sweep. All right, so this was it. And then what it does is validation it did. And with the retail light theme, it applies beautifully and redesign is cohesive, it says. And this is how it looks now.

**37:44** · Right? And then if I go further. All right, so this is what it is. So, let me try to open the Power BI. Let's see how it changed. All right, so if I see the executive summary, so you will see the theme has changed, right? So, let me open what it was earlier.

**38:06** · Oops.

**38:08** · So, this is how it was earlier. So, it was in this theme, blue shaded and we had these data cards, all this blah blah blah. And now we have something like this. So, this looks good. I mean, it depends on how you want to work on. So, if you have a particular theme, so why I provided JSON was to keep it consistent with the upcoming reports for you. So, once you define your JSON with all the hex codes, all the brand palettes, you can apply that JSON on each and every report going forward, right?

**38:39** · So, that way your report will stay consistent forever.

**38:46** · So, that was it. So, this is what I wanted to explain how you can use authoring skills that has been updated through Microsoft, how to utilize them for your agentic workflow in Power BI. So, all you have to do is update those plugins inside Claude. And the next video will be more about how you can use CLI. So, you can go to PowerShell as well and directly connect and work on it. So, you can use Copilot as well, so which is a Microsoft AI.

**39:16** · You can use Copilot instead of Claude and you can do the same things.

**39:21** · All right, before we conclude this video, I just wanted to know in order to create these four four pages, how much I was charged by Claude. So, for that, we can easily use context. So, I applied context command and it gave me 259k uh tokens used and uh it says uh So, I was curious like I used 259k tokens for just this session. So, it say I asked, "You used 259k tokens for just this stat?" And it said, "Yes."

### Token Used in the session

**39:49** · So, the heavy lifting was more about messaging and taking screenshots, all those things. And uh lesser was related to uh system a system or other tools with skills. So, that was just 52k. So, mostly it was messaging, going uh having conversations. So, I just wanted to understand for these number of tokens, how much I was charged. So, I was asking, "How many Can you tell me approximately how many tokens for one AOD cost? So, I knew that, but generally it is 1 million tokens.

**40:20** · So, somewhere it mentioned that. Right? So, yes. So, for $5 USD for 1 million input tokens and 25 USD for 1 million output tokens. Right? So, now approximately how much AOD for this session? Is it more than $5? So, what it says is roughly 3 to 5 USD, which comes out to be 6 to 10 AOD for the complete session. So, in $5 to $10, somewhere between that, we created four pages.

**40:56** · So, this is what uh we are into right now. Right? So, let me know in the comments below uh if you feel this is expensive or you feel this is going to be the norm in the future. And what do you think about working with authoring skills agent that has been uh uh announced by Microsoft.

**41:18** · In the next video, I'll be talking about the same uh data flow. Like how we can create Power BI reports using CLI, using the authoring skills, but using PowerShell instead of cloud. So, we can use Copilot instead. Right? And \[snorts\] after that, we are creating a new series of creating Fabric apps. So, that is a new feature.

**41:38** · So, if I go back to the announcement, and if I go back to announcement and go on the top, so, currently we worked on this. AI-powered Power BI reporting from design to deployment. So, that is one.

**41:58** · So, second is Fabric apps for semantic models. This is going to be very big. I mean, currently we are creating Power BI reports. That is important. So, we are not saying Fabric apps will replace Power BI reporting. that has a different scope, right? So, this is what we will be working on, and the next would be working on new desktop bridge. This is also new feature. All right, so, many new things coming up, and I'm really excited to cover all these topics.

**42:30** · So, feel free to watch other videos as well. Thanks a lot for watching this.