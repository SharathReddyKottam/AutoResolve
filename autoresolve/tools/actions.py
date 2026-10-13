from autoresolve.sim.world import SERVERS

def restart_service(server_name: str) -> str:
    server = SERVERS.get(server_name)
    if server is None:
        return f"Error: unknown server {server_name}"
    if server.disk >= 95:
        server.logs.append("ERROR: restart failed, no space left on device")
        return f"{server.name}: restart failed, disk is full"
    server.status = "healthy"
    server.logs.append("INFO: service restarted")
    return f"{server.name}: service restarted, status is healthy"

def clear_disk(server_name: str) -> str:
    server = SERVERS.get(server_name)
    if server is None:
        return f"Error: unknown server {server_name}"
    server.disk = 40
    server.status = "healthy"
    server.logs.append("INFO: old logs cleared, disk usage at 40%")
    return f"{server.name}: cleared old logs, disk usage is now 40.0%"
