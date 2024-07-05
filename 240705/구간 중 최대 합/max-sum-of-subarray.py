n, k = map(int, input().split())
arr = list(map(int, input().split()))

total_max = 0
for i in range(n - k + 1):
    val_sum = 0
    for j in range(i, i + k):
        val_sum += arr[j]
        total_max = max(val_sum, total_max)
print(total_max)