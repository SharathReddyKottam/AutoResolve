# Memory leak

## Symptoms
- Memory climbs steadily over hours or days
- Service gets slower, then crashes with out-of-memory errors
- Restart fixes it temporarily

## How to check
- Check memory percentage over time
- Look for out-of-memory messages in logs

## Fix
- Restart the service to free memory
- Open a ticket for developers to find the leak

## Risk
- Restart is low risk, but the leak will return. Escalate the root cause.