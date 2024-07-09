N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

cnt = 0
first = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if ((abs(i - arr1[0]) <= 2) or (arr1[0] == 1 and i == 10) or (arr1[0] == 1 and i == 9) or (arr1[0] == 2 and i == 10))\
            and ((abs(j - arr1[1]) <= 2) or (arr1[1] == 1 and j == 10) or (arr1[1] == 1 and j == 9) or (arr1[1] == 2 and j == 10)) \
            and ((abs(k - arr1[2]) <= 2) or (arr1[2] == 1 and k == 10) or (arr1[2] == 1 and k == 9) or (arr1[2] == 2 and k == 10)):
                # print('i',i, j, k)
                first.append([i, j, k])
                cnt += 1
# print(cnt)

second = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if ((abs(i - arr2[0]) <= 2) or (arr2[0] == 1 and i == 10) or (arr2[0] == 1 and i == 9) or (arr2[0] == 2 and i == 10))\
            and ((abs(j - arr2[1]) <= 2) or (arr2[1] == 1 and j == 10) or (arr2[1] == 1 and j == 9) or (arr2[1] == 2 and j == 10)) \
            and ((abs(k - arr2[2]) <= 2) or (arr2[2] == 1 and k == 10) or (arr2[2] == 1 and k == 9) or (arr2[2] == 2 and k == 10)):
                # print('i',i, j, k)
                second.append([i, j, k])
                cnt += 1
# print(cnt)

for i in range(len(first)):
    if first[i] in second:
        cnt -= 1
print(cnt)