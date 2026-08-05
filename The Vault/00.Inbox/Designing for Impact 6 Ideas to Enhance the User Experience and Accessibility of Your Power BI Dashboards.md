---
title: "Designing for Impact: 6 Ideas to Enhance the User Experience and Accessibility of Your Power BI Dashboards"
source: "https://medium.com/the-bi-corner/designing-for-impact-6-ideas-to-enhance-the-user-experience-and-accessibility-of-your-power-bi-a3096742d9eb"
author:
  - "[[Isabelle Bittar]]"
published: 2024-03-02
created: 2026-08-03
description: "A Journey Through the Design of an Equity, Diversity and Inclusion Power BI Dashboard"
Processed: "Unprocessed"
---
## A Journey Through the Design of an Equity, Diversity and Inclusion Power BI Dashboard

![](99.System/Attachments/1!cJ9qZauW-vDwz200yHOlzg.png.webp)

By Isabelle Bittar for KI Data Science

🎁 *Figma file available at the end of this article!*

### Introduction

In some of my recent articles, I’ve introduced using Figma in designing Power BI reports. In this article, I wanted to take a step back and share some design ideas I consider when sketching these views for Power BI. Some of these ideas are maybe backed by theory, but it’s mostly all based on my experience working with different types of clients. Equally, some of the stuff might even go against commonly accepted principals, but I think that if you have been following me by now, you’ve probably noticed I enjoy working in these grey areas and pushing the limits of what we can develop in Power BI 😅.

### Case Study: Equity, Diversity and Inclusion Dashboard

To navigate this article, I will use the dashboard displayed as cover image to illustrate these different ideas. This dashboard focuses on reporting on overall Equity, Diversity and Inclusion (EDI) organizational performance from diverse roadmap initiatives. It’s a fictitious example, but the design is based on my experience working on many of these projects, especially in 2021 and 2022.

It’s a subject I am super passionate about and I think most will agree that EDI is extremely important for our economic and social development, and this, across the world. Unfortunately, I’ve noticed a slowdown in these EDI analytics projects. Maybe this can also (re?)-spark some interest and excitement around the topic! 🤩

With this, let’s get started with the design ideas 🙂.

### 1\. Designing for End-Users That Don’t Know Power BI

If there is one thing that is important to keep in mind it’s your end user. Whenever you are designing and developing analytical products, we are doing it for the end-user, not:

❌ the client that’s sponsoring the project

❌the project manager tracking your progress

❌the other Power BI developers that will be maintaining your report

…the end-user 🤩! In my experience, the end-users I work with aren’t always very familiar with Power BI. It’s sometimes even their first report! More often than not, they expect our reports to behave the same way as their professional applications or websites.

It means we need to keep **report navigation** and **user-actions** simple and obvious.

**👆 How do you make report navigation simple?**

- **Content Hierarchy**: Creating a content hierarchy is important properly plan your dashboard. I find it helpful to initially list out the information I want the dashboard to contain in groupings, such as in the following content hierarchy:
![](99.System/Attachments/1!GTlHYSz2XtiZD-Km6c62Gw.png.webp)

Information Structure for the EDI Dashboard

When I start designing the dashboard, having this type of information structure helps. Then, to help instruct the user on the content hierarchy of the dashboard, I like to leverage the navigation panel to showcase the different report pages:

![](99.System/Attachments/1!48w7GdKgFZvM-TBm1V425w.png.webp)

Navigation Panel of the EDI Dashboard

- **Summarize the Most Important Information**: I like creating a summary/overview page to my dashboards that summarizes the key takeaways from the dashboard, with buttons that direct users to view more detailed information on a specific subject or metric. I also like to integrate alerts, such as illustrated by the button displayed by the notification button on the top right of the dashboard.
![](99.System/Attachments/1!OmSaaYly9scZgSRl20yEYw.png.webp)

Alerts of the EDI Dashboard

Integrating alerts can help orient user’s attention to things that are more critical and that should require their intervention. I wrote the following article on how you can integrate this type of functionality in your Power BI reports here:

## [Alerts in Action: Powering Real-Time Insights by Integrating Custom Alerts in Power BI](https://medium.com/microsoft-power-bi/alerts-in-action-powering-real-time-insights-by-integrating-custom-alerts-in-power-bi-417251524e7c?source=post_page-----a3096742d9eb---------------------------------------)

### Leveraging Visualization to Unlock Actionable Insights

medium.com

