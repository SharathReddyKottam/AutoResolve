from typing import Literal
from pydantic import BaseModel, ConfigDict


class Server(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    name: str
    status: Literal["healthy", "degraded", "down"]
    cpu: float
    memory: float
    disk: float
    logs: list[str]