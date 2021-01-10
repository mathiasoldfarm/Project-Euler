n = 2000000
s = 0
numbers = [True] * (n+1)
for i in range(2,n):
  if numbers[i]:
    s += i
    for j in range(i*i,n,i):
      numbers[j] = False
print(s)