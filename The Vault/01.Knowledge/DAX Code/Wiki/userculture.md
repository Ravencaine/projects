---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# USERCULTURE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the locale (language code-country code) for the current user, determined by the

## Syntax

```dax
USERCULTURE()
```

## Remarks

In the Power BI service, locale is determined by Settings > Language > Language Settings. The default is determined by the user's browser language setting. When used in calculated table and calculated column expressions, the result may differ depending on whether the table is in DirectQuery or Import mode. When in DirectQuery mode, the result is determined by the language (locale) specified in Language Settings in the Power BI service. The default in Language Settings specifies locale is determined by the user's browser language setting, which means the same calculated table or column can retu