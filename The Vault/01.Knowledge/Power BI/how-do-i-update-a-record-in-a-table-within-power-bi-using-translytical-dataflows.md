---
title: "How do I update a record in a table within Power BI using Translytical Dataflows"
source: "https://www.flip-design.de/?p=1498"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

How do I update a record in a table within Power BI using Translytical Dataflows | flip-it.de :: SQL, BI and more In this post, I’d like to provide an update to the following post: https://www.flip-design.de/?p=1480 . In that post, I didn’t describe how, for example, to use a key figure to select the corresponding data record from a table and pass it on to an update. To achieve this, I first inserted the data records from the table into a Power BI table. Then I created a corresponding key figure using the following code: Here, I return the unique identifier of the selected record. This key figure can then be used as described: The corresponding record ID can then be used in the Python function as before to update the record. The record can now be accessed when executing the dataflow. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1498)*
