---
title: "How Do I Look After My Power Automate Flows?"
source: "https://medium.com/@changingsocial/how-do-i-look-after-my-power-automate-flows-aadb94ed5130"
author:
  - "[[Sam M Cooper]]"
published: 2022-11-22
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*8ZJxgQSJUXFIaTgP.jpg)

With Power Automate making a huge difference in our working lives, many more people are creating them to help with personal productivity or [streamlining processes across teams or whole organisations](https://www.changingsocial.com/services/automation/).

With the increase in production of Power Automate flows, comes the need to be able to monitor them and make sure that they’re running the way we wanted them to.

Let’s outline several ways that this can be done!

## Weekly email from Microsoft Power Automate

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*6eEGCCZI3z9LYgKe.png)

Power Automate sends out a weekly email to the owners of flows that have failed in the previous week, with a count of how many times they failed and the ability to click on the flow name and jump straight to it.

This is great as a weekly recap, but what about when we want to know if a flow has failed more quickly?

## Monitor my flows

You can monitor your flows directly from your Power Automate page ([https://flow.microsoft.com/](https://flow.microsoft.com/) or [https://make.powerautomate.com](https://make.powerautomate.com/)).

**Navigate to Monitor > Cloud Flow Activity** on the left sidebar menu to see details of the flows that have been running over the last few days. The default view is set to show all activity, but you can choose to only see ‘Failures’.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*z86iAtQsGtWIhRMe.png)

Clicking on the flow in the list will take you directly to that flow run, so that you can see where the flow failed and start working out how to fix it.

You can only see flows that you have access to here. If you’re an administrator and you want to be able to see all the flows running in an environment, you need to…

## See Power Automate analytics

Administrators can access analytics for Power Automate from the [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/).

Here you can see daily and monthly run numbers, split into successful and failed runs, but you also have access to charts showing the different kinds of errors that are occurring when flows fail.

There’s no drilldown option here and you can’t access the actual flows from this page, but it’s a good way to recognise patterns and contact the flow owners to discuss the matter further.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Smu8ifp5lXxWBjaU.png)

Monitoring means that a user needs to actively go into the Power Automate analytics and look to see if there has been any failures. The best way of ensuring immediate notification when a flow fails is to build some error handling into you flows.

## Error Handling

“Error Handling” is a term that is used in development to describe building in processes to recognise when an error has occurred, and “handling” it — making sure that the program does something specific instead of (or as well as) just falling over.

We can perform Error Handling in Power Automate cloud flows easily by using the **Configure Run After** option against an action.

![](https://miro.medium.com/v2/resize:fit:1254/format:webp/0*X7w3PrUMbIVt8cXP.png)

This allows you to decide what actions you would like to happen when a previous action succeeds, fails, is skipped or times out.

![](https://miro.medium.com/v2/resize:fit:1204/format:webp/0*rCNaFOnXiKM9FPqk.png)

In the example above we can decide to send the owner of the flow an email if the Checkout Project action fails.

If you want to do this for a group of actions, you can use the Scope action to contain the main flow actions, and then send you and email if anything inside the scope fails.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*vMTbyL6Zn0N1EYPt.png)

Obviously, we’ve used sending an email as an example here, but you could send notifications to teams, or even write a record to an error log somewhere!

## Power Platform Center of Excellence

Finally, it would be remiss of us to not mention [Centre of Excellence (CoE)](https://www.changingsocial.com/services/centre-of-excellence/).

The Microsoft Power Platform CoE Starter Kit is a free collection of components and tools that are designed to [help you develop a strategy for adopting Power Platform](https://www.changingsocial.com/blog/microsoft-power-platform/), gain insights into adoption, and create governance by establishing audit and compliance processes.

These tools allow administrators to see all the [Power Apps](https://www.changingsocial.com/services/apps/) and Power Automate flows that are running across all the Power Platform environments in your tenant.

## Summary

So, to wrap up, there are a number of ways that users can see if Power Automate flows have failed. Most of them involve the user proactively looking at analytics to check the flows runs.

There’s no denying that automation is a powerful way to streamline work flows and achieve consistent results. It’s not the simplest thing to implement in your business, but it can save you time and effort along the way.

If you’re considering automating any processes in your company, don’t be discouraged by its complexity. Instead, take the time to understand what it can do for you, how well it will work for your business, and how you can make it part of something bigger.

If you’re looking for a better way to automate your processes, don’t hesitate to get in touch with us.

**We’ll work with you to find a solution that meets all your unique needs, and does it in a way that streamlines your workflow and makes you more efficient. Contact us at** [**hello@changingsocial.co.uk**](mailto:hello@changingsocial.co.uk)