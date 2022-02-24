for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    print(f'#{tc}')
    if m == 1:
        for i in range(1, n+1):
            print('*' * i)
    elif m == 2:
        for i in range(n , 0, -1):
            print('*' * i)
    elif m == 3:
        for i in range(1, n+1):
            print(' ' * (n - i) + '*' * (2*i - 1) + ' ' * (n - i))