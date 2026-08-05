---
type: vault-query
question: "what is CALCULATE in DAX"
date: 2026-07-28T20:54:25
kb: DAX Code
---

# what is CALCULATE in DAX



# CALCULATE in DAX

**CALCULATE** is described as *"the heart of DAX"* and is the **only function in DAX that can modify filter context**.

## Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Purpose** | Changes filter context, enables complex calculations, unlocks advanced analytics |
| **Key Capability** | The only DAX function that can modify filter context |
| **Without CALCULATE** | Limited to whatever filters come from slicers and visuals |
| **With CALCULATE** | Can override filters, add new ones, or keep specific filters |

## Syntax

```dax
CALCULATE(<expression>, <filter1>, <filter2>, ...)
```

## Filter Context Modification

CALCULATE works by:
1. **Evaluating the expression** within a modified filter context
2. **Accepting filter arguments** that can:
   - Override existing filters
   - Add new filters
   - Remove existing filters
   - Keep specific filters active

## Example

```dax
Total Sales US = CALCULATE(
    SUM(Sales[Revenue]),
    FILTER(ALL(Geography), Geography[Country] = "United States")
)
```

This overrides any country filter from slicers/visuals and returns only US sales.

---

**Sources:**
- `01.Knowledge/DAX Code/Wiki/CALCULATE in Power BI The Most Important Function in DAX Explained with Examples.md`
- `01.Knowledge/DAX Code/Wiki/Power BI Demystified Row Context vs. Context Transition Explained with Examples.md`

## Sources

  1. [[01.Knowledge/DAX Code/Wiki/What is Filter Context in Power BI A Complete Guide with Examples and Visuals.md|What is Filter Context in Power BI A Complete Guide with Examples and Visuals]] — score 14.947  2. [[01.Knowledge/DAX Code/Wiki/CALCULATE in Power BI The Most Important Function in DAX Explained with Examples.md|CALCULATE in Power BI The Most Important Function in DAX Explained with Examples]] — score 14.038  3. [[01.Knowledge/DAX Code/Wiki/Power BI Demystified Row Context vs. Context Transition Explained with Examples.md|Power BI Demystified Row Context vs. Context Transition Explained with Examples]] — score 12.571  4. [[01.Knowledge/DAX Code/Wiki/the-dax-concepts-that-actually-save-you-time-source.md|The DAX Concepts that Actually Save You Time in Power BI]] — score 12.288  5. [[01.Knowledge/DAX Code/Wiki/dax-context.md|DAX Context]] — score 12.248

## Query Log

- **Date:** 2026-07-28 20:54
- **Top results:** 20 notes ranked
- **Dominant KB:** DAX Code
