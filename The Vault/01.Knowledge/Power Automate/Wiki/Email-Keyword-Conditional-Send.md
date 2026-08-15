---
created: 2026-08-10
updated: 2026-08-10
source: Automating Workflow with Power Automate for Email Processing
source_url: https://medium.com/@python-javascript-php-html-css/automating-workflow-with-power-automate-for-email-processing-2dfed29641ef
note_type: atomic
tags: [power-automate, email, conditional, trigger, action]
---

# Email Keyword Conditional Send Pattern

Trigger on email arrival → check for keyword in subject or body → extract data → conditionally send a response email. Core email routing pattern used in most Power Automate email automations.

## Minimal Flow Structure

```yaml
Trigger:    When a new email arrives (V3)
            Subject Filter: "Your Email Subject"
            Folder: Inbox

Action:     Get emails (V3)

Condition:  If email contains "Keyword"
  Yes:
    Action: Send an email
            Subject: "Relevant Subject"
            Body: [extracted table row]
  No:
    (End of flow)
```

## Key Decisions

| Element | Choice | Reason |
|---------|--------|--------|
| Trigger | "When a new email arrives" V3 | Polls mailbox on schedule; supports subject filter |
| Filter at trigger | Subject Filter parameter | Reduces processing to only relevant emails |
| Get emails | Separate action | Pulls full email body for content inspection |
| Condition | Body/subject contains keyword | Controls whether data extraction runs |
| Output | Send email with extracted row | Delivers only relevant data |

## Limitations of This Approach

- **Temp Mail / disposable email services** will trigger flows if they land in the inbox — add sender allowlists for production
- **Keyword matching is substring** — "keyword" matches "keywords" and "mykeyword123" — use `contains` with boundary logic for precision
- **Table extraction from HTML email body** requires additional parsing (HTML to text conversion, split on delimiters, or pattern matching)
- **No retry logic** shown — production flows should handle transient failures

## Related

- [[VIP-Email-to-Teams-Alert-Flow]] — email trigger with priority filter → Teams card
- [[Flagged-Email-to-Planner-Task]] — email trigger → Planner task creation
- [[Email-Attachment-Archiver-to-SharePoint]] — email trigger → attachment extraction
