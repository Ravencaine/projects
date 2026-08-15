---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, text, formatting, phone, validation]
note_type: pattern

---

# Phone Number Formatting in DAX

Cleaning and formatting phone numbers from raw inconsistent input.

## Purpose

Phone numbers arrive in dozens of formats: `(555) 123-4567`, `555-123-4567`, `+1 555 123 4567`, `5551234567`. DAX text functions can standardize these.

## Strip Non-numeric Characters

```dax
Digits Only :=
VAR __Raw = [PhoneRaw]
VAR __Digits = SUBSTITUTE( SUBSTITUTE( SUBSTITUTE( SUBSTITUTE( __Raw,
    "(", "" ),
    ")", "" ),
    "-", "" ),
    " ", "" )
RETURN
__Digits
```

## Format as (XXX) XXX-XXXX

```dax
Phone Formatted :=
VAR __Digits = SUBSTITUTE( SUBSTITUTE( SUBSTITUTE( SUBSTITUTE(
    [PhoneRaw], "(", "" ), ")", "" ), "-", "" ), " ", "" )
VAR __Area = LEFT( __Digits, 3 )
VAR __First3 = MID( __Digits, 4, 3 )
VAR __Last4 = RIGHT( __Digits, 4 )
RETURN
"(" & __Area & ") " & __First3 & "-" & __Last4
```

## Notes

- For international numbers, consider handling the country code separately
- Power Query's `Text.Clean()` and `Text.Remove()` are more concise for heavy cleaning
- Use `CONTAINSSTRING()` to check if a number starts with `+` for country code detection

## Related

- [[text-extraction-patterns-in-dax]]
- [[replace-substitute]]
- [[left-right-mid]]
