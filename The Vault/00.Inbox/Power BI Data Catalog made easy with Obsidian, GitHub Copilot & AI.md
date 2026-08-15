---
title: "Power BI Data Catalog made easy with Obsidian, GitHub Copilot & AI"
source: "https://www.youtube.com/watch?v=nqX3Ta-nq44"
video_url: "https://www.youtube.com/watch?v=nqX3Ta-nq44"
creator: "[[Power BI with AI Vibes - Jasmin Simader]]"
published: 2026-07-20
created: 2026-08-08
description: "Want to automatically document your Power BI semantic model and visualize your data lineage?In this tutorial, I'll show you how to build a complete AI-powered data catalog for your Power BI PBIP pro"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=nqX3Ta-nq44)

Want to automatically document your Power BI semantic model and visualize your data lineage?  
  
In this tutorial, I'll show you how to build a complete AI-powered data catalog for your Power BI PBIP project using Obsidian, GitHub Copilot, and AI.  
  
Instead of manually documenting tables, measures, and relationships, you'll learn how to generate structured markdown documentation directly from your semantic model, create clickable links between objects, and explore your model through an interactive knowledge graph.  
  
By the end of this video, you'll have a reusable workflow that helps you understand dependencies, improve documentation, and make your Power BI projects easier to maintain.  
  
In this video you'll learn  
How to create a data catalog from a Power BI PBIP project  
How to use GitHub Copilot for AI-assisted documentation  
How to generate markdown documentation for tables and measures  
How to build reusable documentation templates  
How to visualize data lineage with Obsidian  
How to connect related objects with clickable links  
How to create a reusable AI workflow for future Power BI projects  
Sample Project  
  
GitHub Repository:  
https://github.com/Jasmin319/Power-BI-Vibes/tree/fbb2fe838894cf004fb6b1e6498a6ea680a7f827/Data%20Catalog%20with%20Obsidian%20and%20AI  
  
Tools used  
Power BI Desktop  
Obsidian  
Visual Studio Code  
GitHub Copilot  
  
If you enjoyed this tutorial, don't forget to like the video, subscribe to the channel, and let me know in the comments how you document your Power BI models.  
  
Chapters:  
00:00 — Visualizing a data model with Obsidian and AI  
01:39 — Setting up Obsidian and VS Code  
03:21 — Preparing the data catalog folder structure  
04:35 — Creating a template for table documentation  
05:51 — Generating documentation from the semantic model  
10:36 — Exploring the catalog in Obsidian  
12:16 — Documenting all tables and mapping relationships  
16:07 — Creating a reusable documentation workflow  
21:12 — Generating and linking measure documentation  
32:53 — Exploring dependencies in the visual graph  
36:24 — Using local views to assess model impact  
39:09 — Wrap-up and next step  
  
Website:  
https://www.jasminsimader.com  
  
LinkedIn:  
https://www.linkedin.com/in/jasmin-simader  
  
Medium:  
https://medium.com/@jasminsimader  
  
GitHub:  
https://github.com/Jasmin319

## Transcript

### Visualizing a data model with Obsidian and AI

**0:00** · Some people have a foreign data catalog, but you could have a complete visualization of your data model and all the dependencies by just using Obsidian and AI. And the great thing about this is you can click on a fact table to fact all the table. You can make a right click, go to open local graph, and you can see immediately which elements in your semantic model are using the fact order table, so you can see the measures, this all the M and the line files.

**0:30** · You can see the tables that are connected to the table, and I think this is a pretty good way of organizing and summarizing the knowledge of your semantic model in Obsidian using AI. So, if you want to know more about that, stay tuned.

**0:49** · Welcome back to my latest video, and today I will show you how you can create the data catalog out of your semantic model of the PBIP file using Obsidian and AI.

**1:00** · The idea to do that came out of some discussions with Marcus Riegner, you'll see him in the picture, because Marcus was showing me how he's documenting his knowledge using Obsidian and AI, and he also showed me how I can do that. And then I thought, why should I not use that to do what I love to do to bring data health closer to people.

