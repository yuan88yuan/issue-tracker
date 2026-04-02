# ISSUE-001: support platform holoscan-cuda13-amd64

- **Status**: Open
- **Priority**: Medium
- **Assignee**: 
- **Labels**: Feature
- **Created**: 2026-04-02

---

## Executive Summary
Add support for the new NVIDIA Holoscan platform image `nvcr.io/nvidia/clara-holoscan/holoscan:v4.1.0-cuda13`. This requires building the SDK with the new platform and updating documentation.

## Description
The SDK currently supports older CUDA7/10/11 pulls. The new Holoscan CUDA13 Docker image introduces new dependencies and environment variables that need to be handled.

## Reproduction Steps / Context
1. Build SDK using the Holoscan CUDA13 image.
2. Verify that all binaries compile and run.
3. Update integration scripts to pull the image.

## Technical Analysis (Optional)
The Docker image uses a newer base and requires switching to `holoscan:4.1.0-cuda13`. The SDK must adjust the environment setup to point to the correct `CUDA_HOME` and library paths.

## Acceptance Criteria
- [ ] Build completes with the new Docker image.
- [ ] Runtime tests pass.
- [ ] Documentation updated with the new image link.

## References
- Docker image: `nvcr.io/nvidia/clara-holoscan/holoscan:v4.1.0-cuda13`