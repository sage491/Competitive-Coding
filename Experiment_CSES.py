MAXX = 10**6

divisors = [0] * (MAXX + 1)

for i in range(1, MAXX + 1):
    for j in range(i, MAXX + 1, i):
        divisors[j] += 1

n = int(input())
for _ in range(n):
    x = int(input())
    print(divisors[x])
    

n = int(input())
 
for _ in range(n):
    x = int(input())
    count = 0
    i = 1
 
    while i * i <= x:
        if x % i == 0:
            count += 1
            if i != x // i:
                count += 1
        i += 1
 
    print(count)