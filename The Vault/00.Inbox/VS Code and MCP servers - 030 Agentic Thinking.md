---
title: "VS Code and MCP servers - 030 Agentic Thinking"
source: "https://www.youtube.com/watch?v=nGAfWPq-DW8&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=nGAfWPq-DW8&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Power BI Tips]]"
published: 2026-07-18
created: 2026-08-08
description: "Linkshttps://github.com/microsoft/powerbi-modeling-mcphttps://learn.microsoft.com/en-us/power-bi/developer/mcp/mcp-servers-overviewFollow UsMike: https://www.linkedin.com/in/michaelcarlo/"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=nGAfWPq-DW8)

Links  
https://github.com/microsoft/powerbi-modeling-mcp  
https://learn.microsoft.com/en-us/power-bi/developer/mcp/mcp-servers-overview  
  
Follow Us  
Mike: https://www.linkedin.com/in/michaelcarlo/

## Transcript

**0:00** · \[music\] \[music\] Hello and welcome back to another Agent Thinking episode. I've got a quick demo today. We're doing a quick demo around just generating the Power BI MCP server and working with VS Code to get that set up. I had a couple questions recently from some users.

**0:28** · They were asking like, "Okay, we saw how you did the MCP server with um um Azure DevOps or GitHub. We'd like to see that how you would do it on your desktop. How do you work with it? So, this is a quick demo around that. With that being said, let's get down to our desktop and let's show you what's going on.

**0:46** · So, there are a couple ways to use the Power BI MCP server on your computer.

**0:50** · What you see here is my um desktop and I have a opened version of Power BI Desktop. Inside Power BI Desktop, I have a semantic model over here on the right-hand side. We can observe the model and it has some folders and some measures in it over here on the right-hand side. You can see this.

**1:09** · So, what we're going to do is we're going to connect the our agent. We're going to use in this case, we're going to use VS Code to connect to an MCP server that can talk directly to Power BI Desktop.

**1:20** · In order to do that, we'll need to bring up VS Code. So, this is my Visual Studio Code version here. Let me make it a little bit larger here so we can see what's going on.

**1:29** · Um I'm not going to use the folder area.

**1:31** · That's not something that we're going to need to utilize at this time so I can minimize that window. If you want to bring up your Copilot, you can use control shift I which actually brings up your Copilot and I'm going to clear this and start a new task.

**1:45** · We can mark all these other tasks complete.

**1:48** · We don't need to see that anymore.

**1:50** · These are all my old sessions and because this is so large, yeah, you're done.

**1:55** · Mark it all complete.

**1:57** · Okay, anyways, we'll let that all go. Go away.

**2:01** · Archive all these, we're done.

**2:03** · All right, that being said, so this is our new chat session here for our agent.

**2:08** · We can uh select a couple options here in our agent. One of the things we do need to do though, is we need to make sure that the Power BI MCP server is turned on inside VS Code.

**2:18** · So, what I do over here is I click this little icon, there's a little uh settings icon here in the bottom right uh corner of the chat window.

**2:27** · You click on this and this will bring up a menu and it'll show you all the different MCP servers that I've loaded to my computer, but they're either active or not active for my current session with my agent.

**2:39** · So, in this example here, I am looking at my different agents and I don't have the Power BI modeling MCP server.

**2:48** · If I want to turn this on, I need to check the box here and select that this option is turned on.

**2:55** · Clicking the option of the box and in order to make sure all the tools are loaded, I need to click on the update tools item and it will then bring me all the different items this can do. So, each of these items here is a tool that my agent will be able to use and communicate and talk directly to a model.

**3:14** · So, again, we have Power BI Desktop running locally on our computer, which means there is an Analysis Services model running on my local machine via Power BI Desktop. My agent is now inside VS Code and I'm just turned on the MCP server. I'll click okay and so now I need to be able to prompt my agent.

**3:33** · We're going to start a brand new session here.

**3:37** · Let's see if I can get rid of all these other messages. Okay, great.

**3:39** · All right, next um we can select what kind of agent we want to use. I have found pretty good usage around Claude Sonnet 5 or Opus 4.6. These are two agents that I use fairly regularly with using VS Code. Uh you could pick other agents as well. I find when I'm working with the semantic models, I kind of like a little bit higher-end model. Uh it seems to do a better a bit better job of reasoning and thinking through what I'm going to be building here. So, we're going to try this with Sonnet 5. If I don't get the results I want, I might switch over to 4.6 or 4.8 to get a little bit better modeling reasoning.

**4:12** · Okay. The other thing we want to make sure is if you don't see that MCP um server inside your menu, you may need to go add one.

