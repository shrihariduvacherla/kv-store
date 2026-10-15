# KV-Store (Mini Redis)

A TCP server that stores key-value pairs in memory, with automatic key expiry (TTL) and snapshot persistence, inspired by Redis.

## Features
- SET key value - store a value
- SET key value EX seconds - store a value that auto-expires after N seconds
- GET key - retrieve a value (or (nil) if missing or expired)
- DEL key - delete a key
- SAVE - write all data to dump.json (loaded back automatically when the server starts)

## Tech
- Python, raw TCP sockets (socket module)
- JSON for persistence
- No external dependencies

## Running it
1. Start the server: python server.py
2. In a separate terminal, run the client: python client.py

## Example
SET name shrihari EX 10 -> OK
GET name -> shrihari
(after 10 seconds)
GET name -> (nil)

## What's next
- LRU eviction (bounded memory, evict least-recently-used keys)
- Support for multiple simultaneous clients