---
created: 2026-08-15
source: "7 Powerful Ways to Share Your Power BI Reports Effectively.md"
source_url: https://medium.com/write-a-catalyst/7-powerful-ways-to-share-your-power-bi-reports-effectively-bbb33afe301f
note_type: gotcha
tags: [power-bi, sharing, security, publish-to-web, gotcha]
---

# Publish to Web — Anyone with the Link Can View

<!-- The "anyone with the URL can see it" failure mode that turns internal dashboards into public data leaks -->

## Expected Behaviour

When you share a Power BI report, you'd expect some form of authentication: a sign-in, an audit trail, a way to revoke access. Especially for a corporate BI platform, you'd reasonably assume that "share" implies "share with specific people".

## Actual Behaviour

**Power BI's "Publish to web" feature generates a public URL and an `<iframe>` snippet with no authentication whatsoever.** Anyone — anywhere — who has the URL or the embed snippet can open the report. There is no sign-in, no token, no audit log of who viewed it, and no way to selectively restrict access once it's published.

The URL is also indexable by search engines if it appears on a public web page, which means a misconfigured Publish-to-Web can leak business data into Google results.

## Why It Happens

Publish to Web was designed for an explicit use case: a community blogger or open-data steward wants to share a non-sensitive dashboard with the world. The feature optimises for that scenario (zero friction, embed-anywhere) without any safety belt for the other 90% of cases where the report contains things the author didn't realise were sensitive.

It is easy to find in the Service UI (`File → Publish to web`), has minimal warning, and requires no admin approval by default.

## How to Handle It

1. **Treat Publish to Web as a public broadcast.** Before using it, audit every column and visual in the report for: customer names, employee IDs, financial figures, internal metrics, anything under NDA or compliance (GDPR, HIPAA, SOX, PCI).
2. **Use it only for genuinely public data** — public datasets, marketing dashboards built on public inputs, community samples.
3. **Prefer an authenticated channel when in doubt:**
   - Internal colleagues → [[share-via-power-bi-service-workspace-or-app.md]] or [[share-power-bi-report-link-with-access-permissions.md]]
   - External partners → [[share-power-bi-report-external-users-b2b.md]]
   - Inside your own product → [[embed-power-bi-report-website-or-app.md]]
4. **Revoke when no longer needed.** File menu → Publish to web → **Remove** invalidates the embed immediately.
5. **Tenant admin guardrail:** in the Power BI admin portal, disable "Publish to web" tenant-wide or restrict it to specific security groups. This is the single most effective mitigation against accidental leaks.

## Related Gotchas

- [[pdf-powerpoint-export-loses-interactivity.md]] — the other "default-easy-but-trades-away-something" gotcha on the same article's sharing channel list
- (none yet in vault — add here when more are documented)