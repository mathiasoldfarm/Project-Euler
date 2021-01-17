def factorial(n):
  counter = 2
  prod = 1
  while counter < n:
    prod *= counter
    counter += 1
  return prod

def factorial_digit_sum(n):
  f = factorial(n)
  s = 0
  while(f):
    s += f % 10
    f //= 10

  return s

print(factorial_digit_sum(100))