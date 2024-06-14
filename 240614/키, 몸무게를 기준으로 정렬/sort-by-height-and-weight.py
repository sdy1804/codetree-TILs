class Person:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight =weight

n = int(input())
arr = []
for _ in range(n):
    name, tall, weight = input().split()
    arr.append(Person(name, int(tall), int(weight)))

arr.sort(key=lambda x:(x.tall, -x.weight))

for std in arr:
    print(std.name, std.tall, std.weight)