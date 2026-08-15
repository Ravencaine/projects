---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into tooltip options in Power BI visuals (Generally Available).md"
note_type: pattern
tags: [power-bi, tooltip, sentence-format, field-parameters, pattern]
---

# Field Parameters in Sentence Tooltip Pattern

> **Type:** pattern
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-06

## Problem

Field parameters let users swap the measure a visual displays. The sentence tooltip must reflect both the field name selected in the parameter AND the value of that field — without separate templates for each measure.

## Solution

Reference the field parameter twice in the sentence template: once for the name, once for the value.

## Field Parameter Reference Syntax

| Token | Returns |
|-------|---------|
| `{FieldParameter}` | Name of the selected field (e.g., "Profit", "Revenue") |
| `{FieldParameter Fields}` | Value of the selected field |

**Note:** The word "Fields" must match the value column name in the field parameter definition.

## Example

**Field parameter definition:**
```
MyMetric (Field Parameter)
├── Value column: MyMetric Fields
└── Parameters: Profit, Revenue, Margin
```

**Template:**
```
We had {MyMetric Fields} in {MyMetric} for {Segment}.
```

**Result when "Profit" is selected for Enterprise segment:**
> We had $940,097 in Profit for Enterprise.

## Steps

1. Create a field parameter with the measures to swap (e.g., Profit, Revenue, Margin)
2. Add the field parameter to the visual's axis or legend
3. Turn ON **Sentence format** in the visual's tooltip options
4. Write template using:
   - `{ParameterName}` → displays the selected field name
   - `{ParameterName Fields}` → displays the selected field's value
5. Reference other fields in the same template (e.g., `{Segment}`)

## Use Cases

- **Metric switcher:** "We had $940K in Revenue for Enterprise" vs "We had $180K in Profit for Enterprise"
- **Flexible KPI sentences:** One template works for any measure the user selects
- **Context-aware reporting:** Tooltip always contextualizes the right metric + right dimension

## See Also

- [[Source-Tooltip-Options-Generally-Available]] — source article
- [[Sentence-Format-Template-Pattern]] — sentence format template syntax
- [[Field-Parameters-Show-Values]] — field parameter basics
