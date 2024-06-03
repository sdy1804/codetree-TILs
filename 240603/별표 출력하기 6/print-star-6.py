n = int(input())

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range((2*n)-(2*i)-1):
        print("*", end=" ")
    print()

for i in range(n-1):
    for j in range(n-i-2):
        print(" ", end=" ")
    for k in range(3+(2*i)):
        print("*", end=" ")
    print()