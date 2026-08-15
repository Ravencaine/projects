---
title: "From Cloning a Simple Excel report in Power BI to Building an Enterprise Data Platform: A Technical Deep Dive"
source: "https://medium.com/@dogbeykwamebright/from-cloning-a-simple-excel-report-in-power-bi-to-building-an-enterprise-data-platform-a-technical-c7775fce0cde"
author:
  - "[[Bright Dogbey]]"
published: 2025-11-12
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
How I Built a Fully Automated Data Pipeline with Live Fleet Movement Tracking Using Microsoft Fabric

D ***isclaimer****:* ***This article is a technical guide based on real-world experience building enterprise data platforms. The architecture, code examples, and implementation details shown here represent best practices and lessons learned from production systems. While inspired by actual projects, specific details have been generalized for educational purposes. Think of this as a technical blueprint you can adapt and apply to your own data engineering challenges.***

![Data Flow Diagram](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XIiYXeuKYi8-a9DtucyD2Q.png)

Data Flow Diagram

> **“We have this Excel report for tracking operations across 10 countries. Can you convert it to Power BI?”**

I remember staring at that message, already mentally mapping out the work. A straightforward Excel-to-Power BI migration. Maybe three months if we moved fast. I’d done dozens of these before.

Twelve months later, I’d built something entirely different: a fully automated data engineering platform with live fleet movement tracking on interactive maps, processing data from seven countries, serving thousands of concurrent users, with zero manual intervention required.

This is the story of how a simple dashboard request turned into a production data platform, the six months we spent doing it the wrong way, and the one weekend that changed everything.

## The Discovery Call That Changed Everything

Two days into the project, I sat down with the business team and my colleague for what I thought would be a quick requirements gathering session. What I learned in those two hours completely reshaped my understanding of what we were building.

Yes, they had Excel files stored in SharePoint. Yes, they wanted Power BI dashboards. But as we dug deeper, the real picture emerged.

The Excel files were just reference data. The real magic was supposed to happen when we integrated with their fleet tracking API, a live feed of vehicle locations, statuses, and movement patterns across multiple countries. Business users needed to see vehicles moving on maps in real-time. The operations team needed downloadable reports. And critically, the entire thing needed to run automatically because they didn’t have staff to babysit data pipelines.

“We also need this data feeding into our public website,” someone mentioned casually near the end of the meeting. “For customer access.”

I closed my laptop and looked at my notes. This wasn’t a report conversion. This was building a live tracking platform with automated data pipelines, real-time visualization, and multiple consumption endpoints.

The scope had just 10x’d.

## Six Months in the Wilderness

I did what any data engineer would do: I reached for the tools I knew. Linux VMs on Azure. Python scripts for everything. Cron jobs for scheduling. PostgreSQL for data staging. The standard playbook.

Looking back, I can see where we went wrong. But in the moment, it all made sense.

## The OAuth Nightmare

The first problem hit us immediately: SharePoint.

Business users needed to keep editing their Excel files directly in SharePoint; this was non-negotiable. Their workflows, permissions, and version control were all built around it. But connecting to SharePoint programmatically from a Linux server meant diving into Microsoft’s Graph API, OAuth 2.0 flows, and token management.

I spent three weeks building authentication logic. App registrations in Azure AD, token acquisition, token refresh handling, and rate limit management. The code worked, but it was fragile. Tokens would expire mid-process. Microsoft would throttle our requests during busy periods. Users editing files while our script ran would create file locking issues.

Every few days, I’d get a panicked message: “The pipeline failed again.” I’d SSH into the VM, check the logs, see yet another authentication error, manually rerun the script, and hope it worked this time.

## The Cron Job Blues

Our crontab grew increasingly complex:

```c
# Excel data extraction - daily at 2 AM
0 2 * * * /home/data/scripts/extract_excel.py >> /var/log/excel_extract.log 2>&1
```
```c
# Fleet API data - every 24 hours  
0 */24 * * * /home/data/scripts/fetch_fleet_data.py >> /var/log/fleet_api.log 2>&1# MySQL sync - daily at 3 AM
0 3 * * * /home/data/scripts/sync_to_mysql.py >> /var/log/mysql_sync.log 2>&1
```

