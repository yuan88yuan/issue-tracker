# ISSUE-005: Customize Xilinx HDMI TX DRM Linux Driver for FPGA Design

- **Status**: Open
- **Priority**: High
- **Assignee**: Unassigned
- **Labels**: Feature, Driver, FPGA
- **Created**: 2026-03-18

---

## Executive Summary
The existing Xilinx HDMI TX DRM Linux driver needs significant customization to support our specific FPGA design's HDMI output capabilities and integrate seamlessly with the sc6f0-dante system. This involves adapting the driver to our unique hardware block configuration and potentially extending its functionality.

## Description
The current Xilinx HDMI TX DRM (Direct Rendering Manager) driver, intended for standard Xilinx reference designs, does not directly support the customized HDMI Transmitter IP integrated into our `sc6f0-dante` FPGA design. This customization is necessary to enable proper video output, including specific timing, resolution, color space, and HDCP requirements unique to our hardware. The task involves modifying the driver to recognize and correctly interface with our FPGA's HDMI TX IP block, potentially adding new device tree bindings, and adjusting the DRM framework's output pipeline.

## Reproduction Steps / Context
1. Integrate the `sc6f0-dante` FPGA design with a Linux-based host system.
2. Attempt to use the standard Xilinx HDMI TX DRM driver with our custom HDMI TX IP.
3. Observe driver probe failures, incorrect display detection, or lack of video output.

## Technical Analysis (Optional)
*   **Suspected Cause**:
    *   Mismatch between standard Xilinx IP register maps/control logic and our customized HDMI TX IP.
    *   Missing or incorrect device tree bindings for our specific hardware instantiation.
    *   Unsupported features or configurations in the generic driver for our custom requirements (e.g., specific EDID handling, HDCP versions, audio integration).
    *   Clocking and reset dependencies not handled correctly by the generic driver in our context.
*   **Affected Components**: Xilinx HDMI TX Subsystem IP, Linux DRM subsystem, specific driver modules (e.g., `xilinx_drm.c`, `xilinx_hdm_tx.c`), device tree source (`.dts`).
*   **Diagnostic Strategies**:
    *   Analyze device tree parsing logs during kernel boot to identify binding errors.
    *   Use `debugfs` or `tracepoints` within the DRM driver to inspect register accesses and driver state.
    *   Compare the register map and control flow of our custom HDMI TX IP against the expected behavior of the stock Xilinx driver.
    *   Develop a minimal test application to probe driver functionality and register interactions.
*   **Proposed Solution**:
    *   Create a new or modify an existing platform device driver for our specific HDMI TX IP.
    *   Define accurate device tree nodes and properties that reflect our hardware.
    *   Implement necessary callbacks and functions within the DRM framework to control our HDMI TX IP.
    *   Thoroughly test various video modes, color depths, and HDCP functionalities.

## Acceptance Criteria
- [ ] The customized DRM driver successfully probes and identifies the HDMI TX IP in our FPGA design.
- [ ] The system can output video resolutions (e.g., 1080p60, 4K30) specified in our design.
- [ ] Color space and pixel format settings are correctly applied and displayed.
- [ ] HDCP negotiation (if applicable) functions correctly through the driver.
- [ ] The driver integrates cleanly with the Linux kernel and other relevant subsystems.

## References
- [Links to related issues, documentation, or code snippets.]
