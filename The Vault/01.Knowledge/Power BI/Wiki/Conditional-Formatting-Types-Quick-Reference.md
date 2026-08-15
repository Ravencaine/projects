---
created: 2026-08-06
updated: 2026-08-06
source: Conditional Formatting in Power BI
note_type: reference
tags: [conditional-formatting, reference, power-bi, tables, matrices, color, icons, data-bars]
---

# Conditional Formatting Types Quick Reference

Quick reference for all conditional formatting types available in Power BI tables and matrices — configuration paths, use cases, and key options.

## Formatting Types

### Background Color

- **Location:** Format pane → Cell elements → Background color → ON → fx
- **Options:** Solid color (rule), gradient (field value), color scale
- **Use:** Heat maps, performance at-a-glance, trend shading

### Font Color

- **Location:** Format pane → Cell elements → Font color → ON → fx
- **Options:** Rule-based colors, field-value-driven colors
- **Use:** Contrasting text labels, high-visibility status

### Data Bars

- **Location:** Format pane → Cell elements → Data bars → ON
- **Options:** Show bar only vs. show bar and number, axis settings, bar direction
- **Use:** Inline bar chart within table cells, comparative magnitude

### Icons

- **Location:** Format pane → Cell elements → Icons → ON → fx
- **Options:** Rules, field value, directional (arrows), status (shapes), custom
- **Use:** KPI indicators, trend arrows, traffic lights, thumbs up/down

### Web Links

- **Location:** Format pane → Cell elements → Web URL → ON
- **Options:** Column-based URL or rule-based conditional URL
- **Use:** Product names linking to product pages, customer IDs linking to CRM records

## Rule Configuration (fx Dialog)

| Setting | Description |
|---------|-------------|
| Format by | Rules, Field value, or Percentile |
| Minimum / Maximum | Range endpoints for color scales |
| Add rule | Stack multiple conditions |
| Based on field | For field-value formatting — select the measure |
| Icon style | Shape set for icons (arrows, shapes, ratings) |

## Practical Quick Reference

```
Scenario                          | Type           | Config
Sales > average = green, < = red | Background     | Rule with average threshold
KPI thumbs up / thumbs down       | Icons          | Rule: >= target → thumbs up
Clickable product names           | Web URL        | URL column mapping
Inline bar chart                 | Data bars      | Show bar + number
Traffic light status              | Icons          | 3-rule: red/yellow/green
Dynamic color from DAX measure    | Background     | Format by: Field value
Color scale red → yellow → green  | Background     | Format by: Gradient
```

## Notes

- Data bars and color scales can be combined with rules on the same field
- Web URL formatting requires the column to contain valid URLs (https://...)
- Icons are available as: directional arrows, shapes, ratings, and custom (field value)
- See [[Conditional-Formatting-in-Multi-Row-Card-Visuals]] for the workaround when the visual does not support conditional formatting
- See [[conditional-formatting-via-dax]] for the DAX measure-based field value approach

## Related

- [[Conditional-Formatting-in-Power-BI]] — concept overview and how-to
- [[conditional-formatting-via-dax]] — DAX measure-driven conditional formatting
- [[Conditional-Formatting-in-Multi-Row-Card-Visuals]] — DAX UNICHAR workaround for Card visuals
- [[UNICHAR-based-Conditional-Formatting-Pattern]] — icon pattern via DAX for visuals without formatting UI
