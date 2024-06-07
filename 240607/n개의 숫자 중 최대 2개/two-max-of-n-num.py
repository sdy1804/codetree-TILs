n = int(input())
arr = list(map(int, input().split()))

for k in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr[0], arr[1])