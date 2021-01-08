#https://projecteuler.net/problem=7

def isPrime(n):
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True

n = 10001
counter = 0
while(n > -2):
  if isPrime(counter):
    n -= 1
  counter += 1

print(counter - 1)