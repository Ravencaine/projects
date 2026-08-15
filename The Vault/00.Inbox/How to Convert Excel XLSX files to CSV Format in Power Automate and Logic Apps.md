---
title: "How to Convert Excel XLSX files to CSV Format in Power Automate and Logic Apps"
source: "https://medium.com/@cloudmersive/how-to-convert-excel-xlsx-files-to-csv-format-in-power-automate-and-logic-apps-d64a5ac61462"
author:
  - "[[Cloudmersive]]"
published: 2024-09-18
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Exporting a single Excel document to CSV format is straightforward. However, handling Excel to CSV conversions at scale is a bit more challenging.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Q2KBhijnsQsohsOaMXZEiA.png)

Thankfully, in both Power Automate and Azure Logic Apps, we can automate our Excel to CSV conversion workflows without writing any code. We can utilize the Cloudmersive Convert API (titled **Cloudmersive Document Conversion** connector in Power Automate) to convert entire folders of Excel files to CSV with the click of a button.

We can find and utilize this connector action in a few quick steps.

To find and test the Excel to CSV conversion action, we’ll first set up a manually triggered, instant cloud flow in Power Automate (note: all the below steps apply to Azure Logic Apps as well).

This demonstration will begin with a partially designed instant cloud flow that retrieves Excel files from a specific SharePoint folder. The folder used in this demonstration contains three Excel files.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PfnLz6qwOPas25g8IS7I7g.png)

Note that Power Automate automatically wraps actions dealing with multiple file inputs in an **Apply to each** control (shown in the above flow as a **For each** control).

Within this **For each** control, we’ll add a new action and type “Cloudmersive” into the search bar. This will bring up a list of Cloudmersive connectors, and when we scroll down this list, we’ll find the **Document Conversion** connector.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*b1BG3JGITnKxhtP0vBFQlg.png)

From here, we’ll click “see more” to view the actions list, and we’ll scroll down this list until we find an action titled **Convert Excel XLSX Spreadsheet to CSV**. We’ll find this action surrounded by other useful Excel conversion actions we can use in different workflows.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hRKfhOlkIsJgCgiaFTW9LQ.png)

After we select this action, we’ll need to provide authorization details to establish our connection. We’ll need a premium Power Automate license to use Cloudmersive connectors, but we can create our Cloudmersive connection for free with a free API key. This will give us a limit of 800 API calls per month with zero commitments.

From here, we’ll supply the file bytes and file names retrieved from previous flow actions into the two primary input request parameters. If we want, we can also set the output encoding of our CSV files to UTF-8 (default), ASCII, or UTF-32 using an advanced parameter.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UifapIT3TfxB-tB77sOKEQ.png)

To finalize our flow, we’ll add a **Create file** action that generates our new CSV documents and stores them in another folder. We could, of course, just as easily perform a wide range of other final actions, such as sending the converted files directly to a colleague via email.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Y1t5DTwkBXNGifQbm4S-mA.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eEA67lH3Wfj4n67MECyB-g.png)

All done! Our flow will now generate one new CSV file in our target folder for each Excel file in the original folder.