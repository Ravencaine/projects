---
title: "Update parameters inside a Power BI semantic model using PowerShell"
source: "https://www.flip-design.de/?p=1563"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Update parameters inside a Power BI semantic model using PowerShell | flip-it.de :: SQL, BI and more In this article, I will briefly show how to update parameters inside a Power BI semantic model using PowerShell. Typically, in Microsoft Fabric, deployment pipelines are used to handle this when a semantic model is promoted from one workspace to another. However, many organizations do not have access to Power BI Premium or Microsoft Fabric, but still need to update parameters such as the SQL server name or database name. In such cases, a PowerShell script is a practical and effective solution. A key prerequisite is that the semantic model is designed in a way that the server and database names are controlled via Power Query parameters. Once this is in place, these parameters can be modified after deployment directly through the Power BI Service or automated using PowerShell. These settings can be updated quite easily using PowerShell. The following script can be used to adjust the parameter values accordingly. After executing this script, the parameters in the Power BI Service web interface will appear as shown below. In upcoming posts, I will demonstrate how gateway connections can also be updated and managed using PowerShell. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1563)*
