

## 2026-08-09 — Isabelle Bittar (KI Data Science) batch

Sources: 1 file (Modern Oblique Area Chart Native Visuals, 2025-07-23) → 99.System/InboxArchive/2026-08/
Notes: 5 written (DAX Code)
KBs: DAX Code (5 notes)
Author: Isabelle Bittar (KI Data Science) — new author

New notes (Isabelle Bittar — Oblique Area Chart):
- [[Measure-Type-Filter-Pattern]] — pattern — CALCULATE + FILTER on Measure Type text column; Average/Max/Min in one table
- [[MAXX-MINX-ALL-Date-Dynamic-Range]] — atomic — MAXX(ALL(Date), [Max Vital]) removes date filter; sees full range regardless of context
- [[Dynamic-Graph-Area-Buffer]] — pattern — Max+5% / Min-5%; buffer zone for white fill + dynamic Y-axis range
- [[VAR-for-Intermediate-Measure-Calculation]] — atomic — VAR stores intermediate result; RETURN uses it; standard DAX multi-step pattern



Sources: 3 files (Fix Incorrect Totals — Boniface Muchendu / Data Bear; From 59 Copy Pasted Measures to One Library — Fabric Community Blog / powerbiweekly, 2026-07-01; Find the products in the top 10 every year with DAX — Russo & Ferrari / SQLBI) → 99.System/InboxArchive/2026-08/
Notes: 20 written (19 DAX Code + 1 Power BI)
KBs: DAX Code (19 notes), Power BI (1 note)
- [[Fix-Incorrect-Totals-SUMX-SUMMARIZE-Pattern]] — pattern — SUMX(SUMMARIZE(... CALCULATE(MAX/MIN/AVERAGE))) for correct totals in table/matrix
- [[Totals-Wrong-Row-Context-Missing]] — atomic — total row evaluates under broader filter context; MAX/MIN/AVERAGE return global aggregate instead of sum of per-group values
- [[Fix-Incorrect-Totals-Workflow]] — workflow — Power BI visual-level steps

New notes (Fabric Community — DAX UDFs GA, 2026-07-01):
- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source — DAX UDFs (GA June 2026); 59-measure → ~20-UDF migration; typed parameters; value vs expression passing modes; TMDL version control; 5 dev entry points; compat level 1702
- [[DAX-UDFs-vs-Calculation-Groups]] — atomic — UDFs change how logic is computed; calculation groups change which measure is selected; complementary
- [[Value-vs-Expression-Parameter-Types]] — atomic — Value (NUMERIC etc.) evaluates eagerly; Expression (AnyRef, CalendarRef) passes unevaluated expression for CALCULATE control; wrong type = silent context bug
- [[DAX-UDFs-Require-Compatibility-1702]] — atomic — UDFs unavailable below compat level 1702; FUNCTION block fails silently
- [[dwp.SafeDivide]] — function — parameterized safe division; 6 copy-paste → 1 function; both NUMERIC params
- [[dwp.ABCBand]] — function — ABC classification with optional TierA/TierB defaults (0.8/0.95); named-override syntax at call site
- [[dwp.CurrencyAwareGrowth]] — function — AnyRef param + CALCULATE(MeasureExpr) gives correct context transition; NUMERIC param silently returns wrong total
- [[Measure-Library-to-UDF-Migration]] — pattern — audit → categorize params → define with defaults → document → TMDL Git → deploy
- [[DAX-UDF-Development-Environments]] — workflow — 5 entry points: DAX Query View, TMDL View, Model Explorer, XMLA/SSMS, Semantic Link Labs
- [[Five-Minute-UDF-Audit]] — workflow — count duplicate IF(DIVIDE) → SafeDivide candidates; hardcoded SWITCH thresholds → banding UDF candidates
- [[DAX-UDFs-Dont-Replace-Calculation-Groups]] — gotcha — UDFs and calculation groups solve different problems; don't make one do the other's job
- [[AnyRef-Expression-Parameter-Bug]] — gotcha — NUMERIC param for measure evaluates too early; CALCULATE has no effect; total silently wrong; fix: AnyRef + CALCULATE
- [[DAX-UDFs-Enable-AI-Copilot-Adoption]] — atomic — typed documented UDFs are the contract AI needs to use models correctly

New notes (SQLBI — Top 10 Every Year):
- [[Source-SQLBI-Top-10-Every-Year]] — source — SQLBI article
- [[Evergreen-Top-N-Products]] — atomic — evergreen products: top-N appearing in ≥Coverage% of years
- [[TopN-ProductKey-Override-Gotcha]] — gotcha — BestProds filter replaces outer ProductKey filter without KEEPFILTERS
- [[Local.ComputeForBestProds]] — function — DAX UDF: evaluates any expression only for evergreen top-N products

