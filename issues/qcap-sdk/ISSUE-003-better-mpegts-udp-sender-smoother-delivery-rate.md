# ISSUE-003: Better MPEGTS UDP Sender: Smoother Delivery Rate

- **Status**: Open
- **Priority**: High
- **Assignee**: Unassigned
- **Labels**: Bug, Feature
- **Created**: 2026-03-18

---

## Executive Summary
The current MPEGTS UDP sender in the qcap-sdk exhibits non-uniform packet delivery rates, leading to potential buffer underruns/overruns and visual artifacts in downstream decoders. This issue aims to improve the sender's mechanism to achieve a consistently smoother and more predictable packet transmission, optimizing for constant bitrate (CBR) or managed variable bitrate (VBR) streams.

## Description
Users are experiencing inconsistent delivery of MPEG Transport Stream (TS) packets over UDP when utilizing the `qcap-sdk`'s sender component. This irregularity manifests as jitter and potentially dropped frames on the receiver side, impacting the quality of service for real-time media applications. The objective is to analyze and refactor the UDP sending logic to ensure a more even distribution of packets over time, reducing burstiness and maintaining a stable output rate.

## Reproduction Steps / Context
1. Utilize the `qcap-sdk` to transmit an MPEGTS stream via UDP.
2. Monitor the network traffic and packet inter-arrival times at the receiver.
3. Observe fluctuations and non-uniform distribution of packets.

## Technical Analysis (Optional)
*   **Suspected Cause**: Potential thread scheduling issues, insufficient buffering mechanisms, or imprecise timing loops in the UDP send function. Lack of proper rate-limiting or pacing logic.
*   **Affected Components**: `MpegTsUdpSender` class/module within `qcap-sdk`. Network interface interactions.
*   **Diagnostic Strategies**:
    *   Implement high-resolution timers to measure inter-packet delays directly within the sender.
    *   Analyze CPU utilization and context switching during active sending.
    *   Introduce explicit pacing (e.g., using `nanosleep` or `select` with timeouts) to regulate send rate.
    *   Evaluate the impact of socket buffer sizes (`SO_SNDBUF`).
*   **Proposed Solution**: Introduce a token bucket or leaky bucket algorithm for pacing, or integrate with a more robust real-time scheduling mechanism.

## Acceptance Criteria
- [ ] The MPEGTS UDP sender delivers packets with a significantly reduced jitter (e.g., < 2ms standard deviation on inter-packet time for a 10 Mbps stream).
- [ ] The delivery rate is consistently smooth and predictable, observable via network analysis tools.
- [ ] No packet loss introduced by the new pacing mechanism under normal operating conditions.
- [ ] The sender can maintain specified target bitrates accurately.

## References
- [Links to related issues, documentation, or code snippets.]