- **Integrate Tutorials or Information Views**: Incorporating tutorials or explanatory views within the dashboard can significantly enhance user comprehension and engagement. These elements can be designed as pop-ups, embedded videos, or info icons that, when clicked, provide brief tutorials on how to use the dashboard effectively. I’ve recently wrote an article on how you can create an interactive tutorial in your Power BI reports:

## [Building Interactive Tutorials That Stick in Power BI](https://medium.com/microsoft-power-bi/power-bi-unleashed-building-interactive-tutorials-that-stick-95f97da8eef0?source=post_page-----a3096742d9eb---------------------------------------)

### In It to Win It 🤠: Part 3 of Participating in the FP20 Analytics Challenge on Data-Driven Education Management

medium.com

- **Centralize User Actions Within a Tool Bar**: Positioning all primary user actions within a single toolbar simplifies interaction with the report. I like to think that this approach streamlines the user experience by centralizing essential functions like filtering and searching in one intuitive location. For the EDI dashboard, the toolbar is place at the top right of the dashboard where user can apply filters and check notifications/alerts.
![](99.System/Attachments/1!HHtaeQVk_bo2PbX-ske2bw.png.webp)

Toolbar of the EDI Dashboard

**👥 How do you make user-actions simple and obvious?**

I try to make user actions as simple as possible. For example, most end-users of my projects don’t know how to use drill-downs so I avoid them and try to give them the option of viewing their data differently by selecting from a drop-down slicer instead.

![](99.System/Attachments/1!eQUFCo-ipnzc_7DWfH07Ig.png.webp)

Drop-Down Slicer Example

However, when I do use drill-downs or other features that aren’t as obvious for non-familiar Power BI users, I add additionnal instructions directly in the view to support them. For example, in the following dashboard, I added instructions on the graph’s drill-down feature at the bottom right.

![](99.System/Attachments/1!j7Jjim3T_dcFhoDh_eDsaQ.png.webp)

By Isabelle Bittar for KI Data Science

### 2\. Designing for End-Users That Aren’t Data-Savvy

While I strive to integrate modern aesthetic and contemporary design trends in my dashboard, I prioritize the selection of simple data visualizations, such as bar/line charts, KPI cards, and tables. This choice stems from a commitment to ensure that the reports are accessible and comprehensible to end-users who may not be well-versed in data analysis. I consciously avoid the temptation to utilize some of the more complex or “cool” visualizations available in Power BI, recognizing that such elements, while visually striking, can often obscure the information they’re meant to convey to those not familiar with intricate data representations.

For example, Power BI recently released the feature to overlay the columns of charts and I’ve been seeing stuff like this online, which, as a Power BI report developer, I find very cool!:

![](99.System/Attachments/1!-APyP2yYuj96PDMlCSubJw.png.webp)

But I know my HR colleagues would be like: WHAT?

Side note, these type of charts I am seeing all over LinkedIn this month make me think of a bar chart I was trying to create when I was learning Python. Here was a screenshot I had sent to one of my friends to laugh about my attempts, hope it can make you laugh (or smile) too 😅:

![](99.System/Attachments/1!X2bLoB0m7o6uweaQCGEFrA.png.webp)

Failing at Making Bar Charts in Python

Yes, I’ve received feedback that some of my projects diverge significantly from what is typically expected of Power BI reports, sometimes even bypassing a range of native features. This departure is intentional and, admittedly, can lead to additional maintenance challenges when updates or modifications to the report are necessary. However, this approach is a deliberate choice to prioritize the user experience above all. By simplifying the visual language of the reports, I aim to demystify data and make it as accessible and actionable as possible for all users, regardless of their data literacy levels.

This focus on user-centric design acknowledges that the ultimate value of a report lies in its ability to communicate insights clearly and effectively, not in its adherence to the latest graphical trends or its use of sophisticated features for their own sake. It’s a balance between form and function, where the goal is to empower end-users with the information they need in the most straightforward and intuitive manner. At the end of the day, ensuring that the reports serve their intended purpose for the target audience for me justifies the extra effort and challenges involved in their creation and maintenance. This approach not only enhances the accessibility of data but also fosters a more inclusive environment where decisions are informed by insights understandable to everyone involved. I talk more about designing for accessibility in the last section of this article.

### 3\. Container Over Content

The star of your Power BI dashboard will always be your content. However, to make sure it is effectively communicating the right insights to your audience, I think it’s normal to spend more time defining the container/layout of your report than working with the actual data. An effective dashboard layout is not just about the placement of elements but about creating an intuitive and user-friendly experience that guides the user through data insights efficiently. Here’s a deeper dive into some of the key components previously mentioned and how they can be used to optimize the users’ experience:

