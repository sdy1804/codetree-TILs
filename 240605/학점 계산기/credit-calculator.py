n = int(input())
score_arr = list(map(float, input().split()))

arr_sum = sum(score_arr)
arr_avg = arr_sum / len(score_arr)
print(f"{arr_avg:.1f}")

if arr_avg >= 4.0:
    print("perfect")
elif arr_avg >= 3.0:
    print("Good")
else:
    print("Poor")