---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "date-time", "unix", "epoch", "timestamp"]
note_type: pattern

---

# Unix Times in DAX

Converting Unix timestamps (seconds/milliseconds since 1970-01-01) to datetime.

## Unix Seconds to Date

```dax
Unix to Date :=
DATE( 1970, 1, 1 ) + [UnixSeconds] / 86400
```

## Unix Milliseconds to Date

```dax
Unix ms to Date :=
DATE( 1970, 1, 1 ) + [UnixMs] / 86400000
```

## Date to Unix

```dax
Date to Unix :=
( [Date] - DATE( 1970, 1, 1 ) ) * 86400
```

## Notes

- 86400 = seconds per day; 86400000 = milliseconds per day
- Common in API data (Twitter, financial feeds, logs)

## Related

- [[date-table-creation-in-dax]]
- [[duration-calculations-in-dax]]
