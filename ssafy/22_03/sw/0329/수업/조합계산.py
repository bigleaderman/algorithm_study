def comb(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return comb(n-1, r-1) + comb(n-1, r)


arr = [1, 2, 3, 4]
N = len(arr)
R = 3
T = [0] * R
print(comb(N, R))