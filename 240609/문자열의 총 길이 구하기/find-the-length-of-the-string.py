arr = input().split()
len_sum = 0

for i in range(len(arr)):
    len_sum += len(arr[i])
print(len_sum)