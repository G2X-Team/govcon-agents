"""Hermes adapter: register the pinned Government Contracting skills only.

G2X sign-in and MCP connection settings belong to the host. This adapter does
not read credentials, alter host configuration, or launch an MCP process.
"""
from pathlib import Path
import json


def register(ctx):
    root = Path(__file__).resolve().parent
    catalog = json.loads((root / "skills-index.json").read_text())
    for skill in catalog["skills"]:
        path = (root / "skills" / skill["name"] / "SKILL.md").resolve()
        if not path.is_relative_to(root / "skills"):
            raise ValueError("Skill path must stay inside the package")
        ctx.register_skill(name=skill["name"], path=path, description=skill["description"])
