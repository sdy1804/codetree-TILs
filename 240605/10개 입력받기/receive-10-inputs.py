arr = list(map(int, input().split()))
reverse = arr[::-1]

for i in range(len(reverse)):
    if reverse[i] == 0:
        reverse = reverse[i+1:]
        break

arr_sum = sum(reverse)
arr_avg = arr_sum / len(reverse)

print(arr_sum, f"{arr_avg:.1f}")