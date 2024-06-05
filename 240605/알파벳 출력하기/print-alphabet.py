n = int(input())
alpha_A = ord('A')

for i in range(1, n+1):
    for j in range(i):
        print(chr(alpha_A), end="")
        if alpha_A == ord('Z'):
            alpha_A = ord('A')
        else:
            alpha_A += 1
    print()