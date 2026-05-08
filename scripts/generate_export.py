#!/usr/bin/env python3
"""Generate a single-file export of all site content for AI-assisted editing."""

import os
import glob
from datetime import datetime, timezone

COLLECTIONS = [
    ('_rights',      'Specific Physiological Rights'),
    ('_definitions', 'Core Definitions'),
    ('_critique',    'Nutritional Critique'),
    ('_editorials',  'Editorials'),
    ('_reports',     'Case Reports'),
    ('_resources',   'Resources'),
]

SEP = '=' * 72


def generate_export():
    date = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    lines = [
        '---',
        'layout: none',
        'permalink: /out/',
        '---',
        '# PHYSIOLOGICAL RIGHTS — CONTENT EXPORT',
        f'# Site: https://physiological-rights.org',
        f'# Generated: {date}',
        '#',
        '# HOW TO USE THIS FILE:',
        '#   Read and analyze all content below in your AI of choice.',
        '#   To propose additions or edits, create a file containing only',
        '#   the changed FILE blocks and commit it to _inbox/',
        '#',
        '# INBOX FORMAT (partial updates accepted):',
        '#',
        '#   [FILE: _rights/new-page.md]',
        '#   ---',
        '#   title: "New Page"',
        '#   status: draft',
        '#   ---',
        '#   Content here...',
        '#   [END: _rights/new-page.md]',
        '#',
        '# ALLOWED FOLDERS: _rights/ _definitions/ _critique/',
        '#                   _editorials/ _reports/ _resources/',
        '#',
        SEP,
        '',
    ]

    for folder, section_title in COLLECTIONS:
        if not os.path.isdir(folder):
            continue
        files = sorted(glob.glob(f'{folder}/*.md'))
        if not files:
            continue

        lines.append(SEP)
        lines.append(f'# {section_title}')
        lines.append(SEP)
        lines.append('')

        for filepath in files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            lines.append(f'====FILE: {filepath}====')
            lines.append(content.rstrip('\n'))
            lines.append(f'====END: {filepath}====')
            lines.append('')

    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    os.makedirs('out', exist_ok=True)
    export = generate_export()
    output_path = 'out/index.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(export)
    size_kb = len(export.encode('utf-8')) / 1024
    print(f'Export generated: {output_path} ({size_kb:.1f} KB)')
