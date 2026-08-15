---
title: "The Medallion Data Architecture: An Introduction"
source: "https://towardsdatascience.com/the-medallion-data-architecture/?shem=dsdf,sharefoc,agadiscoversdl,,sh/x/discover/m1/4"
author:
  - "[[Thomas Reid]]"
published: 2026-08-04
created: 2026-08-08
description: "A practical guide to Bronze, Silver and Gold, with a working Python and DuckDB example"
Processed: "Unprocessed"
---
tend to become harder to trust as they grow in scope, and they certainly become harder to run without errors, to document, and to debug.

A CSV arrives from one system, JSON comes from another, a Parquet file from somewhere else. Weeks and months go past, and before you know it, nobody is quite sure which version of the data can be trusted, which rules have been applied to it, or why an error occurred on yesterday’s dashboard.

The medallion architecture is a practical response to that problem. It divides a data platform into three layers, usually called bronze, silver, and gold. At the boundary of each layer, there should be a clear, documented description of the data contained in that layer. This is especially true of the bronze layer, as that is where initial ingestion of your data takes place, so you’ll want to write down as much information as you can about the source of data, who or which system loads it, when it was loaded, how often it’s loaded, etc.

In an ideal world, the data in each layer gets there using tools such as SQL, Python, dbt and others.

## Where did the medallion architecture come from?

The bronze, silver and gold terminology was first proposed by Databricks. Databricks is a data and AI company whose cloud platform helps organisations process, manage and analyse large datasets using technologies such as Apache Spark and Delta Lake.

Databricks describes the medallion structure as a multi-layered pattern in which data quality improves progressively as data moves through the three layers.

Typically, the bronze level is used to store raw, unfiltered data as it arrives from the source. Records are normally immutable and append-only.

Silver contains a cleaned-up version of the data in bronze. For example, null records, invalid dates, missing fields, etc., would be remedied or removed before being stored here.

Gold often contains specialised, aggregate datasets defined as SQL (materialised) views derived from Silver that align with business rules. For example, data dashboards and management reports are usually built from data in the Gold layer because the data is correct, tends to be smaller, and leads to greater accuracy and lower processing times.

Of course, systems like this have been around as long as data has. Most database engineers will have used a “staging” area to bring data into a system before farming it out to where it’s needed long before they heard the term “Medallion”. That’s a simple two-layer medallion system. Databricks just added another layer, gave it a fancy name and popularised it.

## What belongs in each layer?

Let’s have a look in slightly more detail at what each layer should ideally contain. Note that in real-life systems, the gold, silver, and bronze layers usually correspond to different schemas within a modern database or data warehouse.

### Bronze

Bronze is a record of what arrived from the source. Useful bronze data might also include ingestion metadata alongside the source fields such as

- source system and source file or event identifier
- ingestion timestamp and/or business effective date
- number of records ingested
- batch or loading run identifier

How you deal with errors and other types of data issues at this layer stage is important.

For bad and/or missing data values, these should be retained as-is and quarantined at the silver level if required. If a data load fails half-way through, because of a network failure, for example, the load should be marked as failed or superseded and re-loaded as a new batch.

If additional or late data arrives, append it as another batch and record its source, ingestion time and business-effective date.  
If the same delivery is submitted twice, use a file hash, batch identifier or source key to prevent accidental duplication.

Whatever approach is taken, ingestion should be idempotent. Processing the same source delivery more than once should not create duplicate records or otherwise change the resulting state.

### Silver

Silver applies rules to the bronze layer data set that make records dependable and accurate enough to be usable. Typical transformation work includes,

- parsing and enforcing data types
- standardising dates, currencies, country codes and units
- deduplicating records
- quarantining duff data
- joining reference data

Silver should usually retain business-level detail. It is the clean, foundational data that products and downstream systems can rely on.

Getting things wrong at this level can really screw up your downstream systems and processes. For example, a silver **order\_total** column should have a defined currency and numeric type. An **order\_id** should have a documented uniqueness rule. If a row fails those rules, the pipeline needs an explicit outcome, e.g insertion into a quarantine table, rather than a silent omission.

### Gold

Gold is organised around particular business use cases and processes. Gold typically includes:

