---
created: 2026-07-30
updated: 2026-08-02
source: "dax4humans_ch16_bim_ai.txt"
note_type: workflow
tags: [ai, chatbot, bim-file, codegen, power-bi]
---

# Generate DAX with AI Using a BIM File

A workflow for using AI chatbots (ChatGPT, Copilot, etc.) to generate accurate, model-aware DAX measures by providing the semantic model's BIM file as context.

## Prerequisites

- Power BI Desktop (or Tabular Editor for `.bim` export)
- AI chatbot with file upload support (e.g. ChatGPT 4o)
- Tabular Editor 2.x (optional, for cleaner `.bim` export)

## Steps

### 1. Export the Semantic Model as a BIM File

**Option A — Power BI Desktop (preview feature):**
1. File → Options and settings → Options
2. Under Preview features, check **Power BI Project (.pbip) save option**
3. File → Save As → save as `.pbip`
4. The `.SemanticModel/model.bim` file is created

**Option B — Tabular Editor 2.x (recommended, cleaner output):**
1. Open Power BI Desktop and launch Tabular Editor from the External Tools ribbon tab
2. File → Save As → save as `model.bim`

> Patron tip (Alexis Olson): BIM files can be bloated. Run this cleanup script before uploading: https://gist.github.com/AlexisOlson/8cff91128d02d0b1857a93101309eb7b — can reduce file size by up to 80%.

### 2. Upload the BIM File to the Chatbot

In ChatGPT 4o: use the **+ → Upload from computer** button to attach the `.bim` file.

### 3. Prompt the Chatbot with Model Context

Include in the prompt:
- The visual layout (x-axis, y-axis, legend columns)
- The business logic required
- Request a No CALCULATE version if desired

Example prompt:
```
The attached BIM file describes a Power BI semantic model.
For a visual with DateTimeTable[Date] on the x-axis and
Dim_Department[Responsible Department] as the legend, create
a measure for the y-axis that counts transactions from
Tracking_History where Start Date <= x-axis time AND End Date > x-axis time.
Please provide a version that does NOT use CALCULATE.
```

### 4. Review and Refine

The chatbot's first response may not be perfect. Follow up:
- "That measure is not correct. The logic needs [specific correction]."
- "Can you create a version without CALCULATE?"

### 5. Paste into Power BI

Copy the generated measure code and paste directly into Power BI Desktop. Test against the actual semantic model.

## Why the BIM File Works

Without the BIM file, AI chatbots generate generic DAX that must be manually adapted to the specific model. The BIM file provides:
- Table and column names
- Relationship structure
- Data types and cardinality

This context allows the AI to generate measures that work correctly on the first attempt.

## Notes

- The No CALCULATE approach is especially well-suited to AI generation — it's more readable and the AI follows it more reliably.
- Chatbots that only support text can receive the BIM content via copy-paste.
- Test the AI-generated measure carefully — AI is accurate when given proper context but can still misunderstand complex business logic.
- The BIM file is a JSON-formatted `.bim` file describing the Tabular model — completely text-readable and safe to share.

## Related

- [[calcuate-the-calculate-counterculture]] — the No CALCULATE philosophy
- [[dax-optimization-tools-reference]] — verify AI-generated code with DAX Studio
