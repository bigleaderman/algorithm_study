for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst1.sort()
    temp = set(lst1)
    lst2 = list(map(int, input().split()))
    cnt = 0
    for num in lst2:
        if num in temp:
            config = 2
            l, r = 0, N-1
            # 이 경우를 벗어나면 못찾았음을 의미
            while l <= r:
                m = (l+r)//2
                # 찾았을 때
                if lst1[m] == num:
                    cnt += 1
                    break
                # 값이 더커서 l에 m을 넣어줘서 오른쪽으로 이동
                elif num > lst1[m]:
                    # 처음 config값은 2이고 왼쪽으로 갔을 때는 0이므로 오른쪽으로 이미 한번간 경우 break
                    if config == 1:
                        break
                    else:
                        l = m+1
                        config = 1
                else:
                    # 처음 config값은 2이고 오른쪽으로 갔을 때는 1이므로 왼쪽으로 이미 한번 간 경우 break
                    if config == 0:
                        break
                    else:
                        r = m-1
                        config = 0
    print(f'#{tc} {cnt}')

