n = int(input())
a = list(map(int, input().split()))
max_ones = 0
for i in range(n):
    for j in range(i, n):
        ones = 0
        for k in range(n):
            if i<=k<=j:
                ones += 1 -a[k]
            else:
                ones += a[k]
        max_ones= max(max_ones, ones)
print(max_ones)
            
    
        