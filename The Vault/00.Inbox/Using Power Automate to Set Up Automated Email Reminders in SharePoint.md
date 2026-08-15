---
title: "Using Power Automate to Set Up Automated Email Reminders in SharePoint"
source: "https://medium.com/@python-javascript-php-html-css/using-power-automate-to-set-up-automated-email-reminders-in-sharepoint-134640a3121e"
author:
  - "[[Denis Bélanger 💎⚡✨]]"
published: 2024-07-29
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*awsqxl1sGrDOQCcw9KWFcw.jpeg)

## Automating Email Notifications for Due Dates in SharePoint

## [Temp Mail - Generate Temporary Email Addresses for Free](https://www.tempmail.us.com/?source=post_page-----134640a3121e---------------------------------------)

### Disposable email accounts generator including sending emails, 10 minutes mail, fake email, burner email, mail…

www.tempmail.us.com

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tkRdMwSimRNhmIDOAc8O3w.jpeg)

Managing deadlines effectively within any organization can be streamlined using automated tools like **SharePoint** and Power Automate. When working with SharePoint libraries that include date-specific data, it becomes crucial to ensure timely communications. This scenario often involves setting up **flows** to send notifications well before the due dates to keep all stakeholders informed. For instance, automating **reminder** emails 60 and 30 days before an impending deadline could significantly enhance **project management** and ensure no deadlines are missed.

However, implementing these reminders can sometimes become a technical challenge, particularly when conditions within the flow do not trigger as expected. Many users face difficulties with variables and date formats which do not seem to cooperate, leading to frustrating errors. The objective is to have Power Automate reliably fetch and compare dates from a SharePoint library to the current date, thereby facilitating timely automated responses that are crucial for maintaining workflow continuity and project success.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VzvdsMP1yKUhE0ypVrXq0g.png)

## Understanding Automated Reminder Setups in SharePoint

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yG0eZ4_xef-vJYQkJwHFxw.jpeg)

The scripts provided above are designed to facilitate the automation of sending reminder emails from a SharePoint list using Power Automate and PowerShell. These scripts are essential for project management scenarios where timely reminders can help manage deadlines effectively. The first script uses Power Automate to trigger a flow when an item in a SharePoint library is modified or created. It initializes variables to store the due date and today’s date formatted correctly. The logic checks if the due date is in the future compared to today’s date. If true, it computes dates 60 and 30 days before the due date. Depending on whether today’s date matches either of these computed dates, an email is sent. This setup ensures that stakeholders receive reminders at critical times, enhancing the management of project deadlines.

The second script employs PowerShell to integrate with SharePoint and perform similar date comparisons and email triggering based on conditions. It connects to a SharePoint site, retrieves items from a specified list, and iterates through each item to check if the current date matches 60 or 30 days before the due date stored in each item. Commands like *Connect-PnPOnline* and *Get-PnPListItem* are pivotal for accessing SharePoint data, while *Get-Date* and item property accessors like *$item\[“DueDate”\]* are used to manipulate and compare dates. These scripts exemplify how to automate complex workflows within SharePoint to improve operational efficiency and ensure no task falls through the cracks due to missed reminders.

## Implementing Automated Due Date Reminders in SharePoint via Power Automate

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yG0eZ4_xef-vJYQkJwHFxw.jpeg)

Power Automate Flow Script

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fCJcEyJDeoh8347L5oq7LA.png)

```c
Trigger: When an item is created or modified
Action: Initialize variable - Type: String, Name: DueDate, Value: formatDateTime(items('Apply_to_each')?['DueDate'], 'yyyy-MM-dd')
Action: Initialize variable - Type: String, Name: TodayDate, Value: utcNow('yyyy-MM-dd')
Condition: Check if DueDate is greater than TodayDate
If yes:
    Action: Compose - Inputs: addDays(variables('DueDate'), -60, 'yyyy-MM-dd')
    Action: Compose - Inputs: addDays(variables('DueDate'), -30, 'yyyy-MM-dd')
    Condition: Is today 60 days before due?
    If yes:
        Action: Send an email (V2) - To: UserEmail, Subject: 'Reminder: 60 days before due', Body: 'There are 60 days left until the due date.'
    Condition: Is today 30 days before due?
    If yes:
        Action: Send an email (V2) - To: UserEmail, Subject: 'Reminder: 30 days before due', Body: 'There are 30 days left until the due date.'
If no:
    Terminate: Status - Cancelled
```

