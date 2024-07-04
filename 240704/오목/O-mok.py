arr = [list(map(int,input().split())) for _ in range(19)]

# 가로, 세로, 대각선으로 1 또는 2가 5개로 나오는지 체크

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i][j+2] == 1 and arr[i][j+3] == 1 and arr[i][j+4] == 1:
            print(1)
            print(i+1, j+2+1)
        elif arr[i][j] == 2 and arr[i][j+1] == 2 and arr[i][j+2] == 2 and arr[i][j+3] == 2 and arr[i][j+4] == 2:
            print(2)
            print(i+1, j+2+1)

        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i+2][j] == 1 and arr[i+3][j] == 1 and arr[i+4][j] == 1:
            print(1)
            print(i+2+1, j+1)
        elif arr[i][j] == 2 and arr[i+1][j] == 2 and arr[i+2][j] == 2 and arr[i+3][j] == 2 and arr[i+4][j] == 2:
            print(2)
            print(i+2+1, j+1)
        
        if arr[i][j] == 1 and arr[i+1][j+1] == 1 and arr[i+2][j+2] == 1 and arr[i+3][j+3] == 1 and arr[i+4][j+4] == 1:
            print(1)
            print(i+2+1, j+2+1)
        elif arr[i][j] == 2 and arr[i+1][j+1] == 2 and arr[i+2][j+2] == 2 and arr[i+3][j+3] == 2 and arr[i+4][j+4] == 2:
            print(2)
            print(i+2+1, j+2+1)