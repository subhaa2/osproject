#!/bin/bash


count=$(ls *.txt 2>/dev/null | wc -l)

if [ "$count" -gt 0 ]; then
    zip -q mytxt.zip *.txt
    echo "There are $count .txt files and compressed into a .zip file"
else
    echo "No .txt files Detected. Compression skipped."
fi
