arr = list(map(int, input().split()))
cnt_arr = [0]*7

for i in arr:
    cnt_arr[i] += 1

for j in range(1,7):
    print(f"{j} - {cnt_arr[j]}")