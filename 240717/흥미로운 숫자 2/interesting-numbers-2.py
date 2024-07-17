X, Y = map(int, input().split())

# 특정 숫자의 종류가 2개이며, 둘 중 하나는 갯수가 1이여야 함
# 임시 리스트에 붙여넣으면서 확인 가능할지도
# 각 자릿수마다 리스트에 없으면 넣고, 아니면 넣지 않기
# 수 가짓수 확인후 2개라면, 각 수의 카운트를 셈
# 수의 카운트를 세서 둘 중 하나가 1이고 나머지 하나는 전체 길이의 -1이면 cnt 증가

cnt = 0
for i in range(X, Y+1):
    i = str(i)
    lst = []
    for j in range(len(i)):
        if i[j] not in lst:
            lst.append(i[j])
    if len(lst) == 2:
        if (i.count(lst[0]) == 1 and i.count(lst[1]) == len(i) - 1) or (i.count(lst[0]) == len(i) - 1 and i.count(lst[1]) == 1):
            cnt += 1
print(cnt)