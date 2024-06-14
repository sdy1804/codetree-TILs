class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
arr= []
for _ in range(n):
    date, day, weather = input().split()
    arr.append(Data(date, day, weather))

rain_arr = []
for i in range(len(arr)):
    if arr[i].weather == 'Rain':
        rain_arr.append(arr[i])

for idx, data in enumerate(rain_arr):
    index = 0
    if data.date < rain_arr[index].date:
        index = idx

print(rain_arr[index].date, rain_arr[index].day, rain_arr[index].weather)