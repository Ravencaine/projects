---
title: "Step-by-Step Guide to Retrieve Data from SharePoint List with Over 5000 Items"
source: "https://medium.com/@venkadeshblog/step-by-step-guide-to-retrieve-data-from-sharepoint-list-with-over-5000-items-b5a7a88d5f2c"
author:
  - "[[Venkadesh Sundaramurthy]]"
published: 2023-08-27
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
Managing large datasets in SharePoint lists can sometimes be a daunting task, especially when the list contains more than 5000 items. SharePoint imposes a limit on the number of items retrieved in a single request

In this article, we will walk you through a step-by-step approach to retrieve data from a SharePoint list containing more than 5000 items.

## Understanding the Concept:

1\. **Sending HTTP Request to SharePoint REST API:** To retrieve data from a SharePoint list, we’ll be utilizing the SharePoint REST API.

2\. **Managing Data Exceeding 5000 Items:** SharePoint imposes a limit of 5000 items per request when querying a list. However, when the list contains more items, the HTTP response includes a property called `__next`. This property is a URL that points to the next batch of records, enabling us to fetch data beyond the initial 5000 items.

## Steps:

1\. Create a Power Automate Instant Flow

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kR3-W8ZYnUsAMR0OAO5pHg.png)

2\. Initialize a boolean variable named ‘ **varNextPageExists** ’ with the value **‘true’**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hLNfVYkqwKHF6QiH2uMWyQ.png)

3\. Declare a string variable named ‘ **varQuery** ’ and set its value to “$top=5000&$orderby=ID.”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3vHOcReFd0uEyIUx5Lc5wA.png)

4\. Set up an array variable called ‘ **varAllData** ’ which will be utilized later for data population.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-YfYSZT6B9CaxJKuLJFf2Q.png)

5\. Implement a ‘ **Do Until** ’ action with the condition that **‘varNextPageExists’** equals **‘false’**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jGvtGaAn8l4o9mqlYjqM5Q.png)

6\. Add below steps within the ‘Do Until’ loop:

6.1. Send an HTTP request to SharePoint

```c
_api/web/lists/getbytitle(‘DemoLargeList’)/items?@{variables(‘varQuery’)
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*65GnLCBS52RHZFP6VMMMsw.png)

6.2. Parse the JSON response from the HTTP request’s body

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4__9fWpohs9idynJyjlwrA.png)

> Note: Schema can be generated from the sample request. To send the HTTP request, Save and execute the flow. Copy the HTTP response and use it to generate the schema

6.3. Extract the ‘ **Title** ’ field from the ‘ **results** ’ object with required mapping

```c
Formula to use in From Field:
  body(‘Parse_HTTP_Response’)?[‘d’]?[‘results’]

Formula to use in Map Value field:
  item()?['Title']
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LsDW--H9PEY2HgDTyfHXgQ.png)

6.4. Utilize a ‘ **Compose** ’ action and label it as ‘Merge Data’and use below formula in Input field

```c
union(variables(‘varAllData’),body(‘Select’))
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MGzCahKS8aVWX1LZ1hvf6w.png)

6.5. Use a **‘Set Variable’** action to append the merged data to **‘varAllData’** The value should be the output of the previous **‘Compose’** action.

```c
outputs(‘Merge_data’)
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RZzkgJEtk6kDbdGuYonSGA.png)

6.6. Employ a conditional statement to check if the **‘\_\_next’** property exist in the body(‘Send\_an\_HTTP\_request\_to\_SharePoint’)

```c
contains(body(‘Send_an_HTTP_request_to_SharePoint’)?[‘d’], ‘__next’)
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yxvVAyOOOp0phTylJ56WIg.png)

6.7. If true, Use **‘Compose’** action to extract the query part from the **‘\_\_next’** URL using below formula

```c
last(split(body(‘Send_an_HTTP_request_to_SharePoint’)[‘d’][‘__next’], ‘?’)).
```

6.8. Use a **‘Set Variable’** action to update the value of **‘varQuery’** with the output of the above **‘Compose’** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yBRxVQM9ibDCBbyxtXX9Gw.png)

6.9. If False, Use a **‘Set Variable’** action to update the value of **‘varNextPageExists’** with **false**. This stops the Do until Loop

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xOdjJlfFrkOWXi6Tt2hkcg.png)

6.10. Use Compose action to verify the length of the ‘varAllData’ Array. This should be written outside of Do Until block

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bvJpYbtT9sSEe2KVN2dAhQ.png)

That’s It.

After all steps, the flow looks like this

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3pUnnka2j_d9nE0efmCp3g.png)

## Conclusion

By following this step-by-step guide, you can effectively retrieve data from a SharePoint list with more than 5000 items using Microsoft Power Automate.