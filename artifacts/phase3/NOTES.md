# Phase 3 Notes

- Implemented `index_load` parsing:
  - `<mode> <hash-hex> <mtime> <size> <path>`
  - empty index behavior when file is missing
- Implemented `index_save`:
  - sorted write by path
  - temp file flush + `fsync`
  - atomic `rename` to `.pes/index`
  - `.pes` directory `fsync`
- Implemented `index_add`:
  - file read
  - blob write through object store
  - metadata update/insert in memory
  - persistent save to index
