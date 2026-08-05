---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "conditional-formatting", "color", "dax", "format"]
note_type: pattern

---

# Conditional Formatting via DAX

Using DAX measures to dynamically control Power BI conditional formatting.

## Purpose

Power BI's built-in conditional formatting is limited. DAX measures provide full control over color, icons, and data bars.

## Dynamic Color via Measures

```dax
KPI Color :=
VAR __Value = [Sales]
VAR __Target = [Target]
RETURN
SWITCH(
    TRUE(),
    __Value >= __Target * 1.1, "green",
    __Value >= __Target,        "yellow",
    "red"
)
```

Apply in Power BI: Format pane > Conditional formatting > Field value > select the measure.

## Dynamic Icon (SVG)

```dax
KPI Icon :=
VAR __Value = [KPI]
VAR __Icon = IF( __Value >= 0, UNICHAR( 9650 ), UNICHAR( 9660 ) )
RETURN
__Icon & " " & FORMAT( __Value, "0.0%" )
```

## Notes

- Use SVG measures with the Image visual for more complex conditional formatting
- UNICHAR() provides arrow and symbol icons

## Related

- [[svg-visualizations-in-power-bi]]
- [[UNICHAR]]
