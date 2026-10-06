# High CPU usage

## Symptoms
- Slow responses and timeouts
- CPU above 90% for several minutes
- Logs show slow requests or a runaway process

## How to check
- Check CPU percentage and which process uses it
- Look for a recent deploy or traffic spike

## Fix
- Restart the runaway process
- Scale out if load is genuinely high

## Risk
- Killing the wrong process can cause an outage. Require human approval.