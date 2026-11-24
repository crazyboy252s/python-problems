# Read the number of test cases
n = int(input())

# Loop through each test case
for _ in range(n):
    # Read two integers a and b from the input line
    a, b = map(int, input().split())
    # Perform floating-point division
    val = a / b

    # Manual rounding "half away from zero"
    if val >= 0:
        # For positive numbers, add 0.5 and truncate to integer
        ans = int(val + 0.5)
    else:
        # For negative numbers, subtract 0.5 and truncate to integer
        ans = int(val - 0.5)

    # Print the result followed by a space
    print(ans, end=" ")
