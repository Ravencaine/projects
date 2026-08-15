---
created: 2026-08-10
updated: 2026-08-10
source: Automate Data Validation in Power BI Reports using Power Automate
source_url: https://medium.com/@guna24x7/automate-data-validation-in-power-bi-reports-using-power-automate-6deea7b04dbb
note_type: workflow
tags: [power-automate, power-bi, data-quality, validation, dax-query, scheduled-flow]
---

# Power BI DAX Query Data Validation Flow

Scheduled Power Automate flow that runs a DAX query against a Power BI dataset before business hours and validates the output against business rules — sending alerts if validation fails.

## Workflow Steps

1. **Scheduled trigger** — Recurrence action runs the flow daily before business hours
2. **Run a Query against Dataset** — Execute a parameterized DAX query against the target workspace/semantic model
3. **Compose actions** — Define validation rules that inspect the query output
4. **Conditional logic** — Handle pass/fail outcomes
5. **Notification** — Send email or Teams alert if validation fails

## How to Capture the DAX Query

1. Open the report in Power BI Desktop and wait for all visuals to load
2. Navigate to **Performance Analyzer** → **Refresh Visuals**
3. Capture the **Visual Query (DAX)** for the target visual
4. Copy the DAX query and store it in a file
5. Test in **DAX Query View** to confirm expected tabular output

## DAX Query Structure (from article)

```dax
// DEFINE: variables, filters, measure expressions
DEFINE
    VAR __DS0FilterTable =
        TREATAS({"Net sales - category breakdown"}, 'Tooltip Info'[nombre])
    VAR __DS0FilterTable2 =
        TREATAS({"Sold"}, 'Sales'[Status])
    VAR __DS0Core =
        SUMMARIZECOLUMNS(
            'Product'[Product],
            __DS0FilterTable,
            __DS0FilterTable2,
            "SumAmount", CALCULATE(SUM('Sales'[Amount])),
            "Product_Top_N", IGNORE('Design DAX'[Product Top N])
        )
    VAR __DS0PrimaryWindowed =
        TOPN(1001, __DS0Core, [SumAmount], 0, 'Product'[Product], 1)

// EVALUATE: return the result
EVALUATE
    __DS0PrimaryWindowed

ORDER BY
    [SumAmount] DESC, 'Product'[Product]
```

## Parameterizing the Query

Modify the query to include dynamic parameters so the same query template can be reused across different filters or date ranges:

```dax
TREATAS({@{variables('FilterValue')}}, 'Table'[Column])
```

## Power Automate Flow Overview

| Step | Action | Purpose |
|------|--------|---------|
| 1 | Recurrence | Daily trigger before business hours |
| 2 | Run a Query against Dataset | Execute the parameterized DAX query |
| 3 | Compose (×N) | Define validation rules against the output |
| 4 | Condition | Route based on pass/fail |
| 5 | Send email / Teams message | Alert stakeholders on failure |

## Validation Rule Examples (Compose Actions)

Use Compose actions to extract and check values:

```json
// Compose: Get total rows
length(body('Run_a_Query_against_a_Dataset')?['results']?['tables']?['0']?['rows'])

// Compose: Check total > 0
greater(length(outputs('Get_Row_Count')), 0)

// Compose: Check specific value
equals(body('Run_a_Query_against_a_Dataset')?['results']?['tables']?['0']?['rows']?['0']?['SumAmount'], 0)
```

## Limitations

- This approach validates visual-level data after all transformations — it does not validate raw source data
- For deeper data quality checks, consider **Microsoft Fabric + Semantic Link + Great Expectations** (not covered in this article)
- The query must be manually captured from Performance Analyzer — it is not auto-generated per schedule

## Related

- [[Failed-Flow-Monitoring-Alerting]] — Power Automate monitoring and alerting pattern
- [[Weekly-Status-Report-Aggregator]] — scheduled flow with notification step
