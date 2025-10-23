#!/usr/bin/env python3
"""
Rename severity files to match the flat naming pattern: decimalRisk_severity.html
"""

import shutil
from pathlib import Path

# Mapping from risk_X_Y to decimal
risk_mapping = {
    "risk_1_1": "1.1",
    "risk_1_2": "1.2",
    "risk_1_3": "1.3",
    "risk_2_1": "2.1",
    "risk_2_2": "2.2",
    "risk_3_1": "3.1",
    "risk_3_2": "3.2",
    "risk_4_1": "4.1",
    "risk_4_2": "4.2",
    "risk_4_3": "4.3",
    "risk_5_1": "5.1",
    "risk_5_2": "5.2",
    "risk_6_1": "6.1",
    "risk_6_2": "6.2",
    "risk_6_3": "6.3",
    "risk_6_4": "6.4",
    "risk_6_5": "6.5",
    "risk_6_6": "6.6",
    "risk_7_1": "7.1",
    "risk_7_2": "7.2",
    "risk_7_3": "7.3",
    "risk_7_4": "7.4",
    "risk_7_5": "7.5",
    "risk_7_6": "7.6",
}

base_dir = Path(__file__).parent
source_dir = base_dir / 'qual_severity_charts'
dest_dir = base_dir / 'qual_severity_charts_final'

dest_dir.mkdir(exist_ok=True)

count = 0
for file in source_dir.glob('*.html'):
    filename = file.name

    # Extract risk code from filename
    for old_code, new_code in risk_mapping.items():
        if filename.startswith(old_code):
            new_filename = f"{new_code}_severity.html"
            dest_path = dest_dir / new_filename

            shutil.copy2(file, dest_path)
            print(f"Copied: {filename} -> {new_filename}")
            count += 1
            break

print(f"\nTotal files copied: {count}")
print("\nURL pattern: baseURL + decimalRiskNumber + '_severity.html'")
print("Example: https://ai-risk-initiative.github.io/Delphi_R2_Qual_Graphs/1.1_severity.html")
