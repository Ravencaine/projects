---
title: "Fully Local Power BI Development: OpenCode + Qwen 3.5 + Microsoft’s Power BI MCP Server"
source: "https://medium.com/microsoft-power-bi/fully-local-power-bi-development-opencode-qwen-3-5-microsofts-power-bi-mcp-server-81a527abe5ab"
author:
  - "[[Michael Hannecke]]"
published: 2026-04-21
created: 2026-08-11
description: "Featured"
Processed: "Unprocessed"
---
Featured

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*C1Dc4jPfkFHDGR7FFIzyqg.jpeg)

Created with Google Nano 2

*Build semantic models with AI assistance while keeping your DAX, your schemas, and your data on your own machine.*

> ***TL;DR:****  
> This guide walks through setting up an AI-assisted Power BI development environment that runs entirely on your own hardware.  
> Ollama serves Qwen 3.5–35B-A3B locally, OpenCode provides the terminal-based agent, and Microsoft’s Power BI Modeling MCP Server exposes your semantic models to the LLM.  
> No cloud APIs, no data leaves your machine, no per-token costs. The one non-obvious gotcha: Ollama defaults to a 4k context window that silently breaks tool calling, so you have to expand it to at least 32k.  
> Hardware-wise, plan for 48GB+ RAM (32GB works but tight).  
> Total setup time: roughly 60 to 90 minutes including the 24GB model download.*

Power BI developers know this tension well: you want AI help with your DAX and model design, but your data is sensitive. Customer lists, financial projections, HR metrics. These aren’t things you want flowing through a cloud API, regardless of how well-written the data processing agreement is.

Microsoft’s Power BI Modeling MCP Server brings AI-assisted model development to Power BI. OpenCode is an open-source terminal-based AI coding agent that works with any MCP server. Ollama runs large language models on your own hardware. Combine the three and you have a capable AI development partner for Power BI work that never touches the cloud.

This is a step-by-step guide to setting up that stack, using **Qwen 3.5–35B-A3B** as the local model. Released in February 2026, Qwen 3.5 is a 36B parameter Mixture-of-Experts model with only 3.3B active parameters per token, a 256K native context window, and strong tool-calling support. That’s a good fit for agentic work against a complex Power BI model.

By the end you’ll have an AI agent that can inspect your semantic models, write DAX measures, refactor relationships, and generate documentation. Every request, every response, every piece of metadata stays local.

> If the model used here does not fir into your RAM — you can use a smaller one, the most steps remain the same — feel free to test.

## Why This Setup Matters

Before the installation steps, here’s what this architecture actually gives you:

- **Complete data locality.**  
	No DAX expressions, no column names, no measure definitions, and no query results ever leave your machine. For organizations handling regulated data (GDPR, HIPAA, BaFin-regulated financial data), this isn’t a nice-to-have. It’s often the only way to use AI assistance at all.
- **No API costs.**  
	Heavy development sessions with cloud APIs can rack up significant bills. Local inference costs you electricity and the upfront hardware investment.
- **Offline capability.**  
	Work on a plane, in a secure facility, or during an internet outage. Your AI assistant doesn’t care.
- **Auditability.**  
	Everything runs as processes on your machine. You can trace every interaction, inspect every log, and prove compliance with data handling policies.
- **Full model control.**  
	You choose which model version runs. No surprise updates, no deprecated endpoints, no vendor policy changes affecting your workflow.

The trade-off is honest. Local models have historically trailed frontier cloud models on the most complex reasoning tasks, though that gap has narrowed dramatically with Qwen 3.5. Independent benchmarks put it on par with GPT-4 class models for coding and tool use, well ahead of where local open-weight models stood even six months ago. For Power BI development work (generating measures, explaining existing DAX, refactoring relationships, writing documentation) it’s competitive with what you’d get from a cloud API.

## The Architecture

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Xr5gJ4cQ3Tc79dycH9hx2w.jpeg)

Made with assistance of a vision model

> Note for Mac + VM setups: in that topology Ollama runs on the Mac host while the other three components run inside the Windows VM. The communication between OpenCode and Ollama crosses the virtual network instead of staying on localhost. See the Mac Setup section below for the networking details.

Four components, all on your machine:

1. **Power BI Desktop**: your normal dev environment, with a PBIX file open
2. **Power BI Modeling MCP Server**: Microsoft’s official server that exposes semantic model operations
3. **OpenCode**: the terminal-based AI agent that orchestrates LLM and MCP tools
4. **Ollama + Qwen 3.5**: the local LLM providing the intelligence

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Prerequisites

