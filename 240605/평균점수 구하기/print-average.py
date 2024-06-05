arr = list(map(float, input().split()))

arr_sum = sum(arr)
arr_avg = arr_sum / len(arr)

print(f"{arr_avg:.1f}")