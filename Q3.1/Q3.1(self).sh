#!/bin/bash
is_prime() {
    n=$1
    if [ "$n" -le 1 ]; then
        echo "The keyed-in number $n is not a prime number."
        return
    fi
    sqrt=$(echo "sqrt($n)" | bc)

    for (( i=2; i<=sqrt; i++ )); do
        if (( n % i == 0 )); then
            echo "The keyed-in number $n is not a prime number."
            return
        fi
    done
    echo "The keyed-in number $n is a prime number."
}

while true; do
    echo -n "Enter a number: "
    read n
    if [ "$n" == "q" ]; then
        echo "Goodbye"
        break
    fi
    is_prime "$n"
done