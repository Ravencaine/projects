---
title: "Why do we have four levels of security in Power BI?"
source: "https://medium.com/data-science/why-do-we-have-four-levels-of-security-in-power-bi-7bc53e7d5729"
author:
  - "[[Salvatore Cagliari]]"
published: 2021-11-03
created: 2026-08-12
description: "Data security may not be the first topic when you start working with Power BI. But, when you begin to dig into this topic, it becomes very confusing. Let’s go through the security features in Power BI."
Processed: "Unprocessed"
---
## Data security may not be the first topic when you start working with Power BI. But, when you begin to dig into this topic, it becomes very confusing. Let’s go through the security features in Power BI.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Ie4sPCQIDew3otk2)

Photo by Klugzy Wugzy on Unsplash

## Introduction

Power BI is a great tool to collect data and present it to your Audience. But, when you start thinking about Data Security, you will find out that Power BI offers four different security features to protect your data.

But why do we need four places in which we can change settings to control data security?

Well, it turns out that each setting addresses a different area.

We have:

- Privacy Levels in Power Query
- Row Level Security (RLS) in Power BI
- Office 365 Sensitivity Labels
- Power BI Workspace Security

Each of these settings helps you to secure your data in different ways.  
There are plenty of Web-Resources for these topics. I’ll add Links to these Resources instead of rewriting or copying the content from there.

So, let’s look at each of them.

## Privacy levels in Power Query

Of all four, this is one of the least understood mechanisms in Power Query.

This feature is all about managing the possibilities to pass data from one system to another.

