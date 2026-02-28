n = int(input())
count = 0 
for i in range(n):
    p, v, t= map(int, input().split())
    agree_count = p + v + t
    if agree_count >=2:
        count+=1
print(count)