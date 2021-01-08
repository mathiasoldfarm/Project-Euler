#https://projecteuler.net/problem=1

print(sum([i if i % 3 == 0 or i % 5 == 0 else 0 for i in range(1,1000)]))