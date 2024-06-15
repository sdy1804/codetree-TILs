class Student:
    def __init__(self, tall, weight, num=0):
        self.tall = tall
        self.weight = weight
        self.num = num

N = int(input())
arr = []
for i in range(1, N+1):
    tall, weight = map(int, input().split())
    arr.append(Student(tall, weight, i))

arr.sort(key=lambda x:(x.tall, -x.weight))

for std in arr:
    print(std.tall, std.weight, std.num)