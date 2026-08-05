---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: atomic
tags: [stewardship, feedback-loop, iteration, publish, UX, engagement]
related: [Data-Narratives-Report-Design, The-3-30-300-Rule]
---

# Report Stewardship

The ongoing practice of maintaining, improving, and engaging users with a published Power BI report after initial deployment.

## The Stewardship Cycle

```
Publish → Monitor → Collect Feedback → Iterate → Republish
```

## 1 — Publish with a Feedback Mechanism

- Add a **Comments** pane in the Power BI Service.
- Add a **feedback button** via a text box linking to a Teams channel or email.
- Publish the usage metrics dashboard (available in Power BI Admin portal).

## 2 — Monitor Usage

- Check **Usage metrics** in Power BI Service:
  - Most-used pages and visuals.
  - Least-used slicers and filters.
  - Average session time per page.
- Remove or deprioritise unused visuals from the next iteration.

## 3 — Collect Feedback

- **Scheduled check-ins:** Monthly review of usage metrics + stakeholder interviews.
- **Track which 3/30/300 questions users are actually asking**: validate the report design.
- **Log feedback** in a SharePoint list or Teams channel — don't rely on memory.

## 4 — Iterate

- Publish updates quarterly or after major data model changes.
- Maintain a **changelog** for the report (date, what changed, why).
- Apply feedback from the most-active users first.

## 5 — Drive Engagement

- **Annotate** published reports to highlight new features or findings.
- **Subscribe** stakeholders to scheduled refresh emails.
- **Create a dashboard newsletter** using Power Automate.

## The Stewardship Loop in the 3-30-300 Framework

| 3-30-300 Tier | Stewardship Action |
|---------------|------------------|
| 3 seconds | Monitor bounce rate — are users leaving immediately? |
| 30 seconds | Check which exploration filters are used most. |
| 300 seconds | Track drillthrough usage — is the detail page being used? |

## Notes

- Bittar's Data Narratives article includes a "Report Stewardship" section — the idea that a report is a living product, not a one-time delivery.
- [[The-3-30-300-Rule]] provides the feedback metrics framework — each tier has its own stewardship question.

## Related

- [[The-3-30-300-Rule]] — feedback metrics per tier
- [[Data-Narratives-Report-Design]] — the process that includes stewardship as a phase
