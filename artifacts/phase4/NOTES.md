# Phase 4 Notes

- Implemented `commit_create`:
  - constructs root tree from staged index
  - reads parent from HEAD when available
  - fills author, timestamp, and message
  - serializes + writes `OBJ_COMMIT`
  - advances branch ref via `head_update`
- Verified `pes log` walks history through parent links.
