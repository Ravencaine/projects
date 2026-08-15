

## 2026-08-10 — Tony Phillips (Google Maps + Excel Integration)

Sources: 1 file (Google Maps took my Excel spreadsheet to the next level, How-To Geek, Tony Phillips, 2026-07-29) → pending archive

Notes: 2 written (Excel)
KBs: Excel (2 notes)

New notes:
- [[Excel-to-Google-My-Maps-Integration]] — workflow — Excel → Google My Maps: data prep, import, pin styling, layers, reimport
- [[Source-Google-Maps-Excel-Integration-Tony-Phillips]] — source — Tony Phillips, How-To Geek

Errors fixed: 0 | Link ops: 0

## 2026-08-10 — REPT In-Cell Charts (1 source)

Sources: 1 file (Excel REPT Function In Cell Charts, MyOnlineTrainingHub, 2026-06-23) → 99.System/InboxArchive/2026-08/

Notes: 9 written (Excel)
KBs: Excel (9 notes)
Errors fixed: 0 | Link ops applied: 0

## 2026-08-09 — Mynda Treacy batch (10 sources)

Sources: 10 files (5 Boring Excel Functions, 2026-07-21; 5 Hidden Excel Formula Rules, 2025-12-02; 6 Better Alternatives to IF, 2026-06-09; 10 Custom Number Formatting Tricks, 2026-06-16; Advanced CF Using Formulas, 2026-04-28; Dynamic Excel Report 4 Formulas, 2026-05-05; Automated Excel Database, 2025-09-23; Dynamic Drop-Down Lists, 2025-10-28; Excel File Protection Tricks, 2026-05-19; Excel HYPERLINK Function, 2025-11-11) → 99.System/InboxArchive/2026-08/
Notes: 76 written (Excel)
KBs: Excel (76 notes)
Author: Mynda Treacy (MyOnlineTrainingHub)
Author extended: Mynda Treacy (10 sources now)

New notes (source 10 of 10 — Excel HYPERLINK Function):
- [[Source-HYPERLINK-Function-Mynda-Treacy]] — source
- [[CELL-address-Dynamic-Cell-Reference-Retrieval]] — atomic — CELL("address", ref) returns absolute address string; bridge between lookup result and HYPERLINK text arg
- [[HYPERLINK-Syntax-Sheet-Name-Quoting]] — reference — syntax, single-quote wrapping for sheet names with spaces; best practice: always quote
- [[Sheet-Navigation-TOC-HYPERLINK]] — pattern — HYPERLINK("#"&sheet&"!A1", sheet&" Report"); Table of Contents for multi-sheet workbooks
- [[File-Folder-Hyperlinks]] — reference — direct file/folder paths; OneDrive/SharePoint paths for shared workbooks
- [[Dynamic-Hyperlink-XLOOKUP-CELL]] — pattern — HYPERLINK("#"&CELL("address",XLOOKUP(...))); dynamic row-jump from dropdown selection
- [[Broken-File-Paths-HYPERLINK-Does-Not-Validate]] — gotcha — HYPERLINK accepts any string; no validation of file existence; always test before sharing
- [[CtrlK-Static-vs-Formula-Dynamic-Hyperlink]] — gotcha — Ctrl+K = static object; =HYPERLINK() = dynamic formula; do not confuse

New notes (source 3 of 3 — 6 Better Alternatives to IF):
- [[Source-6-Better-Alternatives-to-IF-Mynda-Treacy]] — source
- [[IFS-vs-Nested-IF-Order-Matters]] — atomic — IFS evaluates ALL conditions (no short-circuit); nested IF short-circuits; order matters for correctness
- [[XLOOKUP-vs-IF-for-Lookup-Tables]] — atomic — lookup table + XLOOKUP replaces hard-coded IF chain; maintain table, not formula
- [[SWITCH-vs-IF-One-Value-Multiple-Matches]] — atomic — SWITCH tests one value once; returns different calculations per option; dropdown-driven reports
- [[CHOOSE-for-Position-Based-Mapping]] — atomic — CHOOSE(index, v1...vN); month number → FY quarter mapping; number-as-position pattern
- [[SUMIFS-COUNTIFS-Replace-IF-Helper-Columns]] — atomic — SUMIFS(sum_range, criteria) replaces IF helper column + SUM; one formula, no helper column
- [[LET-for-Deduplication]] — atomic — LET names repeated sub-expression; evaluated once; distinct framing from LET-Makes-Formulas-Readable

Author extended: Mynda Treacy (9 sources now)

