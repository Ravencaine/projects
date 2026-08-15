---
title: "How to Standardize Column Widths in Power BI"
source: "https://medium.com/microsoft-power-bi/how-to-standardize-column-widths-in-power-bi-e6abddaa1291"
author:
  - "[[Mateusz Mossakowski]]"
published: 2026-01-16
created: 2026-08-12
description: "Today I am going to write about how to make Power BI matrix columns the same width. Usually, if different columns of your matrix contain values of different lengths or the attribute element values (which are used in the columns section of the matrix), then you’d end up with columns of different widths. If you ask me, I personally do not care about it 🙃 However, if you do, I have some good news for you — there are some options to achieve it. Let me walk you through it."
Processed: "Unprocessed"
---
## Today I am going to write about how to make Power BI matrix columns the same width. Usually, if different columns of your matrix contain values of different lengths or the attribute element values (which are used in the columns section of the matrix), then you’d end up with columns of different widths. If you ask me, I personally do not care about it 🙃 However, if you do, I have some good news for you — there are some options to achieve it. Let me walk you through it.

Let me start with an example. As you can see in the screenshot below, columns can have different widths because of the attribute element names used in the matrix columns.

However, column names are not the only reason. Sometimes, when measure values are “longer” than attribute names, the values themselves can be responsible for different column widths as well.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

Moving on to the solution. There are a couple of ingredients for this recipe. First, we’re going to use the `format string expression`. Secondly, we will find a way to retrieve the current length of each formatted value and each column header. Finally, a magical ingredient of a non-breaking space (we will be using `UNICHAR(8192)`) which we want to add as a prefix to the out-of-the-box format string in order to have full control over the ultimate column width.

There are different ways to handle the format string expressions. You can do it from the PBI Desktop UI by changing the format to “Dynamic”. Once you make such a change, you’ll be able to switch from the measure expression to the format expression.

You can achieve the same using Tabular Editor by clicking on the measure name in the TOM Explorer and then switching from “Expression” to “Format String Expression”.

Now jumping into the core of the logic and making it as atomic as possible. First, we define the format string of the measure for which we want to force the same width of the columns. Second, we transform `SELECTEDMEASURE()` to a string in which the measure's numeric value is presented using the previously provided format string. Then we define the predefined character length. The next step is to actually calculate the difference between the maximum length and the length of the formatted measure value. As a last step we add a prefix to the original format; the prefix is simply the non-breaking space repeated as many times as the difference in length calculated in the previous step.

![](https://miro.medium.com/v2/resize:fit:1382/format:webp/1*jp0d5BrvWzqyIOSehvzcoQ.png)

The issue with the over-simplistic code above is that it is not “safe”. If someone provides the \_max\_value\_len with a number than is smaller than the formatted measure value (for instance 4 in our example) then the visual will break.

That’s why we can add a safety buffer to the difference in length variable, bounded below by zero. Then the visual will not break, but unfortunately we lose the same-width functionality.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WkmTQqoE-z3mqHxnBrVBuA.png)

What’s a better approach then? Instead of using a safety buffer of zero, we could base it on the maximum length of the column header elements (in our case, country names). In such case even too small maximum length variable doesn’t kill the solution.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*3Q6Rv-06WQ8OFmsfs2jhDg.png)

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*S5Sx017akMIH6QZveaB_uw.png)

Is that all we can do? Of course not. We can actually get rid of manual input of the maximum length altogether. Instead we can check all the formatted measure values, find the longest ones, and treat that as the dynamic maximum length. Here we’re using ROLLUPADDISSUBTOTAL, as the lowest level/individual cell measure values would not always contain the biggest number of characters. Sometimes it is the case for subtotals or grand totals.

Is that the final version? Not yet. Things get more interesting if we can also handle negative values. If we apply the above logic to the Revenue Year Over Year percentage change measure, where there is certainly a possibility of negative values, the outcome won’t be perfect, as the minus sign would be farther from the actual number.

But fear not, my dear reader, we have a solution for that 🙃 It’s a little more convoluted, as the code needs to cover formatting for both positive and negative values. But the core idea stays almost untouched.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*HRGuYEPg36rgk72Pb_IIuw.png)

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*Ycev64sde_lXkvmoJLcH1A.png)

Not every approach is transferable to Power BI DAX user-defined functions. For instance, I don’t believe ROLLUPADDISSUBTOTAL is a good candidate to become a reusable function, but in general we can employ UDFs here for some simpler approaches. Please find the TMDL code below.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VmqxdmCUqpiXG14b7sY1Tw.png)

