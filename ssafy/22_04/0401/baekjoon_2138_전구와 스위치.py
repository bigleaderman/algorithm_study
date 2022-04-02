from sys import stdin

N = int(stdin.readline())
arr1 = list(map(int, input().strip()))
arr2 = list(map(int, input().strip()))
visited = [0] * N
cnt = 0
for _ in range(2):
    for i in range(N-1):
        if i == 0 or i == N-2 and not visited[i] and arr1[i] != arr2[i]:
            visited[i] = 1
            cnt += 1
            for j in range(2):
                if arr1[i+j]:
                    arr1[i+j] = 0
                else:
                    arr1[i+j] = 1
        elif not visited[i] and arr1[i] != arr2[i]:
            visited[i] = 1
            cnt += 1
            for j in range(3):
                if arr1[i + j]:
                    arr1[i + j] = 0
                else:
                    arr1[i + j] = 1

config = 1
for i in range(N):
    if arr1[i] != arr2[i]:
        config = 0
        break

if config:
    print(cnt)
else:
    print(-1)