**1:24** · So, I was thinking, how could I use what he showed me to document a data model and create a data catalog out of it? And this is what we will do today. So, a big thanks again to Marcus for sharing his knowledge, and now we are getting started. So, the first thing you want to do is you want to install Obsidian. To install Obsidian, you can use Google and type in Obsidian.

### Setting up Obsidian and VS Code

**1:48** · And then you can see here Obsidian. You can click on it, and then you can click on the button get Obsidian for Windows. Obsidian is a note-taking tool. This means you can put it all your notes and then you can use Visual Studio and GitHub Copilot to create some MD files out of this notes and turn notes into knowledge because you know having notes does not mean you have knowledge about this.

**2:13** · So you might want to take your notes and make one of restructure them and say this is the knowledge of the notes like what is the key phrase I was talking about and for our measures this will be how are they calculated? What is the business description for the tables? What columns do they contain? What data types are those columns?

**2:33** · And if we create these MD files for the tables and the measures and link them together now, then you can also see the data lineage in the end because the measures will be connected to the tables they use for calculation and so on. And this is what I want to show you in this video.

**2:53** · First thing like I said, you have to start Obsidian.

**2:58** · And then you have to install Visual Studio Code if you don't have it.

**3:03** · If you have it already, it's pretty easy. You have to open the folder you want to work with. My folder is already open. If yours is not open, you go to open folder and choose the folder you want to open.

**3:18** · And I will show you what's in this folder. In this folder, I have put a structure for the data catalog and the Power BI PBI MP file. So for the Power BI PBI MP file, you can see here the report folder, the semantic model folder, and the PBI MP itself.

### Preparing the data catalog folder structure

**3:33** · And if we go back to the data catalog, you can see I have already created a folder for the business glossary, a folder for measures, and there's also already a template how I want to document the measures, and I have a folder for the tables.

**3:54** · I will rename that because it's not English.

**4:00** · So, tables.

**4:03** · Tables.

**4:04** · And then I have here a markdown file and this is the structure of the data catalog. You can find all these files in my GitHub. And if we go to the tables folder, you can see that I created two tables there, one for the dimensions and one for the facts. And there is also an MD file for the template for the table documentation because I already know how I want to create the documentation of the single tables.

### Creating a template for table documentation

**4:35** · I can show you that template here.

**4:39** · So, in the data catalog, if we move to the tables and make a right click on template and open preview, you can see what I was doing here. So, here I'm giving the specific structure I want to have for the table documentation.

**4:55** · So, I want to have a table with the property and the definition, so the classification, the description, the query ID, if it is a well area, the type, is the load enabled, the source system, the source object, the granularity of the table, and so on. The primary key.

**5:14** · Then I want to have a column list that gives me all the columns that live in the table. So, the data type, the property, the description.

**5:23** · I want to have an overview of the keys and the foreign keys, an overview of the relationships of these tables, and then some usage and context. You can delete that. You don't need that.

**5:36** · But in my case, I'm using that. And if you have watched some previous videos, you will know that in the Power BI PBIP file, all these informations are living in the semantic model. And in the semantic model, you can already see in the tables folder, there are these TMDL files for the tables.

### Generating documentation from the semantic model

**6:01** · And AI is now expected to drag all this information out of that and create some MD files. And this is what we will try now.

**6:13** · We will test the table. So, we will tell him, "Can you create a documentation file for the, let's say, customer table by you documentation template for the tables under the TMDL file of the table in this location."

**6:42** · And the great thing is now, I can go to the customer table, make a right click, and say copy path or copy also relative path.

**6:58** · And insert that here, and that then he can see that the path is given. And now we will see what he's coming up with if we run this prompt. The only thing I didn't tell him is where he should put this table now.

**7:12** · But we will see where he's putting it.

**7:14** · But he's already telling us he's doing that in the dimension folder because he found out that this is a dimension table. So, now you can see here the MD file in the dimension folder. As you can make a right click and say open preview, and then you can see what you documented. The name of the table is dimCustomer. The overview is the role, it's a dimension table. The source, it's a customer disease. Fee, it's a Power BI query import. The description was contain for all customer including company name, contact information and geographic location.

**7:47** · And enables analysis of sales by customer and region last update to be defined.

