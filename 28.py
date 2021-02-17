n = 1001

s = 1
size = 1
diff = 2
counter = s
while size != n:
  for i in range(4):
    counter += diff
    s += counter
  size += 2
  diff += 2

print(s)