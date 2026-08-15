---
title: "How to Automatically Send Excel Reports via Email Using Power Automate"
source: "https://medium.com/@arowoloabimbola04/how-to-automatically-send-excel-reports-via-email-using-power-automate-4bb0304c0b7c"
author:
  - "[[Arowolo Abimbola Victoria]]"
published: 2026-03-27
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
**The 15-Minute Setup That Saves You Hours**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GB9xPOvKEVxMDNhUAxEe0A.png)

**Stop doing manually what a computer can do for you every single day**

Let me paint a picture you might recognize.

It is 8:47 AM on a Monday. You have barely touched your coffee. And already, someone is pinging you: “Hey, did you send the weekly sales report?” You open your laptop, find the Excel file, update the numbers, save it, open Outlook, type the same email you have typed 52 times this year, attach the file, and hit send. Ten minutes gone. Every. Single. Week.

Now multiply that by every recurring report your team sends. Monthly summaries. Weekly dashboards. Daily status updates. It adds up to hours of your life doing the exact same thing over and over again.

Here is the good news: you do not have to do that anymore. Power Automate can handle all of it for you, and you do not need to write a single line of code. In this article, I will walk you through exactly how to set it up, step by step, in plain English.

## What is Power Automate and Why Should You Care?

If you have never used Power Automate before, think of it like this: it is a tool that watches for things to happen and then does something in response. “When this happens, do that.” Simple.

In Microsoft’s world, it lives alongside Excel, Outlook, Teams, and SharePoint. If you already use Microsoft 365 at work, you already have access to it. You just might not know it yet.

For Excel users specifically, Power Automate is like giving your spreadsheets legs. Your data no longer just sits there waiting for someone to do something with it. It can now go places, trigger things, and talk to people, all on its own.

## What We Are Building in This Tutorial

By the end of this article, you will have a flow (that is what Power Automate calls an automation) that does the following:

On a schedule you choose (daily, weekly, monthly), it will automatically grab your Excel file from OneDrive or SharePoint and send it as an email attachment to whoever you want, with a custom subject line and message body, without you lifting a finger.

Sounds good? Let us get into it.

## What You Need Before We Start

Before you start building, make sure you have these three things ready:

**1\. A Microsoft 365 account.** Power Automate is included in most Microsoft 365 business plans. If you can open Excel online, you almost certainly have access to Power Automate too.

**2\. Your Excel file stored in OneDrive or SharePoint.** This is important. Power Automate works with files in the cloud, not files saved locally on your computer’s hard drive. If your report lives on your desktop, move it to OneDrive first. I will show you exactly where it needs to be.

**3\. An Outlook email account (work or personal Microsoft account).** Power Automate connects natively with Outlook. If your company uses a different email provider, there are connectors for Gmail and others, but this tutorial will use Outlook.

That is all. No special skills needed. If you can use Excel, you can do this.

## Step 1: Move Your Excel File to OneDrive or SharePoint

If your Excel report is already in OneDrive or SharePoint, skip ahead. If not, here is what to do.

Open File Explorer on your computer and find the Excel file. Right-click on it and choose “Copy.” Then open your OneDrive folder (it looks like a cloud icon in your taskbar or file explorer) and paste the file there.

Alternatively, go to onedrive.live.com or your company’s SharePoint site, click “Upload,” and select your file.

One tip here: put the file in a folder with a clear name, like “Automated Reports.” This will make it easier to find when you set up the flow.

Also, make sure the file name does not change. Power Automate will look for a file with a specific name in a specific location. If you rename the file later, you will need to update the flow too.

## Step 2: Open Power Automate

Go to make.powerautomate.com in your browser. Sign in with the same Microsoft account you use for Excel and Outlook.

You will land on the Power Automate home page. It might look a little overwhelming at first, but do not worry. We only need a small piece of it today.

On the left sidebar, click “Create.” This is where you start building a new flow from scratch.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*U0M3K4iWfLF_hgU0zgyWMg.png)

## Step 3: Choose “Scheduled Cloud Flow”

After clicking “Create,” you will see a few options. Choose “Scheduled cloud flow.”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*b7cO2TZR2UdmwONTShMTVQ.png)

This is the type of flow that runs on a timetable, like every Monday at 8 AM, or the first day of every month, or every day at 7:30 AM. Perfect for recurring reports.

A small setup window will appear. Fill it in like this:

**Flow name:** Give it something descriptive. Something like “Weekly Sales Report Email” or “Monthly Finance Summary.” You will thank yourself later when you have multiple flows and need to find this one.

**Starting:** Choose the date and time you want it to run for the first time.

**Repeat every:** Set the frequency. For a weekly report, choose “1 Week.” For a daily report, choose “1 Day.” For monthly, choose “1 Month.”

Once you have filled that in, click “Create.”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vzxrxYGaz9CsNbC9eePZaw.png)

## Step 4: Your Flow is Open. Now Let’s Build It.

You are now inside the flow editor. You will see your trigger already there: “Recurrence,” which means “run on a schedule.” That is the first block.

Now you need to add the actual steps. Click the “New step” button right below the Recurrence block.

A search box will appear. This is where you search for the action you want to perform.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jx4o9XN4ub3zR4noW7EG7g.png)

## Step 5: Get the File Content from OneDrive

In the search box, type “Get file content.” You will see several options appear. Look for “Get file content” under the OneDrive for Business connector (if your file is in SharePoint, choose “Get file content” under the SharePoint connector instead).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YV94YUtC9A21hOuIOq377Q.png)

Click on it.

Now you need to tell Power Automate where your file is.

Click the “File” field. A file browser will appear. Navigate to your OneDrive or SharePoint folder and select your Excel file.

