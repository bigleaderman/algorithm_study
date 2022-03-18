# import heapq
#
# heap = [7, 2, 5, 3, 4, 6, 13, 15]
# heapq.heapify(heap) # 한번에 히브로 변환
# print(heap)
# heapq.heappush(heap, 1)
# print(heap)
# while heap:
#     print(heapq.heappop(heap), end=' ')


################
import heapq

heap = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(heap)):  # heapq는 어떻게든 최소힙으로 밖에 안되므로 -를 붙여줘서 최소힙으로 만든 후 출력할 때 다시한번 - 붙여줘서 최대힙을 만들수 있게한다.
    heapq.heappush(heap2, -heap[i])
print(heap2)