---
title: "Power Automate to refresh a Power BI report"
source: "https://databear.com/power-automate-to-refresh-a-power-bi-report/"
author:
  - "[[Annamarie Van Wyk]]"
published: 2022-12-19
created: 2026-08-04
description: "Learn how to use Power Automate to refresh your Power BI report automatically. From email attachment received to refresh. Easy steps."
Processed: "Unprocessed"
---
## Use Power Automate to refresh your Power BI report

Today I’ll show you how to use [Power Automate](https://powerautomate.microsoft.com/en-us/) to refresh a Power BI report automatically.

Let me set the scenario for you. I have a report that is dependent on an email from the bank. So I have set up a flow to trigger when the email is received. It takes the excel attachment and places it in a folder on sharepoint, then another flow detects a new file and that is the trigger to refresh the report. I’m sure I could do it in one flow, but my power automate experience is not that advanced and this worked for me.

### Step 1: Create flow

First you need to set up the Power Automate flow to identify the email you are waiting for.

In this example the email will come from [an\*\*\*\*\*\*@gmail.com](mailto:an******@gmail.com) and the subject is simply Excel File attached.

Head over to power automate – this will be available to you if you have an office 365 tenant account.

![Create Power Automate](99.System/Attachments/Create_Power_Automate.png)

### Step 2: Choose your trigger

Choose the option to build your own flow. Once you are in building / editing mode, search for outlook and choose the below option. This is your trigger. When a new email arrives.

![Flow option to choose](99.System/Attachments/Flow_option_to_choose.png)

This is your first step, it’s really straight forward you just fill in what is asked, and only what is relevant for your case. See step 1 what my detail was.

![When email arrives](99.System/Attachments/When_email_arrives.png)

Make sure that you give enough details for the flow to recognise the email. Perhaps have a rule on this email for it to go to a dedicated folder will be good practice, but not necessary.

### Step 3: New step

Once you have completed this step, you need to assign the next action to the flow. In laymens terms, what to do with the attachment.

![Add new step](99.System/Attachments/Add_new_step.png)

Choose the apply to each step, and then Attachments as the output.

![Apply to each](99.System/Attachments/Apply_to_each.png)

## Step 4: Add an action

Add an action to Create file in sharepoint.

Search for Create File, and choose the one with a Sharepoint icon. See below.

![Create File](99.System/Attachments/Create_File.png)

Fill out the details with your Site address and folder etc. It should all pop up in a drop down linked to your Microsoft account.

![Create File Detail filled in](99.System/Attachments/Create_File_Detail_filled_in.png)

For the File Name field, choose the Attachments Name option. Of course you could call it something else, there are some expression options like adding the Date / time of the file to the name, but this is up to you. I did add the date as a prefix, because I don’t want to override the file, I want a new one saved every time.

For the File Content, you will choose Attachments Content.

### Step 5: Send an email

In order to add more, choose the new step option. I used this step to send an email to me, in order for me to see when my flow has run. This step is not necessary if you do not required this Notification email.

Search for “Send an email”.

Choose the below option.

![Send an email](99.System/Attachments/Send_an_email.png)

Fill in the details.

![Send an email details](99.System/Attachments/Send_an_email_details.png)

Great, the first section of our goals is done.

Let’s test it. I sent the email. It was received and a few seconds later, the flow had run.

![Email proof](99.System/Attachments/Email_proof.png)

## Refresh the report

The next section is creating a flow to detect the new file, and this then triggers the refresh. This is last step in using Power Automate to refresh a Power BI report.

### Step 6: Create flow

Create a new flow, and search for Sharepoint. Then choose “When a file is created or modified in a folder”. Add the site and folder address of your sharepoint site.

![When a file is created or modified in a folder](99.System/Attachments/When_a_file_is_created_or_modified_in_a_folder.png)

### Step 7: Refresh report

Add a step to the flow and search for power bi, then simply choose Refresh a dataset. Now you add the location detail of your report.

![Flow to refresh report](99.System/Attachments/Flow_to_refresh_report.png)

That is it. Next you will test your flows.

I sent my email again, and it worked like a charm.

Email sent and flow ran.

![Email and flow received](99.System/Attachments/Email_and_flow_received.png)

Flow kicked off and the report started to refresh

![Refresh started automatically](99.System/Attachments/Refresh_started_automatically.png)

And see below how you use Power Automate to refresh a Power BI report.

![Refresh done](99.System/Attachments/Refresh_done.png)

Don’t forget to head over to our [training page](https://databear.com/power-bi-training/) for great training courses.