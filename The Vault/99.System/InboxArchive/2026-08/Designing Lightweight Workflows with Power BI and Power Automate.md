---
title: "Designing Lightweight Workflows with Power BI and Power Automate"
source: "https://medium.com/@jmwestendorp/designing-lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906"
author:
  - "[[Jacob Westendorp]]"
published: 2026-08-04
created: 2026-08-09
description: "Using DAX, Automate, and SharePoint to keep structured data aligned with real‑world activity"
Processed: "Unprocessed"
---
## Using DAX, Automate, and SharePoint to keep structured data aligned with real‑world activity

*This article was written with assistance from AI. Read my note on AI writing at the bottom of this article*

In my [last article](https://medium.com/@jmwestendorp/turning-power-bi-into-a-lightweight-data-source-for-automate-ea1b01307bd2?sharedUserId=jmwestendorp), I showed how to use a single, purpose-built datapoint from Power BI to trigger an alert in Power Automate. That works well for a small population and a very specific action. But what if you want to do more with Power BI data? Power BI is typically treated as read only, which means any change that affects reporting must happen upstream. One way to extend this is to supplement your dataset with transactional context stored in a collaboratively managed SharePoint list. The challenge is pairing fixed source data from Power BI with user-managed context without breaking the reporting model. Using Power Automate, the same pattern used to extract a single datapoint can be expanded to pull a scoped set of datapoints into SharePoint for action. Power BI remains the primary consumption layer, while SharePoint acts as a lightweight interaction surface.

**Conceptual Model**

At a high level, this pattern is about giving each tool a clear job. Power BI defines which contracts matter and provides the stable identifiers that everything else ties back to. Power Automate takes that contract set and keeps a SharePoint list in sync with it. The SharePoint list is where users interact, updating only the fields that require attention or action. When Power BI refreshes, it pulls that context back in and combines it with the original data so everything shows up in one place.

A key decision in this approach is being explicit about what can and cannot change. Core contract details like vendors, dates, and descriptions are treated as fixed reference points. Fields such as status, responsible owner, in-process flags, and notes are designed to change as work progresses. This distinction allows Power BI to remain reliable while still reflecting what is happening operationally.

**Scoping the Dataset (Critical)**

Before any automation logic runs, the contract population is intentionally constrained using a DAX EVALUATE statement scoped to active and current contracts only. This step does more than reduce volume. It uses DAX to explicitly define both the rows returned and the shape of the dataset that will be handed off to Power Automate. A practical approach is to use the DAX query view in Power BI Desktop to test the EVALUATE statement for completeness and efficiency. Once finalized, the same query can be passed directly into the Power Automate action, ensuring the automation layer consumes a dataset that has already been validated at the source.

Rather than returning an entire contract table, the query filters aggressively and projects only the fields that are required downstream. This allows the dataset to be structured with automation in mind, not just reporting. In practical terms, this means working with a large population of active contracts instead of the full historical population. The result is fewer SharePoint list items to manage, shorter and more predictable flow runtimes, and a much clearer mental model for users interacting with the list.

From a technical standpoint, DAX serves two purposes here. It defines what qualifies as in scope, and it shapes the output so the resulting JSON is predictable and easier to work with in Power Automate. An example of this pattern looks like the following:

```c
EVALUATE
SELECTCOLUMNS (
    FILTER (
        'Contracts',
        'Contracts'[Active Canceled] IN { "Active", "Lapsed" }
    ),
    "ContractID", 'Contracts'[ContractID],
    "ContractUniqueID", 'Contracts'[ContractUniqueID],
    "Contract Status", 'Contracts'[Active Canceled],
    "Contract Start", 'Contracts'[ContractStart],
    "Contract End", 'Contracts'[ContractEnd]
)
```

**Working with the Data**

In the previous article, the flow operated on a single datapoint, which made direct selection and mapping straightforward. Each value could be referenced explicitly, and there was no need to reason about collections or structure. Once the scope expands to a full contract population, that approach breaks down. Instead of handling one value, the Power BI action now returns a dataset as an array of records, which requires a different way of thinking.

This is where the Parse JSON step becomes essential. The output from Power BI is technically usable as-is, but in practice it is cumbersome and fragile to work with directly. Parsing the response converts the raw array into a structured object that Power Automate can understand natively, exposing each contract and its attributes as predictable dynamic content.

This is also the step where I struggled the most when moving from Power BI into truly actionable data. I am comfortable working with M, DAX, and measures, but the level of precision required by a JSON schema took some trial and error to get right, both functionally and efficiently. Even with a well-shaped dataset, Power Automate expects the structure to be explicit, and that shift in mindset is nontrivial.

Taking the time to parse the JSON early creates a clear boundary between data extraction and business logic. Once the dataset is parsed, the flow can treat each contract consistently and reliably, rather than relying on long expressions or assumptions about structure. That discipline pays off quickly, making the rest of the flow easier to build, easier to debug, and easier to extend as requirements evolve.

This is also a good point to call out a built-in assist in Power Automate. The Parse JSON action allows you to generate a schema directly from a sample payload, which is often the fastest way to get unstuck. By running the Power BI action once and capturing a sample of the returned array, you can use the import schema option to scaffold the expected structure instead of hand-authoring it.

That said, I am intentionally not including the full schema here. Once the dataset is properly shaped in DAX, schema generation becomes largely mechanical. The real work happens upstream by constraining and structuring the dataset so that each row resolves cleanly into a flat, predictable object. At that point, the import schema tool is validating intent rather than defining it.

The main takeaway is not the schema itself, but the discipline of making the structure explicit. Let DAX define the rows and columns, let Power Automate infer the schema from a representative sample, and confirm that the parsed output exposes exactly the fields you expect before moving on to business logic.

As a practical sanity check, I found it useful to scan the generated schema and confirm that it matched the SELECTCOLUMNS output one to one before wiring up any downstream actions. Power Automate will sometimes introduce additional nesting or bracketed property names, which can throw the imported schema off if not caught early.

**Enter the SharePoint List**

With the Power BI dataset now actionable, the next step is to bring SharePoint into the flow so user-managed context can be paired with the contract data. The ContractID serves as the key column that ties everything together. By setting this value as a variable for each contract, the flow has a reliable way to test against the existing SharePoint list.

A standard SharePoint connector using Get items is sufficient to return the current list of contracts. If the list is large or contains many columns, this step can be made more efficient by creating a dedicated SharePoint view that exposes only the key column or a small subset of required fields. This reduces the amount of data passed into Power Automate and improves overall performance. There is a slight operational risk in relying on a specific view that could be changed by end users if it is not governed properly, but in practice the efficiency gains tend to outweigh that risk.

For each contract in the dataset, the flow evaluates whether a matching SharePoint item already exists. If a match is found, the item is updated. If no match exists, a new item is created. If a SharePoint item no longer corresponds to an active contract, it is flagged for update or removal as part of the reconciliation logic. The result is a SharePoint list that continuously reflects the active contract population while preserving any user-entered operational context.

The flow is built to handle repeat runs safely. Running it again will not create duplicates or undo user updates. It only aligns the SharePoint list with the current state of the data.

**Handling Changing Data**

The final piece of the pattern is identifying contracts that no longer appear in the active Power BI dataset. Because the dataset is intentionally scoped to current contracts, some SharePoint items will eventually represent records that have fallen out of scope.

At this stage, those records are flagged rather than deleted. ContractIDs that no longer exist in the Power BI result set are marked and surfaced through curated SharePoint views. This allows teams to intentionally separate inactive or obsolete contracts from the active working set without immediately discarding information that may still be relevant elsewhere.

This approach introduces a deliberate pause between detection and deletion. Some records may still require follow-up, historical capture, or downstream handling that falls outside the scope of this workflow. By using flags and views instead of hard deletes, the SharePoint list remains clean for day-to-day use while preserving flexibility for operational or reporting needs that extend beyond this pattern.

This final reconciliation step ensures that SharePoint stays aligned with the Power BI dataset without quietly accumulating stale records, while also avoiding premature deletion of data that may still carry value. It keeps the interaction surface focused and current, and leaves decisions about long-term retention or archival exactly where they belong.

**Bringing the Data Back into Power BI**

This is ultimately what all of this work is for. Once operational context is being captured and maintained in SharePoint, Power BI can ingest that list as a secondary dataset and join it back to the core contract model using the same contract identifier.

The result is a unified semantic model where source-of-truth contract data remains stable, while operational signals are free to evolve independently. Reports can now show not just what a contract is, but what is actively happening to it. Status, ownership, and in‑process context live alongside contract facts without forcing changes upstream.

Nothing in SharePoint overwrites source contract data. The integration is intentionally additive. Power BI continues to represent the authoritative state of the contract, while SharePoint contributes a layer of human and process-driven context that would otherwise be invisible in traditional reporting.

This is where the pattern comes full circle. Power BI defines the population and anchors the facts, Power Automate keeps the systems aligned, and SharePoint captures the operational reality. Together, they produce reporting that reflects both structure and motion, without asking any single system to do more than it is well suited for.

**Conclusion**

In summary, this pattern is about extending Power BI without forcing it to be something it is not. By letting Power BI define the population and anchor the facts, using Power Automate to reconcile change, and capturing operational context in SharePoint, you gain visibility into both structure and motion. The result is reporting that reflects not just what exists, but what is actively happening, without pushing write-back into upstream systems or creating an accidental system of record. This approach works best when scope is clear, populations are controlled, and users understand the distinction between source data and operational context. Used deliberately, it is a practical way to bridge reporting and action while keeping each platform aligned to its strengths.

![Workflow diagram showing a Power Automate process that runs a DAX query against a Power BI dataset, parses the JSON output, loops through each record, updates or creates matching SharePoint items, and flags items that fall out of scope.](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*__bldiAEpnIcAwSL9ZiXRw.png)

A Power Automate flow that queries a scoped dataset, parses it, and synchronizes user‑managed context in SharePoint.

### A note on AI writing

I think one thing that gets lost in the “AI wrote this” conversation is how AI tools can function as training wheels. When I look back at what I wrote in early 2026, it’s cringy and obviously AI‑shaped. But it got me writing, it gave me a voice to start from, even when I wasn’t sure of myself. I could plunk out a rough draft and use AI to edit, transform, and craft my writing. It was great in that the tools used language, structure, and form that made my idea seem more impressive and artificially smooth.

Except it did not, not really, it puffed up and hyperbolized simple ideas and used more and more words to describe complex ideas until they lost meaning. Even with careful line by line editing, the writing was still not my own. I see that now and am working to develop as a better writer on my own. While I still use AI, I am consciously using less and less as I find a more authentic tone in my own work.