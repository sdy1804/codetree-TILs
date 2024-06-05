n = int(input())
alpha_A = ord('A')

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n-i):
        print(chr(alpha_A), end=" ")
        if alpha_A == ord('Z'):
            alpha_A = ord('A')
        else:
            alpha_A += 1
    print()