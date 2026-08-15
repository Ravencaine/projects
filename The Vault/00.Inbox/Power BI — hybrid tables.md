---
title: "Power BI — hybrid tables"
source: "https://medium.com/@michalmolka/power-bi-hybrid-tables-fb043b212fe1"
author:
  - "[[Michal Molka]]"
published: 2023-04-14
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

If you want to speed up your tables refresh process you can partition a table. Then update only partitions where data has been changed. Power BI offers more convenient way to do this process — **Hybrid tables**.

After you imported a table. Set two parameters a **\[RangeStart\]** and a **\[RangeEnd\]**, set both as a Date/time type.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cWt1NXkm9pFHPwLevAEm1A.png)

Set Custom Filter on your column predicate in order to filtering and create partitions. This column has to be a Date/time data type.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aKkze6Ykb7IXnccB4D5zOA.png)

As you see, out table has a following records quantity for respective years.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*e29pOwGdIiO8peywpdkGdA.png)

Go to Incremental Refresh settings.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*84JXRQw3cY5aejtg6ziqvg.png)

Events between 2018 and 2019 are imported and archived — it means that won’t be refreshed during a next refresh processes.

Events between 2020 and 2021 are incrementally refreshed — will be processed during the next refresh processes.

And events from 2022 onwards will be available in a Direct Query mode -if you set **Get the latest data in real time with Direct Query mode**.

If you want the newest data imported then this setup is sufficient.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nwPFnkZ3t-wUCYvd1aP9uw.png)

After the dataset is deployed into Power BI service and initially refreshed then it is automatically partitioned. Let’s check it in the Tabular Editor.

We have five partitions, two for archived data (Import), two for incrementally refreshed data (Import)…

![](https://miro.medium.com/v2/resize:fit:1156/format:webp/1*5fVemxn4NeRRd1kJez4RXw.png)

…and one for live data (Direct Query).

![](https://miro.medium.com/v2/resize:fit:1104/format:webp/1*4SDmUmNojaUI9Jcd7uWSKg.png)