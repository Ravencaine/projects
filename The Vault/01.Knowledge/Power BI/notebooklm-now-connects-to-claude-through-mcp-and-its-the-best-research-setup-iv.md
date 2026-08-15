---
title: "NotebookLM now connects to Claude through MCP, and it's the best research setup I've used"
source: "https://share.google/Nr9pA7ns9GIo3v6Uq"
author: "share.google"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> No more tab-hopping.

NotebookLM now connects to Claude through MCP, and it's the best research setup I've used Close Close By Mahnoor Faisal Published Feb 23, 2026, 1:00 PM EST Mahnoor Faisal is a tech journalist covering AI and productivity tools with bylines at XDA , SlashGear , MakeUseOf , Laptop Mag , and Android Police . She's been writing professionally since she was sixteen, and has since penned hundreds of articles. This includes in-depth coverage of AI tools like NotebookLM to breaking news across the AI space. Her passion for technology started when she received her first iPod Touch (4th generation) on her 8th birthday, and she's been deep in the tech world ever since. Currently pursuing a degree in computer science, Mahnoor brings both a journalist's eye and a technical foundation to her coverage of how AI is reshaping the way we work and learn. Sign in to your XDA account Google’s NotebookLM has been my favorite AI tool since the company first released it. Even back when it was just a shiny experiment buried inside Google Labs , I was already going all in. Interestingly, none of the general AI chatbots going viral all over social media excited me. This includes ChatGPT, Microsoft Copilot, Perplexity, and ironically, even Gemini (yes, I know, Gemini was powering NotebookLM under the hood). Fast forward to today, Anthropic’s Claude became the one AI chatbot that finally convinced me just how powerful a “general-purpose model” can be. I canceled all of my other AI subscriptions in favor of it , and I’ve constantly been looking for ways to push it further. My latest experiment has been connecting Claude directly to NotebookLM through MCP, and it’s easily the best research setup I’ve ever used. Why I felt the need to connect Claude to NotebookLM Best of both worlds By now, you’ve probably realized that every AI tool has its own strengths (and weaknesses) — especially if you’ve been testing every AI tool you can get your hands on. As I mentioned above, NotebookLM is an AI tool I’ve been using since its early days. I’ve relied on it to help me study and turn chaotic lecture notes into something I can actually work with from the day I discovered it. If you look at my NotebookLM setup today, you’ll notice I have a bunch of notebooks. I keep dedicated notebooks for every course I’m taking, new hobbies I’m exploring, skills I’m trying to learn, and more. But NotebookLM isn’t the only tool I rely on. My workflow often meant switching between multiple tools: I’d use another tool to find sources, then jump back into NotebookLM to add them, then switch again to research more or get another perspective, and finally return to NotebookLM to generate a Studio output, like an audio overview, mind map, or another structured summary. It was effective, but messy. I was constantly hopping from one tool to another, which got extremely chaotic. There was a time I paired NotebookLM with multiple productivity tools , which meant I was jumping from several different tools to NotebookLM, then back again, just to keep my workflow moving. Now, I’ve singled out Claude as my primary AI tool, which means my workflow has become much more streamlined. Instead of jumping from one external tool to NotebookLM and then to another tool, it’s now a smoother cycle: NotebookLM to Claude, then Claude back to NotebookLM, and back again. But here’s the thing — what if I didn’t need to keep switching at all? That’s exactly what MCP makes possible. Connecting Claude and NotebookLM through MCP is easier than it sounds No coding skills required While this might sound technical and intimidating to set up, the process is really just a series of copy-paste commands in your terminal. It takes less than 10 minutes to get running. Just to give you some context, MCP is an open-source standard for connecting AI applications to external systems. Claude doesn’t natively know how to interact with NotebookLM, and NotebookLM doesn’t know how to talk to Claude. An MCP server bridges that gap, allowing Claude to interact directly with NotebookLM and get results back, all without you manually jumping between the two. First, you need to have the Claude Desktop app installed, as well as uv, a Python package manager that lets you install and run the MCP server. Here’s what you need to run in your terminal if you’re on a Mac:  If you're on Windows, run this on PowerShell:  Then comes the time to actually install the NotebookLM MCP server. While there are many you can install out there, the one I've been using is one created by Jacob Ben-David. You can find it on this GitHub Repository . To install the server, all you need to do is paste the following command in your terminal:  You then need to authenticate the server with Google (a one-time browser login so the MCP can access your NotebookLM). To do so, run the following command on your terminal:  From here, all you really need to do is create a file to let Claude Desktop know the server you just installed even exists. On Mac, paste the command:  On Windows, press Win + R, and paste the command below:  Now, all you need to do is create a new file named "claude_desktop_config.json" and paste the following code into the file:  You can now access all of NotebookLM's features from Claude Everything you need, all in one place Close Once this is set up, you’ll rarely need to open a NotebookLM notebook until you want to access the Studio outputs you’ve generated. Everything else, including querying your sources, creating notebooks, adding new sources, running research, and even triggering the generation of Studio outputs, can all be done directly by Claude. For instance, when I want to generate an Audio Overview about a specific topic, the first step is usually creating a NotebookLM notebook and compiling all the sources I want to populate it with. Typically, this is where I’d explore another tool like Perplexity or Claude to find more high-quality sources and gather additional perspectives on the topic. This is just someth

## Code / Examples

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
```
uv tool install notebooklm-mcp-server
```
```
notebooklm-mcp-auth
```
```
mkdir -p ~/Library/Application\ Support/Claude/ && open -e ~/Library/Application\ Support/Claude/claude_desktop_config.json
```
```
%APPDATA%\Claude
```
```
{"mcpServers": {"notebooklm": {"command": "uvx","args": ["notebooklm-mcp-server"]}}}
```


---
*Source: [share.google](https://share.google/Nr9pA7ns9GIo3v6Uq)*
