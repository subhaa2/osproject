#!/bin/bash


numbers=(4 7 1 9 3 5)

read -p "Enter a number to check: " target

found=0

for i in "${!numbers[@]}"
do
    for j in "${!numbers[@]}"
    do
        if [ "$i" -ne "$j" ]; then
            sum=$((numbers[i] + numbers[j]))
            if [ "$sum" -eq "$target" ]; then
                echo "There are two numbers in the list summing to $target"
                found=1
                break 2
            fi
        fi
    done
done

if [ "$found" -eq 0 ]; then
    echo "There are not two numbers in the list summing to $target"
fi
