---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: atomic
tags: [dax, user-defined-function, performance, optimization, anti-pattern]
---

# UDFs Don't Automatically Improve Performance

A UDF is a reusable expression, not a performance shortcut. Shared infrastructure multiplies inefficiency by the number of callers.

## Definition

UDFs centralize business logic. If that logic is inefficient, centralizing it makes the inefficiency worse — a slow function called by thirty measures is thirty times slower than a slow measure used once.

## Key Points

- A function is an alias for its expression body — DAX evaluates it identically each time
- Inefficiency scales with the number of callers: a `FILTER` inside a function fires once per measure that calls it
- Shared functions are higher-stakes than single measures: a performance bug in a function library affects every report in the model
- SQLBI guidance: **optimize function code more aggressively than a single measure** precisely because it's shared infrastructure

## The Multiplier Effect

```
Inefficient single measure:
    100ms × 1 caller = 100ms total

Inefficient UDF:
    100ms × 30 callers = 3,000ms total
```

## When Performance Can Improve

Performance can improve indirectly when UDFs replace *multiple different* inefficient copies of the same logic:

- One optimized function replaces twelve slightly different inefficient implementations
- A function with intentional context handling (EXPR) can be more efficient than inline CALCULATE scattered across measures
- Fix once, benefit everywhere — including performance fixes

## Rule

Profile every function with DAX Studio or Performance Analyzer before marking it production-ready. A function that saves 10ms per call is worth it. One that costs 10ms per call across 30 measures is a performance regression.

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[val-vs-expr-parameter-evaluation]] — gotcha
- [[udfs-vs-copy-paste-pattern]] — comparison
