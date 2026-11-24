
largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j

        if str(product) == str(product)[::-1]:#it means ::1 mean reverse the number           if product > largest:
                largest = product

print(largest)