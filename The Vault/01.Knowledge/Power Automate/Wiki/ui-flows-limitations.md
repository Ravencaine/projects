---
created: 2026-08-13
source: Power Automate UI flows — Automating Microsoft Forms Creation
source_url: https://medium.com/jenzushsu/power-automate-ui-flows-automating-microsoft-forms-creation-f3f5cb4677bc
note_type: gotcha
tags: [power-automate, ui-flows, rpa, limitations, gotcha]
---

# UI Flows Limitations

Known limitations and edge cases when running Web UI flows in Power Automate.

## Authentication Gotchas

- **MFA not supported** — Use a tenant account that does not require MFA for the UI flow service account
- **Plain text credentials** — Login credentials are stored in plain text in the `.side` file. Use a dedicated low-privilege account; do not use admin credentials
- **Temporary profile at playback** — Recordings capture actions in the current browser profile, but playback runs under a temporary profile — authentication must be explicitly scripted or the playback will fail silently on the login screen

## Unsupported Selenium Commands

The following Selenium IDE commands are blocked and will cause the flow to fail:

| Command | Category |
|---------|---------|
| `Run` | Test execution |
| `AnswerOnNextPrompt` | Dialog handling |
| `ChooseCancelOnNextConfirmation` | Dialog handling |
| `ChooseCancelOnNextPrompt` | Dialog handling |
| `ChooseOkOnNextConfirmation` | Dialog handling |
| `Debugger` | Developer tools |
| `ClickAt` | Coordinate-based clicks |
| `DoubleClickAt` | Coordinate-based clicks |
| `Echo` | Logging |
| `MouseOut` | Mouse events |
| `MouseUpAt` | Mouse events |
| `MouseDownAt` | Mouse events |
| **Right-click** | Context menu actions |

## Technical Constraints

- **Only the first test project runs** — If a `.side` file contains multiple Selenium test projects, only the first one created is executed at runtime
- **Extra input fields generated** — Foreach loops in Selenium scripts generate additional input fields; any value can be placed in them (they don't affect playback)
- **IDE playback ≠ runtime playback** — A step that works in the Selenium IDE recorder may behave differently at runtime; always test via the Power Automate cloud flow
- **Dynamic web apps** — Single-page applications (SPAs) with async content loading may cause playback failures; add explicit waits if possible

## Related

- [[What-Are-UI-Flows]]
- [[Creating-a-Web-UI-Flow-Selenium-IDE]]
- [[Automating-Microsoft-Forms-Creation-UI-Flows]]
