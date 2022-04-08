N = int(input())
ratio = []
for _ in range(N):
    lst = list(map(int, input().split()))
    cnt = 0
    avg = sum(lst[1:])/lst[0]
    for score in lst[1:]:
        if score > avg:
            cnt += 1
    ratio.append(cnt/lst[0]*100)
for r in ratio:
    print(f'{r:.3f}%')