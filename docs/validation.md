# Validation record

Checked October 17, 2026. These are package and loader checks, not a public release or an authenticated G2X workflow.

## Passed

- `node scripts/validate.mjs`: manifest versions match, all 25 skills match their pinned source hashes and local links resolve. The bundled connection is research-only and contains no credentials or executable command.
- `python3 -m py_compile __init__.py scripts/vendor-skills.py`: adapter and build script compile.
- Build-time vendoring copied the umbrella and 24 focused skills from clean source commit `32654396c774b88606f2a9735594005439ecc315` in `G2X-Team/govcon-skills`. No remote fetch or self-updater runs at installation or runtime.
- OpenClaw **2026.10.4** on isolated **Node 24.16.0** installed and inspected `government-contracting` as an Agent Plugins bundle: loaded status, skills/MCP capabilities and no diagnostics. Its actual skills listing discovered all 25 expected skills.
- Installed Hermes source at commit `3e09adb109dca4159203bd9225b270dd83b5529c`: the native loader registered and resolved all 25 `government-contracting:<skill>` entries. No tools, hooks or middleware were registered. Its portable parser separately accepted all 25 skills and the Streamable HTTP research connection without diagnostics.
- The canonical skills source passed validation for 26 folders including the compatible entry; skills.sh CLI installed a focused skill alone in an isolated project. The source has an independent Codex approval at its pinned commit.

## Limitations and retained failures

- The local Hermes CLI reports `v0.20.0 (2026.8.3)` while its source contains newer portable-plugin code. The exact source commit above defines this check. This is not proof of compatibility with every unmodified 0.20.0 release. A compatibility floor is deliberately omitted pending validation against a current released Hermes build.
- That local CLI has no `plugins validate` subcommand. Current Hermes catalog validation is still a release gate.
- OpenClaw initially refused installation without capability consent. The same local package was then installed with explicit capability acceptance in the isolated test profile. The first refusal is preserved in the local QA receipt.
- The default machine Node is 22.23.2, below the OpenClaw package's declared engine requirement. Checks used a separate Node 24.16.0 runtime; no global Node or host was upgraded.
- OpenClaw's `--no-enable` install preserved config rather than forcing disabled status; fresh-profile inspection reported the bundle enabled by default. No Gateway was running, and no data connection or action was performed.
- G2X OAuth, actual tool discovery, a checked source result and catalog availability have not been verified in these hosts.
- Earlier `govcon-ai` prototype loading and review receipts predate this shared collection and new identifier. They do not replace final-revision review.

Repeat authenticated acceptance and current Hermes catalog validation before release. Keep package loading separate from connection and workflow proof.
