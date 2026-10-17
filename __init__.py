"""Hermes adapter: register the shared GovCon AI workflow skill only.

G2X sign-in and MCP connection settings belong to the host. This adapter does
not read credentials, alter host configuration, or launch an MCP process.
"""
from pathlib import Path


def register(ctx):
    ctx.register_skill(
        name="govcon-ai",
        path=Path(__file__).parent / "skills" / "govcon-ai" / "SKILL.md",
        description=(
            "Government contracting sales, business development and capture: "
            "company context, agency account plans, opportunities, incumbents, "
            "recompetes, teaming, solicitation review, meetings and pipeline decisions."
        ),
    )