- Summarised and aggregated data sets such as totals and counts by day, month, or region (e.g., total sales, active users).
- Star schemas or data marts built for fast queries with fewer joins.
- Tailored, separate data sets for specific teams like finance, marketing, or operations.

Tying everything together here is a diagram of what a typical, very simple, Medallion system might look like.

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/07/call_IcaBEfgHLwMqb7fHEMxxzb7z-1024x413.png)

## What tools do I need to implement a Medallion pattern?

There’s no one way to do this, but as a starter, I’d say that you usually implement a medallion architecture using some kind of database, data warehouse or cloud-based object storage where your gold, silver, and bronze layers are typically different schemas in your database or folders in your object storage. This will work on anything from SQLite on your local laptop to an AWS Redshift data lake on a huge cloud-based cluster or AWS S3/Azure Blob/Google Cloud Storage.

Specifically for cloud based object storage you’ll also need to think about the open table format that you want to use. The three most common are Hudi, Apache Iceberg and Delta tables.

In terms of the software tooling to be used, I see the medallion pattern as just another part of general data engineering (DE). So, the tools that data engineers use in their day-to-day jobs are the same ones used to set up and maintain medallion systems. SQL will be your main go-to, and remember that some other tools like dbt rely on SQL underneath the covers too. Aside from SQL, Python, Spark and other programming languages are typically used.

For cloud based architecture you might also use tools specific to that platform. I mainly use AWS, so I would probably be using AWS Athena for data querying, AWS Glue for pipeline development work and Step for orchestration.

> Note that, other than being a user of the various systems and products mentioned in this article e.g DuckDB, I have no affiliation or commercial association with any of them.

## A working example: retail orders with Python and DuckDB

For this example, I’m using the nightly CSV export from a small online retailer. The file needs some work before it can be used for reporting. Orders may be repeated, some dates fail to parse, and negative amounts need to be rejected. The pipeline runs overnight so that operations has paid and refunded sales totals, split by region and currency, by 07:00.

The pipeline has five stages:

1. Store each CSV import unchanged in the append-only Bronze table.
2. Convert the fields to the correct types, validate the values and remove duplicate orders in Silver.
3. Move rejected rows into a quarantine table for investigation.
4. Aggregate the accepted orders into daily regional sales figures in Gold.
5. Prevents the same source file from being ingested twice.

Using DuckDB as our database keeps the example small, but the layer contracts translate directly to a larger lakehouse if you need it to.

Our project layout will be similar to this.

```markdown
retail-medallion/
├── data/
│   └── incoming/
│       └── orders_2026-07-19.csv    <= manually created by you
├── pipeline.py                      <= manually created by you
└── warehouse.duckdb                 <= this DB file is created by the pipeline
```

### Create a virtual environment and install DuckDB

```powershell
D:\projects\retail-medallion> python3 -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
D:\projects\retail-medallion> python3 -m pip install duckdb pytz tabulate
```

### Creating an input file

This is just a simple CSV, so open your favourite text editor and enter the following data. Save it as a file called orders\_2026-07-19.csv under the data/incoming folder.

```markdown
order_id,ordered_at,customer_id,region,amount,currency,status
1001,2026-07-19T09:10:00Z,C001,North,125.50,GBP,paid
1002,2026-07-19T10:05:00Z,C002,South,89.99,GBP,paid
1002,2026-07-19T10:05:00Z,C002,South,89.99,GBP,paid
1003,not-a-date,C003,North,45.00,GBP,paid
1004,2026-07-19T11:42:00Z,C004,West,-10.00,GBP,paid
1005,2026-07-19T12:20:00Z,C005,North,210.00,GBP,refunded
```

The duplicate and invalid rows are deliberate and a good test to ensure our pipeline copes when data is bad.

### Our pipeline code

Save the following code to pipeline.py in the project’s home directory.

