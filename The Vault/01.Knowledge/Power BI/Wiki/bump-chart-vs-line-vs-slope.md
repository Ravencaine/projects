---
created: 2026-08-02
updated: 2026-08-05
source: What Bump Charts Tell You That Line Charts Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, bump-chart, line-chart, slope-chart, rank, comparison]
---

# Bump Chart vs Line vs Slope: When to Track Rank vs Value vs Before/After

Three chart types that look similar but answer fundamentally different questions — use the right one or the story disappears.

| Chart | What it shows | Use when |
|-------|-------------|----------|
| **Line chart** | How raw values change over time | Actual numbers matter; magnitude of change is the story |
| **Slope chart** | Difference between two points in time | Clean before-vs-after; exactly two time periods |
| **Bump chart** | How categorical rank changes over time | Competitive ordering is the story; overtakes and leadership churn |

**Reading a bump chart:**
- Line moves **up** = better rank (not higher value — rank, ordinal position)
- Line is **flat** = stable rank (nobody passed you; does NOT mean stable value)
- **Crossing** = overtake event; the vertical gap between lines is ordinal, not magnitude
- **Rank 1 at the top:** higher on page = better by convention

**Key limitation:** Bump charts hide magnitude. A company dropping from 50% to 30% share stays at rank 1 if competitors are even lower. Pair with a value chart when both rank and magnitude matter.

**Design rules:**
- Direct-label lines at endpoints (skip legends)
- Highlight top 1–3 series in color; mute the rest in gray
- Show markers at actual data points to distinguish observed ranks from connecting paths
- Straight lines for analytical charts (honest); smooth curves only for editorial with visible anchors

**When NOT to use:**
- Magnitude/gap is the real story → use line or bar chart
- Too many categories (20+) → use small multiples
- Rankings are noisy (polling, small samples) → rank flips reflect noise not signal
- Ties are common and important → ties create overlap that hides lines
