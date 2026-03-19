# ISSUE-004: VCU Video Decoder Failure in Petalinux 2023.2

- **Status**: Open
- **Priority**: High
- **Assignee**: Unassigned
- **Labels**: Bug
- **Created**: 2026-03-19

---

## Executive Summary
The VCU video decoder within the Petalinux 2023.2 environment for the `qcap-sdk` project is non-functional, impacting core video processing capabilities. This issue is specifically observed in contexts involving `ZzVideoDecoder2_allegro2.cpp`.

## Description
Detailed description of the VCU video decoder's failure to initialize or process video streams correctly under Petalinux 2023.2. This impacts the ability to decode video within the `qcap-sdk`. The problem appears to manifest when `ZzVideoDecoder2_allegro2.cpp` is engaged, suggesting potential integration issues or API mismatches with the Allegro Demosaic/Video IP.

## Reproduction Steps / Context
1. Initialize the `qcap-sdk` environment on a Petalinux 2023.2 platform.
2. Attempt to utilize the VCU video decoder functionality, specifically through the `ZzVideoDecoder2_allegro2.cpp` component.
3. Observe that the video decoding process fails to complete or produces corrupted output.

## Technical Analysis (Optional)
*   **Suspected Root Cause**: Potential API incompatibility between the Petalinux 2023.2 VCU drivers and the `allegro2` integration as seen in `ZzVideoDecoder2_allegro2.cpp`. This could involve incorrect register configurations, buffer management issues (e.g., memory alignment, cache coherence), or a misconfiguration of the VCU IP during the Petalinux build process.
*   **Diagnostic Strategies**:
    *   Verify VCU firmware/driver versions and their compatibility with Petalinux 2023.2 and `qcap-sdk` requirements.
    *   Enable verbose logging for VCU operations and the `ZzVideoDecoder2_allegro2.cpp` module to pinpoint failure points (e.g., initialization, frame submission, buffer completion).
    *   Isolate the `allegro2` decoder functionality from `ZzVideoDecoder2_allegro2.cpp` to test VCU independence.
    *   Review VCU IP configuration in Petalinux and ensure all necessary hardware accelerators are correctly enabled and mapped.
    *   Utilize `strace` or similar tools to monitor system calls related to VCU device access.

## Acceptance Criteria
- [x] The VCU video decoder successfully initializes and decodes video streams within the Petalinux 2023.2 environment.
- [x] `ZzVideoDecoder2_allegro2.cpp` successfully utilizes the VCU for video decoding without errors or corruption.
- [ ] Integration of the VCU decoder operates stably under sustained load.

## References
- `ZzVideoDecoder2_allegro2.cpp` (code reference within the project)
