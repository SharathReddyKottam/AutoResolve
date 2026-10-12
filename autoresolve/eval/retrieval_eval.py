from autoresolve.context.hybrid import hybrid_search
from autoresolve.eval.golden import GOLDEN

def first_correct_rank(results, runbook):
    for rank, chunk in enumerate(results, start=1):
        if chunk.startswith(runbook):
            return rank
    return None

def evaluate(k: int = 4):
    hits = 0
    reciprocal_ranks = []
    for item in GOLDEN:
        results = hybrid_search(item["ticket"], k=k)
        rank = first_correct_rank(results, item["runbook"])
        if rank is not None:
            hits += 1
            reciprocal_ranks.append(1 / rank)
        else:
            reciprocal_ranks.append(0)
        print(rank, item["ticket"])
    print(f"Recall@{k}: {hits / len(GOLDEN):.2f}")
    print(f"MRR: {sum(reciprocal_ranks) / len(GOLDEN):.2f}")