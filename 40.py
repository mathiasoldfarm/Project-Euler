from numpy import product


c = ""
i = 1
while(len(c) < 1000000):
    c += str(i)
    i += 1
indicies = [1,10,100,1000,10000,100000,1000000]
p = 1
for index in indicies:
    p *= int(c[index-1])
print(p)