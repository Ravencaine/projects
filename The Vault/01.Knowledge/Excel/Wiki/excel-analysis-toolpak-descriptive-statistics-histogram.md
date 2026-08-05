---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: workflow
tags: [excel, analysis-toolpak, statistics, histogram, descriptive]
---

# Excel Analysis ToolPak: Enable, Descriptive Statistics, Histogram

The Analysis ToolPak is an Excel add-in that provides statistical analysis tools — descriptive statistics, histograms, ANOVA, correlation, regression — that would otherwise require manual programming.

## Prerequisites

- Excel 2013 (or 2010/2016 with minor UI differences)
- Analysis ToolPak add-in (not loaded by default)

## Steps

### 1. Enable the Analysis ToolPak

1. File → Options → Add-Ins
2. At the bottom: Manage Excel Add-Ins → Go
3. Check **Analysis ToolPak** → OK
4. The Data Analysis button appears on the right side of the Data tab

### 2. Descriptive Statistics on Test Scores

1. Click **Data Analysis** on the Data tab
2. Select **Descriptive Statistics** → OK
3. **Input Range:** select the data cells (e.g., test scores in column A)
4. Check **Labels in first row** if column headers are included
5. **Output Range:** click a cell for the output (or New Worksheet Ply)
6. Check **Summary statistics** → OK
7. Output includes: Mean, Standard Error, Median, Mode, Standard Deviation, Sample Variance, Kurtosis, Skewness, Range, Minimum, Maximum, Sum, Count

### 3. Histogram Using Data Analysis

1. Click **Data Analysis** → select **Histogram** → OK
2. **Input Range:** select the data cells
3. **Bin Range:** (optional) select cells containing bin boundaries; if omitted, Excel creates bins automatically
4. Check **Chart Output** → OK
5. Excel places the frequency table and a histogram chart on the same worksheet

## Variations

### Histogram via Pivot Table (More Customizable)

1. Insert → Pivot Table → select data range → OK
2. Drag the numeric field (e.g., scores) to the Rows box
3. Right-click any row → Group → enter Starting at / Ending at / By values → OK
4. Drag the grouped field to Values (default: Count)
5. Insert → Column Chart → 2D Column → the histogram appears
6. Ctrl+1 on a column → Format Data Series → Gap Width = 0 (removes space between bars)

## Notes

- Descriptive Statistics output is static — use Refresh (or F9) to recalculate if data changes
- The histogram chart created by the ToolPak is a static Excel chart — to make it interactive, use the Pivot Table approach
- Analysis ToolPak tools are not available in Excel Online

## Related

- [[descriptive-statistics-mean-median-mode-variance-stddev]] — what each output statistic means
- [[dax-68-95-99-rule]] — interpreting standard deviation in context
- [[scatter-chart-with-r-squared-trendline]] — another visualization for data relationships
