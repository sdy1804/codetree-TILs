arr = list(map(int, input().split()))
cnt_arr = [0] * 10

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]

for j in arr:
    cnt_arr[j//10] += 1

for k in range(1, 10):
    print(f"{k} - {cnt_arr[k]}")