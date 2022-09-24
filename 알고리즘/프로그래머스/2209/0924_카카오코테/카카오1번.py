def solution(today, terms, privacies):
    # 정답을 담을 리스트
    answer = []

    # 날짜를 int로 바꾸기
    today = int(today.replace(".", ""))

    # terms을 dictionary로 만들어 유효기간을 파악하기 쉽게 만들기
    terms_dic = {}
    for i in range(len(terms)):
        limit_kind, limit_day = terms[i].split(" ")
        terms_dic[limit_kind] = int(limit_day)

    # privacies를 반복문으로 돌려 유효기간 지난 것들 확인하기
    for i in range(len(privacies)):
        # 개인정보수집일자, 약관종류
        day, kind = privacies[i].split(" ")

        # 달만 뽑아서 계산
        month = int(day[5:7])
        month += terms_dic[kind]

        plus_year = month // 12
        month = month %  12

        day = int(day.replace(".", ""))

        end_day = day - day % 10000 + day % 100 + month*100 + plus_year*10000

        if today >= end_day:
            answer.append(i+1)


    return answer





