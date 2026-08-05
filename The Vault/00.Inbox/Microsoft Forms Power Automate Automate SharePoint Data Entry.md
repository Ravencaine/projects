---
title: "Microsoft Forms Power Automate: Automate SharePoint Data Entry"
source: "https://databear.com/microsoft-forms-power-automate/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-11-07
created: 2026-08-04
description: "Automate SharePoint data entry with Microsoft Forms and Power Automate. Save time, reduce errors, and simplify your workflow instantly."
Processed: "Unprocessed"
---
When you’re working with student data, surveys, or feedback forms, automation can save hours of manual work. **Using Microsoft Forms Power Automate**, you can automatically write form responses to a SharePoint list no manual data entry required. In this guide, we’ll walk you through the full process step-by-step.

##### Step 1: Set Up Your SharePoint List

Start by creating a **[SharePoint](https://databear.com/power-bi-april-update/ "Power BI April Update Overview") list** to store your data. For this example, we’ll track student birthdays and email addresses.

Your SharePoint list should include:

- **Title** (student name)
- **Birthday** (date)
- **Email** (text)

You can name the list something descriptive, such as **Student Birthdays**. Once created, leave this open we’ll connect to it later in Power Automate.![Set Up Your SharePoint List](99.System/Attachments/Set_Up_Your_SharePoint_List.png)

##### Step 2: Create a Microsoft Form

Next, head to **Microsoft Forms** and create a new form called **Birthday Entries for Students**.  
Add three questions that align with your SharePoint columns:

1. **Student Name** (Text)
2. **Birth Date** (Date)
3. **Student Email** (Text)

This simple form will serve as your data collection tool. Microsoft Forms is a great option for educators because it’s quick to set up, mobile-friendly, and integrates seamlessly with the rest of the Microsoft ecosystem.

##### Step 3: Build Your Flow in Power Automate

Now that the form is ready, let’s automate the process.

1. Go to **Power Automate** → **Create** → **Automated Cloud Flow**.
2. Give your flow a name — for example, *Microsoft Form → Write to SharePoint*.
3. Choose the trigger **“When a new response is submitted”** and click **Create**.

This trigger watches your form for new submissions.![Build Your Flow in Power Automate](99.System/Attachments/Build_Your_Flow_in_Power_Automate.png)

##### Step 4: Get Form Response Details

After setting your trigger, Power Automate needs to know which form and which response to use.

- Under **Form ID**, choose your form (*Birthday Entries for Students*).
- Add a new action called **Get response details**.
- Again, select your form and choose **Response ID** from the dynamic content menu.

This ensures that each response submitted through the form will be retrieved automatically.![Get Form Response Details Microsoft Forms Power Automate](99.System/Attachments/Get_Form_Response_Details_Microsoft_Forms_Power_Automate.png)

##### Step 5: Write Data to SharePoint

Now let’s connect Power Automate to your SharePoint list.

1. Add a new action called **Create item** (under the SharePoint connector).
2. Select your **Site Address** and **List Name** (*Student Birthdays*).
3. Map your fields using dynamic content:
	- **Title** → *Student Name*
		- **Birthday** → *Birth Date*
		- **Email** → *Student Email*

This mapping ensures that every new form submission is saved correctly to the corresponding SharePoint columns.![Write Data to SharePoint Microsoft Forms Power Automate](99.System/Attachments/Write_Data_to_SharePoint_Microsoft_Forms_Power_Automate.png)

##### Step 6: Test the Flow

Once your flow is set up, save it and click **Test**.  
Choose **Manual test**, then submit a sample entry through your Microsoft Form.  
If everything is working correctly, you’ll see green check marks in Power Automate and your new record will instantly appear in the SharePoint list.

You’ve successfully automated your data entry process! ![Test the Flow Microsoft Forms Power Automate](99.System/Attachments/Test_the_Flow_Microsoft_Forms_Power_Automate.png)

##### Step 7: Optional Add an Approval Step

Want to take it further? You can add an **approval step** after the form submission. For example:

- Send a confirmation email to the parent or student asking them to verify the information.
- If they approve, the data is written to SharePoint.
- If not, they’re redirected to re-submit the form.

This ensures accuracy and gives users control over their submissions.

##### Key Takeaways

By connecting **Microsoft Forms**, **Power Automate**, and **SharePoint**, you can:

- Eliminate manual data entry.
- Improve data accuracy and consistency.
- Save valuable time for teachers, administrators, or team leads.

This workflow is perfect for educators managing class data, HR teams collecting employee info, or project managers tracking client details.

##### Conclusion

Using **Power Automate** to link Microsoft Forms to SharePoint is a simple yet powerful way to streamline your workflow. Once configured, you’ll never have to manually copy form responses again the automation does it for you.

If you’d like to expand your Power BI and Power Platform skills, explore the training programs available at [DataBear Power BI Training](https://databear.com/power-bi-training/).