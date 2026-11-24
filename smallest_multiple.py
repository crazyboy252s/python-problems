
import math

num = 1

for i in range(1, 21):
    num = math.lcm(num, i)

print(num)
#we completed this problem using the lcm function from the math module. The lcm function takes two numbers as input and returns their least common multiple. We can use this function to find the lcm of all the numbers from 1 to 20 by iterating through the range and updating the num variable with the lcm of num and i at each step. Finally, we print the value of num, which will be the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.y = set(map(int, input("Enter the numbers for the second set: ").split()))
