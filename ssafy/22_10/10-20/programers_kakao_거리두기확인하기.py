def solution(places):
    # 정답 넣을 리스트
    answer = []
    # 대기실을 반복해서 돌기
    for now_list in places:
        # P있는 곳을 찾기
        conf = 1
        for i in range(5):
            if conf:
                for j in range(5):
                    if conf:
                        if now_list[i][j] == 'P':
                            # x, y 각 1을 더하는 과정
                            for x, y in [[0, 1], [1, 0]]:
                                # 사각형 범위 안에 있을 때
                                if i + x < 5 and j + y < 5:
                                    # 그리고 그게 P이면 무조건 실패한 대기실
                                    if now_list[i+x][j+y] == 'P':
                                        answer.append(0)
                                        conf = 0
                                        break
                            # 이전에 대기실이 모두 조건을 만족하고
                            if conf:
                                # x, y차이가 2인 과정
                                for x, y in [[2, 0], [0, 2], [1, 1], [-1, 1]]:
                                    # 범위 내에 있고
                                    if 0 <= i + x < 5 and 0 <= j + y < 5:
                                        # 그 값이 P일때
                                        if now_list[i+x][j+y] == 'P':
                                            # 세로
                                            if x == 2:
                                                if now_list[i+1][j] == 'O':
                                                    answer.append(0)
                                                    conf = 0
                                                    break
                                            # 아래대각
                                            elif x == 1:
                                                if now_list[i+1][j] == 'O' or now_list[i][j+1] == 'O':
                                                    answer.append(0)
                                                    conf = 0
                                                    break
                                            # 가로
                                            elif x == 0:
                                                if now_list[i][j+1] == 'O':
                                                    answer.append(0)
                                                    conf = 0
                                                    break
                                            # 위대각
                                            elif x == -1:
                                                if now_list[i-1][j] == 'O' or now_list[i][j+1] == 'O':
                                                    answer.append(0)
                                                    conf = 0
                                                    break
        if conf:
            answer.append(1)
    return answer