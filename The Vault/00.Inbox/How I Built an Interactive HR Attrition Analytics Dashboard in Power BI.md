---
title: "How I Built an Interactive HR Attrition Analytics Dashboard in Power BI"
source: "https://medium.com/@kudehinbusamad/how-i-built-an-interactive-hr-attrition-analytics-dashboard-in-power-bi-13eaa10b4ad7"
author:
  - "[[Abdulsamad Kudehinbu]]"
published: 2026-07-13
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KbRihImRkvkNII2YWl-rZQ.jpeg)

## Introduction

Every HR leader has been there — staring at a spreadsheet trying to figure out why good people are leaving, whether hiring is keeping pace with demand, and where workforce levels have drifted dangerously far from plan. The data exists, but it’s scattered across systems, disconnected, and impossible to act on quickly.

For the ZoomCharts 4U Report Challenge (July 2026), I built Workforce Compass — an interactive Power BI report that transforms raw HR data into decision-ready insights. Using 9 ZoomCharts Drill Down visuals across 3 pages, the report helps stakeholders explore workforce growth, identify attrition hotspots, understand why employees leave, and see where workforce reality diverges from organizational targets.

## Project Objectives

This report was designed to answer six critical workforce questions:

- How has headcount and FTE changed over time?
- Which departments, locations, or roles show the highest attrition?
- What are the main termination reasons, and how do voluntary and involuntary exits differ?
- How do engagement, performance, absence, and tenure relate to retention?
- Where are actual workforce levels above or below planned targets?
- How effectively is recruitment supporting workforce needs?

## About the Dataset

The dataset provided is a comprehensive collection of HR workforce planning data spanning 2023 to 2025. It includes information on employee profiles, monthly headcount snapshots, hiring and termination events, compensation, performance reviews, engagement surveys, absences, recruitment activity, and workforce targets. Below are the key details about the dataset:

Scope: HR workforce planning data from a multi-department organization

Timeframe: Covers workforce activity from 2023 to 2025

Content: Includes detailed information on:

- Employee demographics and employment status
- Monthly headcount and FTE snapshots
- Hiring and termination events with reasons
- Compensation and performance records
- Engagement surveys and absence tracking
- Recruitment pipeline metrics
- Workforce planning targets

Structure: 12 tables (4 dimensions, 8 facts) in a Snowflake Schema

Records: Spanning multiple departments, locations, and roles

## Data Preparation

Data preparation was completed using Power Query and DAX. Key steps included:

- Standardizing DepartmentID and LocationID formats across all tables to ensure relationship integrity
- Trimming and cleaning ID columns to remove hidden characters that could break joins
- Creating a Date Hierarchy (Year → Quarter → Month) in DimDate for drill-down functionality
- Ensuring MonthName sorts chronologically using MonthNumber as the sort-by column
- Handling BLANK values in termination measures using COALESCE to prevent visual errors
- Setting up DimDate as the official date table and disabling auto date/time intelligence

## Data Modelling

The data model follows a Snowflake Schema with 15 active relationships across 12 tables. DimEmployee sits at the center as the hub — connecting to 5 fact tables (FactEmployeeEvents, FactCompensation, FactPerformance, FactEngagement, FactAbsence) and 2 dimension tables (DimDepartment, DimLocation).

Conformed dimensions (DimDate, DimDepartment, DimLocation) are shared across multiple fact tables, enabling cross-functional analysis like correlating engagement against attrition or comparing actual headcount to planned targets.

All relationships use Single cross-filter direction (1 → Many) to ensure predictable filter flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mbeV_BkFbpOYuzok7iuPGw.png)

Semantic Model

## Key Performance Indicators (KPIs)

The report tracks 40 DAX measures organized across 6 display folders:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*gj1q2-v5sIPs0sfUkICUnQ.png)

Each KPI card includes a dynamic reference label — a contextual insight that updates with slicer selections (e.g., “72% of exits were voluntary” or “1,024 positions below plan”).

## Key Insights

## Page 1 — Executive Overview

“How has our workforce grown, and are we on track with our targets?”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RfoLjOSuz175lYernzQiRw.png)

Executive Overview

- **Workforce Distribution:** Headcount distribution across Department → Location → Level reveals where the workforce concentrates. Drilling into Engineering, for example, shows how headcount splits across office locations and seniority levels — critical for capacity planning.
- **Workforce Growth vs Plan:** The dual-line comparison of actual vs planned headcount over time exposes where the organization consistently falls short of hiring targets. Drilling from year to quarter to month pinpoints exactly when gaps widened.
- **Headcount Gap Analysis:** Conditional formatting instantly flags understaffed departments in red and overstaffed in green. The largest negative variances signal departments where attrition is outpacing recruitment.
- **Workforce Status Overview:** The active vs terminated split provides a quick health check on overall workforce stability.
- **Recruitment Pipeline**: Comparing open vs filled requisitions by department reveals where hiring is struggling to keep up. Departments with large headcount gaps AND low fill rates are in a double bind.

