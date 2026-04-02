# ISSUE-006: Add Dante Video Processing Scaler IP

- **Status**: Closed
- **Priority**: Medium
- **Assignee**: Unassigned
- **Labels**: Feature
- **Created**: 2026-03-20

---

## Executive Summary
Integrate a Dante Video Processing Scaler IP into the `sc6f0-dante` system to enable flexible video scaling and format conversion capabilities for Dante-enabled video streams.

## Description
The current `sc6f0-dante` system requires enhanced video processing capabilities, specifically resolution scaling and format adaptation, to support diverse display and sink requirements within a Dante AV ecosystem. This issue proposes the addition of a dedicated Dante Video Processing Scaler IP core to handle these functionalities efficiently. This IP should be configurable to support various input/output resolutions and aspect ratios, ensuring seamless integration with existing Dante video infrastructure.

## Reproduction Steps / Context
1. Current `sc6f0-dante` deployment lacks integrated hardware-accelerated video scaling.
2. Need to support multiple video output resolutions (e.g., 720p, 1080p, 4K) from a single Dante AV source.
3. Requirement for on-the-fly aspect ratio correction and frame rate conversion for compatibility with various display devices.

## Technical Analysis (Optional)
Investigation will involve evaluating available Dante-compatible video scaler IP cores (e.g., Xilinx VTC/VPSS, third-party solutions). Key considerations include latency, resource utilization (LUTs, BRAMs, DSPs), and configurability via AXI interfaces. A hardware-level integration plan for the selected IP within the existing FPGA design is required.

## Acceptance Criteria
- [ ] Dante Video Processing Scaler IP is integrated into the `sc6f0-dante` FPGA design.
- [ ] The IP can successfully scale video from a source resolution (e.g., 1080p) to a target resolution (e.g., 720p or 4K).
- [ ] Video scaling operations maintain visual quality without introducing significant artifacts or latency.
- [ ] Configuration registers for resolution and aspect ratio are accessible and controllable via the system's control plane.
- [ ] The integrated scaler is validated with Dante AV streams.

## References
- None
