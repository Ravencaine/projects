---
title: "Advanced TOPN in Power BI"
source: "https://medium.com/microsoft-power-bi/advanced-topn-in-power-bi-deb650b508c9"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-10-16
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
How to show TOPN plus ‘Others’

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*nBlbf-Y4DX8ZqwY1.png)

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

The basic Top N filter in Power BI can be very useful,

but if you need to show the values of the whole you will need to use an advanced Top N Filter

This guide shows you how you can set it up

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*ZADB3ZLsriVGIP7M.png)

If you use the standard top N filter you would see something like this

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*GJdJU0hh0PatTt-0.png)

We outlined how this works in this post  
[TOPN in Power BI — Select Distinct](https://www.selectdistinct.co.uk/2023/06/28/topn-in-power-bi/)

The problem with this method is that it ONLY shows the values for the top 5, but quite often you need to show the whole value with an aggregate row showing the ‘other’ values

We want the users to be able to use a slicer to select how many of the Top N values to see, but to also show the balance as ‘Others’

## Overview of the steps involved

Detailed steps

## 1.Ensure there is a measure value for the ranking

You may have a measure already, but if not create one

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*RVAX0wS9P0zLpkcq.png)

For illustration we are creating a measure called ‘Gross Sales New’ as the sum of the Gross Sales field

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*xNdVrKf8ahoor47Y.png)

DAX Code

**Gross Sales** **New** = SUM(**Financials** \[**Gross Sales**\])

paste this code over where it says Measure =, this creates the new measure

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*D2aPOV5AMrJLWlF_.png)

## 2\. Create a new table to determine the values for other

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*zjo66NaHoXlpbzhA.png)

Use this DAX code to create the new table

*TopN Names =  
UNION  
(ALLNOBLANKROW(* ***Financials*** *\[****Country****\]),  
{“Others”}  
)*

This creates a new table in the Fields Pane

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*nFNj6R0Z4pLgQTGq.png)

This table contains all the values in the matrix, plus ‘Other’ as the last row

## 3\. Now Create a parameter to set the number of top rows to show

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*jTbqO7O895CW_rb0.png)

In the new parameter dialog enter as follows:

Name >> TopN  
Data Type >> Whole Number  
Min >> 0  
Max >> 20 (Optional, TopN results required)  
Increment >> 1 (Usually, may be different)  
Default >> \* (Optional)  
Add Slicer >> Tick (Optional, will show slicer on report)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*EjhSQ-ynrqTH36Qx.png)

This creates a new Parameter table

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*RMoB-d-gHibhZtH3.png)

And slicer for the users to select a value for the Top N

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*tJXSNZ3ENRCvDTOh.png)

## 4\. Add a new measure to the Financials Table

This applies a ranking to all values in the rows, including others, based on the measure.

Right click Financials, select New measure, then replace contents of code box with

*Ranking =  
VAR CatToRank = \[TopN Value\]  
VAR Ranking =  
RANKX (  
ALLSELECTED(‘TopN Names’\[****Country****\]),  
\[****Gross Sales*** ***New****\]  
)  
VAR IsOtherSelected =  
SELECTEDVALUE(‘TopN Names’\[****Country****\]) = “Others”  
VAR Result =  
IF (  
IsOtherSelected,  
CatToRank + 1,  
IF ( Ranking <= CatToRank, Ranking, ranking + 1)  
)  
Return  
Result*

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*ZJ3puDXP0O5tnUOl.png)

This creates a new measure called Ranking in the Financials table

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Lj6TzDWv6WbBVaxS.png)

## 5\. Make the rows visible if their rank is within the Top N results

Create another measure with this code

*RowVisible =  
VAR Ranking = \[Ranking\]  
VAR TopNValue = ‘TopN’\[TopN Value\]  
VAR Result = INT( Ranking <= TopNValue + 1)  
Return  
Result*

**Compute a value for ‘Others’**

