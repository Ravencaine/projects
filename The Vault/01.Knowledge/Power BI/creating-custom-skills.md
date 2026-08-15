---
title: "Creating custom skills"
source: "https://claude.com/docs/skills/how-to"
author: "claude.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Learn how to create, structure, and test your own custom skills

Creating custom skills - Claude.ai Documentation Documentation Index Fetch the complete documentation index at: /docs/llms.txt Use this file to discover all available pages before exploring further. Skip to main content Custom skills extend Claude with specialized knowledge and workflows. This guide explains how to create, structure, and test your own skills. Skills can range from simple instruction sets to multi-file packages with executable code. Effective skills: Solve a specific, repeatable task Have clear instructions Claude can follow Include examples when helpful Define when they should be used Focus on one workflow rather than trying to do everything Skills follow the Agent Skills specification — see the specification for more in-depth information. ​ Directory structure A skill is a directory containing at minimum a  file: The directory name must match the  field in your  . ​ Creating a  file The  file must start with YAML frontmatter containing required metadata, followed by markdown instructions. ​ Required fields SKILL.md name : Lowercase letters, numbers, and hyphens only. Maximum 64 characters. Must match the directory name. description : Explains what the skill does and when to use it. Claude uses this to determine when to invoke your skill. Claude.ai limits descriptions to 200 characters . The Agent Skills specification allows up to 1024 characters, but skills uploaded to Claude.ai must use the shorter limit. ​ Markdown body After the frontmatter, write markdown instructions for Claude. Include: Step-by-step procedures Examples of inputs and outputs Templates or formatting requirements Edge cases to handle Keep your main  under 500 lines. Move detailed reference material to separate files. ​ Complete example SKILL.md ​ Adding resources For content too detailed for  , add files to your skill directory:  : Additional documentation Claude can read when needed  : Templates, images, lookup tables, schemas  : Executable code (see below) Reference these files in  so Claude knows when to load them. Keep files focused—smaller files mean less context usage. ​ Adding scripts Skills can include executable code in Python, JavaScript/Node.js, or Bash. Place scripts in the  directory. Claude can install packages from standard repositories (PyPI, npm) when loading skills. Declare dependencies in your frontmatter: SKILL.md ​ Packaging your skill To upload a skill to Claude: Ensure the directory name matches your skill’s  field Create a ZIP file containing the skill directory Correct structure: Incorrect structure: ​ Testing your skill ​ Before uploading Review  for clarity Verify the description accurately reflects when Claude should use the skill Check that all referenced files exist Validate using  ( validation tool ) ​ After uploading Enable the skill in Customize > Skills Try prompts that should trigger it Review Claude’s thinking to confirm it’s loading the skill Iterate on the description if Claude isn’t using it when expected ​ Best practices Keep it focused : Create separate skills for different workflows. Multiple focused skills compose better than one large skill. Write clear descriptions : Be specific about when the skill applies. Include keywords that help Claude identify relevant tasks. Start simple : Begin with markdown instructions before adding scripts. Use examples : Include example inputs and outputs to help Claude understand what success looks like. Test incrementally : Test after each significant change. Leverage composability : Claude can use multiple skills together automatically. ​ Security considerations Don’t hardcode sensitive information (API keys, passwords) Review any downloaded skills before enabling them Use MCP connections for external service access ​ Example skills See github.com/anthropics/skills for example skills you can use as templates. ​ Related topics Skills in Claude Code Create and test skills from the Claude Code CLI, including the  manager. Distribute as a plugin Package your skill for the plugin directory. Was this page helpful? Yes No ⌘ I Assistant Responses are generated using AI and may contain mistakes.

## Code / Examples

```
SKILL.md
```
```
name
```
```
SKILL.md
```
```
SKILL.md
```
```
SKILL.md
```
```
SKILL.md
```
```
SKILL.md
```
```
references/
```


---
*Source: [claude.com](https://claude.com/docs/skills/how-to)*
