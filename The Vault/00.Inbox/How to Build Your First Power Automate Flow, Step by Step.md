---
title: "How to Build Your First Power Automate Flow, Step by Step"
source: "https://medium.com/@corranforce/how-to-build-your-first-power-automate-flow-step-by-step-9f3e411c4bf0"
author:
  - "[[Allen Davis]]"
published: 2026-08-04
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*hErwFj8sy5fdr-7h)

Power Automate is Microsoft’s low-code tool for connecting apps and automating repetitive tasks without writing code. Building your first Power Automate flow means wiring one trigger to one action, then testing it until it runs without you touching it. If you are transitioning out of the military or already working the help desk grind, this is one of the fastest ways to prove automation skill on paper and in practice. You do not need a computer science degree. You need one hour, one repetitive task, and a five step process that will not let you overbuild your first attempt.

This guide walks the process end to end: what Power Automate actually does, the BUILD method for shipping your first flow, where the PL-900 certification fits if you want it on your resume, and how to fund the training if you are still in uniform.

## Key Takeaways

- A Power Automate flow connects a trigger, something that happens, to one or more actions, something that responds. Microsoft’s free 30 day trial lets you build and test flows with standard connectors before you pay for anything.
- The BUILD method, Bound the mission, Use a template, Install the trigger, Link the action, Deploy and test, gets a working first flow shipped in under an hour.
- Power Automate Premium runs $15 per user per month paid yearly as of August 2026, and unattended bot licenses start at $150 per bot per month, per Microsoft’s official pricing page.
- The PL-900 exam, Microsoft Certified: Power Platform Fundamentals, is a 45 minute, beginner level test covering Power Platform business value, environment management, Power Apps, Power Automate, and Copilot Studio agents. It is optional, not a gate.
- SkillBridge lets active duty service members inside their final 180 days train with an approved provider while still drawing full pay and benefits. VET TEC 2.0 pays tuition directly to approved tech training providers and does not require remaining GI Bill eligibility.
- You do not need to write code to build a working flow. You need to know your trigger and your action before you open the designer.

## What Power Automate Actually Does

Power Automate is part of Microsoft’s Power Platform, alongside Power Apps, Power BI, and Copilot Studio. Every flow you build has two core parts: a trigger and an action. The trigger is the event that starts the flow, something like a new email landing in an inbox, a file dropping into a SharePoint folder, or a form getting submitted. The action is what happens next, something like sending a Teams message, adding a row to an Excel table, or creating a task in Planner.

Microsoft’s current documentation on Copilot in Power Automate shows you can now describe a flow in plain language and have the designer draft the trigger and actions for you. That lowers the floor for a beginner, but you still need to understand what a trigger and an action are so you can check the AI’s work before you deploy it.

## The BUILD Method: Five Steps to Your First Flow

