---
created: 2026-08-15
source: "7 Powerful Ways to Share Your Power BI Reports Effectively.md"
source_url: https://medium.com/write-a-catalyst/7-powerful-ways-to-share-your-power-bi-reports-effectively-bbb33afe301f
note_type: pattern
tags: [power-bi, sharing, embed, azure, sharepoint]
---

# Embed Power BI Report in Website or Application

<!-- Authenticated embed for portals, line-of-business apps, and SharePoint Online pages -->

## Purpose

Render a Power BI report inside another product or portal with authentication — the alternative to [[publish-power-bi-report-to-web-public-embed.md]] when the report must remain gated. Covers two practical paths: **Power BI Embedded** (Azure) and the **SharePoint Online Power BI web part**.

## Components

- A Power BI report in a workspace
- For Power BI Embedded: an **Azure subscription**, a **Power BI Embedded capacity**, an **AAD application registration**, and developer setup
- For SharePoint: a **SharePoint Online** site and the built-in **Power BI web part**

## Structure

### Path A — Power BI Embedded (Azure, for ISVs / custom apps)

```
Report → Power BI Workspace (Embedded capacity)
            ↓
        AAD app registration (service principal)
            ↓
        Embed token (REST API)
            ↓
        powerbi-client React/JS library
            ↓
        Custom web / mobile app
```

### Path B — SharePoint Online Power BI web part

```
SharePoint page → + Add → Power BI web part
                            ↓
                  paste report URL (from Service)
                            ↓
                  users authenticate via SSO
```

## Workflow (Power BI Embedded, high level)

1. Provision a **Power BI Embedded capacity** in Azure (A-series SKU sized to expected load).
2. Assign your target workspace to that capacity.
3. Register an **Azure AD application** and grant it permission on the workspace.
4. Use the Power BI REST API (`GenerateToken` / `GetReports`) to issue embed tokens per user or per app.
5. Load the report in your app using `powerbi-client` (JavaScript / .NET / React).
6. Apply row-level security (RLS) so each viewer only sees their slice of data.

## Workflow (SharePoint web part, simple)

1. Publish the report to a workspace you have access to.
2. Copy the report URL from the Service address bar.
3. Edit any SharePoint Online page → **+ Add** → **Power BI** web part.
4. Paste the URL and publish the page.
5. Page viewers who have access to the underlying report see it inline (single sign-on).

## Example

A SaaS analytics product embeds Power BI reports for its customers:

- Each customer gets their own Power BI Embedded capacity in Azure.
- The SaaS app's backend uses service-principal auth to call `GenerateToken` per tenant.
- The frontend uses `powerbi-client-react` to render reports inside the app shell.
- RLS roles on the dataset scope each customer to their own data only.

## Variations

- **App-Owns-Data** — your app controls auth (the pattern above). Common in ISVs.
- **User-Owns-Data** — the user signs in with their own Power BI identity and the app delegates. Simpler but requires each end user to have a Power BI license.
- **Secure Embed** (SharePoint) — the easiest authenticated embed for non-developers.

## License

- **Power BI Embedded** (Azure) — you pay per hour for capacity; no per-user Power BI license required for end users.
- **SharePoint web part** — sender needs Pro or Premium; viewers need access to the report.
- **Power BI Pro or Premium** — covers scenarios where end users already have a Power BI identity.

## Related

- [[power-bi-sharing-methods-compared.md]] — comparison
- [[publish-power-bi-report-to-web-public-embed.md]] — pattern (unauthenticated counterpart)