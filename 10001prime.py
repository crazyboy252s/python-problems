def is_prime(n):
  if n < 2:
    return False
  for d in range(2, n):
    if n % d == 0:
      return False
  return True


count = 0
num = 2

while True:
  if is_prime(num):
    count += 1
    if count == 10001:
      print(num)
      break
  num += 1