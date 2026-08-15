---
created: 2026-08-10
updated: 2026-08-10
source: 10 Power Automate Flows That Actually Save Hours — Not Just Demos
source_url: https://medium.com/@kaklotarrahul79/10-power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3
note_type: pattern
tags: [power-automate, hr, sharepoint, teams, entra-id, azure-ad, onboarding, automation]
---

# Onboarding/Offboarding User Access Flow

Triggered by a new HR SharePoint List entry or Microsoft Form submission, this flow fires parallel branches that simultaneously notify and action tasks across IT, Facilities, and Payroll — and posts a Teams welcome message to the new employee.

## Purpose

When an employee joins or leaves, IT, HR, and Facilities must coordinate manually across dozens of tasks (account provisioning, hardware allocation, license assignment, badge access). This flow replaces the coordination overhead with parallel, automated tasks.

## Components

1. **Trigger:** A new item is created in an HR SharePoint List OR a new Microsoft Form response is submitted
2. **Branches (parallel):**
   - **IT:** Provision Entra ID (Azure AD) account → assign to appropriate security groups → add to required apps → send welcome email with credentials
   - **Facilities:** Create hardware request ticket → assign badge/access card → notify building security
   - **Payroll:** Add to payroll system → set up bank details → confirm start date
3. **Action:** Post a welcoming Teams message to the new employee with onboarding resources and IT contact

## Structure

```
Trigger:   When an item is created (HR SharePoint List)
           OR  When a new response is submitted (HR onboarding Form)
     ↓
Apply to each: <response fields>
     ↓
Parallel branch:
  ┌─ IT team ──────────────────────────────────────┐
  │  Create user in Entra ID (Azure AD)             │
  │  Add user to security groups                     │
  │  Assign Microsoft 365 license                   │
  │  Send IT welcome email + credentials            │
  └────────────────────────────────────────────────┘
  ┌─ Facilities team ───────────────────────────────┐
  │  Create Planner task: hardware setup             │
  │  Send badge/access notification                  │
  └────────────────────────────────────────────────┘
  ┌─ Payroll team ──────────────────────────────────┐
  │  Add to payroll system                           │
  │  Set up bank details                            │
  └────────────────────────────────────────────────┘
     ↓
Action:   Post Teams message to new employee
          "Welcome to [Company]! Here's your onboarding guide..."
```

## Offboarding Variant

Flip the parallel branches for offboarding:
- Remove Entra ID licenses → deactivate account
- Revoke app access → remove from security groups
- Notify Facilities to reclaim hardware
- Update payroll status to final payment

## Hours Saved

~5 hours per employee onboarded or offboarded.

## Related

- [[Failed-Flow-Monitoring-Alerting]]
- [[Weekly-Status-Report-Aggregator]]
