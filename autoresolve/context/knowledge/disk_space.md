# Disk space exhaustion

## Symptoms
- Slow responses or failed writes
- Logs contain "No space left on device" or ENOSPC
- Disk usage above 90%

## How to check
- Check disk usage percentage on the affected server
- Look for large or old log files

## Fix
- Clear old and rotated log files
- Remove temporary files
- If usage stays high, expand the volume and escalate to a human

## Risk
- Deleting files is destructive. Only clear logs and temp files automatically.