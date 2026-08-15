"""Locked system prompt for the LLM.

This is the only prompt the LLM ever sees. It enforces:
    1. Answer ONLY from the provided context.
    2. If the context doesn't contain the answer, say so explicitly.
    3. Cite every claim with [Source: <name>, p.<page>].

Edit this file with extreme caution. Changing the prompt changes the
behaviour of the entire retrieval pipeline.
"""

from __future__ import annotations


SYSTEM_PROMPT = """You are VaultMind, a private AI knowledge assistant.

You answer questions STRICTLY from the provided context below. You must not use
any knowledge outside the context. If the context does not contain the answer,
reply with exactly:

"Based on the provided materials, I cannot find information about this."

Cite every claim inline using the exact format:
    [Source: <source_name>, p.<page>]

When multiple sources support a claim, cite each one separately. Do not
paraphrase the source name; copy it verbatim.

If the context contains conflicting information, surface the conflict and
cite both sources.

When the user asks a question that is NOT in the provided context, do not
speculate. State that the materials do not address the question and stop.
"""


CONTEXT_TEMPLATE = """CONTEXT:
---
[SOURCE: {name}, pages {page_range}]
{text}
---
[SOURCE: {name}, pages {page_range}]
{text}
---
"""

USER_PROMPT_TEMPLATE = """CONTEXT:
{context}

QUESTION: {query}

ANSWER:"""


def build_context_block(chunks: list[dict]) -> str:
    """Build the context portion of the user prompt from a list of chunks.

    Each chunk dict must have: source_name, text, and either page_start/end
    (preferred) or page_range (string fallback).
    """
    if not chunks:
        return "(no context provided)"
    parts: list[str] = []
    for c in chunks:
        name = c.get("source_name") or c.get("source_id") or "unknown"
        if "page_range" in c:
            page_range = c["page_range"]
        else:
            p_start = c.get("page_start")
            p_end = c.get("page_end")
            if p_start is None:
                page_range = "n/a"
            elif p_start == p_end:
                page_range = str(p_start)
            else:
                page_range = f"{p_start}-{p_end}"
        text = c.get("text", "")
        parts.append(
            f"[SOURCE: {name}, pages {page_range}]\n{text}"
        )
    return "\n---\n".join(parts)


def build_user_prompt(query: str, chunks: list[dict]) -> str:
    """Build the full user-message content (context + question)."""
    return USER_PROMPT_TEMPLATE.format(
        context=build_context_block(chunks),
        query=query,
    )


NO_CONTEXT_REFUSAL = (
    "Based on the provided materials, I cannot find information about this."
)