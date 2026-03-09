import math

t = int(input())
for _ in range(t):
    n = int(input())
    temp = n
    k = 1
    
    i = 2
    while i * i <= temp:
        if temp % i == 0:
            k *= i
            while temp % i == 0:
                temp //= i
        i += 1
    
    if temp > 1:
        k *= temp
    
    print(k)