### Hardware

Qwen 3.5–35B-A3B uses the Mixture-of-Experts architecture: 36B total parameters but only 3.3B activated per token. This keeps inference surprisingly fast even on modest hardware, but you still need enough memory to hold the full weights.

What I’d recommend:

- **32GB RAM**: works but tight, especially with larger context
- **48GB+ RAM**: comfortable for Q4\_K\_M quantization (24GB model plus context)
- **GPU with 24GB+ VRAM**: ideal for speed, but not required (CPU works)
- **30GB free disk space**: for the model weights plus overhead

On Apple Silicon, the unified memory architecture works particularly well with MoE models. A Mac Studio or MacBook Pro with 64GB unified memory runs this model comfortably alongside Power BI Desktop in a Windows VM.

### Software

- **Windows 10/11** (the Power BI Modeling MCP Server is Windows-only, since Power BI Desktop itself only runs on Windows)
- **Power BI Desktop** (latest version)
- **Node.js 20+** (required for OpenCode)
- **PowerShell** or Windows Terminal

> **Mac users:** Power BI Desktop requires Windows. If you’re on Mac, you need Windows running in Parallels, VMware Fusion, or a dedicated Windows machine. Power BI Desktop, the MCP Server, and OpenCode all run inside that Windows environment. Ollama, however, should run natively on macOS to take full advantage of your Apple Silicon’s unified memory and GPU. See the section “Mac Setup: Reaching the Host’s Ollama from Your VM” below for the networking configuration this requires.

### Step 1: Install Ollama