```c
createOrReplace

 function 'MateuszMossakowski.FormatString.SameWidthColumns' =
   
   (
       FormatStringPositive: STRING,  // format string for positive values
       FormatStringNegative: STRING, // format string for negative values
       Length: INT64 VAL, // predefined number of characters in the measure format string
       Col: ANYREF EXPR // column used in the matrix columns section
   ) =>
   VAR _format_positive = FormatStringPositive
   VAR _format_negative = FormatStringNegative
   // transform measure values to use the positive format string
   VAR _formatted_measure_positive = FORMAT( SELECTEDMEASURE( ), _format_positive )
   // transform measure values to use the negative format string
   VAR _formatted_measure_negative = FORMAT( SELECTEDMEASURE( ), _format_negative )
   // retrieve the maximum lenght of the values of the column used in the matrxi column
   VAR _max_len_headers =
       MAXX
       (
           SUMMARIZECOLUMNS( Col, ALLSELECTED( Col ), "@len", LEN( MAX( Col ) ) ),
           [@len]
       )
   // overall maximum length is the maximum of predefined length and the columns headers maxium length
   VAR _max_len = MAX( Length, _max_len_headers )
   // the difference between maximum length and measure value formatted using positive format string
   VAR _len_diff_positive = _max_len - LEN( _formatted_measure_positive )
   // the difference between maximum length and measure value formatted using positive format string
   VAR _len_diff_negative = _max_len - LEN( _formatted_measure_negative )
   // ultimate format striung used for positive values
   // prefix of non trimmable space UNICHAR(8192) is added
   VAR _result_positive = REPT( UNICHAR( 8192 ), _len_diff_positive ) & _format_positive
   // ultimate format striung used for negative values
   // prefix of non trimmable space UNICHAR(8192) is added
   VAR _result_negative = REPT( UNICHAR( 8192 ), _len_diff_negative ) & _format_negative
   // ultimate overall format string expression is a concatenation of the both above
   VAR _result = _result_positive & ";" & _result_negative
   RETURN
       _result
```

Or a more simplistic function disregarding the maximum length of header element names.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vh7okMhYoJ8wgzHDMrj_Pw.png)

```c
createOrReplace

 function 'MateuszMossakowski.FormatString.SameWidthColumnsBasic' =
   
   (
       FormatStringPositive: STRING,  // format string for positive values
       FormatStringNegative: STRING, // format string for negative values
       Length: INT64 VAL // predefined number of characters in the measure format string
   ) =>
   VAR _format_positive = FormatStringPositive
   VAR _format_negative = FormatStringNegative
   // transform measure values to use the positive format string
   VAR _formatted_measure_positive = FORMAT( SELECTEDMEASURE( ), _format_positive )
   // transform measure values to use the negative format string
   VAR _formatted_measure_negative = FORMAT( SELECTEDMEASURE( ), _format_negative )
   // retrieve the maximum lenght of the values of the column used in the matrxi column
   // overall maximum length is the maximum of predefined length and the columns headers maxium length
   VAR _max_len = MAX( Length, 0 )
   // the difference between maximum length and measure value formatted using positive format string
   VAR _len_diff_positive = _max_len - LEN( _formatted_measure_positive )
   // the difference between maximum length and measure value formatted using positive format string
   VAR _len_diff_negative = _max_len - LEN( _formatted_measure_negative )
   // ultimate format striung used for positive values
   // prefix of non trimmable space UNICHAR(8192) is added
   VAR _result_positive = REPT( UNICHAR( 8192 ), _len_diff_positive ) & _format_positive
   // ultimate format striung used for negative values
   // prefix of non trimmable space UNICHAR(8192) is added
   VAR _result_negative = REPT( UNICHAR( 8192 ), _len_diff_negative ) & _format_negative
   // ultimate overall format string expression is a concatenation of the both above
   VAR _result = _result_positive & ";" & _result_negative
   RETURN
       _result
```

Final warning: remember that everything comes with a price. Here, that price is performance. The more convoluted the approach you choose, the more it will impact the timings 🙃 As you can see, the time has almost doubled for the custom approach to format the numbers and secure same width columns.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ptRKAFvYOy3e9g2pGIooAQ.png)

server timings with standard format

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*x3uu9CHzx4WZYsjmk9vAqw.png)

server timings with custom format string expression

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----e6abddaa1291---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** DAX, Data Visualization

**Tags:** Tutorial, DAX, Data Visualization