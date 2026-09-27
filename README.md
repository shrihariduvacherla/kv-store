# KV-Store (Mini Redis)

A TCP server that stores key-value pairs in memory, with support for automatic key expiry (TTL) - inspired by Redis.

## Features
- SET key value - store a value
- SET key value EX seconds - store a value that auto-expires after N seconds
- GET key - retrieve a value (or (nil) if missing or expired)
- DEL key - delete a key

## Tech
- Python, raw TCP sockets (socket module)
- No external dependencies

## Running it
1. Start the server: run python server.py
2. In a separate terminal, run the client: run python client.py

## Example
SET name shrihari EX 10 -> OK
GET name -> shrihari
(after 10 seconds)
GET name -> (nil)

## What's next
- LRU eviction (bounded memory, evict least-recently-used keys)
- Persistence (save data to disk, survive restarts)