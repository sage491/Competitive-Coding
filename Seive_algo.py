def sieve_count(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    count = 0
    for i in range(2, n + 1):
        if prime[i]:
            count += 1

    return count

if __name__ == "__main__":
    n = 10000000000
    print(sieve_count(n))
