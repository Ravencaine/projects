---
title: "Power BI — RLS, part 2"
source: "https://medium.com/@michalmolka/power-bi-rls-part-2-2ca8f6cbff43"
author:
  - "[[Michal Molka]]"
published: 2021-03-19
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

The previous post described how to implement a basic **Row Level Security**. If you need more flexibility you can use an additional permission table.

An exemplary data model has been described in the last post. This example has one difference. An additional table with permissions.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*T-Qowj2tS6cfHiVmR6Ocew.png)

The \[**UserPermission**\]table contains an \[**UserName**\]and a \[**PostTypeId**\]columns. It means that we can dynamically modify or integrate this information from another system.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ehQBIfVTFAJO6YlEd_ibrg.png)

Relationship between the \[**UserPermission**\]and the \[**PostTypes**\]tables needs to be set as a **Bi-directional** and an **Apply security filter in both directions** setting active.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rQVJpteHlyIxOgSZ6Gtm_g.png)

A next step is to apply a role to the \[**UserPermission**\]table. There is only one role and one DAX code for every case/group.

```c
[UserName] = USERPRINCIPALNAME()
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8wIaZrfHQVxgUpMEg8EMaA.png)

The last step is to add a user or a group in the Power BI service portal.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BTZAoSgwVIGmFfYlbzX_hg.png)

There is one question. What is a performance difference between these two approaches?

A \[**Post**\]table contains nearly 50 000 000 records. We use a **Performance Analyzer** to measure a report performance. The report comprises a Matrix visualization which includes three measures (SUM, AVG, COUNTROWS).

The first approach (a basic **RLS**):

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*gvR6RbB1rGfmeqYjLkCByw.png)

172 ms on average.

The second approach (the table based **RLS**):

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*plTvO5hoatA_zJHL3RB_IQ.png)

170 ms on average.

As you see, there is no big difference.