n = int(input())
arr = list(map(int, input().split()))
min_val = 99

for i in range(n):
    for j in range(i+1, n):
        diff = arr[j] - arr[i]

        if diff < min_val:
            min_val = diff
print(min_val)