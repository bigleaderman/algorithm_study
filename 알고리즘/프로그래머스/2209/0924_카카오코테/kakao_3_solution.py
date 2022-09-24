

import copy

def solution(users, emoticons):
    # 이건 완전탐색이다
    # 각 세일되는 경우를 모두 계산하여 가입자 수 및 비용을 구한다.
    answer = [0, 0]
    sale = [0.9, 0.8, 0.7, 0.6]
    # 첫번째는 세일 정도, 두번 째는 이모티콘 가격
    purchase_price = [[0, 0] for _ in range(len(emoticons))]
    num = len(emoticons)

    def find_price(count):

        # 모든 이모티콘을 둘러 봣을때
        if count == num:
            sum_price = [0] * len(users)
            for i in range(len(users)):
                for j in range(len(purchase_price)):
                    if users[i][0] <= purchase_price[j][0]:
                        sum_price[i] += purchase_price[j][1]

            number = 0
            for i in range(len(users)):
                # 이 유저가 구매했던 가격이 유저의 제한 값을 넘어 섰을때
                if sum_price[i] > users[i][1]:
                    number += 1
                    sum_price[i] = 0

            if number > answer[0]:
                answer[0] = number
                answer[1] = sum(sum_price)
            elif number == answer[0] and sum(sum_price) > answer[1]:
                answer[1] = sum(sum_price)
            return

        # 아니면 user_price 만들기
        # 한 상품에 총 네가지 세일하기
        for i in range(4):
            # 세일정도와 물건 가격 넣기
            purchase_price[count][0] = (i+1) * 10
            purchase_price[count][1] = emoticons[count] * sale[i]
            find_price(count + 1)
    find_price(0)
    return answer

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))