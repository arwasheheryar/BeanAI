# BeanAI
Hybrid AI Approaches to Predicting Complex Traits in Plant Breeding
##Introduction 

##Methods 
Handling Large Heterogeneous Dataset
### Step 1: Run the Data Inventory Script
```bash
# Navigate to your project directory
cd /path/to/your/project

# Run the inventory on ALL your dry bean data
python explore_data_inventory.py \
    --data_dir /path/to/all/drybean/files \
    --output_dir ./data_inventory_results
```

**What this does:**
- 🔍 Scans every Excel, CSV, and text file recursively
- 📊 Analyzes structure (headers, columns, sheets)
- 🏷️ Groups files by format patterns
- 📈 Generates statistics and visualizations
- 💡 Gives you actionable recommendations

- **Time:** 5-30 minutes depending on number of files
  
- **Outputs:**
1. `inventory_report.html` ← **OPEN THIS FIRST**
2. `data_inventory.json` ← Complete details
3. `file_inventory.csv` ← Spreadsheet view
   
### Decision Tree

A lot of variation: 
1. Focus on **top 3 most common patterns** (usually covers 60-80% of data)
2. Build specialized parser for each pattern 
3. Process those files first, get 80% of your data unified
4. Tackle remaining patterns iteratively
   
Mostly 2-3 patterns being followed
1. Create 2-3 specialized parsers
2. Process all files with pattern matching
3. Handle edge cases manually (probably <5% of files)

Highly divergent Data
1. Group by year or period (2010-2013, 2014-2017, 2018-2023)
2. Create parser for each period
3. Unify within periods first, then merge periods
4. Consider excluding very old/messy data if not critical

