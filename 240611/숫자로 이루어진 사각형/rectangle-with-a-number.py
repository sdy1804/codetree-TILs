def print_square(n):
    count = 1
    for i in range(n):
        for j in range(n):
            print(count, end=" ")
            if count == 9:
                count = 1
            else:
                count += 1
        print()

N = int(input())
print_square(N)