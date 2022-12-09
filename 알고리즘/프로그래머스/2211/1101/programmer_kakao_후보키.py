from collections import deque
def solution(relation):
    answer = 0
    queue = deque()
    column_length = len(relation[0])
    access_list = [1] * len(relation[0])
    for i in range(len(relation[0])):
        queue.append([i])
    while queue:
        conf = 1
        now_list = queue.popleft()
        check_list = [[] for _ in range(len(relation))]
        check_list2 = []
        for num in now_list:
            if not access_list[num]:
                conf = 0
        if not conf:
            continue
        for i in range(len(relation)):
            for num in now_list:
                check_list[i].append(relation[i][num])
        for item in check_list:
            if item not in check_list2:
                check_list2.append(item)

        if len(check_list) == len(check_list2):
            answer += 1
            for num in now_list:
                access_list[num] = 0
        for i in range(max(now_list) + 1, column_length):
            if access_list[i]:
                queue.append(now_list + [i])


    return answer

question = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(question))