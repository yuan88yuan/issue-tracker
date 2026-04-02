# ISSUE-004: Dante Ultra TX Encoder IP Functionality Issue After ETH0 Up

- **Status**: Open
- **Priority**: Critical
- **Assignee**: Unassigned
- **Labels**: Bug, Network
- **Created**: 2026-03-18

---

## Executive Summary
The Dante Ultra TX Encoder IP fails to function correctly after the ETH0 interface initializes and comes online. This prevents the device from transmitting Dante audio, severely impacting its core functionality.

## Description
Upon system boot-up or after reconfiguring network interfaces, specifically when ETH0 transitions to an 'up' state, the Dante Ultra TX Encoder IP stops processing or transmitting audio. Prior to ETH0 becoming active, or if ETH0 remains down, the encoder appears to operate normally. This suggests a conflict or an initialization sequence dependency related to the network interface.

## Reproduction Steps / Context
1. Boot the `sc6f0-dante` device.
2. Ensure ETH0 is configured to come up automatically, or manually bring it up (`ifconfig eth0 up`).
3. Observe the status of the Dante Ultra TX Encoder; it will fail to transmit Dante streams.
4. (Optional) Disable ETH0; the Dante TX encoder may resume functionality.

## Technical Analysis (Optional)
*   **Suspected Cause**:
    *   Network interface binding order/priority: The Dante IP might be binding to a temporary or incorrect network interface before ETH0 is fully configured, and fails to re-bind correctly.
    *   IP address conflict or routing issue: ETH0 coming up might introduce an IP address or routing change that conflicts with the Dante IP's operation.
    *   Driver interaction: A bug in the ETH0 driver or its interaction with the Dante IP driver/firmware.
    *   Resource contention: ETH0's activation might consume critical resources (e.g., DMA channels, interrupts) required by the Dante IP.
*   **Affected Components**: Dante Ultra TX Encoder IP core, Network Interface Card (NIC) driver for ETH0, network stack configuration.
*   **Diagnostic Strategies**:
    *   Monitor network interface states and Dante IP status simultaneously.
    *   Capture network traffic on all interfaces to observe Dante packet flow.
    *   Check system logs for network-related errors or Dante IP diagnostics.
    *   Test with different ETH0 configurations (e.g., static IP vs. DHCP, different IP ranges).
    *   Attempt to defer Dante IP initialization until after ETH0 is fully up.
*   **Proposed Solution**:
    *   Implement a mechanism to ensure the Dante IP initializes or re-initializes *after* all primary network interfaces are stable.
    *   Investigate potential conflicts in IP address assignment or routing tables.
    *   Review driver interaction and ensure correct resource allocation.

## Acceptance Criteria
- [ ] The Dante Ultra TX Encoder IP correctly transmits audio after ETH0 comes up.
- [ ] Dante audio streams are stable and without interruption once ETH0 is active.
- [ ] No manual intervention is required to restore Dante functionality after ETH0 activation.

## References
- [Links to related issues, documentation, or code snippets.]
