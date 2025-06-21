#!/bin/bash

read -p "Enter numbers separated by space: " -a nums
max=${nums[0]}

for n in "${nums[@]}"; do
  if (( n > max )); then
    max=$n
  fi
done

echo "$max is the largest number"
