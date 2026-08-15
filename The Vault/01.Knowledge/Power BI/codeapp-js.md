---
title: "CodeApp JS"
source: "https://share.google/gXnMh2buvRMKi0rM6"
author: "share.google"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Code Apps are my current favourite thing about the Power Platform, they follow what I think... Tagged with powerapps, powerplatform, vibecoding, ai.

CodeApp JS - My Shortcut to Vibe Coding Power Apps - DEV Community Code Apps are my current favourite thing about the Power Platform, they follow what I think Microsoft's AI strategy should have been all along "Automate the code underneath, not the UI", as that's what LLMS are good at. But I found a couple of issues with Code Apps: The CLI requirements is a barrier for some The process is disjointed (e.g. getting connection id from url) Require repo like GitHub (another barrier) React is good for some use cases but overkill for others So I wanted to create a way to fix these issues, I wanted A way for most makers to build without adding connectors To enable Copilot and other Agents to build right first time No CLI commands needed and a simple workflow Store the editable code in the platform Callout, although I dabble in TypeScript I'm stuck in my ways and prefer JavaScript, also I like to build things, so anyone who calls out this probably isn't necessary and the LLM will do all the complex stuff is right So here was my idea, create a fork of code apps built on top of the power app SDK. This project has rattled on for a while, and it all came together when Microsoft launched a NPM version of the power platform cli, allowing me to build in that inside my solution instead of an external dependency. 1. CodeApp JS My plan was to build a conversion process for the SDK into a simple JavaScript (removing the build stage) file that I could then build on top of. The idea was to have these files: power-apps-data.js - the SDK codeapp.js - helper functions, debugger, Dataverse actions, and later date the Flow actions connectors/ - folder with all of the most used connectors converted to JavaScript, they would have easy to use wrappers and built it debugger Index.js* - where all the project JavaScript is Index.html* - where the app UI is power.config.json* - the app config details *These are standard Code App files that are always required The default connectors I thought of that covered 90%+ of use cases where: Dataverse Office 365 Outlook Office 365 User Office 365 Groups SharePoint SQL Teams The next step was to improve how LLMs build Code Apps, as by default they just want to build normal web apps, so I created 2 main areas, agent and skills. The agent.md file is like a system prompt that you can set in VS Code, it ensures the LLM knows that this is a Code App and to do things like use the SDK instead of simple fetch() functions. The skill.md files are for each connector, they ensure the LLM updates the power.config.json file and doesn't make any silly mistakes. They all started from a foundation and were incremented on with learnings from building apps, the more I built the more learnings I could train the LLM with This means that out of the box a maker could build a Code App, but they would need to add schemas for datasources to help the LLM and still used one cli command to publish to the Power Platform. 2. Build Setup At this point I have done 1 and 2, but what about 3 and 4, well this is where I needed to build (my favourite bit 😎). To make the workflow easy I needed to replace the CLI commands, and that meant a new UI. The approach I decided to go with was, in a strange contradiction to my objective, was to build a CLI. There were 3 reasons why I decided First because I could batch/improve the commands and add new ones. Examples include if I wanted to add a new connector I got the command to find the first valid connection and use that (no getting connection id from the url). The second and most important was because the CLI can be the foundation for any UI. So we have the Code App JS files, which are used by the CLI, which is then used by other Apps. That way when I update the files with new connectors or SDK updates it cascades through, and if I update the CLI with new commands (like when the call flow was added), again it cascades down. Third I just really really wanted to make a CLI. 3. CAP CLI The CLI is split into a light and full version. The light covers the CLI commands, the full version builds Copilot SDK into it so it can be a fully standalone agent tool. Light - the CLI commands The CLI commands in theory should make the process more streamlined and simplified, these are the commands I created.  - signs you into Power Platform  - lists all of your environments and lets you select them. After selecting it also updates the power.config.json file  - inputs dataverse table, adds it to the power.config.json and adds the schema to the config file (deletes or unnecessary files too)  - lists all flows for you to select, adds it to the power.config.json and adds the schema to the config file (deletes or unnecessary files too)  - publishes app to environment, it also copies the power.config.json file into the config folder first (you will see why later)  - turns on debugger so in the app you can see and copy all connector actions (great to passing to LLM to help debugging)  - inputs connector, finds first connection id from environment, imports TypeScript code, converts, embeds debugger functionality and moves to the connector folder (deletes or unnecessary files too) there are more shortcuts to these like CAP environment -- but you get the idea That's the standard commands from the Power Platform API, but why stop there, so I've added some of my own  - copies all of the templated CodeApp JS files into your project folder, asks for name etc to setup power.config.json file  - allows you (or the LLM) to create Dataverse tables, you input name, publisher and then add as many columns as you need (any type)  - my favourite, but I need to explain more CAP import is the key to objective 4. See the best thing about Vanilla JavaScript in CodeApp JS is it does not need a build step (convert from TypeScript to JavaScript), so the code in the Code App is the code you have written. This means in theory you can export the solution, unzip it and see the code you wrote (or Copilot did). The one thing mis

## Code / Examples

```
CAP auth
```
```
CAP environment
```
```
CAP dataverse
```
```
CAP flow
```
```
CAP deploy
```
```
CAP deploy --debugger
```
```
CAP connector
```
```
CAP setup
```


---
*Source: [share.google](https://share.google/gXnMh2buvRMKi0rM6)*
