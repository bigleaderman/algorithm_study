def card_list():
    cnt_list= []
    for c in range(0, len(card), 3):
        if card[c] == 'S':
            make_card[int(card[c + 1:c + 3])] += 1
        elif card[c] == 'D':
            make_card[13 + int(card[c + 1:c + 3])] += 1
        elif card[c] == 'H':
            make_card[26 + int(card[c + 1:c + 3])] += 1
        elif card[c] == 'C':
            make_card[39 + int(card[c + 1:c + 3])] += 1
    for j in range(1, 53, 13):
        cnt = 0
        for k in range(j, j+13):
            if make_card[k] == 0:
                cnt += 1
            elif make_card[k] > 1:
                return ['ERROR']
        cnt_list.append(cnt)
    return cnt_list


for tc in range(1, int(input())+1):
    card = input()  #카드를 문자열로 받는다
    make_card = [0]*53  #make_card로 있는 카드는 1로 받는다
    print(f'#{tc}', *card_list())