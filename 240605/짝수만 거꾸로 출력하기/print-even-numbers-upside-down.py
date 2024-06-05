n = int(input())
arr = list(map(int, input().split()))
reverse = arr[::-1]
even_arr = []

for i in range(len(reverse)):
    if reverse[i] % 2 == 0:
        print(reverse[i], end=" ")