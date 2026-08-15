---
title: "I Built a Power Automate Flow Just to Remove Copy-Paste (and That Was the Point)"
source: "https://medium.com/@anggitapinasthikadewi/i-built-a-power-automate-flow-just-to-remove-copy-paste-and-that-was-the-point-ba3c71632f99"
author:
  - "[[Anggita Pinasthika Dewi]]"
published: 2025-12-13
created: 2026-08-09
description: "What I learned from automating a tiny part of my work"
Processed: "Unprocessed"
---
## What I learned from automating a tiny part of my work

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*KzHeHkA57FWIxNJr)

Photo by Christopher Gower on Unsplash

My manager once gave me a task that sounded simple, but never really was.

I had to recap every valid defect raised in Jira.  
Some defects were already sitting in our defect tracker.  
Some had new impacted test cases that didn’t exist yet in the recap file.

So I had to:

- Check the defect tracker
- Identify which Jira IDs were valid
- Copy the Jira ID and impacted test cases
- Paste them into a separate recap file
- Make sure nothing was duplicated

Over and over again.

At some point, I thought:  
*This shouldn’t need my brain.*

I just wanted something where I could push a button, and it would copy-paste any impacted test case with a Jira ID — as long as it was considered a valid defect.

## Why There Are Two Files in the First Place

The reason this work even exists is because we use two different files:

- **Defect Tracker**  
	This is where everyone works. It’s collaborative, detailed, and already  
	heavy.
- **Recap File**  
	This is my manager’s space.  
	Not everyone can touch it.

The recap file tracks things like:

- When the defect was raised
- Release note date
- Delivery date
- Whether it’s been retested
- Whether it’s repeated
- Whether it’s rejected

It’s mostly used for management and administration, not daily execution.

If we put all those properties into the defect tracker, it would become even more crowded and harder to maintain. So the recap file stays separate — and that separation creates manual work.

## The Actual Manual Pain (Copy-Paste Reality)

My responsibility was very specific:

> *Copy Jira IDs and impacted test cases from the defect tracker into the recap file.*

But the data wasn’t static.

- Impacted test cases could increase every day
- Jira IDs could already exist in the recap file
- I had to make sure nothing was duplicated
- I had to keep track of which defects were delivered, repeated, rejected, or fixed

The copy-paste itself wasn’t the hardest part.  
The **attention cost** was.

I wanted to remove that part, so I could focus on defect delivery and coordination, not Excel mechanics.

## What the Automation Actually Did (Nothing More, Nothing Less)

The automation I built focused on **one thing only**:  
copying valid defects correctly.

Here’s the scope, very clearly:

- If a row in the defect tracker had a Jira ID → it was considered a valid defect
- The flow copied the Jira ID and impacted test cases into the recap file
- If impacted test cases existed in multiple cells, they were merged into one cell in the recap file  
	(this was my manager’s rule — I didn’t change it)
- The flow checked for duplicates:  
	If the Jira ID already existed and the impacted test cases were the same → do nothing,  
	If the Jira ID existed but the impacted test cases were different → append them

That’s it.

It didn’t decide statuses.  
It didn’t manage delivery logic.  
It only prepared clean data.

## Why Power Automate — and Why It Stopped There

I used Power Automate (cloud) mainly because of access.

- We’re fully on Microsoft
- Files live in SharePoint
- Excel is private under company folders
- Power Automate cloud could access all of that safely

I did try other things:

- Power Automate Desktop
- Docker
- n8n

But access and setup became blockers very quickly.

The cloud flow worked — for about two weeks.

Then it broke in a very specific edge case:

- One cell in the Jira ID column contained more than one Jira ID
- The flow kept copy-pasting endlessly
- I couldn’t figure out a clean fix in the time I had

It wasn’t that I gave up.  
I simply didn’t have the capacity anymore — our workload was already too much.

Around the same time, one of my coworkers and I decided to move our tracking into **Notion**, which fit our needs better.

That story is for another article.

## How I Built the Flow — High Level

I won’t go into full technical detail here yet, but at a high level, the flow looked like this:

1. Manual button trigger (on purpose, for control)
2. Read rows from the defect tracker
3. Filter rows with Jira IDs
4. Loop through each valid defect
5. Check if the Jira ID already exists in the recap file
6. Create or update the row based on impacted test cases

I’ll write a deeper, step-by-step version separately.

## Why I Still Wanted to Share This

Even though this automation is no longer used, I still wanted to share it.

Because it proves something to myself:

- I try to solve problems, even small ones
- I’m willing to experiment in real environments
- I want to be useful — to myself and to people around me

And I want to give myself permission to try, fail, and learn outside of perfect conditions.

## Closing Thought

This automation was temporary.

But if I hadn’t tried it, I wouldn’t have known:

- where the real bottlenecks were
- what the tool could and couldn’t do
- or what a better solution might look like later

I did feel like I failed when it stopped working.  
But it was still worth building.

I don’t regret trying.