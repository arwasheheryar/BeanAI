#!/bin/bash
cd ~/BeanAI/data/organized/unknown_year

echo "Files in unknown_year:"
echo "===================="
ls -1

echo ""
echo "Let's move them one by one."
echo "Press Ctrl+C to stop anytime"
echo ""

for file in *.xls*; do
    echo "====================================="
    echo "File: $file"
    echo -n "What year does this belong to? (2015-2023, or 'skip'): "
    read year
    
    if [ "$year" = "skip" ]; then
        echo "Skipping $file"
        continue
    fi
    
    if [ -d "../$year" ]; then
        mv "$file" "../$year/"
        echo "✓ Moved to $year/"
    else
        echo "✗ Year folder $year doesn't exist"
    fi
    echo ""
done

echo "Done! Check results:"
cd ..
for y in 2015 2016 2017 2018 2019 2020 2021 2022 2023; do
    count=$(ls $y/*.xls* 2>/dev/null | wc -l)
    echo "$y: $count files"
done
