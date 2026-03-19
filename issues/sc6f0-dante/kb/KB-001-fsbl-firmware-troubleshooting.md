# KB-001-fsbl-firmware-troubleshooting

## 1. Overview
Troubleshooting guide for FSBL (First Stage Boot Loader) firmware issues on SC6F0-DANTE, especially when patches cause unexpected behavior.

## 2. Problem/Context
FSBL firmware, combined with patches, exhibits inconsistent behavior leading to boot failures or instability. Patches may not apply cleanly or introduce regressions.

**Primary Solution:** To address issues where the default FSBL firmware recipe does not work with patches, it is recommended to change `SRC_URI` to `EMBEDDEDSW_SRCURI`.

## 3. Solution/Details

**Technical Suspicions (Optional):**
- Incorrect patch application order/conflicts.
- Environment-specific build issues.
- Toolchain/SDK dependency problems.
- Misconfigured hardware registers/boot parameters.

**Diagnostic Strategies (Optional):**
1.  **Verify Patch Integrity:** Manually apply patches, check `.rej` files, ensure correct `git apply` or `patch` commands.
2.  **Review Build Logs:** Analyze for warnings/errors, confirm compiler flags.
3.  **Compare FSBL Binaries:** Use `diff` or hex editor with known good binaries.
4.  **JTAG Debugging:** Step through FSBL execution, observe register/memory, focus on MMIO.
5.  **Hardware Environment Check:** Confirm board revisions, power, clocks.

## 4. Related Issues/Articles (Optional)
- Refer to `ISSUE-XXX-fsbl-boot-failure.md`.
- Xilinx documentation for FSBL customization.

## 5. Keywords
FSBL, firmware, boot, troubleshooting, SC6F0-DANTE, patch, build, Yocto, Xilinx, embedded, debugging