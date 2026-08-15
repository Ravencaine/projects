---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: atomic
tags: [dax, udf, power-bi, compatibility, tmdl]
---

# DAX UDFs Require Compatibility Level 1702+

UDFs are only available on database **compatibility level 1702 or higher**. Attempting to define a UDF on a model below this level causes the FUNCTION block to fail with no obvious error message.

## How to Check

In Power BI Desktop: File → Options → Current File → Semantic Model Settings → Advanced → Compatibility Level.

Or via Tabular Editor, SSMS, or XMLA query.

## The Silent Failure

On an older model, the DEFINE FUNCTION block simply fails to parse or deploy. Error messages are not immediately obvious — the first sign is often that the function doesn't appear in Model Explorer or IntelliSense after deployment.

## Migration Path

1. Check current compatibility level
2. Upgrade if below 1702 (Settings → Semantic Model → upgrade)
3. Test UDF deployment in a dev environment first
4. Verify functions appear in Model Explorer after deploy

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
