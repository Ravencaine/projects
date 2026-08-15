---
created: 2026-08-09
updated: 2026-08-09
source: "6 Better Alternatives to the Excel IF Function • My Online Training Hub"
note_type: atomic
tags: [excel, formulas, let, deduplication, repeated-calculation, performance, maintainability]
see_also: [LET-Makes-Formulas-Readable]
---

# LET for Deduplication

`LET` names a sub-expression that appears more than once in a formula, so it is evaluated once and reused. This framing (deduplication / efficiency) is distinct from the readability framing in `LET-Makes-Formulas-Readable` — both are true; this note captures the repeated-calculation use case.

## The Repeated-Calculation Anti-Pattern

Commission formula: paid only if net sales (Sales − Discount) meet the target.

```
=IF(D6*(1-E6)>=F6, D6*(1-E6)*5%, 0)
```
The net sales calculation `D6*(1-E6)` appears **twice:** once in the condition, once in the result. In a real workbook copied across thousands of rows, this duplication compounds.

## The LET Solution

```
=LET(
  netSales, D6*(1-E6),
  IF(netSales>=F6, netSales*5%, 0)
)
```
`netSales` is defined once. Used twice in the IF. Excel evaluates `D6*(1-E6)` once.

## Three Benefits

1. **Correctness:** the calculation is defined once — if the formula logic changes, it changes in one place
2. **Readability:** `netSales` names what the calculation represents
3. **Performance:** repeated sub-expression is evaluated once, not N times

## Why This Framing Is Distinct from LET-Makes-Formulas-Readable

The earlier note covers LET's readability benefit: named variables make a formula read like a sentence. This note covers LET's deduplication/efficiency benefit: a sub-expression appears more than once and LET eliminates the repetition. Both are true of LET simultaneously — they are different aspects worth noting separately.

## When to Use LET (Deduplication Framing)

- The same sub-expression appears 2+ times in a formula
- The formula is long or complex
- The repeated calculation has a business meaning worth naming
- Performance matters (large datasets, complex expressions)

## Related

- [[Source-6-Better-Alternatives-to-IF-Mynda-Treacy]] — source
- [[LET-Makes-Formulas-Readable]] — LET for readability; this note covers the deduplication angle
