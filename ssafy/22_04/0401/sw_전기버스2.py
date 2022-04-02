for tc in range(1, int(input()) + 1):
    # 우선 버스 정류장의 숫자까지 list로 받아와서 pop으로 빼준다
    bus_stop = list(map(int, input().split()))
    N = bus_stop.pop(0)
    cnt = 0
    now = 0
    charge = bus_stop[0]
    # 현재 충전량으로 갈 수 있을 경우는 바로 break
    while now + charge < N-1:
        # charge만큼 이동을해서 어느 bus_stop에 갔을 때 가장 좋은지 비교한다.
        max_charge = 0
        for i in range(now+1, now+charge+1):
            can_charge = bus_stop[i] - charge + i - now
            if can_charge > max_charge:
                max_charge = can_charge
                charge_bus_stop = i
        now = charge_bus_stop
        charge = bus_stop[charge_bus_stop]
        cnt += 1
    print(f'#{tc} {cnt}')