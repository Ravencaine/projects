---
created: 2026-08-05
updated: 2026-08-05
source: Auto-Refresh SharePoint Excel Data in Power BI (Boniface Muchendu)
note_type: workflow
tags: [power-bi, oauth2, authentication, sharepoint, organisational-account, credentials, power-bi-service]
---

# Power BI OAuth2 Org Account Authentication

Configuring OAuth2 authentication with an organisational account for SharePoint Online data sources in Power BI Desktop and Power BI Service.

## Authentication Flow

```
User → Azure AD (Organisational Account) → SharePoint Online → Power BI
```

OAuth2 is an Azure Active Directory (Azure AD) token-based authentication — the user's identity is passed to SharePoint without storing a password in Power BI.

## Power BI Desktop: Initial Authentication

1. **Get Data** → select data source type (Web for SharePoint files)
2. At the authentication prompt, select **Organizational account**
3. Click **Sign in**
4. Enter credentials for the Azure AD account that has SharePoint access
5. Power BI receives an OAuth token from Azure AD and uses it to access SharePoint

## Power BI Service: Re-Authenticate Dataset

After publishing from Power BI Desktop, the dataset in Power BI Service requires its own authentication:

1. Navigate to the workspace → find the dataset → click **ellipsis (⋯)** → **Settings**
2. Expand **Data source credentials**
3. If credentials are missing/warning → click **Edit credentials**
4. Select **OAuth2** as the authentication method
5. Set **Privacy level** to **Organizational**
6. Click **Sign in** and authenticate with the same organisational account

## Privacy Level: Organizational

| Setting | Meaning |
|---------|---------|
| Organizational | Data can be combined with other sources within the same organisation |
| Private | Data can only be used in isolation |
| Public | No restrictions (not recommended) |

For SharePoint Online → Power BI, **Organizational** is required.

## OAuth2 vs Other Auth Methods

| Method | Use case | Supports refresh |
|--------|---------|----------------|
| OAuth2 (Organisational) | SharePoint Online, Microsoft 365, Azure AD sources | ✓ Full refresh |
| Windows (Basic) | On-premises sources | Requires gateway |
| Anonymous | Public web sources | ✓ Limited |
| API Key | Web APIs | ✓ Varies |

## Credential Expiry and Renewal

- OAuth2 tokens expire — Power BI Service auto-renews them as long as the account has access
- If the user loses SharePoint access (removed from site), the dataset refresh fails
- Best practice: use a service account (not a personal user account) for shared datasets

## Troubleshooting Auth Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Credentials are missing" warning | Dataset not re-authenticated in Power BI Service | Re-enter OAuth2 credentials in dataset settings |
| 403 Forbidden on refresh | User lost SharePoint access | Re-grant access or switch to a service account |
| Privacy level error | Mixing Public/Private/Org sources | Set all SharePoint sources to Organizational |

## Related

- [[SharePoint-Excel-Web-Connector-Power-BI]]
- [[Power-BI-Auto-Refresh-Schedule-SharePoint]]
