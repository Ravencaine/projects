---
created: 2026-07-27
source: "Perspectives and Personalization in Power BI"
source_url: https://medium.com/@2020ec0712/perspectives-and-personalization-in-power-bi-ba0c3fc545e5
note_type: source
tags: [power-bi]
---

(Article for beginners)


Perspectives and personalization are two powerful features in Power BI that allow report viewers in Power BI service to customize report experiences according to their needs, without depending entirely on the developer or the report author. In this article, we will look into how they work in detail. An important thing to note is that — Personalization and Perspectives are **not security mechanisms like RLS and OLS**. They are just meant to improve usability and **provide a better end-user experience**.

**Personalization \[It is related to visuals\]:**

Personalization allows report viewers to **customize visuals** according to their needs in **Power BI service**. You might be wondering — isn’t editing reports already a common thing that people do in Power BI service? Yes, but what makes personalization different is that the viewer with whom the report has been shared by the report author, **doesn’t need** **edit permission** on the report. Plus, editing a report can permanently modify the original version. Personalization does not permanently change the original report. They can explore data in many ways without leaving the report reading view and choose to save the personalization for later. If the report author has enabled the **‘Personalize this visual’** feature already, the viewer can personalize the report.

Some modifications that viewers can do to the reports:  
✓ Change the visualization type:


From a Stacked Column Chart, we can change it to (say) a line chart

✓ Swap out a measure or dimension:


We can use Gross Sales column instead of Units Sold

✓ Add or remove a legend:


✓ Compare two or more measures:


✓ Change aggregations:


We can change the aggregation of a numerical column from (say) sum to average

✓ Change the placement of fields:


We can change the order in which the columns occur in a table


We can move a field from legend to axis or interchange columns between axes

Some exploration features that users can use:  
✓ Capture their changes:


Personalize the visuals and save it as a personal bookmark (visible only to you)

✓ Share their changes:


With reshare permissions, when you share the report with a colleague, you can choose to include the personalization changes that you made. This does not overwrite the author’s version. If the colleague has editing permissions, they can save your personalized version as a new report.

✓ Reset all changes for the report:


Click on Reset to default button to undo all changes in the report and set it back to the author’s last saved view of the report

✓ Reset all changes for the visual:


Click on Reset this visual to remove all your changes to a particular visual and set it back to the author’s last saved view of that visual.

✓ Clear out recent changes:


Click on the eraser icon to clear all changes since you opened the Personalize pane.

Remember, the personalization done to a report **does not get saved automatically**. The report viewer has to save it as a bookmark to capture the changes. Also, when personalize visuals is enabled for a report, by default all visuals can be personalized. You can switch the setting on or off for individual pages or visuals. The report author must enable personalization in Power BI desktop before publishing the report to Power BI service.

**Perspectives \[It is related to the model\]:**

Perspectives can be used to **choose a subset of a model** to provide a more **focused view**. This is especially useful when working with very large data models that have numerous columns and measures. A smaller, focused field list makes report exploration easier and less overwhelming for end users. It is essential to know that they do not reduce the size of the model. **All security is inherited from the underlying model**.

**Important points to note:**  
• To use perspectives, you must enable personalize visuals.  
• You need Tabular Editor for creating perspectives.  
• The created perspective can only be applied to an entire page or to all pages in the report — not to individual visuals in a report.  
• Before deleting a perspective from a model, make sure to check that the perspective isn’t used in the personalize visuals.  
• This feature is not supported for publish to web.  
• Users cannot toggle between different perspectives in the Service; they only see the one assigned to the page by the author.


A perspective created as a subset of the data model for use in the report

Here is how to create a perspective in Power BI desktop, for use in Power BI service —  
1) Open the PBIX file -> External tools -> Tabular Editor -> Perspectives -> Create -> Perspective.  
2) Go to those tables and columns that you want to add to perspectives and right click on them -> Show in perspectives -> choose the perspective.  
3) Once you have added all the required columns or tables to the perspectives of your choice, save it to your model in Tabular Editor.


Now, when we open the report and go to the format pane of the page, an option called ‘Personalize visual’ appears. Turn it on and choose the perspective from the dropdown that you want to enable for that page. After you set the Perspective for the report page, the Personalize visuals experience for that page is filtered to the selected Perspective. You may choose to apply your perspective setting to all the pages too.


**Security in Perspectives:**

Row Level Security (RLS) — With perspectives used in a page, when a logged in user has certain restrictions on the dataset for his/her role, the same restrictions apply to the perspective. Hence, the data seen in the visuals for that role is a filtered one, based on the rules specific to that role to which the user belongs.

Object Level Security (OLS) — When a table is hidden for a role using OLS and the same table is included in a perspective, the table and its columns are visible to that role in service, within that perspective. But upon adding a column from that table to the visual, the visual breaks, indicating that the OLS is preventing access to that table for the user. Similar behavior is observed for OLS applied on individual columns in a table, instead of the entire table.

*Sources: Microsoft Learn*