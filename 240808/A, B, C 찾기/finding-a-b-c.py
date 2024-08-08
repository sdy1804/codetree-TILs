arr = list(map(int, input().split()))

all_sum = max(arr)

arr.sort()
A, B = arr[0], arr[1]
C = all_sum - A - B 
print(A, B, C)