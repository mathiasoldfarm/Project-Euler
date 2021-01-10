import math

bound = 1000
a, b, c, j = 0, 0, 0, 2

while (c < 1000):
  for i in range(1,j):
    a = pow(j,2) - pow(i,2)
    b = 2*j*i
    c = pow(j,2) + pow(i,2)

    if a+b+c == bound:
      print(a,b,c)
      print(a*b*c)
      break

  j += 1