**7:54** · I don't like that he's not making breaks here, so I go to the template and check the template and I can see here that this is the problem. So, I have to add two spaces here.

**8:06** · Also here.

**8:08** · And go to control S, then it's saved.

**8:13** · And now I can say I have updated the template for table documentation.

**8:22** · Tation.

**8:23** · Please update the customer table MD file.

**8:29** · And then it's working again. I did not make specific settings, so I'm using GitHub Copilot in the auto mode and let GitHub Copilot choose himself the mode that he wants to use.

**8:44** · And so, he's telling me he's ready. And now you can see it's much more readable.

**8:49** · So, sometimes you have to adjust your templates.

**8:54** · Then you can see here the table description I wanted to have. It's a dimension table, the description, the query, the lineage tag.

**9:03** · So, it's a dimension table, load enabled yes, source system local files used via Power Query. So, I'm loading this from my C drive.

**9:11** · The source object was the customer CSV, the granularity one row represents one customer company, and the primary key is the customer ID.

**9:20** · And now you can see that he's following exactly the structure I gave him. He's giving me also some primary key information, the customer ID, it's a text, it's unique. Of course, it should be unique, it's a primary key.

**9:34** · And the a business key used to uniquely identify each customer.

**9:40** · It wasn't detecting any foreign keys, but it is detecting also relationships, some incoming relationships, foreign keys referenced in this table. So, from the order, the customer ID and outgoing relationships were none. We can check that also if we open up the PBI P file. And then the PBI P file, you can see in the data model the dim customer here. So, it's really connected with fact orders.

**10:11** · It's a dimension table.

**10:14** · And the primary key is the customer ID.

**10:17** · And in the fact order orders, the foreign key is also the customer ID.

**10:23** · So, I think I I did here a pretty good job. And now we will open that in Obsidian. So, in Obsidian, if you have installed it, you will have a screen now where you can connect to a folder. If you have already installed it, you have to go there to vaults.

### Exploring the catalog in Obsidian

**10:43** · And then you can click on open folder as vault.

**10:50** · You go on open.

**10:52** · And then you can choose the folder.

**10:55** · And then you see here the same structure we already saw in Visual Studio Code. And then you can click here, and then you will see a graph, which is pretty great.

**11:09** · You can see here a welcome file, which is empty, I guess.

**11:15** · Yes, because we didn't write anything into that. You can see here a new link in the welcome file because it's pointing to some links. And you can also delete that file because we don't need it. So, right click and delete.

**11:30** · And it's gone.

**11:33** · I will have a look if I can change my language so that it is getting easier for you.

**11:41** · And here I can change it to English.

**11:44** · But we have to restart. So now you can see here it's English and you can also follow it.

**11:51** · Then we have here the master documentation process that is going to an empty link and here you can already see the dim customer.

**11:59** · At the moment everything looks the same and nothing is linked because we did not put any links in the documents. And the next thing we will do is we will do the same what we did for that table, also for the other tables. So we will create all the documentation in Visual Studio Code for all tables.

### Documenting all tables and mapping relationships

**12:23** · And we will try to tell him that can you now create the document tation file for table in this folder view. And now we will see what he's coming up with.

**12:45** · He is telling me he has identified 10 remaining tables to document. Next thing I'm reading HTML so I can build accurate column key and source details before creating all markdown files in which.

**13:00** · And you can see him working now so he has created for the dimension tables the empty files here and also the fact tables are filled now so we have the fact orders and the fact order details.

**13:14** · And you can also see that he had some tables he did not know where to put.

**13:19** · So the time intelligence, the master catalog and the measures and these are outside. And now we will have a look at Obsidian what happened here. So we will go back to the graph.

**13:32** · And you can see here now that they have multiple single table files that I can also click on. And by clicking on I can see the descriptions.

**13:44** · So up to now this is not so bad.

**13:47** · But it's not really helpful because I can only see the single files, but I cannot see some connections. So the next thing we will tell him is the tables are connected via the relationships.

**14:07** · I want to see that in Obsidian.

**14:12** · So please add links in the single table from MD files to the tables they the specific table is connected to relationship.

**14:37** · And now he should add three table links in the tables MD.