## Page 2 — Attrition & Retention Deep Dive

“Which employee segments show the highest attrition, and what’s driving them to leave?”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9lzxNuEKYMf3p7h37hvPsg.png)

Attrition and Retention Deep Dive

- **Termination Breakdown by Type & Reason**: Starting with the voluntary vs involuntary split, drilling into specific reasons (resignation, career growth, performance, restructuring) reveals *why* people leave — and whether the organization has a retention problem or a management decision pattern.
- **Attrition by Department, Location & Role:** This is where attrition hotspots get specific. A department might have an acceptable overall rate, but drilling into a specific location or role within it might reveal a concentrated problem that the average hides.
- **Engagement vs Attrition Correlation:** Plotting engagement scores against attrition rates across departments reveals whether low engagement is a leading indicator of turnover. Departments in the high-attrition / low-engagement quadrant are the most urgent retention intervention targets.
- **Voluntary vs Involuntary Terminations Over Time**: Tracking how the mix of exit types shifts across quarters and months reveals whether organizational changes (restructuring, policy shifts) are driving involuntary spikes or whether voluntary exits are trending upward — a retention warning sign.
- **Absence Days by Department & Type**: High absence levels, particularly in categories like sick leave, often precede voluntary resignations. This visual surfaces absence patterns as an early warning system for retention risk.

## Page 3 — Employee Details (Drill-Through)

“Who are the employees behind the numbers, and what do their individual profiles tell us?”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*g0gQ2KkbIJ9vboCSRBhE-Q.png)

- **Employee Profile Overview Table:** A full employee-level view with conditional formatting on engagement scores (red/amber/green) that lets leaders see exactly who is at risk — low engagement, high absence, short tenure employees stand out immediately.
- **Recruitment Activity by Department & Month:** Drilling into hiring activity for the selected segment shows whether recruitment is aligned with where the workforce gaps actually exist.
- **Performance Ratings by Department & Level:** Comparing performance across roles and seniority levels reveals whether attrition is concentrated among high or low performers — a critical distinction for retention strategy.

## Strategic Recommendations

1. **Prioritize retention in high-attrition departments** — Use the Engagement vs Attrition scatter plot to identify departments where low engagement correlates with high turnover, then invest in targeted engagement initiatives rather than relying solely on recruitment.
2. **Close the headcount-to-target gap systematically —** For departments with large negative variances, drill through to Page 3 to examine whether recruitment is aligned with the specific roles and locations where gaps exist.
3. **Address voluntary exit drivers proactively —** The termination reason drill-down reveals specific drivers. Design interventions based on the top reasons (career growth programs, compensation reviews, management training) rather than generic retention efforts.
4. **Use engagement as a leading indicator —** If the scatter plot confirms an engagement-attrition correlation, treat survey scores as an early warning system and intervene before attrition spikes.
5. **Align recruitment with workforce gaps —** Departments with high open requisitions AND high negative headcount variance need a recruitment strategy review — faster processes, broader sourcing, or adjusted requirements.
6. **Monitor absence as a retention risk signal —** Rising absence, especially sick leave, often precedes voluntary exits. Track it alongside attrition data to catch at-risk employees before they leave.

## Conclusion

This project proves that attrition is not a uniform problem — it concentrates in specific departments, locations, and roles, driven by distinct factors that vary by segment. This report transforms scattered HR data into a clear, interactive narrative: where workforce gaps exist, why people are leaving, whether engagement signals future risk, and whether recruitment is closing the gap fast enough. Instead of asking “Are we losing people?”, HR leaders can now ask “Why are we losing them, and what can we do about it before it impacts the business?”

🔗 [View Live Dashboard](https://app.powerbi.com/view?r=eyJrIjoiY2I4M2I5ZjQtYThiYy00OTE5LWEyMjgtYmQ5NTliOGZhYTEyIiwidCI6IjQ2NTRiNmYxLTBlNDctNDU3OS1hOGExLTAyZmU5ZDk0M2M3YiIsImMiOjl9) | 🔗 [GitHub Repository](https://github.com/Samadkudehinbu/HR-Workforce-Planning-Attrition-Report) | 🌐 [View My Portfolio](https://sites.google.com/view/abdulsamadportfolio/home) 👤 [Connect on LinkedIn](https://www.linkedin.com/in/abdulsamad-kudehinbu/) | 🌐 [View My Portfolio](https://sites.google.com/view/abdulsamadportfolio/home)