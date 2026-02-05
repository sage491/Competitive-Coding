#1 attempt
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 2 or n == 3:
        print(-1)
    else:
        perm = []
        left, right = 1, n
        while left <= right:
            perm.append(right)
            right -= 1
            if left <= right:
                perm.append(left)
                left += 1
        print(*perm)
        
#2 attempt
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 2 or n == 3:
        print(-1)
    else:
        perm = []
        for i in range(n, 0, -1):
            perm.append(i)
        print(*perm)  
# 3 attempt
t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 5:
        print(-1)
        continue

    evens = list(range(2, n + 1, 2))
    odds = list(range(1, n + 1, 2))

    print(*evens, *odds[::-1])
# 4 attempt
t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 3:
        print(-1)
        continue

    evens = [i for i in range(2, n + 1, 2)]
    odds = [i for i in range(1, n + 1, 2)][::-1]

    print(*evens, *odds)
              