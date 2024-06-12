def absolute_val(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = -arr[i]

N = int(input())
array = list(map(int, input().split()))
absolute_val(array)

for elem in array:
    print(elem, end=" ")