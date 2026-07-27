---
created: 2026-07-27
source: "The Python Library That Reads Your Power BI Models Like Data. Most Fabric Teams Have Never Opened It."
source_url: https://medium.com/towards-artificial-intelligence/the-python-library-that-reads-your-power-bi-models-like-data-a8aa1408f2cd
note_type: source
tags: [power-bi]
---

## Semantic Link — the SemPy library — ships preinstalled in every Fabric notebook. It can list every measure in your tenant’s models, evaluate them with filters from Python, run DAX programmatically, and validate your data against the relationships your model claims to have. I’ve used it to automate work that used to consume entire client weeks. Here’s the practitioner’s tour, with the code.


Semantic Link (SemPy)

Here’s a question I ask data teams when I audit their Fabric estates: “How do you verify that the measure values in your semantic model match the source tables in your lakehouse?”

The most common answer is a version of “an analyst eyeballs the dashboard.” The second most common is silence.

It’s not negligence. Cross-checking model outputs against source data is miserable manual work — open the report, note the number, query the lakehouse, compare, repeat per measure, per filter combination. Nobody does it systematically because doing it systematically was never practical.

It’s been practical since Fabric Runtime 1.2. There’s a Python library, built by Microsoft, preinstalled in every Fabric notebook, that treats your semantic models as a programmable surface: **Semantic Link**, imported as `sempy`. In my experience it's the most underused capability in the entire Fabric stack — most teams I meet have never imported it.

A scope note before we start: I’ve written before about automating Power BI externally with Python — REST APIs, refresh orchestration, tenant scanning. That’s plumbing *around* the model. Semantic Link is different: it operates *inside* Fabric, on the model’s actual semantics — measures, relationships, DAX. Different tool, different class of problems.

## What Semantic Link Actually Is


Two Ecosystems, One Capability

Microsoft’s definition: Semantic Link connects Power BI semantic models with Synapse Data Science in Fabric. In practice it has two halves:

**The SemPy Python library** — pandas-flavored. Its core object, `FabricDataFrame`, subclasses the pandas DataFrame and carries semantic metadata: when you read from a model, the data arrives knowing its data categories, relationships, and lineage.

**A Spark native connector** — the same model access from PySpark, Spark SQL, R, and Scala, for when you’re working at Spark scale.

Setup, in its entirety: nothing. It’s built into Fabric Runtime 1.2+ and natively supported in the pure Python notebook experience. (`%pip install -U semantic-link` if you want the latest version.)

## The Five-Minute Tour

The functions that earn their keep, in roughly the order you’ll use them:

```c
import sempy.fabric as fabric

# What models can I see?
fabric.list_datasets()

# What's inside one?
fabric.list_measures("Sales Model")
# → every measure, its DAX expression, home table, format string

# Evaluate a measure — programmatically, with filters
df = fabric.evaluate_measure(
    "Sales Model",
    measure="Net Revenue",
    groupby_columns=["Geo[Region]", "Calendar[Year]"],
    filters={"Product[Category]": ["Electronics"]}
)

# Or run arbitrary DAX
df = fabric.evaluate_dax(
    "Sales Model",
    "EVALUATE SUMMARIZECOLUMNS(Geo[Region], \"Rev\", [Net Revenue])"
)

# Read a whole table with its semantics attached
df = fabric.read_table("Sales Model", "Dim_Customer")
```

If you’ve ever wanted to ask “give me this measure, by these columns, with these filters” *from code* — that’s `evaluate_measure`. No XMLA endpoint configuration, no connection strings, no exporting from a visual. The model becomes a queryable API.

## The Three Use Cases That Pay for the Learning Curve


The Three Use Cases That Pay for the Learning Curve

## 1\. Measure validation — the auditor’s power tool

This is the one that changed my audit practice. The pattern:

```c
# Model says:
model_value = fabric.evaluate_measure(
    "Sales Model", "Net Revenue",
    groupby_columns=["Calendar[Year]"]
)

# Source says (lakehouse, via your engine of choice):
source_value = spark.sql("""
    SELECT YEAR(order_date) AS yr, SUM(net_amount)
    FROM lakehouse.fact_sales GROUP BY YEAR(order_date)
""").toPandas()

# Compare. Alert on drift beyond tolerance.
```

Wrap that in a loop over `list_measures`, run it on a schedule, and you have continuous reconciliation between what your dashboards claim and what your data says. The $180K-class errors I keep writing about — the quiet ones that sit plausible-looking for 18 months — are exactly what this catches. When I described my 15-minute audit framework last year, this is what the "framework, industrialized" looks like.

## 2\. Relationship and data-quality validation

Your model *declares* relationships — one customer to many orders, keys that should join cleanly. Semantic Link can check whether the data actually honors them: documented functions explore functional dependencies and validate declared relationships against reality, and there’s an official tutorial pairing SemPy with **Great Expectations** for suite-based validation.

Orphaned foreign keys, duplicate dimension keys, relationships that silently drop rows — the stuff that produces “the totals don’t match” tickets — becomes a notebook cell instead of a forensic investigation.

## 3\. Living documentation

