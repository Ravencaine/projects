---
created: 2026-08-09
updated: 2026-08-09
source: "Elevating Power BI Reports with HTML & CSS Joining Forces 💪.md"
note_type: atomic
tags: [power-bi, dax, substitute, placeholder, atomic]
---

# SUBSTITUTE Placeholder Chaining Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-html-css-joining-forces-fp20]]

DAX SUBSTITUTE replaces text within a string. When a template has multiple placeholders, chain SUBSTITUTE calls — each inner call replaces one placeholder, outer calls handle remaining ones. Order does not matter when placeholders are unique.

## Single substitution

```dax
SUBSTITUTE([Template], "{PLACEHOLDER}", _Value)
```

Returns the template string with `{PLACEHOLDER}` replaced by `_Value`.

## Two substitutions

```dax
SUBSTITUTE(
    SUBSTITUTE([Template],
        "{PLACEHOLDER1}", _Value1
    ),
    "{PLACEHOLDER2}", _Value2
)
```

## Three substitutions

```dax
SUBSTITUTE(
    SUBSTITUTE(
        SUBSTITUTE(
            [Template],
            "{PLACEHOLDER1}", _Value1
        ),
        "{PLACEHOLDER2}", _Value2
    ),
    "{PLACEHOLDER3}", _Value3
)
```

Each nested layer peels off one placeholder. The innermost `[Template]` has all placeholders intact; each outer SUBSTITUTE resolves one.

## Performance note

SUBSTITUTE is fast. For templates with many placeholders (5+), consider a single `PATH` or `FORMAT` approach instead, but for 2–5 substitutions the nested chain is readable and performant.

## Blank guard

Always wrap the final substitution in a conditional:

```dax
RETURN IF([Value] <> BLANK(), _Shape)
```

Without this, the HTML renders even when the underlying data is blank.

## Related

- [[html-shape-measure-template]] — template with multiple placeholders
- [[font-awesome-dax-icon-measure]] — icon-specific substitution chain
- [[html-measure-integration-pattern]] — full measure structure
