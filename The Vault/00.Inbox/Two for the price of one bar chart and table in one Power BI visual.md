---
title: "Two for the price of one: bar chart and table in one Power BI visual"
source: "https://medium.com/microsoft-power-bi/two-for-the-price-of-one-bar-chart-and-table-in-one-power-bi-visual-01550076f8fb"
author:
  - "[[Mateusz Mossakowski]]"
published: 2026-02-03
created: 2026-08-12
description: "Last week I noticed a post from Anastasiya Kuznetsova about her favorite combo: a bar chart and a table. I like it both visually and analytically, but placing both visuals directly one under the other might be a real pain in the a$$ in Power BI. That is why I wanted to show you a technique that is slightly more demanding from the technical perspective but, on the other hand, it works in scenarios where a double-visual approach fails miserably."
Processed: "Unprocessed"
---
## Last week I noticed a post from Anastasiya Kuznetsova about her favorite combo: a bar chart and a table. I like it both visually and analytically, but placing both visuals directly one under the other might be a real pain in the a$$ in Power BI. That is why I wanted to show you a technique that is slightly more demanding from the technical perspective but, on the other hand, it works in scenarios where a double-visual approach fails miserably.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rb7h3HkHAAsIR237t7Qw2A.gif)

![](https://miro.medium.com/v2/format:webp/0*-c1RxDYNi76__dW9)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

Let’s start where everything should start — from the beginning 😊. Let’s have a look at the beautiful and insightful visual created by Anastasiya. In my opinion it’s a perfect combination of both the first-look data-grasping part (bar chart component) and a more detailed oriented part (table component). While I love it, building such a double visual in Power BI by simply placing one visual under the other might be a very hard, if not impossible, task.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0MGN54MeYc00jK6ZTwNBbw.gif)

There are a couple of ways to solve this more reliably. One approach I’d like to focus on today is a relatively simple SVG measure that we’ll use to generate the bar chart part of the combo visual. Let me break the solution down into as atomic components as possible.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yJ6LZjjEm6oXdfuQfrrW-Q.png)

First, we need an overall maximum measure. In our case it is the overall maximum of either the selected year’s Revenue measure or the previous year’s Revenue measure at the month-name level. This is crucial, as we do not want to operate on nominal values. We want to make all the bar heights relative to the overall maximum so that bar heights across different months are comparable. And instead of values I should rather say the bar heights 😊

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Qth71MXDx4bLKQffjUJYZQ.png)

Nothing fancy, but we need some colors for the conditional formatting of the bars. For the sake of a complete description of the solution, there you go.

Above, you can see the final shape of the bar chart measure. I will paste the code at the very end of the article for your convenience. I hope the comments there are self-explanatory and that you can easily follow my reasoning. Reminder: don’t forget to set the data category to “Image URL.”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rZ6ykw4zbxutE31fmkQdEw.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rC6yaUzy40bO4dOmFMSDAw.png)

Hopefully, in the GIF below you can easily assess the benefits of the SVG approach over the double-visual approach. If you know how to optimize the approach further, please don’t hesitate to reach out to me.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rb7h3HkHAAsIR237t7Qw2A.gif)

```c
Bar charts = 
VAR _max = [Overall Max Revenue] // overall maximum value to make everything relative to this value
VAR _color = [Color] // here we have conditional formatting part responsible for coloring bars
VAR _color_80 = _color & "80" // let's add some partial transparency so that the solution is even more fancy :)
VAR _grey_color = "#e9e9e9" // a hardcoded grey colkor HEX
VAR _x = 10 // x coordinate where we start the year ago (YA) bar
VAR _x_shifted = _x + 10 // x coordinate of the selected year bar - we want it to be shifted a little bit
VAR _width = 40 // width of the YA bar
VAR _half_width = _width/2 // width of the selected year bar - we want it to be narrower as it will be shown in front
VAR _image_height = 200 // overall height - we will use the same in the properties of the image size
VAR _measure_height = DIVIDE( [Revenue], _max ) * _image_height * 0.95 // let's make the selected year value relative to the overall max and give a little bit of spacing by decreasing it by 5%
VAR _measure_ya_height = DIVIDE( [Revenue YA], _max ) * _image_height * 0.95 // we do the exact same thing for the last year value
VAR _header = "data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg'>"
// the tricky part here is that the y coordinate is an overall image height decreased by the bar height
// otherwise the bar charts will be upside down 🙃
VAR _measure_ya_bar =
    "<rect id='bar' x='" & _x & "' y='" & _image_height - _measure_ya_height & "' width='" & _width & "' height='"
        & _measure_ya_height
        & "' fill='"
        & _grey_color
        & "'/>   
"
VAR _measure_bar =
    "<rect id='bar' x='" & _x_shifted & "' y='" & _image_height - _measure_height & "' width='" & _half_width & "' height='"
        & _measure_height
        & "' fill='"
        & _color_80
        & "'/>        
"
VAR _footer = "</svg>"
// the order of last year and selected year bars is crucial as this determines the "layers" of the SVG
VAR _result = IF( ISBLANK( [Revenue] ), BLANK( ), _header & _measure_ya_bar & _measure_bar & _footer )
RETURN
    _result
```

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----01550076f8fb---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualization, DAX

**Tags:** Tutorial, Data Visualization, DAX