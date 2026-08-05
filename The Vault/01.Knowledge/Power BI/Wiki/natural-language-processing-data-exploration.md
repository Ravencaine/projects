---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [nlp, natural-language-processing, question-answering, semantic-matching]
---

# Natural Language Processing for Data Exploration

NLP maps human questions in natural language to precise data queries — enabling non-technical users to explore data through conversation.

## Definition

NLP in the context of Power BI means: when a user types a question in plain English ("Which region had the most sales last quarter?"), the system parses it, matches it to the underlying data model, and returns a visualisation — without the user needing to know DAX, SQL, or data structure.

## Key Points

- Q&A visual in Power BI uses NLP to translate free-text questions into queries
- The Q&A engine performs **semantic matching**: mapping question words to table/column names based on relationships, synonyms, and context
- Supported question types: totals, averages, rankings, comparisons, trends, filters
- The model learns from user corrections — improving accuracy over time

## The NLP Pipeline in Q&A

1. **Parse**: tokenise the question into words
2. **Entity recognition**: identify which words refer to measures, dimensions, or filters
3. **Semantic matching**: match entities to data model fields using synonyms and relationships
4. **Query generation**: produce a DAX/Power Query expression
5. **Visualisation**: render the result as a chart or table

## Related

- [[qa-visual-power-bi]]
- [[semantic-matching-qa-visual]]
- [[language-model-improves-over-time]]
