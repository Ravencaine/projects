---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into tooltip options in Power BI visuals (Generally Available).md"
note_type: pattern
tags: [power-bi, tooltip, sentence-format, field-reference, curly-braces, pattern]
---

# Sentence Format Template Pattern

> **Type:** pattern
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-06

## Problem

Visual tooltips show field names and values but lack narrative context. Report authors want a readable sentence that explains the data point — e.g., "Sales changed by $3.7M (44%) since last year" — rather than a list of numbers.

## Solution

Sentence format lets you write a template mixing plain text and `{FieldName}` field references. Power BI substitutes the actual value for each field reference on hover.

## Syntax

| Token | Meaning |
|-------|---------|
| `{FieldName}` | Insert value of `FieldName` for the hovered data point |
| `**text**` | Bold text (markdown-style) |
| Bold values toggle | Power BI auto-bolds all substituted field values |

## Example Template

```
{Segment} sales changed by {Sales YoY} ({Sales YoY %}) from same period last year with a total of {Sales} across all years.
```

**Renders as:**
> Small Business sales changed by $3,701,592 (44%) from same period last year with a total of $42,427,919 across all years.

## Configuration Steps

1. Select visual
2. Format visual → General → Tooltips → Options
3. Turn ON **Sentence format**
4. Enter template text with `{FieldName}` references
5. (Optional) Turn ON **Bold values** to highlight substituted values
6. (Optional) Turn ON **Sentence format only** to show only the sentence (hide all other fields)

## Combining with Tooltip Fields Only

Sentence format appears below whatever fields the tooltip already shows:
- **Sentence format only = OFF** → sentence at bottom of existing tooltip (field list + sentence)
- **Sentence format only = ON** → sentence only (no field list)

## Common Patterns

### YoY Change Narrative
```
Sales changed by {Sales YoY} ({Sales YoY %}) since the same period last year.
```

### KPI Status
```
{Product} is {KPI Status} with {Sales} in revenue this period.
```

### Contextual Comparison
```
{Region} contributed {Sales} ({Sales % of Total}) to total sales this {TimePeriod}.
```

## See Also

- [[Source-Tooltip-Options-Generally-Available]] — source article
- [[Tooltip-Type-Selection-Workflow]] — decision workflow
- [[Drillable-Hierarchy-Sentence-Tooltip-Pattern]] — ISINSCOPE pattern for drill-aware sentences
- [[Field-Parameters-Sentence-Tooltip-Pattern]] — field parameter references in templates
