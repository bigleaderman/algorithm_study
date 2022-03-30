# nCr

def comb(k, s): # k: 깊이, s: 시작숫자
    if k == R:
        print(*t)
        return
    else:
        for i in range(s, N-R+k+1):
            t[k] = arr[i]
            comb(k+1,i+1)


arr = [1, 2, 3, 4]
N = len(arr)
R = 3
t = [0] * R
comb(0, 0)