New notes (source 9 of 9 — Excel File Protection Tricks):
- [[Source-Excel-File-Protection-Tricks-Mynda-Treacy]] — source
- [[Unlock-Input-Cells-Protect-Sheet-Workflow]] — workflow — Ctrl+1 → uncheck Locked → Review → Protect Sheet; guides users to input cells
- [[Locked-Hidden-Protect-Sheet]] — atomic — Locked (edit) + Hidden (formula bar) + Protect Sheet; both checkboxes must be active
- [[Protect-Sheet-vs-Protect-Workbook]] — atomic — Protect Sheet = content; Protect Workbook = structure; independent, use both
- [[Very-Hidden-Sheets-VBA-Editor]] — atomic — VBA Properties → Visible: xlSheetVeryHidden (-1→2); not in Unhide menu
- [[Document-Inspector-Remove-Personal-Information]] — workflow — File → Info → Inspect Document → Remove All; treat like spell-check for privacy
- [[Encrypt-Workbook-with-Password]] — workflow — File → Info → Encrypt with Password; no recovery if lost; password manager required
- [[Excel-Protection-Methods-Security-Comparison]] — reference — comparison table: method, what it protects, best use, true security flag

New notes (source 8 of 8 — Dynamic Drop-Down Lists):
- [[Source-Dynamic-Drop-Down-Lists-Mynda-Treacy]] — source
- [[Auto-Updating-Dropdowns-via-Excel-Table]] — atomic — table column as DV source; auto-expands on new rows; same-sheet only
- [[Named-Ranges-TOCOL-Cross-Sheet-Dropdowns]] — atomic — Define Name + TOCOL; TOCOL(...,1) ignores blanks; cross-sheet
- [[Cascading-Dropdowns-SORT-FILTER-XLOOKUP]] — pattern — SORT(FILTER) + XLOOKUP spill to DV; category → product dropdown; lookup table approach
- [[XLOOKUP-AutoFill-Related-Data-from-Dropdown]] — atomic — XLOOKUP from dropdown populates Dept, Rate etc.; interactive form
- [[FILTER-UNIQUE-SORT-Excluding-Dropdown-Items]] — atomic — FILTER excludes by condition; Status="Active" removes Discontinued; UNIQUE + SORT
- [[TOCOL-Ignore-Blanks-for-Clean-Dropdown-Lists]] — atomic — TOCOL(range, 1); scan_mode=1 + ignore_blanks=1; prevents empty entries
- [[Search-as-You-Type-in-Modern-Excel-Dropdowns]] — atomic — built-in Excel 365 UI feature; filters as user types; no formula needed

New notes (source 7 of 7 — Automated Excel Database):
- [[Source-Automated-Excel-Database-Mynda-Treacy]] — source
- [[Form-Database-Automation-Architecture]] — pattern — Form → Excel Table → Office Script → PivotTable/Chart; scalable lightweight CRM
- [[XMATCH-for-Form-Level-Duplicate-Detection]] — atomic — ISNUMBER(XMATCH(formField, table[col], 0)); warns before duplicate is saved
- [[COUNTA-UNIQUE-for-Duplicate-Warning-Banner]] — atomic — COUNTA(UNIQUE(col))<>COUNTA(col); banner shows warning when table has duplicates
- [[Data-Entry-Form-Best-Practices]] — reference — DV dropdowns, TODAY(), unlocked cells, sheet protection, tab order
- [[Office-Scripts-Form-Database-Automation]] — workflow — Record Actions → edit logic → button; ChatGPT can rewrite/optimise script

New notes (source 6 of 6 — Dynamic Excel Report 4 Formulas):
- [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy]] — source
- [[UNIQUE-SORT-Dynamic-Dropdowns]] — atomic — SORT(UNIQUE(table[column])); replaces manual copy/remove-duplicates/sort; # spill reference for DV dropdowns
- [[FILTER-Boolean-AND-OR-Logic]] — pattern — * = AND, + = OR; FILTER conditions; SUMPRODUCT-compatible
- [[Dependent-Dropdown-via-FILTER-UNIQUE-SORT]] — atomic — FILTER inside UNIQUE inside SORT; cascading dropdowns update based on parent selection
- [[GROUPBY-CHOOSECOLS-TAKE-Top-N-Summary]] — pattern — GROUPBY aggregates by key; CHOOSECOLS selects columns; TAKE limits to top N; -3 = descending by 3rd agg column
- [[SPILL-Error-Cell-in-Spill-Range]] — gotcha — #SPILL! when cell blocks spill range; fix: clear blocking cells
- [[No-Dynamic-Arrays-Inside-Formatted-Tables]] — gotcha — dynamic arrays cannot be nested inside Excel Tables; data in table, formulas outside
- [[Excel-365-Version-Requirements-Dynamic-Functions]] — atomic — FILTER=Excel 365/2021+; GROUPBY/TAKE/CHOOSECOLS=Excel 365/2024+

