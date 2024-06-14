class Person:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight =weight

n = int(input())
persons = []
for i in range(n):
    name, tall, weight = input().split()
    persons.append(Person(name, tall, weight))

persons.sort(key=lambda x : x.tall)

for person in persons:
    print(person.name, person.tall, person.weight)