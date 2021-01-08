#https://projecteuler.net/problem=4

import math

lower_bound = 100
upper_bound = 999

largest_palindromic = 0

def isPalindromic(n):

  digits = []
  while(n):
    digits.append(n % 10)
    n = int(n / 10)
  if ( len(digits) % 2 == 0 ):
    half = int(len(digits) / 2)
    first = digits[:half]
    last = digits[half:]
    last.reverse()
    return first == last
  half = int(math.floor(len(digits) / 2))
  first = digits[:half]
  last = digits[half + 1:]
  last.reverse()
  return first == last

for i in range(lower_bound, upper_bound + 1):
  for j in range(lower_bound, upper_bound + 1):
    product = i*j
    if int(product) > largest_palindromic and isPalindromic(product):
      largest_palindromic = product

print(largest_palindromic)