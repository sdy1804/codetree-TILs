arr_2d = [list(input().split()) for i in range(5)]
start_ascii = ord(arr_2d[0][0]) - 32
# print(chr(start_ascii))
# print(chr(start_ascii + 32))

for i in range(5):
    for j in range(3):
        arr_2d[i][j] = chr(ord(arr_2d[i][j]) - 32)

for i in range(5):
    for j in range(3):
        print(arr_2d[i][j], end=" ")
    print()