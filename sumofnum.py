sum_of_squares = 0
total_sum = 0

for i in range(1, 101):
  sum_of_squares += i * i
  total_sum += i

square_of_sum = total_sum**2
difference = square_of_sum - sum_of_squares

print(f"{square_of_sum} - {sum_of_squares} = {difference}")