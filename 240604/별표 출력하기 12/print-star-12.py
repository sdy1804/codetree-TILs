n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0:
            print("*", end=" ")
        elif i % 2 != 0:
            if j % 2 != 0 and j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i % 2 == 0:
            if j % 2 != 0 and j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()