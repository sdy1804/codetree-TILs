n = int(input())
alpha_A =  ord('A')

for i in range(n):
    for j in range(n):
        print(chr(alpha_A), end='')
        alpha_A += 1
    print()