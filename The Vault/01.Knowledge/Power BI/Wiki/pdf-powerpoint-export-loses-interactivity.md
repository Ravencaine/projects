---
created: 2026-08-15
source: "7 Powerful Ways to Share Your Power BI Reports Effectively.md"
source_url: https://medium.com/write-a-catalyst/7-powerful-ways-to-share-your-power-bi-reports-effectively-bbb33afe301f
note_type: gotcha
tags: [power-bi, export, pdf, powerpoint, interactivity, gotcha]
---

# PDF / PowerPoint Export Loses Interactivity

<!-- An exported PDF or PPTX is a static snapshot — filters, slicers, drill-through, tooltips, and bookmarks do not survive -->

## Expected Behaviour

Once a recipient opens an exported PDF or PowerPoint, you might expect them to be able to click a chart, apply filters, switch pages, drill through, hover for tooltips, or jump via bookmarks. After all, it came from an "interactive" dashboard.

## Actual Behaviour

A Power BI report exported to PDF or PowerPoint is a **static image set**. Each report page becomes one PDF page or one PowerPoint slide, and the visuals render exactly as they appeared at export time:

- **Slicers and filters** — frozen at the state the exporter had them. The recipient cannot change them.
- **Drill-through** — completely absent. Clicking a visual in the PDF/PPTX does nothing.
- **Tooltips** — not rendered on hover (the tooltip text may appear as static labels if it was visible, otherwise it's gone).
- **Bookmarks** — invisible. There's no "click to navigate" because there's nothing to click on.
- **Custom visuals** — render their default state, but any user-input controls inside them are dead.
- **Cross-filtering** — clicking one visual does not highlight others.

The exported file is a faithful representation of one frozen moment in one user's session. It is not a live report.

## Why It Happens

PDF and PowerPoint are fundamentally static formats. Power BI flattens each report page into a printable layout; there is no runtime to drive the visuals. Export was designed for print/slide-deck scenarios where interactivity isn't possible anyway, not as a substitute for sharing the live report.

## How to Handle It

1. **Choose export deliberately** — only when the audience truly needs a static artifact (board pack, audit archive, compliance record, slide deck).
2. **For interactivity, share the live report** via [[share-via-power-bi-service-workspace-or-app.md]], [[share-power-bi-report-link-with-access-permissions.md]], or [[share-power-bi-report-external-users-b2b.md]].
3. **Document the snapshot moment** — when the audience needs to know what filters were applied at export time, write them on the cover slide or in the email body.
4. **Use paginated reports** (RDL) when you need a print-perfect, parameterised PDF that *is* designed for static output. Paginated reports handle page breaks, repeating headers, and complex layouts far better than exported Power BI reports.
5. **For recurring snapshots**, pair export with [[schedule-power-bi-report-email-subscription.md]] to automate the delivery.

## Related Gotchas

- [[publish-to-web-anyone-with-link-exposure.md]] — the other gotcha extracted from this article, on the same distribution-channel axis