---
title: "Power BI Selected Values: Clarify Visuals with DAX"
source: "https://databear.com/power-bi-selected-values/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-01-19
created: 2026-08-04
description: "Use DAX to show selected values in Power BI visuals, reduce confusion, and make reports clearer for occasional users."
Processed: "Unprocessed"
---
Power BI’s interactivity is powerful but without context, it can confuse users. That’s why displaying **Power BI selected values** using DAX is essential. It helps users instantly understand what filters are applied, especially when visuals dynamically change based on selections.

You’ll learn how to build a flexible DAX measure that makes **Power BI selected values** visible using functions like `CONCATENATEX`, `VALUES`, and `ISFILTERED`.

##### The Problem: Confusion From Interactions

Power BI’s interactive visuals are powerful, but they can be confusing especially to users who aren’t familiar with how one visual affects another. For example:

- A user selects a data point on a **tree map** …
- Then sees a **waterfall chart** suddenly filtered to only that one value…
- But doesn’t notice the **filter icon** or understand why the visual changed.

The result? Confusion, support emails, or worse loss of trust in the data.

Yes, you could use **Edit Interactions** to prevent visuals from filtering each other. But what if you *want* to maintain interactivity and just make the effects of those interactions *clearer*?

##### The Solution: A DAX Measure to Display Selected Values

Let’s build a DAX measure that clearly displays what the user has selected making your visuals easier to interpret and your reports more user-friendly.

##### Step 1: Create a “Visual Measures” Table

Create a new table to store your visual-specific DAX measures:

1. Go to **Modeling** > **Enter Data**.
2. Name your table (e.g., `Visual Measures`).
3. Add a placeholder column (you’ll delete this later).

##### Step 2: Write the “Selected Values Year” Measure

In your new table, create a new measure:

```
Selected Values - Year = 
IF (
    ISFILTERED('Date'[Calendar Year]),
    "Years selected: " & 
        CONCATENATEX (
            VALUES('Date'[Calendar Year]),
            'Date'[Calendar Year],
            ", "
        ),
    "All calendar years"
)
```

##### Breakdown:

- `ISFILTERED`: Checks if a filter is applied on `'Date'[Calendar Year]`.
- `CONCATENATEX` + `VALUES`: Creates a comma-separated list of the selected years.
- Else, it defaults to `"All calendar years"`.

You can use this measure inside a **Card Visual** to display the user’s selected years dynamically.

##### Step 3: Duplicate the Pattern for Other Fields

You can repeat this logic for any other field. For example, to track **Distance Group selections**, create a new measure like:

```
Selected Values - Distance Group = 
IF (
    ISFILTERED('Flight Distance'[Distance Group Name]),
    "Distance group selected: " & 
        CONCATENATEX (
            VALUES('Flight Distance'[Distance Group Name]),
            'Flight Distance'[Distance Group Name],
            ", "
        ),
    "All distance groups"
)
```

Just replace the field names accordingly.

##### Step 4: Use the New Card Visual for Better Formatting

The **new Card visual** in Power BI offers greater formatting flexibility:

- Switch the **layout** from Row to Column.
- Adjust **callout font size** (e.g., reduce it to 25pt).
- **Toggle off labels** if not needed.
- Use **color** to make the text pop and align with your report theme.

##### Step 5: Final Touches & Best Practices

- Delete the placeholder column from your `Visual Measures` table.
- Add your measures to the report canvas using the **new Card visual**.
- Consider adding multiple cards (for year, group, region, etc.) to show all selected filters clearly.
- Be consistent with naming: e.g., “Years selected”, “Distance group selected”, etc.

##### Why This Matters

This small enhancement improves the clarity and usability of your reports, especially for **non-technical or occasional users**. It reduces confusion, increases trust, and enhances the storytelling power of your Power BI dashboards.

By making user selections **visible and understandable**, you’re taking a huge step toward universal design principles in reporting.

##### Want to Learn More?

If you found this technique helpful, check out our **on-demand Power BI training** resources at [Data Bear’s Power BI Training](https://databear.com/power-bi-training/). You’ll find in-depth courses on:

- Power BI Storytelling
- Universal Design
- Advanced DAX Techniques
- And much more!