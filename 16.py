n = int(pow(2,1000))
s = 0

while n:
  s += int(n % 10)
  n = int(n // 10)

print(s)