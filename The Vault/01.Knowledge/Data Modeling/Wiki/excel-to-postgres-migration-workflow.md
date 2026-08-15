---
created: 2026-08-09
updated: 2026-08-09
source: "Excel was my database for 15 years, and Postgres ended that in a weekend.md"
note_type: workflow
tags: [postgres, migration, excel, pandas, psycopg2, docker, workflow]
---

# Excel to Postgres Migration Workflow

**Type:** Workflow · **KB:** Data Modeling · **Source:** [[source-excel-postgres-weekend-yadullah]]

Migrate from Excel-as-database to PostgreSQL in one weekend. Steps: design schema, containerize Postgres, write Python migration script, validate with constraints.

## Step 1 — Sketch the schema

Before touching code:

1. Identify the main entities (customers, orders, payments)
2. Define relationships between entities
3. Define constraints per column (UNIQUE, NOT NULL, FK, type)
4. This sketch exposes data quality problems before scripting

This is the most important step — see [[database-schema-first-migration]].

## Step 2 — Spin up Postgres in Docker

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

```bash
docker compose up -d
```

Named volume ensures data persists across container restarts. Running in under 10 minutes.

## Step 3 — Write the migration script

```python
import pandas as pd
import psycopg2

# Read and clean
df = pd.read_excel("source.xlsx")
df["email"] = df["email"].str.strip()  # normalize

# Insert with constraint enforcement
conn = psycopg2.connect(database="mydb", user="user", password="password")
cur = conn.cursor()
for _, row in df.iterrows():
    try:
        cur.execute(
            "INSERT INTO customers (name, email) VALUES (%s, %s)",
            (row["name"], row["email"])
        )
    except psycopg2.IntegrityError as e:
        print(f"Rejected: {row['email']} — {e}")
conn.commit()
```

## Step 4 — Let constraints catch bad data

Postgres constraints reject:
- Duplicate email addresses (UNIQUE)
- Orders with non-existent customer FK (FOREIGN KEY)
- Amount fields with text values (type constraint)
- Missing required fields (NOT NULL)

See [[postgres-constraint-enforcement]] and [[constraints-catch-bad-data-not-bad-formatting]].

## Step 5 — Connect AI/LLM to Postgres

Local LLMs and Claude can query the same Postgres database, enabling natural-language data retrieval without writing SQL manually.

## Related

- [[database-schema-first-migration]] — Step 1 in detail
- [[postgres-constraint-enforcement]] — what constraints catch
- [[normalized-tables-vs-flat-rows]] — why schema design matters
