---
title: "Automating User Creation with Power Automate though Sharepoint List!"
source: "https://medium.com/@yasserhussien98/automating-user-creation-with-power-automate-though-sharepoint-list-623c81249fe6"
author:
  - "[[Yasser Hussien]]"
published: 2026-08-06
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*YfI0KU2XBfhJ9Ekt)

I’d like to share a useful flow I recently built using Power Automate that helps simplify daily IT tasks.

One of the common responsibilities for IT admins in any cloud-based work environment is creating new user accounts for employees. It’s a repetitive task that can take time when done manually.

That got me thinking: *why not make it easier?*

So I created a simple flow using a SharePoint list. Here’s the idea:

- Add a new employee’s details to the list
- The flow runs automatically
- A user account is created
- A welcome email is sent to the employee

## How the Flow Works?

The first step was creating a SharePoint list with the required columns — such as full name, department, email, and any other information needed for user creation.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*VTJrL54JOAgUsAL8)

Next, I started building the flow using Power Automate. I selected the SharePoint list as the trigger, so whenever a new item is added, the flow runs automatically.

To handle password generation, I added a Compose action in Power Automate to create a random password for each new user.

Instead of setting a fixed or manual password, the flow generates one dynamically using an expression. The user is then required to change this password upon their first login.

The expression used in the Compose action is: concat(substring(guid(),0,4),’!’,substring(guid(),5,4),’A1')

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ur_4ecVUzOpUW1qN)

This works by:

- Generating random characters using guid()
- Extracting parts of it with substring()
- Combining everything with concat()
- Adding special characters and a pattern (! and A1) to meet password complexity requirements

This ensures that every user gets a unique and secure password without any manual effort.

After that, I used a Scope action to organize the flow and group related actions together.

I added the step responsible for creating the user, where the required information is pulled directly from the SharePoint list — such as name, email, and department.

For the password field, I used the output from the Compose action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*nVlgcvcFtQ4qJ5lp)

## At this point, I faced another challenge: how to assign a license to the new user automatically without any manual steps.

I found a simple and effective approach.

Instead of assigning the License directly, I created a security group and assigned the required license to that group. Then I added an action to automatically add the new user to this group.

Once the user is added to the group, the license is assigned automatically — no manual intervention needed.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*234DNUlNeeYHj95S)

## At this stage, the more complex part was done. The remaining steps were mainly about customization—adjusting the flow actions to match specific requirements and ensure everything works exactly as needed.

To improve tracking and visibility, I added two additional columns in the SharePoint list:

- Status – with values such as New and *Licensed*
- Password – to store the initial password generated for the user

Once the user is added to the group and the license is applied, the flow updates the Status column to *Licensed*. It also writes the generated password (from the Compose action) into the Password field.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*tVg0Q-fMXcXjGt9I)

## After completing the user creation and licensing steps I wanted to send a welcome email to the new mailbox, which represents the new employee.

The requirement was simple: the email should include a “Welcome” image displayed inside the email body — not as an attachment.

At first, I faced a small challenge. I couldn’t just attach the image; it needed to render directly within the email content.

To solve this, I stored the image in SharePoint and then used a Compose insert the Result of Action Get file content from SharePoint and convert it into a format that can be displayed in an email.

The idea behind it is:

- The image file is stored as raw binary data (0100101101011100)
- It is then converted into Base64 format
- A prefix is added to define it as an image type

This results in a format like:

concat( ‘data:image/png;base64,’, base64(body(‘Get\_file\_content’)) )

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*y-AD7ID3YJZZqZir)

This tells the email client that the text is actually an image, allowing it to render correctly inside the message body.

Next, I added a Delay action before sending the email. The reason is that mailbox creation in Exchange Online can sometimes take a short time to complete. To avoid issues, I added a 2-minute delay (and in some cases, 5 minutes is even safer).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*19PvcpHkKln6-hdF)

Finally, I used a simple HTML from Chatgpt 😁 email template to control the layout. This allowed me to center the welcome image and adjust its size properly inside the email body.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*bdDm3WWMXaCbHqCL)