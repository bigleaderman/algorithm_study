import math

for tc in range(1, int(input()) + 1):
    n = int(input())
    a = int(n ** (1/3))
    if a ** 3 == n:
        print(f'#{tc} {a}')
    elif (a + 1) ** 3 == n:
        print(f'#{tc}', a+1)
    else:
        print(f'#{tc} {-1}')

for tc in range(1, int(input()) + 1):
    n = int(input())
    i = 1
    flag = 0
    while n >= i ** 3:
        if i ** 3 == n:
            flag = 1
            break
        else:
            i += 1
    if flag:
        print(f'#{tc} {i}')
    else:
        print(f'#{tc} {-1}')