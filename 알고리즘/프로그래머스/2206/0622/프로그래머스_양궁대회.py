# 완탐(10개만 돌면 되기 때문에)
def solution(n, info):
    # 정답
    answer = []
    # 기본 차이를 1로 만들어야 이길 경우
    score_gap = 1

    # dfs
    def dfs(idx, last_num, now_info): # index, 남은 횟수, 현재정보
        # score_gap과 answer은 바꿔야 하므로 nonlocal로 사용해서 함수 안에서도 변경 할 수 있도록한다.
        nonlocal score_gap, answer
        # 맞출 과녁이 0밖에 안남았을 때
        if idx == 10:
            # 0에 몰빵해주기
            now_info[10] += last_num
            # 어피치와 라이언 스코어 비교
            lion_num = 0
            peach_num = 0
            for j in range(len(now_info) - 1):
                if now_info[j] > info[j]:
                    lion_num += 10 - j
                elif info[j]:
                    peach_num += 10 - j

            # 이번 갭차이가 더 클때
            if lion_num - peach_num > score_gap:
                score_gap = lion_num - peach_num
                answer = now_info[:]

            # 같은 갭일 떄에는 젤 작은 수가 어떤쪽이 많은지 생각 해야한다.
            elif lion_num - peach_num == score_gap:
                for j in range(len(now_info)-1, -1, -1):
                    if now_info[j] > answer[j]:
                        answer = now_info[:]
                        break
                    elif now_info[j] < answer[j]:
                        break
            now_info[10] -= last_num

        else:
            # 완탐 이번idx에 수를 넣을 경우와 안 넣을 경우
            if last_num >= info[idx] + 1:
                lst[idx] = info[idx] + 1
                dfs(idx + 1, last_num - 1 - info[idx], now_info)
                lst[idx] = 0
            dfs(idx + 1, last_num, now_info)


    # dfs
    lst = [0] * 11
    dfs(0, n, lst)
    if not answer:
        answer = [-1]

    return answer