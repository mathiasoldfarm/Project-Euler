multiplicand_max = 4999
multiplier_max = 99

def is_pandigital(multiplicand, multiplier, prod):
  return "".join(sorted(list(str(multiplicand) + str(multiplier) + str(prod)))) == "123456789"

pan_digitals = set()
for i in range(1,multiplicand_max + 1):
  for j in range(1, multiplier_max + 1):
    prod = i * j
    if is_pandigital(i,j,prod):
      pan_digitals.add(prod)

print(sum(pan_digitals))