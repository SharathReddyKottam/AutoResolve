from autoresolve.tools.diagnostics import check_disk, read_logs
from autoresolve.tools.actions import restart_service, clear_disk

TOOLS = {
    "check_disk": {
        "function": check_disk,
        "description": "Check the disk usage percentage on a server.",
        "risk": "auto",
    },
    "read_logs": {
        "function": read_logs,
        "description": "Read the most recent log lines from a server.",
        "risk": "auto",
    },
    "restart_service": {
        "function": restart_service,
        "description": "Restart the web service on a server. Fails if the disk is full.",
        "risk": "notify",
    },
    "clear_disk": {
        "function": clear_disk,
        "description": "Delete old log files to free disk space on a server.",
        "risk": "approval",
    },
}