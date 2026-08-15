---
title: "Power BI button slicer as a KPI card on steroids"
source: "https://medium.com/microsoft-power-bi/power-bi-button-slicer-as-a-kpi-card-on-steroids-46bc828b3c10"
author:
  - "[[Mateusz Mossakowski]]"
published: 2025-07-03
created: 2026-08-12
description: "While I’m not a big fan of list or tile slicers in Power BI (since they take up too much space without adding much value) the situation is somewhat different with the 𝗕𝘂𝘁𝘁𝗼𝗻 𝘀𝗹𝗶𝗰𝗲𝗿. This is because two key features come bundled with this type of slicer. One is the ability to use 𝐒𝐕𝐆 𝐦𝐞𝐚𝐬𝐮𝐫𝐞𝐬, and the other is the capability to display different data depending on the 𝐬𝐞𝐥𝐞𝐜𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝐢𝐧𝐭𝐞𝐫𝐚𝐜𝐭𝐢𝐨𝐧 𝐬𝐭𝐚𝐭𝐞𝐬 (Selected, Rest, Hover, Press)."
Processed: "Unprocessed"
---
Featured

## While I’m not a big fan of list or tile slicers in Power BI (since they take up too much space without adding much value) the situation is somewhat different with the 𝗕𝘂𝘁𝘁𝗼𝗻 𝘀𝗹𝗶𝗰𝗲𝗿. This is because two key features come bundled with this type of slicer. One is the ability to use 𝐒𝐕𝐆 𝐦𝐞𝐚𝐬𝐮𝐫𝐞𝐬, and the other is the capability to display different data depending on the 𝐬𝐞𝐥𝐞𝐜𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝐢𝐧𝐭𝐞𝐫𝐚𝐜𝐭𝐢𝐨𝐧 𝐬𝐭𝐚𝐭𝐞𝐬 (Selected, Rest, Hover, Press).

Above, you can see an artificial example demonstrating how the button slicer can be treated as a card and slicer combined on steroids. Why? Because the button slicer’s different states allow you to present multiple pieces of information within a single visual, while still functioning as a regular slicer that affects other visuals (in this case, the matrix below). I highly recommend considering this approach.

That said, there is always a risk of overdoing it. I even used the press interaction state to showcase it with a silly question 🙃

Let me walk you through what I’ve done to achieve the marvelous result you just saw! 😊 One disclaimer upfront: I am by no means an expert in SVG DAX measures, so any comments on improving performance (a significant game changer might be when visual calculations allow for image URL type) and/or responsiveness are more than welcome.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=article-start&utm_campaign=article-start) **🎁**

### DAX measures

Before we jump into the main dish, let me start with the appetizers (I apologize for the redundancy). Below, you’ll find two color measures, along with an overall maximum for both Revenue and Revenue year ago to help standardize the bar sizes within the current context of all brands in the selected country and year. These will later be referenced in the SVG measures used for the KPI-like button slicer element.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*r5MnQ-4XvWVllU98cHqfwg.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2D9Nw5KtxZWnhOazQv0c_w.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Y1TBGuYOK6FQXFagzPBJlw.png)

Now, let’s move on to the main course, which consists of two SVG measures. The first one is for the “Rest” state (to be honest, I much preferred the previously used term “Default” 🙃). It features an embedded bar chart that displays how Revenue (the bar) compares to Revenue year ago (indicated by a vertical black marker). To make it more fancy, the main bar chart is colored green if Revenue is higher than the previous year and red if the condition is not met.

The second measure is for the “Selected” state. The key difference here is that, in addition to what the “Rest” measure provides, it also explicitly shows the Revenue year ago value and the Revenue year-over-year percentage change.

Last but not least, we have a “Hover” measure that simply displays the best-selling month, along with the top customer and the corresponding revenue value.

> And please remember to set the appropriate data category for all SVG measures.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VR_BjtOBw5cVK_Lbm-Be5w.png)

### Button slicer setup

Once we’re done with the DAX and SVG heavy lifting, we can move on to the cool-down stretch to complete the exercise routine. To do this, we need to select the Button slicer from the list of available visuals.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ujlFMHHUzrrPIGd5ex_jww.png)

The magic happens once you scroll down a little bit and expand the Images section. There you can define which SVG measure will be used for which state (Rest, Hover or Selected).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*TZ2ee1PixU_mIpXbNFF5uw.png)

> Pro tip: If you want the hover measure to be “available” even when a specific element of the button slicer is already selected, you’ll need to enable the Advanced options for the slicer states.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*OAdmJjb7KrVBh0hHSpFwcA.png)

below you can find the TMDL script for the above mentioned measures:

