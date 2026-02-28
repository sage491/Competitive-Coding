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

n = int(input())
a = list(map(int, input().split()))

max_ones = 0

# Try all possible segments [i, j]
for i in range(n):
    for j in range(i, n):
        # Count ones after flipping segment [i, j]
        ones = 0
        
        for k in range(n):
            if i <= k <= j:
                # Inside flipped range: flip the value
                ones += 1 - a[k]
            else:
                # Outside flipped range: keep original
                ones += a[k]
        
        max_ones = max(max_ones, ones)

print(max_ones)