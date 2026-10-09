from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from autoresolve.config import config
from autoresolve.context.loader import load_chunks

CHUNKS = load_chunks()

_embeddings = HuggingFaceEmbeddings(model_name=config["embeddings"]["model"])
_store = Chroma.from_texts(
    CHUNKS,
    _embeddings,
    collection_name=config["chromadb"]["collection_name"],
)


def vector_search(query: str, k: int = 4) -> list[str]:
    docs = _store.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]