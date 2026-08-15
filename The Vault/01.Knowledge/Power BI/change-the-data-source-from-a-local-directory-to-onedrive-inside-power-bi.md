---
title: "Change the data source from a local directory to OneDrive inside Power BI"
source: "https://www.flip-design.de/?p=1285"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Change the data source from a local directory to OneDrive inside Power BI | flip-it.de :: SQL, BI and more In the past, some customers asked me, how can I change the path for a local, imported file, to a path which can be refreshed by Power BI Online. You have two options, you can install a Power BI Data Gateway or you can move your data to online storage, like OneDrive. The first one should be managed by your IT department, so I think the OneDrive solution is much easier. But let us start at the beginning. I imported a local file to my data model. If we look to the Advanced Editor inside Power Query, we see the lo al file connector. So, I uploaded the file to my OneDrive Share. You can grab the connection string from your browser: After that, you can get new data from the SharePoint folder. Now, we get every file which is stored inside the OneDrive folder. After clicking “Transform Data”, we can filter our file by the folder and/or filename. Now, navigate to the Advanced Editor and copy the whole M code. After copying the code, we can paste it to our original query and delete the new query. Now, we can upload the report to Power BI and configure the automatic refresh. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1285)*
