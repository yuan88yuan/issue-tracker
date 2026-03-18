# ISSUE-002: Memory Leakage in Asynchronous Snapshot Implementation

- **Status**: Open
- **Priority**: High
- **Assignee**: [Unassigned]
- **Labels**: Bug | Performance
- **Created**: 2026-03-18

---

## Executive Summary
This issue tracks a critical memory leak identified during high-frequency asynchronous snapshot operations. Repeatedly triggering the snapshot API leads to continuous heap exhaustion, eventually causing the application to be terminated by the OOM (Out Of Memory) killer.

## Description
The QCAP SDK provides an asynchronous API for capturing still frames while the main video stream is active. However, when `CaptureSnapshotAsync()` is invoked repeatedly, the system memory consumption increases linearly. This suggests that the underlying buffers, FFmpeg frame structures (`AVFrame`), or internal task objects are not being correctly deallocated upon completion of the asynchronous task.

## Reproduction Steps / Context
1. Initialize a stable video capture pipeline at 1080p60.
2. Trigger the `CaptureSnapshotAsync()` method at a frequency of 5Hz.
3. Monitor the process memory usage using `htop` or `pmap -x [pid]`.
4. Observe the steady increase in RSS (Resident Set Size) and Virtual Memory.
5. (Optional) Run the application through `valgrind --leak-check=full` to pinpoint the allocation site.

## Technical Analysis (Optional)
- **Buffer Management**: Suspected failure to call `av_frame_free()` or `av_packet_unref()` within the asynchronous callback handler.
- **Task Lifespan**: If using `boost::asio` for task dispatch, ensure that shared pointers or lambda captures are not creating circular references or extending the lifespan of large data buffers indefinitely.
- **Encoder Context**: Verify if the MJPEG/PNG encoder used for snapshots is being re-initialized per-call without proper destruction.
- **V4L2 DMA-BUF**: If snapshots are using zero-copy, check if the DMA-BUF file descriptors are being leaked.

## Acceptance Criteria
- [ ] Root cause of the memory leak identified via heap analysis (e.g., Valgrind or Massif).
- [ ] Memory usage remains stable (flat-line) during a 1-hour stress test at 10Hz snapshot frequency.
- [ ] Implement a regression test that monitors memory usage during automated snapshotting.
- [ ] Ensure all asynchronous completion paths (Success, Error, Timeout) perform full cleanup.

## References
- [FFmpeg Memory Management Best Practices](https://ffmpeg.org/doxygen/trunk/group__lavu__mem.html)
- [Valgrind Documentation on Memory Leaks](https://valgrind.org/docs/manual/mc-manual.html)
