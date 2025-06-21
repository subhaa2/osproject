
def largestNumber(numbers):
    largest = max(numbers)
    print(f"{largest} is the largest number")

while True:
    userinput = input("Enter a list of numbers (or 'q' to quit): ")
    if userinput == 'q':
        print("Goodbye")
        break
    else:
        numbers = list(map(int, userinput.split()))
        largestNumber(numbers)



