def distance(k, n):
    global min_value
    if n >= B:
        if min_value > n - B:
            min_value = n - B
        return
    for i in range(k, N):
        n += people[i]
        distance(i + 1, n)
        n -= people[i]

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    people = list(map(int, input().split()))
    min_value = 1000
    distance(0, 0)
    print(f'#{tc} {min_value}')



