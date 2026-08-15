---
title: "Automate Flow and Sharepoint Lists"
source: "https://medium.com/@aameti/automate-flow-and-sharepoint-lists-c60eebcb58cb"
author:
  - "[[Abdul Ameti]]"
published: 2024-04-04
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
Why is it helpful?

Automating email flows and SharePoint list updates brings practical benefits to your workflow. It saves time and effort by handling repetitive tasks, ensuring that reports are accurate and effortlessly generated. With standardized workflows, data remains consistent, reducing errors and discrepancies. Real-time updates keep stakeholders informed. The user experience is simplified, requiring minimal effort for users to interact effectively. Overall, automation reduces errors and streamlines processes, making work more efficient and manageable.

Of course, data increments dynamically.

1\. First, create a trigger condition: “When a new email arrives” (V3)

2\. Initialize the variable. This is the starting value of your string. For example **Subject.** In the code snippet below, the example **Subject Line** is:

```c
"Lorem Ipsum | Lorem Ipsum Dolor | ID 37493874"
```
```c
{
"inputs": {
"variables": [
{
"name": "Subject",
"type": "string",
"value": "Lorem Ipsum | Lorem Ipsum Dolor | ID 37493874"
}
]
},
"metadata": {
"operationMetadataId": ""
}
}
```

3\. Then, you concatanate, or split chunks of the strings respecting your pattern:

```c
{
"inputs": "@split(variables('Subject'), '|')[0]",
"metadata": {
"operationMetadataId": ""
}
}
```

What this regex code does is fetching any value before the ‘|’ separator with the \[0\] array.

Repeat the same for the next strings:

```c
{
"inputs": "@split(variables('Subject'), '|')[1]",
"metadata": {
"operationMetadataId": ""
}
```

Finally, insert the Outputs in your “Create item” (for Sharepoint) and that is it.

**How does it work from a user perpsective:**

1\. Create an email with a subject like this, for example:

This is a Title | And This Too | 5654877  
  
2\. Put [e](mailto:application-tracking-flow@flockconsulting.de) mail@example.com in BCC and leave the “To” **empty.**

3\. You will see that your Sharepoint Lists have been updated with the new data fetched from the Subject Line.

Of course, additionally you can also automate other fields. You can use the “Create Item” flow to dynamically populate any of your Sharepoint List fields.