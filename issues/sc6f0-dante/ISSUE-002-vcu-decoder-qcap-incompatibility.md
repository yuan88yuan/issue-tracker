# ISSUE-002: VCU Video Decoder Incompatibility with QCAP SDK (Petalinux 2023.2)

- **Status**: Open
- **Priority**: High
- **Assignee**: (Unassigned)
- **Labels**: Bug
- **Created**: 2026-03-18

---

## Executive Summary
The Video Codec Unit (VCU) hardware-accelerated decoder integrated into Petalinux 2023.2 is exhibiting critical compatibility failures with the proprietary QCAP SDK on the SC6F0-Dante platform. This regression disrupts video processing pipelines, necessitating a technical resolution to restore decoding functionality within the existing SDK framework.

## Description
Following the migration to Petalinux 2023.2, the interaction between the VCU drivers and the QCAP SDK has become unstable. Initial reports indicate that the VCU decoder fails to initialize correctly when invoked through the QCAP API, suggesting a possible mismatch in API versions, kernel-user space ABI changes, or memory management shifts (e.g., CMA/DMA-BUF handling) introduced in the updated BSP.

## Reproduction Steps / Context
1. Deploy the Petalinux 2023.2 firmware image to the SC6F0-Dante target hardware.
2. Launch a standard QCAP SDK-based video decoding application.
3. Attempt to instantiate and configure the VCU decoder via the QCAP API.
4. Observe the failure: typically manifested as a decoder initialization timeout or a buffer allocation error.

## Technical Analysis (Optional)
The 2023.2 BSP includes updated versions of `vcu-ctrl`, `vcu-omx-il`, and related kernel drivers. The investigation should focus on:
- Discrepancies in the `vcu` kernel driver ABI compared to the previous stable release.
- Changes in the memory allocation strategy for video buffers, particularly around contiguous memory regions.
- Potential deprecation of specific OMX parameters or control structures utilized by the QCAP SDK.

## Acceptance Criteria
- [ ] Identification of the specific API or driver mismatch causing the failure.
- [ ] VCU decoder successfully processes H.264/H.265 bitstreams within the QCAP SDK environment.
- [ ] Verified stability across multiple decoding sessions on the target hardware.
- [ ] Documentation of any necessary SDK or configuration changes required for Petalinux 2023.2 support.

## References
- Petalinux 2023.2 Release Notes (Xilinx/AMD)
- QCAP SDK Integration Guide (v1.4+)
- SC6F0-Dante Hardware Specification (VCU Section)
