c1, c2, c3, c4 = map(int, input().split())
distinct = len(set([c1, c2, c3, c4]))
print(4 - distinct)