N = int(input())
arr = list(map(int, input().split()))

# 각 자릿수는 합보다 작은 수이며 1보다 큰 수
# 수열 첫째자리가 정해지면 차이값에 의해 나머지 값들도 정해짐
# ex) 1, 2, 3에 따라 뒤에 값들이 정해짐
# 리스트에 첫째값 넣어놓고 나머지는 앞에 값에 대한 차이값을 넣으면 될듯
total_arr = []
none_arr = []
for i in range(1, arr[0]):
    now_list = []
    now_list.append(i)
    for j in range(N-1):
        # print(j)
        # print('now_sum, now_list[j]', arr[j], now_list[j])
        now_val = arr[j] - now_list[j]
        if (now_val <= 0) or (now_val in now_list):
            break
        else:
            now_list.append(now_val)
        # print('now_list', now_list)
    if len(now_list) == N:
        total_arr.append(now_list)
# print('total_arr', total_arr)
total_arr.sort()
# print('total_arr', total_arr)
for elem in total_arr[0]:
    print(elem, end=" ")