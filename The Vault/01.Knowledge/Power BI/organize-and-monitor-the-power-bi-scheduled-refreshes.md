---
title: "Organize and monitor the Power BI scheduled refreshes."
source: "https://www.flip-design.de/?p=921"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Organize and monitor the Power BI scheduled refreshes. | flip-it.de :: SQL, BI and more With Power BI you can set up a scheduled refresh of any dataset which have an accessible data source. But you must be aware of, how many refreshes are at the same time. With every particular capacity you have only limited parallel refreshing resources. So, you can only refresh one dataset at the same time when you use an A1 capacity, up to 24 datasets when you use an P3 or A6. To manage this, it can be very hard, because it is mostly impossible to overview every workspace and if your users manage this, it is impossible! Source: Admin in a Day, Microsoft Source: Admin in a Day, Microsoft But you can create an overview with the Power BI REST API by using PowerShell. In my example I created a workspace named “Test” with two datasets which have configured a scheduled refresh. The following PowerShell script calls the REST API and filters all workspaces and datasets in you tenant by a configured scheduled refresh. The data from the following script will be written into a CSV file. The days and times which are configured to each dataset will be written comma delimited into one column. This can be split off with Power Query by using “Split into Columns/Rows”. I think this easier as writing one row for each day. After creating the Dataset with Power BI Desktop, you can analyze the configured refreshes and check how many are at the same time and reconfigure some datasets. You can automate this with Azure Function Apps and write this file into a Blob Store to get automatically Power BI reports with actual data on you tenant. Also, it should be a good idea to get the refreshing duration of each dataset into this report to organize this a little bit better. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=921)*
