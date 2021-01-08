#https://projecteuler.net/problem=2

bound = 4000000
even_sum = 2

s = [0] * 50
s[0] = 1
s[1] = 2
counter = 2

while( s[counter-1] <= bound):
  new_fib = s[counter - 1] + s[counter - 2]
  if new_fib % 2 == 0:
    even_sum += new_fib
  s[counter] = new_fib

  counter += 1

print(even_sum)


  