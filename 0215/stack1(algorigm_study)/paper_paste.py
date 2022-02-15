import sys
sys.stdin = open('sample_input (2).txt', 'r')

for tc in range(int(input())):
    N = int(input())//10
    fix_N = N
    total = 1
    while N >= 2:
        a_F, a = N // 2, N//2
        b, c = fix_N - a*2, a + b
        a_fac, b_fac, c_fac = 1, 1, 1
        while c > 1:
            c_fac = c_fac * c
            c -= 1
        while b > 1:
            b_fac = b_fac * b
            b -= 1
        while a > 1:
            a_fac = a_fac * a
            a -= 1
        
        total += (2**(a_F))*(c_fac // (b_fac * a_fac))
        N -= 2
    print(f'#{tc+1} {total}')