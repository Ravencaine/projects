---
title: "How to Compress Excel Documents, Email the Archive in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-compress-excel-documents-email-the-archive-in-power-automate-665cdc028f2e"
author:
  - "[[Cloudmersive]]"
published: 2025-02-05
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Excel files can get pretty bulky. If we’re emailing a number of Excel files at once, we can quickly find ourselves up against attachment size-limit constraints.

Compressing our files to ZIP archives solves that problem, but we’re still left with the inefficient multi-step process of **1)** dragging Excel docs into an archive, **2)** naming and saving that archive, and **3)** creating the email to share the archive in.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*psD6A9HPb4AYqtzTgY69xA.jpeg)

Thankfully, in Power Automate, we can combine all those steps into one single workflow.

Using the **Cloudmersive File Processing** connector, we can compress multiple Excel files into a ZIP archive at once. Downstream of that, we can simply attach our ZIP archive to an email & send that email as part of our flow using one of the many email connectors available on the Power Automate platform (e.g., O365 outlook, Gmail, etc.).

Below, we’ll walk through a reusable instant cloud flow which accepts multiple file inputs, compresses those inputs to a ZIP archive, and emails the archive to a recipient.

### Creating Manual triggers

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Q3yn4bzuR6lDzediSqEuzg.png)

In the **Manually trigger a flow** window of an **Instant cloud flow**, we can create several input fields for flow users. In this example, we’ll create a series of file input fields (in this case only 3, but we can create up to 10 for our ZIP compression action) along with 3 text input fields.

Our file input fields will allow flow users to select Excel files from their file system, and our text input fields will allow users to enter the subject of their email, message of their email, and name of the ZIP archive.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*V3cirt9yF3u1NfLdwZVBaQ.png)

### Compressing Excel Inputs to a ZIP Archive

In our next step, we’ll find the **Cloudmersive File Processing** connector in Power Automate.

We can do this by typing “Cloudmersive” into the search bar (the **File Processing** connector has a purple logo).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*v3GBu72lSmPsT5RBMm3drQ.png)

After clicking “See more” to view the full actions list, we’ll find the **Compress files to create a new zip archive** action fifth on our alphabetically organized actions list. We’ll select it once we find it.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WpNUIH6CtJ0tRiZuDUjSUw.png)

### Creating a Cloudmersive API connection

When we select this action, our first order of business is creating a **Cloudmersive Document Conversion** connection. We’ll need a free API key to do that, and we can get one by registering a free account on the Cloudmersive website (free API keys allow up to 800 API calls/month with zero commitment).

### Configuring the ZIP archive compression step

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MV7V5GPzY5oDq64HTC2kLQ.png)

We’ll now configure our request. To start, we’ll enter our first set of input file bytes & that file’s name into the first two parameters (both of these options are available as dynamic content from our manual trigger).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YH_Llbu0E_iuAFUMtCTBgA.png)

To compress the rest of our files, we’ll click “Show all” to view the advanced parameters, and we’ll enter our remaining input file byte/file name combinations into the first two sets of file input/file name parameters.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*suSDZ0VwvT0Z6zCNzjT5vA.png)

At this point, we’ve successfully assembled our ZIP archive full of compressed Excel documents; all that’s left now is our email.

### Customizing an Outlook 365 email & adding the ZIP attachment

In this example, we’ll send our email using the **Outlook O365** connector. Specifically, we’ll leverage the **Send an email (V2)** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9FDqHGrOkC4BYG0KHXWRzA.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-DYQIDkAy7TZGvS7rAsPPA.png)

For now, we’ll enter our own email address into the **To** field (later, after we’ve tested our flow successfully, we can ask users to input a recipient email along with the other manual triggers).

We’ll then pass our Email subject and body text inputs to the **Subject** and **Body** fields respectively.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NskrWFTIxn1BYczMWsNOig.png)

Finally, to attach our ZIP file and name it, we’ll click “Show all” to view the advanced parameters, and we’ll click **Add new item** in the **Attachments** parameter.

We’ll pass our ZIP attachment name text input & **OutputContent** values in the **Name** and **Content** fields respectively.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1PWU4phPrl-DqaG6VikMYg.png)

### Testing the flow

At this point, we’ll save our flow and set our inputs.

That means selecting 3 Excel files from our file system, providing Email subject & body text, and giving our ZIP archive a relevant name.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*U8LSnvYLaFnmITmGUP4U5g.png)

After we run our flow, we’ll find our new Excel archive attached to an email in our inbox.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PqJZMuTu7y9KAcKDAOLhlg.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8VvSOMqgzjbGImSljTZNnA.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*j-kUBIynPtZvkUz1pCfeqA.png)

And that’s all there is to it! In just a few quick steps, we assembled and emailed an Excel ZIP archive.

### Conclusion

In this article, we learned how to leverage the **Cloudmersive File Processing** connector in Power Automate for assembling and a quick ZIP archive on the fly. We learned how easy it is to subsequently email that archive with direct input from the user at every level of the process.

If you’re interested in learning more Power Automate tips, remember to check back in on our daily blog!