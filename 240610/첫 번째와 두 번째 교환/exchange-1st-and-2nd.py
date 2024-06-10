string = list(input())
first = string[0]
second = string[1]

for i in range(len(string)):
    if first == string[i]:
        string[i] = second
    elif second == string[i]:
        string[i] = first

for elem in string:
    print(elem, end="")