Extended notes:
- [[query-measure-function-workflow]] — added TopN-ProductKey-Override-Gotcha + Evergreen-Top-N-Products
- [[evergreen-top-n-products-pattern]] — added TopN-ProductKey-Override-Gotcha + Source-SQLBI-Top-10-Every-Year
- [[groupby-sumx-currentgroup-constant-count-pattern]] — added TOPN-per-group (inside GENERATE) + slicer-aware wrapping + UDF-callable sort-expression idioms
- [[generate]] — added generative semantics explanation + CALCULATETABLE+ALLSELECTED wrapping variant
- [[currentgroup]] — added SUMX(CURRENTGROUP(), 1) count-via-constant idiom + variations table
- [[Author-Marco-Russo-Alberto-Ferrari]] — added 5th source (Source-Find-Top-10-Products-Every-Year-DAX, 2025-11-03)

Errors fixed: 0 | Link ops applied: 0

## 2026-08-08 — Ingestion batch

Sources: 1 file (Analyzing the Performance Impact of Visual Calculations — SQLBI, Russo & Ferrari) — pending archive
Notes: 6 written (5 new + 1 extended) across 1 KB
KBs: DAX Code
Attachments: 5 PNGs (server timing screenshots, stored in Attachments/Visual-Calculations-Performance/)

New notes:
- [[Source-Analyzing-Visual-Calculations-Performance]] — source note
- [[PREVIOUS-YoY-VC-Pattern]] — snippet — ready-to-use PREVIOUS(COLUMNS) YoY% for visual calculations
- [[VC-Densification-Performance-Overhead]] — atomic — densification mechanism and performance numbers
- [[VC-vs-Measure-Performance-Decision]] — pattern — decision tree for VC vs measure approach
- [[VC-vs-Measure-Benchmark-Snippet]] — snippet — Contoso benchmark: VC 6s vs Measure 13s (small), VC 62s vs Measure 15.6s (large)
- [[SUMMARIZECOLUMNS-Blank-Elimination-VC-Densification]] — pattern — blank elimination vs densification interaction

Extended notes:
- [[previous-next-period]] — added PREVIOUS VC variant section (distinct from PREVIOUSDAY/PREVIOUSMONTH family)

Errors fixed: 0 | Link ops applied: 0

## 2026-08-08 — Ingestion batch

Sources: 1 file (Create calculation groups in Power BI — Microsoft Learn) — pending archive
Notes: 6 written (4 new + 2 extended) across 1 KB
KBs: DAX Code

New notes:
- [[Source-Create-Calculation-Groups-Power-BI]] — source note
- [[CG-Creation-Power-BI-Model-View]] — workflow — create CG via Power BI Desktop Model View
- [[CG-Dynamic-Format-String]] — pattern — dynamic format strings on calculation items
- [[CG-Variant-Data-Type-Gotcha]] — gotcha — variant data type side effect when CGs are added
- [[ISNUMERIC-Guard-Pattern-for-CG]] — pattern — ISNUMERIC guard for non-numeric measures in CGs
- [[SELECTEDMEASURE-Function]] — function — DAX placeholder for CG expressions

Extended notes:
- [[Calculation-Groups]] — added Gotchas section (variant type, ISNUMERIC guard, implicit measures)
- [[Create-a-Calculation-Group]] — added Power BI Desktop Model View as alternative creation path
- [[TMDL-Syntax-Calculation-Group-Properties]] — added basic CG creation TMDL syntax from MS Learn

Errors fixed: 0 | Link ops applied: 0

## 2026-08-06 — Ingestion batch (×3)

Sources: 3 files → 99.System/InboxArchive/2026-08/ (Calculation Groups in Power BI, Empty/Multiple Selection in CG, Controlling Format Strings in CG)
Notes: 13 written across 1 KB (DAX Code)
1 note extended: SELECTEDMEASURE.md
Attachments downloaded: Implementing-Calculation-Groups-Gif-1.mp4, Slicer-From-Calculation-Group.mp4
Errors fixed: 0 | Link ops applied: 0

## 2026-08-03 — Health check (delta, automated)

Audit: 10 articles read (all modified today 2026-08-03) + 5 random.
Auto-fixed:
- frontmatter: 8 files backfilled with updated: 2026-08-03

Pending judgement:
- external URLs: skipped (Cloudflare timeouts on URL validation)

---
created: 2026-07-26
---

# CHANGELOG

## 2026-08-02 — INDEX Rebuild

