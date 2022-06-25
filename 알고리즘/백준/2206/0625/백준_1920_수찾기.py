from sys import stdin

# 입력받기
N = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
find_lst = list(map(int, stdin.readline().split()))

# 정답 list
answer = [0] * M
# list 정렬해서 이분탐색으로 문제 풀이
lst.sort()

# M번 반복해서 찾기
for i in range(M):
    # 스타트를 0, 끝은 N-1로 설정
    s, e = 0, N - 1
    # target을 find_lst i번째 인덱스로 설정
    target = find_lst[i]

    # 이분탐색
    while s <= e:
        mid = (s+e) // 2

        if lst[mid] == target:
            answer[i] = 1
            break

        elif lst[mid] > target:
            e = mid - 1

        else:
            s = mid + 1
    print(answer[i])