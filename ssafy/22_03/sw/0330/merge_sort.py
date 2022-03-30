from collections import deque

'''
8
69 10 30 2 16 8 31 32
'''

def merge(l, r):
    global cnt
    # 두개의 정렬된 리스트를
    # 정렬된 하나의 리스트로 만들어서 반환
    result = []

    # cnt파악
    if l[-1] > r[-1]:
        cnt += 1

    # 병합과정
    # 각각의 최소값들(가장 왼쪽 값)을 비교해서
    # 더 작은 요소를 결과에 추가
    while l or r:
        # 두 리스트가 모두 존재하면
        if l and r:
            if l[0] <= r[0]:
                result.append(l.pop(0))
            else:
                result.append(r.pop(0))
        elif l:
            result.extend(l)
            l = []
        elif r:
            result.extend(r)
            r = []
    return  result


def merge_sort(a):
    # 종료조건(basis part)
    if len(a) == 1:
        return a

    # 문제를 절반으로 나누어서 각 별도의 정렬을 실행
    middle = len(a)//2
    left = a[:middle]
    right = a[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)   # 비파괴 메소드
    print(arr[N//2], cnt)