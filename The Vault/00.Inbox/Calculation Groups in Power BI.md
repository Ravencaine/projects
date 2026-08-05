---
title: "Calculation Groups in Power BI"
source: "https://databear.com/calculation-groups-in-power-bi/"
author:
  - "[[Annamarie Van Wyk]]"
published: 2022-05-03
created: 2026-08-04
description: "Reduce the number of measure you create by using Calculation Groups in Power BI. This blog will guide you through to get started."
Processed: "Unprocessed"
---
## What are calculations Groups?

Calculation groups are a collection of items, which are basically the same measures that you create in your report but are created in a slightly different way. Calculation groups are created in Tabular Editor, which you can download for free from the internet. You can see the Tabular Editor in your External Tools. This definition was taken from the [Power BI community](https://community.powerbi.com/t5/Community-Blog/How-And-When-To-Use-Calculation-Groups-In-Power-BI/ba-p/1796197).

In a nutshell for example, if you have Sales, Quantity, Revenue and Cost, and you normally need to add 4 – 5 measures to calculation MTD for each. By using Calculation groups you will only have to create 1 measure and apply it to all.

## What are the benefits?

Reduces the number of measures that one must create.

## What you need to do.

Lets’ dive right into how to create calculation groups, that was the only way I could figure out what they are and how great they are.

For Calculation Groups you will only need Tabular Editor, but I’ll show you which ones are good to have. They are Tabular editor, DAX Studio and ALM Toolkit.

First things first, need to check if you have the external tools tab on your ribbon.

![Ribbon no external tools](99.System/Attachments/Ribbon_no_external_tools.png)

If not, you’ll need to do the following. Download tabular editor, DAX studio and ALM toolkit.

[https://tabulareditor.com/downloads](https://tabulareditor.com/downloads)

[https://daxstudio.org/downloads/](https://daxstudio.org/downloads/)

http://alm-toolkit.com/

After you have installed it, you just close Power BI, open it up again and they will automatically be there. Just an FYI, it needs to be the correct versions, otherwise they don’t appear.

![External tools](99.System/Attachments/External_tools.png)

## Ready to start creating Calculation Groups in Power BI

Open Tabular editor, you will see it is automatically connected to your Power BI model.

Add a table by right clicking and choosing add Calculation group.

![Create new calculation group](99.System/Attachments/Create_new_calculation_group.png)

Then add a Calculation Item by right clicking on Calculation Item and add. Rename to appropriate name. My example is MTD.

![Add calculation Item](99.System/Attachments/Add_calculation_Item.png)

Double click on Calculation Item, and a DAX screen will open. Now you will create the MTD measure as you usually would in DAX except where you would add the “Sales” measure as the DAX Measure to use, you will put in SELECTEDMEASURE(). This is essentially a place holder for any measure you choose.

![Tabular Editor MTD](99.System/Attachments/Tabular_Editor_MTD.png)

Once created, save it and go to your Power BI, hit the refresh, and your new table will appear.

![New Time Intelligence Table](99.System/Attachments/New_Time_Intelligence_Table.png)

Now all you need to do is use in on the report canvas in a visual of your choice. In my example I also added the normal Sales measure, in order to have it in the visual as well. This was just SELECTEDMEASURE(). You can now use any measure, like Sales, Quantity, Profit, Revenue etc.

Video Player  <video width="600" height="442" src="https://databear.com/wp-content/uploads/2022/05/Implementing-Calculation-Groups-Gif-1.mp4?_=1" controls=""><source type="video/mp4" src="https://databear.com/wp-content/uploads/2022/05/Implementing-Calculation-Groups-Gif-1.mp4?_=1"> <a href="https://databear.com/wp-content/uploads/2022/05/Implementing-Calculation-Groups-Gif-1.mp4">https://databear.com/wp-content/uploads/2022/05/Implementing-Calculation-Groups-Gif-1.mp4</a></video>

00:00

00:22

I the above video you can see how I use it. If you do not want to show both Calculation Items in the visual, you can just filter in out in the filter pane, of give the user to choose using a slicer.

Video Player  <video width="600" height="402" src="https://databear.com/wp-content/uploads/2025/11/Slicer-From-Calculation-Group.mp4?_=2" controls=""><source type="video/mp4" src="https://databear.com/wp-content/uploads/2025/11/Slicer-From-Calculation-Group.mp4?_=2"> <a href="https://databear.com/wp-content/uploads/2025/11/Slicer-From-Calculation-Group.mp4">https://databear.com/wp-content/uploads/2025/11/Slicer-From-Calculation-Group.mp4</a></video>

00:00

00:14

You may not see the benefit yet, but as we all know reports can get very robust very quickly, and knowing this going in, will definitely reduce your time when creating a measure upon the measure.

Data Bear also offers a great training program, visit our [training page](https://databear.com/power-bi-training/).