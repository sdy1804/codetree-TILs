n = int(input())
arr = list(map(int, input().split()))

def MergeSort(lst, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(lst, low, mid)
        MergeSort(lst, mid+1, high)
        Merge(lst, low, mid, high)

def Merge(lst, low, mid, high):
    i, j = low, mid+1
    idx = low
    merge_lst = [0 for _ in range(n)]
    
    while i <= mid and j <= high:
        if lst[i] < lst[j]:
            merge_lst[idx] = lst[i]
            idx += 1
            i += 1
        else:
            merge_lst[idx] = lst[j]
            idx += 1
            j += 1

    while i <= mid:
        merge_lst[idx] = lst[i]
        idx += 1
        i += 1
    
    while j <= high:
        merge_lst[idx] = lst[j]
        idx += 1   
        j += 1
    # print('merge_lst', merge_lst)
    for index in range(low, high+1):
        lst[index] = merge_lst[index]
    # print('lst', lst)
    return lst

MergeSort(arr, 0, n-1)
for elem in arr:
    print(elem, end=" ")