New notes (source 5 of 5 — Advanced CF Using Formulas):
- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
- [[Mixed-References-for-Row-Formatting]] — atomic — $H2 (col locked, row relative); evaluates each row individually
- [[ISBLANK-Double-Unary-for-Row-Validation]] — atomic — SUM(--ISBLANK(range)); double unary converts TRUE/FALSE to 1/0; SUM collapses to scalar
- [[SEARCH-for-Keyword-Detection-in-CF]] — atomic — SEARCH returns number or error; CF treats number=TRUE, error=FALSE; case-insensitive
- [[TODAY-for-Dynamic-Date-Alerts]] — atomic — TODAY() recalculates each recalc; overdue vs upcoming; priority: overdue above upcoming
- [[COUNTIF-Expanding-Range-for-Duplicates]] — atomic — COUNTIF($E$5:$E5,$E5)>1; top locked, bottom relative; expands as CF evaluates down; first occurrence excluded
- [[COUNTIFS-for-Multi-Column-Duplicates]] — atomic — COUNTIFS with two expanding ranges; composite key; exact vs partial duplicate hierarchy
- [[MOD-SUBTOTAL-for-Filter-Aware-Banding]] — atomic — SUBTOTAL(3,range) counts visible rows only; MOD alternates 0/1; banding respects filters
- [[Rule-Priority-in-CF-Manager]] — workflow — strict rules above general rules; CF stops at first match; overdue above upcoming

New notes (source 4 of 4 — 10 Custom Number Formatting Tricks):
- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
- [[Four-Section-Number-Format-Structure]] — atomic — Positive; Negative; Zero; Text — each section controls one value type
- [[Scale-Numbers-to-K-or-M]] — atomic — #,##0.00,,"M" removes 6 digits; keep scale consistent; units in header
- [[Inline-Colors-in-Number-Format]] — atomic — [Blue]/[Red] inline; replaces conditional formatting for sign-based colour
- [[Pass-Fail-via-Number-Format]] — atomic — [>=0.5]"Pass";[<0.5]"Fail"; value stays numeric; no IF formula
- [[Hide-Zero-Values-with-Format]] — atomic — empty 3rd section hides zeros; value stays numeric for formulas
- [[Symbol-Arrows-in-Number-Format]] — atomic — ▲/▼ symbols for pos/neg; Wingdings for bar charts
- [[Phone-Number-Format-Preserving-Zeroes]] — atomic — " +1 "(000) 000 0000; 0 forces leading zero; no text conversion
- [[Custom-Date-Formats]] — atomic — d/m/yy variants; underlying date serial preserved; grouping still works
- [[Inline-Units-via-Number-Format]] — atomic — 0" km"; value stays numeric; units in header preferred for large datasets
- [[Hide-All-Cell-Values-Format]] — atomic — ;;; hides all sections; not security; visible in formula bar
- [[Leading-Trailing-Characters-in-Format]] — atomic — @*_ repeats underscore to cell edge; *.@ creates dot leader

## 2026-08-03 — Health check (delta, automated)

Audit: 60 articles read (full audit — no prior health check on record).
Auto-fixed:
- writing-rules: 0 em-dash → colon fixes across 0 files
- frontmatter: 0 files backfilled with updated: 2026-08-03

Pending judgement:
- external URLs: skipped (Cloudflare timeouts on URL validation)

---
created: 2026-07-26
---

## 2026-08-02 — INDEX.md Created

**Trigger:** Complete vault health check.
**Action:** First-time INDEX.md created — all wiki notes now indexed and grouped by category.
**Also fixed:** || patch artifacts in Power BI INDEX, em-dash bullet violations (see DAX Code CHANGELOG for vault-wide stats).


# CHANGELOG

## 2026-07-27 — Ingestion batch

Sources: 1 file archived → 99.System/InboxArchive/2026-07/
Notes: 2 written
Highlights: Integrating Python into Excel — xl() and PY() functions, pandas workflow

## 2026-07-26 — Ingestion batch

Sources: 1 file archived → 99.System/InboxArchive/2026-07/
Notes: 7 written (6 extracted + 1 source)
Notes: Beyond VLOOKUP — Excel's TRUE data power. Also: Mastering Excel Copy Without Incrementing

*(No entries yet.)*
Pending judgement:
- external URLs (3 genuinely broken): microsoft-fabric-missing-piece.md — 2× malformed MS Learn URLs (fixed); world-happiness-dataset-workflow.md — GitHub raw 404 (fixed)
- external URLs (144 kanerika.com SEO scrapers): 503 from any bot — links work in browser, not from server
- external URLs (4 logo.clearbit.com): DNS fail — fictional company examples, expected broken
- external URLs (4 LinkedIn): bot-blocked (405/999) — links work in browser
- external URLs (2 packtpub.com): bot-blocked (403)
- external URLs (14 misc): ColorOracle, Ko-Fi, AppSource, Azure blog timeout, etc.