```python
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import duckdb

DATABASE = Path("warehouse.duckdb")

def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def initialise(connection: duckdb.DuckDBPyConnection) -> None:
    connection.execute("CREATE SCHEMA IF NOT EXISTS bronze")
    connection.execute("CREATE SCHEMA IF NOT EXISTS silver")
    connection.execute("CREATE SCHEMA IF NOT EXISTS gold")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS bronze.ingestion_batches (
            source_hash VARCHAR PRIMARY KEY,
            source_file VARCHAR NOT NULL,
            ingested_at TIMESTAMPTZ NOT NULL DEFAULT current_timestamp
        )
    """)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS bronze.orders_raw (
            order_id VARCHAR,
            ordered_at VARCHAR,
            customer_id VARCHAR,
            region VARCHAR,
            amount VARCHAR,
            currency VARCHAR,
            status VARCHAR,
            source_file VARCHAR NOT NULL,
            source_hash VARCHAR NOT NULL,
            ingested_at TIMESTAMPTZ NOT NULL
        )
    """)

def ingest_bronze(connection: duckdb.DuckDBPyConnection, source: Path) -> bool:
    source = source.resolve()
    digest = file_hash(source)
    already_loaded = connection.execute(
        "SELECT 1 FROM bronze.ingestion_batches WHERE source_hash = ?", [digest]
    ).fetchone()
    if already_loaded:
        print(f"Skipping {source.name}: this exact file has already been loaded")
        return False

    connection.begin()
    try:
        connection.execute(
            """
            INSERT INTO bronze.orders_raw
            SELECT
                order_id, ordered_at, customer_id, region, amount,
                currency, status, ?, ?, current_timestamp
            FROM read_csv(?, header = true, all_varchar = true)
            """,
            [source.name, digest, str(source)],
        )
        connection.execute(
            """INSERT INTO bronze.ingestion_batches (source_hash, source_file)
            VALUES (?, ?)""",
            [digest, source.name],
        )
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    print(f"Loaded {source.name} into bronze")
    return True

def build_silver(connection: duckdb.DuckDBPyConnection) -> None:
    connection.execute("""
        CREATE OR REPLACE TEMP VIEW typed_orders AS
        SELECT
            trim(order_id) AS order_id,
            try_cast(ordered_at AS TIMESTAMPTZ) AS ordered_at,
            trim(customer_id) AS customer_id,
            upper(trim(region)) AS region,
            try_cast(amount AS DECIMAL(18, 2)) AS amount,
            upper(trim(currency)) AS currency,
            lower(trim(status)) AS status,
            source_file,
            source_hash,
            ingested_at,
            row_number() OVER (
                PARTITION BY trim(order_id)
                ORDER BY ingested_at DESC, source_file DESC
            ) AS duplicate_rank
        FROM bronze.orders_raw
    """)
    valid = """
        order_id IS NOT NULL AND order_id <> ''
        AND ordered_at IS NOT NULL
        AND customer_id IS NOT NULL AND customer_id <> ''
        AND amount IS NOT NULL AND amount >= 0
        AND currency IN ('GBP', 'EUR', 'USD')
        AND status IN ('paid', 'refunded', 'cancelled')
        AND duplicate_rank = 1
    """
    connection.execute(f"""
        CREATE OR REPLACE TABLE silver.orders AS
        SELECT * EXCLUDE (duplicate_rank)
        FROM typed_orders
        WHERE {valid}
    """)
    connection.execute(f"""
        CREATE OR REPLACE TABLE silver.orders_quarantine AS
        SELECT
            * EXCLUDE (duplicate_rank),
            CASE
                WHEN duplicate_rank > 1 THEN 'duplicate order_id'
                WHEN ordered_at IS NULL THEN 'invalid ordered_at'
                WHEN amount IS NULL THEN 'invalid amount'
                WHEN amount < 0 THEN 'negative amount'
                WHEN currency NOT IN ('GBP', 'EUR', 'USD') THEN 'unsupported currency'
                WHEN status NOT IN ('paid', 'refunded', 'cancelled') THEN 'invalid status'
                ELSE 'missing required value'
            END AS rejection_reason
        FROM typed_orders
        WHERE NOT ({valid})
    """)

def build_gold(connection: duckdb.DuckDBPyConnection) -> None:
    connection.execute("""
        CREATE OR REPLACE TABLE gold.daily_sales_by_region AS
        SELECT
            cast(ordered_at AS DATE) AS order_date,
            region,
            currency,
            count(*) FILTER (WHERE status = 'paid') AS paid_orders,
            sum(amount) FILTER (WHERE status = 'paid') AS gross_sales,
            count(*) FILTER (WHERE status = 'refunded') AS refunded_orders,
            sum(amount) FILTER (WHERE status = 'refunded') AS refunded_value
        FROM silver.orders
        GROUP BY order_date, region, currency
        ORDER BY order_date, region, currency
    """)

def check_quality(connection: duckdb.DuckDBPyConnection) -> None:
    duplicate_count = connection.execute(
        "SELECT count(*) - count(DISTINCT order_id) FROM silver.orders"
    ).fetchone()[0]
    null_key_count = connection.execute(
        "SELECT count(*) FROM silver.orders WHERE order_id IS NULL"
    ).fetchone()[0]
    if duplicate_count or null_key_count:
        raise RuntimeError("Silver quality contract failed")

def print_query(connection: duckdb.DuckDBPyConnection, query: str) -> None:
    result = connection.execute(query)
    print(" | ".join(column[0] for column in result.description))
    for row in result.fetchall():
        print(" | ".join("NULL" if value is None else str(value) for value in row))

def main(source: Path) -> None:
    with duckdb.connect(str(DATABASE)) as connection:
        initialise(connection)
        ingest_bronze(connection, source)
        build_silver(connection)
        check_quality(connection)
        build_gold(connection)
        print("\nGold output")
        print_query(connection, "SELECT * FROM gold.daily_sales_by_region")
        print("\nQuarantined records")
        print_query(
            connection,
            """SELECT order_id, ordered_at, amount, rejection_reason
            FROM silver.orders_quarantine""",
        )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python pipeline.py path/to/orders.csv")
    main(Path(sys.argv[1]))
```

