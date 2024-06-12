def even_change(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] / 2
            arr[i] = int(arr[i])


N = int(input())
array = list(map(int, input().split()))
even_change(array)

for elem in array:
    print(elem, end=" ")