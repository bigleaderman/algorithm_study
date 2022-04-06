def find(n):
    if people[n] == n:
        return n
    else:
        return find(people[n])

def union(a, b):
    people[find(b)] = find(a)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    select = list(map(int, input().split()))
    people = list(range(N + 1))
    cnt = set()
    for i in range(len(select)//2):
        union(select[2*i], select[2*i+1])
    for i in range(1, len(people)):
        cnt.add(find(i))
    print(f'#{tc} {len(cnt)}')