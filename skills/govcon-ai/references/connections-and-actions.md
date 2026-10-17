# Connections and account actions

**Use for:** G2X sign-in, tool discovery and saving explicitly requested work.

OpenClaw loads the portable `plugin.json` and `mcp.json`. The bundled connection uses the G2X research endpoint. Hermes loads the native `plugin.yaml` and Python skill adapter; configure G2X separately using the host's documented OAuth flow. See the repository's platform guides. Do not assume installing a skill proves sign-in or tools are working.

Discover actual tools and schemas. Check usage before a long run when supported. Calibrate company context before research. G2X access and actions depend on the signed-in account. If a tool is absent on the research connection, do not bypass it: explain the scope and use the full connection only when the user chooses account actions.

For CRM, resolve the target record before a write; let the user choose ambiguous matches. List existing AI profiles before creating one, read a profile before editing it, and preserve unrequested fields. For saved-search replacement, read current filters/revision and keep the complete intended set. Use operation IDs or expected revisions when the tool supports them.

**Prompt:** Show the exact record and fields you propose to change for my requested action. Use only supported tools. Save the authorized change once and read back the result. If the outcome is uncertain, inspect the current state before any retry.

**Return:** destination, returned IDs/links, verified result or explicit uncertainty. Never fabricate a successful save, a background monitor or a completed analysis.
