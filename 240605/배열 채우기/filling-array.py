arr = list(map(int, input().split()))
reverse = arr[::-1]

for i in range(len(reverse)):
    if reverse[i] == 0:
        reverse = reverse[i+1:]
        break
for j in reverse:
    print(j, end=" ")