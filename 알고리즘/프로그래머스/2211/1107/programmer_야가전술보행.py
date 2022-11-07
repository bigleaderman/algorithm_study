# greedy로 접근했는데 실패
# import copy
# def solution(distance, scope, times):
#     copy_list = copy.deepcopy(scope)
#     for i in range(len(copy_list)):
#         copy_list[i].sort()
#         scope[i].sort()
#     copy_list.sort()
#     answer = distance
#     for now in copy_list:
#         s_scope, e_scope = now[0], now[1]
#         time_index = scope.index(now)
#         work_time, rest_time = times[time_index][0], times[time_index][1]
#         sum_time = work_time + rest_time
#         # 스코프 시작점과, 끝점으 경비병의 근무, 휴식시간의 합으로 나눴을 때 몫이 다르고 끝 스코프를 총합시간으로 나눴을 때 영이 아니면 무조건 걸린 것이다.
#         # 그리고 시작점을 근무시간의 합으로 나눈 나머지값이 일하는 시간보다 작거나 같고 1보다 크면 걸린 것이다,
#         if (s_scope//sum_time != e_scope//sum_time and e_scope%sum_time != 0) or 1 <= s_scope%sum_time <= work_time or 1 <= e_scope%sum_time <= work_time:
#             for i in range(s_scope, e_scope + 1):
#                 if 1 <= i % sum_time <= work_time:
#                     answer = i
#                     break
#         if answer != distance:
#             break
        
#     return answer


# 완탐으로 돌려야한다.
def solution(distance, scope, times):
    ch = []
    for i in range(len(scope)):
        start, end = sorted(scope[i])
        work, rest = times[i]
        time = start
        while time <= end:
            N = time % (work+rest)
            if 0 < N <= work:
                ch.append(time)
                break
            time += 1

    if ch: return sorted(ch)[0]
    else:  return distance