**14:45** · And if he's doing that, you can see then also in Obsidian that he's starting to link things together. And like I'm always saying things you can't see, you can't check.

**14:58** · I really love to go back then to Obsidian and find out what happened. And you can see here that he was connecting the tables to the tables they are connected with. So you can see here the orders table, you can see the star schema, the dim employee, the fact Sorry.

**15:23** · The fact order, the fact order detail, the dim product, the dim category, the calendar, the dim employee, the dim customer, and the dim shipper. So, you can already see that this node got bigger because here there are a lot of lines incoming.

**15:40** · And that other nodes are smaller because they do not have any connections. And the great thing for the user is he can now click on fact order.

**15:51** · He can scroll down.

**15:54** · And he can also go here to the other tables. So, he can go to the dim customer table.

**16:00** · And from the dim customer table, he can also go back again to the fact order.

### Creating a reusable documentation workflow

**16:07** · And so, this is also getting some clickable knowledge where people can understand how things are connected. And where they are coming from.

**16:17** · So, the next thing is now we want to do the document the measures. But before we do that, we will do something else. We will ask him to summarize this procedure now in an agent MD file because we want to make it reusable for another PBIP file. And the agent should then know how we will handle that knowledge.

**16:39** · So, can you summarize the procedure up to now in an agent MD file so that you know how to create the documentation next time starting with starting with the semantic PBIP file.

**17:05** · Please do that in a way that it can also be transferred to another PBI P file.

**17:22** · And now I expect him to summarize the procedure he was doing and to store it for me. So, next time I don't have to tell him, I just can say him, "Please start creating the documentation of the tables." And he will exactly know where he should go. I will show you what I mean as soon as the edited MD is finished. So, we can also click on the preview here. So, the purpose This playbook defines a repeatable process to create Obsidian ready table documentation from a Power BI PBI P semantic model.

**17:56** · Required import Power BI semantic model definition tables, relationship file is the relationships TMD, and the documentation template is the template for the table documentation, and the target output folders are here.

**18:12** · So, he's referring to the same folder structure. Uh, if you want to change that, you can just tell him that, and then he's giving you also the steps and also some quality checks.

**18:25** · So, as we have the tables now, we need for the next thing the measures, and you can also see that he created here some links because I think he's using them as an example.

**18:41** · If you do not like the Obsidian links, you can also make him use proper links in the table files because then you can click it also outside of Obsidian.

**18:53** · And maybe this would also be a good thing to tell him, "Can you change the Obsidian links and the single table from MD files to real link using the path of the related table and default.

**19:16** · So, this will make sure that you have clickable links that work also outside of city and and we will check that when he's ready because this specific links he was using can only be shown in Obsidian.

**19:35** · We will have a link to what he did and you can see now that the click on effect order.

**19:42** · He's going to affect order and if we click on it to see the link, you can see that it is now really a link and not this Obsidian tag.

**19:52** · And we can check again Obsidian and it is still working.

**19:57** · So, the next thing we will ask him now is to update the update the agent.

**20:09** · And make sure that links used in the workbook are using the path of the connected of the connected file and not the Obsidian way of linking files because I want to keep it reusable.

**20:36** · Because we don't want to lock us into a system that is only working with one software. And so, if you do things like that, just keep in mind how could I do that to keep it reusable. And in our case, this means not using this Obsidian tags because then I can also click through on my laptop because this is living on my laptop in the end in the folder structure.

**21:00** · And he did that now and now we'll eventually go to the master documentation. So, I will tell him I wanted you now a measure documentation documentation for all the measures in the model. Use the measure template.

### Generating and linking measure documentation

**21:22** · Use the measure documentation template for that.

**21:27** · And create for each measure an own empty file.

**21:35** · And now I will see what is coming up because at the moment we can only see the tables. Sometimes you have to allow things because he needs to write things.

**21:46** · You just should read what you're allowing to.

**21:49** · And we will see what he's doing because at the moment this is a strange file he created.

**21:57** · But he's still working and you can see that he already did a lot, but he had also on parsing errors, so he has to check things and he's working on that.

**22:08** · And you can also see in Obsidian right now that they got a lot of dots that are not really connected to anything. They are just somewhere in the knowledge sphere, let's call it like that.

