#!/usr/bin/env python3
"""
Update index.html to use new riskN naming convention
"""

# Mapping from number to risk code (for display)
risk_mapping = {
    "1": "1.1",
    "2": "1.2",
    "3": "1.3",
    "4": "2.1",
    "5": "2.2",
    "6": "3.2",  # SWAPPED
    "7": "3.1",  # SWAPPED
    "8": "4.1",
    "9": "4.3",  # SWAPPED
    "10": "4.2", # SWAPPED
    "11": "5.1",
    "12": "5.2",
    "13": "6.1",
    "14": "6.2",
    "15": "6.3",
    "16": "6.4",
    "17": "6.5",
    "18": "6.6",
    "19": "7.1",
    "20": "7.2",
    "21": "7.3",
    "22": "7.4",
    "23": "7.5",
    "24": "7.6"
}

# Risk names
risk_names = {
    "1.1": "Unfair discrimination and misrepresentation",
    "1.2": "Exposure to toxic content",
    "1.3": "Unequal performance across groups",
    "2.1": "Compromise of privacy by obtaining, leaking or correctly inferring sensitive information",
    "2.2": "AI system security vulnerabilities and attacks",
    "3.1": "Pollution of information ecosystem and loss of consensus reality",
    "3.2": "False or misleading information",
    "4.1": "Disinformation, surveillance, and influence at scale",
    "4.2": "Fraud, scams, and targeted manipulation",
    "4.3": "Cyberattacks, weapon development or use, and mass harm",
    "5.1": "Overreliance and unsafe use",
    "5.2": "Loss of human agency and autonomy",
    "6.1": "Power centralization and unfair distribution of benefits",
    "6.2": "Increased inequality and decline in employment quality",
    "6.3": "Economic and cultural devaluation of human effort",
    "6.4": "Competitive dynamics",
    "6.5": "Governance failure",
    "6.6": "Environmental harm",
    "7.1": "AI pursuing its own goals in conflict with human goals or values",
    "7.2": "AI possessing dangerous capabilities",
    "7.3": "Lack of capability or robustness",
    "7.4": "Lack of transparency or interpretability",
    "7.5": "AI welfare and rights",
    "7.6": "Multi-agent risks",
}

# Read the current index.html
with open('index.html', 'r') as f:
    content = f.read()

# Build the complete new content
new_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delphi Round 2 - Qualitative Analysis Charts</title>
    <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Figtree', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f5f5f5;
            color: #333;
        }
        h1 {
            color: #000;
            text-align: center;
            margin-bottom: 10px;
            font-size: 36px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
            font-size: 18px;
        }
        .section {
            background: white;
            border-radius: 8px;
            border: 2px solid #000;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .section-title {
            background: #000;
            color: white;
            padding: 12px 20px;
            margin: -30px -30px 20px -30px;
            font-size: 22px;
            font-weight: 600;
            border-radius: 6px 6px 0 0;
        }
        .section-description {
            color: #666;
            margin-bottom: 20px;
            font-size: 14px;
            line-height: 1.6;
        }
        .chart-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 15px;
        }
        .chart-link {
            display: block;
            padding: 15px 20px;
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 6px;
            text-decoration: none;
            color: #333;
            transition: all 0.2s;
            font-weight: 500;
        }
        .chart-link:hover {
            background: #a32035;
            color: white;
            border-color: #a32035;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(163, 32, 53, 0.2);
        }
        .chart-link .risk-num {
            font-weight: 700;
            font-size: 16px;
        }
        .chart-link .chart-type {
            font-size: 12px;
            color: #666;
            margin-top: 4px;
        }
        .chart-link:hover .chart-type {
            color: rgba(255, 255, 255, 0.8);
        }
        .subsection {
            margin-bottom: 30px;
        }
        .subsection:last-child {
            margin-bottom: 0;
        }
        .subsection-title {
            font-size: 18px;
            font-weight: 600;
            color: #a32035;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #a32035;
        }
    </style>
</head>
<body>
    <h1>Delphi Round 2 Qualitative Analysis Charts</h1>
    <p class="subtitle">Expert Comments on AI Risks: Responsibility, Severity, and Vulnerability</p>

    <!-- Qualitative Analysis Section -->
    <div class="section">
        <div class="section-title">Qualitative Expert Comments</div>
        <p class="section-description">Structured qualitative analysis of expert comments across 24 AI risks. Charts display expert reasoning on responsibility attribution, severity assessment, and vulnerability analysis for different actors and sectors.</p>

        <div class="subsection">
            <div class="subsection-title">Responsibility Analysis - Part 1 (Required Actors)</div>
            <div class="chart-grid">