Run it using this command.

```powershell
python3 pipeline.py data/incoming/orders_2026-07-19.csv
```

And the output?

```markdown
Loaded orders_2026-07-19.csv into bronze

Gold output
order_date | region | currency | paid_orders | gross_sales | refunded_orders | refunded_value
2026-07-19 | NORTH  | GBP      | 1           | 125.50      | 1               | 210.00
2026-07-19 | SOUTH  | GBP      | 1           | 89.99       | 0               | NULL

Quarantined records
order_id | ordered_at                | amount | rejection_reason
1004     | 2026-07-19 12:42:00+01:00 | -10.00 | negative amount
1003     | NULL                      | 45.00  | invalid ordered_at
1002     | 2026-07-19 11:05:00+01:00 | 89.99  | duplicate order_id
```

After the run, Gold has one row for each date, region and currency, with separate figures for paid and refunded orders. Rows with bad dates, negative amounts or repeated order IDs do not make it that far. They are kept in silver.orders\_quarantine table so they can be checked.

In my example, I elected to keep things simple and disallow reloads of the same input into the bronze layer using a file hash. So, if you run the command a second time, you’ll see that the bronze ingestion part is skipped altogether because the file hash already exists. In a production system, data reloads into your bronze layer are something you’ll need to cater for too. It’s not generally as big a deal for your silver and gold layers, as these should always be reproducible from your bronze layer data, so if you get that right, everything else should fall into place.

You can inspect the medallion layers directly using code like this.

```python
import duckdb
from tabulate import tabulate

def show_table(
    connection: duckdb.DuckDBPyConnection,
    title: str,
    query: str,
) -> None:
    result = connection.execute(query)
    headers = [column[0] for column in result.description]

    print(f"\n{title}")
    print(tabulate(result.fetchall(), headers=headers, tablefmt="psql"))

with duckdb.connect("warehouse.duckdb") as connection:
    show_table(
        connection,
        "BRONZE - Raw orders",
        """
        SELECT
            order_id,
            ordered_at,
            customer_id,
            region,
            amount,
            currency,
            status,
            source_file
        FROM bronze.orders_raw
        ORDER BY order_id
        """,
    )

    show_table(
        connection,
        "SILVER - Validated orders",
        """
        SELECT
            order_id,
            ordered_at,
            customer_id,
            region,
            amount,
            currency,
            status
        FROM silver.orders
        ORDER BY order_id
        """,
    )

    show_table(
        connection,
        "SILVER - Quarantined orders",
        """
        SELECT
            order_id,
            ordered_at,
            amount,
            rejection_reason
        FROM silver.orders_quarantine
        ORDER BY order_id
        """,
    )

    show_table(
        connection,
        "GOLD - Daily sales by region",
        """
        SELECT *
        FROM gold.daily_sales_by_region
        ORDER BY order_date, region
        """,
    )
```

Which results in the following output.

