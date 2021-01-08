#https://projecteuler.net/problem=6

n = 100

print(abs(sum([pow(i, 2) for i in range(1,n+1)]) - pow(sum([i for i in range(1,n+1)]), 2)))