# Lessons Learned — Phase 1

## VM Storage and Snapshot Stability

One of the first infrastructure issues encountered during Phase 1 was VM corruption caused by snapshot dependency failures.

The original Ubuntu lab VM was created using a linked clone stored inside a OneDrive-managed directory. This caused VirtualBox snapshot files to become unavailable, resulting in:

```text
VERR_FILE_NOT_FOUND
```

## Root Cause
 - Linked clones depend on parent snapshot chains
 - OneDrive can offload or modify synchronized files
 - Missing .vdi snapshot files break the VM state chain

## Resolution
The lab VM was rebuilt using:
 - Full clone strategy
 - Local-only VM storage
 - Dedicated VM directory outside OneDrive
   
## Key Takeaways
 - Virtual machines should not be stored inside cloud-synchronized folders
 - Full clones are more stable for beginner lab environments
 - Snapshot dependency chains introduce recovery complexity
 - Infrastructure stability is foundational for cybersecurity experimentation
