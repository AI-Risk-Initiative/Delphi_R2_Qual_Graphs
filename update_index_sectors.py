#!/usr/bin/env python3
"""
Update index.html to add split sector vulnerability charts
"""

# Risk numbers and names
risks = [
    ("1_1", "Unfair discrimination and misrepresentation"),
    ("1_2", "Exposure to toxic content"),
    ("1_3", "Unequal performance across groups"),
    ("2_1", "Compromise of privacy by obtaining, leaking or correctly inferring sensitive information"),
    ("2_2", "AI system security vulnerabilities and attacks"),
    ("3_1", "Pollution of information ecosystem and loss of consensus reality"),
    ("3_2", "False or misleading information"),
    ("4_1", "Disinformation, surveillance, and influence at scale"),
    ("4_2", "Fraud, scams, and targeted manipulation"),
    ("4_3", "Cyberattacks, weapon development or use, and mass harm"),
    ("5_1", "Overreliance and unsafe use"),
    ("5_2", "Loss of human agency and autonomy"),
    ("6_1", "Power centralization and unfair distribution of benefits"),
    ("6_2", "Increased inequality and decline in employment quality"),
    ("6_3", "Economic and cultural devaluation of human effort"),
    ("6_4", "Competitive dynamics"),
    ("6_5", "Governance failure"),
    ("6_6", "Environmental harm"),
    ("7_1", "AI pursuing its own goals in conflict with human goals or values"),
    ("7_2", "AI possessing dangerous capabilities"),
    ("7_3", "Lack of capability or robustness"),
    ("7_4", "Lack of transparency or interpretability"),
    ("7_5", "AI welfare and rights"),
    ("7_6", "Multi-agent risks"),
]

# Read the current index.html
with open('index.html', 'r') as f:
    content = f.read()

# Find the sector vulnerability section
sector_section_start = content.find('<div class="subsection-title">Vulnerability Analysis (Sectors)</div>')
sector_section_end = content.find('</div>\n    </div>\n\n</body>', sector_section_start)

# Build new sector sections (4 parts)
sector_html = '''<div class="subsection-title">Vulnerability Analysis (Sectors) - Part 1</div>
            <p class="section-description" style="font-size: 12px; margin-bottom: 15px;">Agriculture/Mining/Construction/Manufacturing, Trade/Transportation/Utilities, Information, Finance and Insurance</p>
            <div class="chart-grid">
'''

for risk_num, risk_name in risks:
    sector_html += f'''                <a href="qual_vuln_charts_sectors_split/risk_{risk_num}_vulnerability_sectors_part1.html" class="chart-link">
                    <div class="risk-num">{risk_num.replace("_", ".")} {risk_name}</div>
                    <div class="chart-type">Sector Vulnerability - Part 1</div>
                </a>
'''

sector_html += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Sectors) - Part 2</div>
            <p class="section-description" style="font-size: 12px; margin-bottom: 15px;">Real Estate and Rental and Leasing, Professional and Technical Services, Scientific Services, Management/Administrative/Support Services</p>
            <div class="chart-grid">
'''

for risk_num, risk_name in risks:
    sector_html += f'''                <a href="qual_vuln_charts_sectors_split/risk_{risk_num}_vulnerability_sectors_part2.html" class="chart-link">
                    <div class="risk-num">{risk_num.replace("_", ".")} {risk_name}</div>
                    <div class="chart-type">Sector Vulnerability - Part 2</div>
                </a>
'''

sector_html += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Sectors) - Part 3</div>
            <p class="section-description" style="font-size: 12px; margin-bottom: 15px;">Educational Services, Health Care and Social Assistance, Arts/Entertainment/Recreation, Accommodation/Food/Other Services</p>
            <div class="chart-grid">
'''

for risk_num, risk_name in risks:
    sector_html += f'''                <a href="qual_vuln_charts_sectors_split/risk_{risk_num}_vulnerability_sectors_part3.html" class="chart-link">
                    <div class="risk-num">{risk_num.replace("_", ".")} {risk_name}</div>
                    <div class="chart-type">Sector Vulnerability - Part 3</div>
                </a>
'''

sector_html += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Sectors) - Part 4</div>
            <p class="section-description" style="font-size: 12px; margin-bottom: 15px;">Public Administration excluding National Security, National Security</p>
            <div class="chart-grid">
'''

for risk_num, risk_name in risks:
    sector_html += f'''                <a href="qual_vuln_charts_sectors_split/risk_{risk_num}_vulnerability_sectors_part4.html" class="chart-link">
                    <div class="risk-num">{risk_num.replace("_", ".")} {risk_name}</div>
                    <div class="chart-type">Sector Vulnerability - Part 4</div>
                </a>
'''

sector_html += '''            </div>'''

# Replace the sector section
content = content[:sector_section_start] + sector_html + content[sector_section_end:]

# Write the updated content
with open('index.html', 'w') as f:
    f.write(content)

print("Updated index.html successfully!")
print("\nAdded sector vulnerability sections:")
print("- Part 1: Agriculture/Mining/Construction/Manufacturing, Trade/Transportation/Utilities, Information, Finance and Insurance")
print("- Part 2: Real Estate and Rental and Leasing, Professional and Technical Services, Scientific Services, Management/Administrative/Support Services")
print("- Part 3: Educational Services, Health Care and Social Assistance, Arts/Entertainment/Recreation, Accommodation/Food/Other Services")
print("- Part 4: Public Administration excluding National Security, National Security")
