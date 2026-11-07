#!/usr/bin/env python3
"""Validate generated Gemini payload integrity without running tools or jobs."""

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT_FILES = {
    'gemini-extension.json', 'GEMINI.md', 'LICENSE', 'skills-source.lock.json',
}


def validate(root=ROOT):
    root = Path(root).resolve()
    lock = json.loads((root / 'bundle-source.lock.json').read_text(encoding='utf-8'))
    if lock['repository'] != 'https://github.com/fal-ai-community/skills':
        raise ValueError('Unexpected canonical source repository')
    if not re.fullmatch(r'[0-9a-f]{40}', lock['commit']):
        raise ValueError('A full canonical Git commit is required')
    expected = lock['files']
    actual = {p.relative_to(root).as_posix() for p in (root / 'skills').rglob('*') if p.is_file()}
    actual.update(GENERATED_ROOT_FILES)
    if set(expected) != actual:
        raise ValueError('Generated file set differs from source lock')
    for relative, digest in expected.items():
        path = root / relative
        if not path.resolve().is_relative_to(root) or path.is_symlink():
            raise ValueError(f'Unsafe generated file: {relative}')
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError(f'Generated file differs from source: {relative}')

    manifest = json.loads((root / 'gemini-extension.json').read_text(encoding='utf-8'))
    if manifest['name'] != 'fal-ai' or manifest['contextFileName'] != 'GEMINI.md':
        raise ValueError('Unexpected Gemini extension identity or context')
    if manifest['mcpServers'] != {'fal': {'httpUrl': 'https://mcp.fal.ai/mcp-relay'}}:
        raise ValueError('Expected the public hosted fal connection without credentials or approval overrides')
    if any(key in manifest for key in ['settings', 'excludeTools']):
        raise ValueError('Unexpected extension settings or tool overrides')
    if any((root / name).exists() for name in ['hooks', 'policies', 'package.json']):
        raise ValueError('Unexpected startup or executable package configuration')

    index = json.loads((root / 'skills/index.json').read_text(encoding='utf-8'))
    source = json.loads((root / 'skills-source.lock.json').read_text(encoding='utf-8'))
    if source['commit'] != lock['commit'] or source['profile'] != 'gemini':
        raise ValueError('Canonical source and Gemini profile locks disagree')
    if hashlib.sha256(json.dumps(index, sort_keys=True).encode()).hexdigest() != source['registry_sha256']:
        raise ValueError('Skill registry hash differs from source lock')
    indexed = {'skills/index.json'}
    for skill in index['skills']:
        for item in skill['files']:
            relative = f'skills/{skill["name"]}/{item["path"]}'
            path = root / relative
            if not path.resolve().is_relative_to(root / 'skills'):
                raise ValueError('Skill index contains an unsafe path')
            content = path.read_bytes()
            if len(content) != item['bytes'] or hashlib.sha256(content).hexdigest() != item['sha256']:
                raise ValueError(f'Skill index content mismatch: {relative}')
            indexed.add(relative)
    if indexed != {p for p in actual if p.startswith('skills/')}:
        raise ValueError('Skill index omits or invents payload files')
    return len(index['skills']), len(expected)


if __name__ == '__main__':
    count, files = validate()
    print(f'Validated {count} skills and {files} generated files; no tools or jobs executed')