'''

# Add responsibility part 1 links
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    new_content += f'''                <a href="qual_resp_charts_split/risk{num}_responsibility_part1.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Responsibility - Part 1</div>
                </a>
'''

new_content += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Responsibility Analysis - Part 2 (Optional Actors)</div>
            <div class="chart-grid">
'''

# Add responsibility part 2 links
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    new_content += f'''                <a href="qual_resp_charts_split/risk{num}_responsibility_part2.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Responsibility - Part 2</div>
                </a>
'''

new_content += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Severity Analysis</div>
            <div class="chart-grid">
'''

# Add severity links (these weren't split, keep original naming)
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    risk_file = risk_code.replace(".", "_")
    new_content += f'''                <a href="qual_severity_charts/risk_{risk_file}_severity.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Severity</div>
                </a>
'''

new_content += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Actors) - Part 1 (Required Actors)</div>
            <div class="chart-grid">
'''

# Add vulnerability actors part 1 links
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    new_content += f'''                <a href="qual_vuln_charts_actors_split/risk{num}_vulnerability_actors_part1.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Actor Vulnerability - Part 1</div>
                </a>
'''

new_content += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Actors) - Part 2 (Optional Actors)</div>
            <div class="chart-grid">
'''

# Add vulnerability actors part 2 links
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    new_content += f'''                <a href="qual_vuln_charts_actors_split/risk{num}_vulnerability_actors_part2.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Actor Vulnerability - Part 2</div>
                </a>
'''

new_content += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Sectors) - Part 1</div>
            <p class="section-description" style="font-size: 12px; margin-bottom: 15px;">Agriculture/Mining/Construction/Manufacturing, Trade/Transportation/Utilities, Information, Finance and Insurance</p>
            <div class="chart-grid">
'''

# Add vulnerability sectors part 1 links
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    new_content += f'''                <a href="qual_vuln_charts_sectors_split/risk{num}_vulnerability_sectors_part1.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Sector Vulnerability - Part 1</div>
                </a>
'''

new_content += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Sectors) - Part 2</div>
            <p class="section-description" style="font-size: 12px; margin-bottom: 15px;">Real Estate and Rental and Leasing, Professional and Technical Services, Scientific Services, Management/Administrative/Support Services</p>
            <div class="chart-grid">
'''

# Add vulnerability sectors part 2 links
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    new_content += f'''                <a href="qual_vuln_charts_sectors_split/risk{num}_vulnerability_sectors_part2.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Sector Vulnerability - Part 2</div>
                </a>
'''

new_content += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Sectors) - Part 3</div>
            <p class="section-description" style="font-size: 12px; margin-bottom: 15px;">Educational Services, Health Care and Social Assistance, Arts/Entertainment/Recreation, Accommodation/Food/Other Services</p>
            <div class="chart-grid">
'''

# Add vulnerability sectors part 3 links
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    new_content += f'''                <a href="qual_vuln_charts_sectors_split/risk{num}_vulnerability_sectors_part3.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Sector Vulnerability - Part 3</div>
                </a>
'''

new_content += '''            </div>
        </div>

        <div class="subsection">
            <div class="subsection-title">Vulnerability Analysis (Sectors) - Part 4</div>
            <p class="section-description" style="font-size: 12px; margin-bottom: 15px;">Public Administration excluding National Security, National Security</p>
            <div class="chart-grid">
'''

# Add vulnerability sectors part 4 links
for num in range(1, 25):
    risk_code = risk_mapping[str(num)]
    risk_name = risk_names[risk_code]
    new_content += f'''                <a href="qual_vuln_charts_sectors_split/risk{num}_vulnerability_sectors_part4.html" class="chart-link">
                    <div class="risk-num">{risk_code} {risk_name}</div>
                    <div class="chart-type">Sector Vulnerability - Part 4</div>
                </a>
'''

new_content += '''            </div>
        </div>
    </div>

</body>
</html>
'''

# Write the updated content
with open('index.html', 'w') as f:
    f.write(new_content)

print("Updated index.html with new riskN naming convention!")
print("\nAll links now use format: riskN_[type]_partX.html")
print("Where N = 1-24 according to the risk mapping")
