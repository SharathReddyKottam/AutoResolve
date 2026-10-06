# Service crash or unreachable

## Symptoms
- Server is unreachable or returns connection errors
- Status shows down
- Logs show the service process exited unexpectedly

## How to check
- Check the service status on the server
- Read the last log lines before the crash

## Fix
- Restart the service
- If it crashes again right away, escalate to a human

## Risk
- Restarting briefly interrupts the service. Low risk, but notify the team.