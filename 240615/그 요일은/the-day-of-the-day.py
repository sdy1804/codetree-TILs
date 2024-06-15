m1, d1, m2, d2 = map(int, input().split())
A = input()

# 기준일에서 0일 지나면 - 월, 1 - 화, 2 - 수, 3 - 목, 4 - 금, 5 - 토, 6 - 일, 7 - 월
# 즉, 각 지난 일수를 계산하여 뺐을 때의 값을 기준으로 며칠 차이인지 구함
# Ex) 1일 -> 월 1번 화 1 나머지 0, 2일 -> 월 1 화 1 수 1 나머지 0, 7일 -> 월 2번 나머지 1번, 8일 -> 월 2 화 2 나머지 1
# 7로 나머지 연산 했을때, 0 - 월, 1 - 화, 2 - 수, ... 6 - 일, 7 - 월 순으로 횟수 증가
# Ex) 15일 -> 몫 2 나머지 1 = 모든 요일 횟수 2번, 월 화 1씩 더 증가

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def count_date(month, date):
    elapsed_date = 0
    for i in range(month):
        elapsed_date += days[month]
    elapsed_date += date
    return elapsed_date

date_diff = count_date(m2, d2) - count_date(m1, d1)
cnt = date_diff // 7
# print(cnt)
day_cnt = date_diff % 7
# print(day_cnt)
# day_cnt % 7 == 0일 때 -> 월이면 + 1, 아니면 cnt
# day_cnt & 7 == 1일 때 -> 월, 화면 +1, 아니면 cnt ...
total_cnt = 0
if day_cnt == 0:
    if A == 'Mon':
        total_cnt = cnt + 1
    else:
        total_cnt = cnt
elif day_cnt == 1:
    if A == 'Mon' or A == 'Tue':
        total_cnt = cnt + 1
    else:
        total_cnt = cnt
elif day_cnt == 2:
    if A == 'Mon' or A == 'Tue' or A =='Wed':
        total_cnt = cnt + 1
    else:
        total_cnt = cnt
elif day_cnt == 3:
    if A == 'Mon' or A == 'Tue' or A == 'Wed' or A == "Thu":
        total_cnt = cnt + 1
    else:
        total_cnt = cnt
elif day_cnt == 4:
    if A == 'Mon' or A =='Tue' or A =='Wed' or A == 'Thu' or A == 'Fri':
        total_cnt = cnt + 1
    else:
        total_cnt = cnt
elif day_cnt == 5:
    if A == 'Mon' or A == 'Tue' or A == 'Wed' or A == 'Thu' or A == 'Fri' or A == 'Sat':
        total_cnt = cnt + 1
    else:
        total_cnt = cnt  
elif day_cnt == 6:
        total_cnt = cnt              
print(total_cnt)