def is_prime():
    num = int(input("Enter a number: "))
    if num <= 1:
        print(f"The keyed-in number {num} is not a prime number")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"The keyed-in number {num} is not a prime number")
            return
    print(f"The keyed-in number {num} is a prime number")

is_prime()