Add a new measure to the **Financials** table.

Paste the following into the code box.

***Gross Sales New*** *Amount =*

*VAR NewMeasureAll =*

*CALCULATE( \[Gross Sales New\], REMOVEFILTERS(‘TopN Names’\[****Country****\]) )*

*RETURN*

*IF (*

*ISINSCOPE(‘TopN Names’\[****Country****\] ),*

*VAR TopNToRank = \[TopN Value\]*

*VAR IsOtherSelected = SELECTEDVALUE(‘TopN Names’\[****Country****\]) = “Others”*

*VAR TopNWithMeasure =*

*ADDCOLUMNS(*

*ALLSELECTED(‘TopN Names’\[****Country****\]),*

*“@amt”, \[****Gross Sales New****\]*

*)*

*VAR TopNCat = TOPN( TopNToRank, TopNWithMeasure, \[@amt\] )*

*VAR TotalTopN = SUMX( TopNCat,\[@amt\] )*

*VAR Result = IF ( IsOtherSelected, NewMeasureAll — TotalTopN, \[****Gross Sales New****\])*

*RETURN Result,*

*NewMeasureAll*

*)*

This creates a new measure which is used in place of the original. This is necessary as the  
total of “Other” results has to be recalculated when the TopN value changes.

**Filter and Sort Results**

Enable “Other” values by Joining TopN Names table to the **Financials** table.

Open the Model window using the bottom icon in the left menu

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*d8-Bxq5rQ6WlDAF3.png)

Create a connection (Join) between the two **Country** objects

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*P2gtjto6afPpW0pj.png)

Drag the Country item in Financials to the Country item in TopN Names

This creates a join between the two tables wherever the **Country** Field is used.

Check the properties of the join. Right click on the arrow in the join connector, select Properties

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*e0Ckc4iNWaIXYy-y.png)

Ensure the following settings are correct:

Cardinality >> Many to One  
Cross Filter Direction >> Single  
Make this Relationship Active >> Ticked

Filter to show only TopN and Other

As it stands the Matrix is showing the original values, and all values. The Row Visible measure can be used to filter as only TopN and Other

Ensure the Matrix is selected.

Drag Row Visible item from Fields Pane to the Add Data field in the Filter Pane

Change the Show Items drop down to ‘IS’  
Add ‘1’ to the value box  
Click Apply Filter

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*1pi0O_oVvdUFZ94T.png)

The values in the Matrix should change to show only the TopN values. (If a Row item is not in the TopN, the Row Visible value will be 0. Remember, the Other item is not yet showing.)

Include the new values in the Matrix

Swap **Gross Sales New** measure for the **Gross Sales New Amount** in the Visualisations Pane, Values box

This changes the values in the Matrix. Note ‘Other’ is now shown.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*86LcR31bC2PTr_1W.png)

By default this is sorting the values by country ascending, we want the values to sort descending, but with the ‘others’ to always be last

Add Ranking to the Values of the Matrix

We add the ‘Ranking’ measure into the matrix

Order the Ranking values Ascending. Click on the column header in the matrix until the Arrow points up and the ranking is from 1 upwards.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*XUaj7cFkXsO6R8me.png)

**You now have an Advanced Top N Filter in Power BI**

This technique is applicable to other visualisations.

For example, duplicate the Matrix and change type to Pie Chart. This example clearly shows the top 5 as representing around a quarter of the whole, with ‘Others’ showing the majority

In this case we do not need Ranking, it can be removed

![](https://miro.medium.com/v2/resize:fit:1204/format:webp/0*6Tb0oGwHU8ckzc16.png)

## Conclusion

Learning how to create this Advanced Top N Filter in Power BI is a little complex, but worth persevering with.

Having the option to select the Top N value using a slicer in Power BI is a great way to allow the user to interact with the data

Subscribe to our channel to see more tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful SQL, Power BI or other business analytics timesavers in our Blog

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----deb650b508c9---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy