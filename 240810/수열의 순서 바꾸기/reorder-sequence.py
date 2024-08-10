N = int(input())
arr = list(map(int, input().split()))

# 뒤에 있는 숫자들이랑 비교해 나가는 방식
# 뒤에 있는 숫자들보다 크면 뒤에 두기
# 뒤에 있는 숫자들보다 작으면 정렬이 되어있는 곳 앞까지 가기 -> 앞 숫자가 뒤 숫자보다 작은 경우까지

arr_sorted = sorted(arr)

idx = -1
ans = 0
while arr != arr_sorted:
    if arr[0] > arr[-1]: # 맨 앞이 맨 뒤보다 큰 경우 - 그냥 뒤로 붙임
        first_num = arr[0]
        arr = arr[1:]
        arr.append(first_num)
        idx -= 1
        ans += 1
        # print('ans', ans)
        # print('숫자가 커서 뒤로 붙은 경우', arr)
    else: # 맨 앞이 맨 뒤보다 작은 경우
        for i in range(-1, -len(arr_sorted), -1):
            if arr[i] > arr[i-1] and (arr[0] < arr[i] and arr[0] < arr[i-1]):
                # print('arr[0], arr[i-1], arr[i]', arr[0], arr[i-1], arr[i])
                continue
            elif arr[i] > arr[i-1] and (arr[0] > arr[i-1] and arr[0] < arr[i]):
                # print('arr[0], arr[i-1], arr[i]', arr[0], arr[i-1], arr[i])
                first_num = arr[0]
                last_nums = arr[i:]
                arr = arr[1:i]
                arr.append(first_num)
                arr = arr + last_nums
                ans += 1
                # print(arr)
                break
            elif arr[i] < arr[i-1] and arr[0] < arr[i]:
                # print('arr[0], arr[i-1], arr[i]', arr[0], arr[i-1], arr[i])
                first_num = arr[0]
                last_nums = arr[i:]
                arr = arr[1:i]
                arr.append(first_num)
                arr = arr + last_nums
                ans += 1
                # print(arr)
                break
# print(arr)
print(ans)