for tc in range(1, int(input())+1):
    n ,m = map(int, input().split())
    print(f'#{tc}')
    if m == 1:
        for i in range(1, n//2 + 2):
            print('*'*i)
        for i in range(n//2,0,-1):
            print('*'*i)
    elif m == 2:
        for i in range(1, n // 2 + 2):
            print(' '*(n//2+1 - i) + '*' * i)
        for i in range(n // 2, 0, -1):
            print(' '*(n//2+1 - i) + '*' * i)
    elif m == 3:
        for i in range(n, 0, -2):
            print(' ' * ((n-i)//2) + '*'*i + ' ' * ((n-i)//2))
        for i in range(3, n+1, 2):
            print(' ' * ((n-i)//2) + '*'*i + ' ' * ((n-i)//2))
    elif m == 4:
        for i in range(n // 2 + 1, 0, -1):
            print(' ' * (n // 2 + 1 - i) + '*' * i)
        for i in range(2, n//2+2):
            print(' ' * (n // 2) + '*' * i)