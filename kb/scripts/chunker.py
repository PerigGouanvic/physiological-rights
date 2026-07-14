"""Markdown chunking.

Strategy:
1. Split the body along headings, keeping the heading path as context.
2. If a resulting section exceeds CHUNK_MAX_TOKENS, split further at
   paragraph boundaries with a small overlap.
3. If a section is below CHUNK_MIN_TOKENS, merge it forward with the next
   sibling section (unless it stands alone).

Token counts are estimated by whitespace-splitting × 1.3 — good enough for
sizing decisions; Voyage bills the real count at embed time.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from config import CHUNK_MAX_TOKENS, CHUNK_MIN_TOKENS, CHUNK_TARGET_TOKENS


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class Chunk:
    section: str
    content: str
    token_count: int = field(default=0)

    def __post_init__(self) -> None:
        if not self.token_count:
            self.token_count = estimate_tokens(self.content)


def estimate_tokens(text: str) -> int:
    return int(len(text.split()) * 1.3) + 1


def _split_by_heading(body: str) -> list[tuple[str, str]]:
    """Return list of (heading_path, section_body).

    The first tuple carries an empty heading path if the body starts before
    any heading (preamble).
    """
    matches = list(HEADING_RE.finditer(body))
    if not matches:
        return [("", body.strip())]

    sections: list[tuple[str, str]] = []
    if matches[0].start() > 0:
        preamble = body[: matches[0].start()].strip()
        if preamble:
            sections.append(("", preamble))

    stack: list[tuple[int, str]] = []
    for i, m in enumerate(matches):
        level = len(m.group(1))
        title = m.group(2).strip()

        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        path = " > ".join(t for _, t in stack)

        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        section_body = body[start:end].strip()
        sections.append((path, section_body))

    return sections


def _split_long_section(text: str, max_tokens: int, target_tokens: int) -> list[str]:
    """Split an over-long section along paragraph boundaries."""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_tokens = 0

    for para in paragraphs:
        para_tokens = estimate_tokens(para)
        if para_tokens > max_tokens:
            # Rare — a giant paragraph. Emit any pending chunk, then hard-split
            # by sentence.
            if current:
                chunks.append("\n\n".join(current))
                current, current_tokens = [], 0
            sentences = re.split(r"(?<=[.!?])\s+", para)
            buf, buf_tokens = [], 0
            for s in sentences:
                s_tokens = estimate_tokens(s)
                if buf_tokens + s_tokens > max_tokens and buf:
                    chunks.append(" ".join(buf))
                    buf, buf_tokens = [], 0
                buf.append(s)
                buf_tokens += s_tokens
            if buf:
                chunks.append(" ".join(buf))
            continue

        if current_tokens + para_tokens > target_tokens and current:
            chunks.append("\n\n".join(current))
            current, current_tokens = [], 0
        current.append(para)
        current_tokens += para_tokens

    if current:
        chunks.append("\n\n".join(current))

    return chunks


def chunk_markdown(
    body: str,
    *,
    target_tokens: int = CHUNK_TARGET_TOKENS,
    max_tokens: int = CHUNK_MAX_TOKENS,
    min_tokens: int = CHUNK_MIN_TOKENS,
) -> list[Chunk]:
    sections = _split_by_heading(body)
    raw_chunks: list[Chunk] = []

    for path, text in sections:
        if not text:
            continue
        tokens = estimate_tokens(text)
        if tokens <= max_tokens:
            raw_chunks.append(Chunk(section=path, content=text, token_count=tokens))
        else:
            for piece in _split_long_section(text, max_tokens, target_tokens):
                raw_chunks.append(Chunk(section=path, content=piece))

    # Merge tiny consecutive chunks that share a section path.
    merged: list[Chunk] = []
    for c in raw_chunks:
        if (
            merged
            and merged[-1].section == c.section
            and merged[-1].token_count < min_tokens
            and merged[-1].token_count + c.token_count <= max_tokens
        ):
            combined = merged[-1].content + "\n\n" + c.content
            merged[-1] = Chunk(section=c.section, content=combined)
        else:
            merged.append(c)

    return merged
