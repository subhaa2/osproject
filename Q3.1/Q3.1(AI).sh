#!/bin/bash

read -p "Enter a number: " num
is_prime=1

if [ "$num" -le 1 ]; then
  is_prime=0
else
  for ((i=2; i*i<=num; i++)); do
    if (( num % i == 0 )); then
      is_prime=0
      break
    fi
  done
fi

if [ $is_prime -eq 1 ]; then
  echo "The keyed-in number $num is a prime number"
else
  echo "The keyed-in number $num is not a prime number"
fi
