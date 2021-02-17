lower_a = 2
lower_b = 2
high_a = 100
high_b = 100

items = set()
for a in range(lower_a, high_a+1):
  for b in range(lower_b, high_b+1):
    items.add(a**b)
    items.add(b**a)

print(len(items))