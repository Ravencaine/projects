---
title: "How to Use Power BI MCP (Model Context Protocol)"
source: "https://databear.com/power-bi-mcp-setup-guide/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-01-03
created: 2026-08-04
description: "Learn to use Power BI MCP to automate your development. Covers setup, VS Code, Desktop connection, natural language, and tips."
Processed: "Unprocessed"
---
Microsoft recently released the official Power BI MCP (Model Context Protocol), an advanced feature that allows developers to use natural language and AI tools to interact with Power BI semantic models. This protocol enables seamless integration between tools like GitHub Copilot and Power BI Desktop, enhancing developer productivity and enabling more intelligent workflows.

In this guide, we’ll cover:

- What the Power BI MCP is
- How to set it up using Visual Studio Code
- How to connect it to Power BI Desktop and the service
- How to modify visuals and measures using natural language
- Key challenges, tips, and best practices

##### What is Power BI MCP?

The Power BI Model Context Protocol (MCP) is a communication layer that allows natural language interfaces like GitHub Copilot Chat to understand and manipulate your Power BI models. With MCP, you can request changes to measures, visuals, and metadata directly from your development environment.

It works with:

- Power BI Desktop
- Power BI Service (workspaces)
- PBIP project files

This feature is currently in preview and subject to change.

##### Why Power BI MCP Matters

MCP allows you to:

- Use natural language prompts to change DAX logic and visuals
- Connect AI tools to your local or online Power BI models
- Automate common development tasks
- Enhance collaboration and consistency across reports

For example, you can say:  
“Modify this measure to display followers instead of likes, using the forest green color palette and a smooth dumbbell chart.”

The system will parse the instruction and modify the visual or underlying logic without needing to write DAX or navigate the interface manually.

##### Getting Started: Setup Instructions

##### Required Tools

You’ll need the following:

- Visual Studio Code
- Power BI Desktop
- GitHub Copilot and GitHub Copilot Chat (extensions)

Free versions of GitHub Copilot are sufficient for most use cases.

##### Step 1: Install Required Extensions in VS Code

1. Open Visual Studio Code
2. Navigate to the Extensions tab
3. Install:
	- Power BI Modeling MCP Server
		- GitHub Copilot
		- GitHub Copilot Chat

This setup enables AI tools to interact with Power BI models locally.

##### Step 2: Configure GitHub Copilot Chat

After installation, enable the chat panel. Switch from the default “Ask” mode to “Agent” mode so that your prompts can modify files instead of simply reading them.

You can choose from various AI models. The free tier supports models like GPT-4.1 or GPT-5 Mini. Agent mode also enables you to customize prompts, define chat instructions, and set context for better accuracy.

##### Connecting to Power BI Desktop

To establish a connection with MCP:

Prompt:  
“Using the Power BI MCP, connect to the open Power BI Desktop file named UDFV3.”

This command connects your current Visual Studio Code session to the open Desktop file. Ensure the Power BI Desktop is running and the file is loaded.

Be cautious with automated actions. MCP will often request approval before executing operations like modifying measures, connecting to models, or running queries. Read the descriptions carefully and only approve actions you understand.

##### Modifying Measures and Visuals with Natural Language

Once connected, you can run prompts like:

“Find the existing measure, change it to represent likes instead of followers, use a thumbs-up icon, apply navy blue and gray colors, and show a line chart for the current year with columns for the previous year.”

MCP will attempt to:

- Locate the measure
- Modify the logic
- Update the associated chart type

##### Key Tip: Add Context for Accuracy

Adding context files (such as screenshots of valid chart types or an instruction file) significantly improves the AI’s understanding and output quality.

For example, if you include a screenshot of all valid SVG microchart types, MCP can reference that image to determine which visual to use, avoiding unsupported chart types.

##### Use Instruction Files

Define instruction files in your project directory to guide the AI. Example:

“When creating SVG measures, use existing user-defined functions from the SVG library. Do not create custom SVG code unless explicitly requested.”

This ensures consistent output and prevents unsupported logic from being introduced.

##### Common Challenges and How to Solve Them

1. **Unclear Prompts**  
	Vague instructions can result in invalid visuals or DAX expressions. Always be explicit.
2. **Model Disconnection**  
	If the AI stops recognizing your model context, reconnect MCP manually.
3. **Unsupported Chart Types**  
	Without context, MCP may invent chart types. Reference supported visuals using screenshots or instructions.
4. **Timeouts or Memory Loss**  
	Sometimes the AI forgets its previous context or loses the connection. Restart the session and reapply context if this happens.

##### Editing Power BI in the Service

While it’s possible to publish your PBIX or PBIP files to the Power BI Service and attempt to connect via MCP, this feature does not yet appear fully supported, especially under free or trial accounts. Connectivity may fail due to workspace or permission issues.

##### Best Practices

- Be specific in your prompts
- Use screenshots or instruction files to provide context
- Review each requested operation before approving
- Avoid testing with sensitive production data
- Enable “Agent” mode for full editing capabilities

##### Real-World Use Cases

MCP can help you:

- Refactor measures and clean up DAX
- Automate translations or apply descriptions
- Use calculation groups or user-defined functions
- Analyze naming conventions
- Benchmark performance across models

Some features like bulk renaming or applying standards are powerful, but should be used with caution.

##### Final Thoughts

The Power BI MCP offers an exciting new way to work with Power BI models. Although it is still in preview and not without flaws, it represents a major step forward in AI-assisted development for data professionals.

Context is still critical. AI tools need clear, detailed instructions to perform as expected. But with the right setup, the ability to use natural language to interact with your data model can save time, reduce manual errors, and improve efficiency.

[To get started, visit:](https://databear.com/power-bi-training/)