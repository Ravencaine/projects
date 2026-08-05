---
title: "Virtual tables in Power BI"
source: "https://databear.com/virtual-tables-in-power-bi/"
author:
  - "[[Annamarie Van Wyk]]"
published: 2022-10-25
created: 2026-08-04
description: "Learn how create virtual tables in Power BI using DAX. Reducing the number of tables and measures you need to create."
Processed: "Unprocessed"
---
Today I want to show you the power of understanding virtual tables using DAX in Power BI. You could ask why we need virtual tables when we can create real tables, well this is useful because it reduced the number of tables and measures you have to create, simplifying your data model.

I have a very silly example but it should show you how this works, and you can get more adventurous and complicated with it in your examples.

I have a sales table that looks like this, it is nothing too complicated.

![Sales table](99.System/Attachments/Sales_table.png)

Say, for example, you’d like to know in which state most customers were above the age of 40.

## Test by creating an actual table

To test what a table should look like in order for you to achieve this, first create a new table, to check it out. Using the New Table option in on the ribbon, write the following DAX to create the table with which you will check the desired result.

![DAX to create table](99.System/Attachments/DAX_to_create_table.png)

This is the DAX to create the table.

This is the table that it created with the above DAX function.

![Summarized table created](99.System/Attachments/Summarized_table_created.png)

Remembering that this table is not needed for any other purposed other than find the state where most customers bought from. So to simplify the process you can create the table and get the result all by creating 1 measure.

Let’s first see what the desired result should be, by filtering our test table to sorting the Age Count descending, you see that California is the answer we should get.

![Sort descending](99.System/Attachments/Sort_descending.png)

Back to the new measure to create.

## Implement your result in your Virtual table in Power BI

First copy the code from the test table.

Age table =

SUMMARIZE (

Salestable,

Salestable\[State\],

“Age Count”,

CALCULATE (

COUNT ( Salestable\[Customer Age\] ),

FILTER ( Salestable, Salestable\[Customer Age\] > 40 )

)

)

The next step is adding a column to get the rank and this will then give the state with the highest count a ranking of 1, thereafter you will filter the table on the Rank = 1 and return the name of the state with that ranking. Let me show you.

### New Measure for the final DAX to create your virtual table in Power BI

Create a new measure which will do all of the steps mentioned above in 1 DAX statement.

Virtual table =

var tab = ADDCOLUMNS(

SUMMARIZE (

Salestable,

Salestable\[State\],

“Age Count”,

CALCULATE (

COUNT ( Salestable\[Customer Age\] ),

FILTER ( Salestable, Salestable\[Customer Age\] > 40 )

)

),”Rank”,RANKX(SUMMARIZE (

Salestable,

Salestable\[State\],

“Age Count”,

CALCULATE (

COUNT ( Salestable\[Customer Age\] ),

FILTER ( Salestable, Salestable\[Customer Age\] > 40 )

)

),\[Age Count\],,DESC))

return CALCULATE(SELECTEDVALUE(‘Age table'\[State\]),’Age table'\[Rank\] = 1)

This does is the following. First is adding the same code used to create the test table. You then encase that with an ADDCOLUMNS, adding the RANK. Lets stop there for a second and go back to our test table.

If I were to add a column to this table in the conventional why, this is the result it returns.

![Adding rank to table](99.System/Attachments/Adding_rank_to_table.png)

Confirming once again that California is the state we are looking for.

Back to the measure. We will encase our measure to add the column in the syntax. It adds the column to the table, while creating the table. You will also see that I created the entire table creation in a variable (var tab = ). Lastly in the return function, we say that we want the State ([SELECTEDVALUE](https://learn.microsoft.com/en-us/dax/selectedvalue-function) (‘Age table'\[State\])) where Rank = 1, effectively filtering the table and giving only the Selected value of the state column.

![Virtual table Measure](99.System/Attachments/Virtual_table_Measure.png)

Let check if our measure if returning the correct answer.

![Virtual Tables GIF](99.System/Attachments/Virtual_Tables_GIF.gif)

Happiness!

I hope I explained this well enough to understand it. Virtual tables really reduces the number of measures and table you need to create in your data model.

Don’t forget to check out our [training page](https://databear.com/power-bi-training/) for great training programs to learn more about Power BI.

Check out our [consulting services](https://databear.com/power-bi-consulting/) and [support packages.](https://databear.com/power-bi-support-packages/)