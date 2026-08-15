---
created: 2026-08-06
updated: 2026-08-06
source: Conditional Formatting in Power BI Multi-Row Card Visuals
note_type: workflow
tags: [conditional-formatting, multi-row-card, dax, unichar, power-bi, step-by-step]
---

# Add Conditional Formatting to Multi-Row Card

Step-by-step: create a UNICHAR-based DAX measure and apply it to a Multi-Row Card visual to display conditional formatting icons that are otherwise unavailable via the Format pane.

## Step 1 — Open Power BI Desktop

Open your report with the Multi-Row Card visual, or create one from the Visualizations pane.

## Step 2 — Create the Indicator Measure

1. In the Fields pane, right-click on the relevant table → **New measure**
2. Enter the DAX formula:

```dax
ProfitGrowthIndicator :=
VAR GreenCircle = UNICHAR(11044)
VAR RedCircle   = UNICHAR(128308)
RETURN
    IF(
        [Profit Growth] > 0,
        GreenCircle & " " & FORMAT([Profit Growth], "0.0%"),
        RedCircle   & " " & FORMAT([Profit Growth], "0.0%")
    )
```

3. Press **Enter** to save

## Step 3 — Apply the Measure to the Multi-Row Card

1. Select the **Multi-Row Card** visual
2. Drag the **ProfitGrowthIndicator** measure into the **Values** field

The visual now shows green/red circles alongside the percentage values.

## Step 4 — Add the Raw Number (Optional)

To show both the icon and the formatted number in the same card:

1. Drag the **Profit Growth** measure into the Multi-Row Card Values
2. Adjust the visual formatting to align icons and numbers cleanly

## Step 5 — Handle Blank Values (Optional but Recommended)

If some rows have no data, extend the formula:

```dax
ProfitGrowthIndicator :=
VAR GreenCircle = UNICHAR(11044)
VAR RedCircle   = UNICHAR(128308)
RETURN
    IF(
        ISBLANK([Profit Growth]),
        BLANK(),
        IF(
            [Profit Growth] > 0,
            GreenCircle & " " & FORMAT([Profit Growth], "0.0%"),
            RedCircle   & " " & FORMAT([Profit Growth], "0.0%")
        )
    )
```

This prevents a misleading icon from appearing when there is no data for that row.

## Step 6 — Switch to Arrows (Alternative Icons)

Replace the circle codes with arrow codes:

```dax
ProfitGrowthIndicator :=
VAR UpArrow   = UNICHAR(9650)   -- ▲
VAR DownArrow = UNICHAR(9660)   -- ▼
RETURN
    IF(
        ISBLANK([Profit Growth]),
        BLANK(),
        IF(
            [Profit Growth] > 0,
            UpArrow   & " " & FORMAT([Profit Growth], "0.0%"),
            DownArrow & " " & FORMAT([Profit Growth], "0.0%")
        )
    )
```

## Step 7 — Format the Visual

1. In the **Format pane**, adjust card size, font, and spacing to accommodate the icon + text
2. Ensure the number aligns correctly beside the icon
3. Test on a live report page with varied data to verify icons display correctly

## Tips

- The `FORMAT()` format string `"0.0%"` adds one decimal place and the % sign automatically
- Use `& " " &` (space between two ampersands) to separate the icon from the number
- UNICHAR codes 11044/128308 (emoji circles) render reliably in Power BI Desktop and export to PDF/PPT
- UNICHAR codes 9650/9660 (triangle arrows) are more universally supported across fonts than actual arrow characters

## Related

- [[Conditional-Formatting-in-Multi-Row-Card-Visuals]] — concept overview
- [[UNICHAR-based-Conditional-Formatting-Pattern]] — pattern reference with both circle and arrow variants
- [[UNICHAR-Icon-Codes-Reference]] — quick reference for icon codes
- [[UNICHAR]] — the DAX function reference
