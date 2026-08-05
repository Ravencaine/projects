---
created: 2026-08-04
source: "Analyzing Survey Comments in Power BI Using AI.md"
note_type: atomic
tags: [openai, api, cost, pricing, roi, llm, survey-enrichment, gpt-4]
related: [LLM-Survey-Enrichment-GPT4, GPT-4-Thematic-Coding]
---

# OpenAI API Cost Audit

LLM-based enrichment is not free — every prompt + completion costs money, and per-comment tagging multiplies that cost by the number of rows. The cost is small enough (Bittar's full survey run was **$2.99 USD**) that it's a rounding error vs. human tagging time, but it can balloon with corpus size.

## Definition

A simple cost-audit prompt that grounds the "use an LLM" decision in numbers:

> OpenAI API charges per **token** (prompt + completion). For `gpt-4`, pricing is roughly $0.03 / 1k prompt tokens and $0.06 / 1k completion tokens; for `gpt-4o-mini` it's about $0.15 / 1M input and $0.60 / 1M output tokens — orders of magnitude cheaper. Estimates:
>
> - **1k comments, theme extraction (single call):** ~$0.05
> - **1k comments × 2 per-comment calls:** ~$0.50
> - **Total enrichment of 1k free-text survey comments, GPT-4:** under $1
> - **10k comments, same pipeline:** roughly $5–10
> - **100k comments:** $50–100

## Key Points

- **The cost is dominated by per-comment calls, not the one-off theme extraction.** Because there are two per-comment calls (theme tag + sentiment), the per-comment cost is multiplied; the corpus-wide theme extraction call contributes a small percentage of total spend.
- **Model choice is the biggest cost lever.** `gpt-4` is several times more expensive than `gpt-4o-mini`, which is comparable in quality for short classification tasks. For survey enrichment the smaller model is often the better default; reserve `gpt-4` (or higher) for theme *induction* where inductive creativity matters.
- **Token use is the second lever.** Shorter prompts, shorter outputs (request "return only the theme name" not "explain your reasoning"), and batching reduce cost linearly.
- **Cost framing for stakeholders.** "Manual thematic coding of 500 comments takes two analysts about a week. The API runs in 5 minutes for $3. The human time is the real cost." This framing usually wins budget for the API spend.

## Examples

### Example — Bittar's actual survey run

- Corpus: an unspecified number of open-ended survey comments.
- Model: `gpt-4`.
- Pipeline: 1 theme-extraction call + N theme-tag calls + N sentiment-score calls.
- Reported cost: **$2.99 USD**, total runtime a few minutes.
- Compared against: "imagine the human time it would have taken to get something close to this result."

### Example — Scaling rule of thumb

| Comments | Approx. cost (gpt-4) | Approx. cost (gpt-4o-mini) |
| -------- | --------------------- | -------------------------- |
| 100 | < $0.10 | < $0.01 |
| 1,000 | ~$0.50 | ~$0.05 |
| 10,000 | ~$5 | ~$0.50 |
| 100,000 | ~$50 | ~$5 |

(Assume Pass 2 + Pass 3 each ~150 prompt tokens + ~20 completion tokens per comment. Actual cost depends on comment length and prompt length.)

## Notes

- **Pricing changes.** OpenAI revises pricing frequently. Always check the current rate card before quoting a number to a stakeholder.
- **Token counting is the real optimisation lever.** Tools like `tiktoken` can give exact counts per call; for a quick sizing estimate, sample 10 comments and count tokens by hand.
- **Azure OpenAI for regulated data.** The price is comparable (or marginally higher) than OpenAI direct, but you get enterprise data-handling terms. For healthcare, finance, or any PII, this matters more than the unit price.
- **Local LLMs cut cost to zero.** A 7B local model via Ollama can handle per-comment classification at quality levels adequate for many surveys. Cost is electricity + GPU time. See [[Hardware-Acer-Swift-SF14-51-Lunar-Lake]] for one such setup.
- **Don't forget the wrapper engineering.** The DAX dashboard, Power BI license, model refresh schedule, etc., have their own costs. The "$3 LLM" is only part of the total cost of ownership.

## Related

- [[LLM-Survey-Enrichment-GPT4]] — the pipeline whose cost this datum anchors
- [[GPT-4-Thematic-Coding]] — the prompt structure that controls token spend per call
