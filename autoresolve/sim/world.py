from autoresolve.sim.models import Server


def build_servers():
    return {
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


SERVERS = build_servers()


def reset_world():
    SERVERS.clear()
    SERVERS.update(build_servers())