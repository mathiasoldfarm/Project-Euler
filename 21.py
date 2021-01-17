def sum_of_divisors(n):
  s = 0
  for i in range(1,n):
    if n % i == 0:
      s += i
  return s

def is_amicable(n):
  s = sum_of_divisors(n)
  return sum_of_divisors(s) == n and s != n

print(sum([i if is_amicable(i) else 0 for i in range(1,10001)]))