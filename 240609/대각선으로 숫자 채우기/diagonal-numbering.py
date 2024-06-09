n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
start_num, cnt = 1, 0

while arr[-1][-1] == 0: # array의 마지막 요소가 0이 아닐 때까지(0을 다 채울때까지)
    for i in range(cnt+1): # 1, 2, 3
        try:
            arr[i][cnt-i] = start_num # arr[0][0], arr[0][1] arr[1][0], arr[0][3] arr[1][2] arr[2][1] arr[3][0]..arr[0][5] arr[1][4]..arr[1][5] arr[2][4] arr[3][3]
            start_num += 1 # 2
        except:
            continue # arr[0][6], arr[0][7] arr[1][6]...
    cnt += 1

for column in arr:
    for row in column:
        print(row, end=" ")
    print()