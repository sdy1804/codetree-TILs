n = int(input())
arr = list(map(int, input().split()))

arr = arr[arr.index(min(arr)):]
# print(arr)
if arr[1:] == []:
    print(0)
else:
    max_val = max(arr)
    print(max_val - arr[0])