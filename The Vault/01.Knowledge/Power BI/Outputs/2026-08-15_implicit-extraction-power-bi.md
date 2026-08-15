---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: reference
tags: [Power BI, implicit-extraction, report]
---

# Implicit Extraction Report — Power BI

## Summary

| Category | Count |
|----------|-------|
| Entities | 21 |
| Claims | 29 |
| Relationships | 48 |
| Duplicates skipped | 1 |
| Errors | 0 |

## Written Notes

- [[Implicit/Entities/entity-jake-duddy]] — entity: Jake Duddy
- [[Implicit/Entities/entity-janvi-gupta]] — entity: Janvi Gupta
- [[Implicit/Entities/entity-juls]] — entity: Juls
- [[Implicit/Entities/entity-riccardo-perico]] — entity: Riccardo Perico
- [[Implicit/Entities/entity-plotly]] — entity: Plotly
- [[Implicit/Entities/entity-dash]] — entity: Dash
- [[Implicit/Entities/entity-gpt-4]] — entity: GPT-4
- [[Implicit/Entities/entity-openai-api]] — entity: OpenAI API
- [[Implicit/Entities/entity-pbir-power-bi-report-format]] — entity: PBIR (Power BI Report Format)
- [[Implicit/Entities/entity-visual-calculations]] — entity: Visual Calculations
- [[Implicit/Entities/entity-collapsesum-visual-calculation]] — entity: COLLAPSESUM (Visual Calculation)
- [[Implicit/Entities/entity-runningsum-visual-calculation]] — entity: RUNNINGSUM (Visual Calculation)
- [[Implicit/Entities/entity-next-visual-calculation]] — entity: NEXT (Visual Calculation)
- [[Implicit/Entities/entity-geometric-mean]] — entity: Geometric Mean
- [[Implicit/Entities/entity-arithmetic-mean]] — entity: Arithmetic Mean
- [[Implicit/Entities/entity-power-query-m]] — entity: Power Query (M)
- [[Implicit/Entities/entity-powershell]] — entity: PowerShell
- [[Implicit/Entities/entity-ai-agent]] — entity: AI Agent
- [[Implicit/Entities/entity-pbidesktop-reload-cli]] — entity: pbidesktop reload CLI
- [[Implicit/Entities/entity-chart-selection-framework]] — entity: Chart Selection Framework
- [[Implicit/Entities/entity-abc-classification-pareto]] — entity: ABC Classification (Pareto)
- [[Implicit/Claims/claim-flip-card-css3d]] — claim: CSS 3D transforms can implement flip card interactions without JavaScript
- [[Implicit/Claims/claim-flip-card-state-toggle]] — claim: Dash n_clicks can toggle flip card state with no animation logic in Python
- [[Implicit/Claims/claim-perspective-1000px]] — claim: perspective: 1000px is the standard CSS value for natural-looking 3D card rotation
- [[Implicit/Claims/claim-chart-axis-alignment-gotcha]] — claim: Stacked native Power BI visuals have independent X-axis scales and can drift apart
- [[Implicit/Claims/claim-axis-bounds-wired-to-measures]] — claim: X-axis bounds must be wired to measures rather than set manually to maintain visual alignment
- [[Implicit/Claims/claim-transparent-date-buffer]] — claim: A transparent date start buffer measure is needed to align Gantt bars with the timeline
- [[Implicit/Claims/claim-status-measure-family]] — claim: Color-by-status in Gantt charts requires one measure per status, not conditional formatting on a single measure
- [[Implicit/Claims/claim-component-first-reuse]] — claim: Component-first architecture enables dashboard reuse and per-component testing
- [[Implicit/Claims/claim-card-tuples-data-driven]] — claim: Card geometry as data tuples enables scalable dashboard maintenance without component code changes
- [[Implicit/Claims/claim-splat-callback-autoadapt]] — claim: Splat operators in Dash callbacks enable a single generic callback to handle any number of cards
- [[Implicit/Claims/claim-data-ui-separation]] — claim: Separating data from UI components makes the UI reusable and data source swappable
- [[Implicit/Claims/claim-error-band-whiteout]] — claim: Error bands can be repurposed as white-out masks to hide chart regions and enable background images
- [[Implicit/Claims/claim-error-band-not-statistical]] — claim: Using error bands as white-out masks requires explicit documentation to avoid confusion
- [[Implicit/Claims/claim-line-charts-preferred-whiteout]] — claim: Line charts are preferred over area charts for error band white-out masking
- [[Implicit/Claims/claim-two-pass-thematic-coding]] — claim: Thematic coding of survey comments requires a two-pass approach: extract themes first, then classify
- [[Implicit/Claims/claim-thematic-closed-vocabulary]] — claim: A closed theme vocabulary prevents cardinality explosion in survey tagging workflows
- [[Implicit/Claims/claim-sentiment-separate-pass]] — claim: Sentiment scoring requires a separate pass from theme tagging, using a numeric scale
- [[Implicit/Claims/claim-gantt-two-visual-stack]] — claim: A Gantt chart in Power BI can be built from two stacked native visuals without a custom visual
- [[Implicit/Claims/claim-dax-axis-bounds-adapts]] — claim: DAX measures for axis bounds adapt to slicer-selected date ranges automatically
- [[Implicit/Claims/claim-plotly-layout-mutation]] — claim: Plotly update_layout() mutates input dicts in place
- [[Implicit/Claims/claim-visual-calculations-only-see-on-visual]] — claim: Visual calculations can only reference values on the visual
- [[Implicit/Claims/claim-geometric-mean-downweights-outliers]] — claim: Geometric mean down-weights extreme outlier scores
- [[Implicit/Claims/claim-power-query-no-native-geometric-mean]] — claim: Power Query has no built-in geometric mean function
- [[Implicit/Claims/claim-pbir-enables-ai-editing]] — claim: PBIR format enables AI agents to read and edit Power BI reports
- [[Implicit/Claims/claim-ai-agent-generates-powershell]] — claim: AI agents can generate PowerShell scripts from natural-language descriptions
- [[Implicit/Claims/claim-stacked-columns-with-blank-create-threshold-bands]] — claim: Stacked columns with IF/BLANK logic create coloured threshold bands
- [[Implicit/Claims/claim-pie-donut-4-5-slice-limit]] — claim: Pie and donut charts should have at most 4-5 slices
- [[Implicit/Claims/claim-visual-calc-data-format-properties-pane]] — claim: Visual calculation data formats must be set in Properties not the format pane
- [[Implicit/Claims/claim-chart-selection-matches-goal]] — claim: Chart selection should match the analytical goal not aesthetic appeal
- [[Implicit/Edges/builds_on/component-first-dashboard-design--builds_on--data-ui-separation-principle]] — relationship: 
- [[Implicit/Edges/exemplifies/data-driven-ui-card-tuples--exemplifies--component-first-dashboard-design]] — relationship: 
- [[Implicit/Edges/exemplifies/data-driven-ui-card-tuples--exemplifies--data-ui-separation-principle]] — relationship: 
- [[Implicit/Edges/exemplifies/css-flip-card-dash--exemplifies--data-ui-separation-principle]] — relationship: 
- [[Implicit/Edges/exemplifies/css-flip-card-dash--exemplifies--component-first-dashboard-design]] — relationship: 
- [[Implicit/Edges/exemplifies/css-flip-card-dash--exemplifies--data-driven-ui-card-tuples]] — relationship: 
- [[Implicit/Edges/exemplifies/gantt-chart-native-visuals-overlay-pattern--exemplifies--chart-alignment-between-stacked-visuals-gotcha]] — relationship: 
- [[Implicit/Edges/builds_on/gantt-chart-native-visuals-overlay-pattern--builds_on--error-band-as-white-out-mask]] — relationship: 
- [[Implicit/Edges/exemplifies/gantt-chart-native-visuals-overlay-pattern--exemplifies--status-conditioned-measure-family-pattern]] — relationship: 
- [[Implicit/Edges/exemplifies/error-band-as-white-out-mask--exemplifies--oblique-area-chart]] — relationship: 
- [[Implicit/Edges/builds_on/gpt-4-thematic-coding--builds_on--llm-survey-enrichment-gpt4]] — relationship: 
- [[Implicit/Edges/builds_on/gpt-4-thematic-coding--builds_on--openai-api-cost-audit]] — relationship: 
- [[Implicit/Edges/authored_by/author-jake-duddy--authored_by--source-dynamic-data-masking-in-power-bi]] — relationship: 
- [[Implicit/Edges/authored_by/author-janvi-gupta--authored_by--first-data-source-janvi-source]] — relationship: 
- [[Implicit/Edges/authored_by/author-janvi-gupta--authored_by--first-visualizations-janvi-source]] — relationship: 
- [[Implicit/Edges/authored_by/author-juls--authored_by--source-enhancing-power-bi-reports-with-ai]] — relationship: 
- [[Implicit/Edges/authored_by/author-riccardo-perico--authored_by--source-dax-calendar-based-time-intelligence]] — relationship: 
- [[Implicit/Edges/exemplifies/abc-classification-chart-visual-calculations--exemplifies--abc-group-thresholds-stacked-columns]] — relationship: 
- [[Implicit/Edges/builds_on/abc-group-thresholds-stacked-columns--builds_on--visual-calculations-runningsum-order-by]] — relationship: 
- [[Implicit/Edges/exemplifies/geometric-mean-multi-reviewer-rankings--exemplifies--geometric-mean-power-query]] — relationship: 
- [[Implicit/Edges/builds_on/geometric-mean-multi-reviewer-rankings--builds_on--geometric-mean-power-query]] — relationship: 
- [[Implicit/Edges/contradicts/geometric-mean-multi-reviewer-rankings--contradicts--arithmetic-mean]] — relationship: 
- [[Implicit/Edges/builds_on/geometric-mean-power-query--builds_on--geometric-mean-multi-reviewer-rankings]] — relationship: 
- [[Implicit/Edges/builds_on/ai-written-powershell-scripts-design-automation--builds_on--pbir-power-bi-report-format-json]] — relationship: 
- [[Implicit/Edges/builds_on/ai-written-powershell-scripts-design-automation--builds_on--power-bi-ai-agent-cli-reload]] — relationship: 
- [[Implicit/Edges/builds_on/power-bi-ai-agent-cli-reload--builds_on--pbir-power-bi-report-format-json]] — relationship: 
- [[Implicit/Edges/builds_on/bar-column-chart-comparing-groups--builds_on--chart-selection-decision-flow]] — relationship: 
- [[Implicit/Edges/builds_on/line-chart-trend-over-time--builds_on--chart-selection-decision-flow]] — relationship: 
- [[Implicit/Edges/builds_on/pie-donut-chart-parts-whole--builds_on--chart-selection-decision-flow]] — relationship: 
- [[Implicit/Edges/exemplifies/bar-column-chart-comparing-groups--exemplifies--pie-donut-chart-parts-whole]] — relationship: 
- [[Implicit/Edges/contradicts/bar-column-chart-comparing-groups--contradicts--line-chart-trend-over-time]] — relationship: 
- [[Implicit/Edges/contradicts/bar-column-chart-comparing-groups--contradicts--scatter-plot-relationship-variables]] — relationship: 
- [[Implicit/Edges/builds_on/plotly-layout-mutation-gotcha--builds_on--chart-base-plotly]] — relationship: 
- [[Implicit/Edges/exemplifies/plotly-layout-mutation-gotcha--exemplifies--two-layer-area-line-micro-chart]] — relationship: 
- [[Implicit/Edges/exemplifies/visual-calculations-usage-guide--exemplifies--abc-classification-chart-visual-calculations]] — relationship: 
- [[Implicit/Edges/authored_by/source-geometric-mean-sqlservercentral--authored_by--geometric-mean-multi-reviewer-rankings]] — relationship: 
- [[Implicit/Edges/authored_by/source-geometric-mean-sqlservercentral--authored_by--geometric-mean-power-query]] — relationship: 
- [[Implicit/Edges/authored_by/source-abc-analysis-howtopowerbi--authored_by--abc-classification-chart-visual-calculations]] — relationship: 
- [[Implicit/Edges/authored_by/source-abc-analysis-howtopowerbi--authored_by--abc-group-thresholds-stacked-columns]] — relationship: 
- [[Implicit/Edges/authored_by/source-choosing-right-charts-selectdistinct--authored_by--chart-selection-decision-flow]] — relationship: 
- [[Implicit/Edges/authored_by/source-choosing-right-charts-selectdistinct--authored_by--bar-column-chart-comparing-groups]] — relationship: 
- [[Implicit/Edges/authored_by/source-choosing-right-charts-selectdistinct--authored_by--line-chart-trend-over-time]] — relationship: 
- [[Implicit/Edges/authored_by/source-choosing-right-charts-selectdistinct--authored_by--pie-donut-chart-parts-whole]] — relationship: 
- [[Implicit/Edges/authored_by/source-crafting-compelling-impactful-power-bi-reports--authored_by--chart-selection-decision-flow]] — relationship: 
- [[Implicit/Edges/authored_by/ai-changing-power-bi-workflow--authored_by--pbir-power-bi-report-format-json]] — relationship: 
- [[Implicit/Edges/authored_by/ai-changing-power-bi-workflow--authored_by--ai-written-powershell-scripts-design-automation]] — relationship: 
- [[Implicit/Edges/authored_by/ai-changing-power-bi-workflow--authored_by--power-bi-ai-agent-cli-reload]] — relationship: 
- [[Implicit/Edges/authored_by/building-an-interactive-flip-card-kpi-dashboard--authored_by--plotly-layout-mutation-gotcha]] — relationship: 

## Skipped Duplicates

- entity: Plotly

---
*Generated by extract-implicit-knowledge skill*
