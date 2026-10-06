from autoresolve.sim.models import Server

SERVERS = {
    "web-01": Server(
        name="web-01",
        status="healthy",
        cpu=20,
        memory=40,
        disk=45,
        logs=["INFO: service started"],
    ),
    "db-01": Server(
        name="db-01",
        status="healthy",
        cpu=15,
        memory=55,
        disk=60,
        logs=["INFO: connection pool ready"],
    ),
}
def plant_disk_full():
    server = SERVERS["web-01"]
    server.status = "degraded"
    server.disk = 98
    server.logs.append("ERROR: No space left on device")