- **The Navigation Menu**:
![](99.System/Attachments/1!48w7GdKgFZvM-TBm1V425w.png.webp)

Navigation Menu of the EDI Dashboard

Traditionally positioned on the left side for easy access, the navigation menu is pivotal for dashboard orientation. However, the trend towards top-positioned or icon-triggered menus, similar to those found in web applications, reflects a move towards more flexible and space-efficient layouts. In the report template, placing it on the left side offers familiarity, but exploring alternative placements can enhance usability and aesthetic appeal, especially for users familiar with modern web navigation patterns.

![](99.System/Attachments/1!nCJ71NffpTbjdNSuEbjjyA.png.webp)

Example of a Top-Positionned Menu by Yoga Satria for Odama

![](99.System/Attachments/0!6pq_HUv83-DoE8TO.webp)

Example of an Icon Triggered by Bogdan Falin for QClay

- **Support Tools for Users**:
![](99.System/Attachments/1!r2aWf_6g1gHT2HYFtLb8SA.png.webp)

Support Tools of the EDI Dashboard

Including support tools such as tutorials, FAQs, and contact links directly within the dashboard is crucial for user autonomy and satisfaction. These elements should be easily accessible, like through a dedicated ‘Help’ section or icons that do not clutter the main interface. Providing these resources empowers users to resolve queries independently and enhances their overall experience.

- **The Filter (Read: Slicer) Panel**:
![](99.System/Attachments/1!ZYZxQhvs3uF3Tw58Z9SAOQ.png.webp)

Filter Panel of the EDI Dashboard

Filters or slicers can be essentials to your users for them to interact with the dashboard and drill down into specific data points. Positioning the filter panel in a consistent and accessible location, such as alongside or above the main content area, ensures users can easily modify views without losing context. I enjoy using collapsible panels to maximize space and maintain a clean layout. I wrote the following article on how you can achieve this in Power BI here:

## [Streamline Data Exploration with a Custom Slicer/Filter Pane in Power BI](https://isabittar.medium.com/streamline-data-exploration-with-a-custom-slicer-filter-pane-in-power-bi-fce4c109aaa0?source=post_page-----a3096742d9eb---------------------------------------)

### Simplify Filtering Options and Enhance User Experience in Your Reports

isabittar.medium.com

- **The KPIs:**
![](99.System/Attachments/1!gPyu9CdFgdBwf6EmUbslOw.png.webp)

KPIs of the EDI Dashboard

Key Performance Indicators (KPIs) should be the focal point of any dashboard, prominently displayed and immediately visible upon first glance. Designing a distinct area for KPIs, possibly at the top or center of the layout, ensures they capture attention. Utilizing visual hierarchies, such as size and color, can further emphasize their importance.

- **Other Key Visualizations**:
![](99.System/Attachments/1!CCdbJ-lObU12WH6k9xkF7w.png.webp)

Other Key Visualizations of the EDI Dashboard

Beyond KPIs, include other critical visualizations that support the data narrative. These should be arranged logically around the KPIs, guiding the user’s eye through the data story in a coherent sequence. Consider grouping related visualizations to facilitate understanding and comparison.

When planning a dashboard layout, the goal is to balance the desire for comprehensive data access with the need for clarity and simplicity. By thoughtfully organizing the navigation menu, support tools, filter panel, KPIs, and other visualizations, you create an environment that not only informs but also engages and empowers users. Remember, the effectiveness of a dashboard is not just in the data it presents, but in how easily and quickly users can find and interpret that data.

### 4\. Less is Less and More is More: Finding the Right Balance While Maximizing White (Blank) Space

Users don’t believe in “less is more” when it comes to the information they want in their Power BI reports 😂. However, the real challenge isn’t about how much information you show, but how you organize and display it. By arranging content so the most important information stands out and making other details easy to find but not in the way, you can keep your Power BI report pages clear and not too crowded with charts and tables.

When developing dashboards, I try to make sure to highlight the main points I want everyone to see right away. I add buttons for “details” that let users click to see more if they’re interested. This way, the first thing people see is simple and focuses on the key info, but they can easily dig deeper if they want. This method helps tell a better story with the data without making it too much to take in all at once. It also helps make the layout cleaner, with more empty space, which makes everything easier to read and makes the whole experience better for the user.

![](99.System/Attachments/1!2OM3hcNS9rTXGa_FQmxDWQ.png.webp)

Detail Buttons for Further Exploration

Using smart design to group information well and use empty space wisely doesn’t mean you’re giving less information. It means making a dashboard that’s easier and more enjoyable to use, highlighting the most important points while still giving access to more details when needed. This balanced way of doing things makes dashboards not just full of data but also user-friendly, helping people understand the data better and make decisions more easily.

