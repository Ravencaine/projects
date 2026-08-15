---
title: "Tracking Changes: Capture and Restore Previous SharePoint Data Dynamically using PowerAutomate"
source: "https://medium.com/@michealogbeide19/change-log-tracker-using-power-automate-df587c872905"
author:
  - "[[Oluwamayowa Ogbeide]]"
published: 2024-06-30
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Hey there, welcome back to my blog! It’s been a while since my last post, and a lot has happened over the past month. Big news: I became a [Microsoft MVP](https://mvp.microsoft.com/en-US/MVP/profile/7f3eb151-87ba-48bd-be5b-80a63e284416) in Business Applications, focusing on Power Apps and Power Automate. And guess what? I’m the youngest MVP in Africa!

But let’s dive into today’s topic. I’ll show you how to create a change log tracker using Power Automate. This will help you keep track of changes made to items in a SharePoint list.

In my example, I want to capture all the previous data of an item before it was modified — not just one column, but the entire item.

Here’s the plan:

1. Whenever an item in the list is updated, we’ll grab the previous data and save it in a new list.
2. This process will only run when changes occur in any of three specific columns.

Ready to get started? We’ll create an automated flow with the trigger set to “When an item or a file is modified.”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vitkIOfBL1EcHWpRBvnFww.png)

Next, we’ll use the action called **“Get changes for an item or a file (properties only)”**. This step is crucial because it shows you exactly what changes have occurred in the item.

Here’s what to do:

1. **Add the Action**: Search for and select **“Get changes for an item or a file (properties only)”**.
2. **What This Action Does**: It compares the current version of the item with the previous version and highlights the changes. This means you’ll be able to see which properties or columns have been modified.

By using this action, you can pinpoint exactly what has changed in the SharePoint item.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*o-T7M7Bllk6CPBSkx1VEbg.png)

To set up this action, we’ll need to specify the SharePoint site and list we want to monitor for changes. Here’s how to do it step by step:

1. **Select the SharePoint Site and List**: Choose the site and list where you want to track changes.
2. **Set the ID**: Use the `ID` from the trigger “When an item or a file is modified”. This ID represents the item that was changed.
3. **Configure the “Since” Field**: For the “Since” field, use the dynamic content option called `Trigger Window Start Token`. This helps Power Automate know from what point in time it should start checking for changes.

These settings ensure that your flow accurately captures the changes made to items in your SharePoint list.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*6ITGIzepIqlOfF3kabbo4Q.png)

The next step is to add a condition to ensure that we only record the previous data when changes occur in any of the three specific columns we’re interested in.

Here’s how to set it up:

1. **Add a Condition**: In your flow, insert a new condition after the “Get changes for an item or a file (properties only)” action.
2. **Specify the Columns**: Set up the condition to check if any of the three columns you monitor have been changed.
- You’ll compare the value of each column’s “Has Changed” property from the previous action.
- For each column, look for the dynamic content labeled like `Has Column Changed`.

**Set the Logic**:

- The condition should check if `Has Column Changed` OR `Has Column Changed 2` OR `Has Column Changed 3`.
- Use “Or” logic to combine these checks. This way, if any of the specified columns have been changed, the condition will be true.

**Define the Actions for True**:

- If the condition is met (i.e., changes occurred in one of the specified columns), proceed with your actions to record the previous data.

**Define the Actions for False**:

- If no changes are detected in the specified columns, the flow can either end or continue with other steps as needed.

This condition ensures that the flow only triggers the data recording process when one of the specified columns has been updated

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*SmRHmzQPdWLaOWfqw2YgBw.png)

To set up the condition to monitor specific column changes, follow these steps:

**Add the Condition Action**:

After the “Get changes for an item or a file (properties only)” action, add a **Condition** action to your flow.

**Configure the Condition**:

- In the condition’s settings, you’ll specify the logic to check if any of your three target columns have changed.

**Use Dynamic Content**:

- Use the dynamic content from the “Get changes for an item or a file” action.
- For each column you’re monitoring, look for the “Has \[Column Name\] changed” option.

**Set the Condition Logic**:

- Add each column’s “Has \[Column Name\] changed” dynamic content to the condition.
- Use the **“Or”** condition so that any change in the specified columns will trigger the flow.
- Set the value for each to **“true”**.

Here’s how to do it step-by-step:

**Add the Condition**:

- Click on “Add an action” after the “Get changes for an item or a file” action.
- Search for and select **Condition**.

**Configure the First Condition**

