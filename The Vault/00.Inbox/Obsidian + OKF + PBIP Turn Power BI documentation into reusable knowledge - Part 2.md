---
title: "Obsidian + OKF + PBIP: Turn Power BI documentation into reusable knowledge - Part 2"
source: "https://www.youtube.com/watch?v=EMGfCK3_9Rk&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=EMGfCK3_9Rk&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Power BI with AI Vibes - Jasmin Simader]]"
published: 2026-07-27
created: 2026-08-08
description: "In this video, I show how to standardize an existing Power BI data catalog in Obsidian using the LLM Wiki concept and the Open Knowledge Format (OKF).You will learn how to run a structured gap check"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=EMGfCK3_9Rk)

In this video, I show how to standardize an existing Power BI data catalog in Obsidian using the LLM Wiki concept and the Open Knowledge Format (OKF).  
  
You will learn how to run a structured gap check, add YAML frontmatter, introduce index and log files, and improve graph navigation with tags and color groups. I also walk through creating a semantic model overview and a business glossary with reliable links to table and measure files.  
  
The outcome is a documentation system that is cleaner, more reusable, and easier for both teams and AI agents to work with.  
  
This walkthrough is especially useful if you work with Power BI PBIP files, semantic model documentation, Obsidian knowledge management, GitHub Copilot workflows, metadata standardization, Open Knowledge Format (OKF), and LLM wiki patterns for a portable data catalog.  
  
Resources and shownotes:  
https://karpathy.ai/  
  
Obsidian Plugin - LLM Wiki  
https://community.obsidian.md/plugins/karpathywiki  
  
Karpathy Gist - LLM Wiki  
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
  
Google - OKF description  
https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing?hl=en  
  
OKF - Google Spec  
https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md  
  
OKF - Obsidian Plugin  
https://community.obsidian.md/plugins/okf-enforcer  
  
Starter File on GitHub:  
https://github.com/Jasmin319/Power-BI-Vibes/tree/main/Standardize your Data Catalog witk OKF  
  
Chapters:  
00:00 Introduction: Upgrading a Data Catalog  
01:11 What Is an LLM Wiki?  
02:00 Understanding the OKF Standard  
03:04 Adding Indexes and Metadata  
06:19 Organizing Notes with Tags and Colors  
09:30 Creating a Semantic Model Overview  
10:50 Building the Business Glossary  
11:56 Wrap-Up: A Standardized, Shareable Catalog

## Transcript

### Introduction: Upgrading a Data Catalog

**0:00** · So, welcome back. In my last video, I showed you how you can use Visual Studio and GitHub for Copilot to turn your PBI RP into a visible and clickable data catalog. Today, I will show you how you can improve that data catalog in Obsidian and most important, how you can standardize it by using OKR F and the idea of the LLM wiki. This helps you to make it more standardized.

**0:30** · It will always be structured in the same way and it will also be fully portable. So, first today, I will show you some basics about the LLM wiki and what the OKR F means and then I will show you how you can implement that in the existing data catalog we built together and how you can upgrade your data catalog by doing so. So, this is what we were building together last time.

**0:55** · You can see here the time intelligence measure group and you can see here a table, the fact order and you can see it is not colored right now because we had travels last time also implementing the colors. So, I'll show you today how to

### What Is an LLM Wiki?

**1:13** · structure that a little bit better so that it is standardized according to the OKR F and I will show you some tips and tricks on bringing in here the right colors to differentiate if this is a table or if it is a measure or something else because I found out it can be done pretty easy when you know how.

**1:32** · So, the first thing I want to show you is the idea of the LLM wiki. The idea of the LLM wiki was created by Andrej Karpathy. This is Andrej Karpathy.

**1:45** · And this is his idea of the LLM wiki.

**1:50** · And the LLM wiki is an idea how you could structure your wiki better for agents without using rack. Rack means retrieval augmented generation, so you have to translate the words of a document and of a search into vectors, then you create a database with all these vectors, and then you can search in this database by putting in a word. This word is translated into vector, and then the database is searched for this vector.

