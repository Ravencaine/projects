---
title: "Power Automate | Getting the values from SharePoint, into a Excel File"
source: "https://medium.com/@suarez.sergio.g/power-automate-getting-the-values-from-sharepoint-into-a-excel-file-62cf5dd21384"
author:
  - "[[Sergio Suarez]]"
published: 2026-08-07
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8Di5rAPBNgwxb2eu-beA4Q.png)

## Scope

For the past two months, my **BIG BOSS** has been asking me for a report of all the travel the workers in our organization have taken/completed. This is because I have all those values in a Share Point list, attached to the app I created…… last year.

Here’s the “rub”, the information he wants is listed in all the columns I have set up, that works with the other automations and the app. However, the WAY he needs it differs in “column name” of each value. So, I have to manually copy then paste to another file, those values, while keeping the formatting clean. It’s a lot of “hand jamming”, more than I want to spend. So…… let’s automate it.

### Setup before hand

Before I we start, there are a few things we need to make sure we have:

- A template `.xlsx` file that list all the columns the way “ **BIG BOSS** ” is asking for
- A directory to save the new file
- Access to the SharePoint list

## Action descriptions

These are the different codes, or to be aware of, within each action.

### Manually trigger a flow

Ok, we want to make sure that this process is “repeatable” for every month in the calendar year. So, the “triggering” event is a “Manual trigger”. In the “Parameters” section, ensure you ‘Add an input’ and choose `number`, name it `SelectMonth`.

![](https://miro.medium.com/v2/resize:fit:1240/format:webp/1*5gn7PT9Th-6qbytiELh43g.png)

### Compose actions

Add two **Compose** actions below this trigger. Name them `StartDate` and `EndDate`.

**// StartDate**

Within the ‘Inputs’ field, put the following:

```c
concat('2026-', if(less(triggerBody()?['number'], 10), concat('0', string(triggerBody()?['number'])), string(triggerBody()?['number'])), '-01')
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DZosM-wHatThrnh7uuwk6g.png)

**// EndDate**

Within the ‘Inputs’ field, put the following:

```c
startOfDay(addToTime(outputs('StartDate'), 1, 'Month'))
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HMAJASCuAhemySS18w0IsA.png)

### Get items from SP

This will retrieve the inputs from the SharePoint list, where the records are stored. Add an action, ‘Get items’ (this will be under the SharePoint grouping). Fill out, like below.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-Z4Qa38Pqfd3cadDhebUnQ.png)

> \*\*UPDATE\*\*: Change your “Filter Query” section to read like below:

```c
(Departure ge '@{outputs('StartDate')}') and (Departure lt '@{outputs('EndDate')}') and (Status eq 'Approved')
```
![](https://miro.medium.com/v2/resize:fit:1246/format:webp/1*OmgNbcPk86MbcMvAZKgPMA.png)

**// Filter Query Explination**

- ‘Departure’ is the name of a column from the SharePoint list; it is in `date` format.
- `ge` is “greater than or equal to” `'@{outputs(‘StartDate’)}'`
- then, `lt` stands for “less than” `‘@{outputs(‘EndDate’)}’`
- ‘Status’ is the name of a column from the SharePoint list; `eq` is “equal” to a value of ‘Approved’

### Apply to each

Add an action, “Apply to each”; this will ‘loop’ for each `item`, within the initial ‘Get items from SP’ action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hI7bEpIUrRElpJD3vv--lQ.png)

### Add a row into a table

Within the afore mentioned action, add a “ **Add a row into a table** ”action. Here you associate each value, from the “ **Get items from SP** ” action created earlier, then place them in their associated fields, within selected `File *` (the template `.xlsx` file you created earlier).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xMsA0XlbO10nSf--HPezqg.png)

### Copy file

Now, OUTSIDE of the “ **Apply to each** ” loop, add a action; choose “ **Copy file** ”. This action makes a copy of the `TEMPLATE_FILE.xlsx` that has been written in, with all the items from the SharePoint List. It will copy it to another directory, under a different name.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JIy3zSONs6kOrijLh1Ttnw.png)

Within the ‘Destination File Path’ field, select the NEW DIRECTORY where you will store the `output` of the finalized `.xlsx` file (for this example, it is `.../_output/`). Then after the last `/` hit the `fx` Expression button and input the following code:

```c
concat(if(equals(triggerBody()?['number'], 1), 'January', if(equals(triggerBody()?['number'], 2), 'February', if(equals(triggerBody()?['number'], 3), 'March', if(equals(triggerBody()?['number'], 4), 'April', if(equals(triggerBody()?['number'], 5), 'May', if(equals(triggerBody()?['number'], 6), 'June', if(equals(triggerBody()?['number'], 7), 'July', if(equals(triggerBody()?['number'], 8), 'August', if(equals(triggerBody()?['number'], 9), 'September', if(equals(triggerBody()?['number'], 10), 'October', if(equals(triggerBody()?['number'], 11), 'November', 'December'))))))))))), '_2026_Travel.xlsx')
```

This code designates the MONTH to associate with the `number` you input during the “ **trigger** ” action for this flow. For example, if you input a `7` at the start of this flow, the output file will be named `July_2026_Travel.xlsx`.

## The fun part

Now, the original template file is written in. It needs to be cleared out but, with the table “headers” still there. We cannot just delete the file and place a new one because Power Automate has a specific **GUID** (Globally Unique Identifier) associated with the template file.

We just have to add two more Excel actions:

- **List rows present in table**
- **Delete a row**
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*jd_aw0NLv2nP7oL2TGcuAA.png)

### List rows present in a table

Add a action, and select “ **List rows present in a table** ” (it should be located in the Excel grouping). I named mine ‘List rows present in ORIG table’. Point it to the `TEMPLATE_FILE.xlsx`.

![](https://miro.medium.com/v2/resize:fit:1238/format:webp/1*et1nreHPWV5ozt90Oyie0g.png)

### Delete a row

Add a action, and select “ **Delete a row** ” (it should be located in the Excel grouping).

![](https://miro.medium.com/v2/resize:fit:1258/format:webp/1*f5SUSPMZTml1fMIaCr9B7g.png)

You will then point it to your specific `.xlsx` file and set the `Key Column` and `Key Value`. Here, for this example, the `Key Column` we will be using is `Trip ID`. This is record `id` for each entry, as listed in the `.xslx` file.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*VVEnHv_xGHB10hiTVcHBrg.png)

The `Key Value` will be "sourced" from the ‘List rows present in ORIG table’ Action.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*YzSGILjezY2GXo3kgAdBcA.png)

The translation of all this:

- **Key Column**: This is will be selected from the drop-down that appears. For this example, we selected `Trip ID`.
- Key Value: This is the specific unique identifier for the row we are looking to delete. For this example, our \[`value`\] for each of the rows is `JTR-####`, or `JTR-1027`.

**// BONUS INFO**

The `For Each` loop is automatically created. With this selected, click on "Settings". Go and enable 'Concurrency control'. I set my limit to `10`. This means that it will delete `10 records per run`, which should cut down on "processing time" for your automation.

You are free to change it to what ever value you want, depending on the size of your file.

…and now, the Template file, is returned BACK to it’s initial state, ready for the next report, “BIG BOSS” is happy, and now it takes me 10 seconds to run a automation.

## Closing Thoughts

This was a lot of fun to figure out. The “Final” solution came in different parts. At first, it would NOT work the way I wanted (when I tried to clear the template file). Took a lot of trial and error but, in the end, having it work properly is the best part of this.

Leave a clap if you got something out of this. Thanks and have a good one.