def find_largest():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    max_num = max(nums)
    print(f"{max_num} is the largest number")

find_largest()
