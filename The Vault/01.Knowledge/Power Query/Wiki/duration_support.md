---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: reference
tags: [m-language, dates, duration]
---


# Duration Support in Power Query M

M supports duration values representing a span of time. Durations are constructed with `#duration(days, hours, minutes, seconds)` and support arithmetic with dates, datetimes, and other durations.

## Quick Reference

| Literal | Meaning |
|---------|---------|
| `#duration(1, 2, 30, 0)` | 1 day, 2 hours, 30 minutes, 0 seconds |

### Arithmetic

| Operation | Result |
|-----------|--------|
| `datetime + duration` | datetime shifted forward |
| `datetime - duration` | datetime shifted backward |
| `datetime - datetime` | duration between datetimes |
| `date - date` | duration between dates |
| `duration + duration` | combined duration |
| `duration - duration` | difference |
| `duration * number` | scaled duration |
| `duration / number` | divided duration |

### Total Accessors

| Function | Returns |
|----------|---------|
| `Duration.Days(d)` | Integer days component |
| `Duration.Hours(d)` | Integer hours component |
| `Duration.Minutes(d)` | Integer minutes component |
| `Duration.Seconds(d)` | Integer seconds component |
| `Duration.TotalDays(d)` | Total days as number |
| `Duration.TotalHours(d)` | Total hours as number |
| `Duration.TotalMinutes(d)` | Total minutes as number |
| `Duration.TotalSeconds(d)` | Total seconds as number |

## Examples

```m
#date(2025, 7, 24) - #date(2025, 7, 23)        // #duration(1, 0, 0, 0)
#datetime(2025, 7, 24, 12, 0, 0) - #duration(0, 2, 0, 0)  // #datetime(2025, 7, 24, 10, 0, 0)
Duration.TotalHours(#duration(1, 2, 30, 0))   // 26.5
```

## Related

- duration_support — Duration.* functions
- [[standard_date_and_time_format_strings]] — formatting durations