### Understanding the OKF Standard

**2:24** · This is one concept, and the other concept to store knowledge in an accessible way for AI to agents is an LLM wiki.

**2:33** · You can find that in this test, and then you can read through it. I will link it also in the show notes. And here is given the idea of an LLM wiki.

**2:44** · And the architecture of such an LLM wiki is usually the same, so you have three layers. The raw sources where put in all the information you'll find, then you have the wiki. So, in the wiki there is the translated knowledge that you pulled out of your raw sources, and you have a schema. So, a document, a cloud MD, or an agents MD for Codex.

### Adding Indexes and Metadata

**3:12** · You can read about all of that in this document, and you will also find Obsidian here and some other tools you can use to visualize that. So, this is the first thing you want to read through.

**3:25** · The second thing is then Google was building a standard on this idea of the LLM wiki to standardize it more and to make sure that you can use it across multiple LLM wikis, and that people have an idea how this LLM wikis could be structured, and people could reuse it.

**3:45** · And this is written down in the open knowledge format, short OKF.

**3:51** · And here you can the idea of the OKF.

**3:54** · The OKF says you will use just markdown files, so it will be readable in any editor and renewable on GitHub. And it will be indexable, and you will not lock in yourself into a tools.

**4:09** · It will use just files and nothing else, so you can store it anywhere, and you can also store it in Git.

**4:16** · And one of the most important thing you will have a YAML front matter, and this front matter helps agents find your information faster and interpret and understand them better. And the good thing now is you don't have to read through all of that because also the OKF is on GitHub. I will also put the link in the show note, and you only need a spec empty file.

**4:43** · And if you download the LLM Wiki from Copacetic and the spec file, we are ready to go.

**4:52** · Because what I did then is I created a folder. You can see that in Obsidian where I put them in.

**5:01** · And now we will jump into Visual Studio Code, and I will show you how you can use these two MD files to improve your existing data catalog. So, here we are in Visual Studio, and you can see here the LLM and the spec MD I put in, and the rest is the same like in the last video.

**5:20** · And the first thing we will do now is we will ask what the difference is from the existing Wiki to the spec or to what's described in the spec and in the LLM Wiki MD, and what changes would be necessary to come closer to the concept, but we also will tell the agent not to change anything yet.

**5:44** · So, can Can me the main differences from the data catalog in this folder to the concept described in the L M Wiki MD and the spec MD.

**6:07** · Please list the differences but do not change anything.

**6:17** · And then we will see what it's coming up with. And here you can see that it's coming up with some points.

### Organizing Notes with Tags and Colors

**6:24** · So he's saying the catalog is a domain specific Power BI documentation set centered on tables, measures, dimensions, dashboards, and he's also saying OKF expects each concept to be a marked on file with the YAML front matter including a required type field and optional title, descriptions, resources, tags, and timestamps. The catalog docs instead use custom model-oriented page layouts like measure group and quick overview. So the first thing we could include later is the front matter.

**6:54** · OKF treats index.md and log.md as optional by the conventions for progression, disclosure, and change history. This folder uses a separate structure node class per asset documentation, not the OKF index log pattern. We will also include that in our dictionary. And in my opinion, these are the most two important ideas we will take over from this L M Wiki.

**7:21** · The first thing we will tell him that he's not allowed to change anything in the Power BI folder.

**7:28** · So we will copy the path and tell him can you please add an index MD file to all the places where necessary.

**7:45** · And also add the front matters in the single MD files, but please also make sure not to touch that folder because this is our Power BI file and do not make any changes in this folder.

**8:12** · In this folder.

**8:18** · And now we will wait because the index.md is important because it's an index, so you will see immediately which files are in single folder. So, I think this is really helpful because we have a folder with measures and we have a folder with tables. So, I really like the idea of the index files.

