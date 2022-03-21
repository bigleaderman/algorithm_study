for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pizza = [[idx, value] for idx, value in enumerate(map(int, input().split()), start=1)]
    stack = []
    for _ in range(N):
        stack.append(pizza.pop(0))

    while len(stack) != 1:
        now = stack.pop(0)
        now[1] //= 2
        if now[1]:
            stack.append(now)
        else:
            if pizza:
                stack.append(pizza.pop(0))
    print(f'#{tc}', stack[0][0])