### 5\. Riding the Wave of Design Trends: Beyond the Dashboard

Staying updated with the newest styles in website and mobile app design is very important. This is because the popular designs we see in apps today shape what people expect from other things they use, like dashboards and Power BI reports. The idea here is that when people are used to a certain look and feel in the apps they use every day, they expect a similar navigation experience in their reports or dashboard. So, making sure the design of dashboards and reports matches what’s trendy in web and app design is key to making users happy and giving them a good experience.

Some notable design trends include:

- **Light Mode Comeback**: Despite the popularity of dark mode among many users (🙋♀️), light mode has seen a resurgence. It is now widely embraced for design, offering a clean and vibrant alternative to the sleek appeal of dark themes. This shift suggests a balanced approach to theme selection, catering to user preferences for both light and dark modes.
![](99.System/Attachments/1!nPT8SEz5H6IbDz4HDi3-Yg.png.webp)

Dark Mode Example by Vitalina Vykhrystiuk for Fireart Studio and Light Mode Example by Shayan Umar Creative Ind Design

- **Designing for All Types of Devices**: Modern reports need to be versatile, capable of being displayed effectively across a range of devices — from desktop computers and laptops to large boardroom screens and handheld smartphones. This trend underscores the importance of responsive design, ensuring that reports are accessible, readable, and navigable regardless of the screen size or device type.
- **Bold Typography**: Embracing bold typography is not just about making a statement; it’s about improving readability and drawing attention to key information. I don’t know if you have also noticed, but in the past 2 years, lighther fonts have been increasingly replaced by bold fonts across different user applications.
- **Micro-Interactions**: Micro-interactions are subtle design elements that enhance user experience through feedback or visual cues. These include any animations to charts, visualizations, buttons you can add to catch the user’s attention. These actions make reports more interactive and responsive, providing users with immediate feedback on their actions and making the data exploration process a bit more dynamic and engaging.
- **Expanding Color Palettes**: The use of color in design is evolving, with palettes becoming more diverse and vibrant. The color of year for 2024 was declared as peach fuzz by Pantone. Yes, I agree this is a tough shade to work with, but these are the types of colors we will see increasingly across different user applications.
![](99.System/Attachments/1!eXitkwHhS5EnrzZQfqEWFA.png.webp)

Peach Fuzz by Pantone

By integrating these modern design trends into dashboard and Power BI report design, we can create more effective, user-friendly, and visually appealing reports. This approach not only enhances the user experience but also ensures that our reports remain relevant and engaging in the ever-evolving landscape of digital design.

### 6\. Designing for Vulnerability

You might be familiar with the concept of designing for accessibility, which focuses on ensuring that products, services, and environments are usable by people with a wide range of abilities, including those with disabilities. Designing for vulnerability takes things a step further by not only addressing physical and digital accessibility but also considering the emotional, psychological, and situational vulnerabilities of users. This approach involves understanding and empathizing with the challenges and barriers that individuals may face due to diverse factors.

Great concept, but how do we tie this to our Power BI dashboards? Here is an example of my interpretation of this concept:

Sometimes, when displaying performance information, the way things are presented can create political tension between different teams within an organization. For example, in this dashboard, showing information on program performance and activity roadmap could lead users to believe that the resources in charge of the roadmap activities linked to different initiatives are responsible for the overall program performance, but that’s usually not the case. Therefore, it was a design choice to remove the clear link between the program names and program workstreams to avoid making that association. I’m sure there is a tone of other examples you might have witnessed where showing some information can cause more harm than good.

I’m sure there is a tone of other examples you might have witnessed where showing some information can cause more harm than good. I personally think that it’s important to keep these senstivities in mind because I’ve seen projects where they were ignored, and the dashboard or analytical product was not championed as much as it could have been in the organization and ended up not being exploited to its full potential.

### Conclusion

In conclusion, here were a few design ideas I wanted to share with you that can hopefully be helpful for your next dashboard development project! Some of these ideas may go against some principles you are familiar with and I would love to know what you think! 🙂

As well, if you have any suggestion on subjects you would like me to cover in the future, please let me know! Thank you so much for your readership! 🤗

**🎁** [**Here**](https://www.figma.com/file/dQAIh0lcMxpH2SPKYsr9iw/Power-BI-Dashboard-Template?type=design&node-id=0%3A1&mode=design&t=xEQ0gqddPJnxVv9P-1) **is the Figma file of the EDI Dashboard!**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X (Formerly Twitter)***](https://twitter.com/KI_Datascience)