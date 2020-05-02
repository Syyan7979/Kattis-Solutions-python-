n = int(input())
ans = sum([int(i) for i in input().split() if int(i) < 0])
print(-ans)