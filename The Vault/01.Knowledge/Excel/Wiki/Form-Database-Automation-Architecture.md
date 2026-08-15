---
created: 2026-08-09
updated: 2026-08-09
source: "Build an Automated Excel Database • My Online Training Hub"
note_type: pattern
tags: [excel, database, forms, excel-table, office-scripts, automation, architecture, crm, scalable-system]
---

# Form-Database-Automation Architecture

A lightweight Excel database system has three distinct layers: a data entry form (user-facing), an Excel Table (storage), and an automation layer (form → table). Analysis tools sit on top of the table.

## Three-Layer Architecture

```
┌─────────────────────────────────────┐
│ Layer 1: Data Entry Form            │
│   - Input cells with Data Validation│
│   - TODAY() for Date field         │
│   - XMATCH duplicate warnings       │
│   - Sheet protection (locked cells) │
└────────────────┬────────────────────┘
                 │ Office Script (one-click button)
┌────────────────▼────────────────────┐
│ Layer 2: Excel Table (ClientData)  │
│   - Structured references           │
│   - Auto-expands on new rows       │
│   - Duplicate warning banner        │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│ Layer 3: Analysis                  │
│   - Filter/sort, PivotTables       │
│   - Charts, dynamic reports        │
│   - COUNTIF/SUMIFS summaries       │
└─────────────────────────────────────┘
```

## Why Each Layer Exists

| Layer | Purpose | Why Separate |
|-------|---------|-------------|
| Form | Clean, guided user input | Reduces errors, enforces structure |
| Table | Structured, scalable storage | Auto-expand, named, filterable |
| Analysis | Insights and reporting | Depends on clean, structured data |

## Application Scenarios

- Client/CRM management
- Inventory tracking
- Expense tracking
- Employee information
- Project management

## Key Design Principles

- Keep form and database on separate sheets
- Use Excel Tables for the database (not plain ranges)
- Automate the save step (Office Scripts or VBA)
- Protect only the input cells on the form
- Validate before saving (XMATCH in the form itself)

## Related

- [[Source-Automated-Excel-Database-Mynda-Treacy]] — source
- [[Office-Scripts-Form-Database-Automation]] — how to automate the form→table step
- [[XMATCH-for-Form-Level-Duplicate-Detection]] — form-level validation
- [[Data-Entry-Form-Best-Practices]] — form design specifics
