class Person:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

arr = []
for _ in range(5):
    name, tall, weight = input().split()
    arr.append(Person(name, int(tall), float(weight)))

arr.sort(key=lambda x: x.name)
print('name')
for std in arr:
    print(std.name, std.tall, std.weight)
print()

arr.sort(key=lambda x:-x.tall)
print('height')
for std in arr:
    print(std.name, std.tall, std.weight)
print()