1. **Bound the mission.** Pick one repetitive task you already do by hand at least three times a week. Do not automate a process you have never mapped out on paper first.
2. **Use a template.** Power Automate ships with prebuilt templates for common triggers like “when a new email arrives” or “when a file is added to a folder.” Start from a template instead of a blank canvas.
3. **Install the trigger.** Connect the account, email, SharePoint, Forms, whatever fires the event, and confirm the trigger fires on a test event before you build anything downstream of it.
4. **Link the action.** Add the response step. Keep it to one action for your first flow. Do not chain five actions together before you have confirmed the first one works.
5. **Deploy and test.** Turn the flow on and run it against a real event. Your first automation flow [doesn’t need to be perfect](https://corranforcedesigns.blog/first-automation-workflow-not-perfect/) to prove the concept, it needs to run once without failing.

## Example Scenario: Client Intake to Team Notification

Example scenario: a one person service business collects new client requests through a Microsoft Form. The trigger is “when a new response is submitted.” The action is “post a message in a Teams channel” with the client’s name and service request pulled from the form fields. Build time for this exact flow, using the built in template, runs about 15 to 20 minutes for a first attempt including testing.

That flow alone does not replace a full CRM, but it kills the habit of manually checking a form spreadsheet every morning. Stack two or three flows like this and you have the skeleton of the one person AI service business model this brand teaches, covered in more depth in [your first paid automation offer](https://corranforcedesigns.blog/ai-automation-service-business/).

## Where the PL-900 Certification Fits, and Where It Doesn’t

The PL-900, Microsoft Certified: Power Platform Fundamentals, is a 45 minute, beginner level exam that covers the business value of Power Platform, environment management, and the capabilities of Power Apps, Power Automate, and Copilot Studio agents, per Microsoft’s own certification page checked in August 2026. It does not expire once earned, since Microsoft fundamentals credentials are lifetime credentials.

Exam vouchers run close to $99 USD according to several 2026 exam prep trackers, though Microsoft’s own certification page states price is set by the country or region where you sit the exam. Confirm the number at registration rather than trusting any figure in this post, mine included.

A certification does not build the flow for you. It proves you understand the platform on paper, which matters more on a resume during a career transition than it does once you already have three shipped flows an employer can look at. [When a certification is actually worth the study hours](https://corranforcedesigns.blog/ai-automation-certifications/) goes deeper on that trade-off.

## Funding This If You Are Still in Uniform or Just Getting Out

If you are active duty with at least 180 days of continuous service and inside your final 180 days before separation or retirement, SkillBridge lets you train with an approved civilian provider while your command still pays your full active duty pay, BAH, BAS, and TRICARE. Approval now requires an O-5 or higher sign off under 2025 and 2026 policy updates, and DoD has tightened which training providers can participate, so confirm your provider is currently listed at skillbridge.osd.mil before you count on the slot.

If you have already separated, VET TEC 2.0 reopened applications on June 15, 2026 and is funded through September 30, 2027. It pays tuition and fees directly to an approved training provider, adds a books and supplies stipend, and pays a monthly housing allowance matched to the Post 9/11 GI Bill rate. You do not need remaining GI Bill eligibility to apply.

I separated in January 2010, four years before SkillBridge was formally authorized under DoD Instruction 1322.29 in 2014, so I built [my own transition from 25U to RPA developer](https://corranforcedesigns.blog/from-25u-to-rpa-developer/) without it. Use the funding if it exists for you. I did not have the option.

Either path gets you Power Automate and PL-900 study time paid for while you still have a paycheck coming in. Neither path builds the flow for you. That part is still on you, covered step by step in [the veteran AI career transition field guide](https://corranforcedesigns.blog/veteran-ai-career-transition/).

## FAQ

## How long does it take to build a Power Automate flow?

A first flow built from a template, with one trigger and one action, typically takes 15 to 30 minutes including testing. Complex flows with multiple conditions and approvals take longer, but nothing in this guide requires that on day one.

## Do I need to know how to code to use Power Automate?

No. Power Automate is a low-code platform. You connect prebuilt triggers and actions through a visual designer, and Microsoft’s Copilot feature can now draft a flow from a plain language description, though you still need to check its work before you deploy it.

## Is the PL-900 exam worth it for veterans?

It is worth it if you need a credential on a resume during a transition when you have no shipped work to show yet. Once you have two or three working flows an employer can see, the shipped work carries more weight than the fundamentals badge.

## Action Steps

1. Pick one task you do by hand at least three times a week.
2. Sign up for the Power Automate free trial and start from a template, not a blank canvas.
3. Build one flow with one trigger and one action. Test it against a real event.
4. If you want the credential, study the free Microsoft Learn path before you pay for the PL-900 exam voucher.
5. If you are still active duty or recently separated, check your SkillBridge or VET TEC eligibility before you spend your own money on training.

**Follow @AllenDavis-AI for the next build in this series, where this flow chains into a three step system that runs a client intake process without you touching it.**

## Recap

Building your first Power Automate flow is not about proving you can code. It is about proving you can bound a mission, ship something small, and test it before you scale it. The BUILD method gets that first flow live in under an hour. PL-900 is a resume line if you need one, not a requirement to start. If you are still in uniform, the government will pay for the training before you separate, so use the window while it is open.

## References

Best Military Resume. (2026). *SkillBridge program guide 2026: DoD internship for transitioning military*. [https://bestmilitaryresume.com/skillbridge](https://bestmilitaryresume.com/skillbridge)

Microsoft. (2026). *Copilot in Power Automate*. Microsoft Learn. [https://learn.microsoft.com/en-us/power-automate/copilot-overview](https://learn.microsoft.com/en-us/power-automate/copilot-overview)

Microsoft. (2026). *Microsoft Certified: Power Platform Fundamentals*. Microsoft Learn. [https://learn.microsoft.com/en-us/credentials/certifications/power-platform-fundamentals/](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-fundamentals/)

Microsoft. (2026). *Power Automate pricing*. Microsoft Power Platform. [https://www.microsoft.com/en-us/power-platform/products/power-automate/pricing](https://www.microsoft.com/en-us/power-platform/products/power-automate/pricing)

Rank and Pay. (2026). *SkillBridge: 2026 guide to DoD internships*. [https://www.rankandpay.org/skillbridge/](https://www.rankandpay.org/skillbridge/)

U.S. Department of Defense. (2014). *DoD Instruction 1322.29: Job training, employment skills training, apprenticeships, and internships (JTEST-AI) for eligible service members*.

U.S. Department of Veterans Affairs. (2026). *VET TEC 2.0 (high-tech program)*. [https://www.va.gov/education/other-va-education-benefits/vet-tec-2/](https://www.va.gov/education/other-va-education-benefits/vet-tec-2/)