#!/usr/bin/env python3
"""
Update index.html to point to split responsibility and vulnerability charts
"""

# Read the current index.html
with open('index.html', 'r') as f:
    content = f.read()

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

# Replace responsibility section
old_resp_section_title = '<div class="subsection-title">Responsibility Analysis</div>'
new_resp_section_title = '<div class="subsection-title">Responsibility Analysis - Part 1 (Required Actors)</div>'
content = content.replace(old_resp_section_title, new_resp_section_title)

# Replace all responsibility links to part1
for risk_num, _ in risks:
    old_link = f'href="qual_resp_charts/risk_{risk_num}_responsibility.html"'
    new_link = f'href="qual_resp_charts_split/risk_{risk_num}_responsibility_part1.html"'
    content = content.replace(old_link, new_link)

    old_type = '<div class="chart-type">Responsibility</div>'
    new_type = '<div class="chart-type">Responsibility - Part 1</div>'
    # This is trickier - need to replace within the responsibility section only
    # We'll do a more targeted approach

# Let's rebuild the responsibility section properly
resp_section_start = content.find('<div class="subsection-title">Responsibility Analysis - Part 1 (Required Actors)</div>')
resp_section_end = content.find('</div>\n        </div>\n\n        <div class="subsection">', resp_section_start)

# Build new responsibility sections (both part 1 and part 2)
resp_html = '''<div class="subsection-title">Responsibility Analysis - Part 1 (Required Actors)</div>
            <div class="chart-grid">
'''

for risk_num, risk_name in risks:
    resp_html += f'''                <a href="qual_resp_charts_split/risk_{risk_num}_responsibility_part1.html" class="chart-link">
                    <div class="risk-num">{risk_num.replace("_", ".")} {risk_name}</div>
                    <div class="chart-type">Responsibility - Part 1</div>
                </a>
'''

resp_html += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Responsibility Analysis - Part 2 (Optional Actors)</div>
            <div class="chart-grid">
'''

for risk_num, risk_name in risks:
    resp_html += f'''                <a href="qual_resp_charts_split/risk_{risk_num}_responsibility_part2.html" class="chart-link">
                    <div class="risk-num">{risk_num.replace("_", ".")} {risk_name}</div>
                    <div class="chart-type">Responsibility - Part 2</div>
                </a>
'''

resp_html += '''            </div>'''

# Replace the responsibility section
content = content[:resp_section_start] + resp_html + content[resp_section_end:]

# Now do the same for vulnerability (actors)
vuln_section_start = content.find('<div class="subsection-title">Vulnerability Analysis (Actors)</div>')
vuln_section_end = content.find('</div>\n        </div>\n\n        <div class="subsection">', vuln_section_start)

vuln_html = '''<div class="subsection-title">Vulnerability Analysis (Actors) - Part 1 (Required Actors)</div>
            <div class="chart-grid">
'''

for risk_num, risk_name in risks:
    vuln_html += f'''                <a href="qual_vuln_charts_actors_split/risk_{risk_num}_vulnerability_actors_part1.html" class="chart-link">
                    <div class="risk-num">{risk_num.replace("_", ".")} {risk_name}</div>
                    <div class="chart-type">Actor Vulnerability - Part 1</div>
                </a>
'''

vuln_html += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Actors) - Part 2 (Optional Actors)</div>
            <div class="chart-grid">
'''

for risk_num, risk_name in risks:
    vuln_html += f'''                <a href="qual_vuln_charts_actors_split/risk_{risk_num}_vulnerability_actors_part2.html" class="chart-link">
                    <div class="risk-num">{risk_num.replace("_", ".")} {risk_name}</div>
                    <div class="chart-type">Actor Vulnerability - Part 2</div>
                </a>
'''

vuln_html += '''            </div>'''

# Replace the vulnerability section
content = content[:vuln_section_start] + vuln_html + content[vuln_section_end:]

# Write the updated content
with open('index.html', 'w') as f:
    f.write(content)

print("Updated index.html successfully!")
print("\nAdded:")
print("- Responsibility Analysis - Part 1 (Required Actors)")
print("- Responsibility Analysis - Part 2 (Optional Actors)")
print("- Vulnerability Analysis (Actors) - Part 1 (Required Actors)")
print("- Vulnerability Analysis (Actors) - Part 2 (Optional Actors)")
