n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
start_num = 1

for i in range(n-1, -1, -1):
    if n % 2 == 0:
        if i == n-1: # 3
            for j in range(n-1, -1, -1): # 3, 2, 1, 0
                arr[j][i] = start_num
                start_num += 1
        elif i % 2 != 0: # 1
            start_num = arr[n-1][i+1] + 1
            for j in range(n-1, -1, -1):
                arr[j][i] = start_num
                start_num += 1
        else: # 2
            start_num = arr[0][i+1] + 1 
            for j in range(n):
                arr[j][i] = start_num
                start_num += 1
    else:
        if i == n-1: # 4
            for j in range(n-1, -1, -1): # 4, 3, 2, 1, 0
                arr[j][i] = start_num
                start_num += 1
        elif i % 2 == 0:
            start_num = arr[n-1][i+1] + 1
            for j in range(n-1, -1, -1):
                arr[j][i] = start_num
                start_num += 1
        else: # 3
            start_num = arr[0][i+1] + 1 
            for j in range(n):  
                arr[j][i] = start_num
                start_num += 1

for column in arr:
    for row in column:
        print(row, end=" ")
    print()