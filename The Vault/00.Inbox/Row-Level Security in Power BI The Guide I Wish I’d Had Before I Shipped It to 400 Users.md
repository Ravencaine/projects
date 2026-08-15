---
title: "Row-Level Security in Power BI: The Guide I Wish I’d Had Before I Shipped It to 400 Users"
source: "https://medium.com/towards-artificial-intelligence/row-level-security-in-power-bi-the-guide-i-wish-id-had-before-i-shipped-it-to-400-users-4b74255ef2e3"
author:
  - "[[Sheth Priyanka]]"
published: 2026-08-05
created: 2026-08-09
description: "Static vs dynamic RLS, the USERPRINCIPALNAME pattern, the bi-directional trap that quietly leaks data, and how to test it properly — before your users test it for you."
Processed: "Unprocessed"
---
## Static vs dynamic RLS, the USERPRINCIPALNAME pattern, the bi-directional trap that quietly leaks data, and how to test it properly — before your users test it for you.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vV7ctIq18Ov877IDBsa-aQ.png)

One report, one semantic model — and every user seeing only their own rows. That’s the whole promise of RLS. Getting there is where it gets interesting.

The message came in on a Tuesday: *“Quick question — why can I see the Northeast numbers? I’m supposed to only have my region.”*

I read it three times.

The report had been live for a week. Forty regional managers, one shared dashboard, and a set of security roles I had tested — I thought carefully — before shipping. And yet here was a manager, politely telling me he could see revenue that wasn’t his.

Nothing had failed. No error, no broken visual, no red banner. That’s the thing about Row-Level Security: **when RLS is wrong, it doesn’t crash. It just quietly shows someone data they shouldn’t have.** It’s the only bug in Power BI where the failure mode is a compliance conversation.

I fixed it that afternoon (it was a relationship direction — more on that below, because it’s the single most common cause). But it sent me back to properly learn RLS instead of copying patterns from forum posts.

This is the guide I wish someone had handed me first: what RLS actually does, the two ways to build it, the traps that leak data, and how to test it so your users never have to.

## First: What RLS Is — and What It Isn’t

**Row-Level Security (RLS) restricts which *rows* a user can see in a semantic model.** You define a role, write a DAX filter on one or more tables, assign users to that role, and the filter applies automatically to every query that user runs.

Three things it is *not*, and each one bites someone every year:

- **It’s not column or table security.** Hiding entire columns or tables is **Object-Level Security (OLS)**, a separate feature configured through external tools like Tabular Editor. RLS filters rows; OLS hides fields.
- **It’s not security on the underlying source.** RLS protects the semantic model. If a user has direct access to the warehouse or Lakehouse behind it, RLS in Power BI doesn’t stop them there.
- **It doesn’t apply to everyone.** This one surprises people: users with **edit permissions on the semantic model** (such as workspace Admins, Members, and Contributors) aren’t restricted by RLS when accessing the model through those permissions. RLS applies to **Viewers** and to users who receive the report through an app or a shared link.

*Takeaway: RLS is row filtering for read-only consumers of a semantic model. Plan your workspace roles accordingly, or your “restricted” users will quietly see everything because you made them Contributors.*

## The Two Flavours: Static and Dynamic RLS

Almost every RLS implementation is one of these two — or a combination.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*d97e_AHG04eHFVv08Tb4bQ.png)

Static RLS hardcodes the filter into the role. Dynamic RLS resolves it at query time from the signed-in user. Same outcome, very different maintenance cost.

Both are built in the same place: open **Manage roles** in Power BI Desktop (*Modeling → Manage roles*) to create or edit your RLS roles before publishing the semantic model.

### Static RLS

You create one role per group and hardcode the filter.

```c
-- Role: "East Region"
-- Table filter on DimRegion
[RegionName] = "East"
```

It’s simple and it’s fast. It’s also a maintenance trap: five regions means five roles, and a new region means editing and republishing the model. Static RLS is fine when the groups are few and genuinely stable — three business units, two legal entities — and painful beyond that.

### Dynamic RLS

You create one role that resolves the current user at query time. This is where `USERPRINCIPALNAME()` comes in — it returns the signed-in user's UPN (usually their email) in the Power BI Service.

```c
-- Role: "Regional Access" (a single role for everyone)
-- Table filter on DimUser
[UserEmail] = USERPRINCIPALNAME ()
```

You maintain a mapping table — one row per user per thing they’re allowed to see — and the model filters itself. Adding a new manager becomes a *data* change, not a model change. Nobody republishes anything.

*Takeaway: if you have more than a handful of groups, or the groups change more than once a year, go dynamic. The extra hour of setup pays for itself the first time someone joins the team.*

> *Why* `*USERPRINCIPALNAME()*` *and not* `*USERNAME()*`*? In the Power BI Service both return the UPN, but in Power BI Desktop* `*USERNAME()*` *returns* `*DOMAIN\user*` *while* `*USERPRINCIPALNAME()*` *returns the UPN. Using* `*USERPRINCIPALNAME()*` *keeps Desktop and Service behaviour consistent, which saves you a confusing afternoon.*

