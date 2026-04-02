# ISSUE-001: System Hang During Linux Kernel Initialization (Suspected FPGA Interaction)

- **Status**: Open
- **Priority**: Critical
- **Assignee**: [Unassigned]
- **Labels**: Bug, Hardware, FPGA, Boot
- **Created**: 2026-03-18

---

## Executive Summary
The system experiences a total hang during the Linux boot sequence, preventing the kernel from reaching a functional user-space environment. Preliminary observations suggest the hang occurs during the initialization of FPGA-dependent subsystems or drivers, indicating a potential hardware/software synchronization failure.

## Description
The boot process proceeds through the bootloader but fails during the kernel's hardware discovery or driver initialization phase. The system becomes unresponsive (no console output, no heartbeat), necessitating a hard reset. This issue significantly impacts development velocity and system reliability.

## Reproduction Steps / Context
1. Power on the **sc6f0-dante** target hardware.
2. Monitor the serial console output during the Linux kernel decompression and early boot.
3. Observe the point of failure (typically after [Specific Driver] or during [FPGA Bitstream Loading]).
4. The system hangs indefinitely at this stage.

## Technical Analysis (Optional)
- **Identified Root Cause**: The system hang is attributed to an issue within the SD controller.

- **Affected Components**: Linux Kernel (early boot), FPGA PCIe/AXI Bridge, Custom FPGA IP Cores.
- **Diagnostic Strategy**: Utilize JTAG debugging to inspect the PC (Program Counter) at the time of the hang and analyze the FPGA state machine status.

## Acceptance Criteria
- [x] Root cause of the boot hang is identified and documented.
- [ ] System consistently reaches the login prompt over 50 consecutive boot cycles.
- [ ] FPGA-related drivers handle initialization timeouts gracefully without hanging the kernel.

## References
- [Link to Serial Console Logs]
- [FPGA Bitstream Version Info]
- [Schematics for sc6f0-dante Board]
