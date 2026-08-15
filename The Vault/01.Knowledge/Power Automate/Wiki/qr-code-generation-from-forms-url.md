---
created: 2026-08-13
source: Power Automate UI flows — Automating Microsoft Forms Creation
source_url: https://medium.com/jenzushsu/power-automate-ui-flows-automating-microsoft-forms-creation-f3f5cb4677bc
note_type: atomic
tags: [power-automate, qr-code, microsoft-forms, data-uri]
---

# QR Code Generation from Forms URL

Extract and generate QR codes from Microsoft Forms share URLs using the `data:image` base64 output.

## Purpose

Microsoft Forms generates a shareable QR code natively. When automating Form creation via UI Flows, capture the QR code as a `data:image` URI and save it as an HTML or image file for printing and distribution.

## How It Works

1. During UI Flow recording (Selenium IDE), capture the QR code element:
   ```text
   store        text     css=.qr-code     QRCodeData
   ```
2. The captured value is a `data:image/png;base64,...` URI
3. Save this value to an HTML file or decode to a PNG

## Output Format

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==
```

## Generating the HTML File

Power Automate can use the `data:image` output to create an HTML file:

1. UI flow returns `QRCodeData` (base64 `data:image`)
2. Create HTML file with embedded image:
   ```html
   <html>
   <body>
   <img src="data:image/png;base64,..." alt="QR Code" />
   </body>
   </html>
   ```
3. Save to a designated folder path

## Use Case

Print and distribute QR codes to physical locations — users scan the QR code and are taken directly to the mobile version of the corresponding Microsoft Form.

## Related

- [[Automating-Microsoft-Forms-Creation-UI-Flows]]
- [[What-Are-UI-Flows]]