**22:23** · But you can see he has to do a lot because there are really some measures in the table.

**22:33** · But it could be bigger. So, this is an empty file we do not need because I don't know what he did there, so I will already delete that.

**22:41** · And then we will have a look what he was doing. So, this is for example the measure average days to ship.

**22:48** · It has a measure group shipping and it's living in the measures table.

**22:54** · The DAX is the fact order days to ship.

**22:57** · The technical description of the measure is named average days to ship. Purpose average number of days from order date to ship date using days to ship and the current filter context. The used measures are none. The used columns is the fact order days to ship. The used table is the fact order.

**23:16** · And this is what we want to do first now is we want to link to that used table because in the data catalog we want to know which measures are using which tables. So, the first thing we will tell him now is in the section

**23:39** · used table used used tables of the single ID measures from empty bars can you make sure that the tables listed there also have clickable links.

**24:05** · And then I'm expect him now to make this link clickable and if this link gets clicked ever, I can also go back to the table alarm and we will see that in Obsidian. And you can see already here the used table is now a link which is pretty great. And if we go back to Obsidian now we should see that the measures are linked, but it doesn't look like that. So, we will have a look at this link. The editor could not open because the file was not found.

**24:39** · So, something is not working with this file.

**24:44** · So, he's he has created now a file what we do not want.

**24:49** · So, we will delete that also that.

**24:53** · And now you can see he didn't do what we wanted want him to do. so we will have a look again.

**25:00** · Fact fact order and the this a little bit of funny because it's not working but we will just say can you please check if all the table links are working now.

**25:16** · It seems like the link in the average days to ship {point} md is broken. And this is also the great thing of Obsidian. You can check immediately if things are working out and if he's doing what you want to do him by connecting all these dots because you can follow up the process visually.

**25:46** · And you can see here that the measure is connected now to the fact order table because the average days to ship is using that table. The only thing I do not like now is that I cannot see anymore that this is a measure so the first thing I will tell him is can you please put the prefix for all the measure {point} md files

**26:22** · because then it's getting much easier for me to see in Obsidian which is what.

**26:27** · So now I can see for the fact order table there are some measures like late orders order count and the average days to ship. As we already see that there are some other measures that are not connected we will go back now and you can also see that we do not have related tables for measures that are relating to a measure.

**26:56** · And these are the measures we will not connect to a table. We will connect them to a related measure. So, we will make sure in the next step that the related measures section is also a clickable link. So, we will go back here and you can still see that there are some unconnected ones and I think that unconnected ones are having these issues.

**27:20** · So, we will say to him now, "Can you also make sure that in the measure from MD files in the section related measures, the link to the MD file, total.md file from the related measure is included.

**27:54** · And included.

**27:58** · And now I expect him to change that to a clickable link. When we are finished with that, we will also ask him to update the agent MD file with these informations before we do anything else.

**28:11** · Can you update now the process described agent MD file to make sure that you know how to handle that you know next time how to handle the measure the generation of single measure. This is something I do in between just to make sure that he knows what he's doing.

**28:42** · You can also split that up then later into the measures folder and tell him just if you talk about meshes in the agent empty go to this measure folders prompt file or anything else. But at the moment I keep it in the agent empty.

**28:59** · So you can experiment with that and find what works best for you. So we will open the preview here again.

**29:08** · And we can see that the link is still not working. So we will check what he's doing here. And you can see that we are having travels with a blank. So this is always happening if you are creating links with blanks. So we will tell him, "Please make sure that links are working as the file names often include blanks and this is causing problems.

**29:39** · This is a problem that occurs very often if you use file names with blanks. So maybe you should avoid that.

**29:48** · I use them, but sometimes I have to correct the links then. And I hope it will work then afterwards because this is at the moment the reason why these links are broken.

**31:48** · And the funny thing is here it's working now. But in the current folder, it's still broken. So we will really go back here. Copy path and say the link to the relative measures in that file is still broken. Please fix it in that file.

**32:23** · And now I really hope that he's also fixing it in that file and we will have a look at the other files because in the other files, you can see it's working because here is the use measure, the average discount rate. So it's working. I didn't want to break it down on the granularity of columns because I think this is too much for visual representation.

