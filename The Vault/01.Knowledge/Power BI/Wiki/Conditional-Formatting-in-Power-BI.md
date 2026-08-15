---
created: 2026-08-06
updated: 2026-08-06
source: Conditional Formatting in Power BI
note_type: atomic
tags: [conditional-formatting, power-bi, visual-design, tables, matrices]
---

# Conditional Formatting in Power BI

Power BI's conditional formatting feature dynamically changes the appearance of visual elements based on data values — applying background colors, font colors, data bars, icons, or web links to cells in tables and matrices.

<!-- one-line description: Built-in Power BI feature for dynamic visual formatting of table/matrix cells based on rules, field values, or percentile thresholds -->

## Definition

Conditional formatting in Power BI applies dynamic styling to visual elements — cells in tables and matrices, data points in charts — based on rules you define. Unlike DAX-based formatting (see [[conditional-formatting-via-dax]]), this is configured through the Format pane and does not require writing DAX expressions.

## Formatting Types

| Type | Description | Use case |
|------|-------------|---------|
| **Background Color** | Fill color of cells | Heat maps, at-a-glance performance |
| **Font Color** | Text color within cells | Contrasting labels, status indicators |
| **Data Bars** | Horizontal bars inside cells | Bar chart embedded in a table |
| **Icons** | Pre-built or custom icons | KPI indicators, status badges |
| **Web Links** | Clickable URLs inside cells | Product → detail page links |

## How to Apply

1. Select a **Table** or **Matrix** visual
2. In the **Format pane**, expand **Cell elements**
3. Toggle the formatting type **ON** (Background color, Font color, etc.)
4. Click **fx** to open the rule editor
5. Configure: rule type (rule / field value / percentile), thresholds, colors

## Rule Types

- **Rules**: Static thresholds you define (e.g., > 6000 = green)
- **Field value**: Use a DAX measure's output to drive the color/icon — see [[conditional-formatting-via-dax]]
- **Percentile**: Based on data distribution (top 10%, bottom 10%, etc.)
- **Number / Text / Date**: Automatic based on field data type

## Practical Examples

| Example | Implementation |
|---------|----------------|
| Sales above average = green, below = red | Rule with average as threshold |
| KPI thumbs up/down icons | Icons conditional formatting with rule |
| URL column clickable in table | Web links conditional formatting |
| Data bars in a numeric column | Data bars conditional formatting |
| Color scale across all cells | Background color with gradient |

## Scope and Limitations

- Available in **Table** and **Matrix** visuals (via Format pane → Cell elements)
- Also available in some chart visuals (bar, column, ribbon, scatter) via their format panes
- **Multi-Row Card** and plain **Card** visuals do **not** have conditional formatting — see [[Conditional-Formatting-in-Multi-Row-Card-Visuals]] for the DAX UNICHAR workaround
- For icons via DAX measure (in visuals without formatting UI), see [[UNICHAR-based-Conditional-Formatting-Pattern]]

## Related

- [[conditional-formatting-via-dax]] — DAX measure-based conditional formatting (Format pane → Field value)
- [[Conditional-Formatting-in-Multi-Row-Card-Visuals]] — DAX UNICHAR workaround for Card/Multi-Row Card visuals
- [[UNICHAR-based-Conditional-Formatting-Pattern]] — the DAX pattern for icon-based conditional formatting
- [[UNICHAR-Icon-Codes-Reference]] — Unicode icon code quick reference
- [[Conditional-Formatting-Types-Quick-Reference]] — reference card for all formatting types and their configuration
