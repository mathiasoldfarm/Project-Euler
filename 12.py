def isPrime(n):
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True

primes = []
n_primes = 1000
counter = 0
while(n_primes > -2):
  if isPrime(counter):
    n_primes -= 1
    if counter > 1:
      primes.append(counter)
  counter += 1

def add_to_dict(dictionary, key):
  if key in dictionary:
    dictionary[key] += 1
  else:
    dictionary[key] = 1

def number_of_divisors(n):
  primes_factorization = {}
  while ( not isPrime(n) ):
    counter = 0
    while( n % primes[counter] != 0 ):
      counter += 1
    prime = primes[counter]
    n = int(n / prime)
    add_to_dict(primes_factorization, prime)
  add_to_dict(primes_factorization, n)
  n_divisors = 1
  for key in primes_factorization:
    n_divisors *= (primes_factorization[key] + 1)
  return n_divisors

tri_numb = 1
counter = 1
bound = 500
while( number_of_divisors(tri_numb) <= bound ):
  counter += 1
  tri_numb += counter

print(tri_numb)