Head to [ollama.com/download](https://ollama.com/download) and download the Windows installer. Run it. The installer sets up Ollama as a service that auto-starts with Windows and listens on `localhost:11434`.

Verify the installation:

```c
ollama --version
```

You should see a version number. If the command isn’t found, restart your terminal to pick up the updated PATH.

### Step 2: Pull Qwen 3.5–35B-A3B

```c
ollama pull qwen3.5:35b-a3b
```

This downloads approximately 24GB (Q4\_K\_M quantization, the default). Expect 15 to 40 minutes on a decent home connection.

Once complete, verify:

```c
ollama list
```

You should see `qwen3.5:35b-a3b` in the list.

Quick sanity check:

```c
ollama run qwen3.5:35b-a3b "Write a DAX measure for year-over-year sales growth"
```

If you get a coherent DAX response, the model is working. Type `/bye` to exit the interactive session.

A note on model variants: the Ollama library also offers `qwen3.5:35b-a3b-coding-nvfp4` (22GB, optimized for coding) and several other quantizations. The default `qwen3.5:35b-a3b` (Q4\_K\_M) is a solid general-purpose choice for Power BI work. It balances quality and memory footprint well, and supports both text and image input should you want to share screenshots of Power BI reports with the model.

If you prefer the absolute latest, Qwen 3.6 was released in late April 2026, focused on agentic coding stability. You can substitute `qwen3.6:35b-a3b` throughout this guide if you prefer it. The configuration is otherwise identical.

### Step 3: Configure the Context Window (Critical!)

**This is the single most common failure point.** Ollama does not always use a model’s full context capacity. Depending on your Ollama version and hardware, the effective context window can default to as low as 4096 tokens, even when the model supports far more. With a context that small, the model can’t hold the system prompt, tool definitions, conversation history, and your Power BI model metadata simultaneously. Tool calling silently breaks. OpenCode’s own documentation recommends explicitly setting `num_ctx` to at least 16k to 32k for this reason.

Qwen 3.5–35B-A3B supports 256K tokens natively. For most Power BI work, 32K is plenty and uses reasonable memory. If you’re working with very large models that have hundreds of measures, bump this higher.

Create a modified version of the model with a larger context window:

```c
ollama run qwen3.5:35b-a3b
```

At the prompt, run:

```c
/set parameter num_ctx 32768
/save qwen3.5:35b-a3b-32k
/bye
```

This creates a new model reference `qwen3.5:35b-a3b-32k` with the expanded context window. Verify it's there:

```c
ollama list
```

You should now see both `qwen3.5:35b-a3b` and `qwen3.5:35b-a3b-32k`.

**Memory note:** Larger context windows consume more RAM. 32K context on this model adds roughly 4 to 6GB to memory usage. If you’re tight on memory, try 16K first (`num_ctx 16384`). If you're working with unusually large Power BI models and have headroom, 64K or even 128K is viable given the 256K native support.

### Step 4: Install OpenCode

OpenCode installs via npm. In PowerShell:

```c
npm install -g opencode-ai
```

Verify:

```c
opencode --version
```

You should see a version number. If you get a “not recognized” error, restart your terminal.

### Step 5: Configure OpenCode for Ollama

OpenCode uses a JSON config file. The global config lives at `~/.config/opencode/opencode.json` on all platforms. On Windows, that translates to `%USERPROFILE%\.config\opencode\`. Create the directory and file:

```c
mkdir $HOME\.config\opencode -Force
notepad $HOME\.config\opencode\opencode.json
```

Paste this configuration:

```c
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen3.5:35b-a3b-32k": {
          "name": "Qwen 3.5 35B-A3B (32k context)",
          "tools": true
        }
      }
    }
  }
}
```

Key points:

- `**npm: "@ai-sdk/openai-compatible"**`: Ollama exposes an OpenAI-compatible API, so the generic adapter works
- `**baseURL**`: pointing at Ollama's local endpoint
- `**tools: true**`: explicitly declares that the model supports tool calling (essential for MCP to work)

Save and close. Test the configuration:

```c
opencode
```

You should see the OpenCode TUI launch. Run `/models` and confirm "Qwen 3.5 35B-A3B (32k context)" appears in the list. Select it.

Try a quick prompt to verify the model responds. Then exit with `/exit`.

### Step 6: Install the Power BI Modeling MCP Server

Microsoft distributes the server as a VSCode extension, but we want to use it standalone with OpenCode. The trick: VSIX files are just ZIP archives with a different extension.

1. Download the latest VSIX from the Visual Studio Marketplace:
- Go to [aka.ms/powerbi-modeling-mcp-vscode](https://aka.ms/powerbi-modeling-mcp-vscode)
- On the marketplace page, click **Download Extension** in the right sidebar
- Alternatively, grab the direct link from the [GitHub repo](https://github.com/microsoft/powerbi-modeling-mcp)

2\. Rename the downloaded `.vsix` file to `.zip`

3\. Extract the ZIP to a permanent location. I put mine at:

```c
C:\MCPServers\PowerBIModelingMCP\
```

4\. Verify the executable exists:

```c
C:\MCPServers\PowerBIModelingMCP\extension\server\powerbi-modeling-mcp.exe
```

5\. Test that the server starts:

```c
C:\MCPServers\PowerBIModelingMCP\extension\server\powerbi-modeling-mcp.exe --start
```

You should see startup logs indicating the MCP server is listening on stdio. Press `Ctrl+C` to stop it. OpenCode will manage the process lifecycle from here on.

### Step 7: Connect the Power BI MCP Server to OpenCode

Back to the OpenCode config file:

```c
notepad $HOME\.config\opencode\opencode.json
```

Extend the configuration to include the MCP server:

```c
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen3.5:35b-a3b-32k": {
          "name": "Qwen 3.5 35B-A3B (32k context)",
          "tools": true
        }
      }
    }
  },
  "mcp": {
    "powerbi-modeling": {
      "type": "local",
      "command": [
        "C:\\MCPServers\\PowerBIModelingMCP\\extension\\server\\powerbi-modeling-mcp.exe",
        "--start",
        "--readonly"
      ],
      "enabled": true
    }
  },
  "model": "ollama/qwen3.5:35b-a3b-32k"
}
```

Note the safety choice: we’re starting in `--readonly` mode. The MCP server can inspect your semantic model but cannot modify it. Once you're comfortable with how the agent behaves, switch to read/write by removing `--readonly` or replacing it with `--readwrite`.

The `"model"` field sets the default model, so you don't have to select it every time you launch OpenCode.

## Mac Setup: Reaching the Host’s Ollama from Your VM

If you’re running Power BI Desktop and OpenCode inside a Windows VM on a Mac, with Ollama running natively on macOS, you need to solve a networking problem. By default, Ollama only listens on `127.0.0.1:11434`. From your Windows VM, `localhost` points to the VM itself, not your Mac host. So the config above won't connect.

Two things need adjusting.

### 1\. Make Ollama listen on all interfaces

On your Mac (not inside the VM), open a terminal and run:

```c
launchctl setenv OLLAMA_HOST "0.0.0.0"
```

Then restart Ollama. Quit it from the menu bar and reopen, or if you installed via Homebrew:

```c
brew services restart ollama
```

Verify it’s binding correctly:

```c
lsof -i :11434
```

You should see `*:11434` instead of `localhost:11434`.

### 2\. Find your Mac’s IP as seen from the VM

In VMware Fusion with NAT networking (the default), your Mac gets a gateway IP on the virtual network. Inside your Windows VM, open PowerShell:

```c
ipconfig
```

Look for the **Default Gateway** on the VMware network adapter. That’s your Mac’s IP from the VM’s perspective. VMware Fusion typically assigns `.2` for the host in NAT mode, so you'll see something like `192.168.xxx.2`.

Alternatively, on your Mac:

```c
ifconfig vmnet8
```

The `inet` address there is what your VM sees as the host.

## 3\. Update the OpenCode config in your VM

Replace `localhost` with your Mac's IP in the `baseURL`:

```c
"options": {
  "baseURL": "http://192.168.xxx.2:11434/v1"
}
```

Use the actual IP you found in the previous step.

### Firewall check

If you’re running the macOS firewall, make sure Ollama is allowed to accept incoming connections. Go to System Settings > Network > Firewall > Options, and confirm Ollama isn’t being blocked.

### A note on the IP stability

You might wonder whether this IP changes due to DHCP. It doesn’t. The IP your VM sees for the Mac is the **gateway address** of VMware Fusion’s virtual NAT network, not a DHCP lease. VMware Fusion sets that gateway when it creates the virtual network (vmnet8), and it stays fixed. The DHCP server on that network only assigns IPs to guests (your Windows VM), not to the host. So your VM’s own IP can shift between reboots, but that doesn’t matter here since the connection goes *from* the VM *to* the host. The host gateway stays put.

The nice side effect of this split topology: your model inference runs on Apple Silicon with full access to unified memory and the GPU, while Power BI Desktop gets the Windows environment it requires. The network hop between VM and host is negligible in terms of latency for LLM inference, since the bottleneck is always token generation, not the request/response transport.

## Step 8: First Session, Connecting to a Power BI Model

- Open **Power BI Desktop** and load a PBIX file you want to work with. For the first test, use a non-critical file, ideally a sample like the AdventureWorks model.
- In a new terminal window, launch OpenCode in a project directory:
```c
mkdir C:\pbi-work
   cd C:\pbi-work
   opencode
