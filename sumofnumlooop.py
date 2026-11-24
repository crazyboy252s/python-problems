nums = map(int, input("Enter numbers separated by spaces: ").split())
total = 0
for n in nums:
    total = total + n
print("Sum:", total)