from sys import stdin
def f(n, cnt):
    global  min_cnt
    if cnt >= min_cnt:
        return
    if n == 1:
        min_cnt = cnt
    else:
        if not n % 3:
            f(n//3, cnt+1)
        if not n % 2:
            f(n//2, cnt+1)
        f(n-1, cnt+1)



N = int(stdin.readline())
cnt = 0
min_cnt = 10 ** 6
f(N, 0)
print(min_cnt)