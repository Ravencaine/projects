---
title: "Power BI — RLS, part 1"
source: "https://medium.com/@michalmolka/power-bi-rls-part-1-9d714382ec47"
author:
  - "[[Michal Molka]]"
published: 2021-03-05
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

There are two basic approaches of implementing a **Row Level Security** in Power BI. This post shows how to implement a basic **RLS**.

We will be working on a simple model example. Two tables: a \[**Posts**\] (Fact) and a \[**PostTypes**\] (Dimension).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MKFNmyu0piX_pA59ZB9B_g.png)

The first approach, you can implement the **RLS** directly in Power BI.

1. Pick the **Manage Roles** button on the ribbon,
2. Create a new role,
3. Select a table and a column which you want to filter - the \[**PostTypes**\].\[**Id**\] in this case,
4. Write a DAX statement, **\[Id\] = 1** in this case. This is our filter definition.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5kBgQpAWHkR_YOrLZnHF6w.png)

I have created four roles for better understanding:

1. **PostType Question**: *\[Id\] = 1*, a user is able to see only a post which a PostType\[Id\] is equal to 1,
2. **PostType Answer**: *\[Id\] = 2*, like above, but the Id equals 2,
3. **PostType Wiki**: *\[Id\] in {4,5}*, the Id equals 4 or 5,
4. **PostType All**: *True()*, a user is able to see all the data.

Select a **View as** option and choose a role…

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*K5Vc8NPj5cA3lObsqYhX7g.png)

…the data is filtered.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FI57sHS9wUJ51w0x5E8DbQ.png)

Now, we can upload a report to Power BI service.

Pick a **Security** position for an uploaded dataset.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sQVPkXQ6CUguLpqSXzVn_g.png)

And add users to suitable groups.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Jvx78eog5NFli-9kfV536g.png)

After the report is set. You can log in as Adam Orlowski who is a **PostType Answer** group member.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jFnKauCECfEkvIHaHdzlyA.png)

It is a basic approach. Useful in small projects. There is a second approach; helpful especially when you have a larger amount of recipients. Here is a post: [Power BI — RLS, part 2. Previos post described how to implement… | by Michal Molka | Medium](https://medium.com/p/2ca8f6cbff43)