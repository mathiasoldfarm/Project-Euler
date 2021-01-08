#https://projecteuler.net/problem=5

smallest = None

upper = 20
counter = upper

while(True):
  if all([ counter % i == 0 for i in range(2,upper + 1) ]):
    smallest = counter
    break
  counter += upper

print(smallest)