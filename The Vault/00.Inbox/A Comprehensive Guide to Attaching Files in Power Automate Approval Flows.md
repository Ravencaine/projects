---
title: "A Comprehensive Guide to Attaching Files in Power Automate Approval Flows"
source: "https://medium.com/@serenisoft/title-a-comprehensive-guide-to-attaching-files-in-power-automate-approval-flows-0b43eb5a937b"
author:
  - "[[Avanteria]]"
published: 2024-08-19
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*uBP3C7jKb143NMwvK3AsrA@2x.jpeg)

## Introduction

Power Automate provides a powerful platform for automating workflows, including approval processes. One of the key features in an approval flow is the ability to attach files, such as PDFs or JPEGs, to the approval request. However, correctly formatting these attachments in the flow can be challenging, especially when dealing with different content types and formats. This article will guide you through the process of correctly configuring attachments in Power Automate, explaining the necessary steps, formats, and best practices to ensure your files are properly attached and processed.

## Understanding the Attachment Format

In Power Automate, when adding attachments to an approval action, you must format the data correctly to ensure that it is interpreted as a valid file by the system. The attachment is represented as a JSON object containing the file name and the content in base64 format. Additionally, each attachment should specify the content type to inform the system how to handle the file.

## Why and When to Use Different Content Types

1. `**application/octet-stream**`: This is a generic binary content type used when the specific type of the file is not easily determined. It's often used in cases where the file's content could be anything, and you want the system to handle it as raw binary data. This is useful when you're uncertain about the file type, or when dealing with various file formats in a dynamic environment.
2. **Specific Content Types (**`**image/jpeg**`**,** `**application/pdf**`**, etc.)**: When you know the file type, it's generally best to specify it. This helps the receiving system (e.g., an email client, a web browser, etc.) to correctly interpret and handle the file. For instance, using `image/jpeg` ensures that a JPEG file is recognized as an image and rendered correctly.

## Step-by-Step Guide: Creating an Attachment Array for Approval Flows

### Step 1: Initialize the Array Variable

Begin by initializing an array variable that will store all your attachments. This array will be passed into the approval action later.

- **Power Automate Action**: Initialize Variable
- **Name**: `AttachmentsArray`
- **Type**: Array
- **Value**: Leave this empty as you will append to it later.

### Step 2: Get the Attachment Content

Depending on where your files are stored (e.g., SharePoint, OneDrive), you’ll need to retrieve the file content. This content is typically encoded in base64 format, which Power Automate uses to handle binary data.

- **Power Automate Action**: Get file content (for SharePoint) or Get file content using path (for OneDrive)
- **Output**: This action will output the file content in base64 format.

### Step 3: Append File Content to the Array

Next, append the file content to the `AttachmentsArray`. This step is crucial and requires correct formatting. Here's the JSON structure to append for each type of file.

- **Power Automate Action**: Append to array variable

**For Files Converted to Base64**

```c
{
  "name": "@{outputs('Convert_file')?['headers/x-ms-file-name']}",
  "content": {
    "$content-type": "application/octet-stream",
    "$content": "@{body('Convert_file')?['$content']}"
  }
}
```

**Explanation**:

- `**name**`: This dynamically captures the file name from the conversion step.
- `**$content-type**`: The `application/octet-stream` is used to handle the file as binary data.
- `**$content**`: This is the base64 content of the file.

**For SharePoint Attachments**

```c
{
  "name": "@{item()?['DisplayName']}",
  "content": {
    "$content-type": "application/octet-stream",
    "$content": "@{body('Get_attachment_content')['$content']}"
  }
}
```

**Explanation**:

- `**name**`: The display name of the file is retrieved from the current item.
- `**$content-type**`: The generic binary content type is used.
- `**$content**`: Base64 content from the SharePoint file.

### Step 4: Use the Attachment Array in the Approval Action

Finally, pass the `AttachmentsArray` to the approval action. This ensures that all files in the array are attached to the approval request.

- **Power Automate Action**: Start and wait for an approval
- **Attachments**: Reference the `AttachmentsArray` variable directly without any additional formatting.
```c
@{variables('AttachmentsArray')}
```

## Best Practices

- **Use Specific Content Types**: Whenever possible, specify the correct content type (e.g., `application/pdf`, `image/jpeg`) to ensure compatibility and correct file handling.
- **Keep Arrays Simple**: Ensure your array structure is flat and straightforward to avoid unnecessary errors.
- **Test Extensively**: Always test your flows with various file types to confirm that the attachments are handled correctly.

## Conclusion

Handling file attachments in Power Automate approval flows requires attention to detail, especially when dealing with different file types and content formats. By following the steps outlined in this guide, you can ensure that your files are correctly formatted and attached, enhancing the efficiency and reliability of your approval processes. Always consider the content type that best suits your needs and test your flows thoroughly to prevent issues down the line.

This detailed guide should equip you with the knowledge to manage file attachments in Power Automate, ensuring a smooth and efficient workflow experience.

## Further Reading and Resources

- [Microsoft Power Automate Documentation](https://docs.microsoft.com/en-us/power-automate/)
- [Understanding Base64 Encoding](https://www.base64.guru/)
- [Working with JSON in Power Automate](https://docs.microsoft.com/en-us/power-automate/use-json)

This article provides a comprehensive, step-by-step approach to attaching files in Power Automate, with detailed explanations and visual aids to enhance understanding

> ***Enjoyed this article?*** *Don’t forget to* ***follow us*** *for more insightful content. Your* ***claps and comments*** *mean the world to us and help us create more of what you love! 🌟*