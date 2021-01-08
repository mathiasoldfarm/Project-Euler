#https://projecteuler.net/problem=3

n = 600851475143

factors_begin = [1]
factors_end = [n]

largest_prime = 1

def isPrime(n):
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True

counter = 2
while( factors_end[0] - factors_begin[0] > 1 ):
  if ( n % counter == 0 ):
    factor = int(n / counter)
    factors_begin.insert(0, counter)
    factors_end.insert(0, factor)

    if ( counter > largest_prime and isPrime(counter) ):
      largest_prime = counter

  counter += 1
  
print(largest_prime)

