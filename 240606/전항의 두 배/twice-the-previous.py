first, second = map(int, input().split())
arr = []
arr.append(first)
arr.append(second)

for i in range(2,10):
    arr.append(arr[i-1]+2*arr[i-2])

for j in arr:
    print(j, end=" ")