---
title: "Power Automate Tips: Tracked Properties"
source: "https://medium.com/@berilevliyaoglu/power-automate-tracked-properties-04f8d20e4b74"
author:
  - "[[Beril]]"
published: 2024-05-15
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
In a Power Automate flow, some actions may be highly time-sensitive, meaning that the output could change depending on the step’s execution time. If you want to exactly know when your flow step is executed, and want to track the time passed between the executions of two steps, you can use “tracked properties”.

This is not the only use-case for tracked properties, however it is the most common way of how power automate developers utilize it. You can think of any other usages of the feature, by considering:

- Tracked properties are hidden away from the inputs/outputs sections.
- Tracked properties as “key-value” pairs are output all together as a JSON.
- Syntax for receiving the output JSON is, ***actions(‘NameOfTheAction’)?\[‘TrackedProperties’\]***
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wIs3FF8aotlcd3OxX9tjiQ.png)

go to settings of the action

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1qg3o44_rCty07RNnoVc8A.png)

you can use expressions, strings, numbers, json (which makes nested json) for the value

![](https://miro.medium.com/v2/resize:fit:1156/format:webp/1*o58hmA7luuLbpI8ks05DFQ.png)

you can access the json by using actions function

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hOqkEh16jp2abz3qG-V1Iw.png)

sample output