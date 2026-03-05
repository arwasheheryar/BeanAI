# Data Organization Summary

**Date:** March 5, 2026  
**Total Files:** 149 Excel files  
**Years Covered:** 2015-2023

## Organization Process

1. Ran `step2_organize_by_year.py` to organize files by year
2. Used `inspect_unknown_files.py` to identify files without year in filename
3. Interactively moved 20 unknown files to correct year folders

## Final Distribution

| Year | File Count | Notes |
|------|-----------|-------|
| 2015 | 25 files | Includes preliminary trials |
| 2016 | 24 files | Largest increase from unknowns |
| 2017 | 20 files | Includes pursuit summaries |
| 2018 | 9 files | Smallest year |
| 2019 | 23 files | Multiple trial types |
| 2020 | 20 files | |
| 2021 | 14 files | |
| 2022 | 7 files | Recent data |
| 2023 | 7 files | Most recent data |
| **Total** | **149 files** | |

## Data Structure
```
data/
├── raw_excel_files/     # Original unorganized files
└── organized/           # Files organized by year
    ├── 2015/
    ├── 2016/
    ├── 2017/
    ├── 2018/
    ├── 2019/
    ├── 2020/
    ├── 2021/
    ├── 2022/
    └── 2023/
```

## Next Steps

1. Run comprehensive inventory analysis
2. Identify format patterns
3. Build custom parsers for each pattern
4. Begin data unification

## Files Created

- `step1_check_files.py` - Initial file verification
- `step2_organize_by_year.py` - Automated organization by year
- `inspect_unknown_files.py` - Year detection from file contents
- `interactive_move.sh` - Interactive file organization tool