**Trigger:** Complete vault health check.
**Action:** Full INDEX.md rebuild — 872 notes categorized into 14 sections. Previous INDEX had ~7 entries (corrupted during prior patch attempt).
**Categories:** Conceptual Atomics (429), Context & CALCULATE (51), Date & Time (73), Math & Trig (54), Statistical (63), Text (25), Table Manipulation (39), Financial (54), Bitwise (5), Information (56), Relationships & Data Modeling (1), Debugging & Evaluation (8), Governance & Metadata (5), AI & Advanced Analytics (9).
**Also fixed:** || patch artifacts, em-dash bullet violations, 5 missing INDEX.md files (Power BI, Power Query, Excel, Data Modeling, VBA).

## 2026-07-29 — DAX for Humans (Greg Deckler, Packt 2025)

**Source:** DAX for Humans.epub — Greg Deckler, Packt Publishing, September 2025
**KB:** DAX Code
**Notes:** 64 written (1 source + 63 extracted); 21 chapters; 806K source chars; 146 DAX formulas extracted across 62 sections
**Novel content:** CALCUHATE philosophy (Banana Pattern, No CALCULATE first), 15 novel KPI patterns not in Microsoft Learn (ETR, NPS, LTV, Churn, Bradford, Kaplan-Meier, Gini, HCVA, Burndown, EVM, OTIF, OEE, MTTR/MTBF, DOS, FIFO), spatial trigonometry suite (ATAN2, Haversine, Bearing, Nearest Point, Transitive Closure), SVG star ratings, Levenshtein fuzzy matching, multi-column aggregation

**New to KB:** absenteeism, reverse-ytd, modified-dietz-return, compound-interest, market-basket-analysis, delivery-date-accuracy, fifo, order-fulfillment, cartesian-to-polar, box-size-optimization

## 2026-07-29 — Forensic Health Check

**Trigger:** User requested forensic health check — suspected prior ingestion left phantom archives.

**Finding:** dax.pdf (2026-07-26) and m-code.pdf (2026-07-27) showed as "archived" in _INGESTED.md but files were still in inbox. Registry was updated; shutil.move never ran. Also: 1,278 notes (503 dax.pdf + 775 m-code.pdf) not registered in NewNotesTracker.md; dax-source-note missing from INDEX.

**Remediated:**
- Moved dax.pdf, m-code.pdf, DAX for Humans.epub → InboxArchive/2026-07/
- Registered 503 dax.pdf notes + 775 m-code.pdf notes in NewNotesTracker.md
- Added dax-source-note + DAX Reference Functions section to DAX Code INDEX
- Frontmatter quality verified: clean across both KBs

## 2026-07-27 — Ingestion batch (25 files)

Sources: 25 files archived → 99.System/InboxArchive/2026-07/
Notes: 57 written
Highlights: TREATAS (function + comparison + dynamic segmentation), EARLIER (function + gotcha), VAR, Measure Branching, Time Intelligence (YTD + SAMEPERIODLASTYEAR vs PARALLELPERIOD), Measure Library Architecture + Naming Conventions, DAX UDF/Lambda syntax, Performance anti-patterns (5,000-measure analysis), 5 Senior Analyst Patterns (Measure Branching, Defensive DAX, Context Isolation, SSOT, Validation Loop), Dynamic Top N Ranking, Iterator Fundamentals

## 2026-07-26 — PDF extraction (dax.pdf)

Sources: 1 file archived → 99.System/InboxArchive/2026-07/
Notes: 71 written (62 extracted + 1 source + 8 subagent-written)
Notes: dax.pdf extracted via pdfplumber. 299+ DAX functions across 71 notes. Covers: aggregators, iterators, time intelligence, filters, relationships, CALCULATE, context functions, table functions, and more.

## 2026-07-26 — Ingestion batch (batch 2)

Sources: 25 files archived → 99.System/InboxArchive/2026-07/ (second session of the day)
Notes: ~30 written across multiple KBs
Notes: Mixed article ingestion — DAX, Data Modeling, Power BI, Power Query articles. Key additions include: ALL/ALLEXCEPT/ALLSELECTED/REMOVEFILTERS comparison, CALCULATE deep dive, FILTER function, Row Context vs Context Transition, Data Warehouse Architectures (Inmon/Kimball/Data Vault 2.0), Fabric Pipelines, TMDL governance, Storage Modes, Perspectives & Personalization

*(No entries yet.)*
Pending judgement:
- external URLs (3 genuinely broken): microsoft-fabric-missing-piece.md — 2× malformed MS Learn URLs (fixed); world-happiness-dataset-workflow.md — GitHub raw 404 (fixed)
- external URLs (144 kanerika.com SEO scrapers): 503 from any bot — links work in browser, not from server
- external URLs (4 logo.clearbit.com): DNS fail — fictional company examples, expected broken
- external URLs (4 LinkedIn): bot-blocked (405/999) — links work in browser
- external URLs (2 packtpub.com): bot-blocked (403)
- external URLs (14 misc): ColorOracle, Ko-Fi, AppSource, Azure blog timeout, etc.