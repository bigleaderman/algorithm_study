for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    for i in range(1, M+1): #피자의 순서를 주기 위해서 반복문 실행
        pizza.append([pizza.pop(0), i])
    make = pizza[0 : N] #화덕에 피자를 다 넣은 것을 가정
    pizza = pizza[N : M]    #남은 피자

    while len(make) != 1:   #화덕에 하나 남을 때 까지 반복
        check = make.pop(0) #queue를 이용하여 피자 check
        check[0] = check[0]//2  #피자의 치즈양을 반으로 줄이기
        if not check[0]:    #피자의 치즈양이 0이고 밖에 피자가 있을 경우 화덕에 넣기
            if pizza:
                make.append(pizza.pop(0))
        else:   #피자를 다시 화덕에 넣기
            make.append(check)
    print(f'#{tc} {make[0][1]}')

