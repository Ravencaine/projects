---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: reference
tags: [dax, calculate, philosophy, counterculture, deckler]
---

# CALCUHATE — The CALCULATE Counterculture

Greg Deckler's contrarian stance: CALCULATE is inessential, overhyped, and makes DAX harder to write, debug, and maintain.

## The Argument

On July 24, 2020, Greg Deckler posted "CALCUHATE - Why I Don't Use DAX's CALCULATE Function" on the Microsoft Community forum. His thesis: CALCULATE is not "the most important function in DAX" — it's a "fancy FILTER" that obscures what the DAX engine is actually doing.

Brian Julius's foreword in DAX for Humans (the book's Foreword) documents the intellectual journey: the community's unanimous belief that CALCULATE was essential, Greg's dissent, and Julius's own 30-day experiment of writing DAX without CALCULATE.

## The No CALCULATE Alternative

Every calculation that can be written with CALCULATE can be written without it using the **Banana Pattern**:

```dax
Measure =
    VAR __ExcludeItem = "Pickle"
    VAR __Table = FILTER( 'Table', 'Table'[Item] <> __ExcludeItem )
    VAR __Result = SUMX( __Table, [Total Cost] )
    RETURN __Result
```

Compare to the CALCULATE equivalent:

```dax
Sum Total Cost No Pickle C =
    CALCULATE(
        SUM( 'Table'[Total Cost] ),
        'Table'[Item] <> "Pickle"
    )
```

Both return the same result. The No CALCULATE version exposes every step as a VAR — this is Deckler's core argument for readability and debuggability.

## Why CALCULATE Is "Opaque"

According to Deckler, CALCULATE has these problems:

1. **Hidden context transition**: CALCULATE inside an iterator (like SUMX) creates a context transition — the row context becomes a filter context. This transition is invisible in the CALCULATE syntax.
2. **Nested CALCULATEs compound confusion**: Multiple nested CALCULATEs make it impossible to trace which filter is active at any point.
3. **The "fancy FILTER" problem**: CALCULATE(EVALUATE(expression), filter) is semantically equivalent to FILTER(table, filter) followed by the aggregation — but the syntax hides this equivalence.
4. **No intermediate inspection**: CALCULATE doesn't expose its working table. TOCSV can't easily inspect what's happening inside a CALCULATE.

The counterpoint: CALCULATE's power lies in its ability to change filter context while preserving other active filters. The No CALCULATE approach often requires REMOVEFILTERS or ALL to replicate this.

## When Deckler Accepts CALCULATE

Ch16 "When to Use CALCULATE?" makes clear: Deckler doesn't ban CALCULATE entirely. He argues for starting without it, and only reaching for it when truly needed (e.g., cross-directional filters, complex REMOVEFILTERS scenarios, CALCULATETABLE for query context).

## The Community Response

The community response to CALCUHATE was mixed. Some found it liberating; others found it impractical for complex scenarios. The DAX for Humans book represents the most thorough written argument for the No CALCULATE approach.

## Related

- [[no-calculate-banana-pattern]] — the foundational FILTER + iterator pattern
- [[no-calculate-vs-calculate-deckler]] — side-by-side comparison
- [[calculate-internal-context-transition]] — CALCULATE's context transition mechanism
- [[dax-debugging-tocsv]] — the No CALCULATE debugging workflow