```c
createOrReplace

 ref table _measures

  measure Color =
    
    IF ( [Revenue YoY %] > 0, "#008100", "#ff0000" )
   lineageTag: a8aa0279-6faa-4d03-8e3b-3c252cf49319

  measure 'Grey Color' =
    
    "#ededed"
   lineageTag: 2450a5b1-2184-4159-82f6-c93dd4e7f140

  measure 'Overall Max Revenue' =
    
    MAXX(
        {
            MAXX( ALLSELECTED( product_dim[brand] ), [Revenue] ),
            MAXX( ALLSELECTED( product_dim[brand] ), [Revenue YA] )
        },
        [Value]
    )
   lineageTag: f62b42a7-f477-4be8-ae2f-66140427fc78

  measure Selected =
    
    VAR _max = [Overall Max Revenue]
    VAR _color = [Color]
    VAR _color_60 = _color & "60"
    VAR _grey_color = [Grey Color]
    VAR _x = 10
    VAR _header = "data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg'>"
    VAR _footer = "</svg>"
    VAR _core =
        "   <rect id='bar' x='" & _x & "' y='10' width='150' height='20' fill='" & _grey_color
            & "'/>
            <rect id='fill' x='"
            & _x
            & "' y='15' width="
            & "'"
            & DIVIDE( [Revenue], _max ) * 100
            & "' height='10' fill='"
            & _color_60
            & "'></rect>
            <rect id='marker' x='"
            & _x + DIVIDE( [Revenue YA], _max ) * 100
            & "' y='10' width='2' height='20' fill='black'></rect>
            <text x='"
            & _x
            & "' y='45' fill='"
            & _color
            & "' font-family = 'Segoe UI Semibold' font-size = '10'>"
            & "Revenue   : "
            & FORMAT( [Revenue], "#,##0,,.0 M" )
            & "</text>
            <text x='"
            & _x
            & "' y='60' fill='black' font-family = 'Segoe UI Semibold' font-size = '10'>"
            & "Revenue YA: "
            & FORMAT( [Revenue YA], "#,##0,,.0 M" )
            & "</text>
            <text x='"
            & _x
            & "' y='75' fill='grey' font-family = 'Segoe UI Semibold' font-size = '10'>"
            & "Revenue YoY: "
            & FORMAT( [Revenue YoY %], "#,##0.0 %" )
            & "</text>
    "
    VAR _result = _header & _core & _footer
    RETURN
        _result
   lineageTag: c40eec72-6bea-4081-b37b-855988c82399
   dataCategory: ImageUrl

  measure Rest =
    
    VAR _max = [Overall Max Revenue]
    VAR _color = [Color]
    VAR _color_60 = _color & "60"
    VAR _grey_color = [Grey Color]
    VAR _x = 10
    VAR _header = "data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg'>"
    VAR _footer = "</svg>"
    VAR _core =
        "   <rect id='bar' x='" & _x & "' y='10' width='" & 150 & "' height='25' fill='" & _grey_color
            & "'/>
            <rect id='fill' x='"
            & _x
            & "' y='15' width="
            & "'"
            & DIVIDE( [Revenue], _max ) * 100
            & "' height='15' fill='"
            & _color_60
            & "'></rect>
            <rect id='marker' x='"
            & _x + DIVIDE( [Revenue YA], _max ) * 100
            & "' y='10' width='2' height='25' fill='black'></rect>
            <text x='"
            & _x
            & "' y='65' fill='"
            & _color
            & "' font-family = 'Segoe UI Semibold' font-size = '14'>"
            & "Revenue   : "
            & FORMAT( [Revenue], "#,##0,,.0 M" )
            & "</text>
    "
    VAR _result = _header & _core & _footer
    RETURN
        _result
   lineageTag: 461edc66-33a9-4574-9202-bf2a841c3e1a
   dataCategory: ImageUrl

  measure Hover =
    
    VAR _best_selling_month =
        MAXX (
            SELECTCOLUMNS (
                TOPN ( 1, ADDCOLUMNS ( DISTINCT ( calendar_dim[year_month_name] ), "@rev", [Revenue] ), [@rev] ),
                "description", calendar_dim[year_month_name] & " (" & FORMAT ( [@rev], "#,##0,,.0 M" ) & ")"
            ),
            [description]
        )
    VAR _best_selling_customer =
        MAXX (
            SELECTCOLUMNS (
                TOPN ( 1, ADDCOLUMNS ( DISTINCT ( store_dim[customer] ), "@rev", [Revenue] ), [@rev] ),
                "description", store_dim[customer] & " (" & FORMAT ( [@rev], "#,##0,,.0 M" ) & ")"
            ),
            [description]
        )
    VAR _x = 5
    VAR _header = "data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg'>"
    VAR _footer = "</svg>"
    VAR _core =
        "       <text x='" & _x
            & "' y='15' fill='grey' font-family = 'Segoe UI Semibold' font-size = '10'>top month</text>
            <text x='"
            & _x
            & "' y='30' fill='black' font-family = 'Segoe UI Semibold' font-size = '10'>"
            & _best_selling_month
            & "</text>
            <rect id='bar' x='"
            & _x
            & "' y='40' width='"
            & 150
            & "' height='1' fill='#e6e6e6'/>
            <text x='"
            & _x
            & "' y='55' fill='grey' font-family = 'Segoe UI Semibold' font-size = '10'>top customer</text>
            <text x='"
            & _x
            & "' y='70' fill='black' font-family = 'Segoe UI Semibold' font-size = '10'>"
            & _best_selling_customer
            & "</text>
    "
    VAR _result = _header & _core & _footer
    RETURN
        _result
   lineageTag: 12915b9a-ead3-42a3-9112-0e907b748de7
   dataCategory: ImageUrl

  measure Press =
    
    VAR _x = 2
    VAR _header = "data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg'>"
    VAR _footer = "</svg>"
    VAR _core =
        "   <text x='" & _x
            & _x
            & "' y='30' fill='black' font-family = 'Segoe UI Semibold' font-size = '16'>Can you read it? 😅</text>
    "
    VAR _result = _header & _core & _footer
    RETURN
        _result
   lineageTag: 71b492b2-8db5-42d1-97e5-f9ae0099eba3
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_Uqe1K0RClBQcJb_YdZo4A.png)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----46bc828b3c10---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX, Data Visualization

**Tags:** Tutorial, DAX, Data Visualization