## How Dynamic RLS Actually Propagates

This is the part most tutorials skip, and it’s exactly where my leak came from.

The DAX filter lands on your **user mapping table**. It only reaches your fact table if the relationships carry it there. So the filter has to travel: `DimUser → DimRegion → FactSales`.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bYrjTBTypevb3tbGXW7VRg.png)

The RLS filter starts at the user table and has to reach the fact table through your relationships. If the path breaks anywhere, the filter silently stops — and users see more than they should.

A minimal working setup looks like this:

```c
DimUser    (UserEmail, RegionKey)
DimRegion  (RegionKey, RegionName)
FactSales  (RegionKey, SalesAmount, ...)
```
```c
DimUser ──1:*──> (filters) DimRegion ──1:*──> FactSales
```

The exact relationship path depends on your model, but the key idea is universal: **the security filter must propagate from the security table to every fact table that requires protection.**

Then the role filter, on `DimUser`:

```c
[UserEmail] = USERPRINCIPALNAME ()
```

If a user is missing from `DimUser`, they see **nothing** — which is the correct, safe default, but it does generate support tickets. Decide deliberately whether an unmapped user should see nothing (secure) or a public subset (friendly), and document that choice.

### For manager hierarchies, use PATH

A common requirement: a manager should see their own numbers *and* everyone below them. Flat mapping tables can’t express that. `PATH` can.

```c
-- Calculated column on DimEmployee
EmployeePath = PATH ( DimEmployee[EmployeeID], DimEmployee[ManagerID] )
```
```c
-- Role filter on DimEmployee
PATHCONTAINS (
    DimEmployee[EmployeePath],
    LOOKUPVALUE (
        DimEmployee[EmployeeID],
        DimEmployee[Email], USERPRINCIPALNAME ()
    )
)
```

This says: *show me every employee whose management chain contains me.* One role, any depth of hierarchy, no maintenance when the org chart changes.

One constraint worth knowing: `PATH` works only with p **arent-child hierarchies stored in the same table** — an employee table with both `EmployeeID` and `ManagerID`. It won't traverse a hierarchy spread across unrelated tables.

*Takeaway: model the security relationship first, write the DAX second. Most “RLS isn’t working” problems are relationship problems wearing a DAX costume.*

## The Bi-Directional Trap (This Was My Bug)

Here’s the one that cost me that Tuesday message.

RLS filters flow in the direction your relationships allow. When a filter can’t reach the fact table, the instinct is to reach for a **bi-directional relationship** to force it through. It works — and it can also open a path you didn’t intend, because filters now travel *both* ways through that relationship.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vo1sfIFKmlpNrG97XdUyaw.png)

Bi-directional relationships are the most common cause of RLS leaking data. Reach for them last, and test hard when you do.

Microsoft’s own guidance is cautious here, and so am I now. My rules:

- Default every relationship to **single direction.**
- If the filter won’t reach the fact table, fix the **model** first — add the missing key, or a bridge table.
- Only if that fails, enable “ **Apply security filter in both directions** ” on the specific relationship — and then re-test every role.

In my case, a bi-directional relationship I’d added months earlier for an unrelated slicer convenience let the region filter escape. Nothing looked wrong. The numbers just quietly included rows they shouldn’t have.

*Takeaway: every bi-directional relationship in a model with RLS is a security surface. Audit them deliberately, not accidentally.*

## Test It Before Your Users Do

This is the step I had rushed, and it’s the cheapest insurance in the entire process.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HCE9qZlqrawXj-ueDgJekg.png)

Test in Desktop with “View as,” then again in the Service with “Test as role.” The two don’t always behave identically — check both.

**In Power BI Desktop:** *Modeling → View as*. Tick a role, and crucially, tick Other user and type a real UPN. Without that, `USERPRINCIPALNAME()` returns *your* account and your dynamic RLS will look like it works when it doesn't. This single checkbox is the most commonly missed step in dynamic RLS.

**In the Power BI Service:** open the semantic model’s security settings and use Test as role. This validates the role *assignments*, not just the DAX.

Four tests I now run every single time:

1. **Every role**, against a known expected row count.
2. **A user who isn’t in the mapping table** — confirm they see nothing (or your intended default), not everything.
3. **A user in two roles** — remember roles are *additive*: a user in two roles sees the union of both, not the intersection. People assume the opposite and get it backwards.
4. **Totals, not just tables**. A card showing a grand total is often where a leak shows up first, because it aggregates rows the user can’t see individually.

*Takeaway: “I tested it” means you tested as someone else. Testing as yourself proves almost nothing.*

## Assign Roles With Security Groups, Not People

You can assign individual users to a role. Please don’t, beyond a pilot.

