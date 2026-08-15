---
title: "Power Automate: How to delete SharePoint Files and Folder"
source: "https://medium.com/@domliu37/power-automate-how-to-delete-sharepoint-files-and-folder-97999ca14301"
author:
  - "[[Dominic Liu]]"
published: 2024-06-25
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Building a scheduled Flow to delete SharePoint files and folders is essential, especially if you have a Dynamics 365 environment integrated with your SharePoint. After a record has been retained for a certain number of years, you may reach a point where you need to delete it from your system. However, simply deleting the record directly in D365 will not delete the corresponding files on the SharePoint side, which means you will end up with a lot of junk data in your SharePoint.

In this blog, I will show you how to use Power Automate to delete SharePoint files and folders.

### Trigger of the Flow:

Select Recurrence trigger. In my example, I’d like to have my flow to run at 5am everyday.

![](https://miro.medium.com/v2/resize:fit:1204/format:webp/1*9xLmlpyiYZTAgqAz5Z6FXw.png)

### Step 1: Get the all Accounts created on over 10 years

This is just my example; you can modify your trigger as long as you have a list of accounts to be deleted.

![](https://miro.medium.com/v2/resize:fit:1202/format:webp/1*7U94LU1WX9XVh4kpydCXpw.png)

### Step 2: Get the ‘relativeurl’

The ‘relativeurl’ column is from the Document Location table. We need that column in order to find the correct SharePoint Item.

![](https://miro.medium.com/v2/resize:fit:1214/format:webp/1*Be79xnY_iOUZrruawwYw1A.png)

### Step 3: Get Files

Using the OOTB SharePoint action in Flow to get all the files you want to delete; Things to be aware:

1. Include Nested Items meaning you are retrieving files from the Subfolder.
2. By Default, Get Files action treat Subfolder as a ‘File’, so we use this ODATA query to get the actual files only, not any subfolders.  
	FSObjtype eq 0
![](https://miro.medium.com/v2/resize:fit:1300/format:webp/1*H6lw7WIliOFcLGWkVJtU2g.png)

### Step 4: Delete File

Use the SharePoint Delete File action to delete the file, using the Identifier column from the Step 3 — Get Files

![](https://miro.medium.com/v2/resize:fit:1220/format:webp/1*El6dFSEMCftltk0RdyTuvQ.png)

### Step 5: Delete Folder

Unfortunitely, at this time, we still dont have a built in action in Power Automate to delete SharePoint folder, so we have to use the ‘Send an HTTP request to SharePoint’ to delete the folder.

![](https://miro.medium.com/v2/resize:fit:1228/format:webp/1*2Tq4ne7xOkE1Pm2cHXBoBg.png)

*Please note that this step will fail, if your folder contains sub folders.*

Now that the SharePoint side of things is all done, you can continue using your flow to delete the target record. Thanks to the cascading rule, the related Document Location record will also get deleted.

Hope this blog helps you.