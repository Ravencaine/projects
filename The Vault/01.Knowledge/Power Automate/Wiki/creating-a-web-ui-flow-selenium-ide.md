---
created: 2026-08-13
source: Power Automate UI flows — Automating Microsoft Forms Creation
source_url: https://medium.com/jenzushsu/power-automate-ui-flows-automating-microsoft-forms-creation-f3f5cb4677bc
note_type: pattern
tags: [power-automate, ui-flows, selenium-ide, web-automation]
---

# Creating a Web UI Flow (Selenium IDE)

Step-by-step for recording a web UI flow using Selenium IDE inside Power Automate.

## Prerequisites

- Power Automate with UI flows add-on (Premium)
- Browser extension for UI flows installed
- Web application with a consistent, predictable UI (not heavily dynamic/SPAs with async loading)

## Structure

### Step 1 — Create the Web UI Flow

1. In Power Automate → **My flows** → **UI flows (preview)**
2. Select **Web UI flow**
3. Name the flow and open the Selenium IDE recorder
4. Enter the starting URL of the web application
5. Click **Record** — every click and keystroke is captured as a Selenium command

### Step 2 — Record the Workflow

Example for duplicating a Microsoft Form:
```text
open         https://forms.office.com/ManageForm
click        id=duplicate-button
type         id=form-title   ${LocationName}
click        id=save-button
store        text     css=.share-url    FormURL
store        text     css=.qr-code      QRCodeData
click        id=exit-button
```

### Step 3 — Add Login Steps

Selenium recordings run against the current user's profile, but playback uses a **temporary profile** — authentication must be explicitly added to the script.

```text
type        id=email-input      your.email@tenant.com
type        id=password-input   yourpassword
click       id=submit-button
```

> **Security note:** Authentication credentials are stored in plain text in the `.side` file. Consider a dedicated service account with minimal privileges.

### Step 4 — Define Inputs and Outputs

| Parameter | Direction | Example |
|-----------|-----------|---------|
| `LocationName` | Input | Campus Building A |
| `FormURL` | Output | `https://forms.office.com/f/abc123` |
| `QRCodeData` | Output | `data:image/png;base64,...` |

### Step 5 — Test and Validate

1. Run the UI flow from the Selenium IDE directly (may differ from runtime behaviour)
2. Run via the Power Automate cloud flow for full validation
3. Monitor the **UI flows run history** for playback failures

## Related

- [[What-Are-UI-Flows]]
- [[Automating-Microsoft-Forms-Creation-UI-Flows]]
- [[UI-Flows-Limitations]]
