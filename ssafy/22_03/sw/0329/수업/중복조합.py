
def comb(n, r):
    if r == 0:
        print(*T)
    elif n == 0: return
    else:
        T[r-1] = arr[n-1]
        comb(n, r-1)
        comb(n-1, r)


arr = [1, 2, 3, 4]
N = len(arr)
R = 3
T = [0] * R
comb(N, R)