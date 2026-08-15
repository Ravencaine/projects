---
title: "From Symptoms to Strategy: How I Built a Patient Health Monitoring Dashboard in Power BI"
source: "https://medium.com/@kudehinbusamad/from-symptoms-to-strategy-how-i-built-a-patient-health-monitoring-dashboard-in-power-bi-345a7b4fdaa2"
author:
  - "[[Abdulsamad Kudehinbu]]"
published: 2026-03-30
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
## Introduction

Healthcare data is among the most important in the world — yet it often sits in spreadsheets, disconnected from the decisions it could inform. As a Data Analyst, I wanted to explore what it looks like when patient visit records, blood test results, and symptom data are brought together in one place and made truly interactive.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7Z1VrqGRbRCPN3NuPdHEGA.jpeg)

In this article, I’ll walk you through how I built the **Patient Health Monitoring Report** — a 4-page Power BI dashboard covering 20,000 patient visits across multiple clinic locations. I’ll break down what the data looked like, how I prepared it, what the key numbers tell us, and what healthcare teams can actually do with these insights.

Whether you work in healthcare, data, or are just curious about how BI dashboards come to life — this one’s for you.

## Project Objectives

The goal of this project was to answer four core questions using patient data:

1. **Who is at risk?** — Identify the proportion of high-risk patients and understand which fever types and demographics are driving that risk.
2. **What chronic conditions are present?** — Track the burden of diabetes and hypertension across the patient population.
3. **How are patients engaging with care?** — Understand visit frequency, follow-up gaps, and care continuity patterns.
4. **What does the individual patient picture look like?** — Provide a searchable, row-level view for clinical reference and decision-making.

## About the Dataset

The dataset used for this project is a simulated but realistic collection of patient health records from multiple clinic locations in India. Here are the key details:

- **Scope:** Patient visit and clinical data from a multi-location health monitoring system
- **Timeframe:** 2024–2025
- **Records:** 20,000 patient visits across 4,887 unique patients
- **File Type:** Excel (.xlsx)
- **Structure:** 4 related tables

**Content includes:**

- Patient demographics (Age, Gender, Location)
- Symptom flags (Cough, Fatigue, Body Pain, Chills, and more)
- Fever type diagnosis (Viral, COVID, Dengue, Bacterial, Malaria, Influenza, Chikungunya, Typhoid)
- Blood pressure and diabetes readings
- Blood test results (Hemoglobin, WBC, CRP, Platelets, and more)
- Visit dates and admission status
- Fever type reference profiles and medication guides

## Data Preparation

Before building any visuals, the data needed to be cleaned and enriched in Power Query. Here is what that process involved:

**Cleaning steps:**

- Removed duplicate visit records and checked for missing Patient IDs
- Standardised text formatting across categorical columns (Gender, Fever Type, Risk Level)
- Split the combined Blood Pressure column (`BP S/D`) into two separate numeric columns — **Systolic BP** and **Diastolic BP** — to enable individual aggregations

**Calculated columns created:**

`Age Group` Grouped patient ages into bands: Child (<13), Teen (13–19), Young Adult (20–35), Adult (36–60), Senior (60+)  
`Diabetes Category` Classified patients as Diabetic or Normal based on post-meal glucose readings (threshold: 200 mg/dL)  
`BP Risk` Flagged patients as High BP or Normal based on Systolic and Diastolic thresholds  
`Hemoglobin Range` Bucketed hemoglobin values into clinical ranges (e.g. Low <12, Normal 12–14, High 14–16, Very High 16+)  
`Previous Visit Date` Calculated each patient's prior visit date to enable gap analysis  
`Visit Gap (Days)` Calculated the number of days between a patient's consecutive visits  
`Visit Category` Classified each return visit as First Visit, Regular, Moderate Gap, or Delayed Follow-Up based on the visit gap  
`Visit Type` Simplified classification of One-Time vs. Repeat patients

