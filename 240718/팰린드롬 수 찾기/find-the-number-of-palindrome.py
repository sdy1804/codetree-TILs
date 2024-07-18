X, Y = map(int, input().split())

cnt = 0
for i in range(X, Y+1):
    i = str(i)
    num_list = []
    for j in range(len(i)):
        num_list.append(i[j])
    # print(num_list)
    # print(num_list[::-1])
    if num_list == num_list[::-1]:
        cnt += 1
print(cnt)