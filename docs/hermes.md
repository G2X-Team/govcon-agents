# Government Contracting for Hermes

Hermes loads the native `plugin.yaml` and the small Python adapter in this package. The adapter registers the main Government Contracting skill and 24 focused workflows from the pinned local skill index. It does not change configuration, read credentials, add tools, install dependencies or create hooks. The portable `mcp.json` is consumed by OpenClaw, not by this Hermes native adapter.

## Review install

For an isolated local test, place the complete package under that profile's plugins directory and enable `government-contracting` through Hermes. For a Git install, use a reviewed repository revision following the current host's supported syntax. Do not advertise `hermes plugins install government-contracting` until a catalog listing exists.

```sh
hermes plugins list
hermes plugins enable government-contracting
```

Start a new session. Ask Hermes to use `skills_list`, then `skill_view` for the returned Government Contracting qualified name. Its reference files must stay next to `SKILL.md`.

## Connect G2X with native OAuth

First inspect existing `mcp_servers` entries and reuse an appropriate connection. G2X's current Hermes guide documents native OAuth with `cimd: false`. A research connection is:

```yaml
mcp_servers:
  govcon:
    url: https://mcp.g2x.com/mcp/research
    auth: oauth
    oauth:
      cimd: false
```

Merge this into the intended profile without replacing other settings, then run:

```sh
hermes mcp login govcon
hermes mcp test govcon
```

The person signs in through G2X. Keep credentials in host-managed storage. A remote host may need the callback/port-forward procedure in the official guide. For explicitly requested account actions, choose the full `https://mcp.g2x.com/mcp` connection and verify it separately. Account permissions and usage limits still apply.

## Acceptance

Verify skill discovery/loading, then complete one authenticated read-only query with a selected profile/query. Keep tool discovery, a successful request and a checked source record as separate proof. Do not call an install a working connection or test by changing an account.

## Hermes catalog submission

Submit a catalog entry only after an approved public commit exists and the current catalog validation passes. Pin the full 40-character commit, quote the version and declare accurate capabilities. The adapter registers a workflow skill only; no tools, hooks, middleware, environment secrets, self-updater or analytics. Hermes maintainers review and merge the entry. Prepared metadata and an opened PR are not listing approval.

- https://g2x.com/docs/connect/hermes
- https://hermes-agent.nousresearch.com/docs/developer-guide/plugins
- https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/catalog-submission
