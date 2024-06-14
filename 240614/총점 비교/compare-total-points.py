class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
arr = []
for _ in range(n):
    name, kor, eng, math = input().split()
    arr.append(Student(name, int(kor), int(eng), int(math)))

arr.sort(key=lambda x : x.kor + x.eng + x.math)

for student in arr:
    print(student.name, student.kor, student.eng, student.math)