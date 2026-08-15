---
title: "🤖Power Automate UI flows — Automating Microsoft Forms Creation"
source: "https://medium.com/jenzushsu/power-automate-ui-flows-automating-microsoft-forms-creation-f3f5cb4677bc"
author:
  - "[[Jenzus Hsu]]"
published: 2020-02-14
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
## Recap

In my earlier post, I did a quick simple hack to develop a Contact Tracing app using Power Apps for **internal (organizational) users to do** check in on their known location(s) to facilitate contact tracing if needed in an event of an epidemic outbreak.

For those who miss my previous post, you can get it from here ([link](https://link.medium.com/n600wSplZ3)).

## New Problem Statement

In another scenario where the use of Power Apps is not possible for whatever reasons, the next best alternative is the use of Microsoft Forms.

[Jeffery Tay](https://medium.com/u/f65c1299e026?source=post_page---user_mention--f3f5cb4677bc---------------------------------------) shared his method to automate the mass creation of Microsoft Forms using Selenium — writing a custom Console app ([link](https://medium.com/@jefferytay/automating-large-scale-creation-of-microsoft-forms-c835140dffc5)).

In the spirit of using Power Platform, I will be exploring the use of **UI flows** to replicate this process.

### Scenario

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*uWe3UigXllGZsE5Eqf__TQ.png)

Proposed Process Flow

***Contoso Campus*** would like to create a Microsoft Forms for every single known locations in the campus. There are thousands of known locations and it is cumbersome to create thousands of Microsoft Forms within a short period of time.

## Process flow for Contoso Campus:

1. The administrator will prepare the following information — (1) Microsoft Forms Template and (2) An excel sheet of the location details.
2. Develop a Button Flow which will loop through the excel sheet and using the Forms Template to duplicate location-specific Forms and QR codes.
3. Run the Flow.
4. Distribute the generated QR Codes to the specific locations. The QR code is uniquely generated for every single Microsoft Forms.

Before sharing the high level implementation details, I will quickly run through what exactly is UI Flows.

## What is UI Flows?

UI flows is one of the latest features released through [Power Automate](https://flow.microsoft.com/en-us/) — providing Robotic Process Automation (RPA) capabilities on top of the typical work flows which Power Automate already provides.

According to Microsoft, you can use UI flows to automate repetitive tasks in Windows and Web applications. UI flows records and plays back user interface actions (clicks, keyboard input, etc.) for applications that don’t have easy-to-use or complete APIs available.

UI Flows is currently a preview feature and may have limited availability and restricted functionality. To find out more, please refer to this [link](https://docs.microsoft.com/en-us/power-automate/ui-flows/overview).

## High Level Implementation

### 1\. Prepare

Microsoft Forms has a duplicate feature where you can take an existing form and create multiple copies of the same form. For the scenario, every known location will have **1** Microsoft Forms.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Pnh7fcNhW_Yav_wtEpGw8w.png)

Duplicate Feature in Microsoft Forms

Below are the information which will be collected for every single location:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4jleDgOI9nQXE-5eSjXvkA.png)

Sample of the template

With duplicates, the administrator can simply change the title and the option. However with more than thousands of locations, it is very tedious to create manually. Hence, an automated process would benefit this scenario (***and the poor administrator***).

Besides the form, the administrator will also need a list of locations. I choose to curate a sample list of location in the form of Excel as I would be using this a data source for my flow. Below is the sample excel as a data source stored in OneDrive:

![](https://miro.medium.com/v2/resize:fit:1296/format:webp/1*k9A9x0PFcEbpmF_oRaM0RQ.png)

### 2\. Automate

Using Power Automate, I have designed a Button Flow to automate the process of creating (duplicating) Microsoft Forms for every single location, generating QR code references and web URL Microsoft Forms, by default, has shareable link and QR code.

Below is the overall flow for this automation:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*iVreHe5pw_BdSB7n8jxWBA.png)

This is how the flow will be executed:

1. The flow will look at the list of rows present in the excel sheet prepared in Step 1.
2. Using an “Apply to each” action, this will iterate or process the list of items periodically. For example, this action will take in an output (list of rows from Excel) and check if the column “URL” has an empty value using a Condition. If the condition is true, it will then flow the process to “ **If yes** ” step. For this scenario, all of the items will flow in this pattern.
![](https://miro.medium.com/v2/resize:fit:1266/format:webp/1*owPPFf1YU8nyDXjFdJOfwQ.png)

3\. When the process goes to the “If yes” step, there are 3 actions which will be triggered sequentially.

![](https://miro.medium.com/v2/resize:fit:1228/format:webp/1*eZfhNhR_Nr4iop2hyha5Cg.png)

The “ **Run a UI flow for web** ” will be the key to automate this duplication process for all the listed locations in the excel sheet. Before this step, you need to make sure that meet the pre-requisites for UI flows. You can refer to this [link](https://docs.microsoft.com/en-us/power-automate/ui-flows/setup).

The essence of creating a UI flow for web is the use of Selenium IDE. Selenium IDE is an open source tool that lets you record and playback human interactions on Websites. With UI flows, you can run Selenium IDE scripts from Power Automate and keep them stored securely (with appropriate IT governance) in Common Data Service.

Follow this step to create UI flows for web ([link](https://docs.microsoft.com/en-us/power-automate/ui-flows/create-web)), the Selenium IDE will launch and record your steps on how you will duplicate the Form, extract the URL and QR code for the new Form.

You should see a similar flow of action/commands in Selenium IDE below.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UhXkEe6veN9B9DA6SedLPQ.png)

Please take note of the following — Selenium IDE recordings are done with the current user’s profile, but playback is done using a **temporary user profile**. This means that websites that need authentication may not ask for credentials during a recording session. To address this, the user needs to manually edit the script to insert the commands needed for the login process.

In the above script, you will then need to add in the authentication steps to handle the playback when this flow executes. The additional limitation is that authentication details are stored in **plain text**.

Besides the list of actions, you will need to define the outputs which you require to capture for the subsequent steps. In Web UI flow, you can define both the inputs and outputs where you may need to pass information from an external source or store value.

Below are the link on defining input and output for web UI flows:

- Defining Inputs ([link](https://docs.microsoft.com/en-us/power-automate/ui-flows/inputs-outputs-web#define-inputs-for-a-web-ui-flow))
- Defining Outputs ([link](https://docs.microsoft.com/en-us/power-automate/ui-flows/inputs-outputs-web#define-outputs-for-a-web-ui-flow))

4\. With the outputs from web UI flows, you can then update the excel sheet with the required information.

![](https://miro.medium.com/v2/resize:fit:1230/format:webp/1*9NdRAKYo56Rtpt-daqcPYA.png)

5\. To make it more efficient, I can easily generate the QR code as a separate file using the **data:image** output using the following action.

![](https://miro.medium.com/v2/resize:fit:1228/format:webp/1*KI2LpDAbfd9rJzWFu8qDzw.png)

This will create a HTML file with the QR code and save the generated file in a Folder Path indicated.

Below is a short video on how this flow will be executed without any manual intervention.

### 4\. Distribute

With the generated QR code files, the administrator can easily print out and place it at identified location.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rVpUB1JKQTtf2_jZszPmXA.gif)

User can easily scan the QR code and it will take them to the mobile version of the Microsoft Forms.

## Summary

The use of RPA will definitely help with routine, mundane and repetitive task. UI Flows is still in preview with limited capabilities but I do see lots of potentials with this feature and complimenting with the existing Power Automate offerings.

There are some limitations to web UI flows which you need to understand before deciding on this approach:

- Multi-Factor Authentication (MFA) is not supported, use a tenant that doesn’t require MFA.
- These Selenium IDE commands are not supported: Run, AnswerOnNextPrompt, ChooseCancelOnNextConfirmation, ChooseCancelOnNextPrompt, ChooseOkOnNextConfirmation, Debugger, ClickAt, DoubleClickAt, Echo, MouseOut, MouseUpAt, and MouseDownAt.
- Right click is not supported.
- Additional Web UI flow input is generated when you use Foreach commands. To work around this issue, input any value into the extra fields. It doesn’t impact the playback.
- If the.side file contains multiple test projects, only the first one that was created runs.
- Playback directly in the Selenium IDE might not behave as intended. However, playback at runtime through the UI flow infrastructure behaves correctly.

The other challenge is the use and understanding of Selenium. If you have not played with Selenium, I would recommend you to go search and read some tutorials before jumping in.

With limited knowledge, you will end up banging your head or throwing your laptop out of the windows (nearly did either of these actions).

Try it and let me know if you have any fun out of this!

Happy #powerhacking away and wash your hands regularly 😃

*The opinions and views expressed here are those of my own and do not necessarily state or reflect those of Microsoft Singapore or Microsoft Corporation.*