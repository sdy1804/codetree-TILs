def RadixSort(lst, k):
    for pos in range(1, k+1):
        arr_new = [[] * col for col in range(10)]
        # print(arr_new)
        # print('pos', pos)
        for i in range(len(lst)):
            if pos == 1:
                digit = lst[i] % 10
            elif pos == 2:
                digit = lst[i] // 10
            elif pos == 3:
                digit = lst[i] // 100
            elif pos == 4:
                digit = lst[i] // 1000
            elif pos == 5:
                digit = lst[i] // 10000
            else:
                digit = lst[i] // 100000
            # print(digit)
            arr_new[digit].append(lst[i])
        
        store_arr = []
        for i in range(10):
            for j in range(len(arr_new[i])):
                store_arr.append(arr_new[i][j])
        # print(store_arr)
        lst = store_arr
    return lst
        

n = int(input())
arr = list(map(int, input().split()))

if max(arr) // 100000 > 0:
    k = 6
elif max(arr) // 10000 > 0:
    k = 5
elif max(arr) // 1000 > 0:
    k = 4
elif max(arr) // 100 > 0:
    k = 3
elif max(arr) // 10 > 0:
    k = 2
else:
    k = 1
arr = RadixSort(arr, k)

for elem in arr:
    print(elem, end= " ")