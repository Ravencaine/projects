---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: atomic
tags: [power-query, parameter, devops, environment, best-practice]
---

# Power Query Parameters: Environment Switching

Use Power Query parameters to switch between development, test, and production environments without rewriting queries.

## Definition

Power Query parameters store named values (server names, database names, file paths) that can be referenced in connection strings. When moving from dev → test → prod, you change the parameter value once instead of editing every query's source step.

## Key Points

- Create parameters via Manage Parameters → New Parameter (name + current value + type)
- Common parameters: `ServerName`, `DatabaseName`, `FilePath`
- Reference parameters in source steps using `Parameter("Name")`
- Enable "Allow Parameters" via View → options in Power Query Editor
- Change parameter values in Data Source Settings or Manage Parameters
- All queries referencing the parameter update automatically
- Type-cast parameters explicitly (text, number, etc.)
- Not needed for every report — essential when moving across environments regularly

## Example

**Create parameters:**
- `ServerName` = `localhost` (type: Text)
- `DatabaseName` = `NorthstarDev` (type: Text)

**Use in source:**
```
Source = Sql.Databases(Parameter("ServerName")){[Name=Parameter("DatabaseName")]}[Data]
```

**Advanced Editor (M):**
```
let
    Source = Sql.Databases(Parameter("ServerName")){[Name=Parameter("DatabaseName")]}[Data]
in
    Source
```

**Switch environments:**
Change parameter value to `NorthstarProd` / `ProductionServer` → all queries update.

## Related

- [[Test-Mode-Parameters-Development]] — another PQ parameter use case (row limiting)
- [[Calculate-Upstream-vs-DAX]] — when to push logic upstream vs keep in Power Query
