for tc in range(1, int(input()) + 1):
    N = int(input())
    tree = [0] * (N + 1)

    # 1이 들어갈 idx 넣기 찾기 ex) 1이면 1, 2~3이면 2, 4~7이면 4이므로 다음과 같은 식을 넣었다.
    a = 1
    while a <= N:
        a *= 2
    a = a // 2
    stack = [a]

    # 트리를 순회하면서 값넣기 첫 value는 1
    value = 1
    while stack:
        idx = stack.pop(0)
        tree[idx] = value
        value += 1
        # 오른쪽 트리 도착을 가정
        if idx == 1:
            if a + a//2 <= N:
                stack = [a + a//2]
            else:
                stack = [a//2 + a//2//2]
            continue
        # 왼쪽 자식 요소가 있는지와 방문 체크
        if idx * 2 <= N and not tree[idx * 2]:
            stack.append(idx * 2)
        # 오른쪽 자식 요소 있는지와 방문 체크
        if idx * 2 + 1 <= N and not tree[idx * 2 + 1]:
            stack.append(idx * 2 + 1)
        # 부모요소의 방문 체크와 부모요소의 idx 0이 아님을 체크
        if idx // 2 and not tree[idx//2]:
            stack.append(idx//2)
        print(tree)
        print(stack)
    print(f'#{tc}', tree[1], tree[N//2])