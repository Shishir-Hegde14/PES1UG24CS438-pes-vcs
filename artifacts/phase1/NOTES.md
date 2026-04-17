# Phase 1 Notes

- Implemented `object_write` with:
  - object header construction (`<type> <size>\0`)
  - SHA-256 on full object bytes
  - dedup check
  - shard directory creation
  - temp file + `fsync` + atomic `rename`
  - shard directory `fsync`
- Implemented `object_read` with:
  - full file read
  - hash re-verification against requested ID
  - header parse and payload size validation
  - payload extraction for caller ownership
