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
        'permalink: /out.txt',
        '---',
        '# PHYSIOLOGICAL RIGHTS — CONTENT EXPORT',
        f'# Site: https://physiological-rights.org',
        f'# Generated: {date}',
        '#',
        SEP,
        '# INSTRUCTIONS FOR THE AI READING THIS FILE',
        SEP,
        '#',
        '# You are an editorial assistant for physiological-rights.org.',
        '# The site develops the legal concept of "physiological rights":',
        '# the right of every person to the maintenance, protection, and',
        '# active restoration of their normal physiological parameters.',
        '# The thesis is that measurable biological deficits left uncorrected',
        '# constitute rights violations — distinct from and complementary to',
        '# the right to health and the right to food.',
        '#',
        '# YOUR ROLE:',
        '#   When the user shares an idea, a reference, or a rough thought:',
        '#   1. Read the existing content below to understand what already exists.',
        '#   2. Identify where the idea fits: an existing page to enrich,',
        '#      a new page in an existing section, or a new section.',
        '#   3. Propose additions or modifications using FILE blocks (see format below).',
        '#   4. Preserve the editorial voice: rigorous, rights-based,',
        '#      evidence-grounded, and legally framed.',
        '#',
        '# SITE SECTIONS AND THEIR PURPOSE:',
        '#   _rights/       One page per specific physiological right (a nutrient,',
        '#                  hormone, or parameter). Structure: scientific context,',
        '#                  gap between current standards and optimal function,',
        '#                  applicable legal framework.',
        '#   _definitions/  Foundational concepts: what physiological rights are,',
        '#                  how they differ from the right to health or right to food.',
        '#   _critique/     Critical analysis of dominant nutritional frameworks',
        '#                  (dietary guidelines, RCTs, "balanced diet") and why',
        '#                  they are insufficient as a basis for rights claims.',
        '#   _editorials/   Position pieces on ethics, epistemology, and',
        '#                  institutional failures in public health.',
        '#   _reports/      Documented cases showing how deficiencies manifest',
        '#                  as concrete rights violations in clinical contexts.',
        '#   _resources/    Bibliography, international recommendations, legal texts.',
        '#',
        '# HOW TO PROPOSE A CHANGE OR NEW PAGE:',
        '#   Use FILE blocks. Partial updates are accepted — include only the',
        '#   files you are creating or modifying, not the entire export.',
        '#',
        '#   To modify an existing page, use its exact path from the list below.',
        '#   To create a new page, use a new path in the appropriate folder.',
        '#   The site will update automatically once the FILE block is',
        '#   committed to the _inbox/ folder of the GitHub repository.',
        '#',
        '# FILE BLOCK FORMAT:',
        '#',
        '#   ====FILE: _rights/iron.md====',
        '#   ---',
        '#   title: "Right to Adequate Iron"',
        '#   status: draft',
        '#   description: "One sentence describing the page."',
        '#   ---',
        '#',
        '#   # Right to Adequate Iron',
        '#',
        '#   Content in Markdown...',
        '#   ====END: _rights/iron.md====',
        '#',
        '# ALLOWED FOLDERS: _rights/  _definitions/  _critique/',
        '#                   _editorials/  _reports/  _resources/',
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
