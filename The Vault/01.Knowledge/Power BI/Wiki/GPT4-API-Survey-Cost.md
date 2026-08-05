---
created: 2026-08-05
updated: 2026-08-05
source: Analyzing Survey Comments in Power BI Using AI (Isabelle Bittar)
note_type: atomic
tags: [gpt-4, api, cost, survey, roi, openai, python, budget]
---

# GPT-4 API Survey Cost

Isabelle Bittar's actual cost for processing a survey corpus via GPT-4: **$2.99 USD** for approximately 500 open-ended comments. Includes cost breakdown, factors that affect price, and ROI comparison against manual tagging.

## Actual Cost

| Metric | Value |
|--------|-------|
| Corpus size | ~500 survey comments |
| Model | GPT-4 |
| Total cost | **$2.99 USD** |
| Cost per comment | ~$0.006 |

## Cost Components

| Step | # of calls | Tokens per call (approx) | GPT-4 cost |
|------|-----------|------------------------|------------|
| Extract themes | 1 (batch) | ~5,000 input | ~$0.10 |
| Tag themes | N (one per comment) | ~50–100 input + ~10 output | ~$0.03–0.05 |
| Score sentiment | N (one per comment) | ~30–50 input + ~2 output | ~$0.01–0.03 |
| **Total** | | | **~$0.15–0.20** |

GPT-4 input tokens are the dominant cost driver. GPT-4o and newer models are significantly cheaper — swapping to `gpt-4o-mini` or `gpt-4o` could reduce cost by 10–50×.

## Factors That Affect Cost

| Factor | Impact |
|--------|--------|
| Number of comments | Linear — more comments = more per-comment API calls |
| Model choice | GPT-4o-mini ≈ 1/50th the cost of GPT-4 for comparable quality |
| Comment length | Longer comments → more tokens per call |
| Number of themes | More themes = longer prompt in tagging step |
| Batch vs sequential | Theme extraction is batched (1 call); tagging/scoring are per-comment |

## Cost vs Manual Tagging

| Approach | Cost | Time | Accuracy |
|----------|------|------|---------|
| Manual (human reader) | Labour cost | 1–2 min/comment (~8–17 hrs for 500) | Variable; fatigue degrades consistency |
| GPT-4 API | $2.99 | ~5 min for 500 (API rate) | Consistent; requires spot-check QA |
| GPT-4o-mini API | ~$0.05–0.10 | ~5 min | Similar consistency, much cheaper |

Isabelle's conclusion: $2.99 is cheap relative to the human time saved — even if the tagging needs spot-checking, the workflow is dramatically faster than fully manual processing.

## Optimisation Options

- **Switch to GPT-4o-mini**: for structured tagging/scoring tasks, the smaller model performs comparably at a fraction of the cost
- **Batch sentiment scoring**: instead of one call per comment, include 10–20 comments per prompt with a JSON structured output request (if the API supports it)
- **Cache intermediate results**: if re-running on the same corpus, cache the theme list and only re-call for new comments

## Related

- [[Python-GPT4-Survey-Enrichment-Workflow]]
- [[Analyzing-Survey-Comments-AI-Power-BI-Isabelle-Bittar-source]]
