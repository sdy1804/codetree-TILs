N = int(input())
arr = list(int(input()) for _ in range(N))

now_count, max_count = 0, 0
for i in range(len(arr)):
    if i == 0 or (arr[i-1] < 0 and arr[i] < 0) or (arr[i-1] > 0 and arr[i] > 0):
        now_count += 1
        if now_count > max_count:
            max_count = now_count
    elif (arr[i-1] < 0 and arr[i] > 0) or (arr[i-1] > 0 and arr[i] < 0):
        now_count = 1
print(max_count)