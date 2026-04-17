# Phase 2 Notes

- Implemented `tree_from_index` recursively:
  - reads staged paths from `.pes/index`
  - groups entries by current directory prefix
  - emits file entries directly
  - emits subdirectory entries by recursive subtree write
  - serializes each tree and stores as `OBJ_TREE`
- Tree object writing is deterministic through `tree_serialize` sorting.
