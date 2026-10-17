# Validation record

Checked October 17, 2026. This records package and loader checks, not a public release or an authenticated G2X workflow.

## Passed

- `node scripts/validate.mjs`: host metadata versions match; eleven playbooks; local Markdown references resolve; bundled endpoint is research-only and contains no credential headers.
- `python3 -m py_compile __init__.py`: native Hermes adapter compiles.
- OpenClaw **2026.10.4**, running on isolated **Node 24.16.0**: installed the local directory and inspected `govcon-ai` as an Agent Plugins bundle. Inspection reported loaded status, skills and MCP server capabilities, the `govcon` server and no diagnostics. No Gateway was started and no authenticated tool call was made.
- Installed Hermes source at commit `3e09adb109dca4159203bd9225b270dd83b5529c`: actual native plugin loader registered `govcon-ai:govcon-ai`, resolving to the shared `SKILL.md`; no tools, hooks or middleware were registered. Its portable loader separately parsed the manifest, skill and Streamable HTTP research server without diagnostics.

## Limitations and retained failures

- The local Hermes CLI reports `v0.20.0 (2026.8.3)` while its source contains newer portable-plugin code. The exact source commit above defines this check. This is not proof of compatibility with every unmodified 0.20.0 release. A compatibility floor is deliberately omitted pending validation against a current released Hermes build.
- That local CLI has no `plugins validate` subcommand. Current Hermes catalog validation is still a release gate.
- OpenClaw initially refused installation without capability consent. The same local package was then installed with explicit capability acceptance in the isolated test profile. The first refusal is preserved in the local QA receipt.
- The default machine Node is 22.23.2, below the OpenClaw package's declared engine requirement. Checks used a separate Node 24.16.0 runtime; no global Node or host was upgraded.
- OpenClaw's `--no-enable` install preserved config rather than forcing disabled status; fresh-profile inspection reported the bundle enabled by default. No Gateway was running, and no data connection or action was performed.
- G2X OAuth, actual tool discovery, a checked source result and catalog availability have not been verified in these hosts.

Repeat authenticated acceptance and current Hermes catalog validation before release. Keep package loading separate from connection and workflow proof.
