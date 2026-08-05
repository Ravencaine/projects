---
title: "🔄 Sorting Non-Adjacent Column Pairs in Excel"
source: "https://medium.com/@markchen69/sorting-non-adjacent-column-pairs-in-excel-c8ac3473fee2"
author:
  - "[[Mark Chen]]"
published: 2025-06-24
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
It started innocently. I had an Excel table with two key columns:

- `Account Type` (say in column A)
- `Ledger Account` (somewhere distant, like column C)

Naturally, each Account Type could show up with multiple Ledger Accounts — the classic many-to-one setup. But here’s the itch: I wanted to **see all the unique pairs**, **sorted by Account Type**, then **Ledger Account**, *without moving columns around like a barbarian*.

Yes. I wanted Excel sorcery.

## 😤 First Reaction: Why Can’t I Just UNIQUE(A2:A100, C2:C100)?

I tried it.

```c
=UNIQUE((A2:A100, C2:C100))  ❌
```

Excel threw a tantrum like I’d asked it to solve quantum physics with a crayon. Turns out, **you can’t directly apply** `**UNIQUE()**` **to non-adjacent columns**.

## 💘 Then I Met CHOOSE() — and We Made a Table

That’s when `CHOOSE()` entered like a hot barista in a spreadsheet café:

```c
=CHOOSE({1,2}, A2:A100, C2:C100)
```

This merges non-adjacent columns into a virtual 2D array. Two distinct columns — now talking. It’s like Excel couples counseling.

Pair it with `UNIQUE()` and we’re cooking:

```c
=UNIQUE(CHOOSE({1,2}, A2:A100, C2:C100))
```

Now I had all the distinct `Account Type` + `Ledger Account` combos. But they were messy.

## ✨ Next Level: Sorting the Lovebirds

I wanted order. The kind where **Account Type alphabetizes first**, and within each, **Ledger Account** follows like a loyal pup.

That’s where `SORT()` strutted in:

```c
=SORT(UNIQUE(CHOOSE({1,2}, A2:A100, C2:C100)), {1,2}, {TRUE,TRUE})
```
![](99.System/Attachments/1!LkbF0yfRX0dnkeb8FWijQA.png.webp)

> *✅ Voilà: A tidy, deduplicated, alphabetically sorted set of pairs.*

- `{1,2}` means sort first by column 1, then 2.
- `{TRUE,TRUE}` means both ascending.

No more manual moving. No more helper columns. Just one cell — and full control.

## 🔍 Reflections: What Did I Actually Learn?

1. **You can pair non-adjacent columns** with `CHOOSE()` — mind-blowing.
2. `**UNIQUE()**` \*\* + `**SORT()**` + \*\* `**CHOOSE()**` = a powerful array cocktail.
3. Excel is sexier when you stop clicking and start thinking in formulas.

## 🧵 Bonus: Want to Take It Further?

- Filter by condition inside `CHOOSE()`? Yes.
- Wrap in `LET()` to optimize performance? Even better.
- Drop into Power BI? Absolutely.

## 🎁 TL;DR: Final Formula

```c
=SORT(UNIQUE(CHOOSE({1,2}, A2:A100, C2:C100)), {1,2}, {TRUE,TRUE})
```

> *“Data is like a relationship — if two columns are meant to be together, don’t let adjacency get in the way.”*

Now go on — weave your non-adjacent lovers together and make your Excel shine.