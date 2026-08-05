---
created: 2026-07-30
updated: 2026-08-02
source: "dax4humans_ch6_timezone.txt"
note_type: pattern
tags: [timezone, utc, date-time, conversion]
---

# Timezone Conversion in DAX

Converts a source time from one timezone to multiple destination timezones using UTC as the intermediate reference point and UTC offset arithmetic.

## Purpose

When reports span multiple geographic regions, times must be displayed in each local timezone. DAX has no built-in timezone functions — this pattern uses simple UTC offset arithmetic to convert between timezones, including crossing the date boundary.

## Components

- `TIME(hour, minute, second)` — constructs a time value
- UTC offset as a decimal fraction of a day (offset ÷ 24)
- Addition/subtraction to convert through UTC as the pivot

## Structure

```dax
TZ Convert =
  VAR __SourceTime     = TIME( 13, 0, 0 )          -- source time to convert
  VAR __SourceTZOffset = -5 / 24                    -- source UTC offset (e.g. EST = UTC-5)
  VAR __DestTZOffset   = MAX( 'Time Zones'[UTC Offset] ) / 24  -- destination offset from table
  VAR __UTCTime        = __SourceTime - __SourceTZOffset        -- convert source to UTC
  VAR __Result         = __UTCTime + __DestTZOffset              -- convert UTC to destination
  RETURN __Result
```

## Example

| Abbr | Name | UTC Offset | Result |
|------|------|-----------|--------|
| EST | Eastern Standard Time | -5 | 8:00 AM |
| GMT | Greenwich Mean Time | 0 | 1:00 PM |
| JST | Japan Standard Time | +9 | 10:00 PM (+1 day) |

If the result date is `12/31/1899`, the destination timezone is one calendar day ahead of the source.

## Variations

**Fixed source timezone (no lookup table):**
```dax
VAR __SourceTZOffset = -5 / 24   -- hardcoded source offset
```

**Multiple destination columns:**
```dax
VAR __DestTZOffset = -8 / 24     -- PST
```

**Dynamic destination from a slicer:**
```dax
VAR __DestTZOffset = SELECTEDVALUE( 'Time Zones'[UTC Offset] ) / 24
```

## Notes

- UTC offsets are divided by 24 because DAX stores dates as serial numbers where 1 = one day.
- A negative UTC offset (e.g. EST = UTC-5) becomes a smaller negative fraction; subtracting it from the source time effectively adds hours.
- Crossing the date boundary is visible in the date portion of the result — check for `12/31/1899` to detect when the destination is ahead by a full day.

## Related

- [[duration-calculations-in-dax]] — related date/time arithmetic
- [[time-intelligence-functions]] — DAX built-in time functions
