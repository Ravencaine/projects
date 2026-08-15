---
title: "How to trigger flows with Power Automate Button"
source: "https://medium.com/@dynamicscrm/how-to-trigger-flows-with-power-automate-button-246f6fec0702"
author:
  - "[[Inogic Tech]]"
published: 2022-02-17
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
## Introduction:

Microsoft Power Automate Button provides flexibility due to which users can now run/trigger the flow from their mobile from anywhere at any time. Earlier this used to be a time-consuming process for the users i.e. open Power Platform, search flow, and then run it.

But now, by using the ‘Power Automate’ app on Mobile, the users can easily search the Button and run the flow. Recently, we had a business requirement where Dynamics 365 CRM users can mark all their Orders as ‘Submit’ and on the click of ‘Order Submit,’ the existing pre-built integration logic will trigger and move Orders in another system. Usually, orders were submitted at any time as there was no specific time. But here they wanted to run flow at their convenient time.

Given below are the steps to execute the above business scenario.  
**Prerequisite:** To click this button through the Mobile, you need to download the Power Automate app on your smartphone or tablet.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*pMaam4AqZ7txTqpE.jpeg)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*J7tM4sZDlOw0fJ0w.jpeg)

In the below steps we have shown how easily we can develop a Power Automate Button.

Step 1: Create the flow from outside the solution i.e. from Cloud Flow as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*tZTzBn8DiZapFpAG.jpeg)

Step 2: In next step, give name to the Power Automate flow and select triggering event. As we want the flow to trigger on the click of button, select trigger as ‘Manually Trigger a Flow’ and then finally click on ‘Create’ button.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*j4wGLZ1d6gXp5KRu.jpeg)

Step 3: We can also add Input parameters on the button that will take input from the user when the ‘Power Automate Button’ is clicked:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*4xViF2F13CVaP1Ye.jpeg)

It will show parameters and their types i.e. text, Yes/No, Email, Date, Number. You can use them as per your need. Here, in our case we selected the input parameter as ‘Text’.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*HhNRwNr0_CaBun-E.jpeg)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ESYVfUq7G7akAJb2.jpeg)

We can also update field properties like make them optional/required, add a dropdown list, or multi-select list. To update field properties, click on the menu icon and select the required option:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*1d55MvM7EagL08w4.jpeg)

Step 4: In the below step we have retrieved all Orders which are created today and needs to be submitted. To retrieve Orders we have used Data verse ‘List rows’ action:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*lXZylB2rDRBPbmcD.jpeg)

Step 5: Now in the next step we have added the Data verse ‘update a row’ action to update retrieved Order status as “Submit”.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*2oPWOH87GxHhrGie.jpeg)

Step 6: Save the flow.

Now our Button is ready to use and we can test it through the Phone ‘Power Automate’ app. All the Power Automate buttons will show under the Buttons section as shown in the below screenshot:

![](https://miro.medium.com/v2/resize:fit:1388/format:webp/0*8KSThA5waB_1CitJ.jpeg)

Step 7: To run the Button, just click on the ‘Submit Order’ button and a pop-up will appear with the parameter/ field that we created. Next, you just need to fill the fields and click on ‘Done’. Now the Power Automate flow will run.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*HxXTb4JYWxJzXBHg.jpeg)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*blMTGoW0Zkvp0gDG.jpeg)

Moreover, we can also allow another user to run the ‘Power Automate button’. And for this, we need to just share this button with a specific user.

## Conclusion:

The Power Automate Button feature provides flexibility where users can run the logic just by tapping a button, thereby avoiding the time-consuming steps.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*35pe8kAuM5nqTaVE.jpg)