When you load data from a relational database, [Query folding](https://docs.microsoft.com/en-us/power-query/power-query-folding) can happen. This means that Power Query transformations can be translated into SQL code and passed to the source database.

Now imagine that you get data from two databases. One database contains sensitive data — for example, personal data about employees or customers.

Imagine that you want to filter data in the database without sensitive data based on data from the database with sensitive data. You may want to avoid the passing of sensitive data from one database to the other.

Privacy Levels helps you to manage such scenarios.

When you set the correct privacy Levels on your sources, you can disable Query folding, and no sensitive data is shared between different sources.

You can set Privacy levels on Sources when you use them for the first time, for example, when you want to merge two sources:

![Privacy Levels on first use (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cflz2eqpVhS8JiDaaaULuw.png)

Figure 1 — Privacy Levels on first use (Picture by the Author)

And you can change the Privacy Level at any time in the “Data source Settings” dialogue:

![Change Privacy Levels (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-psun82YXTLOQVX_D7P3Kw.png)

Figure 2 — Change Privacy Levels (Picture by the Author)

Here are some links with more detail on this topic:

[Microsoft documentation about Privacy levels](https://docs.microsoft.com/en-us/power-bi/admin/desktop-privacy-levels)

[Short explanation about Privacy Levels by alphabold](https://www.alphabold.com/data-privacy-settings-in-power-bi/)

[Throughout descriptions from Chris Webb](https://blog.crossjoin.co.uk/2019/01/13/power-bi-data-privacy-cloud-web-data-sources/) (Check out his Series, which shows Privacy levels in great detail linked in this blog post)

I strongly suggest looking at the available levels and set them according to the data source:

- *Public*, for data from the Internet
- *Organizational*, for internal data sources
- *Private*, for data with Sensitive data

Do not use *None* to avoid unwanted side effects, like the passing of data between data sources.

## Row-Level-Security (RLS) in Power BI models

Row-Level-Security (RLS) controls who has access to which data in the data model.

This feature of Power BI is well documented and understood in the community.

There are three forms of this feature:

1. Lookup-Tables with E-Mail addresses
2. Parent-Child Relationships
3. Dynamic RLS

The simplest form, with a Lookup-Table, works as shown in the following example:

1\. Your model contains a table with a list of users. This list includes the E-Mail address of each user:

![Lookup table with E-Mail addresses (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Xvn55fSzj5Jbuz8EMnAGrw.png)

Figure 3 — Lookup table with E-Mail addresses (Picture by the Author)

In this example, each user has a Reference to an Entity to control the access to the existing entities.

2\. You have to enable the Lookup table to filter the table referenced by the column EntityId in your Data-Model:

![Data-Model (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VrWMy9XyPCV2cFYvxdRNOQ.png)

Figure 4 — Data-Model (Picture by the Author)

We need bidirectional Cross-Filtering to enable the Filtering of the DimEntity table by the EmployeEntity table.  
In addition, the relationship must have the “Apply security filter in both directions” Option enabled. This Option activates the transfer of the RLS filter to the Fact table.

3\. Configure the RLS Role

![Configure RLS role and expression (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7sz6Rlg6huVGrWhNqoyFlg.png)

Figure 5 — Configure RLS role and expression (Picture by the Author)

You can click on the “Manage roles” button in the Modeling Ribbon to get the dialogue and set up the roles. Then you need to create a Role and give it a meaningful name.

After that, you have to select the table on which you have to write the filter condition and enter this Condition as a DAX Expression.

We use the USERPRINCIPALNAME() function to compare the actual user’s E-Mail address with the list of users in the table.

4\. Test the RLS role

Now, you can test the role by clicking on the “View as role” Button:

![Test the RLS role (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*tkMsGvJ37bSsYhjAM779pQ.png)

Figure 6 — Test the RLS role (Picture by the Author)

You can either select the role to see the effect of the RLS role on yourself, or enter the Mail-Address of another user, to see the impact of the RLS role on that user:

![Effects of RLS permissions (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2CFyW8527rJFIN7BK0e5ng.png)

Figure 7 — Effects of RLS permissions (Picture by the Author)

You can stop the RLS testing mode by clicking on the “Stop Viewing” button on the top right corner of the report.

With a parent-child hierarchy, you can set up access for superiors who can see all data of their subordinates and similar scenarios with a parent-child hierarchy.  
You can implement this by using the PATH() DAX-function and an RLS filter which uses LOOUPVALUE() or the PATHCONTAINS() function to grant the appropriate access.

You can read the article [Dynamic Row Level Security with Organizational Hierarchy Power BI](https://radacad.com/dynamic-row-level-security-with-organizational-hierarchy-power-bi) for more Details.

Or you can watch this YouTube video from the “London Business Analytics Group” YouTube channel, which explains the same approach:

Dynamic RLS is the most complex to understand and has the most significant performance impact.

Look at these References for more Details:

- [Dynamic Row Level Security in Power BI (by PragmaticWorks)](https://blog.pragmaticworks.com/dynamic-row-level-security-in-power-bi)
- [What Do You Need to Implement Dynamic Row-Level Security in Power BI? (by RADACAD)](https://radacad.com/what-do-you-need-to-implement-dynamic-row-level-security-in-power-bi)

You need Dynamic RLS when both of the approaches shown above are not enough to cover the requirements.  
For example, your users need access to data based on other tables, such as an assignment to a geographic area or the Business Unit.

But, the setup of RLS doesn’t stop here.

You need to configure the access to the Power BI RLS role after publishing the report to the Power BI service.

You can access this setting on the context menu of the Dataset:

![Set Dataset security (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1Iia223Cr2gzGgdq5XU3Xg.png)

Figure 8 — Set Dataset security (Picture by the Author)

There, you can add users to the RLS role:

![Add member to RLS role (Picture by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PdYIud6TYvMxiyu-Uaz47Q.png)

Figure 9 — Add member to RLS role (Picture by the Author)

This step assigns users to specific RLS roles.

Users have no access to data inside a Power BI report with RLS until the users are not assigned to an RLS role.

You watch this video from the “Guy in a Cube” YouTube channel to learn more about this topic:

## Sensitivity Labels

Sensitivity Label is a Feature controlled by Azure and Microsoft 365 admins.

An Admin can enable Data Protection and create Sensitivity labels in your organization to control enforced encryption and to limit capabilities to distribute information inside and outside your tenant.

This feature can cause additional costs, depending on your Microsoft 365 subscription level.

You can add a Sensitivity label on a Power BI report as soon as the admin configures labels and policies.

For example, Sensitivity labels can restrict the distribution capability in Power BI reports.

One of the great features of Sensitivity labels is that when you mark Power BI Report with a label, the same label is applied to an Office file created with the Export function in Power BI.

Sensitivity Labels is an enormous topic. I cannot cover this topic in this article in more detail, as I don’t have access to the Admin portal. Thus, I’m not able to configure this feature and test it thoroughly.

I encourage you to watch the following video from “Guy in a Cube” about this topic:

Go to the Microsoft documentation about [Sensitivity labels in Power BI](https://docs.microsoft.com/en-us/power-bi/admin/service-security-sensitivity-label-overview) to learn more about it.

## Workspace Security

Last but not least, you can configure access to your Workspace in Power BI Service.

You create Workspaces in the Power BI service. Microsoft has disabled the automatic creation of a Power BI Workspace while creating a Team in MS Teams a few months ago per default.

You can read the Microsoft article about creating a Workspace and grant access to members here: [Create the new workspaces in Power BI](https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-create-the-new-workspaces).

Each Workspace has four roles:

- Admin  
	An Admin can do anything in a Workspace
- Member  
	Each Member can add any content and change most settings in a Workspace. A Member can add other Users with the Member Role, and he can add Contributors and Viewers.
- Contributor  
	Members of this role can add Reports and Datasets to a Workspace with the Contributor role. But they’re not allowed to change a Power BI App, as long an Admin doesn’t delegate this permission to the user.
- Viewer  
	Viewer exists when you have a Premium Capacity. Viewers can access any content, even without a Pro License. But they cannot change anything.

In the Microsoft documentation, you can look at the complete list of permissions in the list of [Roles in the new workspaces in Power BI](https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-roles-new-workspaces).

You need to assign the Roles to users, Windows Groups or even Microsoft 365 groups, including Teams from Microsoft Teams.

Each user with access to a Workspace can share Artifacts with other users who are not Workspace members. The possible permissions include Build permission on a data set and sharing of reports.

Power BI Apps are somewhat outside of a Workspace and aren’t controlled by Workspace security. As described [here](https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps#publish-your-app), you can configure access to your Power App, which goes beyond the users with access to your Workspace.

## Conclusion

Each level of Security in Power BI covers a specific area.

- Workspace security controls access to published artefacts, like data sets and reports.
- RLS controls the access to data by users within a report.
- Privacy levels for Power Query Sources protect the transfer of sensitive data between data sources.
- Sensitivity levels control what can be done with confidential data when moving data within and outside your company.

All of us need to know how to handle Workspace security. It is the first level of protection.

We need to know how to work with RLS as soon as we need to control which user has access to which data in our reports.

Privacy levels in Power Query are mostly underrated when avoiding sharing potentially sensitive data between data sources. You need to know the consequences of query folding and how to use privacy levels to protect your data.

An admin usually controls Sensitivity labels, and you need to know which one you can use in which scenario. Ask your Security officer for documentation about the available labels if you don’t know their purpose. If the button for Sensitivity labels is disabled, then you can ignore this feature as it is not set up in your organization.

I hope that this article is helpful to understand the available security features in Power BI and how to them. I recommend following the mentioned Links to learn more about each feature.

## [Join Medium with my referral link - Salvatore Cagliari](https://medium.com/@salvatorecagliari/membership?source=post_page-----7bc53e7d5729---------------------------------------)

### As a Medium member, a portion of your membership fee goes to writers you read, and you get full access to every story…

medium.com

If you appreciate my work, feel free to support me through

## [Salvatore Cagliari](https://buymeacoffee.com/salvatorecagliari?source=post_page-----7bc53e7d5729---------------------------------------)

### I write technical articles about Data Analysis and Reporting with Power BI. In addition I love building and flying RC…

buymeacoffee.com

Or scan this QR Code:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*btH95UXO7gboS30eZMk6ug.png)

Any support is greatly appreciated.

Thank you.