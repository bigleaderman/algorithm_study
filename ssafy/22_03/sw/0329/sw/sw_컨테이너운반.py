for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    total = 0
    # 트럭값이 큰 값부터 이동
    for truck in trucks[::-1]:
        # 이 트럭이 이동할 수 있는 최대 컨터에너
        for i in range(len(containers) - 1, -1, -1):
            # 큰 값순으로 오기 때문에 truck보다 작으면 바로 들고가기
            if truck >= containers[i]:
                total += containers[i]
                containers.pop(i)
                break
    print(f'#{tc} {total}')
