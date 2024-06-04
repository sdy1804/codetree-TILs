n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(i):
            print("*", end=" ")
        print()
    else:
        for k in range(1):
            print("*", end=" ")
        print()