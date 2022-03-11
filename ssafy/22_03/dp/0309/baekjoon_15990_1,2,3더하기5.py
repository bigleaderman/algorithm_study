from sys import stdin

def f(n, card_number):

    # 카드를 끝난 숫자만 카운트를 하기 위해서 세개의 value를 가지는 list를 만들었다.
    card = [[0, 0, 0] for _ in range(100000)]
    # 1, 2, 3일때는 미리 만들었다.
    card[0] = [1, 0, 0] # 1
    card[1] = [0, 1, 0] # 2
    card[2] = [1, 1, 1] # 3

    # 처음에 3차원으로 하다가 이건 아니다 싶어서 2차원으로 생각했습니다.
    # 돌아가면서 1,2,3차이 나는 수자에 마지막 숫자가 다른 수를 더하기
    # card를 계산할때 계속 나눠줘서 메모리와 시간을 줄여야한다.
    for i in range(3, n):
        card[i][0] = (card[i-1][1] + card[i-1][2]) % 1000000009
        card[i][1] = (card[i-2][0] + card[i-2][2]) % 1000000009
        card[i][2] = (card[i-3][0] + card[i-3][1]) % 1000000009
    # card_number의 카드수를 card_list에 담기
    card_list = [sum(card[i-1]) for i in card_number]
    return card_list

num = int(stdin.readline())
# card_number중 최대인 카드 number으로만 카드 수를 계산해서 그 파생된 값들을 통해서 최대값 보다 작은 값들 계산
card_number = [0] * num
for i in range(num):
    card_number[i] = int(stdin.readline())
count_card = f(max(card_number), card_number)
for number in count_card:
    print(number % 1000000009)