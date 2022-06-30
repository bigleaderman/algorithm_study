def solution(record):
    # nickname dictionary
    nickname = {}
    # state와 user을 넣을 list
    lst = []
    # 정답을 넣을 list
    answer = []

    # 반복문
    for i in range(len(record)):
        # split으로 분리한 단어들의 숫자로 enter, change와 leave를 구분
        if len(record[i].split()) == 2:
            state, user = record[i].split()
        else:
            state, user, name = record[i].split()

        # 각 상태별로 list에 값을 넣을 건지 아니면 dictionary value값만 바꿀건지 확인.
        if state == "Enter":
            nickname[user] = name
            lst.append([state, user])
        elif state == "Leave":
            lst.append([state, user])
        else:
            nickname[user] = name

    # 정답들을 answer list에 넣기
    for j in range(len(lst)):
        if lst[j][0] == "Enter":
            answer.append(f"{nickname[lst[j][1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{nickname[lst[j][1]]}님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))