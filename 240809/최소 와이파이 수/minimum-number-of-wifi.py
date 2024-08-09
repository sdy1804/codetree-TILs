n, m = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)

# idea 1. 처음 1을 만났을 때, m칸 만큼 뒤로 가서 와이파이 꽂기
wifi_cnt = 0
i = 0
while i < n:
    if arr[i] == 0:
        i += 1
    elif arr[i] == 1:
        i = i + m
        wifi_cnt += 1
        i += m
        i += 1
    # print('wifi_cnt', wifi_cnt)
    # print(i)
print(wifi_cnt)