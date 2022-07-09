import itertools

def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def get_permutations(n):
    s = ""
    for i in range(1,n+1):
        s += str(i)
    permutations = list(itertools.permutations(s))
    permutations = [int("".join(s)) for s in permutations]
    permutations = list(sorted(permutations, reverse=True))
    return permutations

def solve():
    for n in range(9,0,-1):
        permutations = get_permutations(n)
        for p in permutations:
            if is_prime(p):
                return p

print(solve())