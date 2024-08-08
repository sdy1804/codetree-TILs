n = int(input())
arr = list(map(int, input().split()))

# 최대값이 나오는 경우의 수
# 1. 양 * 양 * 양 -> 양수 중 제일 큰 수 3개
# 2. 음 * 음 * 양 -> 음수 중 제일 작은 수, 그 다음 작은 수, 양수 중 제일 큰 수
# 3. 0과 음수뿐일 때 -> 0과 음수 2개
# 4. 수가 단 3개일 때 -> 모두 곱한 값
# 5. 음수만 있을 때 -> 그 중에서 제일 작은 수들로만

def three_pos(lst):
    first_big, scd_big, trd_big = 0, 0, 0
    for i in range(len(lst)):
        first_big = max(first_big, lst[i])
        if first_big == lst[i]:
            first_big_idx = i
    for i in range(len(lst)):
        if lst[i] <= first_big and i != first_big_idx:
            scd_big = max(scd_big, lst[i])
            if scd_big == lst[i]:
                scd_big_idx = i
    for i in range(len(lst)):
        if lst[i] <= scd_big and i != first_big_idx and i != scd_big_idx:
            trd_big = max(trd_big, lst[i])
    return first_big * scd_big * trd_big

def two_neg_one_pos(lst):
    first_neg, scd_neg, pos = 0, 0, 0
    for i in range(len(lst)):
        first_neg = min(first_neg, lst[i])
        if first_neg == lst[i]:
            first_neg_idx = i
    for i in range(len(lst)):
        if lst[i] >= first_neg and first_neg_idx != i :
            scd_neg = min(scd_neg, lst[i])
    for i in range(len(lst)):
            pos = max(pos, lst[i])
    return first_neg * scd_neg * pos

def only_neg_and_zero(lst):
    return 0

def only_neg(lst):
    first_neg, second_neg, third_neg = -10000, -10000, -10000
    for i in range(len(lst)):
        first_neg = max(first_neg, lst[i])
        if first_neg == lst[i]:
            first_neg_idx = i
    for i in range(len(lst)):
        if lst[i] <= first_neg and i != first_neg_idx:
            second_neg = max(second_neg, lst[i])
            if second_neg == lst[i]:
                second_neg_idx = i
    for i in range(len(lst)):
        if lst[i] <= second_neg and i != first_neg_idx and i != second_neg_idx:
            third_neg = max(third_neg, lst[i])
    return first_neg * second_neg * third_neg

def only_three_num(lst):
    return lst[0] * lst[1] * lst[2]

no_pos = False
for idx in range(n):
    if arr[idx] <= 0:
        no_pos = True
    else:
        no_pos = False
        break
    if 0 not in arr:
        no_pos = False

no_pos_and_zero = False
for idx in range(n):
    if arr[idx] < 0:
        no_pos_and_zero = True
    else:
        no_pos_and_zero = False
        break
# print(no_pos, no_pos_and_zero)
if no_pos == True:
    print(only_neg_and_zero(arr))
elif no_pos_and_zero == True:
    print(only_neg(arr))
elif len(arr) == 3:
    print(only_three_num(arr))
else:
    print(max(three_pos(arr), two_neg_one_pos(arr)))