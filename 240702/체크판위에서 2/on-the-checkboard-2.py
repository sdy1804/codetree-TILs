R, C = map(int, input().split())
arr = [list(input().split()) for _ in range(R)]

start_str = arr[0][0]
cnt = 0
total_case = 0
for i in range(1, R - 2):
    for j in range(1, C - 2):
        if start_str == 'W':
            if arr[i][j] == 'B':
                for k in range(i + 1, R - 1):
                    for l in range(j + 1, C - 1):
                        if arr[k][l] == 'W' and arr[R - 1][C - 1] == 'B':
                            total_case += 1
        else:
            if arr[i][j] == 'W':
                for k in range(i + 1, R - 1):
                    for l in range(j + 1, C - 1):
                        if arr[k][l] == 'B' and arr[R - 1][C - 1] == 'W':
                            total_case += 1                    
print(total_case)