These columns were essential to powering the Chronic Health, Visit Analysis, and Summary Table pages of the report.

## Key Performance Indicators (KPIs)

Before diving into individual pages, here are the headline numbers from across the report:

**KPI Values**

Total Patients: 4,887

Total Visits: 20,000

High-Risk Patients: 4,058

High-Risk %: 83.04%

Diabetes Patients: 1,326 (27.13%)

High Blood Pressure Patients: 4,048 (82.83%)

Avg Systolic Blood Pressure: 130.11 mmHg

Avg Diastolic Blood Pressure: 85.18 mmHg

Repeat Patients: 4,480

Average Visit Gap: 138 days

Delayed Follow-Up %: 40.60%

These numbers alone tell a story — a patient population with a heavy chronic disease burden, significant follow-up gaps, and a very high proportion of high-risk cases.

## Key Insights

## Page 1 — Risk Overview

This page provides a bird’s-eye view of the entire patient population.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kyjRmtesJhboMUD-qvI_Tg.png)

Patient Risk Overview

- **83% of patients are classified as high risk.** This is a striking figure — it tells us that the majority of patients presenting at these clinics are not low-severity cases. Clinical triage systems need to be equipped to handle a persistently high-acuity patient load.
- **Bacterial, COVID, and Dengue cases have the highest admission rates.** These three fever types consistently required hospitalisation more than others, pointing to their severity and the resource planning implications that follow.
- **Viral fever accounts for the highest visit volume overall,** but has a much lower admission rate — it is common but manageable. Understanding this split helps clinics plan staffing versus bed capacity separately.
- **Adults (36–60) and Seniors (60+) dominate the patient population.** Younger patients (children and teens) are considerably underrepresented, suggesting that this health system primarily serves working-age and older adults.
- **Guntur and Nellore are the busiest locations** by patient count, followed by Visakhapatnam, Hyderabad, and Vijayawada. These locations should receive priority in resource and capacity planning.
- **Gender distribution is nearly even** — 50.19% Male, 49.81% Female — meaning interventions and communications should be designed to reach both groups equally.

## Page 2 — Chronic Health Monitor

This page zooms in on the two biggest chronic conditions in the dataset: hypertension and diabetes.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EeGIYVABN7n2F5_INXqIHQ.png)

Chronic Health Monitor

- **82.83% of patients have elevated blood pressure**, with an average reading of 130/85 mmHg — sitting squarely in the Stage 1 Hypertension range by clinical standards. This is not a marginal finding; it represents a systemic chronic disease burden running alongside acute fever presentations.
- **Hypertension is concentrated in the Adult and Senior age groups**, which is expected clinically, but the volume is significant enough to warrant dedicated blood pressure management pathways within these clinics.
- **27.13% of patients are diabetic.** More than 1 in 4 patients presenting for a fever-related visit also carries a diabetes diagnosis — a comorbidity that increases infection severity and recovery time.
- **COVID and Bacterial fever patients show the highest CRP levels.** CRP (C-Reactive Protein) is a blood marker for inflammation — the higher it is, the more severe the infection. This pattern confirms these two fever types are the most systemically dangerous in the dataset.
- **The majority of patients fall in the 12–14 g/dL hemoglobin range** (normal), but a notable portion fall below 12 (mild anaemia), particularly among Dengue and Malaria patients — where platelet suppression and red blood cell impact are clinically expected.
- **The WBC vs. Platelets scatter plot** reveals clear clustering by fever type, with Dengue patients showing the most dramatic platelet suppression — a key diagnostic signal that this visual makes easy to spot.

## Page 3 — Visit Analysis

This page focuses not on what is wrong with patients, but on how they engage with the healthcare system over time.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Dv-d0D9iu_9Z0rjHFmk87Q.png)

Visit Analysis