**4:22** · So, over here, if I go to extensions inside VS Code, I can search for Power BI MCP, and there should be an item in this list called Power BI MCP Modeling Server.

**4:37** · So, this is the tool that I'm using.

**4:39** · This is the MCP server that I have installed into my VS Code, and that's what came down in the menu. So, if you don't see that in your menu item, you need to go install the extension directly from the store, and that's how you find it as well. Okay? We're going to close that out. We already know what we're doing there. And then, uh because I want to maximize my usage screen, if you click this little icon in the upper right right-hand window here, you can maximize your chat session and make it full screen.

**5:05** · So, I'm going to maximize my chat session, and I have that fully centered here.

**5:09** · Next, I need to tell my agent how to talk to Power BI Desktop.

**5:14** · So, the next thing here is how do I communicate with my agent, and how do I get it to connect to Power BI Desktop?

**5:20** · So, here, I can directly talk to uh my agent, and so I'm going to attempt to write a little message here and ask the agent to find my file, which is called star model. It's a star diagram. So, that's my star model. So, I need to know that when I'm talking to my agent here.

**5:37** · Also, I like to use this little chat icon. There's a voice chat inside VS Code, which you can use, which I absolutely love. I like talking to my coding tools more than I like typing to them nowadays.

**5:54** · I would like to connect to the Power BI Desktop file using the Power BI MCP modeling server.

**6:04** · And the file name is called star model.

**6:10** · Okay, I'm going to adjust my words here.

**6:12** · I think I said them out of out of step here. I'd like to connect to the Power BI Desktop to a Let's just do it to a Power BI Desktop file using the Power BI modeling MCP server. I'm going to use it the exact name. It's kind of backwards, but that's what they name it.

**6:31** · And the file name is called star model.

**6:32** · Okay, we'll see if it can get this. So, this in combination with the MCP server that we have here earlier. You can see that we have it turned on Power BI modeling MCP.

**6:43** · This should allow the agent to understand how to connect directly to this model locally. So, if I click return here or send, I'm going to send this over to my agent and we'll let my agent think for a bit about getting this modeling running.

**6:56** · It should be able to use the server. It should understand what's going on here.

**7:00** · Okay, so it's first it's looking through the connection tool. It's checking. Hey, I think I found this modeling MCP server. Let's establish the connection.

**7:08** · Great.

**7:09** · Okay, this happens to me all the time and I forget to turn this off all the time.

**7:13** · Every time the agent wants to make a command to read things or edit files or do something to your computer, there's this idea of a tool request. Every tool request, it is going to ask you or prompt you to to approve this. Do you want to let it talk to your machine?

**7:28** · You can allow in this session, that means the entirety of this session. You can click the drop-down menu and allow once in this workspace, always allow it, and then you can always allow other options here as well. Or I can go down here to default approvals and I can turn this on to auto autopilot. This is going to allow me to not have to say yes, yes, yes every single time. I can trust more of the agent and what it's building.

**7:50** · So since I've done this before and I kind of trust what the agent's doing, I'm going to click on autopilot on preview and then I'm going to allow in this session and that way it as it makes additional tool calls, it's not going to ask me for permissions for every single tool call that we make here.

**8:06** · So first thing it's doing, it's running the connection, found it, found the port, found the connection settings, connected to the star model.

**8:14** · Okay, great. Now we can start interacting with my semantic model. So the idea of this is that is as easy as it is. You give it the right kind of prompt. I found you really need to be explicit about what you're saying to the agent. I want to connect to Power BI desktop file. I want to use the MCP modeling server and you have to give it like the file name very clearly. With those three kind of really key pieces of details, the agent's really consistent on getting accessing and figuring out how to use that server.

**8:41** · Again, I really like calling out the server the MCP modeling server directly because then it knows to use that in order to connect to the model.

**8:50** · All right. So now we can actually interact with our model directly. I can say list all measures and then it will go through and it will make a tool call to go interrogate what's going on inside the semantic model. It'll run that tool. It'll then go get the data directly from all the measures that are in my semantic model and there we go. So it's able to talk to my semantic model and make all the additional measures that we want here.

**9:16** · I could also ask the agent to suggest we can and now it's a a co-pairing pairing code buddy basically. So I could actually even talk to the agent and ask it to suggest some additional measures I may need in this report.

**9:28** · So I can click on the microphone.

**9:32** · Please suggest some additional measures that might be useful to this report. I really want to focus on sales and sales performance.

