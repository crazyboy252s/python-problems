x = set(map(int, input("Enter the numbers for the first set: ").split()))
y = set(map(int, input("Enter the numbers for the second set: ").split()))
z = set(map(int, input("Enter the numbers for the third set: ").split()))

combined_set = x | y | z#| ante itl union of three sets
ascending_list = sorted(combined_set)#direct sort chesi padesthadi crazy compare to c

print("Combined set:", combined_set)
print("Ascending order:", ascending_list)