```markdown
BRONZE - Raw orders
+------------+----------------------+---------------+----------+----------+------------+----------+-----------------------+
|   order_id | ordered_at           | customer_id   | region   |   amount | currency   | status   | source_file           |
|------------+----------------------+---------------+----------+----------+------------+----------+-----------------------|
|       1001 | 2026-07-19T09:10:00Z | C001          | North    |   125.5  | GBP        | paid     | orders_2026-07-19.csv |
|       1002 | 2026-07-19T10:05:00Z | C002          | South    |    89.99 | GBP        | paid     | orders_2026-07-19.csv |
|       1002 | 2026-07-19T10:05:00Z | C002          | South    |    89.99 | GBP        | paid     | orders_2026-07-19.csv |
|       1003 | not-a-date           | C003          | North    |    45    | GBP        | paid     | orders_2026-07-19.csv |
|       1004 | 2026-07-19T11:42:00Z | C004          | West     |   -10    | GBP        | paid     | orders_2026-07-19.csv |
|       1005 | 2026-07-19T12:20:00Z | C005          | North    |   210    | GBP        | refunded | orders_2026-07-19.csv |
+------------+----------------------+---------------+----------+----------+------------+----------+-----------------------+

SILVER - Validated orders
+------------+---------------------------+---------------+----------+----------+------------+----------+
|   order_id | ordered_at                | customer_id   | region   |   amount | currency   | status   |
|------------+---------------------------+---------------+----------+----------+------------+----------|
|       1001 | 2026-07-19 10:10:00+01:00 | C001          | NORTH    |   125.5  | GBP        | paid     |
|       1002 | 2026-07-19 11:05:00+01:00 | C002          | SOUTH    |    89.99 | GBP        | paid     |
|       1005 | 2026-07-19 13:20:00+01:00 | C005          | NORTH    |   210    | GBP        | refunded |
+------------+---------------------------+---------------+----------+----------+------------+----------+

SILVER - Quarantined orders
+------------+---------------------------+----------+--------------------+
|   order_id | ordered_at                |   amount | rejection_reason   |
|------------+---------------------------+----------+--------------------|
|       1002 | 2026-07-19 11:05:00+01:00 |    89.99 | duplicate order_id |
|       1003 |                           |    45    | invalid ordered_at |
|       1004 | 2026-07-19 12:42:00+01:00 |   -10    | negative amount    |
+------------+---------------------------+----------+--------------------+

GOLD - Daily sales by region
+--------------+----------+------------+---------------+---------------+-------------------+------------------+
| order_date   | region   | currency   |   paid_orders |   gross_sales |   refunded_orders |   refunded_value |
|--------------+----------+------------+---------------+---------------+-------------------+------------------|
| 2026-07-19   | NORTH    | GBP        |             1 |        125.5  |                 1 |              210 |
| 2026-07-19   | SOUTH    | GBP        |             1 |         89.99 |                 0 |                  |
+--------------+----------+------------+---------------+---------------+-------------------+------------------+
```

## Summary

As database and data engineers, we hear talk of the Medallion pattern in ETL jobs all the time, and honestly, you’ve probably already implemented at least a cut-down version of it many times. What I tried to do in this article is give you a flavour of how you might implement a practical Medallion architecture from first principles.

Don’t get me wrong. The example I showed you was very much a toy example. It used limited input data and a local database, but the principles you would need for a bigger, productionised system are in place.

For production, you will have to decide whether you want to use an enterprise-level RDBMS like Postgres or Oracle or use cloud-based object storage like AWS S3. If the latter you will have to think about what transactional table storage format to use, hudi, delta tables or iceberg. You’ll also need to consider whether you need a pipeline orchestration tool such as Airflow or Dagster.

And I’ve not even talked about the types of automated checks you would need for layer boundaries. Examples include:

- bronze row counts and source completeness
- silver key uniqueness, accepted-value checks and referential integrity
- gold reconciliation against silver totals
- freshness and volume thresholds
- alerts for quarantine rates and schema drift.

But those are just the toppings on the cake. The important point is to understand the basics of the medallion pattern and recognise how and where it can fit into your new or existing ETL pipelines.

The medallion architecture works because it makes distinctions in your data visible. Data received isn’t the same as data validated, and data validated isn’t automatically ready for a particular business decision.