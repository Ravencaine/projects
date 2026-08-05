---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, power-query, beginner, load, transform-data]
---

# Load vs Transform Data

After selecting a data source in the Navigator pane, Power BI gives you two choices. The difference matters for almost every real-world dataset.

## Load — Import Immediately

Click **Load** to import the selected data into Power BI immediately, with no transformation.

Use Load when:
- The data is already clean, properly formatted, and ready for analysis
- You want the fastest path from connection to usable data
- You are confident the source data needs no changes

## Transform Data — Open Power Query Editor First

Click **Transform Data** to open Power Query Editor before any data enters the model.

Use Transform Data when:
- The data needs cleaning (fixing types, removing errors, handling blanks)
- The structure needs reshaping (unpivoting, merging columns, changing headers)
- You want to review or adjust what Power BI auto-detected before committing
- You need to combine data from multiple files (Append Queries)

## The Practical Default

**Transform Data is almost always the right first move** even if the data looks clean. Reasons:
- Power Query records every step as a repeatable transformation
- Auto-detected types are often wrong (dates as text, numbers as text)
- Reviewing the data before loading lets you catch issues at the source rather than debug them in the model later
- Applied Steps are reusable — next month's data import uses the same pipeline automatically

The Load button is for when you are certain: source is clean, structure is correct, and you have seen this exact file format before.

## Related

- [[get-data-button-locations]] — how to reach this choice
- [[import-vs-directquery-connection]] — the other decision made at this stage
