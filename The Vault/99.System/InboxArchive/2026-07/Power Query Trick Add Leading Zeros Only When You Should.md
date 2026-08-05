---
title: "🧙 Power Query Trick: Add Leading Zeros Only When You Should"
source: "https://medium.com/@markchen69/power-query-trick-add-leading-zeros-only-when-you-should-625bd5040111"
author:
  - "[[Mark Chen]]"
published: 2025-06-26
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
It started with a simple column in Excel — or so I thought.

Column1 had a messy little party going on:

- Some values were **4-digit numbers** like `1001`
- A few were **3-digit numbers** like `100`
- Others were already **text values**, like `"ABC"` or `"T-900"`
- And some were **5-digit numbers**, like `10010`
![](99.System/Attachments/1!4-Wx7Ltc9_IoNtV_K5OhRg.png.webp)

What I *wanted* was a clean column where:

1. All **3-digit numbers** were padded with a leading zero: `100` → `"0100"`
2. All other values — whether text or longer numbers — stayed untouched
3. Everything was formatted as **text**, for consistency

Sounds simple. Until you realize that Power Query doesn’t babysit type mismatches. So I rolled up my sleeves and wrote this:

## ✅ The Safest Way to Pad 3-Digit Numbers (and Nothing Else)

```c
= Table.TransformColumns(
    Source,
    {{"Column1", each if Value.Is(_, type number) and Text.Length(Text.From(_)) = 3
        then Text.PadStart(Text.From(_), 4, "0")
        else Text.From(_), type text}}
)
```

Let’s unpack that little marvel.

## 🔍 What’s Happening Here:

- `Value.Is(_, type number)` checks if the value is numeric — so we don’t mess with pure text
- `Text.Length(Text.From(_)) = 3` ensures we only touch **3-digit** numbers
- `Text.PadStart(..., 4, "0")` does the padding
- `else Text.From(_)` leaves everything else alone, but coerces it into text for output consistency

## 📌 Why Not Use Simple PadStart Everywhere?

Because that would give you:

- `100` → `"0100"` ✅
- `1001` → `"1001"` ✅
- `ABC` → `"0ABC"` 🚨
- `T-900` → `"0T-900"` 🤯

So yeah. Be gentle. Use conditions. 🧠

## 💬 Final Thoughts

Power Query is brilliant, but it doesn’t protect you from assumptions.  
This little trick makes sure:

- You **only pad when needed**
- You **don’t corrupt existing data**
- And you keep things nice and **textually consistent**

> *“In a world of type chaos, be the query that thinks twice.”*

🎁 Now go forth — and tidy those columns with the respect they deserve.