#!/usr/bin/env python3
"""
Organize Excel files by year into subfolders
"""
import os
import shutil
import re
from pathlib import Path

def extract_year(filename):
    """Extract year from filename"""
    # Look for 4-digit year (2010-2025)
    match = re.search(r'(20[1-2][0-9])', filename)
    if match:
        return match.group(1)
    return 'unknown_year'

def organize_files(source_dir, target_dir):
    """Organize files into year-based folders"""
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    
    # Find all Excel files
    excel_files = []
    for ext in ['*.xlsx', '*.xls', '*.xlsm']:
        excel_files.extend(source_path.rglob(ext))
    
    print(f"Found {len(excel_files)} files to organize\n")
    
    # Organize by year
    year_counts = {}
    
    for file in excel_files:
        year = extract_year(file.name)
        
        # Create year folder if it doesn't exist
        year_folder = target_path / year
        year_folder.mkdir(exist_ok=True)
        
        # Copy file (don't move, keep originals safe!)
        target_file = year_folder / file.name
        shutil.copy2(file, target_file)
        
        # Track counts
        year_counts[year] = year_counts.get(year, 0) + 1
        
        print(f"Copied: {file.name} → {year}/")
    
    # Summary
    print("\n" + "=" * 60)
    print("ORGANIZATION COMPLETE")
    print("=" * 60)
    for year in sorted(year_counts.keys()):
        print(f"{year}: {year_counts[year]} files")

if __name__ == '__main__':
    source = '../data/raw_excel_files'
    target = '../data/organized'
    
    organize_files(source, target)