**9:42** · Again, you know your business, you're going to know how to directly talk to your models and build semantic models the way you want, but I find this is really interesting to kind of collaborate with the agent and ask it to build various measures. Again, you should always check its work, you should always make sure the measures are doing what you expect them to do, but I find this is a really interesting way of giving additional feedback to yourself as you're building semantic models.

**10:05** · So, right now it's running a number of operations, it's looking at relationships, it's figuring out the tables, it's figuring out what columns are there.

**10:13** · And it's thinking through some things, it's reasoning about what other measures might be relevant to what we're building here.

**10:24** · Okay, so it's doing something around discount rates, it's doing some same period it's doing some time bound calculations. So, you can see here we can observe that the agent is now using same period last year, so it's uh trying to identify some time period differentiations, which is great.

**10:44** · Okay, it's going to build some structure here.

**10:47** · One thing I will do double check because my semantic model has different time periods, I'm just going to go check my model here really quick and see what date ranges we've got going on here. So, 2021 through 2022. I wonder if I still have the parameter here.

**11:06** · So, I'm I'm shifting the date range so that it can be more current. I have it currently pushing 8 years ahead.

**11:13** · So, 2026 I need it another 4 years, so let's make that instead of 8, let's make that 12.

**11:19** · And let's hit okay.

**11:21** · Let's apply the changes.

**11:23** · So, what I'm going to do is I'm going to reload my data, hopefully, and I'm going to hopefully push the calendar dates a little bit further.

**11:31** · What did I do wrong?

**11:34** · Oh, I have an issue in my sales model.

**11:36** · Yes, I know what this issue is.

**11:38** · The Power BI format, I'm using the standard Power BI format from inside Power BI. So, bear with me here while I fix this really quickly as my initial load data table does not have the table called sales.

**11:52** · Uh I believe there's a column issue in here that we will go fix.

**12:02** · Let's see if that will work.

**12:11** · Yep, right here.

**12:14** · Okay.

**12:15** · Hopefully that will run.

**12:18** · Are we getting everything else to work?

**12:22** · Seems like we're working out. Okay, close and apply.

**12:25** · I need to update my model. It's had some changes in since we've done some things here. Okay, excellent.

**12:31** · Let that run. While we let that update our model there, hopefully yeah. Okay, so 2026. This will help us with the deer the year date calculations that it's trying to do. I'm just pulling the dates a little bit forward here. Okay.

**12:42** · So, here it's suggesting some new measures. Okay, all these new measures are here.

**12:47** · Wow, it did a lot. Profit margin, discount rate, transaction count, which is doing some row transaction counting.

**12:53** · Okay, interesting.

**12:54** · Uh I also marked a dim date as the official date table. Awesome, previously unmarked. This is required for the year of a year and year-to-date. Great, that's the kind of stuff we want it to be doing. Very helpful. All right. Um so, these measures are here. Let's go see if we can find them now.

**13:09** · Oh, wow. It did a great job. So, couple areas of that it built here. So, even though I had the model make the changes, it actually made those changes. It followed my pattern of trying to move some of those measures into the folders that we see here. So, we can see here all those additional measures. So, we still have some sales KPIs and then some sales performance measures also being added here as well. Interesting.

**13:33** · Well, the the real test here is does any of this actually work?

**13:38** · So, um let's see here. Um average order value. All right, so let's just do that one. That one seems like something that would work over time.

**13:47** · Look at that. And we've got an average order value. Again, we have to check all the data as the agent makes these things. Um so they actually have sales prior year. Let's put that in there.

**13:56** · Okay, yeah, we've got some sales prior year, which would make sense.

**13:59** · The 2016 dates would have sales from the prior year. That makes sense for me as well. All right.

**14:04** · They seem to be working at an initial glance. I would probably review that a lot more. But now we have the agent building the measures for us directly in the model and with just a couple prompts, I got a a lot more information out of my model.

**14:17** · Okay.

**14:18** · So, we can go back over here. So, this is one way to connect with semantic model, right? We have Power BI Desktop open and I'm using VS Code. The Power BI MCP modeling server can also connect to models that are in the powerbi.com service. So, what I'm going to attempt to do is I'm going to to attempt to create a new chat session and we're going to try connect our Power BI GitHub Copilot here to a model that lives in powerbi.com and we'll see if it's able to connect there as well. So, first things first, let's create a new session.

**14:47** · I'll clear this and and make a brand new session here as well.

**14:51** · So, we've got a new session for VS Code.

**14:54** · And then I'd like to go over to powerbi.com and go find the URL of an existing model that I have. So, let me go pull up a powerbi.com. So, let's go to app.powerbi.com.

**15:05** · I'm going to go find this a similar data model semantic model and we'll see if we can connect to it and also grab some measures there as well.

