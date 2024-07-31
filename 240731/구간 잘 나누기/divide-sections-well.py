n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 최댓값을 어떻게 만들어 나갈 것인가??
# 예를 들어 최댓값 8일 때, 어떻게 8을 만드는 구간을 찾아서 자를 것인가??
# -> 딱 8을 만들어내는 것이 아닌, 최대값의 기준으로 그 이상 커지지 않도록 앞에서부터 만들기

####################################################################################
# 토론 참고 풀이

# for val_max in range(max(arr), sum(arr)+1):
#     parts = arr[0]
#     temp_sum = []
#     for i in range(1, n):
#         if parts + arr[i] > val_max:
#             temp_sum.append(parts)
#             parts = arr[i]
#         else:
#             parts += arr[i]
#     temp_sum.append(parts)
#     # print(temp_sum)
#     if len(temp_sum) <= m:
#         # print(len(temp_sum))
#         print(val_max)
#         break

################################################################
# 해설 참고 풀이

MAX_VAL = 10000
ans = MAX_VAL
for i in range(1, MAX_VAL+1):
    possible = True # 구간을 나눌 수 있는지
    section = 1 # 구간의 수
    cnt = 0
    for j in range(n):
        if arr[j] > i:
            possible = False
            break
        if arr[j] + cnt > i:
            cnt = 0
            section += 1
        cnt += arr[j]
        # print('cnt', cnt)
        # print('section', section)
    if possible and section <= m:
        ans = min(ans, i)
print(ans)