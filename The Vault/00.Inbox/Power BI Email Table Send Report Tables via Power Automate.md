---
title: "Power BI Email Table: Send Report Tables via Power Automate"
source: "https://databear.com/send-power-bi-table-email/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-07-20
created: 2026-08-04
description: "Send a Power BI email table with Power Automate. Learn to extract and send filtered report tables via email in HTML format—step-by-step."
Processed: "Unprocessed"
---
Need to send a **Power BI email table** without sharing the full report? In this guide, you’ll learn how to email just the filtered table data using Power Automate. Unlike Power BI subscriptions, which only send full-page visuals as PDFs or images, this method lets you email dynamic tabular data in a structured HTML format.

Whether you’re a report developer or business user, this technique saves time and improves targeted data sharing.

##### Why Send Table Data via Email?

Most Power BI users rely on report subscriptions but these only send static snapshots of entire pages. With this solution, you can send just the table content relevant to a selected date range, department, or segment.

By using Power Automate, you can:

- Filter report data on the fly
- Format it into a clean HTML table
- Email it directly to stakeholders

This enables a **Power BI email table** experience that’s dynamic and scalable.

##### Step 1: Prepare Your Table in Power BI

Start with a report that includes a table visualization. For example, a table showing **Year, Month, Day**, and **Total Sales**, filtered using a date slicer.

Filter your visual to display the desired data (e.g., August sales), which we’ll extract and email.![Prepare Your Table in Power BI](99.System/Attachments/Prepare_Your_Table_in_Power_BI.png)

##### Step 2: Add the Power Automate Visual

1. Add the **Power Automate visual** from the Visualizations pane.
2. Drag in the fields you want to include: Year, Month, Day, and Total Sales.
3. Click the visual’s **ellipsis (⋯)** and select **Edit** to configure the flow.![Add the Power Automate Visual](99.System/Attachments/Add_the_Power_Automate_Visual.png)

##### Step 3: Build Your Flow in Power Automate

Click **Create New** to launch a new **Instant Cloud Flow**. Then, build your flow as follows:

##### ➤ Use the “Select” Action

This action shapes the table structure:

- **From**: Choose “Power BI Data”
- **Map**: Define column/value pairs like:
	- Year → `Power BI data - Year`
		- Month → `Power BI data - Month`
		- Day → `Power BI data - Day`
		- Total Sales → `Power BI data - Total Sales`

##### ➤ Create an HTML Table

Add the **Create HTML Table** action:

- **From**: Use the output from the Select step.

##### ➤ Send an Email

Add the **Send an Email (V2)** action:

- **To**: Enter the recipient’s email
- **Subject**: “Total Sales for August”
- **Body**: Insert the HTML table output
- Optionally add a timestamp or dynamic content

Rename your flow (e.g., “Send Table via Email”) and save it.![Send an Email](99.System/Attachments/Send_an_Email-1.png)

##### Step 4: Trigger the Flow from Power BI

Return to Power BI Desktop and customize the Power Automate button:

- Rename it (e.g., “Send to Email”)
- Test it by selecting a date range and clicking the button

Check your **Power Automate dashboard** under “My Flows” to confirm the flow ran successfully. Then, open your email to view the sent data.![Trigger the Flow from Power BI](99.System/Attachments/Trigger_the_Flow_from_Power_BI.png)

##### Troubleshooting Tip

If the table appears summarized or incorrect:

- Select the Power Automate visual
- Ensure the fields in the Values section are not being aggregated (e.g., no “Sum of”)

Click **“Don’t Summarize”** where necessary and re-run the flow.

##### Final Output

Once configured, you’ll receive a well-formatted HTML email containing only the table data you filtered for. This is far more efficient than sending entire reports and allows you to automate routine data sharing.

##### Why This Matters

This workflow is perfect for:

- Sales teams needing quick performance snapshots
- Managers who only need specific slices of data
- Automating regular email updates without exporting data manually

Using Power BI with Power Automate enhances your reporting toolkit, providing precision and flexibility in how you distribute data.

##### Learn More

Want to deepen your Power BI and automation skills? Join our [Advanced Power BI Boot Camp](https://databear.com/power-bi-training/) and get expert-led training on Power Automate, RLS, data modeling, and more.