Once you select it, Power Automate will grab the file path automatically. You do not need to type anything manually.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XwHjqVJdKfuK1zOt3472tA.png)

This step essentially tells Power Automate: “Go to this location and get me this file.”

## Step 6: Send the Email with the File Attached

Click “New step” again.

In the search box, type “Send an email.” Look for “Send an email (V2)” under the Outlook connector. This is the one you want.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3U_YIz_SJmrR8ipvEjVqLw.png)

Click on it. Now you will see a familiar-looking email form. Fill it in like this:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*95P6jF2pObp8-chxi35_8w.png)

**To:** Type the email address of whoever should receive the report. You can add multiple recipients separated by semicolons.

**Subject:** Write your subject line. For example: “Weekly Sales Report for the Week of \[date\].” You can even make the date dynamic by clicking in the subject field and then clicking the lightning bolt icon to insert a dynamic value like “utcNow()” formatted as a date. But for now, a simple fixed subject line works perfectly.

**Body:** Write your email message. Something like: “Hi team, please find this week’s sales report attached. Let me know if you have any questions.”

**Attachments:** This is where it gets exciting. Click “Show advanced options” at the bottom of the email action. You will see two new fields: “Attachments Name” and “Attachments Content.”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*40QUp5SveNNQBedxFsSBWg.png)

For “Attachments Name,” type your file name exactly as it appears, including the extension. For example: Sales Report.xlsx

For “Attachments Content,” click inside the field. A blue “dynamic content” panel will pop up on the right. Look for “File Content” from the previous step you created (the “Get file content” step). Click on it.

This is the magic moment. You are telling Power Automate: “Take the file you just grabbed and attach it to this email.”

## Step 7: Save and Test Your Flow

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BpPJnIib8EozsvOn9xumfg.png)

You are almost done. Click “Save” at the top of the screen.

Now let’s make sure it works before you trust it with your real reports.

Click the “Test” button (top right corner). Choose “Manually” and click “Test.” Then click “Run flow.”

Give it about 10 to 30 seconds. Check the inbox of whoever you put in the “To” field (or use your own email address for testing). Your Excel file should arrive as an attachment.

If it worked, you will see green checkmarks next to each step in your flow. Congratulations. You just automated your first report.

If something went wrong, Power Automate will show you a red “X” on the step that failed, along with an error message. The most common issues are: the file was not found (double-check the file path), or permissions (make sure you have access to the file location). Both are easy to fix.

## Step 8: Turn It On and Let It Run

Once your test is successful, your flow is already live. It will run automatically at the schedule you set in Step 3.

You can check in on it anytime by going to “My flows” in the left sidebar of Power Automate. Click on your flow to see its run history, edit it, or turn it off temporarily.

## Pro Tips to Make This Even Better

Now that you have the basics working, here are a few things you can do to take this further:

**Make the subject line dynamic.** Instead of a static subject line, you can include today’s date automatically. In the Subject field, click “Add dynamic content” and insert an expression like `formatDateTime(utcNow(), 'dddd, MMMM d yyyy')`. Your emails will now say things like "Sales Report for Monday, March 27 2026" without you typing anything.

**Send to a distribution list.** Instead of listing individual emails, use a shared mailbox or a Teams channel email address. Easier to manage as your team grows.

**Add a condition to only send if the file was updated.** This is more advanced, but you can add a condition step that checks the “Last modified” date of the file and only sends the email if the file was updated in the last 24 hours. No update, no email. This prevents sending stale reports.

**CC yourself for peace of mind.** When you are just starting out, CC your own email so you always know when the flow ran. Once you trust it completely, remove yourself.

**Store your Excel file in a SharePoint document library that your whole team can access.** That way the report is always up to date and everyone can also view it directly, not just receive it in their inbox.

## The Most Common Questions People Ask

**“What if my Excel file is updated by someone else right before the email sends? Will the latest version be sent?”**

Yes. Power Automate pulls the file at the exact moment the flow runs. So whatever version exists in OneDrive or SharePoint at that moment is what gets sent. If someone updates it at 7:55 AM and your flow runs at 8:00 AM, the updated version will be sent.

**“Can I send the email to different people on different days?”**

Yes, but this requires a slightly more advanced setup with conditions or variables. It is very doable, just a bit more involved than what we covered here.

**“What if I want to send multiple Excel files in one email?”**

You can add multiple “Get file content” steps and add them all as separate attachments in the same email action. Just add additional rows in the Attachments section.

**“Does this work if I rename the Excel file?”**

No. If you rename the file, Power Automate will not be able to find it. You will need to update the file path inside the flow. This is why I recommend keeping your report file names consistent and stable.

## Why This Matters Beyond Just Saving Time

I want to end with something a little bigger than the technical steps.

When you automate repetitive tasks like this, you are not just saving 10 minutes on a Monday morning. You are building a system that works even when you are sick, on vacation, in a long meeting, or having a terrible day. Your reports go out. On time. Every time. Without you.

That is reliability. And in a work environment, reliability builds trust.

For you personally as someone growing in the Microsoft ecosystem, building these flows also does something important: it changes how you think about your work. You start seeing manual, repetitive tasks differently. Instead of just doing them, you start asking: “Could a flow do this for me?”

That shift in thinking is exactly what separates good Microsoft 365 users from great ones. And it is exactly the kind of value that Power Automate experts bring to their communities and organizations.

You have built your first one. The next 50 will come faster than you think.

*Have questions about this flow or want to share how it worked for you? Drop a comment below. And if you found this helpful, give it a clap or share it with a colleague who is still sending reports manually.*