arr = list(map(int, input().split()))
cnt_arr = [0]*10

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

for j in arr:
    if j//10 > 0 and j//10 < 10:
        cnt_arr[j//10] += 1
    elif j // 10 == 0:
        continue
    elif j // 10 == 10:
        cnt_arr[0] += 1

for k in range(100, 0, -10):
    if k == 100:
        print(f"{k} - {cnt_arr[0]}")
    else:
        print(f"{k} - {cnt_arr[k//10]}")