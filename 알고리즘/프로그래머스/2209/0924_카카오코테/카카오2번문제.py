def solution(cap, n, deliveries, pickups):
    num = 0
    # 배달할 집이 있는지 없는지 처음 확인
    if sum(deliveries) + sum(pickups):
        deliveries_num = n - 1
        pickups_num = n - 1


        now_deliveries_cap = cap
        now_pickups_cap =cap

        # 배달, 수거할게 남아 있는지 하고 남아 있으면 반복
        while deliveries_num >= 0 or pickups_num >= 0:
            config_deliver = 1
            # 한번 돌때 수거할 count
            now_count = 1
            # 배달 할게 남아 있는지 확인
            if deliveries_num >= 0:
                # 끝에서 부터 배달하기
                for i in range(deliveries_num, -1, -1):
                    # 그곳이 배송할게 있는지 확인하기
                    if deliveries[deliveries_num]:
                        if config_deliver:
                            now_count += deliveries_num
                            config_deliver = 0
                        # 배송할 수 있는것보다 배송받을게 클거
                        if deliveries[deliveries_num] > now_deliveries_cap:
                            deliveries[deliveries_num] = deliveries[deliveries_num] - now_deliveries_cap
                            now_deliveries_cap = cap
                            break

                        elif deliveries[deliveries_num] == now_deliveries_cap:
                            deliveries[deliveries_num] = 0
                            now_deliveries_cap = cap
                            deliveries_num -= 1
                            break

                        else:
                            now_deliveries_cap -= deliveries[deliveries_num]
                            deliveries[deliveries_num] = 0
                            deliveries_num -= 1
                    else:
                        deliveries_num -= 1

            if pickups_num >= 0:
                config_pickup = 1
                # 끝에서 부터 픽업하기
                for i in range(pickups_num, -1, -1):
                    # 그곳이 배송할게 있는지 확인하기
                    if pickups[pickups_num]:
                        if config_pickup:
                            if pickups_num + 1 > now_count:
                                now_count = pickups_num + 1
                            config = 0
                        # 배송할 수 있는것보다 배송받을게 클거
                        if pickups[pickups_num] > now_pickups_cap:
                            pickups[pickups_num] = pickups[pickups_num] - now_pickups_cap
                            now_pickups_cap = cap
                            break

                        elif pickups[pickups_num] == now_pickups_cap:
                            pickups[pickups_num] = 0
                            now_pickups_cap = cap
                            pickups_num -= 1
                            break

                        else:
                            now_pickups_cap -= pickups[pickups_num]
                            pickups[pickups_num] = 0
                            pickups_num -= 1
                    else:
                        pickups_num -= 1

            num += now_count * 2

    return num


solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])