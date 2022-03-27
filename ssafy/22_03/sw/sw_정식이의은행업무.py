def solve(num_three):
    for i in range(len(num_two)):
        # 1비트 값만 바꿔서 10진수 값으로 변환
        num_two[i] = (num_two[i] + 1) % 2

        dec = 0 # 10진수로 변환
        for idx in range(len(num_two)):
            dec = dec * 2 + num_two[idx]

        s = []  # 3 진수로 변환
        ret = dec
        while dec > 0:
            s.append(dec % 3)
            dec //= 3
        num_three = num_three[::-1]

        cnt = 0
        for idx in range(min(len(s), len(num_three))):
            if s[idx] != num_three[idx]:
                cnt += 1
        cnt += abs(len(s) - len(num_three))
        if cnt == 1:
            return ret

        num_two[i] = (num_two[i] + 1) % 2
for tc in range(1, int(input()) + 1):
    num_two = list(map(int, input()))
    num_three = list(map(int, input()))
    ans = solve(num_three)
    print(f'#{tc} {ans}')