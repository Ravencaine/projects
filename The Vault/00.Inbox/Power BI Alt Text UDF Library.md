---
title: "Power BI Alt Text UDF Library"
source: "https://smart-frames.co.uk/2026/07/11/power-bi-alt-text-udf-library-release-v1-1-0/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Juls]]"
published: 2026-07-11
created: 2026-08-08
description: "I’ve just shipped v1.1.0 of the Power BI Alt Text UDF Library, and this update brings a big expansion: a brand‑new family of six accessibility‑focused DAX UDFs designed to describe common KPI visual patterns with clean, structured, screen‑reader‑friendly narratives. This update was inspired by the brilliant work shared by Alena Shkel, whose SVG‑based KPI patterns…"
Processed: "Unprocessed"
---
I’ve just shipped v1.1.0 of the Power BI Alt Text UDF Library, and this update brings a big expansion: a brand‑new family of six accessibility‑focused DAX UDFs designed to describe common KPI visual patterns with clean, structured, screen‑reader‑friendly narratives.

This update was inspired by the brilliant work shared by **Alena Shkel**, whose SVG‑based KPI patterns show just how far you can push native Power BI without custom visuals. Her post sparked the idea to bring structured, parameter‑driven alt text to the same set of patterns, but in a **generic, visual‑agnostic** way. If you haven’t checked her LinkedIn post yet, make sure you do, clicking [here.](https://www.linkedin.com/posts/alenashkel_your-power-bi-report-doesnt-need-a-custom-share-7481012143799226368-8hxc/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAbwLugBbKQgf7EaHFhJ6z5IFqrKV7kQyC4)

## What’s new

This release introduces **AltText\_VisualPatterns**, a set of parameter‑driven UDFs that generate alt text for visuals such as progress bars, bullet/target charts, trend sparklines, ratings, status indicators, and variance chips. Like *AltText\_LineChart*, these functions:

- take only parameters (context + values)
- avoid referencing internal model objects
- avoid naming chart types or colours
- follow accessible alt text best practices

## Included updates

- Added AltText\_VisualPatterns.dax containing six new UDFs: ProgressBarAltText, BulletChartAltText, SparkBarsAltText, RatingDotsAltText, StatusPillAltText, VarianceChipAltText
- Added AltText\_VisualPatterns\_Demo.dax with placeholder measures and example calls
- Updated README with a full VisualPatterns section, example outputs, and guidance for creating true DAX UDFs using FUNCTION syntax in DAX Query View or TMDL

## Functional changes

This release adds new functions only, no changes were made to existing UDFs: **AltText\_Context**, **AltText\_ChangeNarrative**, and **AltText\_LineChart** remain unchanged.

The full release is available at GitHub repository [Power BI Alt Text UDF Library](https://github.com/Juls-BI/powerbi-alttext-udfs)