**32:43** · And you can see already that the links are getting bigger and that you see where a lot of meshes are moving in. And the time intelligence is something that is used here a lot. And we will have a look at the Power BI file what this time intelligence is doing. And this time intelligence is a calculation group.

### Exploring dependencies in the visual graph

**33:11** · And I know that I was creating a calculation group for the current, the prior, the year over year because I was too lazy to rewrite the measure logic each time again and I used MCP for that. You can also see that in that video.

**33:29** · And so, it's right that there is a lot of going back to the time intelligence and then you can see that there is a big dot for the fact orders and the order count and the total sales and things like that. And what you can also do is you can go to the forces and play around with these slices to make the model more compact or to put things farther apart and then it's easier for you to see what's going on.

**34:03** · You can also play around here. And you can also try to get some colors in, which is not always that easy by creating new groups. You can, for example, create a group for all these and files and make it green.

**34:21** · And we will check if he's taking the tables. This is not always a very intuitive way. I'm did also not found out how he is applying that because he's not always applying what I want him to apply in the colors, but here you can see now that the fact order, the fact order detail, and the dim product are green.

**34:48** · And the tables, the dim shipper, and so on are pink, which I did not want. But you can see that everything that is connected to I don't know. So, the logic of these colors is not very clear for me often, but you can try.

**35:06** · But you can see also that there are some links that are not working, and the not working links are these one, for example, because the fact order table link is not always working because you can see that the average days to ship table has a wrong link, and the average discount rate has a wrong link.

**35:32** · But these parts of the star, let's call it like that, or the flower, or however you want to name it, should go back to one of the tables and not end here somewhere in nowhere. But the great thing, which I'm really like about that, is for the user, you can see the dependencies, you can see where there's going on a lot. If you want to delete things in um a model, you will immediately see the impact of it.

**36:01** · You can also cut out pieces by going to the fact order, for example, making a right click, open linked view, linked view, and open a local graph, then you will only see what's connected to the fact order, so you get a better overview, and you can here again play around and make it bigger and smaller. You You also drag around things. So, in my opinion, it's really great what you can do with it.

### Using local views to assess model impact

**36:31** · You can also close it here and just um make it better visible. So, you have endless options. And I really like this way of visualizing the little and the model dependencies because, like I always say, what you can't see, you can't check, and you can't understand.

**36:52** · And this is a pretty good way of making a visual data catalog. So, here we will finish up. We see it's still not working. So, we have to go to the singer MD files and check what he's doing there. So, we go to the MD um the discount rate. Go on the preview mode and check all the details, facts. And now you can see that the link is working.

**37:17** · I think he's using the wrong slashes, and we have the same problem still in the average days to ship, average days to ship. And here the fact order is also not working.

**37:35** · fact order control S And I hope now, yes, it's working and it's properly connected. We can close that to show you. And now you can see that it's all going back to this node. We can also change the node sizes, which I often like to do to make it a little bit better. You can also change the line thickness.

**38:00** · And you can see now that this is a very important node. So, in the time intelligence, you can see that this is a calculation group. So, we will have to overwork this table, I guess, because it's not that clear, but at least you can see that there's a lot of measures are depending on that. So, if you delete that, you will be lost.

**38:23** · And you can also see that on the order details, there are a lot of measures and on the fact orders. And if you click in there, you can also see where these things are going. You could also add now in the tables as the system knows it the measures that are connected to the table, but I think for now it is enough and I showed you how you could approach that and how you could do that.

**38:47** · So, I hope I could tell you how you can use Obsidian and AI to create a data catalog that is clickable, that is showing you the data lineage, where the objects are coming from, where they are connected, and what happens if you're deleting one of them. In my opinion, this is a pretty nice way to visualize what's going on in your model. You can also connect it to GitHub and make it reusable or make it versionable, also. You can also bring in more semantic models by doing so.

### Wrap-up and next step

**39:18** · So, this is all up to you. I just wanted to show you the core concept here and give you a starting point for doing that. So, I hope you liked the video and see you next time. Wish you a great day now and bye-bye.