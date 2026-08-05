---
created: 2026-08-02
updated: 2026-08-05
source: The New Image Visual in Power BI Is a Quiet Game Changer
note_type: atomic
tags: [power-bi, image-visual, accessibility, alt-text, screen-reader, inclusive-design]
---

# Image Visual Accessibility — Alt Text, Screen Readers

The Image visual now generates accessible elements with semantic meaning — critical for public sector, healthcare, and large enterprise clients.

## Accessibility Features

| Feature | Detail |
|---------|--------|
| **Alt text** | Front-and-center in the visual properties pane |
| **Screen reader support** | Image content read aloud to users |
| **Semantic meaning** | Images are not decorative noise — they carry information |
| **Narration** | Dynamic alt text can reflect current state (via measure) |

## Why It Matters

- **Public sector** — compliance with accessibility standards (WCAG)
- **Healthcare** — HIPAA-adjacent environments require inclusive design
- **Enterprise** — corporate accessibility policies increasingly require it
- **All audiences** — inclusive design benefits everyone

## Dynamic Alt Text Pattern

```dax
Status Alt Text :=
    SWITCH(
        TRUE(),
        [Risk] <= 3, "Status: Low risk — within acceptable threshold",
        [Risk] <= 6, "Status: Medium risk — review recommended",
        "Status: High risk — immediate action required"
    )
```

Set the Image visual's Alt text → Field value → `Status Alt Text` measure.

## Related

- [[image-visual-dynamic-binding]] — dynamic image content
