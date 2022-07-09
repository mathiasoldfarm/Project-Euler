def primes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while(p*p <= n):
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    res = []
    for i in range(2, n+1):
        if prime[i]:
            res.append(i)
    return res

def generate_primes(n):
    with open("./primes.txt", "w") as f:
        f.write("")
        f.write(str(primes(n)))

generate_primes(500000)