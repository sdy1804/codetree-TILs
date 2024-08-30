def partition(lst, low, high):
    pivot = lst[high]
    blue = low - 1
    # print('pivot', pivot)
    for red in range(low, high):
        # if blue == -1 and lst[red] < pivot:
        #     blue += 1
        if lst[red] < pivot:
            blue += 1
            # print('blue, red', blue, red)
            # print('lst[blue], lst[red]', lst[blue], lst[red])
            lst[blue], lst[red] = lst[red], lst[blue]
            # print('switch lst', lst)
    lst[blue+1], lst[high] = lst[high], lst[blue+1]
    # print('reach pivot', lst)
    return blue+1

def QuickSort(lst, low, high):
    if low < high:
        pos = partition(lst, low, high)
    
        QuickSort(lst, low, pos-1)
        QuickSort(lst, pos+1, high)

n = int(input())
lst = list(map(int, input().split()))
QuickSort(lst, 0, n-1)

for elem in lst:
    print(elem, end=" ")