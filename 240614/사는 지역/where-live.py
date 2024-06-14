class Person:
    def __init__(self, name, addr, location):
        self.name = name
        self.addr = addr
        self.location = location

n = int(input())
arr = []
for i in range(n):
    name, addr, location = input().split()
    arr.append(Person(name, addr, location))

name_arr = []
for i in range(len(arr)):
    name_arr.append(arr[i].name)

name_arr.sort()
for i in range(len(arr)):
    if name_arr[-1] == arr[i].name:
        print(f"name {arr[i].name}")
        print(f"addr {arr[i].addr}")
        print(f"city {arr[i].location}")