**15:14** · So, go here. I'll go to my test database.

**15:17** · And I have this model over here in the service called another star model. Very similar design to what we have here. I believe the measures are slightly different and there's no folders, but we can go into the semantic model.

**15:30** · And what you'll notice is this model is um the view of it is here.

**15:36** · But I really want the URL. I want the workspace name and I want the modeling name. So what I'm going to do is I'm going to grab the entire URL. We'll copy that.

**15:46** · We're going to go back over to VS code and I'm going to say similar things, right? I want to connect to a model in the powerbi.com service using my MCP modeling server. And then we'll go that route.

**15:57** · Let me click the record button here and we'll try this again.

**16:02** · I'd like to connect to a semantic model that lives in powerbi.com.

**16:07** · I want to use the Power BI modeling MCP server to connect and make changes to this model.

**16:15** · Here is the URL of the model.

**16:20** · All right, so now I need to paste my full URL there into the agent.

**16:25** · And I will just also confirm that I just started a new session. I will confirm by clicking the settings, the configuring tools button.

**16:34** · We're just going to confirm that the modeling server is in fact still selected. Yes, it is.

**16:38** · We should be good and then now I can hit return.

**16:43** · And we will let the agent go connect directly to the model.

**16:49** · All right, so we're going to let that think here for a minute.

**16:53** · Now it might require me to sign in. So one of the things here too is before I was working on Power BI desktop. That's just local permissions for me on my computer with my agent in VS code. I may want to connect to a a model in the service.

**17:07** · But if I connect to a model in the service, there's going to be an authentication required to sign me in.

**17:13** · And so um over here on my other window, you can see here this just popped up on a different screen and it's asking me, "Hey, I need to connect to that model."

**17:22** · So, I will use my Mike at Power BI Tips email account.

**17:25** · It will authenticate me. So, it's going to authenticate me there, which is great.

**17:30** · And then, um I'm actually going to turn on the autopilot approval here.

**17:35** · Okay, so it's saying, um it was doing the request, it found the connection, it found the server. Okay, great. So, I think we're connected.

**17:43** · As expected, the XMLA endpoint needs the workspace name, it found it, here is the workspace name.

**17:50** · Uh oh, okay. So, it's actually asking me not for the GUIDs, which is interesting.

**17:53** · It'd be nice if this model uh was able to handle the GUIDs. So, by passing it just the URL, it's asking me for, "Hey, the workspace has a name and the semantic model dataset has an ID. I don't really have a way of connecting to those. Can you please give me those uh variables?" So, let me go back over to powerbi.com and I will directly connect using or get the agent the name of the model. So, the name is star model and the workspaces it is in is called workloads-dev.

**18:24** · So, it's asking me for this and this and not just the URL. Okay, so we got a little stuck there.

**18:30** · Let's fix this.

**18:32** · The workspace name is workloads-dev and the model name is star model. And I'll put those in quotes so it knows that that is entirely of what I'm talking about.

**18:49** · Give it a little bit of extra context here.

**18:53** · Okay. Now, I will hit enter to send this back to the agent. Enter.

**18:58** · Okay. So, now that I've given it some explicit information about directly connecting to this model, we'll see if we are able to get it connected. All right, connect successfully connected to the star model. Okay, great.

**19:12** · Uh let me know what changes you'd like.

**19:14** · List all measures.

**19:17** · So, let's see if it's able to list the measures from powerbi.com and to give you a comparison, I have the fact sales table and I have a handful of measures in some folders as well. So, I should see a similar result to what we saw earlier and there we go.

**19:32** · Great.

**19:33** · You can also do the same thing we were doing in Power BI Desktop, which was uh once we've connected to the model, we're able to list the measures. You can ask it to make manipulations to tables, do formatting and changes, add documentation, add descriptions, move things into folders, all the really rich things that you need to do within semantic models. This chatting experience will allow you to directly talk to the model and it will make changes to the model. Again, models and agents are not always great.

**20:00** · So, um you definitely need to be careful when the agents are building things. It will build things for you, but you need to be mindful of what it is building and reviewing its output to make sure that it's all correct and acceptable.

**20:12** · All right. That's all for our demo today. I hope you liked working with VS Code and directly connecting to the MCP modeling server and getting that information directly up into powerbi.com and in Power BI Desktop.

**20:27** · Thank you so much. We appreciate your time today.

**20:29** · Have a great day. I hope you learned something new and fun today with our agentic thinking demos demonstration today. Thank you all and we'll see you next time.

**20:41** · Agentic thinking.

**20:45** · \[music\] Agentic thinking. \[music\]