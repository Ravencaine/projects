---
title: "Power BI RLS: Setup Row-Level Security & Dynamic Roles"
source: "https://databear.com/row-level-security-power-bi-guide/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-07-15
created: 2026-08-04
description: "Learn how to set up Power BI RLS, use the enhanced editor, and apply dynamic row-level security to control user data access in your reports."
Processed: "Unprocessed"
---
When sharing reports in Power BI, not everyone should see the same data. That’s where **Power BI RLS (Row-Level Security)** comes in. It allows you to restrict data access by defining user roles, so each person only sees what’s relevant to them.

In this comprehensive guide, you’ll learn how to:

- Set up basic RLS roles and filters in Power BI Desktop
- Assign users to roles in the Power BI Service
- Use the Enhanced RLS Editor for a more intuitive setup
- Implement **Dynamic RLS** for scalable, user-driven security

Let’s dive in.

##### What is Row-Level Security (RLS) in Power BI?

RLS lets you filter report data for individual users or groups based on their roles. This way, a sales manager in the U.S. sees only U.S. data, while a colleague in Germany sees only data relevant to their region.

The setup involves:

1. Creating roles and filters in Power BI Desktop
2. Assigning users to those roles in the Power BI Service

##### Step-by-Step: Basic RLS Setup in Power BI Desktop

Here’s how to create a basic RLS role:

1. Go to the **Modeling** ribbon in Power BI Desktop.![Go to the Modeling ribbon in Power BI Desktop](99.System/Attachments/Go_to_the_Modeling_ribbon_in_Power_BI_Desktop.png)
2. Click **Manage Roles**.![Click Manage Roles](99.System/Attachments/Click_Manage_Roles.png)
3. Create a new role (e.g., “USA”) and add a filter:
	- Select the `Customers` table → `Country` column
		- Apply filter: `[Country] = "USA"![Create a new role (e.g., “USA”) and add a filter:](99.System/Attachments/Create_a_new_role_(e.g.,_“USA”)_and_add_a_filter.png)`
4. Click **Verify DAX Expression** to ensure there are no errors.![Click Verify DAX Expression to ensure there are no errors](99.System/Attachments/Click_Verify_DAX_Expression_to_ensure_there_are_no_errors.png)
5. Create additional roles (e.g., “Germany”) as needed.

You can preview these roles using the **View As** feature in Desktop to confirm each role only sees its assigned data.

##### Assigning RLS Roles in the Power BI Service

Once your report is ready:

1. Publish the report to Power BI Service.
2. Go to your workspace → find the dataset → click the **ellipsis (⋯)** → select **Security**.
3. Assign users or groups to each RLS role.

: RLS only applies to users with **Viewer** access. Contributors, Members, and Admins will bypass RLS due to elevated permissions.![Assigning RLS Roles in the Power BI Service](99.System/Attachments/Assigning_RLS_Roles_in_the_Power_BI_Service.png)

##### Using the Enhanced RLS Editor

Writing DAX expressions can be tricky, especially for non-technical users. The **Enhanced RLS Editor** provides a drag-and-drop interface that simplifies role creation.

##### How to Enable It:

1. In Power BI Desktop, go to **Settings** → **Preview Features**.
2. Enable **Enhanced Row-Level Security Editor** and restart Power BI.

##### Benefits:

- Visually select tables and columns
- Use simple UI to define filters (e.g., “equals”, “does not equal”)
- Group filters for complex logic using “AND” / “OR” controls
- Toggle between UI and DAX editor with real-time conversion

This editor is perfect for beginners and teams who prefer a visual approach over writing code.![Using the Enhanced RLS Editor](99.System/Attachments/Using_the_Enhanced_RLS_Editor.png)

##### Advanced Security: Dynamic RLS

Dynamic RLS adapts report filtering based on who is logged in. This method is ideal for large teams or when user-role mappings are stored in tables.

##### Example Setup:

1. Create a **Permissions** table with columns: `Email`, `Country`.
2. Link `Country` to your `Customers` table in the data model.
3. In Manage Roles, switch to **DAX Editor** and apply this filter:
	```
	[Email] = USERPRINCIPALNAME()
	```

##### How It Works:

When a user views the report in the Power BI Service, the DAX function `USERPRINCIPALNAME()` returns their email. The model uses this to filter data dynamically, based on your permissions table.![How It Works:](99.System/Attachments/How_It_Works.png)

##### Tips for Effective RLS Implementation

- **Test Roles Thoroughly** using the “View As” feature.
- **Use Dynamic RLS** for scalability especially useful for large or growing teams.
- **Group filters** for multi-region or multi-role scenarios using Enhanced Editor.
- **Avoid assigning RLS to admins or contributors** unless testing.

##### Learn More and Take It Further

Want to master RLS and other advanced Power BI features? Join the [Advanced Power BI Boot Camp](https://databear.com/power-bi-training/) to get hands-on training, expert guidance, and demo files to accelerate your development.

##### Final Thoughts

RLS is essential for tailoring Power BI reports to different audiences without duplicating work. Whether you use basic roles, enhanced editing, or dynamic logic, securing your data appropriately is critical to building trust and efficiency.