import re
from rank_bm25 import BM25Okapi
from autoresolve.context.loader import load_chunks


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


CHUNKS = load_chunks()
INDEX = BM25Okapi([tokenize(chunk) for chunk in CHUNKS])


def bm25_search(query: str, k: int = 4) -> list[str]:
    scores = INDEX.get_scores(tokenize(query))
    best = sorted(range(len(CHUNKS)), key=lambda i: scores[i], reverse=True)[:k]
    return [CHUNKS[i] for i in best]