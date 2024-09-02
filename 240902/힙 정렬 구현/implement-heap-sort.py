def heapify(lst, n, i):
    largest = i
    l = i * 2
    r = i * 2 + 1

    if l <= n and lst[l] > lst[largest]:
        largest = l
    
    if r <= n and lst[r] > lst[largest]:
        largest = r
    
    if largest != i:
        lst[largest], lst[i] = lst[i], lst[largest]
        heapify(lst, n, largest)

def HeapSort(lst, n):
    for i in range(n//2, 0, -1):
        heapify(lst, n, i)
    
    for j in range(n, 0, -1):
        lst[1], lst[j] = lst[j], lst[1]
        heapify(lst, j-1, 1)

n = int(input())
arr = list(map(int, input().split()))

heap_list = [0]
for i in range(len(arr)):
    heap_list.append(arr[i])
# print(heap_list)

HeapSort(heap_list, n)

heap_list.pop(0)
for elem in heap_list:
    print(elem, end=" ")