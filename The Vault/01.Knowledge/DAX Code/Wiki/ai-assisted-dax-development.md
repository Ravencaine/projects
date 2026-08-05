---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "ai", "chatgpt", "llm", "bim", "copilot"]
note_type: pattern

---

# AI-assisted DAX Development (BIM Prompting)

Using large language models to generate accurate, context-aware DAX code by feeding them the BIM file.

## Problem with Generic Prompts

Asking ChatGPT for DAX without model context produces generic code that may not work with your specific schema (table names, column names, relationships).

## The BIM Prompting Workflow

1. Export the semantic model's BIM file from Visual Studio or Power BI
2. Paste the relevant table/column definitions into the AI prompt
3. Ask for DAX based on those specific definitions

## Example Prompt Template

```
My semantic model has these tables:
- Sales(SaleID, ProductID, CustomerID, Amount, DateKey)
- Product(ProductID, Category, Margin)
- Dates(DateKey, Year, Month, Quarter)
- Customer(CustomerID, Region, Segment)

Write a DAX measure that calculates the gross margin percentage
by product category, filtering for the selected year.
```

## Example Output

```dax
Gross Margin % :=
VAR __Margin =
    SUMX( 'Sales', 'Sales'[Amount] - 'Sales'[Amount] / ( 1 + [Margin Pct] ) )
VAR __Revenue = SUM( 'Sales'[Amount] )
RETURN
DIVIDE( __Margin, __Revenue )
```

## Notes

- Always verify AI-generated DAX — it may use non-existent functions or wrong table references
- The BIM file provides ground truth for table/column names and relationships
- Combine with [[dax-debugging-with-evaluateandlog-and-tocsv]] for validation

## Related

- [[dax-debugging-with-evaluateandlog-and-tocsv]]
- [[storage-engine-vs-formula-engine-in-dax]]
