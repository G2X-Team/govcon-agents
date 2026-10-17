# Release checklist

The package is a review candidate, not a released plugin.

- Confirm G2X publisher ownership and preserve the repository's existing license.
- Review final positioning and setup copy with Ron before public launch.
- Validate portable manifest/MCP schemas and all reference paths.
- Verify the canonical skills source commit is approved for release; rebuild the vendored collection only from that clean pinned source.
- Load the OpenClaw bundle in an isolated profile on a pinned supported Node/host version.
- Load the Hermes native adapter and resolve its registered skill and reference files.
- On a supported current Hermes release, run `hermes plugins validate /path/to/govcon-agents --install-deps`. The older local CLI may not expose this command; that is a release gate, not a passing result.
- Verify G2X OAuth, tool discovery, one bounded research call and exact source links in each host with a designated test account. Do not sign in using Ron's saved production login.
- Confirm that the bundled OpenClaw research connection has no account-changing tools and that Hermes native config uses the intended endpoint.
- Complete independent technical review of the final commit; resolve P0/P1 findings.
- Create a complete release artifact. Run ClawHub's current publication dry run after confirming how portable bundles are accepted and the company publisher scope.
- Prepare Hermes catalog YAML from the approved commit. Use the full real SHA, current verified compatibility floor, description, maintainer and version. Do not submit placeholders or invent verified/official catalog status.
- Publish/submit only with the applicable launch authorization. Save actual release and catalog URLs, then verify the reader's install path from the live listing.

Keep package loading, authenticated connection, working research and public catalog availability as separate outcomes.
