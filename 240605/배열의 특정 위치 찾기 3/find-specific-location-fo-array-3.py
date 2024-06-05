arr = list(map(int,input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i+1]
        break
# print(arr[-4:-1])
print(sum(arr[-4:-1]))