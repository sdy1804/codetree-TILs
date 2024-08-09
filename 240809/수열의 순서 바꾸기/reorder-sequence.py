N = int(input())
arr = list(map(int, input().split()))

# 꼴찌 숫자가 첫번째 숫자보다 크면 첫번째 숫자가 꼴찌 숫자의 앞으로 이동
# 앞으로 이동시, 꼴지와 뒤에서 2번째 숫자 사이에 들어가는 값인지 확인
# 아니라면, 맞을 때까지 앞으로 이동하며 비교하여 찾기
# 꼴찌 숫자가 첫번째 숫자보다 작으면 꼴찌 숫자의 뒤로 이동
# 반복하여 sorting된 arr과 같으면 중단

arr_sorted = sorted(arr)

# first_num = arr[0]
# last_num = arr[-1]
# print(last_num)
# arr = arr[1:-1]
# print(arr)
# arr.append(first_num)
# arr.append(last_num)
# print(arr)

ans = 0
while arr_sorted != arr:
    if arr[0] > arr[-1]:
        first_num = arr[0]
        arr = arr[1:]
        arr.append(first_num)
        ans += 1
        # print(arr)
    elif arr[0] < arr[-1] and arr[1:] != sorted(arr[1:]):
        first_num, last_num = arr[0], arr[-1]
        arr = arr[1:-1]
        arr.append(first_num)
        arr.append(last_num)
        ans += 1
        # print(arr)
    elif arr[0] < arr[-2] and arr[0] < arr[-1]:
        for i in range(1, len(arr)-2):
            # print('arr[0], arr[i]', arr[0], arr[i])
            if (arr[0] > arr[i] and arr[0] < arr[i+1]):
                first_num = arr[0]
                # print('first_num', first_num)
                lower_nums = arr[1:i+1]
                # print('lower_nums', lower_nums)
                arr = arr[i+1:]
                arr.insert(0, first_num)
                # print(arr)
                # lower_nums.extend(arr)
                arr = lower_nums + arr
                ans += 1
                # print(arr)
# print(arr)
print(ans)