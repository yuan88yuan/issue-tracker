# ISSUE-002: Add VCU Video Decoder Test

- **Status**: Closed
- **Priority**: High
- **Assignee**: 
- **Labels**: Feature | Test
- **Created**: 2026-03-23

---

## Executive Summary
This issue tracks the addition of a VCU video decoder test to the `qcap-demos` project. This test will validate VCU decoding functionality and ensure proper integration with the existing demuxer framework, building upon the work from `ISSUE-001`.

## Description
Building on `ISSUE-001-add-test-to-default-demuxer.md`, this issue focuses on integrating a VCU video decoder into the `qcap-demos` test framework. This test is dependent on the resolution of `qcap-sdk/ISSUE-004-vcu-video-decoder-petalinux-2023-2-not-working.md` as it aims to validate the VCU decoding functionality. The test should initialize the VCU decoder, feed it elementary streams from a demuxed file, and verify the decoded output. This will ensure that the VCU decoding path is functional and correctly integrated within the `qcap-demos` environment, providing comprehensive validation of the video processing pipeline.

## Reproduction Steps / Context
1.  Ensure a suitable VCU-enabled platform is available.
2.  Obtain a sample H.264/H.265 elementary stream compatible with the VCU decoder.
3.  Utilize the demuxer test infrastructure from `ISSUE-001` to extract video elementary stream data.
4.  Implement a new test case that initializes the VCU video decoder with the appropriate configuration.
5.  Feed the extracted elementary stream data to the VCU decoder.
6.  Retrieve and verify the decoded frames (e.g., through checksum comparison, visual inspection, or comparison with reference frames).

## Technical Analysis (Optional)
-   **VCU API Integration**: Investigate and utilize the correct VCU decoder APIs for initialization, parameter configuration, elementary stream submission, and decoded frame retrieval.
-   **Buffer Management**: Implement efficient handling of input elementary stream buffers and output decoded frame buffers, considering zero-copy mechanisms if available.
-   **Error Handling**: Implement robust error checking and reporting for all VCU decoder operations, including stream corruption and hardware errors.
-   **Performance**: Analyze and optimize decoder throughput and latency to meet real-time processing requirements.
-   **Concurrency**: If necessary, manage concurrent access to VCU resources in a multi-threaded testing environment.

## Acceptance Criteria
-   [ ] A new test case, `test_vcu_video_decoder`, is added to the `qcap-demos` project's test suite.
-   [ ] The test successfully initializes and configures the VCU video decoder.
-   [ ] The VCU decoder successfully decodes a variety of sample elementary streams (e.g., H.264, H.265).
-   [ ] Decoded frames can be accurately retrieved and validated against known good outputs.
-   [ ] The new test integrates seamlessly with the existing test infrastructure established in `ISSUE-001` and is designed to facilitate joint testing with fixes from `qcap-sdk/ISSUE-004`.
-   [ ] The test demonstrates proper resource cleanup after execution.

## References
-   `issues/qcap-demos/ISSUE-001-add-test-to-default-demuxer.md`
-   `issues/qcap-sdk/ISSUE-004-vcu-video-decoder-petalinux-2023-2-not-working.md`
-   [Xilinx VCU TRD Documentation - Placeholder URL]
-   [VCU Linux Driver API Documentation - Placeholder URL]
