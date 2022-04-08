for tc in range(int(input())):
    k, n = int(input()), int(input())
    lst = list(range(1,n+1))
    for _ in range(k):
        for i in range(n, 0, -1):
            lst[i-1] = sum(lst[:i])
    print(lst[n-1])