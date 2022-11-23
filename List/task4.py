list = [int(s) for s in input().split()]
list.sort()
print(*list)
list.sort(reverse=True)
print(*list)