Simple enough, right? Except when things went wrong.

Cron jobs fail silently. There’s no notification unless you explicitly build one. No dependency management, and if the Excel extraction failed, the MySQL sync would happily run anyway, syncing stale data. Debugging meant SSH-ing into VMs at 3 AM, scrolling through log files, trying to piece together what happened.

The worst part? Timezone handling. We had users across seven African countries in different time zones, and coordinating when pipelines should run became a constant headache.

## The Schema Drift Problem

About three months in, we hit a wall that would become our recurring nightmare.

A business user in Tanzania added three new columns to their Excel file: “Driver Name,” “Vehicle Type,” and “Fuel Level” without telling anyone. Why would they? From their perspective, they were just adding helpful information to their tracking spreadsheet.

Our Python script broke immediately:

```c
KeyError: 'Driver Name'
```

The fix required me to:

1. SSH into the production VM
2. Update the Python parsing script
3. Add the new columns to the database schema
4. Manually rerun the failed job
5. Cross my fingers that nothing else broke

This happened every few weeks. Different countries, different columns, same problem. Each time felt like playing whack-a-mole with production incidents.

## The Fleet API That Wouldn’t Cooperate

The fleet tracking API was its own special challenge. Pagination with 100 records per page across 200+ vehicles. Rate limiting at 100 requests per minute. Nested JSON structures that seemed to change format depending on the vehicle type.

Our Python script grew to over 1,500 lines, most of it error handling and retry logic:

```c
def fetch_fleet_data():
    """
    Fetch all fleet data with pagination and rate limiting.
    This function is a nightmare to maintain.
    """
    all_vehicles = []
    page = 1
    max_pages = 500  # Safety limit
    
    while page <= max_pages:
        try:
            response = requests.get(
                f"{API_URL}?page={page}&per_page=100",
                headers={"Authorization": f"Bearer {get_token()}"},
                timeout=30
            )
            
            if response.status_code == 429:  # Rate limited
                time.sleep(60)  # Wait a minute
                continue
            
            data = response.json()
            vehicles = parse_vehicle_data(data)
            all_vehicles.extend(vehicles)
            
            if not data.get('pagination', {}).get('has_next'):
                break
                
            page += 1
            time.sleep(0.6)  # Rate limiting
            
        except Exception as e:
            log_error(f"API call failed on page {page}: {str(e)}")
            # Should we retry? Skip? Die? Who knows!
            
    return all_vehicles
```

Every time the API provider changed something, we’d spend hours debugging production failures.

## The Performance Problem Nobody Saw Coming

When we finally got everything working, we hit our next wall: performance.

Power BI connected to PostgreSQL through an on-premises data gateway. Dashboard load times were 10–15 seconds. Complex queries would timeout. Users complained constantly. We tried everything: materialized views, query optimization, indexes, and connection pooling. Nothing got us below five seconds.

For a dashboard tracking live vehicle movements, five seconds felt like an eternity.

## The Maintenance Burden

By month six, I was spending 20+ hours a month just keeping the system running:

- Ubuntu security updates (with server reboots)
- PostgreSQL version upgrades
- Python dependency updates (dealing with breaking changes)
- Disk space monitoring (logs would fill up)
- SSL certificate renewals
- Firewall rule management
- Backup verification
- VM performance tuning

I wasn’t building features. I wasn’t improving the platform. I was just keeping it alive.

One Friday evening, after debugging yet another authentication failure at 11 PM, I had a moment of clarity: this was unsustainable. There had to be a better way.

## The Weekend Experiment

I’d been hearing about Microsoft Fabric but had dismissed it as “just another Microsoft product.” That Friday night, out of desperation more than curiosity, I decided to give it a shot. Just a prototype. Just to see.

## Friday Night: 30 Minutes That Shouldn’t Have Worked

I created a new Dataflow Gen2 in Fabric and selected “Get Data from SharePoint folder.” I entered the SharePoint site URL, authenticated with my work account, and selected the folder containing our Excel files.

That was it. Data started flowing.

No OAuth code. No token management. No authentication debugging. No Azure AD app registration. It just… worked.

I stared at my screen in disbelief. I’d spent *three weeks* building what Fabric had just done in five minutes.

