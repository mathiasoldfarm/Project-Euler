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

def prime_factorization(n):
  primes_factorization = {}
  while ( not isPrime(n) ):
    counter = 0
    while( n % primes[counter] != 0 ):
      counter += 1
    prime = primes[counter]
    n = int(n / prime)
    add_to_dict(primes_factorization, prime)
  add_to_dict(primes_factorization, n)
  return primes_factorization

def get_divisor(factorization):
  divisor = 1
  for key in factorization:
    divisor *= pow(int(key), factorization[key])
  return divisor

def find_all_divisors(current_factorization, max_factorization, memory, divisors):
  if current_factorization != max_factorization:
    for key in current_factorization:
      if current_factorization[key] < max_factorization[key]:
        new_current = current_factorization.copy()
        new_current[key] += 1

        divisor = get_divisor(new_current)
        if divisor not in memory and new_current != max_factorization:
          divisors.append(divisor)
          memory[divisor] = True
          find_all_divisors(new_current, max_factorization, memory, divisors)
  return divisors

def is_abundant(n):
  max_factorization = prime_factorization(n)
  current_factorization = {}
  for key in max_factorization:
    current_factorization[key] = 0

  divisors = find_all_divisors(current_factorization, max_factorization, {}, [])
  return sum(divisors) > n

limit = 28123
all_abundant = set()
for i in range(1,limit):
  if i not in all_abundant and is_abundant(i):
    for j in range(i, limit, i):
      all_abundant.add(j)

combination_ints = set()
all_abundant = list(all_abundant)
for i in range(len(all_abundant)):
  for j in range(i, len(all_abundant)):
    num1 = all_abundant[i]
    num2 = all_abundant[j]
    if num1 + num2 <= limit:
      combination_ints.add(num1 + num2)

s = sum(combination_ints)
s1 = int(limit*(limit+1) / 2)

print(s1-s)



