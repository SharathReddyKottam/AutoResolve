from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from autoresolve.config import config

load_dotenv()

def get_llm():
    settings = config["llm"]
    if settings["provider"] == "openai":
        return ChatOpenAI(model=settings["model"], temperature=settings["temperature"])
    raise ValueError(f"Unknown LLM provider: {settings['provider']}")