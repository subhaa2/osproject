import math

def is_prime(n):
    if n <= 1:
        print(f"The keyed-in number {n} is not a prime number.")
        return
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"The keyed-in number {n} is not a prime number.")
            return
    print(f"The keyed-in number {n} is a prime number.")

while True:
    n = input("Enter a number(or 'q' to quit): ")
    if n == 'q':
        print("Goodbye")
        break
    else:
        n = int(n)
        is_prime(n)