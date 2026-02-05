def mod(a, b, mod):
    result = 1
    a = a % mod
    
    while b > 0:
        if b % 2 == 1: 
            result = (result * a) % mod
        a = (a * a) % mod
        b = b // 2
    
    return result

MOD = 10**9 + 7
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(mod(a, b, MOD))
