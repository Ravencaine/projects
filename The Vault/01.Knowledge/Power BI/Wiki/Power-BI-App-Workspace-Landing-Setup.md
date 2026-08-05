---
created: 2026-08-05
source: Power BI Dashboards Decision-Making (Boniface Muchendu)
note_type: atomic
tags: [power-bi, app, workspace, landing-page, navigation, publish]
---

# Power BI App Workspace Landing Page Setup

How to configure a dashboard as the first screen users see when they open a published Power BI App — via the Power BI Service app settings.

## Overview

Power BI apps can contain multiple dashboards and reports. By default, the app may open on a blank screen or a specific report. Setting a landing dashboard gives users a clear entry point.

## Steps

1. Publish your dashboard to the target workspace
2. In the **Power BI Service**: go to **Apps → [Your App] → Edit**
3. Navigate to **Navigation** (or **App settings**, depending on the UI version)
4. Find the **Landing page** dropdown and select the target dashboard
5. **Save** and republish the app

## What Happens After

- Any user who opens the app lands directly on the selected dashboard
- From the dashboard, users navigate to reports via button links or the nav pane
- The landing dashboard should include clear navigation to key reports

## When to Use

- Apps with 3+ reports — a landing page prevents navigation confusion
- Self-service apps where new users need orientation
- Executive apps where the landing dashboard IS the deliverable (see [[Executive-One-Pager-Dashboard-Design]])

## Related

- [[Dashboard-as-App-Landing-Page]]
- [[Executive-One-Pager-Dashboard-Design]]
