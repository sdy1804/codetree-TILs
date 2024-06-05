arr = list(map(int, input().split()))
odd_sum = 0
even_sum = 0

for i in range(len(arr)):
    if i % 2 == 0:  #odd sum
        odd_sum += arr[i]
    else: # even sum
        even_sum += arr[i]

if odd_sum > even_sum:
    diff = odd_sum - even_sum
else:
    diff = even_sum - odd_sum
print(diff)