def SelectionSort(lst):
    for i in range(len(lst)-1):
        minimum_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minimum_idx]:
                minimum_idx = j
        temp = lst[i]
        lst[i] = lst[minimum_idx]
        lst[minimum_idx] = temp

n = int(input())
arr = list(map(int, input().split()))
SelectionSort(arr)

for elem in arr:
    print(elem, end=" ")