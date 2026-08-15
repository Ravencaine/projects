---
title: "How to Validate File Contents in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-validate-file-contents-in-power-automate-d817a9680741"
author:
  - "[[Cloudmersive]]"
published: 2024-10-23
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
There’s a lot that can go wrong internally with seemingly innocuous files in our system. File types like PDF, DOCX, XLSX, etc. can have all kinds of different errors, and while we might notice warnings for those errors when we attempt to open files manually, we’re much less likely to catch them in a programmatic workflow.

Validating files with error checks in Power Automate can help streamline our file processing workflows, making it easier to “set and forget” complex operations. We can implement validation checks before critical workflows (such as document & data conversions, document editing, etc.) and prevent those workflows from taking place on error-ridden files.

In this quick walkthrough, we’ll validate a PDF document using the **Cloudmersive Document Conversion** connector in Power Automate. We’ll see how this works in a quick manually triggered flow, and we’ll review the validation response for our sample file.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Zug46AadD2xTQOhiQmQgJA.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*D4Z1aQWFivQw9-fsCX3Oqg.png)

We’ll begin by getting an example PDF document from our file system. To do that, we’ll use a **Get file content** action (I’ll be grabbing a file from a OneDrive for Business folder).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*slvvnzKpE6WIIsz97-EVMA.png)

We’ll now add a new action and type “Cloudmersive” into the search bar. We’re looking for the Document Conversion connector on this list.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*iu6HHhjwYgU4AX79HqRdZA.png)

We’ll click “See more” to view the actions list, and from there, we’ll look for an action called **Autodetect content type and validate**.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7xoD5d2luJKk_0h5KSz0XQ.png)

We’ll next select this action, and we’ll then create our Document Conversion connection with a Cloudmersive API key. We can get one for free by visiting the Cloudmersive website and creating a free account (this allows a limit of 800 API calls per month with zero additional commitments).

This action can automatically detect and validate dozens of different file types — including PDF, as we’re using in our current example — and also DOCX, XLSX, PPTX, JPG, PNG, and many more.

We’ll structure our request by adding our PDF file bytes and file name into each of our request parameters. When we run our flow, the **ValidateDocument** library will automatically check that the contents of our PDF document rigorously conform to PDF formatting standards.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wQByFmI7IMvyUMXx33W95w.png)

We’ll now save and test our flow, and we’ll then review the outputs.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Hn_ptn-fcfb6sh6Skp7SJA.png)

For valid PDFs, we can expect a response like the one shown below.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ebaEQN6ZTXUjX6d_lsN6IA.png)

For invalid files (i.e., files with an error and warning count above 0), we’ll receive an **ErrorsAndWarnings** array in our response describing the problem with our input file. We can review this response model below.

```c
{
  "FileFormatExtension": "string",
  "DocumentIsValid": true,
  "ErrorCount": 0,
  "WarningCount": 0,
  "ErrorsAndWarnings": [
    {
      "Description": "string",
      "Path": "string",
      "Uri": "string",
      "IsError": true
    }
  ]
}
```

We can use the **DocumentIsValid** response to determine whether our file-processing flows should take subsequent steps based on the validity of our files.