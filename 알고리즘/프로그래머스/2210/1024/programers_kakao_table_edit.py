def solution(n, k, cmd):
    # 정답 리스트
    answer_list = ['O'] * n
    # 링크드 리스트 흉내
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    # 삭제 된 것을 넣는 리스
    delete_list = []
    # 현재 위치
    now = k
    # 첫위치와 끝위치 변경
    linked_list[0][0] = None
    linked_list[n - 1][1] = None

    for order in cmd:
        if order[0] == 'C':
            # 정답 리스트 변경
            answer_list[now] = 'X'
            # 수치값 확보하기
            pre, adv = linked_list[now]
            # delete_list를 통해서 삭제된 것들 확보하기
            delete_list.append([pre, now, adv])
            # linked_list 수정
            if pre == None:
                linked_list[adv][0] = None
            elif adv == None:
                linked_list[pre][1] = None
            else:
                linked_list[adv][0] = pre
                linked_list[pre][1] = adv

            # now 위치 변경
            # 만약 현재 위치의 링크드 리스트 다음이 None이면 앞으로 이동
            if adv == None:
                now = pre
            # 없으면 뒤로 이동
            else:
                now = adv
        # 복귀하는 것은 C의 반대로 하면된다.
        elif order[0] == "Z":
            del_pre, del_now, del_adv = delete_list.pop()
            answer_list[del_now] = 'O'
            if del_pre == None:
                linked_list[del_adv][0] = del_now
            elif del_adv == None:
                linked_list[del_pre][1] = del_now
            else:
                linked_list[del_pre][1] = del_now
                linked_list[del_adv][0] = del_now
        # 이동하는 것은 링크드 리스트 연결된 것을 타고 이동하면 된다.
        else:
            method, value = order.split()
            if method == "U":
                for _ in range(int(value)):
                    now = linked_list[now][0]
            else:
                for _ in range(int(value)):
                    now = linked_list[now][1]

    return ''.join(answer_list)