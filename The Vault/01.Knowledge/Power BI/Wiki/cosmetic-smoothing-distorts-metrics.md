---
created: 2026-08-02
source: When a Line Chart Misleads (And What to Use Instead)
note_type: gotcha
tags: [powerbi, gotcha, data-visualization, line-chart, smoothing, spline, rolling-average, trendline]
---

# Cosmetic Smoothing: Splines Overshoot Real Bounds, Rolling Averages Smear Spikes

Smoothing jagged lines with splines or rolling averages introduces three systematic distortions:

1. **Overshoot:** Splines can dip below real bounds (e.g., below zero) just to maintain mathematical curvature — a physical impossibility in most real data.
2. **Spike smearing:** A one-day viral spike gets smeared across days or weeks, making a sudden event look like a gentle, prolonged hill.
3. **Lag:** Rolling averages shift the signal forward in time, making trends appear to start later than they actually do.

**When cosmetic smoothing is especially dangerous:**
- Operational metrics (server load, response times, error rates) where the exact timing of spikes matters
- Any time series where sudden changes are the signal, not the noise

**Honest alternative:** Plot raw points with a separate, clearly labeled trendline overlay. This preserves the visual truth of daily volatility while still showing long-term direction. The key is that the trendline is visually distinct from the raw data — they should never be conflated.

**Rule:** Never let smoothing hide real signal. If the spike is real, it should be visible.
