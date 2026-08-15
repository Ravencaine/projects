---
title: "Power BI — dataflows"
source: "https://medium.com/@michalmolka/power-bi-dataflows-af3865131436"
author:
  - "[[Michal Molka]]"
published: 2021-08-06
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

The Power BI Service allows you to create ETL processes using dataflows with a well-known Power Query editor.

Here is a short example.

Go to a workspace, select **NEW** -> **Dataflow**.

![](https://miro.medium.com/v2/resize:fit:1182/format:webp/1*bYv6rva8v-CJBay23vEtPg.png)

Add a **New Entity**. You can find a lot of connectors here. We choose an Azure SQL database.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*T_xqm4yyCek7Q-g4bqT2_A.png)

Enter your credentials and select tables.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BHJcFYnyOM3OQvlHRQi6ig.png)

As you can see, you can make transformations in the Power Query editor.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sz4qrgGWKKwND1XpiemUhg.png)

I’ve made a few changes, you can review details in the M editor.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oVTTts7pdinZl2MqxAarfg.png)

Our data flow is ready.

You can configure an incremental refresh, a schedule refresh, etc.

![](https://miro.medium.com/v2/resize:fit:1236/format:webp/1*crbvkevXpFZOG1zuFIVp1w.png)

You can build reports based on them….

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*6kgvpgBtWYgn7OYqDo1xDw.png)

…link tables from another dataflows or reference in datasets.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*h5K1a2i1_jbPbqy8jVs03Q.png)

Using dataflows we are able to build more complex flows. A user can divide transformations by a type, a topic, a domain, etc.; simply by placing a particular group inside a separate entity. Team members don’t have to request every change and wait for a Data engineering team.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Kkd7q_jXko-av5b5unvoqg.png)

Nevertheless, if you work with a large amount of data and want to implement many transformations. Consider to use a dedicated tool like Databricks, a SQL engine or Azure Data Factory. Performance is better.