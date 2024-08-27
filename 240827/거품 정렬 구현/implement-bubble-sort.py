def BubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

n = int(input())
arr = list(map(int, input().split()))
BubbleSort(arr)

for elem in arr:
    print(elem, end=" ")