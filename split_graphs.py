#!/usr/bin/env python3
"""
Script to split responsibility and vulnerability HTML files into two sets:
- Set 1: 4 required actors
- Set 2: 3 optional actors
"""

import os
import re
from pathlib import Path

# Define actor groups
GROUP_1_ACTORS = [
    "AIDeveloperGeneralpurposeAI",
    "AIDeployer",
    "AIGovernanceActor",
    "AIUser"
]

GROUP_1_LABELS = [
    "AI Developer (General-purpose AI)",
    "AI Deployer",
    "AI Governance Actor",
    "AI User"
]

GROUP_2_ACTORS = [
    "AIDeveloperSpecializedAI",
    "AIInfrastructureProvider",
    "AffectedStakeholder"
]

GROUP_2_LABELS = [
    "AI Developer (Specialized AI)",
    "AI Infrastructure Provider",
    "Affected Stakeholder"
]

def process_file(input_path, output_dir, group_num, actor_ids, actor_labels):
    """Process a single HTML file and create split version"""

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the title
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        original_title = title_match.group(1)
        new_title = f"{original_title} - Part {group_num}"
        content = content.replace(f'<title>{original_title}</title>',
                                f'<title>{new_title}</title>')

        # Also update h1
        h1_match = re.search(r'<h1>(.*?)</h1>', content)
        if h1_match:
            original_h1 = h1_match.group(1)
            new_h1 = f"{original_h1} - Part {group_num}"
            content = content.replace(f'<h1>{original_h1}</h1>',
                                    f'<h1>{new_h1}</h1>')

    # Extract nav pills section
    nav_start = content.find('<div class="nav-pills">')
    nav_end = content.find('</div>', nav_start)

    # Build new nav pills with only selected actors
    new_pills = []
    for i, (actor_id, label) in enumerate(zip(actor_ids, actor_labels)):
        active_class = ' active' if i == 0 else ''
        pill = f'''            <button class="nav-pill{active_class}" data-target="{actor_id}">
                {label}
            </button>'''
        new_pills.append(pill)

    new_nav = f'''        <div class="nav-pills">
{chr(10).join(new_pills)}
        </div>'''

    # Replace nav pills section
    content = content[:nav_start] + new_nav + content[nav_end + 6:]

    # Extract content sections
    sections_start = content.find('<div class="content-sections">')
    sections_end = content.find('</div>', content.find('</div>',
                                content.find('</div>', sections_start) + 1) + 1)

    # Find and keep only selected actor sections
    # For responsibility files, look for actor-section
    # For vulnerability files, look for entity-section
    section_class = 'actor-section' if 'responsibility' in str(input_path) else 'entity-section'

    # Extract all sections
    all_sections = []
    temp_content = content[sections_start:sections_end]

    for actor_id in actor_ids:
        # Find the section for this actor
        pattern = f'<div class="{section_class}.*?" id="{actor_id}">'
        match = re.search(pattern, content)
        if match:
            section_start = match.start()
            # Find the end of this section (next </div> that closes the main section div)
            section_text = content[section_start:]
            depth = 0
            pos = 0
            for i, char in enumerate(section_text):
                if section_text[i:i+4] == '<div':
                    depth += 1
                elif section_text[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        pos = i + 6
                        break

            section_html = section_text[:pos]
            # Make first section active
            if actor_id == actor_ids[0]:
                section_html = section_html.replace(f'class="{section_class}"',
                                                   f'class="{section_class} active"')
            else:
                section_html = section_html.replace(f'class="{section_class} active"',
                                                   f'class="{section_class}"')
            all_sections.append(section_html)

    # Build new content sections
    new_sections = f'''        <div class="content-sections">
{chr(10).join(all_sections)}
        </div>'''

    # Replace content sections
    content = content[:sections_start] + new_sections + content[sections_end + 6:]

    # Create output filename
    input_name = os.path.basename(input_path)
    output_name = input_name.replace('.html', f'_part{group_num}.html')
    output_path = os.path.join(output_dir, output_name)

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created: {output_path}")

def main():
    base_dir = Path(__file__).parent

    # Process responsibility charts
    resp_input_dir = base_dir / 'qual_resp_charts'
    resp_output_dir = base_dir / 'qual_resp_charts_split'
    resp_output_dir.mkdir(exist_ok=True)

    print("Processing responsibility charts...")
    for html_file in resp_input_dir.glob('*.html'):
        process_file(html_file, resp_output_dir, 1, GROUP_1_ACTORS, GROUP_1_LABELS)
        process_file(html_file, resp_output_dir, 2, GROUP_2_ACTORS, GROUP_2_LABELS)

    # Process vulnerability charts
    vuln_input_dir = base_dir / 'qual_vuln_charts_actors'
    vuln_output_dir = base_dir / 'qual_vuln_charts_actors_split'
    vuln_output_dir.mkdir(exist_ok=True)

    print("\nProcessing vulnerability charts...")
    for html_file in vuln_input_dir.glob('*.html'):
        process_file(html_file, vuln_output_dir, 1, GROUP_1_ACTORS, GROUP_1_LABELS)
        process_file(html_file, vuln_output_dir, 2, GROUP_2_ACTORS, GROUP_2_LABELS)

    print("\nDone!")

if __name__ == '__main__':
    main()
