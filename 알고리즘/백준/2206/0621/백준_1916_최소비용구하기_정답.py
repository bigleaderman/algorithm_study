from sys import stdin
import heapq

# input 받기
N = int(stdin.readline())
M = int(stdin.readline())

# index를 이용해서 간선의 위치를 파악 할수 있게 해주는 list만들기
lst = [[] for _ in range(N+1)]

# 최소비용을 찾는거기 때문에 각 위치까지 도착할 비용을 최대로 잡기
inf = int(1e9)
cost_lst = [inf] * (N+1)

# 출발 index에 [도착, cost]를 append 하기
for i in range(M):
    S, E, C = list(map(int, stdin.readline().split()))
    lst[S].append([E, C])

# 출발지, 도착지 받아오기
s, e = map(int, stdin.readline().split())

# 출발지는 비용이 0이므로 0으로 만들어주고, Q에 (비용, 출발지) 리스트로 넣기
cost_lst[s] = 0
Q = [(0, s)]

# 다익스트라
while Q:
    # 현 위치까지 오는데 비용, 현 위치
    c, n = heapq.heappop(Q)
    # heapq를 쓰기 때문에 이전에 방문했던 곳이면 pass
    if cost_lst[n] == c:
        # lst안에 들어있는 갈수있는곳과 cost 파악하기
        for go, cost in lst[n]:
            now_cost = cost_lst[n] + cost
            # 갈곳의 비용이 계산한 비용보다 클 때에만 가게하기
            if cost_lst[go] > now_cost:
                cost_lst[go] = now_cost
                heapq.heappush(Q, (now_cost, go))
print(cost_lst[e])
