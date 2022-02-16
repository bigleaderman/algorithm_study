for tc in range(int(input())):
    num = int(input())
    carrots = list(map(int, input().split()))
    total = max_total = 1
    pre_c = carrots[0]
    for i in carrots:
        if i > pre_c:
            total += 1
            pre_c = i
            if total > max_total:
                max_total = total
        else:
            total = 1
            pre_c = i
    print(f'#{tc+1} {max_total}')
