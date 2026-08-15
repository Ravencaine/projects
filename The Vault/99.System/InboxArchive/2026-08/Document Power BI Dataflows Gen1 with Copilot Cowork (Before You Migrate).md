---
title: "Document Power BI Dataflows Gen1 with Copilot Cowork (Before You Migrate)"
source: "https://www.youtube.com/watch?v=MfENXZxHoN4&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
video_url: "https://www.youtube.com/watch?v=MfENXZxHoN4&utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
creator: "[[Power BI with AI Vibes - Jasmin Simader]]"
published: 2026-07-06
created: 2026-08-08
description: "Still using **Power BI Dataflows Gen1**? Although Dataflows Generation One are now considered legacy, many organizations continue to rely on them. Before migrating to **Dataflows Gen2** or another sol"
language: "en"
processed: "Unprocessed"
---
![](https://www.youtube.com/watch?v=MfENXZxHoN4)

Still using \*\*Power BI Dataflows Gen1\*\*? Although Dataflows Generation One are now considered legacy, many organizations continue to rely on them. Before migrating to \*\*Dataflows Gen2\*\* or another solution, creating complete technical documentation can save hours of work and make the migration process much smoother.  
  
In this tutorial, I'll show you how to use \*\*Microsoft Copilot CoWork\*\* to automatically generate professional documentation for your \*\*Power BI Dataflows Gen1\*\*. You'll learn how to export the \*\*export.json\*\* file from Power BI Service, use \*\*Microsoft Copilot\*\* to create a documentation template, and build a reusable \*\*CoWork Skill\*\* that can generate the same high-quality documentation for future dataflows with just a few clicks.  
  
Instead of documenting every table, column, data type, relationship, and \*\*Power Query\*\* transformation manually, you'll let AI do the repetitive work while keeping you in control of the final result.  
  
In this video you'll learn:  
• Why documenting Power BI Dataflows Gen1 is important before migration  
• How to export the \*\*export.json\*\* file from Power BI Service  
• How to generate documentation with Microsoft Copilot  
• How to create a reusable CoWork Skill  
• How to use reference documents for consistent output  
• How CoWork validates the generated documentation  
• How much Copilot CoWork costs  
• Best practices for testing and improving your AI skills  
  
  
Files can be found in my GitHub: https://github.com/Jasmin319/powerbi-copilot-usecases/tree/38f93621a7475eee6f6e335fdf508ed157be10b3/Document%20Data%20Flow%20Gen%201%20Cowork  
  
\*\*Chapters\*\*  
  
00:00 Why Document Power BI Dataflows Gen1?  
00:45 Exporting the Dataflow JSON File  
02:15 What's Inside export.json?  
03:33 Creating Documentation with Microsoft Copilot  
05:18 Reviewing the Generated Word Document  
07:06 Building a Copilot CoWork Skill  
09:42 Adding Reference Files and Instructions  
12:14 Understanding the Generated Skill  
14:58 Skill Guardrails and Best Practices  
16:34 How Much Does Copilot CoWork Cost?  
17:43 Testing the Documentation Skill  
19:45 Where Copilot CoWork Stores Your Skills  
21:12 Validating the Generated Documentation  
23:36 Final Result and Quality Check  
24:45 Using This Workflow for Any Documentation Project  
25:38 Final Thoughts  
  
If you're working with \*\*Power BI\*\*, \*\*Microsoft Fabric\*\*, \*\*Power Query\*\*, \*\*Power BI Dataflows\*\*, or planning a migration from \*\*Dataflows Gen1\*\* to \*\*Dataflows Gen2\*\*, this workflow can help you automate one of the most time-consuming documentation tasks.  
  
If you found this video helpful, please like the video, subscribe to the channel, and let me know in the comments how you're currently documenting your Power BI solutions.  
  
#PowerBI #MicrosoftFabric #Dataflows #DataflowsGen1 #DataflowsGen2 #Copilot #MicrosoftCopilot #CoWork #PowerQuery #BusinessIntelligence #PowerBIDocumentation #AI #DataEngineering

## Transcript

### Why Document Power BI Dataflows Gen1?

**0:00** · So we will click on the file and find out what it looks like. And you see that it really looks like the file we wanted to have. So welcome back and today I will show you how you can document your data flows generation one. I think you may have heard about data flows generation one being legacy which means at the moment there are no new features developed for them but you can still use them till some point in the future which has not been announced.

**0:30** · So there is no need for panic but maybe you want to document your data flows at the moment that you can make sure then to transform them to data flows generation 2 or something else and to have a full documentation about them when doing that. For documentation, we will use Kovac because I think this is pretty good because the skills are a pretty good feature to do that and I will show you what you need to get all the informations to create skill that will do that for you in future in co.

### Exporting the Dataflow JSON File

**1:02** · So here we are in PowerBI service and in PowerBI service you can see that I have here a data flow generation one. In this data flow there are several tables. The tables are not very complicated data sources. They are just referring to some CSV files. But the process will be the same also for more complex data sources because all the informations will be stored in your export JSON file. So we can close that.

**1:34** · And then we go to the three dots next to the data flow generation one. And if you click on that you see the option export.json. JSON.

**1:45** · You can click that and then you can export the adventure works row data from the data flow. And if we open that file, you will see here a lot of information about all your tables and all your columns. And you will also see that here is the lead from the power query code.

**2:06** · So you will also get some informations about the transformations you did. So you will have information about the source tables and the target tables and all the column names and the data types and so on and so forth. So I think this is really a pretty good file to start for the documentation.

### What's Inside export.json?

**2:26** · What I did then I was importing all of that into a word file.

**2:34** · So I was opening up word opening the document using copilot and telling copilot by adding the file please generate a full documentation of all the tables in the data flow. I want to have for each table a table

**2:58** · section that includes all the information about the source table names. the granularity of the entries and the short business description.

**3:25** · I also want for each table a tabular section with all the columns in the table including the data types and also a short business description or then you can run them and copilot will come back with a proposal and create start creating this documentation.

### Creating Documentation with Microsoft Copilot

**3:56** · So I usually do that and start with that. And you can see here the data flow name, the description, the version, the output format. It was modified on the 20th of June. And there are 11 tables in it. And then you can see that Copilot is starting to do documentation and that he's also doing things that I do not like.

**4:22** · Like this what he's doing with the columns, but I can correct that afterwards and telling that you should make sure that all the widths are aligning and that they do fit the text and that it is not looking so strange.

**4:45** · And here is a document that I created by doing so. And this is the end document I created. So you can see here now that I have a table of content that I have an overview what I'm documenting.

**5:01** · I have in here the source system. So the source system, the server, the database, the schema, um the source objects, the data bias is not applicable as there isn't one and the schema also not. If we scroll down here you will see the table catalog. So there is a classification of the table. These are sales transactions order year 2022 description is not excluded in export. There's a query ID that's a fake table.

### Reviewing the Generated Word Document

**5:29** · The load enabled is on and the source system is my shareepoint and there is a source object adventure work sales data 2022.

**5:42** · The granularity is assumed because there was no information. So I have to check that. Here are information about the primary key, the foreign key and the business purpose of this table. Also information what it can be used for and if there are any special logics in the table I have created while transforming it. And then there are usage nodes like the territory key links to the sales territory key and adventure territory lookup.

**6:14** · And there is also information about the refresh. Then there is information about the technical structure. There's the order date, the stock date, the order number, the product key and also the linked data types. So I know now exactly how my output should look like and I know exactly how my input should look like.

**6:37** · And this is pretty great because now I can go to co-pilot co-work and in co-work I can go now to customize under customize you can see skills you have created and you can see I have here multiple skills already. This is the data flow documentation skill and you can have 50 skills in total. So we will click on add and create new.

### Building a Copilot CoWork Skill

**7:07** · And then you can see that Kobe is starting the process where he's guiding us through the skill creation.

**7:18** · And let's see what he's coming up with.

**7:20** · First thing he needs to know is what should the skill actually do for you.

**7:25** · Everything else the name, description, category, and instructions flows from that. And we want to have a document and a table. You can also say writing drafting but I think we want to have a document template because we want to have a document in a very specific structure. So we can click on document template. You could also add an own description and then you can click on submit. And then he is asking us what kind of task do you want this new skill to handle.

**7:56** · And then he's asking us what structured document or template should this skill produce. Pick one or describe your own if you choose. And we will pick our own word documents in a specific format that contains all the technations about the data flow generation one.

**8:28** · And now I think he will get back to us with additional questions. But we will take a shortcut and I will add here some files.

**8:39** · So I will add here the JSON file we have exported and the word document we already knew we want to have as a final documentation.

**8:51** · And I will tell him the scale should transform The information in the JSON file always in a word document that matches exactly exactly the structure in the attached document.

**9:17** · And the great thing in co-work is you can send him this although he is still working on the previous one and thinking because he will cue it and then he will just take it when he's ready. And you also can see

**9:36** · that before he was checking how many skills I already have and if the name is valid because if I would have an existing data flow with the name he would have to choose another name or he would ask me why do you want to create the same again and he's telling me I have three or 50 skills. So the maximum you can have for 50 skills and now he will draft the skill and you can still see him thinking about what we told him here and you can also see that he put the documents we delivered into the references.

### Adding Reference Files and Instructions

**10:08** · So here is the word file and here is the JSON file in the reference and then he is saying me this is a crucial clarification. The skill isn't a generic template. It should take a JSON file like your adventure work data and always turn it into a virtual command that exactly matches the structure of your reference dock. That's a much more precise skill and then can anchor it to your actual reference to command.

**10:33** · So you can see that you can click through in the beginning but I think you will be faster if you already know very specific what to do if you just type it in and attach the files you need. And now you can see that is inspecting the files and working on that and is telling us now I have now the complete structure. Let me find the reference documented to skill and write a precise structured specification.

**11:03** · Then we build the skill MD around this proposal. First one quick check on the JSON column definition so the spec is accurate. And you do already see this take sometimes. You can also do some other things in between and let him work on that and come back then. But you will see with the results. It's really worth investing the time and I will show you also later the costs for this task because co-work tasks have to be paid.

**11:32** · So it's a pay as you go and uncork created is one US cent. So you can easily find out how much this task will cost you in the end and by doing such things you have to find out in the end how much effort would you have needed is the document and the result really adding business value and if yes then

**11:58** · you can compare the cost and if co-work is much more efficient than you would be co-work would be the way to go and I think especially for so specific specific documents where you have a really really precise result you're expecting, co-work is really worth a shot because of course you can also use copilot for that. But I think when the document is specified so precise, co-work is doing the better job.

### Understanding the Generated Skill

**12:28** · And you can already see here that the skill MD document is created that the skill quality report is created. And you can also have a look at the skill quality report. You can say that it's 96 out of 100 meets the board publish. The risk is medium and the crowning is passed. So it switches on the right time. It knows what to do. It steps in its lane and it handles surprises safely.

**12:59** · The skill is in a great shape. And you could also click on the technical details. And you can also see that the score is 96 out of 100. The publish bar is 70. So skills under 70 shouldn't be published. And you can see also here the single scores for these four criterias again. Then we can close that. And we can also have a look at the skill MD file. So the skill MD file is containing a name. It's the data flow doc description.

**13:30** · And here's also a description what this skill is doing.

**13:36** · And then you can see here again takes a PowerBI data flow JSON export and produces a word. Then you have an overview when to use a when not to use and you have also a quick start. There are some core instructions so you can read through that. And there are also some guardrails. And guardrails are pretty much important for skills because they make sure that the skill is really doing what you want. So match the reference structure exactly. So no other structure. Never fabricate fact.

**14:07** · So he should never make something up. So retrieve before asking. Locate and pass the JSON yourself. Ask the user only if no data flow. JSON can be found. So maybe we want to change that in the skill to ask the user each time for the JSON file and fail honestly if the JSON can't be read say so and ask for reattach do not produce a document from placeholder or same data and confirm the file exists in output before announcing completion.

**14:38** · So he should not make up any failed success. He should just report the truth. And the next thing we will test is how much did it cost us. So you can use slash cost.

**14:55** · Then you see that this is also a built-in scale that Microsoft is building in. And then you can run that.

### Skill Guardrails and Best Practices

**15:02** · And you can see right up to now the task only costed us 341 credits. So this is around €3 US or €3, which is not much in my opinion because I can reuse this skill every time. And now we will let him test the skill. So because he was asking us the next best step is a real world test. Want me to run it now on your adventure Jason and generate the actual virtual command?

**15:32** · That's the shest way to confirm it. And we will say yes.

**15:37** · And now you can see him thinking again.

**15:40** · and he should create the document for us and test the skill on that and you can still follow up here what's happening.

**15:50** · So he is extracting all the data and building the right document and then he is trying to verify the document but he's still working on that. As you can see there are no check marks here and also here he's still thinking. What would also worth a shot here is testing with another export file because it's very easy to create the same exact output again from the \[clears throat\] file the skill was created for.

**16:19** · So I really recommend you to test the skill also on another export from a data flow to make sure that the skill is working each time. As I only have this one here, I won't do that. And in the time he's working, I will also show you where you can find your skills. So you can go to the one drive to your files to documents and then you have a cowork folder. I have two and you can see here are three items. So I will go to cowork one.

### How Much Does Copilot CoWork Cost?

**16:50** · I don't know why he created a separate one. Then you can go to skills and in the skills you can find your different skills. You can go to the data flow document and here you can find the skill MD file. We had a look at that before.

**17:07** · You can see the quality report. We also had a look at that before. And here you can also find a folder with the reference files. So you can also import skills in there that you have created for claude or for another AI tool. But you have to check them and make sure that they work well with copilot. So you can see now I have completed reference content and I've verified the JSON is the same underlying data by crosschecking every datadriven field metadata.

**17:36** · So we back met data my big data love all 11 query ideas every column and type against the JSON and update the export file to your current file name. But you really see that creating skills and testing them takes some time. But like said before, I think especially for documentation, co-work is really worth a shot.

### Testing the Documentation Skill

**18:02** · And now you can see he's checking every page against my reference, which is also great because then it really makes sure that it looks like that. Then you can see the validating at the moment failed. So he has to work on better on it. But I think this is a really great hint because you see that it's checking itself and not just producing anything that's not working in the end which is also a big advantage against copilot because copilot could not do that so well before

**18:34** · and if I did the same within copilot agent I often had to say oh you forgot this and you forgot that can you please do it like that but when creating the skills I see that they really get usually on the first try when running the skill what I really need and this saves me so much time at the moment and documentation because all this back and forth is no more needed. I just have to wait until co-work is finished. And now you can see that the document is built, validated, and passed every check.

**19:04** · And let me confirm delivery and take a quick look at the pages myself. And in the end, it says it works. The date the flow skill reduced the word document from the adventure works. And it matches your re structure. And he is also telling me the document is ready. And he saved it. So, we will click on the file and find out what it looks like. And you see that it really looks like the file we wanted to have.

**19:32** · Like I said before, it would be pretty good testing with another export um to really make sure that the skill is working. And then you can click on more actions. You can share the file. You can download it. You can open it in word.

### Where Copilot CoWork Stores Your Skills

**19:46** · And you can also open the location where the file is saved. And you see it is saved in one drive in the output file.

**19:58** · So I really hope you enjoyed the video and I could show you how easy it is now with co-work to create documentation over and over again you need for PowerBI by just using some JSON files. And you can also take the process I've shown you and transfer it to other problems you have regarding documentation. You just need a sample for the input and a sample for the output.

**20:21** · And you can see the co-work will do the steps between and connect dots and create a scale that will do the documentation for you. So I wish you a great day now.

**20:34** · Hope to see you soon. Bye-bye.