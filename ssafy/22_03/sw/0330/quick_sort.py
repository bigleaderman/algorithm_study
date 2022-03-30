'''
6
11 45 23 81 28 34
10
11 45 22 81 23 34 99 22 17 8
10
1 1 1 1 1 0 0 0 0 0
9
0 0 0 0 0 1 1 1 1
'''

def quick(a, l, r): #l은 왼쪽좌표, r은 오른쪽 좌표
    pibot = a[l]
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= pibot:
            i += 1
        while i <= j and a[j] >= pibot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def quick_sort(a, l, r):
    if l < r:
        s = quick(a, l, r)
        quick_sort(a, l, s-1)
        quick_sort(a, s+1, r)

N = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr)-1)
print(arr)