`list_measures`, `list_tables`, relationship listings — over every model in the workspace, dumped to a lakehouse table, on a schedule. That's a data dictionary that's never stale, diffable over time ("who changed this measure's DAX last month?"), and queryable. I described AI-generated documentation in my MCP posts; this is the deterministic, zero-hallucination version. They pair well: SemPy extracts the facts, AI writes the prose around them.

## A Worked Example: The Reconciliation Notebook

Patterns are nice; runnable shape is nicer. Here’s the skeleton of the reconciliation notebook I leave behind at client engagements — simplified, but structurally complete:

```c
import sempy.fabric as fabric
import pandas as pd
from datetime import datetime

# 1. Define the contract: measure → source-of-truth SQL
CHECKS = [
    {
        "model": "Sales Model",
        "measure": "Net Revenue",
        "groupby": ["Calendar[Year]"],
        "source_sql": """
            SELECT YEAR(order_date) AS Year,
                   SUM(net_amount)  AS expected
            FROM fact_sales
            WHERE is_test_account = 0
            GROUP BY YEAR(order_date)
        """,
        "tolerance": 0.001,   # 0.1% relative drift allowed
    },
    # ... one dict per critical measure
]

results = []
for chk in CHECKS:
    model_df = fabric.evaluate_measure(
        chk["model"], chk["measure"], groupby_columns=chk["groupby"]
    )
    source_df = spark.sql(chk["source_sql"]).toPandas()

    merged = model_df.merge(source_df, on="Year")
    merged["rel_diff"] = (
        (merged[chk["measure"]] - merged["expected"]).abs()
        / merged["expected"].abs()
    )
    worst = merged["rel_diff"].max()
    results.append({
        "run_ts": datetime.utcnow(),
        "measure": chk["measure"],
        "worst_drift": worst,
        "status": "PASS" if worst <= chk["tolerance"] else "FAIL",
    })

# 2. Land results in the lakehouse — history is the point
spark.createDataFrame(pd.DataFrame(results)) \
     .write.mode("append").saveAsTable("audit.measure_reconciliation")
```

Three design choices worth copying even if you rewrite everything else:

**The contract is data, not code.** Adding a measure to the nightly check means appending a dict, not writing logic. In practice this is what determines whether the team keeps the habit after you leave.

**Tolerance is explicit.** Floating-point arithmetic and timing differences mean zero-drift is the wrong bar; an agreed tolerance per measure turns “the numbers are slightly off” arguments into configuration.

**Results append to a table.** The first FAIL is useful. The *history* is gold — “this measure started drifting on March 4th” turns a forensic investigation into a `WHERE` clause, and pairs beautifully with "what changed in the model that week?" (which `list_measures` snapshots, from the documentation pattern above, will answer).

At one client this notebook’s third nightly run caught a 0.7% revenue drift introduced by a “harmless” Power Query change. The fix took an hour. Finding it the old way — at quarter close, via an auditor — is the counterfactual I invoice against.

## SemPy vs. Semantic-Link-Labs

One distinction worth knowing before you go exploring, because you’ll hit both names:

- `**sempy**` (package `semantic-link`) is the official core library — preinstalled, documented on Microsoft Learn, stable.
- `**semantic-link-labs**` (`%pip install semantic-link-labs`, `import sempy_labs`) is Microsoft's open-source companion on GitHub — "early access to new features," maintained by the Fabric CAT team. It adds the admin-flavored tooling: running Best Practice Analyzer programmatically, model migration helpers, bulk operations.

My rule: production validation pipelines on `sempy` core; exploratory and admin tooling from labs, version-pinned, with the understanding that it's a fast-moving open-source project rather than a serviced product.

## What It Won’t Do

Honest scope limits, before you over-promise to your team:

- **Fabric only.** This is a Fabric notebook capability. No Fabric, no SemPy.
- **It’s not a modeling tool.** Reading, evaluating, validating — yes. Restructuring models conversationally is the Power BI Modeling MCP’s job (different post, different tool).
- **Read paths are the mature paths.** Write scenarios exist (and labs pushes further), but the dependable production patterns today are read-and-validate.
- **Capacity isn’t free.** Notebook executions consume CUs like any other workload. A tenant-wide measure-validation sweep is real compute — schedule it like the batch job it is, and watch the Capacity Metrics app the first few runs.

## Practitioner Verdict


Practitioner Verdict


That last row is my actual theory for why adoption is so low. Semantic Link lives exactly on the seam between the Power BI developer (who owns the models but doesn’t open notebooks) and the data engineer (who lives in notebooks but treats semantic models as someone else’s deliverable). It belongs to whoever claims the seam.

Claim it. The first afternoon you spend looping `evaluate_measure` over your estate's critical measures and comparing them to source will either confirm your numbers are right — worth knowing — or find the discrepancy that's been quietly compounding for a year. I've seen both outcomes. The second one pays for a lot of afternoons.

*Have you put Semantic Link to work — validation, documentation, something I haven’t thought of? Drop your use case in the comments; the interesting ones become follow-up posts.*

> See also [[reports-semantic-models-power-bi-service]] for reference.
