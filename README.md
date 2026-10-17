# GovCon AI by G2X

Government contracting sales, business development and capture workflows for your AI agent.

Build agency account plans, screen opportunities, research incumbents and potential recompetes, evaluate teaming partners, read solicitations, prepare meetings and turn pursuit reviews into clear next steps. The package helps your agent produce useful work with evidence from the sources you authorize.

G2X supplies government market intelligence. GovCon MCP connects that intelligence and supported account actions to your agent. The playbooks also work with approved files and public sources; installing them does not grant data access or turn on ongoing monitoring.

## What is included

One entry skill routes to eleven focused playbooks:

- Company brief and target-market context
- Agency account plans
- Opportunity screening
- Incumbent and competitor research
- Potential recompete watch
- Teaming-partner diligence
- Solicitation and amendment review
- Capture plans and decision memos
- Meetings and industry days
- Pipeline decisions and follow-up
- Connections and requested account actions

Each playbook defines the inputs, method, a copyable prompt and the expected deliverable. Facts, hypotheses, missing information and proposed actions stay distinct.

## Choose your host

| Host | Package loaded | G2X connection |
| --- | --- | --- |
| OpenClaw | Portable Agent Plugins v1: root `plugin.json`, `skills/` and `mcp.json` | Research endpoint declared in the bundle; host-managed sign-in must be completed and verified |
| Hermes | Native `plugin.yaml` and `__init__.py`; registers the same workflow skill | Configure the host's native MCP OAuth connection separately |

See [OpenClaw setup](docs/openclaw.md) and [Hermes setup](docs/hermes.md).

## Try a workflow

Ask your host to load the GovCon AI skill, then try:

> Turn this company capability statement into a company brief. Separate supported claims from gaps. Then help me choose three buying offices to research, with evidence and a next question for each. Draft only.

Or:

> Review this opportunity and the available solicitation documents against our confirmed company brief. Produce a shortlist of fit evidence, conflicts and unknowns with sources. Do not start paid analysis, change records or contact anyone.

For Hermes, use `skills_list` to discover the exact qualified skill name and `skill_view` to load it. For OpenClaw, inspect the installed bundle and confirm its skills are available in a new session. The presence of a skill does not establish a successful data connection.

## Evidence and account actions

Keep original record links, document versions and dates with the work. A search sample is not a market total, an expiring award is not a confirmed recompete and a requirements extraction is not a compliance decision. Check the controlling notice and complete document set before a contracting decision.

Research and drafts do not authorize messages, publication, purchases or account changes. A specific user request can authorize a bounded action, subject to the host's controls. Resolve ambiguous identities and destinations, preserve unrelated values and read back applied changes. The research endpoint excludes account-changing tools.

## Development status

Version 0.1.0 is a review candidate. Catalog publication, authenticated host acceptance and release approval are separate from local loading tests. See [release checklist](docs/release-checklist.md). Do not claim a catalog listing or advertise a by-name catalog install until it exists.

## References

- [G2X tools and connection documentation](https://g2x.com/mcp)
- [Existing G2X workflow skills](https://github.com/G2X-Team/govcon-skills)
- [Agent Plugins specification](https://agent-plugins.org/specification)
- [OpenClaw plugin bundles](https://docs.openclaw.ai/plugins/bundles)
- [Hermes plugin development](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)

The repository's existing license is unchanged.
