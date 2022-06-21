import heapq
def solution(N, road, K):
    # index를 통해서 간선의 위치를 파악해주기 위해서 list 만들기
    lst = [[] for _ in range(N + 1)]
    # 출바 index애 [cost, 도착index]를 넣어서 list 간선 만들어 주기
    for s, e, c in road:
        lst[s].append([c, e])
        lst[e].append([c, s])

    # cost는 최대한 큰 값으로 사용
    inf = int(1e9)
    cost = [inf] * (N + 1)

    # 1번에서 출발하므로 cost[1]은 0을 넣고 Q에 (비용, 현재위치) 넣기
    cost[1] = 0
    Q = [(0, 1)]

    # heapq를 할용한 다익스트라 구현
    while Q:
        c, n = heapq.heappop(Q)
        if cost[n] == c:
            for go_cost, go in lst[n]:
                now_cost = go_cost + cost[n]
                if cost[go] > now_cost and now_cost <= K:
                    cost[go] = go_cost + cost[n]
                    heapq.heappush(Q, (now_cost, go))
    answer = sum([1 if cost[i] <= K else 0 for i in range(1, N+1)])
    return answer

print(solution(5, 	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))