- **40.60% of all return visits are classified as delayed follow-ups.** Nearly half of the patients who come back are doing so later than they should be. For patients managing chronic conditions like hypertension or diabetes, these gaps in care can have serious consequences.
- **The average visit gap is 138 days** — roughly 4.5 months between visits. For a population where 83% are high-risk, this level of infrequency is a red flag for care continuity.
- **97.88% of visits are from repeat patients**, confirming that the clinics are primarily serving an established patient base rather than seeing a constant influx of new cases. This makes follow-up management even more critical.
- **Visit volume peaks in January through March** and declines through mid-year. This seasonal pattern likely reflects fever season dynamics — particularly for Dengue and Malaria — and should inform staffing and supply planning ahead of Q1 each year.
- **The Visit Insight alert on this page flags the high number of patients missing follow-ups** — a deliberate design choice to make this finding impossible to overlook for anyone reviewing the dashboard.

## Page 4 — Summary Table

This page shifts from aggregated insights to individual patient records.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*h3LER4pZm-Q8-k4HyFyf2A.png)

Summary Table

- The table provides a **row-level view of every patient visit**, showing Fever Type, Risk Level, Blood Pressure, Hemoglobin, CRP, WBC, Platelets, and symptom flags side by side.
- A **Patient ID search bar** at the top allows clinical staff to look up a specific patient in seconds — making this page a practical reference tool, not just an analytical one.
- The combination of lab results and symptom flags in one row gives a **complete diagnostic snapshot** that would typically require pulling from multiple systems.

## Strategic Recommendations

Based on everything the data shows, here are the most important actions healthcare teams should consider:

1. **Fix the follow-up gap first.** With 40.6% of return visits classified as delayed, implementing automated appointment reminders — via SMS or phone call — for high-risk and chronic condition patients should be the immediate priority.
2. **Build a hypertension management pathway.** 82.83% of patients with elevated BP is too high to treat as incidental. Dedicated blood pressure check-ins and medication reviews should be embedded into routine visit workflows.
3. **Plan resources around Q1 seasonality.** Visit volumes peak in January–March. Clinics — especially in Guntur and Nellore — should pre-position additional staff, diagnostics capacity, and medication stock ahead of this window.
4. **Fast-track Bacterial and COVID cases.** These two fever types consistently show the highest CRP levels and admission rates. A dedicated triage pathway for suspected bacterial or COVID presentations could reduce bottlenecks and improve outcomes.
5. **Integrate diabetes screening into fever consultations.** With 1 in 4 patients diabetic, routine blood glucose checks during fever visits would catch unmanaged cases early and reduce complication risk.
6. **Flag low hemoglobin cases in Dengue and Malaria patients** for nutritional counselling and iron supplementation before they progress to clinical anaemia.

## Conclusion

Building this dashboard reinforced something I believe strongly as an analyst: the most valuable thing data can do is make the invisible visible. Before this report, the 40% delayed follow-up rate, the 82% hypertension burden, and the seasonal visit spikes were all buried in rows of an Excel file. Now they are actionable.

If you work in healthcare data, I hope this project gives you ideas for how to structure your own monitoring reports. And if you are a non-technical reader, I hope it shows you just how much a well-designed dashboard can do to turn raw numbers into decisions that matter.

🔗 [**View the Live Power BI Dashboard**](https://app.powerbi.com/view?r=eyJrIjoiODNmZDdkN2MtZjdmYi00MmIyLTlmOTEtMWY2M2YzOTIwNjMyIiwidCI6IjgxMTQ1ZWNkLTc5NTAtNDk4Ny1hOGFmLTJhMDY1YTgwMWVhYyJ9)

🔗 [**Read the GitHub documentation**](https://github.com/Samadkudehinbu/Patient-Health-Monitoring-Report/tree/main)

👤 [**Connect with me on LinkedIn**](https://www.linkedin.com/in/abdulsamad-kudehinbu/)

🌐 [**View my Portfolio**](https://sites.google.com/view/abdulsamadportfolio/home)