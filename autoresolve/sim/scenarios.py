from typing import Callable
from pydantic import BaseModel
from autoresolve.sim.world import SERVERS


def plant_disk_full():
    server = SERVERS["web-01"]
    server.status = "degraded"
    server.disk = 98
    server.logs.append("ERROR: No space left on device")


class Scenario(BaseModel):
    id: str
    tickets: list[str]
    root_cause: str
    correct_fix: str
    plant: Callable[[], None]


DISK_FULL = Scenario(
    id="disk_full",
    tickets=[
        "web-01 is returning errors and customers are complaining",
        "the website is really slow and some pages won't load",
        "checkout keeps failing, please look at web-01 urgently",
    ],
    root_cause="disk full on web-01",
    correct_fix="clear disk space on web-01",
    plant=plant_disk_full,
)


def plant_service_down():
    server = SERVERS["web-01"]
    server.status = "down"
    server.logs.append("ERROR: web service process exited unexpectedly")


SERVICE_DOWN = Scenario(
    id="service_down",
    tickets=[
        "web-01 is completely unreachable",
        "our site shows a connection error for every visitor",
        "web-01 stopped responding about ten minutes ago",
    ],
    root_cause="web service process crashed on web-01",
    correct_fix="restart the web service on web-01",
    plant=plant_service_down,
)

ALL_SCENARIOS = [DISK_FULL, SERVICE_DOWN]