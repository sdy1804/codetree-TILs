arr = list(map(int, input().split()))
reverse = arr[::-1]
even_sum = 0
even_cnt = 0

for i in range(len(reverse)):
    if reverse[i] == 0:
        reverse = reverse[i+1:]
        break

for elem in reverse:
    if elem % 2 == 0:
        even_sum += elem
        even_cnt += 1
print(even_cnt, even_sum)