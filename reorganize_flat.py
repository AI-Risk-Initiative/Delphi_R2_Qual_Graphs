#!/usr/bin/env python3
"""
Reorganize files to flat structure: decimalRiskNumber_type_partX.html
This matches the URL pattern: baseURL + decimalRiskNumber + '_vulnerability_actors_part1.html'
"""

import os
import shutil
from pathlib import Path

# Mapping from number to risk code
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

def reorganize_directory_flat(source_dir, dest_dir):
    """
    Reorganize files to flat structure
    riskN_type_partX.html -> decimalRisk_type_partX.html
    Example: risk1_vulnerability_actors_part1.html -> 1.1_vulnerability_actors_part1.html
    """
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)

    if not source_dir.exists():
        print(f"Source directory {source_dir} does not exist, skipping...")
        return 0

    # Create destination directory
    dest_dir.mkdir(exist_ok=True)

    renamed_count = 0

    for file in source_dir.glob('*.html'):
        filename = file.name

        # Extract risk number from filename (e.g., risk1_...)
        import re
        match = re.match(r'risk(\d+)_(.*)', filename)
        if match:
            risk_num = match.group(1)
            rest_of_name = match.group(2)

            # Get decimal risk number (e.g., 1.1, 2.1, etc.)
            if risk_num in risk_mapping:
                decimal_risk = risk_mapping[risk_num]

                # New filename: decimalRisk_type_partX.html (e.g., 1.1_vulnerability_actors_part1.html)
                new_filename = f"{decimal_risk}_{rest_of_name}"
                dest_path = dest_dir / new_filename

                # Copy file
                shutil.copy2(file, dest_path)
                print(f"Copied: {filename} -> {new_filename}")
                renamed_count += 1

    print(f"Copied {renamed_count} files from {source_dir} to {dest_dir}")
    return renamed_count

def main():
    base_dir = Path(__file__).parent

    # Process each type of chart
    reorganizations = [
        ('qual_resp_charts_split', 'qual_resp_charts_final'),
        ('qual_vuln_charts_actors_split', 'qual_vuln_charts_actors_final'),
        ('qual_vuln_charts_sectors_split', 'qual_vuln_charts_sectors_final')
    ]

    total_moved = 0

    for source, dest in reorganizations:
        print(f"\n{'='*70}")
        print(f"Reorganizing {source} -> {dest}")
        print('='*70)
        count = reorganize_directory_flat(base_dir / source, base_dir / dest)
        total_moved += count

    print(f"\n{'='*70}")
    print(f"Total files copied: {total_moved}")
    print('='*70)
    print("\nNew structure (flat):")
    print("  qual_vuln_charts_actors_final/")
    print("    1.1_vulnerability_actors_part1.html")
    print("    1.1_vulnerability_actors_part2.html")
    print("    1.2_vulnerability_actors_part1.html")
    print("    1.2_vulnerability_actors_part2.html")
    print("    ...")
    print("\nURL pattern: baseURL + decimalRiskNumber + '_vulnerability_actors_part1.html'")
    print("Example: https://ai-risk-initiative.github.io/Delphi_R2_Qual_Graphs/1.1_vulnerability_actors_part1.html")

if __name__ == '__main__':
    main()
