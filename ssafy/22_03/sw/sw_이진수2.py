def find_bin(n):
    asw = ''
    cnt = 0
    while cnt < 12:
        n = n * 2
        if n >= 1:
            asw += '1'
            n -= 1
        else:
            asw += '0'
        if n == float(0):
            return asw
        cnt += 1
    return 'overflow'

for tc in range(1, int(input()) + 1):
    N = float(input())
    print(f'#{tc} {find_bin(N)}')
    print(float(0))