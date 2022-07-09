import itertools

bound = 3000
pentagons = [int(n*(3*n-1)/2) for n in range(1,1+bound)]
pentagons_set = set(pentagons)

pairs = itertools.combinations(pentagons, 2)
pairs = list(sorted(pairs, key=lambda x: abs(x[0]-x[1])))
print(len(pairs))
for n1, n2 in pairs:
    if (n1+n2) in pentagons_set and abs(n1-n2) in pentagons_set:
        print(abs(n1-n2))
        break