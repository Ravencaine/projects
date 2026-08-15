---
created: 2026-08-13
source: Power Automate UI flows — Automating Microsoft Forms Creation
source_url: https://medium.com/jenzushsu/power-automate-ui-flows-automating-microsoft-forms-creation-f3f5cb4677bc
note_type: atomic
tags: [power-automate, ui-flows, rpa, selenium]
---

# What Are UI Flows

UI Flows extends Power Automate with Robotic Process Automation (RPA) capabilities — recording and replaying user interface actions (clicks, keyboard input) for applications without APIs.

## Purpose

Bridges the gap between cloud flows (which work with APIs) and legacy desktop/web applications that expose no programmatic interface. Use UI Flows to automate repetitive tasks in Windows and Web applications by recording a human performing the task, then replaying it programmatically.

## Two Types

| Type | Scope |
|------|-------|
| **Desktop UI flows** | Windows desktop applications (Win32 apps) |
| **Web UI flows** | Browser-based web applications via Selenium IDE |

## How It Works (Web UI Flows)

1. Open **Selenium IDE** inside Power Automate
2. Record the sequence of steps on a web application
3. Define input parameters (values to pass in at runtime)
4. Define output parameters (values captured from the UI during playback)
5. Embed the UI flow inside a Power Automate cloud flow
6. The cloud flow passes inputs to the UI flow and receives outputs

## Limitations

- MFA is not supported during playback
- Plain text authentication storage (no secure credential store)
- Only the first Selenium test project runs if `.side` file contains multiple
- Unsupported Selenium commands: Run, AnswerOnNextPrompt, ChooseCancelOnNextConfirmation, ChooseCancelOnNextPrompt, ChooseOkOnNextConfirmation, Debugger, ClickAt, DoubleClickAt, Echo, MouseOut, MouseUpAt, MouseDownAt
- Right-click is not supported

## Related

- [[Automating-Microsoft-Forms-Creation-UI-Flows]]
- [[Creating-a-Web-UI-Flow-Selenium-IDE]]
- [[UI-Flows-Limitations]]
