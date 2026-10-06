from autoresolve.sim.world import SERVERS

def plant_disk_full():
    server = SERVERS["web-01"]
    server.status = "degraded"
    server.disk = 98
    server.logs.append("ERROR: No space left on device")