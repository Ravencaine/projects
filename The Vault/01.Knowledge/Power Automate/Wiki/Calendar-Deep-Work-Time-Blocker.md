---
created: 2026-08-10
updated: 2026-08-10
source: 10 Power Automate Flows That Actually Save Hours — Not Just Demos
source_url: https://medium.com/@kaklotarrahul79/10-power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3
note_type: pattern
tags: [power-automate, recurrence, calendar, deep-work, productivity, automation]
---

# Calendar Deep Work Time-Blocker

Every Sunday evening, scan the calendar for open blocks of 2+ hours in the coming week and automatically create "Deep Work — Do Not Book" events with status set to Busy to prevent colleagues from scheduling over them.

## Purpose

Open calendar slots get instantly booked by colleagues. By proactively blocking 2+ hour deep work windows before the week starts, the user protects their focus time without manually hunting for gaps.

## Components

1. **Trigger:** Recurrence — Every Sunday evening (e.g., Sunday at 7:00 PM)
2. **Action:** Get calendar events for the next 7 days (Office 365 Outlook — Get calendar view)
   - Start time: tomorrow 8:00 AM
   - End time: tomorrow 6:00 PM (iterate through each day)
3. **Action:** For each day, find gaps ≥ 2 hours between existing events
4. **Action:** Create a "Deep Work" calendar event
   - Subject: "Deep Work — Do Not Book"
   - Status: **Busy** (critical — this blocks colleagues from booking the slot)
   - Show as: Busy
   - Duration: the open gap (minimum 2 hours)

## Structure

```
Trigger:   Recurrence — Weekly (Sunday 7:00 PM)
     ↓
Action:   Get calendar view (Office 365 Outlook)
          Start time: tomorrow 8:00 AM
          End time: tomorrow 6:00 PM
     ↓
Apply to each (day of the week):
     ↓
Action:   Find free slots ≥ 2 hours
          (Calculate: event_end[n] - event_start[n+1] >= 2hrs)
     ↓
Action:   Create calendar event
          - Subject: Deep Work — Do Not Book
          - Status: Busy
          - Show as: Busy
          - Start: gap start time
          - End: gap start + gap duration
```

## Key Detail

Setting `Show As: Busy` (or `Status: Out of Office`) on the created events is essential — this makes the blocks visible to anyone trying to schedule a meeting with the user.

## Variations

- **Daily morning version:** Run Monday morning to fill in gaps created by cancelled meetings during the day
- **Hybrid:** Create the blocks with a 15-minute buffer at each end to prevent partial meeting bookings

## Hours Saved

~3–5 hours/week of protected focus time.

## Related

- [[Weekly-Status-Report-Aggregator]]
- [[Flagged-Email-to-Planner-Task]]
