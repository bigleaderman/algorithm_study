
def partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= p:
            i += 1
        while i <= j and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def quick_sort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quick_sort(lst, l, s - 1)
        quick_sort(lst, s + 1, r)

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, N-1)
    print(f'#{tc} {lst[N//2]}')