## Saturday Morning: The API Integration

Still riding the momentum, I tackled the fleet API integration. Instead of Python, I used Fabric’s Dataflow Gen2 with Power Query M:

```c
let
    // Function to fetch API data with pagination
    GetFleetData = (pageNum as number) =>
    let
        url = "https://api.example.com/fleet?page=" & Number.ToText(pageNum) & "&per_page=100",
        response = Json.Document(Web.Contents(url, [
            Headers=[
                #"Authorization"="Bearer " & ApiToken,
                #"Content-Type"="application/json"
            ]
        ]))
    in
        response,
    
    // Get first page to determine total pages
    FirstPage = GetFleetData(1),
    TotalPages = FirstPage[pagination][total_pages],
    
    // Fetch all pages
    AllPages = List.Transform({1..TotalPages}, each GetFleetData(_)),
    AllVehicles = List.Transform(AllPages, each _[data]),
    CombinedData = List.Combine(AllVehicles),
    
    // Convert to table and expand nested records
    VehiclesTable = Table.FromList(CombinedData, Splitter.SplitByNothing()),
    ExpandedData = Table.ExpandRecordColumn(VehiclesTable, "Column1",
        {"vehicle_id", "latitude", "longitude", "status", "last_updated"})
in
    ExpandedData
```

Two hours. Pagination handled. JSON parsing done. Data loaded into the Lakehouse.

Compare that to our 1,500-line Python script that took weeks to build and constantly broke.

## Saturday Afternoon: The Database That Wasn’t

I created a Lakehouse, Fabric’s data storage layer. No database configuration. No schema setup. No connection strings. Just click “Create Lakehouse” and it provisions everything automatically: OneLake storage in Delta Lake format, a SQL analytics endpoint, and compute for transformations.

I connected Power BI Desktop to the Lakehouse via the SQL analytics endpoint. Built a simple map visual showing vehicle locations. Hit refresh.

Sub-second query performance. Out of the box. No optimization needed.

After six months of fighting with PostgreSQL and data gateways, I almost didn’t believe it.

## Sunday: The Pipeline Orchestration

The final piece: automation. Instead of cron jobs, I used Fabric’s visual pipeline designer.

I created three pipelines:

1. **Excel Migration Pipeline**: Pulls data from SharePoint, transforms it, and loads it to Lakehouse
2. **Fleet API Pipeline**: Calls the API, enriches the data, and stores it in Lakehouse
3. **MySQL Sync Pipeline**: Copies data from Lakehouse to MySQL for the web application

Each pipeline had visual scheduling and no crontab syntax to remember. Built-in error notifications. Automatic retries. Dependency management between pipelines. Comprehensive logging.

By Sunday evening, I had a complete working system:

- ✅ Excel data flowing from SharePoint
- ✅ Fleet API data integrated with full pagination
- ✅ Live maps showing vehicle locations
- ✅ Automated pipelines scheduled with dependencies
- ✅ Sub-second Power BI performance
- ✅ Zero VMs, zero Python authentication code, zero cron jobs

Total time: One weekend.

Monday morning, I showed the client team. Their response: “How fast can we rebuild everything on Fabric?”

## Building the Production System

The prototype proved the concept. Now came the real work: building a production-grade platform that could handle seven countries, thousands of users, and zero downtime tolerance.

## The Country Template Strategy

Rather than building seven separate data pipelines, I created a reusable template. Each country got the same standardized data flow, just with different parameters:

