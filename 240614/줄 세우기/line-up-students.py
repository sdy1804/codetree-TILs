class Student:
    def __init__(self, tall, weight, num=0):
        self.tall = tall
        self.weight = weight
        self.num = num

N = int(input())
arr = []
for _ in range(N):
    tall, weight = map(int, input().split())
    arr.append(Student(tall, weight))

for idx, std in enumerate(arr, start=1):
    std.num = idx

arr.sort(key=lambda x : (-x.tall, -x.weight, x.num))

for student in arr:
    print(student.tall, student.weight, student.num)