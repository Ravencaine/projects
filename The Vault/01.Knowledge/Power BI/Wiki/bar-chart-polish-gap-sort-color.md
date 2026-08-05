---
created: 2026-08-02
updated: 2026-08-05
source: Why Simple Bar Charts Are Harder Than They Look
note_type: pattern
tags: [powerbi, pattern, data-visualization, bar-chart, design, sorting, color, label, polish]
---

# Bar Chart Polish: Flat Design, Gap Ratio, Labels, Sorting, Color Intent, Orientation

Once the data is right, these design choices make the chart professional rather than misleading.

**Keep it flat:**
3D bars distort length (value at front vs. back of block is unclear) and add noise. Flat is not boring — it is professional.

**Mind the gap:**
Default settings often create a "picket fence" — thin bars with wide gaps. Rule of thumb: gap width ≈ half the bar width (x/2). Makes the data feel connected and substantial.

**Direct labels vs. gridlines (pick one):**
- **Direct labels** at the end of bars: exact numbers matter. Delete gridlines and axis numbers for a cleaner look.
- **Gridlines**: when comparing distant bars or general shape matters more than exact values. Keep gridlines faint — they should be a whisper, not a shout.

**Sorting for the story:**
- **For ranking:** sort by value. Instantly shows leader vs. laggard.
- **For structure:** keep natural order when categories have inherent sequence (Weeks 1–8, Jan–Dec). Never sort these by value — it destroys the logical story.
- **Alphabetical:** only when no ranking or structure applies. Never the default.

**Color with intent:**
If every bar is a different color, readers waste energy looking for a pattern. Use one neutral color (teal, gray) for all bars, and a highlight color only for the bar you are discussing.

**Flip to horizontal when:**
- Category labels are long (e.g., "Cannot log in or reset password")
- Horizontal layout lets labels read left-to-right, how people naturally scan
- Vertical default for short labels in wide layouts

**Dot plot substitute:** When differences are tiny relative to the values (e.g., 1,000,000 vs. 1,000,010), bar charts make them look identical. Switch to a dot plot — position encoding handles small relative differences better than length encoding.
