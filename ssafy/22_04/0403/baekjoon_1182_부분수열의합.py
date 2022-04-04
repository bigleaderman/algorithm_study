from sys import stdin

N, S = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
cnt = 0

for i in range(1, 1<<N):
    total = 0
    for j in range(N):
        if i & (1<<j):
            total += lst[j]
    if total == S:
        cnt += 1
print(cnt)