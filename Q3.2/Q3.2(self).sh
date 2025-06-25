#!/bin/bash
largestNumber() {
    numbers=("$@")
    largest=${numbers[0]}
    for n in "${numbers[@]}"; do
        if [ "$n" -gt "$largest" ]; then
            largest=$n
        fi
    done
    echo "$largest is the largest number"
}

while true; do
    echo -n "Enter a list of numbers (or 'q' to quit): "
    read input
    if [ "$input" = "q" ]; then
        echo "Goodbye"
        break
    fi
    numbers=($input)
    largestNumber "${numbers[@]}"
done