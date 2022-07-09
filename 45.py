pentagonals = set()
hexagonals = set()

n = 1
while True:
    triangle = n*(n+1)/2
    if triangle == 40755:
        break
    n += 1

print(n)
while True:
    triangle = n*(n+1)/2
    penta = n*(3*n-1)/2
    hexa = n*(2*n-1)
    pentagonals.add(penta)
    hexagonals.add(hexa)
    if triangle in pentagonals and triangle in hexagonals:
        print(triangle)
        break
    n += 1