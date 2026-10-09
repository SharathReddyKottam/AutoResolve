from autoresolve.context.bm25 import bm25_search
from autoresolve.context.vector import vector_search

def hybrid_search(query: str, k: int = 4) -> list[str]:
    scores = {}
    for results in (bm25_search(query, k=10), vector_search(query, k=10)):
        for rank, chunk in enumerate(results, start=1):
            scores[chunk] = scores.get(chunk, 0) + 1 / (60 + rank)
    best = sorted(scores, key=scores.get, reverse=True)[:k]
    return best