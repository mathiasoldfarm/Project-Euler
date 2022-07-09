from ast import literal_eval
import math

with open('primes.txt') as f:
    line = f.readline()
    primes = list(literal_eval(line))


def check(n):
    for prime in primes:
        if prime > n:
            return False
        n1 = (n - prime) / 2
        n2 = int(math.sqrt(n1))
        if n1 == (n2**2):
            return True
    return False

n = 9
while True:
    if n not in primes and not check(n):
        break
    n += 2

print(n)