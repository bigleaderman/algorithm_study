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
    i, j = 0, 0
    len_l, len_r = len(l), len(r)
    while len_l != i or len_r != j:
        # 두 리스트가 모두 존재하면
        if len_l != i and len_r != j:
            if l[i] <= r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        elif len_l != i:
            result.extend(l[i:])
            i = len_l
        elif len_r != j:
            result.extend(r[j:])
            j = len_r
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
    print(f'#{tc} {arr[N//2]} {cnt}')