## Backend Logic for Date Comparisons in SharePoint

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yG0eZ4_xef-vJYQkJwHFxw.jpeg)

PowerShell Script for SharePoint and Power Automate Integration

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qoIiKYm5QMOYe7Cr7m-e1Q.png)

```c
$SiteURL = "Your SharePoint Site URL"
$ListName = "Your List Name"
$Creds = Get-Credential
Connect-PnPOnline -Url $SiteURL -Credentials $Creds
$Items = Get-PnPListItem -List $ListName
foreach ($item in $Items)
{
    $dueDate = [datetime]$item["DueDate"]
    $daysAhead60 = $dueDate.AddDays(-60)
    $daysAhead30 = $dueDate.AddDays(-30)
    $currentDate = Get-Date
    if ($daysAhead60 -eq $currentDate.Date)
    {
        # Send Email Logic for 60 days reminder
    }
    if ($daysAhead30 -eq $currentDate.Date)
    {
        # Send Email Logic for 30 days reminder
    }
}
```

## Enhancing Workflow Automation with SharePoint and Power Automate

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yG0eZ4_xef-vJYQkJwHFxw.jpeg)

One key aspect of using SharePoint and Power Automate together is their ability to streamline workflow processes and improve efficiency in document management systems. SharePoint libraries are widely used for their robust handling of documents and metadata, including due dates critical for project management. By integrating Power Automate, users can automate actions based on these metadata fields, such as sending timely reminders. This capability not only ensures better adherence to deadlines but also reduces the manual effort required to monitor dates and send out notifications, thereby significantly reducing errors and improving operational efficiency.

Moreover, SharePoint’s integration with Power Automate allows for greater customization and flexibility in handling complex workflows. Users can design flows that trigger under specific conditions, send customized emails, and even manage exceptions, such as delayed projects or changed due dates. This adaptability is crucial for businesses that operate under tight schedules or require frequent updates to their project timelines. By leveraging these tools, organizations can ensure that every team member stays informed about upcoming deadlines and project milestones without manual oversight, leading to smoother project execution and enhanced team coordination.

## Frequently Asked Questions on SharePoint Date Reminders

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yG0eZ4_xef-vJYQkJwHFxw.jpeg)

How do I set up a reminder in SharePoint?

Use Power Automate to create a flow that triggers email notifications based on the date column in your SharePoint library.

Can Power Automate send reminders before a specific date?

Yes, you can configure the flow to send emails a specific number of days before the date stored in a SharePoint column.

What if the reminder flow isn’t triggering?

Check that your date comparisons are correctly formatted and that the flow’s conditions are set up to accurately evaluate date differences.

Can I customize the email sent by Power Automate?

Absolutely, Power Automate allows you to customize the email body, subject, and recipients as part of the flow design.

What is the best practice for date formats in SharePoint?

It is recommended to use ISO 8601 format (YYYY-MM-DD) to avoid regional format issues in calculations and comparisons.

### Key Takeaways and Next Steps

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MtDvT7rvXrt-QJsjA2_YKQ.jpeg)

Setting up automated **reminders** in **SharePoint** using Power Automate is a practical solution that can significantly enhance **project management** by ensuring that all stakeholders are aware of upcoming deadlines. The process involves configuring **flows** to send out emails at predetermined times, such as 60 and 30 days before a due date. This system helps prevent missed deadlines and promotes better time management within teams. However, challenges such as incorrect date formatting or conditions not being met can impede the **flow’s** effectiveness. It’s crucial for users to ensure that the date formats are consistent and to thoroughly test the **flow** to verify that it triggers as expected. For those struggling with these setups, consulting documentation or seeking help from forums could provide additional guidance. Implementing these automated **reminder** systems ultimately contributes to more streamlined operations and improved project outcomes.

[**Using Power Automate to Set Up Automated Email Reminders in SharePoint**](https://www.tempmail.us.com/en/sharepoint/setting-up-automated-email-reminders-in-sharepoint-with-power-automate)