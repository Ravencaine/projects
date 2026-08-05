---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: reference
tags: [statistics, reference, normal-distribution, standard-deviation]
---

# The 68-95-99 Rule (Three Sigma Rule of Thumb)

A mnemonic for interpreting standard deviation in a normal distribution: the percentage of values that fall within 1, 2, and 3 standard deviations of the mean.

## Quick Reference

| Range | % of Values Within |
|-------|-------------------|
| μ ± 1σ (one standard deviation) | 68.27% |
| μ ± 2σ (two standard deviations) | 95.45% |
| μ ± 3σ (three standard deviations) | 99.73% |

Where μ (mu) is the arithmetic mean and σ (sigma) is the standard deviation.

## Definition

The 68-95-99 rule applies specifically to a **normal (Gaussian) distribution**: a symmetric bell curve. In any normal distribution:
- The highest point of the curve is at the mean (μ)
- The curve is symmetric around the mean
- The width of the curve is determined by the standard deviation (σ)

## Key Points

- 68.27% of all values lie between μ-1σ and μ+1σ
- 95.45% of all values lie between μ-2σ and μ+2σ
- 99.73% of all values lie between μ-3σ and μ+3σ
- This means that values beyond ±3σ (in either direction) are exceedingly rare — less than 0.3% of the population
- The margin of error for a sample is approximately `1 / √n` — doubling the sample size reduces the margin of error by a factor of √2

## Practical Examples

- **Home prices:** If median home price is $500,000 and std dev is $50,000, then ~95% of homes are priced between $400,000 and $600,000
- **Test scores:** If mean = 75 and std dev = 10, then ~95% of scores fall between 55 and 95
- **Quality control:** Manufacturing defects beyond 3σ from the mean trigger investigation

## Notes

- This rule ONLY applies to normal distributions. Skewed distributions (income data, user activity counts) do not follow this rule.
- The "Three Sigma Rule of Thumb" is a simplification — the exact percentages for 1σ, 2σ, 3σ in a true normal distribution are 68.2689%, 95.4499%, 99.7300%
- Excel's `NORM.DIST()` and `NORM.INV()` functions let you compute exact probabilities for any normal distribution

## Related

- [[descriptive-statistics-mean-median-mode-variance-stddev]] — the underlying statistics this rule interprets
- [[excel-analysis-toolpak-descriptive-statistics-histogram]] — generating the statistics in Excel
- [[scatter-chart-with-r-squared-trendline]] — R² as a complementary measure of data fit
