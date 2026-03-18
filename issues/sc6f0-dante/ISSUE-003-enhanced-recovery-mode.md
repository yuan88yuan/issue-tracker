# ISSUE-003: Enhanced Recovery Mode via Boot-Time GPIO Interaction (Button Combinations)

- **Status**: Open
- **Priority**: Medium
- **Assignee**: [Unassigned]
- **Labels**: Feature
- **Created**: 2026-03-18

---

## Executive Summary
This issue tracks the implementation of a robust, hardware-triggered recovery mechanism. The system must detect specific button combinations (GPIO states) during the early boot phase (FSBL/U-Boot) to initiate a fallback recovery mode. This is critical for field-serviceability when the primary boot sequence or filesystem is corrupted.

## Description
Currently, recovering a system with a corrupted root filesystem or invalid configuration often requires specialized hardware (JTAG) or manual intervention via the serial console. To improve user experience and field-recovery, we need a "better recovery mode" that allows users to trigger a safe-boot or factory-reset state by holding down specific physical buttons during power-on.

## Reproduction Steps / Context
1. Power on the sc6f0-dante hardware.
2. Observe standard boot sequence leading to potential hang or failure.
3. Lack of a user-accessible hardware-level trigger to force an alternative boot path (e.g., TFTP, SD card recovery, or minimal RAMdisk).

## Technical Analysis (Optional)
- **Hardware Interface**: Identification of available GPIO pins mapped to physical buttons (e.g., Reset, Function, or User buttons).
- **U-Boot Integration**: Modification of the U-Boot environment or `board_init` logic to poll GPIO states before the `bootcmd` is executed.
- **Timing/Debouncing**: Implementation of a short delay/poll loop (e.g., 2-3 seconds) during boot to ensure the user has sufficient time to engage the buttons and to debounce the input.
- **Recovery Actions**:
  - `boot_recovery`: Load a minimal initramfs from a dedicated "recovery" partition.
  - `force_tftp`: Trigger a network boot attempt regardless of local environment variables.
  - `reset_env`: Clear U-Boot environment variables to factory defaults.

## Acceptance Criteria
- [ ] U-Boot successfully detects a specific button combination during the first 3 seconds of power-on.
- [ ] System diverts from standard `bootcmd` to a defined recovery sequence when the trigger is active.
- [ ] Recovery mode provides a visual/serial confirmation (e.g., "Recovery Mode Activated").
- [ ] Documentation updated for field technicians.

## References
- [Xilinx U-Boot Documentation](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18841973/U-Boot)
- [Project Dante Hardware Schematic v1.2 (GPIO Mapping)]
