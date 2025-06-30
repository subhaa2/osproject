#!/bin/bash


numbers=(4 7 1 9 3 5)

echo "Enter a number to check:"
read target

for (( i=0; i<${#numbers[@]}; i++ ))
do
    for (( j=i+1; j<${#numbers[@]}; j++ ))
    do
        sum=$((numbers[i] + numbers[j]))
        if [ "$sum" -eq "$target" ]; then
            echo "There are two numbers in the list that sum to $target"
            exit 0  
        fi
    done
done

# Only reached if no match was found
echo "No two numbers in the list add up to $target"
