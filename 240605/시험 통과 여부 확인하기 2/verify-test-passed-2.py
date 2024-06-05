n = int(input())
pass_cnt = 0

for i in range(n):
    arr = list(map(int, input().split()))
    arr_sum = 0
    arr_avg = 0
    
    arr_sum = sum(arr)
    arr_avg = arr_sum / len(arr)

    if arr_avg >= 60:
        print("pass")
        pass_cnt += 1
    else:
        print("fail")
print(pass_cnt)