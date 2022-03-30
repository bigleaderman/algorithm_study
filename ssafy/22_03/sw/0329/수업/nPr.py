# nPr

def perm(n, r, k):  # n:배열크기, k:깊이
    if r == k:
        print(*p)
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                p[k] = arr[i]
                perm(n, r, k + 1)
                visited[i] = 0

arr = [1, 2, 3]
N = len(arr)
R = 2
p = [0] * R
visited = [0] * N
perm(N, R, 0)

# 첫자리 고정
# p[0] = arr[0]
# visited[0] = 1
# perm(N, 1)