Redis is an open-source, **in-memory data structure** store used as a:
- Database
- Cache
- Message Broker
- Streaming engine
## Installation on Linux - Ubuntu
`sudo apt-get update`
`sudo apt-get install redis-server`

## Start redis-server as daemon
`redis-server --daemonize yes`

---

## Redis Data Types
### Strings
* stores redis key with a value of type sequences of bytes, including text, serialized objects, and binary arrays
* often used for caching but also support increments and bitwise operations

**Commands**

|command|description|
|---|---|
|`KEYS *` |get all keys|
|`SET`|stores a string value|
|`SETNX`|stores a string value if key doesn'y already exists, useful for implementing locks|
|`GET`|retrieves a string value|
|`MSET`|set multiple string values|
|`MGET`|retrieve multiple string values|
|`INCRBY`|atomically increments counters stored at a given key|
|`INCRBYFLOAT`|atomic increment for floating point numbers|


## JSON
* sets a redis key with a JSON value