```c
let
    // Parameters that change per country
    CountryName = "Nigeria",
    CountryCode = "NG",
    FileName = "Nigeria_Operations.xlsx",
    
    // Connect to SharePoint folder
    Source = SharePoint.Files("https://[tenant].sharepoint.com/sites/FleetOps"),
    
    // Filter to this country's file
    FilteredFile = Table.SelectRows(Source, each Text.Contains([Name], FileName)),
    ExcelFile = FilteredFile{0}[Content],
    
    // Import and transform data
    ExcelWorkbook = Excel.Workbook(ExcelFile, null, true),
    DataSheet = ExcelWorkbook{[Item="Data",Kind="Sheet"]}[Data],
    Headers = Table.PromoteHeaders(DataSheet, [PromoteAllScalars=true]),
    
    // Standardize column names (handling variations across countries)
    RenamedColumns = Table.RenameColumns(Headers,{
        {"Vehicle ID", "vehicle_id"},
        {"Vehicle Number", "vehicle_id"},  // Some countries use different names
        {"Product", "product_name"},
        {"Quantity", "quantity"},
        {"Date", "operation_date"}
    }, MissingField.Ignore),
    
    // Add metadata for tracking
    AddCountryCode = Table.AddColumn(TypedColumns, "country_code", each CountryCode, type text),
    AddLoadTimestamp = Table.AddColumn(AddCountryCode, "load_timestamp", 
        each DateTime.LocalNow(), type datetime),
    
    // Quality checks: remove empty rows and duplicates
    RemoveEmptyRows = Table.SelectRows(AddSourceFile, 
        each [vehicle_id] <> null and [vehicle_id] <> ""),
    RemovedDuplicates = Table.Distinct(RemoveEmptyRows, {"vehicle_id", "operation_date"})
in
    RemovedDuplicates
```

Setting up all seven countries took about two hours. Adding a new country later? Fifteen minutes.

The template approach also meant consistency. Every country’s data followed the same schema, made the same quality checks, and had the same error handling. No more country-specific bugs.

## The Fleet Tracking Challenge

The fleet API integration was where things got interesting. We weren’t just pulling static data; we needed live vehicle positions, statuses, and movement patterns for over 200 vehicles across seven countries.

The API returned data like this:

```c
{
  "vehicles": [
    {
      "vehicle_id": "NGV-001",
      "latitude": 6.5244,
      "longitude": 3.3792,
      "status": "in_transit",
      "speed_kmh": 65,
      "heading": 87,
      "last_updated": "2024-11-12T14:30:00Z",
      "driver_id": "DRV-123",
      "route_id": "RT-LAG-ABJ-001"
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 50,
    "total_vehicles": 200
  }
}
```

I built a dataflow that fetched all pages, parsed the nested JSON, validated coordinates, flagged stale data (anything over two hours old), and joined it with the operational data from our Excel files. The result was a unified view of where every vehicle was, what it was carrying, where it was headed, and when it should arrive.

The magic happened when we connected this to Power BI’s map visuals. Suddenly, operations managers could see their entire fleet at a glance. Green dots for vehicles moving at speed. Yellow for vehicles moving slowly. Orange for recently stopped vehicles. Red for idle vehicles. Gray for stale data that needed investigation.

## The Automation Architecture

The complete system runs on three automated pipelines that execute in sequence every day:

**2:00 AM UTC: Excel Migration Pipeline** starts its run. It fetches Excel files from SharePoint for all seven countries, runs them through their country-specific dataflows, validates the data, and loads everything into the Lakehouse. Takes about 25 minutes.

**4:00 AM UTC: Fleet API Pipeline** kicks off. It calls the fleet tracking API, fetches vehicle data with pagination, enriches it with operational data from the Excel files, and stores everything in the Lakehouse. Takes about 15 minutes.

**3:00 AM UTC: MySQL Sync Pipeline** waits for both previous pipelines to complete, then springs into action. It copies all transformed data from the Lakehouse to Azure MySQL (for the web application), triggers the web app to refresh its cache, and validates that row counts match between source and destination. Takes about 10 minutes.

**5:00 AM UTC: Power BI Refresh** runs automatically. Pulls the latest data from the Lakehouse and updates all dashboard visuals. Takes about 5 minutes.

Total automated process time: roughly 55 minutes. Human intervention required: zero.

If anything fails, email alerts go out immediately. The pipeline automatically retries up to three times. Error details get logged to control tables. But in six months of production use, we’ve had only three incidents requiring human intervention, minor and resolved within 15 minutes.

## The Map Visualization That Won Hearts

The fleet tracking map became the star of the show. I spent considerable time getting it right.

The visual uses Power BI’s custom map component with vehicle locations plotted by latitude and longitude. Each vehicle is color-coded by status, sized by speed (faster vehicles show as larger dots), and includes rich tooltips with vehicle ID, country, product being transported, destination, current speed, estimated time to arrival, and data freshness.

