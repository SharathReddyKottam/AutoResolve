# Slow database queries

## Symptoms
- Pages load slowly while the web server looks healthy
- Logs show query timeouts or long-running queries
- Database connections pile up

## How to check
- Check database CPU, memory, and connection count
- Look for long-running or blocked queries

## Fix
- Stop the blocking query
- Restart the connection pool
- Add an index if one is missing (human review)

## Risk
- Stopping queries can lose in-flight work. Require human approval.