**8:40** · And the front matter is also a good thing because the front matter helps you to keep your files more standardized and then you can also share it with other colleagues or other places where you might need them. And last but not least, the front matter helps agents understand your MD files better. So, in my opinion, these are the most two important things we have to implement.

**9:09** · And then you can see here already the front matter coming up with a type, a title, a description, and a timestamp.

**9:17** · And we will also check another one and it's also there. And we will also have a look at the tables.

**9:25** · And also in the table you can see the front matter. And you can see here already the index.md in the tables and this is looking like that. So, it's again an overview about everything that is in this folder.

### Creating a Semantic Model Overview

**9:40** · What we forgot is the log file, so we will also tell him, "Please and also the log MD to the catalog. Because the log MD is also important, I will be able to see all the changes. And we can also see here an index file for the workspace.

**10:02** · And in the workspace it's pointing to the A turn, to the L and M, and the week here, and here you can see the log files now, so also for the dimension tables there is a log file.

**10:15** · And at the moment it is initialized, so I did a log file for the dimension score. We will keep that, and we will have a look at Obsidian now how this is looking like.

**10:25** · And you can see here this is the fact order, this is also the fact order detail. So, things did not change that much, but here you can also see this index notes. And I do not like to have the index files in the graph view because I find it misleading.

**10:44** · You can go to settings, you can go to files and links.

**10:48** · You can scroll down and excluded files, and in manage you can also enter a reg ex for the index file, so we will make a screenshot of that and ask here, "Can you give me the reg ex to exclude the index MD files from Obsidian?

### Building the Business Glossary

**11:16** · And the stranger, "Please use also the information in the screenshot." And then we will see what he's coming up with. You should type much better than I do.

**11:31** · Then we will copy that, go back to Obsidian, and I think we will need it like that.

**11:39** · Click save and close. Then you can see that the index files are gone.

**11:45** · What I still do not like is that I still do not have colors for tables or for measures, and in Obsidian I can group.

**11:55** · So, new group, and then you can see you can group by tag, but this has to be a real tag. So, what will you now in Visual Studio Code is we will say, "Please add to all the measure .md file the end of the file hash. You need a hash.

### Wrap-Up: A Standardized, Shareable Catalog

**12:23** · measure.

**12:26** · And then, if he's finished, we should be able to give all the files with this hashtag a color. So, he is telling us that he has 72 measure .md files and that he's now working on them.

**12:44** · So, we will have a look, and you can see him switching to PowerShell now because the bundle is too big for him, which is okay. And then you can see here the measure tag at the end. We will go back to Obsidian. We will click here on group by tag, and then you can already see the whole list of the available tags.

**13:06** · So, we will take the measure, and here you can choose the color. I want to have them green.

**13:13** · And now you can see I have a measure group, which is pretty great because I can immediately see when I have a lot of data in there that the green nodes are the measures.

**13:27** · He forgot some of them. You can also see that. So, we could go back and have a look at the average discount rate.

**13:39** · Open preview.

**13:41** · And you can see that the tag is here, but Obsidian is not showing that, which is in my opinion a bug because it is here.

**13:51** · So, we will see if it's working if we put the tables in because sometimes this is happening. Can you please add to all the table from tag at the end of We will click on We will have a look at the tables. So, on preview, you can see it's still working. And if we check it, I don't see the tag.

**14:22** · So, I will tell him again in this file, "I can't see the tag. Please make sure you have an He didn't copy He didn't copy the right path.

**14:41** · So, copy path.

**14:44** · This is the file where I do not see the tag. We have to reopen the file, and he put the tag here at the end of the maintenance note.

**14:57** · Please make sure to put the tag in a new section.

**15:07** · Because we will never find it here again. So, now you can see it takes tables, and he also did this in the messages. So, now we will go back to Obsidian, add a new group, tag and tables. And here I will go for a blue.

**15:25** · And then you can see that the tables are blue now, and all the measures have turned green now, so there was a little bit of leg in the graph before.

