---
created: 2026-08-06
updated: 2026-08-06
source: Calculation Groups in Power BI
note_type: reference
tags: [calculation-groups, tabular-editor, dax-studio, alm-toolkit, external-tools]
---

# Calculation Group External Tools

Quick reference for the three external tools required for working with Calculation Groups in Power BI.

## Quick Reference

### Tabular Editor

| | |
|---|---|
| **Purpose** | Create and manage Calculation Groups and Calculation Items |
| **Download** | https://tabulareditor.com/downloads |
| **Cost** | Free |
| **Access in Power BI** | External Tools ribbon tab (auto-appears after install) |

Tabular Editor connects directly to the active Power BI model. It is the primary tool for creating Calculation Groups.

### DAX Studio

| | |
|---|---|
| **Purpose** | Query, analyse, and debug DAX expressions |
| **Download** | https://daxstudio.org/downloads/ |
| **Cost** | Free |
| **Access in Power BI** | External Tools ribbon tab |

DAX Studio is useful for testing and validating the DAX expressions used inside Calculation Items before deploying them.

### ALM Toolkit

| | |
|---|---|
| **Purpose** | Compare and deploy Tabular models between environments |
| **Download** | http://alm-toolkit.com/ |
| **Cost** | Free |
| **Access in Power BI** | External Tools ribbon tab |

ALM Toolkit can deploy Calculation Groups from one PBIX file to another — useful for promoting them across dev/staging/prod environments.

## Version Compatibility

All three tools must be compatible with the version of Analysis Services (the engine inside Power BI) that is running the model. If tools do not appear in the External Tools tab after installation, check that the installed versions match the Power BI Desktop version.

## Notes

- After installing any external tool, close and reopen Power BI Desktop for it to appear in the External Tools tab.
- Tabular Editor is the only tool **required** to create Calculation Groups. DAX Studio and ALM Toolkit are recommended but optional.
- All three tools connect directly to the in-memory model — no gateway or deployment required.

## Related

- [[Create-a-Calculation-Group]] — step-by-step workflow using Tabular Editor
- [[Calculation-Groups]] — concept overview
- [[SELECTEDMEASURE]] — the function used inside Calculation Items
