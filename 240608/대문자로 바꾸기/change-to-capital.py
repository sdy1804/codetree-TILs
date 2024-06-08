arr_2d = [list(input().split()) for i in range(5)]
A_ascii = 65

for i in range(5):
    for j in range(3):
        arr_2d[i][j] = chr(A_ascii)
        A_ascii += 1

for i in range(5):
    for j in range(3):
        print(arr_2d[i][j], end=" ")
    print()