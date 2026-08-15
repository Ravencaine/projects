---
title: "How to Validate Phone Numbers from Excel Online in Power Automate"
source: "https://medium.com/@cloudmersive/how-to-validate-phone-numbers-from-excel-online-in-power-automate-8cf00ce92426"
author:
  - "[[Cloudmersive]]"
published: 2026-08-05
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4X0ZOYTfCt512t5-Z88ZKw.jpeg)

Phone numbers have a special talent for showing up in every format imaginable. Some include their country codes, others arrive with a lively assortment of spaces and parentheses, and plenty more leave us guessing whether they’re usable at all.

Fortunately, we don’t have to sort through that mess one row at a time.

In this workflow, Power Automate retrieves vendor records from an Excel Online table, finds the phone numbers waiting for review, validates each one with the Cloudmersive Data Validation connector, and writes the results of that validation back to the same Excel row.

It’s a tidy little workflow with an outsized impact on contact data quality. Let’s build it.

## Validate Excel Phone Numbers in Power Automate

We’ll begin with an Excel table containing our vendor information and a unique record ID for each row.

Alongside the original phone number, we’ll include a **Phone Validation Status** column and several blank columns for the results. Setting the status to **Pending** gives our flow a simple way to find the records that still need attention.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Bzy9j-n8fG7P_rRAkDmEJg.png)

Next, we’ll create a cloud flow using whichever trigger best fits our process. We can run it manually, put it on a schedule, or connect it to a larger vendor-management workflow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Pf8aAWckR1gWtPUKvZRrlw.png)

Now we’ll add the Excel Online (Business) **List rows present in a table** action and point it toward our vendor workbook and table.

With that, the spreadsheet rows are ready to move through our validation process.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-bIXG_fOP3LvNihBtFTmNQ.png)

Next up, we’ll add a **Filter array** action.

For **From**, we’ll use the `value` output from **List rows present in a table**. We’ll then keep only the rows where **Phone Validation Status** is equal to `Pending`.

That gives us a clean validation queue without touching rows we’ve already processed.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XUaazp3ikpvP3rukpFEI2g.png)

From here, we’ll add an **Apply to each** control and use the **Body** output from **Filter array** as its input.

Our flow can now work through the pending vendor records one at a time.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*I_D1ih77oqnATa0De2nfDg.png)

Inside the loop, we’ll add the Cloudmersive Data Validation **Validate phone number (basic)** action.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5b_jKcjg_EqvBL_e0a3a9g.png)

For **Value/PhoneNumber**, we’ll use **Raw Phone Number** from the current Excel row. If our table includes a country code, we can also map it to **Value/DefaultCountryCode** to give locally formatted numbers a little extra context.

If this is our first time using the connector, Power Automate will prompt us to create a connection using our Cloudmersive API key.

The action returns a helpful set of structured results:

- **Successful**
- **IsValid**
- **CountryCode**
- **CountryName**
- **E164Format**
- **InternationalFormat**
- **NationalFormat**
- **PhoneNumberType**

In other words, one unpredictable phone-number entry comes back organized, standardized, and much easier to work with.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KAtoCNB5stXNhET_q1wjaQ.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NXCyFBztpn1DVNeka4HNQw.png)

Now we’ll add the Excel Online (Business) **Update a row** action beneath the validation step.

We’ll point it to the same workbook and table. For **Key Column**, we’ll choose our unique vendor record ID column. For **Key Value**, we’ll use the vendor record ID from the current row.

This little pairing is important: it guides Power Automate straight back to the exact row we just validated.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YaPbQS3uNDRxQAHMaJLlew.png)

Finally, we’ll open the action’s advanced parameters and pair the Cloudmersive outputs with their matching Excel columns.

We’ll change **Phone Validation Status** to `Validated`, populate the available validation fields, and enter the following expression in **Phone Validated At**:

`utcNow()`

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*i6UuZS7KREhh3S_ounBi6Q.png)

Just like that, every processed row receives its validation results and a fresh timestamp.

Now we’ll save our flow and give it a quick test.

The flow should collect the spreadsheet rows, process every record marked as Pending, and return the standardized phone-number details to those same rows.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BTVG3D2QAyDmBa87bKjW7g.png)

Back in Excel, we can watch the formerly empty result columns fill in with useful validation data.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MV5eYDqPuYPQrOFwI3y6ew.png)

And that’s the whole flow. Instead of manually untangling an international grab bag of phone-number formats, we now have a quick & repeatable process that does the sorting for us.

The same pattern works nicely for customer records, supplier directories, contact imports, and just about any other Excel-based list where phone-number quality matters.