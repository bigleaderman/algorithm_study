# nPn

def perm(n,k):  # n:배열크기, k:깊이
    if n == k:
        print(*p)
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                p[k] = arr[i]
                perm(n, k + 1)
                visited[i] = 0

arr = [1, 2, 3]
N = len(arr)
p = [0] * N
visited = [0] * N
# perm(N, 0)

# 첫자리 고정
p[0] = arr[0]
visited[0] = 1
perm(N, 1)