Users can filter by country, status, or time range. The default view shows only the last 24 hours of data to keep performance snappy. There’s a drill-down to see individual vehicle details.

The first time I demoed this to the operations team, the room went silent. Then someone said, “This is exactly what we needed. We can actually see what’s happening across all our markets at once.”

That’s when I knew we’d built something special.

## The Problems We Didn’t Expect

Building the system was one thing. Keeping it running in production revealed a whole new set of challenges.

## Schema Drift Redux

Remember that schema drift problem from the traditional infrastructure days? It came back, but this time we were ready for it.

A user in Tanzania added three new columns to their Excel file without warning. Instead of breaking the entire pipeline, our dataflow handled it gracefully:

```c
// Resilient column mapping
RenamedColumns = Table.RenameColumns(Headers,{
    {"Vehicle ID", "vehicle_id"},
    {"Product", "product_name"}
}, MissingField.Ignore)  // Ignore if column doesn't exist
```
```c
// Capture unknown columns for review
KnownColumns = {"vehicle_id", "product_name", "quantity", "operation_date"},
UnknownColumns = Table.RemoveColumns(Headers, KnownColumns, MissingField.Ignore)
```

Unknown columns get logged to a separate table. An email alert goes to the data team. The dataflow continues processing with the known columns. No production failure. No panicked messages. Just a notification that says, “Hey, Tanzania added some new fields. Want to integrate them?”

## The Rate Limiting Dance

About two months in, we started getting 429 errors from the fleet API: “Too Many Requests.” The API provider was throttling us during their peak hours.

The fix was elegant: we shifted our pipeline from 10 AM UTC to 4 AM UTC, hitting their off-peak hours. We also added exponential backoff to the dataflow, and if a request fails, wait one minute and retry. If it fails again, wait five minutes. Third failure, wait fifteen minutes.

We haven’t hit a rate limit in five months.

## The Performance Optimization Journey

The fleet map initially took 60–1000 seconds to load when showing all 200+ vehicles. For a supposedly “real-time” tracking dashboard, that was unacceptable.

The solution was a two-tier approach: an overview page showing aggregated heatmaps (sub-second load time) and a detailed drill-down page showing individual vehicles (<10-second load time when needed). We also added default filters that last 24 hours only, excluded stale data, which reduced the default visible vehicles from 200+ to about 100.

Users loved it. The overview gave them the big picture instantly. The details were there when they needed them.

## The Concurrent Edit Conflict

Two users in Nigeria edited the same Excel file simultaneously. SharePoint handled it by creating a conflict copy “Nigeria\_Operations\_UserB.xlsx.” Our pipeline dutifully processed both files, creating duplicate records.

The fix was simple but important: filter out any files with “\_User” or “\_conflict” in the name, always take the most recently modified file if multiple matches exist, and deduplicate based on vehicle ID and operation date.

We also trained users on SharePoint’s co-authoring features. Edit in Excel Online instead of downloading. SharePoint handles concurrent edits properly when you work in the browser.

## The 15-Minute Country Addition

Six months into production, the business wanted to expand to Burundi, country number eight.

I walked through the process:

**Step 1** (5 minutes): Business team creates a new Excel file following the standard template, uploads it to SharePoint.

**Step 2** (5 minutes): I duplicate an existing country’s dataflow, rename it to “DF\_Excel\_Burundi,” change three parameters (country name, country code, filename), and publish.

**Step 3** (3 minutes): I open the master pipeline, add Burundi to the country list, and save.

**Step 4** (2 minutes): I open Power BI, add the new Lakehouse table to the data model, and publish.

Total time: 15 minutes. Compare that to the 2–3 days it would have taken with our old system.

The business team was stunned. “That’s it? Can we expand to new countries this quickly?”

Yes. That’s the power of building for modularity from day one.

## What We Learned

Looking back over the entire journey, six months of struggle followed by six months of smooth operation, several lessons stand out.

## Infrastructure Alignment Matters More Than Technical Purity

We spent months fighting SharePoint integration with Linux VMs and Python because that’s what “real” data engineers do. But our business users lived in SharePoint. Fighting against their workflow was like swimming upstream.

Fabric’s native SharePoint connector wasn’t technically interesting. It wasn’t something I could brag about on a resume. But it solved the actual problem effortlessly.

