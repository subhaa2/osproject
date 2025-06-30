#!/bin/bash

# List .txt files in the current directory
txt_files=(*.txt)

# Count .txt files (if none exist, prevent zipping)
count=0
for file in "${txt_files[@]}"; do
    if [[ -f "$file" ]]; then
        ((count++))
    fi
done

if [ "$count" -gt 0 ]; then
    zip -q mytxt.zip *.txt
    echo "There are $count .txt files and compressed into a .zip file"
else
    echo "There are 0 .txt files. No compression performed."
fi
