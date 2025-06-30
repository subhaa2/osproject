

numbers = [4, 7, 1, 9, 3, 5]

target = int(input("Enter a number to check: "))
found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"There are two numbers in the list that adds up to {target}")
            found = True
            break
    if found:
        break

if not found:
    print(f"No two numbers in the list add to {target}")
