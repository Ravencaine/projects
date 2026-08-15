---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: workflow
tags: [dax, udf, power-bi, tmdl, xmla, semantic-link-labs, ssms, devops]
---

# DAX UDF Development Environment Options

Five entry points for building, testing, and deploying DAX UDFs. None are interchangeable — each suits a different workflow.

## 1. DAX Query View

- **Best for:** interactive testing during development
- **How:** Right-click a function → "Quick Queries" → "Define and evaluate"
- Write DEFINE block, EVALUATE expression, run against live model
- Instant feedback loop

## 2. TMDL View

- **Best for:** code-first editing and Git version control
- **How:** Switch to TMDL in Power BI Desktop; functions live in `functions.tmdl`
- Check `functions.tmdl` into Git alongside the model definition
- One source of truth for CI/CD pipelines

## 3. Model Explorer

- **Best for:** ad-hoc creation and quick edits through the formula bar
- **How:** Open Model Explorer → Functions node → Create or edit
- Functions appear under the Functions node in the model tree
- Good for exploratory work, less good for bulk operations

## 4. XMLA Endpoint / SSMS 22.5+

- **Best for:** programmatic or DevOps-style deployment
- **How:** Connect to the workspace's XMLA endpoint via SSMS; deploy TMDL or execute DAX script
- Enables CI/CD pipelines: check `functions.tmdl` into source control, deploy via script
- Supports deployment to production without manual steps

## 5. Semantic Link Labs (Fabric Notebooks)

- **Best for:** scripting entire library deployment in one notebook cell
- **How:** Use `sempy.links.tom.connect_semantic_model` + `set_user_defined_function` to push all UDFs at once
- Enables: rebuild a demo model from scratch in seconds by running all UDF definitions from a notebook
- Only available in Microsoft Fabric (not standalone Power BI Desktop)

## Quick Selection Guide

| Scenario | Entry Point |
|---------|------------|
| Interactive learning / testing | DAX Query View |
| Git-versioned library | TMDL View |
| Ad-hoc function creation | Model Explorer |
| CI/CD / DevOps deployment | XMLA / SSMS |
| Fabric notebook automation | Semantic Link Labs |

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[Measure-Library-to-UDF-Migration]] — deployment strategy
