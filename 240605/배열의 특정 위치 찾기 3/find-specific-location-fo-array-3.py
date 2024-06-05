arr = list(map(int,input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break
print(sum(arr))