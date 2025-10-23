#!/usr/bin/env python3
"""
Rename files from risk_X_Y format to riskN format based on mapping
"""

import os
from pathlib import Path

# Mapping from number to risk code
risk_mapping = {
    "1": "1_1",
    "2": "1_2",
    "3": "1_3",
    "4": "2_1",
    "5": "2_2",
    "6": "3_2",  # SWAPPED
    "7": "3_1",  # SWAPPED
    "8": "4_1",
    "9": "4_3",  # SWAPPED
    "10": "4_2", # SWAPPED
    "11": "5_1",
    "12": "5_2",
    "13": "6_1",
    "14": "6_2",
    "15": "6_3",
    "16": "6_4",
    "17": "6_5",
    "18": "6_6",
    "19": "7_1",
    "20": "7_2",
    "21": "7_3",
    "22": "7_4",
    "23": "7_5",
    "24": "7_6"
}

# Create reverse mapping (from risk_X_Y to number)
reverse_mapping = {v: k for k, v in risk_mapping.items()}

def rename_files_in_directory(directory):
    """Rename all files in directory from risk_X_Y to riskN format"""
    directory = Path(directory)
    if not directory.exists():
        print(f"Directory {directory} does not exist, skipping...")
        return

    renamed_count = 0
    for file in directory.glob('*.html'):
        filename = file.name

        # Extract risk code from filename (e.g., risk_1_1 from risk_1_1_responsibility_part1.html)
        # Pattern: risk_X_Y_...
        import re
        match = re.match(r'risk_(\d+_\d+)_(.*)', filename)
        if match:
            risk_code = match.group(1)
            rest_of_name = match.group(2)

            if risk_code in reverse_mapping:
                risk_num = reverse_mapping[risk_code]
                new_filename = f'risk{risk_num}_{rest_of_name}'
                new_path = directory / new_filename

                print(f"Renaming: {filename} -> {new_filename}")
                file.rename(new_path)
                renamed_count += 1

    print(f"Renamed {renamed_count} files in {directory}")
    return renamed_count

def main():
    base_dir = Path(__file__).parent

    directories = [
        'qual_resp_charts_split',
        'qual_vuln_charts_actors_split',
        'qual_vuln_charts_sectors_split'
    ]

    total_renamed = 0
    for dir_name in directories:
        print(f"\n{'='*60}")
        print(f"Processing {dir_name}...")
        print('='*60)
        count = rename_files_in_directory(base_dir / dir_name)
        total_renamed += count

    print(f"\n{'='*60}")
    print(f"Total files renamed: {total_renamed}")
    print('='*60)

if __name__ == '__main__':
    main()
