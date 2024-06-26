N = int(input())
arr = list(int(input()) for _ in range(N))

now_count, max_count = 0, 0
for i in range(len(arr)):
    if i == 0 or arr[i-1] < arr[i]:
        now_count += 1
        if now_count > max_count:
            max_count = now_count
    else:
        now_count = 1
print(max_count)