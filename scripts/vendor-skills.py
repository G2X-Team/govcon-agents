"""Build-time copy of a clean, pinned G2X skills revision; never runs at install."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
source = Path(sys.argv[1]).resolve(strict=True)
origin = subprocess.check_output(['git','-C',str(source),'remote','get-url','origin'],text=True).strip()
if origin.lower().removesuffix('.git') not in {
    'https://github.com/g2x-team/govcon-skills', 'git@github.com:g2x-team/govcon-skills'
}:
    raise SystemExit('Expected the company-owned G2X-Team/govcon-skills source')
if subprocess.check_output(['git','-C',str(source),'status','--porcelain'],text=True).strip():
    raise SystemExit('Commit the source before vendoring')
sha = subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip()
entries = []
for entry in sorted((source/'skills').iterdir()):
    if entry.name == 'govcon-mcp' or not entry.is_dir():
        continue
    text = (entry/'SKILL.md').read_text()
    name = re.search(r'^name:\s*(\S+)\s*$',text,re.M)[1]
    description = re.search(r'^description:\s*(.+)$',text,re.M)[1]
    if name != entry.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name):
        raise SystemExit(f'Invalid skill identity: {entry.name}')
    destination = root/'skills'/name
    destination.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(entry/'SKILL.md', destination/'SKILL.md')
    entries.append({'name':name,'description':description,
                    'sha256':hashlib.sha256(text.encode()).hexdigest()})
if len(entries) != 25 or 'government-contracting' not in {x['name'] for x in entries}:
    raise SystemExit('Expected the umbrella and 24 focused workflows')
(root/'skills-index.json').write_text(json.dumps({
    'source':'https://github.com/G2X-Team/govcon-skills', 'commit':sha,
    'skills':entries},indent=2)+'\n')
print(f'Vendored {len(entries)} skills from {sha}; no runtime fetch or updater')
