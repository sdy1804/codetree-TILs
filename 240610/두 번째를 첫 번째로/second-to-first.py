string = list(input())
first = string[0]
second = string[1]

for elem in string:
    if elem == second:
        elem = first
    print(elem, end="")