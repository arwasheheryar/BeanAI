#!/usr/bin/env python3
"""
Simple script to count and list all Excel files
"""
import os
from pathlib import Path

def count_excel_files(directory):
    """Count Excel files and show summary"""
    excel_files = []
    
    # Find all Excel files
    for ext in ['*.xlsx', '*.xls', '*.xlsm']:
        excel_files.extend(Path(directory).rglob(ext))
    
    print(f"Found {len(excel_files)} Excel files\n")
    print("Files:")
    print("-" * 60)
    
    for i, file in enumerate(sorted(excel_files), 1):
        size_mb = file.stat().st_size / (1024 * 1024)
        print(f"{i:3d}. {file.name:50s} ({size_mb:.2f} MB)")
    
    return excel_files

if __name__ == '__main__':
    data_dir = '../data/raw_excel_files'
    files = count_excel_files(data_dir)
    
    print("\n" + "=" * 60)
    print(f"Total: {len(files)} files")
