---
created: 2026-07-27
updated: 2026-08-02
source: "How to Set Up Power BI Subscriptions for Hidden Pages"
note_type: workflow
tags: [power-bi, subscriptions, power-bi-service, automation, hidden-pages]
---

# Power BI Subscription Setup (Including Hidden Pages)

Configure automated email delivery of Power BI report pages — including hidden pages for targeted distribution.

## Use Cases

- **Hidden data export page:** raw data table on a hidden page, auto-emailed as CSV to analysts
- **Executive summary only:** dashboard on hidden page, distributed to executives without exposing the full report
- **Behind-the-scenes detail:** diagnostic visuals on hidden pages for IT/BI team only

## Steps

### 1. Create and Hide the Page

1. In Power BI Desktop, create the page
2. Right-click the page tab > **Hide page**
3. Publish to Power BI Service

### 2. Configure the Subscription

1. Open the published report in Power BI Service (app.powerbi.com)
2. Navigate to the hidden page (bookmark link or direct URL)
3. Click **Subscribe** (bell icon or menu)
4. Set **Frequency:** Daily / Weekly / Monthly / On a schedule
5. Set **Time** and **Time zone**
6. Under **Content:** ensure the hidden page is selected
7. Under **Recipients:** add email addresses
8. Under **Attachment:** choose PDF, PPTX, or PNG
9. Enable **Include link to report** if recipients need access

### 3. Key Settings

| Setting | Options | Notes |
|---------|---------|-------|
| Frequency | Daily, Weekly, Monthly, Custom | |
| Attachment | PDF, PPTX, PNG | Only the subscribed page is included |
| Recipients | Email addresses | Internal or external (with external sharing enabled) |
| Link to report | On/Off | Recipients may not have report access |

## Hidden Page Access Note

Users do NOT need access to the full report to receive the subscription — they receive the page content directly in email.

## Related

-  — pre-subscription deployment checklist
