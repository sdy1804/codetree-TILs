N = int(input())
arr = list(map(int, input().split()))

# 최대한 적게 묶는게 좋겠지만, 아무래도 일단 모든 수를 쓰는게 중요
# 짝수끼리는 아무리 더해도 홀수를 만들 수 없다라는 점과 홀수는 짝수를 만들 수 있다는 점 활용
# 남은 숫자들의 묶음 처리가 중요

even = 0
odd = 0
for nums in arr:
    if nums % 2 == 0:
        even += 1
    else:
        odd += 1
# print(even, odd)

group_num = 0
while True:
    if group_num % 2 == 0:  # 짝수 묶음 만들 차례
        if even:
            even -= 1
            group_num += 1
        elif odd >= 2:
            odd -= 2
            group_num += 1
        else: # 짝수 묶음을 더 이상 만들 수 없는 경우
            if even > 0 or odd > 0: # 남은 숫자들이 있을 때
                group_num -= 1  # 그룹 수를 줄이는 것이 최선
            break
    
    else:
        if odd:
            odd -= 1
            group_num += 1
        else: # 홀수 묶음을 더 이상 만들 수 없는 경우
            break # 그룹 수를 그대로 유지하는 것이 최선
print(group_num)