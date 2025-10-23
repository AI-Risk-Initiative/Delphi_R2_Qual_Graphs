#!/usr/bin/env python3
"""
Script to split sector vulnerability HTML files into 4 groups:
- Group 1: Agriculture/Mining/Construction/Manufacturing, Trade/Transportation/Utilities, Information, Finance and Insurance
- Group 2: Real Estate and Rental and Leasing, Professional and Technical Services, Scientific Services, Management/Administrative/Support Services
- Group 3: Educational Services, Health Care and Social Assistance, Arts/Entertainment/Recreation, Accommodation/Food/Other Services
- Group 4: Public Administration excluding National Security, National Security
"""

import os
import re
from pathlib import Path

# Define sector groups
GROUP_1_SECTORS = [
    "AgricultureMiningConstructionManufacturing",
    "TradeTransportationUtilities",
    "Information",
    "FinanceandInsurance"
]

GROUP_1_LABELS = [
    "Agriculture Mining Construction Manufacturing",
    "Trade Transportation Utilities",
    "Information",
    "Finance and Insurance"
]

GROUP_2_SECTORS = [
    "RealEstateRentalLeasing",
    "ProfessionalandTechnicalServices",
    "ScientificServices",
    "ManagementAdministrativeSupportServices"
]

GROUP_2_LABELS = [
    "Real Estate Rental Leasing",
    "Professional and Technical Services",
    "Scientific Services",
    "Management Administrative Support Services"
]

GROUP_3_SECTORS = [
    "EducationalServices",
    "HealthCareandSocialAssistance",
    "ArtsEntertainmentRecreation",
    "AccommodationFoodOtherServices"
]

GROUP_3_LABELS = [
    "Educational Services",
    "Health Care and Social Assistance",
    "Arts Entertainment Recreation",
    "Accommodation Food Other Services"
]

GROUP_4_SECTORS = [
    "PublicAdministrationexcludingNationalSecurity",
    "NationalSecurity"
]

GROUP_4_LABELS = [
    "Public Administration excluding National Security",
    "National Security"
]

def process_file(input_path, output_dir, group_num, sector_ids, sector_labels):
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

    # Build new nav pills with only selected sectors
    new_pills = []
    for i, (sector_id, label) in enumerate(zip(sector_ids, sector_labels)):
        active_class = ' active' if i == 0 else ''
        pill = f'''            <button class="nav-pill{active_class}" data-target="{sector_id}">
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

    # Find and keep only selected sector sections
    section_class = 'entity-section'

    # Extract all sections
    all_sections = []

    for sector_id in sector_ids:
        # Find the section for this sector
        pattern = f'<div class="{section_class}.*?" id="{sector_id}">'
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
            if sector_id == sector_ids[0]:
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

    # Process sector vulnerability charts
    vuln_input_dir = base_dir / 'qual_vuln_charts_sectors'
    vuln_output_dir = base_dir / 'qual_vuln_charts_sectors_split'
    vuln_output_dir.mkdir(exist_ok=True)

    print("Processing sector vulnerability charts...")
    for html_file in vuln_input_dir.glob('*.html'):
        process_file(html_file, vuln_output_dir, 1, GROUP_1_SECTORS, GROUP_1_LABELS)
        process_file(html_file, vuln_output_dir, 2, GROUP_2_SECTORS, GROUP_2_LABELS)
        process_file(html_file, vuln_output_dir, 3, GROUP_3_SECTORS, GROUP_3_LABELS)
        process_file(html_file, vuln_output_dir, 4, GROUP_4_SECTORS, GROUP_4_LABELS)

    print("\nDone!")
    print(f"\nGroup 1 ({len(GROUP_1_SECTORS)} sectors): {', '.join(GROUP_1_LABELS)}")
    print(f"Group 2 ({len(GROUP_2_SECTORS)} sectors): {', '.join(GROUP_2_LABELS)}")
    print(f"Group 3 ({len(GROUP_3_SECTORS)} sectors): {', '.join(GROUP_3_LABELS)}")
    print(f"Group 4 ({len(GROUP_4_SECTORS)} sectors): {', '.join(GROUP_4_LABELS)}")

if __name__ == '__main__':
    main()
