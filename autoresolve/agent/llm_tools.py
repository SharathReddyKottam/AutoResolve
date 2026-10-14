from langchain_core.tools import StructuredTool
from autoresolve.tools.registry import TOOLS

def build_langchain_tools():
    return [
        StructuredTool.from_function(
            func=tool["function"],
            name=name,
            description=tool["description"],
        )
        for name, tool in TOOLS.items()
    ]