- In the left field of the condition, click on “Choose a value”.
- From the dynamic content panel, select **“Has \[Column1\] changed”**.
- Set the comparison to **“is equal to”**.
- Set the value to **“true”**.

**Add More Conditions with “Or”**:

- Click on **“Add row”** to add another condition within the same condition block.
- Repeat the steps to add **“Has \[Column2\] changed”** and **“Has \[Column3\] changed”**.
- Ensure you set the logical operator to **“Or”**. This way, the condition will be true if any of these columns have changed.

**Your Condition Should Look Like This**:

- **“Has Column1 changed” is equal to true**  
	**OR**
- **“Has Column2 changed” is equal to true**  
	**OR**
- **“Has Column3 changed” is equal to true**
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Quy47TdrF8xIkbn6yC67GA.png)

To get the previous data of the changed item in SharePoint, we'll use the **"Send an HTTP Request to SharePoint"** action. This will allow us to retrieve the item's data before the changes were made. Here's how to set it up:

## Steps to Configure the HTTP Request:

**Add the "Send an HTTP Request to SharePoint" Action**:

- In your flow, click **"Add an action"** after the condition we set up earlier.
- Search for and select **"Send an HTTP Request to SharePoint"**.

**Select Your SharePoint Site**:

- In the **"Site Address"** field, choose the SharePoint site you are monitoring.

**Set the Method**:

- Set the **"Method"** to **GET**. This tells SharePoint that we want to retrieve information.

**Input the URI**:

- In the **"Uri"** field, input the following URI format:
```c
_api/lists/GetByTitle('List Name')/items(Tiggerid)/versions?$filter=VersionLabel eq'sub(decimal(triggerOutputs()?['body/{VersionNumber}']),1)'
```

List Name — The list you want the previous data retrieved  
Trigger id — Trigger action Id  
Expression — sub(decimal(triggerOutputs()?\[‘body/{VersionNumber}’\]),1)- This retrieves the Version number and subtract 1 from it to only bring in the previous data before the change.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*OTleo3VuUsJglSOELnbRlA.png)

After retrieving the version history of the item from SharePoint using the "Send an HTTP Request to SharePoint" action, the next step is to parse the JSON response so that we can work with the data in Power Automate. Here’s how to set up the Parse JSON action:

## Steps to Configure the Parse JSON Action:

**Add the "Parse JSON" Action**:

Click on **"Add an action"** after the "Send an HTTP Request to SharePoint" action.  
Search for and select **"Parse JSON"**.

**Configure the Action**:

- In the **"Content"** field, select the dynamic content **"Body"** from the "Send an HTTP Request to SharePoint" action. This is the JSON response containing the version history of the item.

**Generate the Schema**:

- Click on **"Generate from sample"** to automatically generate the schema based on a sample JSON response.
- To generate the sample, you can run your flow up to this point and make a test call to the SharePoint action to retrieve the JSON response. This will provide a sample of the data structure that you can use to generate the schema.

**Define the Schema**:

Once the sample JSON response is populated, click **"Done"** to generate the schema.

- Power Automate will parse the JSON response based on the schema, allowing you to access specific properties and values in subsequent actions.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*P5LwQShCfrKQnnmWFdVUFA.png)

Finally use an apply to each:  
For the output use this expression

```c
body('Parse_JSON')?['d']?['results']
```

The full expression `body('Parse_JSON')?['d']?['results']` navigates through the JSON data output from the `Parse_JSON` action to retrieve the `results` array (or object) within the `d` property.

This is a common pattern when working with JSON responses from web services, particularly those following OData conventions. Here’s a step-by-step breakdown:

1. **Retrieve the body of the** `**Parse_JSON**` **action's output**: `body('Parse_JSON')`.
2. **Safely access the** `**d**` **property**: `['d']` with a null-check (`?`).
3. **Safely access the** `**results**` **property**: `['results']` with a null-check (`?`).
- In this case, `body('Parse_JSON')` would get the entire JSON response.
- `['d']` accesses the `"d"` object containing the `"results"` array.
- `['results']` then retrieves the actual array of items, which you can further process within your flow.

Next, select the Create an item for Sharepoint:  
Use this Expression for each column —

```c
body('Parse_JSON')['d']['results'][0]['PatientName']
```

The expression `body('Parse_JSON')['d']['results'][0]['PatientName']` in Power Automate is used to navigate through a nested JSON structure to retrieve the `PatientName` of the first item in the `results` array.

I hope this was informative, stay tuned for this next Post😁.