m1 , d1, m2, d2 = map(int, input().split())

# 전, 후로 요일이 바뀌게 될듯 함. 
# 1일 전 - 일, 2 - 토, 3- 금, 4 - 목, 5 - 수, 6 - 화, 7 - 월
# 1일 후 - 화, 2 - 수, 3 - 목, 4 - 금, 5 - 토, 6 -일 , 7 - 월
# 즉, 7일 전 또는 후면 월요일 돌아옴.
# 날짜 계산 후에 7로 나머지 연산하면 알 수 있을듯 함.

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def count_day(month, date):
    elapsed_date = 0
    for i in range(month):
        elapsed_date += days[i]
    elapsed_date += date

    return elapsed_date

date_diff = (count_day(m1, d1) - count_day(m2,d2))
if date_diff >= 0: # 월요일인 날이 후인 경우 (더 늦은 날)
    if date_diff % 7 == 1:
        print('Sun')
    elif date_diff % 7 == 2:
        print("Sat")
    elif date_diff % 7 == 3:
        print("Fri")
    elif date_diff % 7 == 4:
        print("Thu")
    elif date_diff % 7 == 5:
        print("Wed")
    elif date_diff % 7 == 6:
        print("Tue")
    elif date_diff % 7 == 0:
        print("Mon")
else: # 월요일인 날이 전인 경우 (더 빠른 날)
    if -date_diff % 7 == 1:
        print('Tue')
    elif -date_diff % 7 == 2:
        print("Wed")
    elif -date_diff % 7 == 3:
        print("Thu")
    elif -date_diff % 7 == 4:
        print("Fri")
    elif -date_diff % 7 == 5:
        print("Sat")
    elif -date_diff % 7 == 6:
        print("Sun")
    elif -date_diff % 7 == 0:
        print("Mon")