n = int(input())
arr = list(map(int, input().split()))
merge_lst = [0] * n

def MergeSort(low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(low, mid)
        MergeSort(mid+1, high)
        Merge(low, mid, high)

def Merge(low, mid, high):
    i, j = low, mid+1
    idx = low
    
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            merge_lst[idx] = arr[i]
            idx += 1
            i += 1
        else:
            merge_lst[idx] = arr[j]
            idx += 1
            j += 1

    while i <= mid:
        merge_lst[idx] = arr[i]
        idx += 1
        i += 1

    while j <= high:
        merge_lst[idx] = arr[j]
        idx += 1
        j += 1

    for index in range(low, high+1):
        arr[index] = merge_lst[index]


MergeSort(0, n-1)
for elem in arr:
    print(elem, end=" ")