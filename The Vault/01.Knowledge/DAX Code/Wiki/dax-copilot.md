---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: concept
tags: [dax, tools, copilot, power-bi, dax-query]
---

# Copilot for DAX Queries

Article - 12/10/2024

Copilot in Power BI can write and explain DAX queries in DAX query view of a Power BI semantic model.

## Requirements

- Fabric Copilot must be enabled
- Power BI Desktop: Enable in Preview features
- Power BI Service: Users need "edit data models" permission in workspace settings

## Using Copilot to Write DAX Queries

1. Choose a published semantic model in a workspace
2. Right-click - Write DAX queries (enable in workspace settings if greyed out)
3. Type a prompt describing the DAX query you want
4. Select Send or press Enter
5. Select Run or F5 to see results
6. Select Keep to save the query

Copilot generates a DAX query, which you can run to see the results and then keep if satisfied.

## What Copilot Can Do

- **Write DAX queries**: Describe what you want and Copilot generates the query
- **Explain DAX queries**: Ask Copilot to explain a DAX query's logic
- **DAX topics help**: Ask about DAX concepts and functions
- **Inspire**: Use the inspire button to get query suggestions

## How Copilot Works

Copilot uses the model metadata (tables, columns, measures) - rich, descriptive metadata yields better results.

Copilot may use MIN/MAX to get sample values in import storage mode, but cannot use other table data.

Copilot may not fully understand complex model relationships or complex DAX patterns.

## Best Practices for Copilot

- Use clear, descriptive table and column names
- Provide context in prompts (e.g., "sum Amount column from Sales table")
- Review generated queries carefully - always verify the logic
- Test with expected results before using in production

## Limitations

- Cannot use full table data (only sample values)
- Complex relationships may not be handled correctly
- DAX query language only - cannot generate measure DAX directly
- Requires specific permissions in Power BI Service

## Example Prompts

```
"Show total sales by product category for 2024"
"Count customers who made a purchase last year but not this year"
"Get the top 10 products by revenue"
"Calculate month-over-month growth for each region"
```

## Related

- [[dax-queries]]
- [[dax-overview]]