```
- Verify the MCP server loaded. Type `/mcp` in the OpenCode TUI and confirm `powerbi-modeling` is listed as connected.
- Now give it the connection prompt from Microsoft’s docs:
```c
Connect to '[YourPBIXFileName]' in Power BI Desktop
```

Replace `[YourPBIXFileName]` with the filename (without `.pbix`) of the model you have open.

- The first time, the MCP server prompts for approval (this is the MCP Elicitation protocol working as designed). Confirm.
- Try a first query:
```c
List all tables in the connected model and show me which ones have the most measures.
```

Qwen 3.5 will invoke the appropriate MCP tools, query your model, and return results. The DAX queries, the schema, the responses, all stay on your machine.

### Practical Workflows

Prompts that work well for daily Power BI development with this setup:

- **Understanding an unfamiliar model:**
```c
Give me an overview of the model structure: tables, their purposes, 
and the relationships between them.
```
- **DAX generation:**
```c
Create a measure called "Revenue MoM Growth %" that calculates 
month-over-month revenue growth as a percentage. Use the Sales table 
and the existing Date dimension.
```
- **DAX review:**
```c
Look at the "Customer Lifetime Value" measure. Is there a more 
efficient way to write this? What are the performance implications 
of the current approach?
```
- **Documentation:**
```c
Generate markdown documentation for all measures in the Sales table. 
Include the DAX, a business-friendly description, and any dependencies 
on other measures.
```
- **Naming convention audit:**
```c
Analyze the naming conventions across all tables and columns in the 
model. Identify inconsistencies and suggest a cleanup plan.
```
- **Relationship analysis:**
```c
Show me all inactive relationships in the model and explain when 
each one should be activated using USERELATIONSHIP.
```

## Switching to Read/Write Mode

Once you trust the setup, you’ll want write operations. Edit the config:

```c
"command": [
  "C:\\MCPServers\\PowerBIModelingMCP\\extension\\server\\powerbi-modeling-mcp.exe",
  "--start",
  "--readwrite"
]
```

With read/write enabled, the MCP server will prompt you before each modification via the Elicitation protocol. That’s a good thing. It gives you a chance to review changes before they happen.

For experienced use where you want to skip confirmations:

```c
"command": [
  "C:\\MCPServers\\PowerBIModelingMCP\\extension\\server\\powerbi-modeling-mcp.exe",
  "--start",
  "--readwrite",
  "--skipconfirmation"
]
```

**Important:** Always back up your PBIX file before giving write access to any AI agent. Save a copy, then let the agent work on the active file.

## Troubleshooting

### “Tool calls not working” or the agent ignores MCP tools

The #1 cause is context window size. Verify you’re using the expanded model:

```c
opencode
```

Then in the TUI run `/models` and confirm you selected the `-32k` version.

If you’re using the base `qwen3.5:35b-a3b` model, the 4k default context truncates tool definitions and the agent can't see them.

### OpenCode can’t find Ollama

Check that Ollama is running:

```c
curl http://localhost:11434/api/tags
```

You should get a JSON response listing your models. If this fails, Ollama isn’t running. Start it from the Start menu or run `ollama serve` manually.

### MCP server fails to start

Test the executable directly:

```c
C:\MCPServers\PowerBIModelingMCP\extension\server\powerbi-modeling-mcp.exe --start
```

Common issues:

- Path has spaces that weren’t escaped properly in the JSON
- Missing Visual C++ redistributables (install from Microsoft if you get DLL errors)
- Antivirus software quarantining the executable (add an exception)

### “Connection refused” when connecting to Power BI Desktop

The MCP server needs Power BI Desktop to be running with a PBIX file loaded. Without an active instance, there’s nothing to connect to. Open your PBIX file first, then retry the connect command.

### Slow responses

Local inference speed depends on your hardware. What to expect:

- **High-end GPU (RTX 4090, A6000):** 30 to 60 tokens/second, conversational feel
- **Apple Silicon M2/M3 Max/Ultra:** 20 to 40 tokens/second, very usable
- **Modern CPU only:** 3 to 8 tokens/second, functional but you’ll wait

If you’re CPU-only and responses feel too slow, try a smaller model variant first to confirm the setup works, then decide whether to upgrade hardware:

```c
ollama pull qwen3:8b
```

Or for a smaller Qwen 3.5 variant:

```c
ollama pull qwen3.5:9b
```

## Security Considerations

Even with everything local, a few things to keep in mind:

- **MCP command injection risk:**  
	OpenCode’s `mcp.command` array executes arbitrary binaries specified in the config. Never add MCP servers from untrusted sources, and be cautious with project-level `opencode.json` files in repositories you clone. A January 2026 security writeup flagged this; the principle "config files can execute code" applies.
- **Model weight integrity:**  
	Ollama downloads models over HTTPS, but verify the digests if your organization has strict supply chain requirements. The model manifest is available at the Ollama library page.
- **Logging:**  
	OpenCode stores conversation history locally. Check `~/.local/share/opencode/` for what's being persisted if you're handling particularly sensitive data.
- **Network isolation:**  
	For maximum assurance, run the whole stack on a machine with the Power BI Desktop network adapter disabled after authentication. Ollama, OpenCode, and the MCP server only need `localhost` communication.

## What You’ve Built

Here’s what’s now running on your machine:

- A 36-billion parameter language model (3.3B active via MoE) generating code and analyzing your data
- A terminal-based AI agent coordinating tool use and conversation
- An MCP server connected to your live Power BI semantic model
- Everything communicating via `localhost` only

Nothing in transit. No cloud accounts needed. No per-token costs. And for regulated industries, no question about where your customer data goes when you ask an AI to help write a DAX measure.

The quality gap between this local setup and the top cloud models has narrowed faster than most people expected. Qwen 3.5 in early 2026 is already at a level that was frontier-cloud quality six to nine months earlier, and the community is iterating monthly. Qwen 3.6 landed just weeks after 3.5. For most development work, local is increasingly not just a privacy choice but a performance-competitive one.

For Power BI developers working in regulated industries, dealing with sensitive data, or just preferring full control over their tooling, this setup delivers real AI-assisted development without the compromises.

*I write about sovereign AI infrastructure, Apple Silicon inference, and agentic AI security for the DACH enterprise market. Follow me for practitioner-depth technical content, no vendor fluff.*

*This article reflects my professional perspective. AI assistance was used in drafting; insights and final curation are entirely my own.*

[*Sovereign AI Architect*](https://www.linkedin.com/in/michaelhannecke/) *@* [*bluetuple.ai*](https://www.bluetuple.ai/) *| Exploring autonomous AI systems, agentic architectures, and secure AI independence. Writing about what it takes to build AI that stays under your control.*

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----81a527abe5ab---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** AI

**Tags:** Tutorial, AI