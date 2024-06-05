arr = list(map(int, input().split()))
even_arr = arr[1::2]
odd_arr = arr[2::3]
# print(even_arr)
# print(odd_arr)
even_sum = sum(even_arr)
odd_sum = sum(odd_arr)
odd_avg = odd_sum / len(odd_arr)

print(even_sum, f"{odd_avg:.1f}")