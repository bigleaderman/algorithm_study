from sys import stdin
import copy

def find_paper():
    global min_cnt
    # 최고 큰 종이가 5,4,3,2인 기준으로 나눠서 붙여야한다.
    for n in range(5, 1, -1):
        papers = [5, 5, 5, 5, 5]
        arr = copy.deepcopy(arr1)
        cnt = 0
        flag1 = 1
        while n > 0:
            # n만큼 넓이를 가진 paper가 있다는것
            flag = 1
            for i in range(10):
                # 가지치기
                if cnt >= min_cnt:
                    n = 0
                    break
                # n을 교체
                if not flag:
                    break
                for j in range(10):
                    # n 교체
                    if not flag:
                        break
                    # arr이 1이면
                    if arr[i][j]:
                        # 그리고 붙일 색종이가 범위 내일 때
                        if i + n <= 10 and j + n <= 10:
                            total = 0
                            # 붙일 색종의 크기 만큼 1이 있는지 확인
                            for k in range(n):
                                total += sum(arr[i + k][j:j + n])
                            # 붙일 색종이가 알맞은 크기이면  cnt를 더하고 그 페이퍼를 뺀다
                            if total == n ** 2:
                                cnt += 1
                                papers[n-1] -= 1
                                # 그 범위 만큼을 0으로 만들어준다.
                                for a in range(n):
                                    for b in range(n):
                                        arr[i + a][j + b] = 0
                                # 만약 색종이의 수가 0이면 이제 이 종이는 못쓴다.
                                if not papers[n-1] and n != 1:
                                    flag = 0
                                # 만약 색종이가 1이면 이것을 붙일 수 없는 종이임
                                if papers[n-1] == -1:
                                    flag1 = 0
                                    flag = 0

            n -= 1
        # 크기가 1일 종이에서도 못 붙였을 때는 최소값 계산을 하면 안된다.
        if flag1:
            min_cnt = min(cnt, min_cnt)


arr1 = [list(map(int, stdin.readline().split())) for _ in range(10)]
min_cnt = 9999
find_paper()
print(-1 if min_cnt == 9999 else min_cnt)