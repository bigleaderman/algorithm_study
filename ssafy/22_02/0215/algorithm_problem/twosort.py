import sys
sys.stdin = open('sample_input (2).txt', 'r')

for tc in range(int(input())):
    P, A, B = map(int, input().split())
    A_r, B_r, A_l, B_l, n_a, n_b = P, P, 1, 1, 0, 0
    while True:
        n_a += 1
        c_a = (A_l + A_r) // 2
        if c_a > A:
            A_r = c_a
        elif c_a < A:
            A_l = c_a
        else:
            break
    while True:
        n_b += 1
        c_b = (B_l + B_r) // 2
        if c_b > B:
            B_r = c_b
        elif c_b < B:
            B_l = c_b
        else:
            break
    if n_a > n_b:
        print(f'#{tc+1} B')
    elif n_b > n_a:
        print(f'#{tc+1} A')
    else:
        print(f'#{tc+1} 0')