n = int(input())

def solve(n, source, auxiliary, destination):
    if n == 0:
        return
    solve(n - 1, source, destination, auxiliary)
    print(source, destination)
    solve(n - 1, auxiliary, source, destination)

print(2**n - 1)

solve(n, 1, 2, 3)