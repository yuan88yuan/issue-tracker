# ISSUE-006: VCU Decoder Timestamp Handling Discrepancies

- **Status**: Open
- **Priority**: High
- **Assignee**: 
- **Labels**: Bug | VCU
- **Created**: 2026-04-01

---

## Executive Summary
This issue addresses discrepancies and potential inaccuracies in VCU video decoder timestamp handling within the `qcap-sdk` framework. Accurate timestamp propagation is crucial for proper A/V synchronization and stream processing, especially in live decoding and playback scenarios.

## Description
Observations indicate that the VCU video decoder in `qcap-sdk` may not be correctly preserving or generating timestamps for decoded frames. This could manifest as:
-   Out-of-order frames when presented to a renderer.
-   A/V synchronization problems when integrating with audio pipelines.
-   Incorrect frame rates being reported or processed downstream.
-   Issues with seeking and trick-play functionalities.

This issue aims to investigate the timestamp flow from elementary stream input through the VCU decoder to the output frames, identify any points of loss or modification, and implement a robust timestamp handling mechanism.

## Reproduction Steps / Context
1.  Utilize a sample elementary stream (H.264/H.265) with known, verifiable timestamps (e.g., PTS/DTS embedded in the stream).
2.  Integrate the VCU decoder as per existing `qcap-sdk` tests.
3.  Feed the elementary stream to the VCU decoder.
4.  Monitor the timestamps of the input elementary stream packets and compare them against the timestamps of the decoded output frames.
5.  Observe any discrepancies in the timestamp values or their progression.

## Technical Analysis (Optional)
-   **VCU API for Timestamps**: Investigate specific VCU decoder APIs or configurations related to timestamp injection, extraction, and pass-through.
-   **Firmware/Driver Behavior**: Analyze whether the underlying VCU firmware or Linux driver handles timestamps implicitly or requires explicit application-level management.
-   **PTS/DTS Coherence**: Ensure proper handling and propagation of Presentation Timestamp (PTS) and Decode Timestamp (DTS) from the elementary stream.
-   **Clock Domains**: Consider potential issues related to different clock domains between the system, VCU, and any downstream components.
-   **Buffer Metadata**: Verify if timestamp information is correctly attached to output frame buffers as metadata.

## Acceptance Criteria
-   [ ] VCU decoded frames accurately reflect the timestamps of their corresponding input elementary stream packets (PTS/DTS).
-   [ ] The timestamp propagation mechanism is robust against stream discontinuities or errors.
-   [ ] A new test is added to `qcap-sdk` specifically validating VCU decoder timestamp accuracy.
-   [ ] Documentation is updated to reflect proper timestamp handling practices for the VCU decoder.
-   [ ] No A/V synchronization issues are observed when decoded video is paired with synchronized audio.

## References
-   `issues/qcap-sdk/archive/CLOSED-ISSUE-004-vcu-video-decoder-petalinux-2023-2-not-working.md`
-   [Relevant VCU Programming Guide/Datasheet - Placeholder URL]
-   [Video Timestamping Standards (e.g., MPEG-2 Systems, H.264/H.265 SEI messages) - Placeholder URL]
