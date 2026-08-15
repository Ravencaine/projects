---
created: 2026-08-11
source: How DAX Studio Helped Us Reduce Power BI Report Load Time in Production — Part 1 of 2.md
note_type: pattern
tags: [dax, performance, dax-studio, debugging, workflow]
---

# DAX Studio Performance Debugging Workflow

Step-by-step workflow for diagnosing slow DAX queries using DAX Studio — from copying a query to identifying the bottleneck.

## Prerequisites

- DAX Studio installed ([daxstudio.org](http://daxstudio.org/), free)
- Power BI Desktop open with the slow report, or access to a published semantic model's XMLA endpoint

## Steps

1. **Open Performance Analyzer in Power BI Desktop** — View tab → Performance Analyzer → Start recording
2. **Refresh the slow visual** — click Refresh visuals, identify the slowest card/visual
3. **Copy query** — click **Copy query** on the slow visual to capture the exact DAX query
4. **Connect DAX Studio to the report** — DAX Studio auto-detects the running Power BI Desktop session; or paste the semantic model's XMLA endpoint
5. **Enable diagnostic panels** — click **Server Timings** and **Query Plan** in the Home ribbon before running
6. **Paste and run** — paste the copied query, run it, read the results
7. **Interpret Server Timings** — look for FE time dominating SE time (see [[Server-Timings-Interpretation]])
8. **Scan the Query Plan** — look for repeated operations (see [[Query-Plan-Analysis]])

## Output

Two diagnostic views:

| Panel | Tells you |
|-------|-----------|
| **Server Timings** | How long each SE/FE operation took; SE cache hits |
| **Query Plan** | What steps the engine took; repetition as an anti-pattern fingerprint |

## Variations

- **Live connection / published model:** copy the XMLA endpoint from the semantic model's settings in the Power BI service, paste into DAX Studio's Connect dialog
- **No Performance Analyzer copy-query:** write the query directly in DAX Studio using `EVALUATE` + your measure

## Related

- [[Storage-Engine-vs-Formula-Engine]] — SE vs FE explained
- [[Server-Timings-Interpretation]] — how to read the Server Timings panel
- [[Query-Plan-Analysis]] — how to read the Query Plan panel
- [[Performance-Analyzer-vs-DAX-Studio]] — why Performance Analyzer alone is insufficient
