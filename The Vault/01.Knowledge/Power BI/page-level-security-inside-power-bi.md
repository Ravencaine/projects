---
title: "Page Level Security inside Power BI?"
source: "https://www.flip-design.de/?p=1145"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Page Level Security inside Power BI? | flip-it.de :: SQL, BI and more At my last Q&A sessions at the Power BI summit regarding my sessions about Power BI and security, I got many questions about Page security inside Power BI reports. Natively, the is no option available. The best way, from my point of view, is to embed your report with Power BI Embedded in an App or embed your report to a Power APP or something ales. So, with these options you can hide your pages and give the users only access to the pages, which they need to view. If you hide your pages and your users only able to open them where they allowed to, they can open the pages if they have the URL for the page. The page, or the report section, is only a generated ID by the service. So, if I have access to a page and I bookmark the URL, and now I declined the access, I can refer to this page. The other option is to create different datasets and publish them to different workspaces, it is more secure, but it needs more maintenance. This blog post will show you, how to implement a secure page navigation based on my last blog post: https://www.flip-design.de/?p=1065 I will implement a dynamic Row Level Security by creating a table where I assign the users to the different pages. Now I need to connect the tables by the page attribute Next, you need a role where you filter the table by the username Now, you need to set the relationship to Both and enable the RLS. Now, we are ready to go: Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1145)*
