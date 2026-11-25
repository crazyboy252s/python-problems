def find_maximum(arr):
    max=arr[0]
    for num in arr:
        if num>max:
            max=num
    return max
x = find_maximum([1, 2, 3, 4, 5,99])
print(x)