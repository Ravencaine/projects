---
title: "Exploring the Power BI Remote MCP Server with Claude"
source: "https://medium.com/microsoft-power-bi/exploring-the-powerbi-remote-mcp-server-with-claude-f5fec92f0612"
author:
  - "[[Peter Beck]]"
published: 2026-02-17
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
**Connecting Claude to Power BI with the Model Context Protocol**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*H9TNO-YXhLIZAlgmKhF48Q.png)

PowerBI and Claude, together at last

The idea behind Model Context Protocol (MCP) is simple but powerful: give LLMs a standardized way to connect to external data sources and tools. I’d already played around with a [Snowflake MCP server](https://medium.com/snowflake/model-context-protocol-claude-and-snowflake-9f1e37775d80) through Claude Desktop, and the experience of just *\*asking questions\** about your data in plain English is really compelling. Recently someone suggest I take a look at the “remote” [Power BI MCP server](https://learn.microsoft.com/en-us/power-bi/developer/mcp/remote-mcp-server-get-started), which has been in preview since November last year. I have to say I was really impressed with this tool.

Microsoft has a bare-bones intro to the server [here](https://learn.microsoft.com/en-us/power-bi/developer/mcp/remote-mcp-server-get-started). Basically, with very little effort, you can get natural language queries running against your Power BI data using the Github Chat interface in VSCode. I recommend you take a quick look to get the feel of what the server does.

The Microsoft demo is a nice intro into how the server behaves, but once I went through it I decided I wanted to build something that would let me have a genuine conversation with my Power BI datasets outside VSCode — and not just a one-shot query, but a back-and-forth where my client could call tools, inspect results, decide it needs more information, and keep going until it has a proper answer. I wanted to use Claude (in this case, Claude Sonnet 4.5) as my LLM because… well, because I’m sending money to Anthropic every month. In reality any reasonably performant LLM will work.

Here’s a sample of the kind of output Claude can generate using this server:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PCCJoONHHEqFjN8xNRuEjQ.png)

LLM Output Analyzing PowerBI Data

## What This Thing Actually Does

What I ended up with — with lots of help from Claude Code — is a chat interface ([available as both a CLI and a browser-based Streamlit app](https://github.com/peterjohnbeck/Connecting_PowerBI_MCP)) where you type a question in plain English and the LLM figures out what Power BI data it needs, generates the appropriate queries, fetches it via MCP, analyses the results, and gives you an “intelligent” answer. In the Streamlit version it will even generate charts using Altair.

Ask something like *\*What were the total sales in Q3 of 2025?\** …

![](https://miro.medium.com/v2/resize:fit:1118/format:webp/1*EsjV7YqPZaVP4WMOj5k-Yg.png)

Natural language query of my PowerBI data

… and Claude will

- discover the available Power BI tools
- execute the right DAX query or queries
- get the results back
- and **render analysis** like this:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*XeCTJ0kZ-lfIDfJK2_iWvA.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*FUUGdHDKrKvZKfsPdSTilw.png)

Natural-language query results

… all without you writing a single line of DAX!

The key word there is “discovers.” Claude doesn’t have a hardcoded list of queries it can run. At startup, the app connects to the Power BI MCP server, asks it what tools are available, and converts those into Claude’s tool format. Claude then decides which tool or tools to call based on your question, evaluates the result, and then makes additional calls as required.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DE39M-LwrEC2ycSu5sweTg.png)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## The Agentic Loop

This was the part that was most interesting. The orchestrator doesn’t just send your question to Claude and return the response. It runs a loop:

1\. Send your message (plus conversation history) to Claude, along with the available Power BI tools

2\. Claude responds — either with a final answer, or with a request to call one or more tools

3\. If Claude wants to call tools, execute them against Power BI via MCP

4\. Feed the tool results back to Claude

5\. Repeat until Claude decides it has enough information to give you a final answer

This means Claude can chain multiple queries together. It might:

- Look at the schema of the semantic model first
- Then query a specific table
- Then ask a follow-up to if required and go through the loop again

The loop is bounded (max\_iterations) so it won’t run forever, but in practice most questions resolve in one to five tool calls.

```c
for iteration in range(max_iterations):
    response = await claude_client.send_message(messages, tools)

    if response.stop_reason == "end_turn":
        break  # Claude has its answer
    elif response.stop_reason == "tool_use":
        tool_results = await execute_tools(response.tool_calls)
        messages.extend(tool_results)
        # Loop continues — Claude sees the results and decides next steps
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Gy6lQWKSEzapwdtbGpk41w.png)

Iterating through tool usage

## The MCP Connection Challenge

Most MCP servers use Server-Sent Events (SSE) for communication — that was the standard transport in the original MCP spec (now replaced with Streamable HTTP). The Power BI MCP server seems to use HTTP POST with JSON-RPC instead, so I couldn’t just use the standard MCP SDK client out of the box.

I ended up with a custom \`SimpleMCPClient\` with its own \`HTTPTransport\` layer. It handles the JSON-RPC request/response pattern, manages request IDs, and injects the Azure authentication token into every call. It’s not a lot of code, but it was the kind of thing where you spend an afternoon wondering why nothing works before you realize the transport layer is just different. Documentation on this product is pretty thin and it took a lot of trial-and-error.

## Authentication

For authentication the app uses Microsoft’s MSAL library with the device code flow. On first run, you get a URL and a code to punch into your browser. After that, the token gets cached locally and auto-refreshes. It’s the same flow you’d use for any Azure-authenticated CLI tool, and it means you don’t need to store passwords or manage service principals for development use. The app is also registered with Azure and given access to PowerBI.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ITmUXkD3Q1FbyuA-dTCYZQ.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*SOQCIRD5dtESPhDzq1JRUg.png)

Authentication and the connected server

## The Streamlit UI

I wanted a nice chat experience, not just a terminal. Streamlit was the obvious choice for a quick, interactive UI…

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ym_FX0YotNADDWM8C8JvlQ.png)

Streamlit Interface

… but it introduced its own set of challenges.

The big one: Streamlit reruns your entire script on every interaction. That’s fine for simple apps, but when you have persistent async connections to external services, it’s can be problem. A client created in one script run can’t be used in the next because the event loop is gone.

The solution was an \`AsyncRunner\` class that maintains a single persistent daemon thread with its own event loop. All async operations — MCP calls, Claude API requests — get submitted to this one loop via \`asyncio.run\_coroutine\_threadsafe\`. The loop survives across Streamlit reruns, so connections stay alive.

## Automatic Chart Detection

One of the things that makes the experience feel polished is automatic chart rendering. When Claude returns tool results that contain tabular data, the app analyzes the data and decides whether a chart would be useful — and if so, what type.

The logic is straightforward: if there’s one row, show a metric card. If there’s a datetime column, use a line chart. If percentages sum to roughly 100, use a pie chart. Otherwise, default to a bar chart. The user can also hint at what they want — include “pie chart” in your question and it’ll override the auto-detection.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*M4hYybZfitGWiJcCIPtLsg.png)

Explicitly requesting the Pie Chart for data

The charts are rendered with Altair, which gives you interactive Vega-Lite visualizations that look good out of the box.

## The Stack

For anyone who wants to dig in or build something similar:

**LLM**: Claude via the Anthropic API (Sonnet 4.5 by default, but configurable in the.env, with full tool use support)

**Protocol**: Model Context Protocol over HTTP POST

**Auth**: MSAL device code flow with local token caching

**Web UI**: Streamlit with a persistent async event loop

**CLI**: prompt-toolkit REPL with Rich formatting

**Charts**: Altair (declarative, Vega-Lite based)

**Config**: Pydantic settings with \`.env\` file support

## What I Learned

1 — The MCP ecosystem is still young, and the implementations vary. Don’t assume every MCP server follows the spec to the letter — the Power BI server’s transport caught me off guard. Getting Claude Code to help build my own transport layer wasn’t hard, but it took a while to figure out what was wrong.

2 — Streamlit and async Python are not natural friends. If you’re building anything with persistent connections in Streamlit, plan for the rerun behavior from the start. The persistent event loop pattern I landed on works well, but it took a few rounds of “why is my connection dead?” to get there.

3 — The agentic loop pattern — letting Claude decide when it has enough information — is very powerful. Most questions are simple enough that one or two tool calls handle it. But occasionally Claude will chain together three or more calls, exploring the data in a way that at least “feels” genuinely intelligent. That’s when this approach really shines compared to a traditional dashboard.

This started as a weekend experiment to see how the remote PowerBI MCP server worked. Then I wondered if I could get Claude talking to Power BI through MCP. It turned into something I can actually see myself building out for day-to-day use for both quick data exploration and more detailed analysis.

As an example, I asked Claude to “Create a strategic analysis of the customer with the most sales” in my toy data set, and in about 90 seconds it returned a very robust examination of the top customer several pages long, including an an analysis of their sales profile, their purchasing patterns, and recommendation on how to engage with them going forward. Here is a section of the analysis:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*1yqlVDWn925xqldqv1WhCg.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*xH7Gv12Eym7nijQ263IWxQ.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*i_ZzalLUnZN3qRNnsWnprA.png)

Section of Strategic Analysis Report

The combination of natural language, an agentic loop, and automatic visualization means I can go from question to insight without context-switching in Power BI Desktop or writing DAX.

The code is on a [public repo here](https://github.com/peterjohnbeck/Connecting_PowerBI_MCP) — feel free to take a look, fork it, and tell me all the things I’m doing wrong!

***I hope you have found this useful — follow me here on Medium for more data-related content, and connect with me on*** [***linkedin***](https://www.linkedin.com/in/peter-beck-cbip-7609063/)***!***

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** AI

**Tags:** Tutorial, AI, MCP