Assign a **Microsoft Entra security group** instead. Then joiners and leavers are handled by whoever manages access, not by you republishing a list. It’s the difference between RLS being a one-time setup and RLS being a permanent chore with your name on it.

## RLS in Direct Lake and Fabric

Since a lot of us are on Fabric now: **RLS works with Import, DirectQuery, and Direct Lake semantic models**. The roles and DAX filters you write are the same — Direct Lake doesn’t change how RLS is authored, it changes how the semantic model reads data.

Two things worth knowing:

- Fabric also offers security at the **OneLake / warehouse layer,** which is separate from semantic-model RLS. They can coexist, and it’s worth being deliberate about which layer enforces what, rather than assuming one covers the other.
- Certain query patterns in Direct Lake can **fall back to DirectQuery**. RLS still applies, but performance characteristics change — so test with realistic data volumes, not a 500-row sample.

## What RLS Costs You (Performance)

RLS isn’t free. Every query a restricted user runs carries the security filter with it.

Keep it cheap:

- Keep RLS DAX simple. A filter on a single indexed-ish column is fast; a filter wrapping `CALCULATE` around several tables is not.
- Keep the mapping table small and low-cardinality. It’s queried constantly.
- Avoid RLS filters on huge fact tables — filter the dimension and let the relationship do the work.
- Avoid unnecessary many-to-many security relationships. They increase filter complexity and are a common source of slow, hard-to-debug RLS in production.
- Re-run Performance Analyzer with a role active. Your unrestricted timings are not the timings your users experience. (I wrote a whole post on [Power BI performance tuning](https://medium.com/towards-artificial-intelligence/my-power-bi-report-took-14-seconds-to-load-heres-everything-i-did-to-get-it-under-2-7ef5de8f5214) if you want the wider playbook.)

## Common RLS Mistakes — The Short List

- Testing as yourself and not using **Other user**.
- Assuming multiple roles **intersect** — they **union**.
- Forgetting that **workspace Contributors bypass RLS entirely**.
- Adding a **bi-directional relationship** to force a filter through, without re-testing.
- Assigning **individual users** instead of security groups.
- Leaving users **out of the mapping table** and calling the resulting blank report a bug.
- Expecting RLS to **hide columns** — that’s Object-Level Security.
- Never re-testing RLS after a **model change**. Relationships move; security follows.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9HVgz__MtvSaCOwy73eG6w.png)

The eight-step order I follow now. Step 6 is the one almost everybody skips — and it’s the one that catches leaks

## Your RLS Checklist

1. **Decide static or dynamic**. More than a few stable groups? Go dynamic.
2. **Build the user mapping table**. One row per user per entitlement.
3. **Write the role filter** with `USERPRINCIPALNAME()`.
4. **Verify the filter reaches the fact table** through single-direction relationships.
5. **Audit every bi-directional relationship** in the model.
6. **Test with “View as” + “Other user,”** then “Test as role” in the Service.
7. **Assign security groups**, not individuals.
8. **Re-test after every model change.**

## The Bigger Picture

Most of what we build as analysts fails loudly. A broken measure throws an error. A failed refresh sends an email. A bad join produces numbers so obviously wrong that someone asks within a day.

RLS is different. It fails silently, in the direction of *showing more*, and the person most likely to discover it is the one who shouldn’t have seen it.

That’s why I stopped treating security as the last checkbox before publishing and started treating it as part of the model design — decided at the same time as the star schema, not bolted on the night before launch.

The manager who messaged me that Tuesday was gracious about it. He didn’t have to be. Somewhere between his message and the fix, I stopped thinking of RLS as a Power BI feature and started thinking of it as a promise: *you will only ever see what’s yours.*

Test it like a promise. Because that’s what it is.

## FAQ

**What is row-level security in Power BI?**  
RLS restricts which rows a user can see in a semantic model. You define roles with DAX filters, assign users or security groups to those roles, and the filters apply automatically to every query those users run.

**What’s the difference between static and dynamic RLS?**  
Static RLS hardcodes a filter into each role (one role per group). Dynamic RLS uses a single role with `USERPRINCIPALNAME()` and a user mapping table, so adding a user is a data change instead of a model change. Dynamic scales better.

**Why is my dynamic RLS not working?**  
The two usual causes: you tested as yourself instead of using View as → Other user, or the filter can’t travel from the user table to the fact table through your relationships. Check the relationship path before you rewrite the DAX.

**Does RLS apply to workspace admins?**  
No. Users with Admin, Member, or Contributor roles in the workspace have edit permission on the semantic model, so RLS doesn’t apply to them. RLS applies to Viewers and to users consuming the report via an app or shared link.

**Can RLS hide columns or tables?**  
No — that’s Object-Level Security (OLS), configured through external tools like Tabular Editor. RLS filters rows only.

**If a user is in two RLS roles, what do they see?**  
The union of both roles. Roles are additive, not restrictive — a common and costly assumption to get backwards.