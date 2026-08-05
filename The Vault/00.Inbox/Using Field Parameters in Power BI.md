---
title: "Using Field Parameters in Power BI"
source: "https://databear.com/field-parameters-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2022-10-22
created: 2026-08-04
description: "The field parameter is an essential feature meant to make work easy. It is easy to toggle between measures and dimensions using a single button."
Processed: "Unprocessed"
---
## Power BI Field Parameters

Recently, Microsoft has added field parameters as a new feature in Power Bi. The field parameter is an essential feature meant to make work easy. It is easy to toggle between measures and dimensions using a single button rather than following complex steps and procedures. In simpler terms, parameters represent variables, while a field represents measures or a table column.

Field parameters will decrease the time spent on developing Power BI reports and improve the flexibility of the entire process. Previously Power BI was using the what-if parameters, which allowed toggling between values; the improved field parameters make it easy to toggle between fields. Now, a feature will make everything easier; however, how do we navigate the field parameter feature in Power BI?

Let’s dive into this;

## How to use the field parameter in Power BI.

### Step 1: Enable the field parameter feature in the preview features of Power BI.

To start your practice and understand field parameters in Power BI, you must have access to this feature. The old version does not have a field parameter as a native feature and thus must be activated from the preview features.

On the top of your home page, click on settings and then navigate to options. This brings you to a page with all the available choices in the options box, which include; data load, power query, direct query diagnostics, and preview features, among others. The preview features avail all the new Power BI features available for you to try. Some of these preview features include; the field parameter feature, sparklines, and error bars, among others. You need to tick the box next to the preview feature to activate it, as shown below.

![Field parameter](99.System/Attachments/Field_parameter.jpg)

From the image above, you can see that I have checked all the preview features that I would want to use in generating reports. To activate and gain the functionality of the preview features, you need to close and restart Power BI.

### Step 2: Create your field parameter.

The field parameter feature is now part of your native features and is ready for use. Let’s jump right into creating our first field parameter.

To begin, you must navigate the dashboard to the modeling ribbon (located at the top of the Power BI dashboard). In the parameter section, a drop-down was previously used to access the what-if parameter. A new interface has two areas: fields and numeric range. The numeric range is similar to the what-if parameter. It allows the user to handle numeric values within a certain range. The field feature is active and ready for use.

![Field parameter location ](99.System/Attachments/Field_parameter_location_.jpg)

To create a field parameter, click on the field option. It is possible to toggle it to the numeric range if you want to. On selecting the field option, you are presented with a name box where you type your desired name for the field parameter.

The parameters option contains several boxes representing fields that you might want to include in your field parameter. You can add the fields by simply checking the boxes or dragging them in your desired order; these fields will appear in the same order in your slicer when you add them to your report.

![Field parameter page Fill](99.System/Attachments/Field_parameter_page_Fill.jpg)

Power BI Desktop creates a field parameter, a new table is concurrently added to your field’s pane on the right side. For instance, we have created a field and named the table Row because it will be toggling between the rows below.

![FLEID parameter ](99.System/Attachments/FLEID_parameter_.png)

Below shows the syntax for creating a field parameter with several rows (six in this case). The right section of the syntax represents the order of fields, and it is possible to sort and alter this arrangement.

![](99.System/Attachments/Field-parameter-page-furmulat.jpg)

I hope you found this helpful. Read more blogs from DataBear [here](https://databear.com/blog/).