import assert from 'node:assert/strict';
import { readFile, readdir, stat } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const manifest = JSON.parse(await readFile(join(root, 'plugin.json'), 'utf8'));
const mcp = JSON.parse(await readFile(join(root, 'mcp.json'), 'utf8'));
assert.equal(manifest.$schema, 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json');
assert.equal(mcp.$schema, 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json');
assert.equal(manifest.name, 'government-contracting');
assert.equal(mcp.mcpServers.govcon.type, 'streamable-http');
assert.equal(mcp.mcpServers.govcon.url, 'https://mcp.g2x.com/mcp/research');
assert.deepEqual(Object.keys(mcp.mcpServers.govcon).sort(), ['type', 'url']);
const yaml = await readFile(join(root, 'plugin.yaml'), 'utf8');
assert(yaml.includes(`version: "${manifest.version}"`), 'Host versions differ');
const files = [];
async function walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.') || entry.name === 'node_modules' || entry.name === '__pycache__') continue;
    const path = join(dir, entry.name);
    if (entry.isDirectory()) await walk(path);
    else if (entry.name.endsWith('.md')) files.push(path);
  }
}
await walk(root);
let links = 0;
for (const file of files) {
  const body = await readFile(file, 'utf8');
  for (const match of body.matchAll(/\]\(([^)]+)\)/g)) {
    const target = match[1].split('#')[0];
    if (!target || /^[a-z]+:/i.test(target)) continue;
    const path = resolve(dirname(file), target);
    assert(path.startsWith(root + '/'), `Link escapes package: ${file}: ${target}`);
    assert((await stat(path)).isFile(), `Missing reference: ${file}: ${target}`);
    links++;
  }
}
const catalog = JSON.parse(await readFile(join(root, 'skills-index.json'), 'utf8'));
assert.equal(catalog.source, 'https://github.com/G2X-Team/govcon-skills');
assert.match(catalog.commit, /^[a-f0-9]{40}$/);
assert.equal(catalog.skills.length, 25);
assert.equal(new Set(catalog.skills.map(x => x.name)).size, 25);
for (const skill of catalog.skills) {
  assert.match(skill.name, /^[a-z0-9]+(?:-[a-z0-9]+)*$/);
  const text = await readFile(join(root, 'skills', skill.name, 'SKILL.md'), 'utf8');
  assert(text.includes(`name: ${skill.name}\n`));
  assert.equal(createHash('sha256').update(text).digest('hex'), skill.sha256);
}
const dirs = (await readdir(join(root, 'skills'), { withFileTypes: true })).filter(x => x.isDirectory());
assert.equal(dirs.length, 25, 'Unexpected or stale skill folders in bundle');
console.log(JSON.stringify({ version: manifest.version, markdown_files: files.length,
  checked_local_links: links, skills: catalog.skills.length, source_commit: catalog.commit,
  research_endpoint: mcp.mcpServers.govcon.url }, null, 2));
