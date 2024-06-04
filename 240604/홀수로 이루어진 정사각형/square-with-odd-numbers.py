n = int(input())

for i in range(n):
    for j in range(11, 11+(n*2-1), 2):
        print(j + i*2, end=" ")
    print()