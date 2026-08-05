---
created: 2026-08-02
updated: 2026-08-03
source: The New Image Visual in Power BI Is a Quiet Game Changer
note_type: pattern
tags: [dax, pattern, image-visual, dynamic-image, svg, url, measure, status]
---

# DAX-Driven Dynamic Images: One Measure → Infinite Visual States

The new Image Visual accepts a DAX measure as its image source — enabling fully dynamic, context-aware visuals driven entirely by the data model.

**Pattern:** A measure returns a URL or SVG string; the Image Visual renders it. The same measure adapts to filter context, slicer selections, and calculated conditions.

**Example use cases:**

```dax
-- Status indicator: color dot based on variance
Status Icon :=
SWITCH(
    TRUE(),
    [Variance %] > 0.05, "https://mysite.com/green-dot.png",
    [Variance %] < -0.05, "https://mysite.com/red-dot.png",
    "https://mysite.com/yellow-dot.png"
)

-- SVG string directly (no external hosting needed)
Arrow Icon :=
SWITCH(
    TRUE(),
    [Sales] > [Target], UNICHAR(128316),  -- 🔼 fire emoji
    [Sales] < [Target], UNICHAR(128317),  -- 🔽
    UNICHAR(128528)                        -- 😐 neutral face
)

-- Navigation icon: highlights active section
Nav Icon :=
SWITCH(
    TRUE(),
    SELECTEDVALUE(PageTracker[Page]) = "Sales", "data:image/svg+xml;utf8,<svg>...</svg>",
    SELECTEDVALUE(PageTracker[Page]) = "Inventory", "data:image/svg+xml;utf8,<svg>...</svg>",
    "data:image/svg+xml;utf8,<svg>...</svg>"
)
```

**SVG embedding:** Encode SVG as a `data:image/svg+xml;utf8,<svg>...</svg>` URL. No external hosting required. Works for icons, arrows, pills, status lights.

**Design benefit:** All state logic lives in the measure — the visual is purely declarative. One measure drives all visual states, adapts to filter context, and is reusable across pages.

> Complements `sparklinesvg-lastndays.md` — that UDF generates SVG; this pattern shows how to wire it into the new Image Visual natively without a table container.