Choose infrastructure that aligns with your users’ workflows, not what’s trendy in tech Twitter.

## Automation Is Binary

You either automate everything or you automate nothing. Partial automation is worse than no automation because it creates the illusion of automation while still requiring human intervention.

We made automation non-negotiable: no manual data exports, no scheduled reminders to run scripts, no “remember to refresh the dashboard.” If a human had to remember to do something, it would eventually be forgotten.

This discipline meant more upfront work but zero ongoing maintenance.

## Build for Failure

Schema drift, API errors, concurrent edits, network timeouts, rate limiting, these aren’t exceptional cases; they’re normal operating conditions.

We designed for failure from day one: graceful handling of unknown columns, automatic retry logic, validation at every stage, and comprehensive error notifications. That’s why we maintain a 99.5% pipeline success rate.

Assume users will do unexpected things, APIs will go down, and data will be dirty. Build accordingly.

## Managed Platforms Free You to Build

Not managing VMs freed up 18 hours per month. Not debugging cron jobs gave us mental space to focus on what users actually needed. Not applying security patches meant we could build features instead of maintaining infrastructure.

Our competitive advantage wasn’t in server management. It was in understanding the business problem and solving it elegantly.

## The Cost Reality Check

Let’s talk money, because that matters.

A Fabric setup like this costs about $448 per month:

- Fabric F64 capacity: ~$410/month (with auto-pause enabled)
- Azure MySQL: ~$37/month
- Key Vault: ~$1/month

The traditional infrastructure approach would have cost about $2,527 per month:

- 2x Azure VMs: ~$280/month
- PostgreSQL: ~$150/month
- Storage, monitoring, networking: ~$60/month
- MySQL: ~$37/month
- Staff time for maintenance: ~$2,000/month (20 hours @ $100/hour)

Monthly savings: $2,079. Annual savings: nearly $25,000.

But the real savings isn’t the infrastructure cost. It’s the opportunity cost. Those 18 hours per month we’re not spending on maintenance? We’re using them to build new features, optimize performance, and improve the user experience.

That’s worth more than any infrastructure savings.

## When Fabric Makes Sense (And When It Doesn’t)

After six months running this in production, I can honestly assess when Fabric is the right choice.

Use Fabric when you’re already in the Microsoft ecosystem, when business users work in SharePoint or OneDrive, when you want rapid development over perfect customization, when you’re building for hundreds or thousands of dashboard users, when your team is BI-focused rather than engineering-focused, and when operational overhead needs to be minimal.

Consider alternatives when you need real-time streaming with sub-second latency, when you need specialized ML frameworks not available in Fabric’s environment, when you’re primarily on AWS or GCP, when your team prefers Kubernetes and Airflow, or when you need bare-metal control over your infrastructure.

For our use case, business users editing Excel, Power BI dashboards with maps, mixed API and file sources, thousands of users, minimal staff, Fabric was perfect.

## The Transformation

Six months ago, my colleague and I were debugging cron jobs at 3 AM, dealing with OAuth token failures, and manually rerunning failed pipelines. Users complained about slow dashboards. Adding a new country meant days of work.

Today, the system runs itself. Zero manual intervention. Seven countries (soon to be eight) are operating smoothly. Thousands of users are tracking live fleet movements on interactive maps. Sub-2-second dashboard performance. Fifteen minutes to add a new country. Two hours per month maintenance time. 99.5% pipeline reliability.

What started as “convert this Excel report to Power BI” became a fully automated fleet tracking platform because we eventually chose infrastructure that aligned with business workflows, was built for automation from day one, designed for expansion, prioritized performance, and handled failures gracefully.

The right infrastructure decision turned a six-month nightmare into a success story.

Sometimes the best technical decision is the one that gets you out of the infrastructure business entirely.

*Building a data platform? Have questions about Fabric, Power BI, or automated pipelines? Drop a comment, or reach me via* [*dogbeykwamebright@gmail.com,*](<mailto: dogbeykwamebright@gmail.com>) and *I’m happy to share more details about any part of this journey.*

*If you found this useful, follow me for more stories about data engineering in the real world, where things break, users do unexpected things, and good-enough today beats perfect never.*