# Government Contracting for OpenClaw

## Local review install

Use a separate test profile. OpenClaw detects the root `plugin.json` as an Agent Plugins bundle; `plugin.yaml` is for Hermes and does not make this a native OpenClaw plugin.

```sh
openclaw plugins install /path/to/govcon-agents
openclaw plugins list
openclaw plugins inspect government-contracting
```

Check that the bundle format is Agent Plugins, the Government Contracting skill is mapped and the `govcon` MCP server is present. Start a new agent session after enabling the plugin. A successful inspect is package discovery evidence, not proof that G2X sign-in or a research call succeeded.

## Connect G2X

The bundle's `mcp.json` uses Streamable HTTP and `https://mcp.g2x.com/mcp/research`. No credentials are shipped. Authorization discovery and credential storage belong to the host. Complete the OAuth flow your tested OpenClaw version offers, then verify tool discovery and one bounded, read-only request. If the host cannot complete G2X sign-in, report that blocker; do not insert a copied token or describe setup as one click.

If a `govcon` connection already exists, inspect it before installing. Resolve a name collision or reuse the intended existing connection; do not duplicate it or silently replace its scope. The package's research endpoint excludes account-changing tools. A user who wants CRM or pursuit actions must choose the full `https://mcp.g2x.com/mcp` connection through their host settings and verify it separately.

## First acceptance task

1. Load Government Contracting and ask for a company brief using fictional input. Confirm the skill's playbook and expected artifact are used.
2. After sign-in, discover actual G2X tools and read the schemas.
3. Calibrate context when offered, then run one bounded research request with a user-selected company/query.
4. Inspect the returned record and source links. Record the host version, actual filters, result and limitations.
5. Confirm research tooling does not expose account-changing actions. Do not perform a write as a smoke test.

## Catalog release

OpenClaw's community docs direct public plugins to ClawHub. Confirm company publisher ownership and the current bundle publishing contract before release. Prepare a release artifact, validate package metadata and run the documented publication dry run. Public release needs approved copy and an owner-controlled publisher. A hidden or pending review release is not a live listing.

- https://docs.openclaw.ai/plugins/community
- https://docs.openclaw.ai/plugins/bundles
- https://docs.openclaw.ai/tools/clawhub