**15:37** · And I really like to use this text because this text helped me so much to find things later again in my knowledge graph. Like I showed you last time, you can click on a node and go to open linked view and open local graph.

**15:55** · Then you can see the local graph, but the bad thing is you can't keep the group, so you have to do the same here.

**16:03** · Tag measures and go back to your green setting, and then you can see here again your measures new group, tag tables, and here we will go to the blue.

**16:18** · And then you can see again your nodes. The interesting thing is that it didn't take effect order as a color, so we will have a look what's going on here.

**16:32** · We will go to the fact tables, the fact order, and we will have a look. And you can see that the tag is here, so it looks like that there you have sometimes some problems with the colors and the colors adapting.

**16:53** · And I still did not find out why it's working sometimes and why it's not working sometimes. And one thing that I want to show you is the plugins, because you can also use plugins in Obsidian, and I also found a capacity LLM VT plugin, so you can also try out that plugin if you want. So, I think this is not so bad at the moment. In the next step, we will extend this for the visuals later.

**17:22** · So, if you want, you can also put in a semantic model overview.

**17:30** · And we will do that now. Please also add a semantic model MD file where you list all the tables and add a link to the single table prompt.

**17:52** · Because then you will also get the note that links to all that tables, and you will know exactly that this is the semantic model in there.

**18:01** · And we will see what he's doing here.

**18:04** · So, here is the semantic model.

**18:08** · And we will also add a tag here. Please also add a tag in the file as tag semantic and a tag section. And here you can see all the tables that are in, so the dimension tables, the fact tables, the metadata, and the helper tables. And here we also have the tag section.

**18:34** · And the next thing we will tell him is to update the items file. Please update the items items.md with all the changes we made to make sure you can remember.

**18:57** · And you can do that from time to time to make sure that all the things you're changing and want him to do are written down there. So, now he has adapted the items.md and we will go back to Obsidian. We will add a new tag.

**19:11** · Tag the semantic model and we will choose this pink for that.

**19:19** · And here you can see the semantic model node. So, later when we have put in more than the tables and the measures, you can start here from this node and then you will know that everything connected here from this side is the semantic model. The blue things are the tables and the green are the measures. So, you will not lose our view so easily.

**19:46** · What you could do now also is you can see we have a business glossary folder, but it is empty.

**19:52** · And we will tell him now, "Can you please create a business glossary .md file with all the measures and a business and their business description from the single .md files and the tables and and all the tables and their

**20:27** · business description. Please sort the tables and the measures into separate sections and sort each section alphabetically, please.

**20:47** · Also, add links to the measures and tables because this glossary is important for users later to get a complete overview what measures are in, what they are doing, and also which tables are used. So, we can open that file and see what he's doing. At the moment, he is listing a lot of things, but the links are not working because I think he made a mistake in the measures and in the tables.

**21:19** · Where is the blanks, please? Recheck the links.

**21:24** · There are spaces in the name and the links are not I already told you last time that maybe you want to introduce a naming convention that there may be no spaces or blanks in file names because this will solve your problem immediately. And you can see he's fixing that now. So, if I click on that later, I will be able to go to the file, which is important. In my opinion, he also added a tag, and you can also see he created an alphabetical order.

**21:57** · And now I also have a business closer. The only thing you need to cross-check now is if he took the right descriptions out of the measure files or if he was reducing them. We will not do that now because I think you can do that on your own, and you have to do that anyway each time when you're creating things. You have to recheck if this is really what you wanted to have, and otherwise you have to advise him how to make it better.

**22:31** · So, I hope I could show you today how you can upgrade your catalog and sort it a little bit better, and also use the LLM Wiki concept and the OKF from Google to standardize it more and to use it across different LLM Wikis or to share it also with your colleagues because if more people are working on the same things, you should really agree on one standard format so that you can exchange files and that everything will look the same. All the agents can work with the wiki.

**23:03** · There.

**23:04** · So, if you like the video, don't forget to leave a thumbs up, and hope to see you soon. Bye-bye.