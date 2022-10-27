def solution(topping):
    # 토핑의 길이
    length = len(topping)
    # 미리 set을 해 놓기
    left_kind = set()
    right_kind = set()
    # 몇개의 단어가 들어가 있는지 확인하기 위한 리스트
    left_num = []
    right_num = []

    # 정답
    answer = 0

    # left는 왼쪽부터 right는 오른쪽부터 종류 숫자 세기
    for i in range(len(topping) - 1):
        left_kind.add(topping[i])
        right_kind.add(topping[-i - 1])
        left_num.append(len(left_kind))
        right_num.append(len(right_kind))

    # left는 왼쪽부터 right는 오른쪽부터해서 똑같으면 count하기
    kind_num = len(right_num)
    for i in range(kind_num):
        if left_num[i] == right_num[kind_num - 1 - i]:
            answer += 1
    return answer


from collections import Counter


def solution(topping):
    answer = 0
    dic = dict(Counter(topping))
    dic_len = len(dic)
    dic_set = set()

    for now_topping in topping:
        dic[now_topping] -= 1
        if not dic[now_topping]:
            dic_len -= 1
        dic_set.add(now_topping)
        if dic_len == len(dic_set):
            answer += 1

    return answer

