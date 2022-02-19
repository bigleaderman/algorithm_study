for tc in range(int(input())):
    print(f'#{tc+1}', end=' ')
    bus_stop = [0]*5000
    for _ in range(int(input())):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bus_stop[i-1] += 1
    for _ in range(int(input())):
        print(bus_stop[int(input())-1], end=' ')
    print()
