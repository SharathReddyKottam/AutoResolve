from autoresolve.sim.world import SERVERS

def check_disk(server_name: str) -> str:
    server = SERVERS.get(server_name)
    if server is None:
        return f"Error: unknown server {server_name}"
    return f"{server.name}: disk usage is {server.disk}%"

def read_logs(server_name: str, lines: int = 5) -> str:
    server = SERVERS.get(server_name)
    if server is None:
        return f"Error: unknown server {server_name}"
    return "\n".join(server.logs[-lines:])